# GHG Intensity Analysis — Wisconsin Fake Test Farm 2 | Meeting Brief (v3)

**Date:** March 12, 2026
**Version:** v3 — simplified to four scenarios; Scenario D is now full pasture system (manure + pasture diet)
**Audience:** Stakeholders (non-technical briefing)
**Purpose:** Summary of greenhouse gas (GHG) intensity analysis comparing confined vs. pasture heifer management

---

## What Changed from v2

| Item | v2 | v3 |
|---|---|---|
| Scenarios | A, B (FARMES), C, D (RuFaS) | A, B (FARMES), C, D (RuFaS) — but **Scenario D is now the complete pasture system** (manure + grazing diet) |
| v2 Scenario D (manure routing only) | Included | **Dropped** — intermediate step, not a meaningful standalone scenario |
| RuFaS Baseline (C) runs | 3 of 4 | **4 of 4** (all completed successfully in Mar 12 run) |
| RuFaS Heifer Pasture + Feed (D) runs | — | 3 of 4 |
| RuFaS Baseline total intensity (excl. LUC) | 1.469 | **1.470** (negligible shift from fresh seed set) |
| v2 diet gap addressed | Partially — identified as missing | **Closed**: heifers now modeled eating grazed cool-season grass (97.3%) + mineral supplement (2.7%) |

**Key change in framing:** v2 had an intermediate scenario where heifers were moved to pasture but still ate the same purchased TMR. That is not a realistic or decision-relevant scenario — in practice, pasture heifers eat grazed grass. v3 drops that intermediate step and presents the complete comparison: **confined heifers eating TMR** (A, C) vs. **pasture heifers eating grazed grass** (B, D).

---

## Executive Summary

This brief presents results from an ongoing analysis of GHG emissions intensity for a representative 1,000-cow Wisconsin dairy farm. Two modeling tools were used to evaluate the same question: **does moving heifers to pasture — with a realistic grazing diet — reduce the farm's greenhouse gas footprint?**

**The two tools still give different answers.** FARMES shows pasture management increases emissions by +8.4%. RuFaS shows it decreases emissions by −2.9% (including land use change) or −2.2% (excluding land use change). Both effects are primarily driven by heifer manure management; the diet change contributes a smaller additional benefit through lower land use change emissions.

**The most important unresolved gap** is soil carbon sequestration under pasture, which RuFaS does not currently model and which is likely to favor the pasture scenario.

---

## Background: What Is Being Compared

### The Two Tools

- **FARMES** — A nationally used reference model. Results are the average of four independent simulation runs.
- **RuFaS** — A local simulation model developed at this institution, currently undergoing validation. Uses NASEM 2021 nutrition standard.

### The Four Scenarios

| Scenario | Tool | Heifer Manure Management | Heifer Diet |
|---|---|---|---|
| **A: FARMES Baseline** | FARMES (avg 4 runs) | Straw bedding; scraped and stored in covered slurry tank for 120 days | Purchased TMR |
| **B: FARMES Heifer Pasture** | FARMES (avg 4 runs) | No bedding; manure deposited directly on pasture | Purchased TMR |
| **C: RuFaS Baseline** | RuFaS (avg 4 runs) | Straw bedding; scraped and stored in covered slurry tank for 120 days | Purchased TMR |
| **D: RuFaS Heifer Pasture** | RuFaS (avg 3 runs) | No bedding; 1-day storage/crust; manure deposited on pasture | **97.3% grazed cool-season grass + 2.7% mineral supplement** |

**In plain terms:** A and C represent the current, conventional approach — heifers housed indoors, manure collected and stored, diet balanced by a nutritionist. B and D represent the alternative: heifers graze on pasture, deposit manure outdoors, and eat grazed grass with a free-choice mineral supplement.

**Note on Scenario B:** The FARMES heifer pasture scenario does not change the heifer diet — only where manure lands. This is a limitation of FARMES, not a deliberate choice. The RuFaS Scenario D models both the manure and diet change, making it a more complete representation of a real pasture system.

---

## Input Comparison

