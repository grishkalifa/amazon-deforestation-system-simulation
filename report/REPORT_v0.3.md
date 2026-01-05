# Amazon Deforestation System Simulation — Colombia  
## Technical Report V0.3 (Intact/Degraded Feedback Model)

---

## 1. What changed in V0.3 (why this version matters)

V0.1 and V0.2 treated fire mostly as a direct loss or as a simple shock channel.

V0.3 introduces a more realistic systems mechanism:

- The forest can exist in **two states**:
  - **Intact** (healthy, resilient)
  - **Degraded** (still present, but weakened)

- Fire does not only "remove forest".
  It can **convert intact → degraded**, creating **system memory**.

- Degradation creates a reinforcing loop:
  **more degraded forest → higher vulnerability → more degradation**.

- A balancing loop is added through recovery:
  **degraded → intact** at a slow rate.

This version is not meant to be a precise prediction.
It is a structural model that captures vulnerability dynamics and tipping risk.

---

## 2. Key results (human interpretation)

### 2.1 The main insight
The system can appear "stable" by looking only at total forest area,
while internally it becomes increasingly fragile due to the accumulation of degraded forest.

In other words:
- You may not “see” collapse early in total hectares,
- but the system can already be weakening toward a tipping regime.

### 2.2 Scenario comparison (high-level)
- **Enforcement (lower human conversion)** clearly delays threshold crossings.
  This indicates that governance and human conversion pressure remain a dominant long-term driver.

- **Climate stress (higher fires + stronger feedback)** increases degraded forest accumulation
  and accelerates the decline of intact forest.
  The core danger is not only fire loss, but the **vulnerability feedback** created by degradation.

---

## 3. What the dashed lines mean (critical clarification)

In V0.3, dashed lines are **not “trees growing”** and not “annual loss”.

They represent:
> Forest area that still exists but is in a weakened state (degraded).

This degraded state matters because it:
- burns more easily in the future
- dries faster
- has more fuel load
- becomes easier to convert or collapse after repeated stress cycles

Degraded forest is a **leading indicator** of future conversion risk.

---

## 4. Why this matters for real decision-making

A key takeaway from V0.3 is:
- Preventing human conversion slows total loss
- But preventing (and reversing) degradation is essential to reduce tipping risk

This suggests that policy and interventions should target both:
1) **conversion pressure** (governance, enforcement)
2) **degradation pathways** (fire prevention, landscape resilience, recovery/restoration)

---

## 5. Limitations 

- Parameters in V0.3 are scenario assumptions (not calibrated in this stage)
- No spatial modeling
- No explicit "deforested stock" tracked (we infer total loss from decline)
- Recovery is simplified
- Fire dynamics are still simplified relative to full ecological processes

Despite this, V0.3 successfully demonstrates the system logic:
**degradation as a memory state + feedback loop**.

---

## 6. Conclusion (V0.3)

V0.3 closes the conceptual gap left by earlier versions.

The model shows why “fire as a pulse” is not enough:
fire can act as a structural degradation process that increases future vulnerability.

This turns the Amazon problem into a classic system dynamics pattern:
- slow decline at first
- hidden fragility accumulation
- accelerating risk later due to reinforcing feedback

V0.3 is considered complete.

---

# Project Conclusion (V0.1 → V0.3)

Across the full study:

- **V0.1** established a clear baseline: constant annual loss leads to threshold crossings on century time horizons.
- **V0.2** showed that the dominant driver is persistent human conversion regimes; pulse-like fires do little under those assumptions.
- **V0.3** introduced the key missing mechanism: degradation and vulnerability feedback, which can silently weaken the forest before collapse becomes visible in total area.

Overall conclusion:
> Colombia’s Amazon deforestation trajectory may not look “immediately catastrophic” in total hectares,
> but sustained pressure and degradation accumulation make long-term risk unacceptable.
> The responsibility is intergenerational: protecting a resilient Amazon is a choice we either make now or we lose later.


