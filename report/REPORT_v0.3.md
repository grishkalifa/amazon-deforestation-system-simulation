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


## Conclusions and Interpretation (V0.3)

This study models the Colombian Amazon as a **dynamic system**, not as a static resource.  
The goal is not to predict an exact future, but to understand **structural risks and trajectories**.

### 1. Current deforestation is alarming, even if it does not look catastrophic yet

At current average rates (~80,000 hectares per year), Colombia loses the equivalent of:

- **~220 hectares per day**
- **~300 football fields every single day**

This pace may appear “manageable” in annual statistics, but system dynamics show that **slow, continuous pressure is precisely how irreversible damage accumulates unnoticed**.

### 2. Post-peace-agreement deforestation marks a structural regime shift

After the 2016 peace agreement, deforestation increased sharply.  
This does **not** imply environmental protection motives by armed groups, but it does reveal an important systemic reality:

> Armed control, land access restrictions, and informal governance unintentionally limited forest conversion.

Once that control disappeared, **human-driven land conversion intensified**, creating a new baseline regime that persists unless active enforcement changes it.

In the model, this is represented as a **persistent increase in human conversion pressure**, not a temporary shock.

### 3. Why the 80% threshold matters

Crossing **80% of remaining forest** is not an arbitrary number.

Scientific literature suggests that below this level:
- Regional rainfall recycling weakens
- Forest microclimates dry out
- Fire susceptibility increases
- Recovery becomes slower and less reliable

In system terms, this is where **reinforcing feedback loops dominate**:
degradation → vulnerability → more degradation.

Once crossed, the system becomes **much harder and more expensive to stabilize**, even if deforestation slows later.

### 4. Degradation is the hidden early warning

This model separates **intact forest** from **degraded forest**.

Degraded forest:
- Still “exists” in official statistics
- Still looks green from above
- But has lower resilience and higher fire risk

Rising degradation is a **leading indicator** of future collapse.  
Waiting until total forest loss looks dramatic is waiting too long.

### 5. Why this matters for future generations

This is a classic delayed-feedback problem:

> The damage accumulates quietly, while consequences arrive suddenly.

If current trajectories continue, future generations will not inherit a sudden disaster —  
they will inherit a **system already past its recovery point**.

The Amazon does not fail overnight.  
It fails gradually… until it doesn’t recover anymore.

### 6. What this model is — and what it is not

This model is:
- A **structural thinking tool**
- A way to test scenarios and feedbacks
- A lens to reason about long-term risk

This model is not:
- A precise forecast
- A spatial or ecological micro-simulation
- A substitute for field data

Its value lies in **clarifying why early action matters more than late reaction**.
