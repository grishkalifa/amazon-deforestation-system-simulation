"""
Amazon Deforestation System Simulation — Colombia (V0.1)

System dynamics baseline model:
- Single stock: forest cover (hectares)
- Annual discrete time steps
- Deforestation as constant annual flow (two scenarios)
- Regeneration set to zero (worst-case baseline)
- Marks precautionary thresholds at 20% and 25% cumulative loss

Outputs:
- A year-by-year plot of remaining forest
- Printed threshold crossing years for each scenario
"""

from dataclasses import dataclass
import math
from typing import Dict, List, Tuple
import os


import matplotlib.pyplot as plt


@dataclass
class Scenario:
    name: str
    start_year: int
    F0: int            # initial forest (ha)
    D: float           # deforestation rate (ha/year)
    years: int = 150   # simulation horizon


def simulate(s: Scenario) -> Tuple[List[int], List[float]]:
    """Returns (calendar_years, forest_series)."""
    years = [s.start_year + t for t in range(s.years + 1)]
    forest = [float(s.F0)]

    for _ in range(s.years):
        next_F = forest[-1] - s.D  # R_t = 0 in V0.1
        forest.append(max(next_F, 0.0))

    return years, forest


def crossing_year(start_year: int, F0: float, D: float, frac_remaining: float) -> int:
    """
    Returns calendar year when forest first goes <= frac_remaining * F0
    under constant D and R=0.
    """
    threshold = frac_remaining * F0
    # Solve F0 - D*t <= threshold  => t >= (F0 - threshold)/D
    t = math.ceil((F0 - threshold) / D)
    return start_year + max(t, 0)


def main() -> None:
    # --- Core parameters (V0.1) ---
    # Initial forest stock (IDEAM Amazon biome forest cover reference year 2021)
    F0 = 39_011_117

    # Scenario 1: BAU proxy using 2020–2024 avg deforestation (Amazon region)
    D_BAU = 81_240

    # Scenario 2: Post-agreement peak (aggressive) proxy using 2017–2018 avg deforestation
    # (You can update this number if you later compute an exact average from a single dataset.)
    D_POST_PEAK = 141_161  # approx avg of 2017 (144,147) and 2018 (138,176)

    start_year = 2025
    horizon_years = 150

    scenarios = [
        Scenario("BAU (2020–2024 avg)", start_year, F0, D_BAU, horizon_years),
        Scenario("Post-Agreement Peak (2017–2018 avg)", start_year, F0, D_POST_PEAK, horizon_years),
    ]

    # Precautionary thresholds
    thresholds = {
        "20% loss (80% remaining)": 0.80,
        "25% loss (75% remaining)": 0.75,
    }

    # --- Run simulations ---
    results: Dict[str, Tuple[List[int], List[float]]] = {}
    for s in scenarios:
        results[s.name] = simulate(s)

    # --- Print threshold crossing years ---
    print("\n=== Threshold Crossing Years (V0.1, R=0) ===")
    for s in scenarios:
        print(f"\nScenario: {s.name}")
        for label, frac in thresholds.items():
            y = crossing_year(s.start_year, s.F0, s.D, frac)
            print(f"  {label}: {y}")

    # --- Plot ---
    plt.figure(figsize=(11, 5))

    for s in scenarios:
        years, forest = results[s.name]
        plt.plot(years, forest, linewidth=2, label=s.name)

    # Draw threshold lines
    for label, frac in thresholds.items():
        thr = frac * F0
        plt.axhline(thr, linestyle="--")
        plt.text(start_year + 1, thr, f"  {label}", va="bottom")

    plt.title("Colombian Amazon — Forest Remaining Over Time (V0.1, No Regeneration)")
    plt.xlabel("Year")
    plt.ylabel("Forest remaining (hectares)")
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Ensure outputs directory exists
    os.makedirs("outputs", exist_ok=True)

    # Save figure
    plt.tight_layout()
    plt.savefig("outputs/forest_remaining_v0_1.png", dpi=200)

    plt.close()


if __name__ == "__main__":
    main()
