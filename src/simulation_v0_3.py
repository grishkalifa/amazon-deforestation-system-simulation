import os
from typing import Dict, List, Optional, Set, Tuple
import matplotlib.pyplot as plt

F0_TOTAL = 39_011_117
F0_INTACT = F0_TOTAL
F0_DEGRADED = 0

START_YEAR = 2000
HORIZON_YEARS = 200

D_BASE = 81_240
POST_ACCORD_START = 2017
POST_ACCORD_MULT = 0.30

FIRE_BASE = 20_000
ELNINO_YEARS: Set[int] = {2015, 2016, 2023, 2024}
ELNINO_MULT = 0.20

RHO_RECOVERY = 0.01

# IMPORTANT CHANGE: don't prioritize degraded too much, or it never accumulates
W_DEGRADED_TARGET = 0.20  # was 0.70

THRESHOLDS = {
    "20% loss (80% remaining)": 0.80,
    "25% loss (75% remaining)": 0.75,
}

def first_crossing_year(years: List[int], series: List[float], threshold_value: float) -> Optional[int]:
    for y, v in zip(years, series):
        if v <= threshold_value:
            return y
    return None

def simulate_v03(
    start_year: int,
    horizon: int,
    F0_intact: float,
    F0_degraded: float,
    post_accord_on: bool,
    climate_stress: float,
    enforcement_factor: float,
    alpha_vuln: float,
) -> Tuple[List[int], List[float], List[float], List[float]]:

    years = [start_year + t for t in range(horizon + 1)]
    intact = [float(F0_intact)]
    degraded = [float(F0_degraded)]
    total = [float(F0_intact + F0_degraded)]

    for t in range(horizon):
        y = years[t]
        F_int = intact[-1]
        F_deg = degraded[-1]
        F_tot = max(F_int + F_deg, 1.0)

        # Human conversion
        post_mult = POST_ACCORD_MULT if (post_accord_on and y >= POST_ACCORD_START) else 0.0
        D_human = (D_BASE * enforcement_factor) * (1.0 + post_mult)

        # Allocate conversion pressure: small preference to degraded (but not enough to erase it)
        convert_deg = min(F_deg, D_human * W_DEGRADED_TARGET)
        remaining = D_human - convert_deg
        convert_int = min(F_int, max(remaining, 0.0))

        # Fire-driven degradation (reinforcing)
        deg_share = F_deg / F_tot
        vuln_factor = 1.0 + alpha_vuln * deg_share

        eln = ELNINO_MULT if y in ELNINO_YEARS else 0.0
        fire_pressure = (FIRE_BASE * climate_stress) * vuln_factor * (1.0 + eln)

        degrade = min(F_int - convert_int, max(fire_pressure, 0.0))
        degrade = max(degrade, 0.0)

        # Recovery (balancing)
        recover = min(F_deg - convert_deg, RHO_RECOVERY * F_deg)
        recover = max(recover, 0.0)

        next_int = F_int - convert_int - degrade + recover
        next_deg = F_deg - convert_deg + degrade - recover

        intact.append(max(next_int, 0.0))
        degraded.append(max(next_deg, 0.0))
        total.append(max(next_int + next_deg, 0.0))

    return years, intact, degraded, total

def main() -> None:
    scenarios = [
        ("Base (post-accord ON, baseline climate)", True, 1.0, 1.0, 2.0),
        ("Alt 1: Enforcement (lower human conversion)", True, 1.0, 0.7, 2.0),
        ("Alt 2: Climate stress (higher fires + stronger feedback)", True, 1.7, 1.0, 4.0),
    ]

    results: Dict[str, Tuple[List[int], List[float], List[float], List[float]]] = {}

    for name, post_on, climate_stress, enforcement, alpha in scenarios:
        years, intact, degraded, total = simulate_v03(
            start_year=START_YEAR,
            horizon=HORIZON_YEARS,
            F0_intact=F0_INTACT,
            F0_degraded=F0_DEGRADED,
            post_accord_on=post_on,
            climate_stress=climate_stress,
            enforcement_factor=enforcement,
            alpha_vuln=alpha,
        )
        results[name] = (years, intact, degraded, total)

    print("\n=== Threshold Crossing Years (V0.3, total forest remaining) ===")
    for name, *_ in scenarios:
        years, _, _, total = results[name]
        print(f"\nScenario: {name}")
        for label, frac in THRESHOLDS.items():
            thr = frac * F0_TOTAL
            y_cross = first_crossing_year(years, total, thr)
            print(f"  {label}: {y_cross if y_cross is not None else 'Not crossed within horizon'}")

    plt.figure(figsize=(11, 5))
    for name, *_ in scenarios:
        years, intact, degraded, _ = results[name]
        plt.plot(years, intact, linewidth=2, label=f"{name} — intact")
        plt.plot(years, degraded, linewidth=2, linestyle="--", label=f"{name} — degraded")

    plt.title("Colombian Amazon — Intact vs Degraded Forest (V0.3)")
    plt.xlabel("Year")
    plt.ylabel("Area (hectares)")
    plt.grid(True, alpha=0.3)
    plt.legend()

    os.makedirs("outputs", exist_ok=True)
    plt.tight_layout()
    plt.savefig("outputs/forest_intact_degraded_v0_3.png", dpi=200)
    plt.close()

if __name__ == "__main__":
    main()

