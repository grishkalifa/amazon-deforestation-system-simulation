# Amazon Deforestation System Simulation — Colombia  
## Technical Report V0.2 (Channelized Shocks)

---

## 1. Purpose of Version 0.2

Version 0.2 extends the baseline model (V0.1) by introducing **channelized shocks** to avoid double counting and preserve causal clarity.

The objective of this version is **not prediction**, but **structural insight**:
- Which drivers dominate long-term forest loss?
- How sensitive are system thresholds to different shock channels?

This version prepares the ground for a more realistic degradation-feedback model in V0.3.

---

## 2. Model Scope and Simplifications

The model remains intentionally simple:

- Single stock: **Amazon forest cover (hectares)**
- Annual discrete time steps
- No regeneration (worst-case baseline)
- No population or economic dynamics
- No spatial heterogeneity

These simplifications are deliberate and documented.

---

## 3. Channelized Deforestation Structure

Deforestation is separated into two distinct components:

### 3.1 Human-driven deforestation (D_human)

- Baseline proxy: average Amazon deforestation (2020–2024)
- A **persistent post-accord regime shift** is applied from 2017 onward
- This shock affects **only the human component**

This represents sustained land-use pressure, governance changes, and expansion dynamics.

---

### 3.2 Fire-driven loss (D_fire)

- Fires are modeled as **additive pulses**, not as baseline deforestation
- El Niño years amplify **only the fire component**
- Fires are **intentionally excluded from 2017–2018** to avoid double counting with post-accord dynamics

In this version, fires act as a simplified proxy, not as a full degradation mechanism.

---

## 4. Scenarios Simulated

Four scenarios were analyzed:

1. **BAU (human only, no shocks)**
2. **Post-accord regime shift (human-driven only)**
3. **Post-accord + fire pulses**
4. **Post-accord + fire pulses + El Niño amplification**

---

## 5. Key Results — Threshold Crossing Years

| Scenario | 80% Remaining | 75% Remaining |
|--------|---------------|---------------|
| BAU (no shocks) | 2097 | 2121 |
| Post-accord (human regime shift) | 2078 | 2097 |
| Post-accord + fires | 2078 | 2096 |
| Post-accord + fires + El Niño | 2078 | 2096 |

---

## 6. Interpretation

The dominant finding of V0.2 is that:

> **Persistent human-driven deforestation regimes dominate long-term system outcomes.**

Under the modeled assumptions:
- The post-accord regime accelerates the loss of critical forest thresholds by ~20–25 years.
- Fire pulses and El Niño amplification, when modeled as isolated shocks, have **minimal impact on threshold timing**.

This does **not** imply that fires are unimportant in reality.
Rather, it shows that **fires modeled as simple pulses are insufficient to explain system collapse**.

---

## 7. Conceptual Insight and Model Limitation

Expert feedback indicates that fires should be treated as a **distinct degradation channel** with feedback:

- Initial fires degrade forest structure
- Degraded forests become more vulnerable to future fires
- After multiple cycles, degradation tips into permanent conversion

Version 0.2 does **not** yet model this degradation pipeline.
Doing so would require:
- Additional system states
- Memory and feedback loops
- Nonlinear transition dynamics

This mechanism is therefore **explicitly deferred to Version 0.3**.

---

## 8. Conclusion

Version 0.2 demonstrates that:
- The primary risk to the Colombian Amazon is **persistent human pressure**, not isolated shocks.
- Preventing regime-level deforestation dynamics is more impactful than reacting to episodic events.
- Accurately capturing fire dynamics requires a degradation-feedback model, not additive losses.

Version 0.2 is considered **complete**.

---

## 9. Next Step (V0.3)

Version 0.3 will introduce:
- Forest degradation as an explicit system state
- Fire-driven feedback loops
- Tipping-point dynamics from degradation to deforestation

This will move the model from **shock analysis** to **structural vulnerability analysis**.
