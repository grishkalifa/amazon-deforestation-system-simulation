import streamlit as st
import matplotlib.pyplot as plt

from typing import List, Optional, Set, Tuple

# -----------------------------
# Core baseline constants (from your model)
# -----------------------------
F0_TOTAL = 39_011_117
START_YEAR_DEFAULT = 2000
HORIZON_DEFAULT = 200

# El Niño years (can be toggled ON/OFF as a block)
ELNINO_YEARS: Set[int] = {2015, 2016, 2023, 2024}

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
    D_base: float,
    post_accord_on: bool,
    post_accord_start: int,
    post_accord_mult: float,
    enforcement_factor: float,
    fire_base: float,
    climate_stress: float,
    alpha_vuln: float,
    elnino_on: bool,
    elnino_mult: float,
    rho_recovery: float,
    w_degraded_target: float,
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
        post_mult = post_accord_mult if (post_accord_on and y >= post_accord_start) else 0.0
        D_human = (D_base * enforcement_factor) * (1.0 + post_mult)

        # Allocate conversion pressure (small preference to degraded, but not enough to erase it)
        convert_deg = min(F_deg, D_human * w_degraded_target)
        remaining = D_human - convert_deg
        convert_int = min(F_int, max(remaining, 0.0))

        # Fire-driven degradation (reinforcing)
        deg_share = F_deg / F_tot
        vuln_factor = 1.0 + alpha_vuln * deg_share

        eln = elnino_mult if (elnino_on and y in ELNINO_YEARS) else 0.0
        fire_pressure = (fire_base * climate_stress) * vuln_factor * (1.0 + eln)

        degrade = min(F_int - convert_int, max(fire_pressure, 0.0))
        degrade = max(degrade, 0.0)

        # Recovery (balancing)
        recover = min(F_deg - convert_deg, rho_recovery * F_deg)
        recover = max(recover, 0.0)

        next_int = F_int - convert_int - degrade + recover
        next_deg = F_deg - convert_deg + degrade - recover

        intact.append(max(next_int, 0.0))
        degraded.append(max(next_deg, 0.0))
        total.append(max(next_int + next_deg, 0.0))

    return years, intact, degraded, total


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Amazon Forest System Simulator (V0.3)", layout="wide")
st.title("Amazon Forest System Simulator — V0.3 (Intact / Degraded)")

st.markdown(
    """
### What are you seeing?

This dashboard simulates the Colombian Amazon as a **dynamic system**, not as a static forest map.

**Key ideas:**
- Forest loss is not only about how much is cut, but **how vulnerable what remains becomes**.
- Degradation is an early warning signal.
- Small yearly losses accumulate into irreversible outcomes due to feedback loops.

**Units**
- All values are shown in **hectares**.
- Current deforestation levels correspond to **~300 football fields lost per day**.

**Why assumptions?**
This version (V0.3) uses **scenario assumptions**, not calibrated predictions.
The purpose is to explore:
- Direction
- Sensitivity
- Structural risk

Not to claim exact numbers.
"""
)


with st.sidebar:
    st.header("Simulation Settings")

    start_year = st.number_input("Start year", value=START_YEAR_DEFAULT, step=1)
    horizon = st.slider("Horizon (years)", min_value=50, max_value=300, value=HORIZON_DEFAULT, step=10)

    st.divider()
    st.subheader("Human Conversion (Deforestation)")

    D_base = st.number_input("D_base (ha/year)", value=81240, step=1000)
    enforcement = st.slider("Enforcement factor (lower = stronger enforcement)", 0.3, 1.2, 1.0, 0.05)

    post_on = st.checkbox("Post-accord regime shift ON", value=True)
    post_start = st.number_input("Post-accord start year", value=2017, step=1)
    post_mult = st.slider("Post-accord multiplier (+)", 0.0, 1.0, 0.30, 0.05)

    w_deg = st.slider("Conversion targeting degraded (w)", 0.0, 1.0, 0.20, 0.05)

    st.divider()
    st.subheader("Fire → Degradation")

    fire_base = st.number_input("Fire base (ha/year degraded)", value=20000, step=1000)
    climate_stress = st.slider("Climate stress multiplier", 0.5, 3.0, 1.0, 0.1)
    alpha = st.slider("Vulnerability feedback strength (alpha)", 0.0, 8.0, 2.0, 0.2)

    elnino_on = st.checkbox("El Niño amplification ON (predefined years)", value=True)
    elnino_mult = st.slider("El Niño multiplier (+)", 0.0, 1.0, 0.20, 0.05)

    st.divider()
    st.subheader("Recovery (Degraded → Intact)")

    rho = st.slider("Recovery rate (rho per year)", 0.0, 0.10, 0.01, 0.005)

    st.divider()
    st.subheader("Initial Conditions")
    f0_total = st.number_input("Initial total forest (ha)", value=F0_TOTAL, step=100000)
    f0_degraded = st.number_input("Initial degraded forest (ha)", value=0, step=100000)
    f0_degraded = min(f0_degraded, f0_total)
    f0_intact = f0_total - f0_degraded