| Input | FARMES (A, B) | RuFaS (C, D) |
|---|---|---|
| Dairy cows | 1,000 Holstein cows | 1,000 Holstein cows |
| Calves | 333 | 333 |
| Growing heifers | ~718 | ~633 (simulated average) |
| Annual milk production | ~9.2 million kg | ~10.1 million kg |
| Milk per cow per day | 28.6 kg | ~31.1 kg |
| Fat- and protein-corrected milk (FPCM)* | ~9.14 million kg/yr | ~10.1 million kg/yr |
| Feed intake per lactating cow per day | 21.5 kg dry matter | ~30.4 kg dry matter |
| Confined heifer diet (A, C) | Corn silage, alfalfa silage, hay, grass-legume silage, byproduct blend, corn grain, mineral | Same |
| Pasture heifer diet (B) | Purchased TMR (unchanged) | — |
| Pasture heifer diet (D) | — | **Grazed cool-season grass (97.3%) + mineral supplement (2.7%)** |
| On-farm crop production | None — all feed purchased | None — all feed purchased |
| Emissions allocated to milk | 86.0% | ~88.5% |

*FPCM is a standardized milk measure used as the emissions denominator.

**Why are feed intake and milk production higher in RuFaS?** RuFaS uses the NASEM 2021 nutrition standard, which estimates higher energy requirements. This is a known difference under active review during validation. Only compare scenarios within the same tool.

---

## Output Comparison: GHG Intensity Results

GHG intensity = kg CO2-equivalent emitted per kg of fat- and protein-corrected milk produced. **Lower is better.**

> **Note on units:** FARMES reports in lb CO2e / lb FPCM, which is numerically identical to kg/kg.

### FARMES Results (Scenarios A and B)

| Emission Source | A: FARMES Baseline | B: FARMES Heifer Pasture | Change |
|---|---|---|---|
| Enteric methane (digestion) | 0.456 | 0.456 | No change |
| Manure management | 0.272 | 0.359 | **+32%** |
| Feed production | 0.229 | 0.229 | No change |
| On-farm energy use | 0.043 | 0.043 | No change |
| **Total (excl. land use change)** | **0.999** | **1.086** | **+8.7%** |
| Land use change | 0.024 | 0.024 | No change |
| **Total (incl. land use change)** | **1.024** | **1.110** | **+8.4%** |

### RuFaS Results (Scenarios C and D)

| Emission Source | C: RuFaS Baseline | D: RuFaS Heifer Pasture | Change |
|---|---|---|---|
| Enteric methane (digestion) | 0.764 | 0.771 | **+0.9%** |
| Manure management | 0.335 | 0.299 | **−10.7%** |
| — of which: manure methane (CH4) | 0.334 | 0.292 | **−12.6%** |
| — of which: manure nitrous oxide (N2O) | 0.000 | 0.007 | **+3,300%** |
| Feed production (excl. land use) | 0.371 | 0.367 | **−1.1%** |
| On-farm energy use | Not yet captured | Not yet captured | — |
| **Total (excl. land use change)** | **1.470** | **1.437** | **−2.2%** |
| Land use change | 0.034 | 0.024 | **−29%** |
| **Total (incl. land use change)** | **1.504** | **1.461** | **−2.9%** |

**Note on enteric methane:** Heifers eating grazed cool-season grass produce slightly more enteric methane than heifers eating a balanced TMR (+0.9%). Fresh grass has higher fiber content and lower digestibility, increasing rumen fermentation per unit of dry matter. The effect is small and physically expected.

**Note on manure N2O:** The large relative increase (+3,300%) reflects urine and feces deposited directly on soil in aerobic conditions. This is physically correct — it is large relative to a near-zero baseline. In absolute terms, the N2O increase (~0.007 kg CO2e / kg FPCM) is far smaller than the methane decrease (~0.042), so the net manure effect is a reduction.

**Note on land use change:** The larger LUC reduction in Scenario D (−29%) reflects the shift from purchased corn silage and alfalfa to grazed pasture grass. Grass grown on managed pasture requires minimal fertilizer, machinery, or processing, and carries essentially no land conversion footprint. This is the primary reason Scenario D's total intensity (including LUC) is lower than it would appear from the excl. LUC comparison alone.

---

## Summary Table: All Four Scenarios

