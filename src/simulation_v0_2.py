"""
Amazon Deforestation System Simulation — Colombia (V0.2)

V0.2 (channelized shocks) separates deforestation into two components:

1) Human-driven deforestation (D_human):
   - Baseline annual deforestation proxy (D_base)
   - Post-accord regime shift (persistent multiplier from 2017 onward)

2) Fire-driven loss (D_fire):
   - Additive pulse in selected fire years
   - El Niño increases ONLY the fire component (multiplies D_fire), not D_human

Key design choice (to avoid double counting):
- Fire pulses are NOT applied by default in 2017–2018, because post-accord regime
  may already capture part of the same land-use expansion dynamics in those years.

Still simplified:
- Single forest stock (hectares)
- Annual discrete steps
- Regeneration = 0

Outputs:
- PNG saved in /outputs
- Threshold crossing years printed (80% and 75% remaining)
"""

import os
from typing import Dict, List, Optional, Set, Tuple

import matplotlib.pyplot as plt


# -----------------------------
# PARAMETERS (Scenario knobs for V0.2)
# -----------------------------

# Baseline (human-driven) deforestation proxy (ha/year)
D_BASE_HUMAN: float = 81_240

# Forest stock (ha)
F0: int = 39_011_117

# Simulation horizon
START_YEAR: int = 2000
HORIZON_YEARS: int = 200


# -----------------------------
# SHOCKS (Channelized)
# -----------------------------

# Post-accord persistent regime shift on HUMAN component only
POST_ACCORD_START: int = 2017
POST_ACCORD_MULT_HUMAN: float = 0.30   # +30% on D_human from 2017 onward (scenario assumption)

# Fire pulses (additive hectares lost) - NOT applied by default in 2017–2018
FIRE_YEARS: Set[int] = {2019, 2024}    # intentionally excludes 2017–2018 to avoid double count
FIRE_EXTRA_HA: float = 15_000          # additive hectares in fire years (scenario assumption)

# El Niño increases ONLY the fire component
ELNINO_YEARS: Set[int] = {2015, 2016, 2023, 2024}
ELNINO_MULT_FIRE: float = 0.20         # +20% on D_fire in El Niño years (scenario assumption)


# -----------------------------
# THRESHOLDS
# -----------------------------
THRESHOLDS = {
    "20% loss (80% remaining)": 0.80,
    "25% loss (75% remaining)": 0.75,
}


def simulate_channelized(
    start_year: int,
    years_horizon: int,
    F0: int,
    D_base_human: float,
    post_accord_on: bool,
    fires_on: bool,
    elnino_on: bool,
) -> Tuple[List[int], List[float], List[float], List[float]]:
    """
    Returns:
      years: calendar years (len = horizon + 1)
      forest: forest stock each year (len = horizon + 1)
      D_human_series: realized human deforestation each year (len = horizon)
      D_fire_series: realized fire loss each year (len = horizon)
    """
    years = [start_year + t for t in range(years_horizon + 1)]
    forest = [float(F0)]

    D_human_series: List[float] = []
    D_fire_series: List[float] = []

    for t in range(years_horizon):
        y = years[t]

        # --- HUMAN component (post-accord regime shift) ---
        m_post = POST_ACCORD_MULT_HUMAN if (post_accord_on and y >= POST_ACCORD_START) else 0.0
        D_human = D_base_human * (1.0 + m_post)

        # --- FIRE component (pulse + El Niño multiplier ONLY on fires) ---
        D_fire_base = FIRE_EXTRA_HA if (fires_on and y in FIRE_YEARS) else 0.0
        m_eln_fire = ELNINO_MULT_FIRE if (elnino_on and y in ELNINO_YEARS) else 0.0
        D_fire = D_fire_base * (1.0 + m_eln_fire)

        # Total loss this year
        D_total = D_human + D_fire

        next_F = forest[-1] - D_total  # regeneration still 0 in V0.2
        forest.append(max(next_F, 0.0))

        D_human_series.append(D_human)
        D_fire_series.append(D_fire)

    return years, forest, D_human_series, D_fire_series


def first_crossing_year(years: List[int], forest: List[float], threshold_value: float) -> Optional[int]:
    """Returns first year where forest <= threshold_value; None if not crossed within horizon."""
    for y, f in zip(years, forest):
        if f <= threshold_value:
            return y
    return None


def main() -> None:
    scenarios = [
        ("BAU (human only, no shocks)", False, False, False),
        ("Post-accord (human regime shift)", True, False, False),
        ("Post-accord + fires", True, True, False),
        ("Post-accord + fires + El Niño (fires amplified)", True, True, True),
    ]

    results: Dict[str, Tuple[List[int], List[float], List[float], List[float]]] = {}

    for name, post_on, fire_on, eln_on in scenarios:
        years, forest, Dh, Df = simulate_channelized(
            start_year=START_YEAR,
            years_horizon=HORIZON_YEARS,
            F0=F0,
            D_base_human=D_BASE_HUMAN,
            post_accord_on=post_on,
            fires_on=fire_on,
            elnino_on=eln_on,
        )
        results[name] = (years, forest, Dh, Df)

    # -----------------------------
    # Print threshold crossing years
    # -----------------------------
    print("\n=== Threshold Crossing Years (V0.2, channelized shocks, R=0) ===")
    print(f"Post-accord: start={POST_ACCORD_START}, mult_human=+{int(POST_ACCORD_MULT_HUMAN*100)}% (persistent)")
    print(f"Fire years={sorted(list(FIRE_YEARS))}, fire_extra={int(FIRE_EXTRA_HA)} ha (scenario param)")
    print(f"El Niño years={sorted(list(ELNINO_YEARS))}, mult_fire=+{int(ELNINO_MULT_FIRE*100)}% (scenario param)")
    print("Note: Fires are intentionally NOT applied in 2017–2018 to avoid double counting.\n")

    for name, _, _, _ in scenarios:
        years, forest, _, _ = results[name]
        print(f"Scenario: {name}")
        for label, frac in THRESHOLDS.items():
            thr_value = frac * F0
            y_cross = first_crossing_year(years, forest, thr_value)
            if y_cross is None:
                print(f"  {label}: Not crossed within horizon")
            else:
                print(f"  {label}: {y_cross}")
        print("")

    # -----------------------------
    # Plot forest stock
    # -----------------------------
    plt.figure(figsize=(11, 5))

    for name, _, _, _ in scenarios:
        years, forest, _, _ = results[name]
        plt.plot(years, forest, linewidth=2, label=name)

    for label, frac in THRESHOLDS.items():
        thr = frac * F0
        plt.axhline(thr, linestyle="--")
        plt.text(START_YEAR + 1, thr, f"  {label}", va="bottom")

    plt.title("Colombian Amazon — Forest Remaining (V0.2, Channelized Shocks, No Regeneration)")
    plt.xlabel("Year")
    plt.ylabel("Forest remaining (hectares)")
    plt.grid(True, alpha=0.3)
    plt.legend()

    os.makedirs("outputs", exist_ok=True)
    plt.tight_layout()
    plt.savefig("outputs/forest_remaining_v0_2_channelized.png", dpi=200)
    plt.close()


if __name__ == "__main__":
    main()