# Run simulation
years, intact, degraded, total = simulate_v03(
    start_year=int(start_year),
    horizon=int(horizon),
    F0_intact=float(f0_intact),
    F0_degraded=float(f0_degraded),
    D_base=float(D_base),
    post_accord_on=bool(post_on),
    post_accord_start=int(post_start),
    post_accord_mult=float(post_mult),
    enforcement_factor=float(enforcement),
    fire_base=float(fire_base),
    climate_stress=float(climate_stress),
    alpha_vuln=float(alpha),
    elnino_on=bool(elnino_on),
    elnino_mult=float(elnino_mult),
    rho_recovery=float(rho),
    w_degraded_target=float(w_deg),
)

# Derived metrics
deforested = [max(f0_total - t, 0.0) for t in total]
degraded_pct = [(d / max(t, 1.0)) * 100.0 for d, t in zip(degraded, total)]

# Threshold years
thr_80 = first_crossing_year(years, total, 0.80 * f0_total)
thr_75 = first_crossing_year(years, total, 0.75 * f0_total)

col1, col2, col3 = st.columns(3)
col1.metric("80% remaining threshold year", thr_80 if thr_80 else "Not crossed")
col2.metric("75% remaining threshold year", thr_75 if thr_75 else "Not crossed")
col3.metric("Peak degraded (%)", f"{max(degraded_pct):.2f}%")

st.divider()

# Plot 1: Intact + Total
st.subheader("Forest Remaining (Total vs Intact)")
fig1 = plt.figure()
plt.plot(years, total, linewidth=2, label="Total forest (intact + degraded)")
plt.plot(years, intact, linewidth=2, label="Intact forest")
plt.xlabel("Year")
plt.ylabel("Area (hectares)")
plt.grid(True, alpha=0.3)
plt.legend()
st.pyplot(fig1)

# Plot 2: Degraded only + % degraded
st.subheader("Degraded Forest (Leading Indicator)")
c1, c2 = st.columns(2)

with c1:
    fig2 = plt.figure()
    plt.plot(years, degraded, linewidth=2, linestyle="--", label="Degraded forest (ha)")
    plt.xlabel("Year")
    plt.ylabel("Area (hectares)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    st.pyplot(fig2)

with c2:
    fig3 = plt.figure()
    plt.plot(years, degraded_pct, linewidth=2, linestyle="--", label="Degraded (% of total)")
    plt.xlabel("Year")
    plt.ylabel("Percent (%)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    st.pyplot(fig3)

# Plot 3: Deforested derived
st.subheader("Deforested (Derived)")
fig4 = plt.figure()
plt.plot(years, deforested, linewidth=2, label="Deforested (derived) = initial - total remaining")
plt.xlabel("Year")
plt.ylabel("Area (hectares)")
plt.grid(True, alpha=0.3)
plt.legend()
st.pyplot(fig4)

st.divider()
st.markdown(

    """
### How to interpret this responsibly

- If total forest declines slowly but **degraded forest rises fast**, risk is increasing.
- Enforcement policies mainly reduce **human conversion**.
- Climate stress and fires mainly increase **vulnerability**, even if total loss looks similar.
- Waiting for visible collapse means the system is already too unstable to recover.

This is why delayed environmental problems are the hardest to solve.
"""

)