| | A: FARMES Baseline | B: FARMES Heifer Pasture | C: RuFaS Baseline | D: RuFaS Heifer Pasture |
|---|---|---|---|---|
| **Tool** | FARMES | FARMES | RuFaS | RuFaS |
| **Heifer manure** | Indoor / 120-day slurry | Pasture deposit | Indoor / 120-day slurry | Pasture deposit |
| **Heifer diet** | Purchased TMR | Purchased TMR | Purchased TMR | Grazed grass |
| **Runs averaged** | 4 | 4 | 4 | 3 |
| **Enteric CH4** | 0.456 | 0.456 | 0.764 | 0.771 |
| **Manure** | 0.272 | 0.359 | 0.335 | 0.299 |
| **Feed (excl. LUC)** | 0.229 | 0.229 | 0.371 | 0.367 |
| **Energy** | 0.043 | 0.043 | — | — |
| **Total (excl. LUC)** | **0.999** | **1.086** | **1.470** | **1.437** |
| **Total (incl. LUC)** | **1.024** | **1.110** | **1.504** | **1.461** |
| **Change vs. baseline** | — | **+8.4% ↑** | — | **−2.9% ↓** |

⚠️ **FARMES and RuFaS disagree on the direction of the effect.** See Key Findings.

**Do not compare absolute values between FARMES and RuFaS.** Total intensity is ~50% higher in RuFaS due to differences in nutrition methodology.

---

## Key Findings

### Finding 1: The two tools disagree — and the disagreement matters

| Question | FARMES | RuFaS |
|---|---|---|
| Does heifer pasture reduce GHG intensity? | **No — +8.4%** | **Yes, slightly — −2.9%** |
| What drives the change? | Manure CH4 and N2O both increase | Manure CH4 drops sharply; N2O rises; CH4 reduction dominates |

The disagreement traces to a single question: does moving heifers to pasture increase or decrease manure methane?

- **FARMES says methane increases (+30%)** when heifers go to pasture. This is physically counterintuitive — 120-day anaerobic slurry storage is the primary condition for methane production.
- **RuFaS says methane decreases (−13%)** when heifers go to pasture. This is the physically expected result and is likely more correct.

The FARMES result likely reflects an older emission factor approach. However, RuFaS still has gaps — most importantly soil carbon (see below).

### Finding 2: The net RuFaS result depends on whether land use change is included

| Accounting boundary | C: RuFaS Baseline | D: RuFaS Heifer Pasture | Change |
|---|---|---|---|
| **Incl. land use change** | 1.504 | **1.461** | **−2.9%** |
| **Excl. land use change** | 1.470 | **1.437** | **−2.2%** |

The pasture scenario is better under both accounting conventions, but the margin is slightly larger when land use change is included — because grazed grass carries much lower LUC emissions than purchased corn silage or alfalfa. For standard lifecycle GHG reporting, LUC is typically included.

### Finding 3: Soil carbon is the missing piece

Neither FARMES nor RuFaS models soil carbon sequestration under permanent pasture. Managed grassland can sequester 0.2–1.0 tonnes CO2 per hectare per year depending on soil, climate, and management. This offset — likely favorable to Scenario D — is not captured in the current results. The true benefit of the pasture scenario is probably larger than the −2.9% shown here.

---

## Can RuFaS Answer the Grazing Question? — Model Assessment

### What RuFaS currently captures well

| Emission source | Notes |
|---|---|
| Enteric methane | Correctly increases slightly for grazed-grass diet |
| Manure methane from housing and storage | Key differentiator — correctly penalizes long anaerobic slurry storage |
| Manure N2O (direct) | Large increase for pasture correctly modeled |
| Feed production emissions and LUC | Captures lower footprint of grazed pasture vs. purchased TMR ingredients |

### Remaining gaps

**1. Soil carbon sequestration (most material)**
Permanent pasture sequesters carbon in soil organic matter. RuFaS does not model this. It is the single largest missing piece and is expected to further favor the pasture scenario.

**2. Pasture-specific N2O indirect pathways**
RuFaS captures direct soil N2O. Indirect N2O from leached nitrate and atmospheric deposition (from ammonia volatilized off pasture) is less certain.

**3. On-farm energy use**
Not modeled in RuFaS. FARMES estimates ~0.043 kg CO2e / kg FPCM; adding this would affect A/B and C/D equally and not change the direction of any comparison.

### Where RangeSTAR and SmartScape could help

- **RangeSTAR:** Designed to quantify soil carbon changes, pasture-specific N2O, and the full carbon cycle of a grazed system. Directly addresses Gap #1. Output could be added as an emission component in RuFaS.
- **SmartScape:** Spatial landscape tool for carbon sequestration, nutrient retention, and water quality at the farm or watershed level. Most useful if the analysis needs to move from whole-farm intensity to field-level or watershed-scale evaluation.

