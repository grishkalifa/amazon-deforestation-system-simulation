"""
Amazon Deforestation System Simulation — Colombia (V0.2)

V0.2 introduces *shocks* (time-varying drivers) on top of a simple baseline:
- Post-accord regime shift (multi-year elevated pressure)
- El Niño years (episodic multiplier)
- Fire pulses (additive extra hectares)

Still simplified:
- Single stock: forest cover (hectares)
- Annual discrete time steps
- Regeneration = 0 (kept intentionally simple for interpretability)

Outputs:
- A plot of remaining forest for multiple shock scenarios
- Printed threshold crossing years (80% and 75% remaining) per scenario
- Saved PNG in /outputs
"""

import math
import os
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt


def simulate_with_shocks(
    start_year: int,
    years_horizon: int,
    F0: int,
    D_base: float,
    post_accord_mul: Dict[int, float] | None = None,
    elnino_mul: Dict[int, float] | None = None,
    fire_extra_ha: Dict[int, float] | None = None,
) -> Tuple[List[int], List[float], List[float]]:
    """
    Returns:
      years: list of calendar years (length = years_horizon + 1)
      forest: forest stock each year (length = years_horizon + 1)
      deforestation: realized deforestation each year (length = years_horizon)
    """
    post_accord_mul = post_accord_mul or {}
    elnino_mul = elnino_mul or {}
    fire_extra_ha = fire_extra_ha or {}

    years = [start_year + t for t in range(years_horizon + 1)]
    forest = [float(F0)]
    defo = []

    for t in range(years_horizon):
        y = years[t]

        m_post = post_accord_mul.get(y, 0.0)   # e.g., 0.40 means +40%
        m_eln = elnino_mul.get(y, 0.0)         # e.g., 0.25 means +25%
        extra_fire = fire_extra_ha.get(y, 0.0) # e.g., +20000 ha that year

        D_t = (D_base * (1.0 + m_post) * (1.0 + m_eln)) + extra_fire

        next_F = forest[-1] - D_t  # regeneration still 0 in V0.2
        forest.append(max(next_F, 0.0))
        defo.append(D_t)

    return years, forest, defo


def first_crossing_year(years: List[int], forest: List[float], threshold_value: float) -> int | None:
    """
    Returns the first calendar year where forest <= threshold_value.
    If never crossed, returns None.
    """
    for y, f in zip(years, forest):
        if f <= threshold_value:
            return y
    return None


def main() -> None:
    # -----------------------------
    # Core parameters (kept from V0.1)
    # -----------------------------
    F0 = 39_011_117  # initial forest stock (ha)
    D_BAU = 81_240   # baseline deforestation (ha/year) proxy

    # IMPORTANT: start before 2017 so post-accord shock is visible in simulation
    start_year = 2000
    horizon_years = 200

    # -----------------------------
    # V0.2 SHOCK DEFINITIONS (assumptions)
    # NOTE: In V0.2 these are scenario assumptions; in V0.3 we calibrate to data.
    # -----------------------------
    post_accord = {
        2017: 0.40,
        2018: 0.30,
        2019: 0.25,
        2020: 0.20,
        2021: 0.15,
    }

    elnino = {
        2015: 0.25,
        2016: 0.25,
        2023: 0.20,
        2024: 0.20,
    }

    fires = {
        2019: 20_000,
        2024: 15_000,
    }

    thresholds = {
        "20% loss (80% remaining)": 0.80,
        "25% loss (75% remaining)": 0.75,
    }

    # -----------------------------
    # Scenarios (V0.2)
    # -----------------------------
    scenarios_v02 = [
        ("BAU (no shocks)", D_BAU, {}, {}, {}),
        ("Post-accord shock", D_BAU, post_accord, {}, {}),
        ("Post-accord + El Niño + fires", D_BAU, post_accord, elnino, fires),
    ]

    results_v02: Dict[str, Tuple[List[int], List[float], List[float]]] = {}

    for name, D_base, s_post, s_eln, s_fire in scenarios_v02:
        years, forest, defo = simulate_with_shocks(
            start_year=start_year,
            years_horizon=horizon_years,
            F0=F0,
            D_base=D_base,
            post_accord_mul=s_post,
            elnino_mul=s_eln,
            fire_extra_ha=s_fire,
        )
        results_v02[name] = (years, forest, defo)

    # -----------------------------
    # Print threshold crossing years (V0.2, based on time series)
    # -----------------------------
    print("\n=== Threshold Crossing Years (V0.2, shocks, R=0) ===")
    for name, _, _, _, _ in scenarios_v02:
        years, forest, _ = results_v02[name]
        print(f"\nScenario: {name}")
        for label, frac in thresholds.items():
            thr_value = frac * F0
            y_cross = first_crossing_year(years, forest, thr_value)
            if y_cross is None:
                print(f"  {label}: Not crossed within horizon")
            else:
                print(f"  {label}: {y_cross}")

    # -----------------------------
    # Plot (V0.2)
    # -----------------------------
    plt.figure(figsize=(11, 5))

    for name, _, _, _, _ in scenarios_v02:
        years, forest, _ = results_v02[name]
        plt.plot(years, forest, linewidth=2, label=name)

    for label, frac in thresholds.items():
        thr = frac * F0
        plt.axhline(thr, linestyle="--")
        plt.text(start_year + 1, thr, f"  {label}", va="bottom")

    plt.title("Colombian Amazon — Forest Remaining Over Time (V0.2, Shocks, No Regeneration)")
    plt.xlabel("Year")
    plt.ylabel("Forest remaining (hectares)")
    plt.grid(True, alpha=0.3)
    plt.legend()

    os.makedirs("outputs", exist_ok=True)
    plt.tight_layout()
    plt.savefig("outputs/forest_remaining_v0_2_shocks.png", dpi=200)
    plt.close()


if __name__ == "__main__":
    main()
