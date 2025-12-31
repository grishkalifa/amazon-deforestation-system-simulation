# Amazon Deforestation System Simulation — Colombia (V0.1)

## 1. Objective

The objective of this project is to model the long-term evolution of forest cover in the Colombian Amazon using a **system dynamics approach**, and to evaluate how different deforestation regimes affect the timing of critical risk thresholds.

This work is not intended to provide precise predictions.  
Instead, it aims to **identify structural behaviors, regime changes, and risk acceleration** under simplified but transparent assumptions.

This project serves as a foundational case study in applied systems simulation, forming part of a broader research path toward AGI-oriented decision-support systems.

---

## 2. System Overview

### 2.1 System Boundary

The system is modeled as **semi-closed**.

External drivers such as climate variability, governance, economic incentives, and population dynamics are **not explicitly modeled**.  
Their effects are instead **implicitly reflected through changes in deforestation rates**.

This boundary choice prioritizes clarity and interpretability over full realism in early model versions.

---

### 2.2 Core Stock

- **Stock:** Forest cover in the Colombian Amazon  
- **Unit:** Hectares (ha)

The forest is represented as a **single homogeneous stock**, without distinguishing forest type, quality, or spatial distribution.

---

### 2.3 Flows

#### Outflow — Deforestation
Deforestation aggregates multiple processes into a single annual flow:
- Illegal logging  
- Forest fires  
- Agricultural and land-use expansion  

Unit: hectares per year (ha/year)

#### Inflow — Regeneration
In Version 0.1, regeneration is **set to zero** in order to analyze a conservative worst-case baseline and isolate loss-driven dynamics.

---

## 3. Mathematical Formulation

Time is modeled in **discrete annual steps**.

Let:

- `F_t`: forest cover at year `t` (ha)  
- `D_t`: deforestation during year `t` (ha/year)  
- `R_t`: regeneration during year `t` (ha/year)

The system evolves according to:

F_(t+1) = F_t - D_t + R_t


For Version 0.1:


R_t = 0


Deforestation is modeled as:

D_t = D_base × P_t


Where:
- `D_base` is a constant baseline deforestation rate
- `P_t` is an external pressure multiplier

---

## 4. Data and Parameters

### 4.1 Initial Forest Stock

- Initial forest cover: **39,011,117 ha**  
- Source: IDEAM — Forest cover in the Amazon biome (reference year 2021)

This value is used as the starting stock `F_0`.

---

### 4.2 Baseline Deforestation Rate

- Baseline deforestation rate: **81,240 ha/year**
- Derived from the **average deforestation in the Amazon region during 2020–2024**

This value defines the **Business-As-Usual (BAU)** scenario.

---

### 4.3 Post-Agreement Peak Scenario (Aggressive Regime)

To evaluate regime change effects, a second scenario is defined using the **maximum post-peace-agreement deforestation spike**:

- Years considered: **2017–2018**
- Average deforestation rate: **≈119,000 ha/year**

This scenario is not treated as permanent reality, but as a **proxy for a high-pressure deforestation regime** following structural territorial change.

---

## 5. Critical Threshold Definition

The model does not define an exact ecological tipping point.  
Instead, it uses **precautionary loss thresholds** as proxies for increased risk of irreversible degradation.

Two thresholds are analyzed:

- **20% cumulative forest loss** (lower-bound risk zone)
- **25% cumulative forest loss** (upper-bound risk zone)

These thresholds are commonly referenced in scientific literature as ranges where large-scale Amazon dieback risk increases when combined with additional stressors.

---

## 6. Results

### 6.1 Baseline Scenario (2020–2024 Average)

Under a constant deforestation rate of **81,240 ha/year** and no regeneration:

- 20% cumulative loss is reached around **2122**
- 25% cumulative loss is reached around **2146**

This trajectory suggests a slow but persistent erosion of forest cover under Business-As-Usual conditions.

---

### 6.2 Post-Agreement Peak Scenario (2017–2018)

Under the aggressive post-agreement regime (**≈119,000 ha/year**):

- 20% cumulative loss is reached around **2091**
- 25% cumulative loss is reached around **2107**

Compared to the baseline, critical thresholds are reached **30–40 years earlier**, demonstrating strong sensitivity to regime changes even when they are not permanent.

---

## 7. System Interpretation

The results highlight three key systemic insights:

1. **Deforestation dynamics are non-linear in risk**, even when modeled linearly in time.
2. **Temporary regime shifts** can permanently alter long-term outcomes.
3. The system exhibits **irreversibility**: losses accumulated during high-pressure periods are not recovered when pressure returns to baseline.

This behavior is characteristic of complex systems operating near critical thresholds.

---

## 8. Model Limitations

This Version 0.1 model intentionally excludes:

- Climate feedbacks
- Biodiversity indicators
- Spatial heterogeneity
- Socioeconomic variables
- Governance and enforcement dynamics
- Regeneration and restoration processes

These exclusions preserve interpretability and will be addressed in future versions.

---

## 9. Conclusion

This first iteration demonstrates how **changes in deforestation regimes**, rather than slow linear trends alone, can significantly accelerate the approach to critical risk thresholds in the Colombian Amazon.

The model establishes a transparent baseline for future extensions, including regeneration dynamics, external shocks, and AI-assisted scenario exploration.

---

## 10. Next Steps

Planned extensions include:

- Introduction of regeneration dynamics (Version 0.2)
- Explicit shock modeling (climate or governance-driven)
- Interactive visualization and dashboards
- Integration with AI-based reasoning layers for policy exploration

---

### Status
**Version:** 0.1  
**Purpose:** Structural system understanding  
**Not intended for:** Precise forecasting or policy prescription