### Is RuFaS sufficient?

| Question | Answered? |
|---|---|
| Does eliminating slurry storage reduce manure methane? | Yes — likely more accurately than FARMES |
| Does pasture deposit increase N2O? | Partially — direct N2O yes; indirect pathways uncertain |
| What is the diet impact of grazing? | Yes — modeled in Scenario D |
| Does soil carbon sequestration offset emissions? | No — requires RangeSTAR or equivalent |
| What is the full lifecycle impact? | Not yet — soil carbon gap remains |

**RuFaS gives a physically credible partial answer.** The key mechanisms — manure storage methane reduction, N2O increase from pasture deposits, and lower feed LUC — are all correctly captured. The missing soil carbon component is expected to make the pasture scenario look even better than currently shown.

---

## Caveats and Limitations

1. **FARMES and RuFaS disagree on the direction of the effect.** RuFaS is likely correct on manure methane, but neither captures soil carbon.

2. **Do not compare absolute values between FARMES and RuFaS.** Total intensity is ~50% higher in RuFaS. Only compare A vs. B and C vs. D.

3. **RuFaS run counts: 4 baseline (C), 3 heifer pasture (D).** A race condition in the parallel task runner occasionally causes one worker to crash before producing output. Seed-to-seed variation is negligible (±0.002 kg CO2e / kg FPCM); 3-run averages are reliable.

4. **Scenario D uses a simplified pasture diet.** The model does not capture seasonal variation in pasture quality, stocking density requirements, or the transition from TMR to grazing.

5. **Soil carbon is not modeled.** Permanent pasture can sequester 0.2–1.0 tonnes CO2/ha/year. This offset is not included in any scenario and is likely favorable to Scenario D.

6. **All feed is treated as purchased.** In Scenario D, pasture grass is modeled as a purchased feed with very low production emissions. Actual on-farm pasture management could have additional co-benefits not captured here.

7. **Energy use is not captured in RuFaS.** FARMES estimates ~0.043 kg CO2e / kg FPCM; adding this would affect C and D equally.

8. **RuFaS is still being validated.** Absolute values are expected to shift as the nutrition model is refined. These results are directional, not final.

9. **Results are specific to this farm.** Different herd sizes, climate, soil types, or manure infrastructure may show different results.

---

## Notes on Non-Technical Presentation

- **The comparison is now clean and intuitive:** confined heifers eating TMR vs. pasture heifers eating grass. This resonates with a non-technical audience much more directly than an intermediate manure-routing scenario.
- **Lead with the bottom line:** the two tools disagree, RuFaS is likely more correct on the direction, and the missing piece is soil carbon.
- **The N2O number (+3,300%) needs immediate context.** It is a large relative change from a near-zero baseline. The absolute increase (~0.007 kg CO2e / kg FPCM) is far smaller than the methane decrease (~0.042). Without this framing it will alarm people.
- **The soil carbon gap is the most accessible storyline.** "Grass stores carbon in the ground — and we haven't counted that yet" is easy to communicate and positions RangeSTAR integration as the obvious next step.
- **The FARMES vs. RuFaS disagreement is an opportunity.** Frame it as "our newer, more detailed model tells a different story" rather than "the models are confused."

---

*Document prepared for internal stakeholder briefing. Results are preliminary. v3 supersedes v2 (2026-03-10). Run data from March 12, 2026.*

---

## Appendix: Input File Changes by Scenario

This appendix documents the exact files and lines changed to construct each scenario. All scenarios share a common base; the changes below are relative to Scenario C (RuFaS Baseline).

---

### Scenario C vs. D: Three files changed

Each scenario is defined by a metadata file that points to input data files. The metadata files themselves differ at three lines:

| Field | Scenario C metadata | Scenario D metadata |
|---|---|---|
| Animal file (line 13) | `rufas_match_animal_baseline.json` | `rufas_match_animal.json` |
| Feed file (line 76) | `example_Midwest_feed.json` | `example_Midwest_feed_heifer_pasture.json` |
| Manure config (line 97) | `example_freestall_processor_configs_baseline.json` | `example_freestall_processor_configs.json` |

