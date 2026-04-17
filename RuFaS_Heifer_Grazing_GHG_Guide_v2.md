# Heifer Pasture Management and GHG Emissions
## A Guide for Carbon Programs and Cooperative Members

**Version:** v2 (April 2026)
**Previous version:** v1 (March 2026) — superseded; see What Changed section
**Audience:** Carbon program administrators, co-op staff, dairy producers
**Purpose:** Summarize findings from a simulation-based analysis of GHG emissions intensity for pasture vs. confined heifer management on a representative Wisconsin dairy farm

---

## What Changed from v1

| Item | v1 (March 2026) | v2 (April 2026) |
|---|---|---|
| Modeling method for pasture manure | Legacy workaround (manure briefly routed through storage) | **Correct method: direct pasture deposit (DailySpread)** |
| Heifer pasture diet | Pure cool-season grass (97.3%) | **Realistic 80:20 grass-legume mix** |
| Reported GHG reduction | −2.9% | **−4.1%** |
| Manure nitrous oxide result | Reported +3,300% increase | **Retracted — was a modeling error; N2O unchanged from baseline** |
| Simulation completeness | 3 of 4 runs completed | **4 of 4 runs completed** |
| Confirmed by RuFaS team | No | **Yes — GitHub discussion #2941** |

**The most important change:** The v1 document reported a large manure nitrous oxide increase and described it as physically correct. This was incorrect. The spike was caused by a modeling error — routing manure briefly through a storage tank even for the pasture scenario. The correct modeling approach (DailySpread) bypasses storage entirely, and N2O returns to baseline levels. The pasture result is therefore cleaner than v1 suggested, and the emissions reduction is larger (−4.1%, not −2.9%).

---

## Overview

Moving growing heifers to pasture is a practice that dairy producers and carbon programs are evaluating as a potential emissions reduction strategy. The main mechanisms are:

1. **Eliminating anaerobic manure storage** — Confining heifers means collecting and storing manure in a covered or uncovered slurry tank, often for 4+ months. This produces significant methane. Pasture heifers deposit manure directly on soil.
2. **Reducing feed production emissions** — Grazed pasture has a much lower carbon footprint than harvested and transported silage, grain, and byproducts.
3. **Potential soil carbon sequestration** — Permanent pasture can build soil organic matter over time, but this is not yet captured in these results (see Limitations).

This guide summarizes findings from two modeling tools — FARMES and RuFaS — comparing confined and pasture heifer scenarios for a 1,000-cow Wisconsin dairy.

---

## The Two Tools

| | FARMES | RuFaS |
|---|---|---|
| Description | Nationally used reference model for farm-level GHG accounting | Local simulation model using NASEM 2021 nutrition standard |
| Status | Established, widely accepted | Under active development and validation |
| Each result | Average of 4 independent simulation runs | Average of 4 independent simulation runs |

**Important:** Do not compare absolute GHG values between FARMES and RuFaS. Total GHG intensity is about 50% higher in RuFaS due to differences in how the nutrition standard estimates feed requirements. Only compare Scenario A vs. B (within FARMES) and Scenario C vs. D (within RuFaS).

---

## The Four Scenarios

| Scenario | Tool | Heifer Housing | Heifer Diet | Heifer Manure |
|---|---|---|---|---|
| **A: FARMES Baseline** | FARMES | Confined freestall | Purchased TMR | Collected, 120-day slurry storage |
| **B: FARMES Heifer Pasture** | FARMES | Pasture | Purchased TMR (unchanged) | Pasture direct deposit |
| **C: RuFaS Baseline** | RuFaS | Confined freestall | Balanced TMR (7 ingredients) | Collected, 120-day slurry storage |
| **D: RuFaS Heifer Pasture** | RuFaS | Pasture | **77.8% cool-season grass + 19.5% legume + 2.7% mineral** | **Direct pasture deposit (no storage)** |

In all four scenarios, lactating cows remain in a confined freestall barn. Only the growing heifer management changes.

**Note on Scenario B:** FARMES does not change the heifer diet in the pasture scenario — only where the manure lands. This understates the diet-related benefits of pasture and is a limitation of the tool.

---

## GHG Intensity Results

GHG intensity is measured as kilograms of CO2-equivalent per kilogram of fat- and protein-corrected milk (kg CO2e/kg FPCM). **Lower is better.**

### FARMES (Scenarios A and B)

