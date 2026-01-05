# Amazon Deforestation System Simulation (V0.3)

This project models the Colombian Amazon as a **dynamic system**, using a
**system dynamics approach** (stocks, flows, feedback loops).

Rather than producing precise forecasts, the goal is to understand
**structural risks, tipping points, and long-term trajectories** under
different deforestation regimes.

---

## Purpose

Environmental collapse is often a **delayed-feedback problem**:
damage accumulates quietly, while consequences appear suddenly.

This project explores:
- Why deforestation can look “manageable” until it is too late
- How degradation acts as a leading indicator of collapse
- Why post-2016 deforestation represents a structural regime shift
- How climate stress and fires amplify vulnerability over time

---

##  Modeling Approach

**Core concepts**
- System dynamics (stocks & flows)
- Reinforcing and balancing feedback loops
- Threshold behavior (80% / 75% remaining forest)
- Scenario comparison

**Key stocks**
- Intact forest (resilient)
- Degraded forest (vulnerable)

**Key flows**
- Human-driven land conversion (deforestation)
- Fire-driven degradation
- Natural recovery (simplified)

This separation allows degradation to be treated as an **early warning signal**,
not just an intermediate accounting step.

---

##  Versions

### V0.1 — Baseline
- Single stock (total forest)
- Constant deforestation rates
- No regeneration
- Structural baseline

### V0.2 — Shocks
- Post-peace-agreement regime shift
- Fire shocks and climate stress
- Scenario comparison

### V0.3 — Two-stock system (current)
- Intact vs degraded forest
- Reinforcing vulnerability feedback
- Balancing recovery loop
- Interactive dashboard
- Written interpretation and conclusions

---

##  Interactive Dashboard (V0.3)

The project includes a **Streamlit dashboard** that allows users to:
- Explore scenarios via sliders
- Compare intact, degraded, and total forest
- Track degradation as a leading indicator
- Identify threshold crossing years (80% / 75%)

### Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