**Metadata files:**
- C: `input/metadata/example_freestall_dairy_metadata_baseline.json`
- D: `input/metadata/example_freestall_dairy_metadata_heifer_pasture_feed.json`

---

### Change 1 — Bedding

**File:** `input/data/animal/rufas_match_animal_baseline.json` → `input/data/animal/rufas_match_animal.json`

| Line | Field | Baseline (C) | Heifer Pasture (D) |
|---|---|---|---|
| 196 | `bedding_name` (growing pen) | `"straw"` | `"none (no bedding)"` |

All other pens unchanged: calf pen (line 177) keeps `"calf_straw"`; close-up and lactating cow pens (lines 215, 237) keep `"straw"`.

---

### Change 2 — Manure Handler and Storage

**File:** `input/data/manure/example_freestall_processor_configs_baseline.json` → `input/data/manure/example_freestall_processor_configs.json`

**Handler (growing heifer pen):**

| Line | Field | Baseline (C) | Heifer Pasture (D) |
|---|---|---|---|
| 26 | `processor_type` for `growing_alley_scraper` | `"AlleyScraper"` | `"ManualScraper"` |

**Storage (growing heifer storage only — `slurry_storage_outdoor_growing`):**

| Line | Field | Baseline (C) | Heifer Pasture (D) |
|---|---|---|---|
| 85 | `cover` | `"no_crust_or_cover"` | `"crust"` |
| 86 | `storage_time_period` | `120` (days) | `1` (day) |

All other storage units (close-up, lactating cow) are unchanged: `"no_crust_or_cover"`, 120 days.

**Why these changes matter:** The baseline stores growing heifer manure in an uncovered outdoor slurry tank for 120 days — the primary condition for anaerobic methane production. The heifer pasture scenario reduces storage to 1 day and adds a natural crust, sharply reducing the time manure spends under anaerobic conditions.

---

### Change 3 — Growing Heifer Feed Ration

**File:** `input/data/feed/example_Midwest_feed.json` → `input/data/feed/example_Midwest_feed_heifer_pasture.json`

**`growing_feeds` list (lines 6–13):**

| | Baseline (C) | Heifer Pasture (D) |
|---|---|---|
| Feed IDs | `[44, 50, 95, 104, 110, 301, 302]` | `[92, 301]` |

**`user_defined_ration_percentages.growing` (lines 110–135 → lines 110–115):**

| | Baseline (C) | Heifer Pasture (D) |
|---|---|---|
| ID 50 — Corn silage (line 110) | 30.41% | removed |
| ID 110 — Alfalfa silage (line 114) | 26.30% | removed |
| ID 95 — Hay (line 118) | 10.755% | removed |
| ID 104 — Grass-legume silage (line 122) | 10.755% | removed |
| ID 44 — Corn grain (line 126) | 3.84% | removed |
| ID 302 — Byproduct blend (line 134) | 15.21% | removed |
| ID 301 — Mineral mix (line 130) | 2.74% | **2.74%** (line 114, unchanged) |
| ID 92 — Cool-season grass, pasture | — | **97.26%** (line 110) |

**Additional changes to support ID 92:**
- `purchased_feeds` list: ID 92 added (line 41) with `purchased_feed_cost: 0.01`
- `allowances` list: ID 92 added (line 185) with `runtime_purchase_allowance`, `advance_purchase_allowance`, and `planning_cycle_allowance` all set to `1000.0`

All other pen rations (calf, close-up, lactating cow) are identical between the two feed files.

---

### Feed ingredient reference

| RuFaS ID | Name | Type | Source database |
|---|---|---|---|
| 44 | Corn, yellow — grain | Grain | `user_feeds.csv` line 45 |
| 50 | Corn, yellow — silage, immature | Forage | `user_feeds.csv` line 51 |
| 92 | Grasses, cool season — pasture | Forage | `user_feeds.csv` line 93 |
| 95 | Grass-legume mixtures — hay, mature | Forage | `user_feeds.csv` line 96 |
| 104 | Grass-legume mixtures — silage | Forage | `user_feeds.csv` line 105 |
| 110 | Legumes, forage — alfalfa silage | Forage | `user_feeds.csv` line 111 |
| 301 | Farm ES Mineral Mix | Mineral | `NASEM_Comp_with_TDN.csv` line 171 |
| 302 | Farm ES Midwest BP Blend | Conc | `NASEM_Comp_with_TDN.csv` line 172 |