| | A: Baseline | B: Heifer Pasture | Change |
|---|---|---|---|
| Enteric methane | 0.456 | 0.456 | No change |
| Manure management | 0.272 | 0.359 | +32% |
| Feed production | 0.229 | 0.229 | No change |
| On-farm energy | 0.043 | 0.043 | No change |
| **Total (excl. land use)** | **0.999** | **1.086** | **+8.7%** |
| Land use change | 0.024 | 0.024 | No change |
| **Total (incl. land use)** | **1.024** | **1.110** | **+8.4%** |

### RuFaS (Scenarios C and D)

| | C: Baseline | D: Heifer Pasture | Change |
|---|---|---|---|
| Enteric methane | 0.764 | 0.770 | +0.9% |
| Manure management | 0.335 | 0.289 | **−13.7%** |
|   — of which: methane (CH4) | 0.334 | 0.289 | −13.7% |
|   — of which: nitrous oxide (N2O) | 0.0002 | 0.0002 | No change |
| Feed production (excl. land use) | 0.371 | 0.358 | −3.7% |
| **Total (excl. land use)** | **1.470** | **1.417** | **−3.6%** |
| Land use change | 0.034 | 0.026 | −24% |
| **Total (incl. land use)** | **1.504** | **1.443** | **−4.1%** |

---

## What Drives the Difference?

The −4.1% reduction in RuFaS Scenario D has four components:

| Driver | Effect | Explanation |
|---|---|---|
| Manure methane (CH4) | −13.7% | Eliminating 4-month anaerobic slurry storage removes the primary condition for manure methane production |
| Land use change (LUC) | −24% | Grazed pasture has near-zero land conversion footprint vs. purchased corn silage, grain, and alfalfa |
| Feed production | −3.7% | Lower energy inputs for grazed forage vs. harvested feed |
| Enteric methane | +0.9% | Fresh forage is higher in fiber than balanced TMR; slightly more rumen fermentation |
| Manure N2O | No change | Pasture direct deposit produces no more N2O than confined collection |

**The single largest lever is eliminating anaerobic manure storage.** This is the most well-understood mechanism and the most credible part of the result.

---

## Why the Two Tools Disagree

FARMES shows a +8.4% increase for heifer pasture; RuFaS shows a −4.1% decrease. The disagreement is centered on manure methane.

Eliminating 4 months of anaerobic slurry storage should reduce methane — this is the physically expected result, and what RuFaS shows. FARMES shows the opposite (+32% increase). This likely reflects an older emission factor approach in FARMES that does not properly penalize long-term anaerobic storage vs. pasture deposit.

**The RuFaS result is considered more physically credible for this specific question.** The direction and mechanism are well-supported by the science.

---

## What Is Not Yet Counted

**Soil carbon sequestration is the most important missing piece.** Managed permanent pasture can build soil organic matter over time, sequestering carbon at rates of 0.2–1.0 tonnes CO2 per hectare per year depending on soil, climate, and management. This sequestration is not included in the −4.1% figure.

Including soil carbon would make the pasture scenario look significantly better. This offset is being evaluated using additional modeling tools (RangeSTAR, SmartScape).

Other items not yet counted:
- **On-farm energy use** — not modeled in RuFaS (FARMES estimates ~0.043 kg CO2e/kg FPCM; would affect C and D equally)
- **Seasonal pasture variation** — fixed annual ration assumed
- **Heifer health and growth outcomes** — not modeled

---

## Co-Benefits Beyond GHG

The GHG analysis above captures only one dimension of the case for heifer pasture. Well-managed perennial pasture delivers substantial additional benefits across water quality, hydrology, and biodiversity — none of which are captured in RuFaS or FARMES modeling outputs.

The comparison below is pasture vs. tilled corn-soy rotations, which is the land use most likely displaced by heifer grazing in the Upper Midwest.

### Water quality and hydrology

| Metric | Tilled corn-soy | Managed perennial pasture | Change |
|---|---|---|---|
| Soil erosion | Baseline | Near zero | **~−100%** |
| Phosphorus runoff | 2.0 lb P/ac/yr | 0.2 lb P/ac/yr | **−90%** |
| Nitrate leaching | 28.6 lb N/ac/yr | 8.9 lb N/ac/yr | **−69%** |
| Stormwater runoff (5-inch event) | Baseline | −36% | **−36%** |

Perennial root systems maintain year-round soil structure, dramatically reducing both the volume and nutrient load of runoff — a meaningful benefit in Upper Midwest watersheds where phosphorus and nitrate loading are ongoing water quality concerns.

### Biodiversity

| Metric | Tilled corn-soy | Managed perennial pasture | Change |
|---|---|---|---|
| Grassland bird nesting density | 0.04 pairs/acre | 2.6 pairs/acre | **65× higher** |
| Pollinator habitat quality (0–10 index) | Baseline | 3–4× higher | **3–4× higher** |

Managed pasture provides nesting structure, floral resources, and reduced disturbance compared to annually tilled crop systems — habitat that has largely disappeared from the Upper Midwest agricultural landscape.

### Why this matters for carbon programs

These co-benefits represent additional unreported value in the GHG-only analysis. A heifer grazing practice delivers water quality, biodiversity, and carbon outcomes simultaneously. Programs that can stack or bundle these across markets (carbon, water quality, biodiversity offsets) will present a much stronger economic case to producers than a GHG-only intervention.

**Source:** Paine, L.K., Jackson, R., Raff, Z., Booth, E., Gratton, C., Gibson, A., LeZaks, D., Lloyd, S., and Wepking, C. (2021). *Well-managed perennial pasture: Setting the gold standard for ecosystem services.* Grassland 2.0, University of Wisconsin–Madison. grasslandag.org. Underlying data from Jackson (2020), Raff (2021), and Booth (2021); see Paine et al. for full reference list.

---

## Implications for Carbon Programs

### What this analysis supports

- A well-constructed heifer pasture system that eliminates long-term anaerobic manure storage is expected to reduce farm-level GHG intensity by a measurable amount (~4% or more in RuFaS).
- The mechanism is tractable and verifiable: eliminating manure storage time reduces methane.
- A realistic pasture diet (grass-legume mix) does not increase GHG intensity; it reduces it through lower feed production emissions.

### What requires more work before a carbon credit claim

- **Soil carbon must be quantified** — this is the largest unresolved component and likely the largest benefit.
- **RuFaS validation is ongoing** — absolute values are expected to shift as the nutrition model is refined. Results are directional, not final.
- **Site-specific factors matter** — herd size, soil type, climate, and existing manure infrastructure will affect the magnitude of the reduction.

### Practical recommendation

Programs and producers evaluating heifer pasture as an eligible practice should treat the −4.1% RuFaS figure as a conservative floor, with meaningful additional reductions expected once soil carbon is quantified. The practice is not yet ready for a precise per-tonne carbon credit calculation, but the directional signal is clear and the mechanism is credible.

---

## Frequently Asked Questions

**Q: Does moving heifers to pasture reduce total farm emissions?**
Yes, according to RuFaS (−4.1% intensity vs. baseline). FARMES disagrees, but RuFaS is more credible on this question due to its more detailed manure management model.

**Q: What about the large N2O increase that was reported in v1?**
That was a modeling error. The v1 analysis accidentally routed manure through a storage tank even in the pasture scenario, which triggered storage-based N2O emission factors. The correct modeling approach shows N2O is essentially unchanged from baseline. There is no increase.

**Q: Can heifers get enough nutrition from pasture alone?**
The model uses a Wisconsin-appropriate managed pasture ration (80% cool-season grass, 20% legume, 2.7% mineral). This is a realistic representation of intensive rotational grazing. The model does not currently capture reduced growth if the ration falls short, so results should be interpreted with that caveat.

**Q: Why is the RuFaS baseline intensity so much higher than FARMES (1.504 vs. 1.024)?**
Different nutrition standards. RuFaS uses NASEM 2021, which estimates higher energy requirements for the same cows. Only compare within the same tool (A vs. B, C vs. D).

**Q: Is the analysis public?**
Yes. All input files, simulation code, and documentation are available at https://github.com/carbon-yield/rufas-grazing-heifers, branch `heifer-pasture-analysis`.

---

## Summary

| Question | Answer |
|---|---|
| Does heifer pasture reduce GHG intensity? | Yes — RuFaS shows −4.1% (incl. land use change) |
| What is the main driver? | Eliminating 4-month anaerobic slurry storage (−13.7% manure CH4) |
| Does pasture diet increase emissions? | No — a grass-legume diet modestly reduces total emissions |
| Does pasture increase N2O? | No — previous report of +3,300% was a modeling error |
| Is soil carbon included? | Not yet — omitting it makes the −4.1% figure conservative |
| Which tool is more credible? | RuFaS on this question; FARMES result (+8.4%) likely reflects older emission factors |

---

*v2 — April 2026. Prepared by the carbon analysis team. Supersedes v1 (March 2026).*
*GitHub: https://github.com/carbon-yield/rufas-grazing-heifers | Branch: heifer-pasture-analysis*
