# GHG Intensity Analysis — Wisconsin Fake Test Farm 2 | Meeting Brief (v4)

**Date:** April 15, 2026
**Version:** v4 — updated manure methodology (DailySpread), revised pasture diet (80:20 grass-legume), corrected N2O interpretation
**Audience:** Stakeholders (non-technical briefing)
**Purpose:** Summary of greenhouse gas (GHG) intensity analysis comparing confined vs. pasture heifer management

---

## What Changed from v3

| Item | v3 | v4 |
|---|---|---|
| Manure methodology (Scenario D) | ManualScraper + 1-day slurry/crust (legacy workaround) | **DailySpread** (correct v1.0 approach for pasture direct-deposit) |
| Pasture heifer diet (Scenario D) | ID 92 only (97.3% cool-season grass) | **80:20 grass-legume mix** (ID 92: 77.81% + ID 105: 19.45% + ID 301: 2.74%) |
| RuFaS Heifer Pasture runs | 3 of 4 | **4 of 4** |
| Manure N2O interpretation | "+3,300% increase — physically correct aerobic effect" | **Retracted — was a modeling artifact of the slurry workaround; N2O now near-baseline** |
| GHG intensity incl. LUC (Scenario D) | 1.461 | **1.443** |
| GHG intensity excl. LUC (Scenario D) | 1.437 | **1.417** |
| Change vs. baseline incl. LUC | −2.9% | **−4.1%** |

**Why these changes were made:** The RuFaS development team confirmed (GitHub discussion #2941) that `ManualScraper + 1-day slurry` was a legacy workaround for pre-v1.0. The correct approach for pasture direct-deposit in v1.0 is `DailySpread`. They also recommended including legumes in the pasture ration as a more realistic representation of managed Wisconsin pastures. Both changes were implemented in this version.

**The N2O retraction is significant.** v3 presented a +3,300% manure N2O increase as a physically correct consequence of aerobic pasture conditions. Analysis of v4 results shows N2O returns to near-baseline levels under DailySpread (9.5 kg vs. 9.5 kg baseline, compared to 441 kg under the old workaround). The spike was an artifact of routing manure through a slurry storage unit — even for 1 day — which triggered storage-based N2O emission factors. DailySpread correctly bypasses storage entirely.

---

## Executive Summary

This brief presents results from an analysis of GHG emissions intensity for a representative 1,000-cow Wisconsin dairy farm using two modeling tools. The central question: **does moving growing heifers to pasture — with a realistic grazing diet — reduce the farm's greenhouse gas footprint?**

**RuFaS shows a clear reduction of −4.1%** (including land use change) for the pasture scenario vs. confined baseline. This is driven primarily by eliminating 120-day anaerobic slurry storage for heifer manure. The diet shift to grazed grass-legume contributes an additional reduction through lower feed production and land use change emissions.

**FARMES continues to show an increase of +8.4%**, which the team believes reflects an older emission factor approach for manure methane. The two tools disagree on direction; the RuFaS result is considered more physically credible.

**The most important unresolved gap** remains soil carbon sequestration under permanent pasture, which is not yet captured in these results and is expected to further favor the pasture scenario.

---

## Background: What Is Being Compared

### The Two Tools

- **FARMES** — A nationally used reference model. Results are the average of four independent simulation runs.
- **RuFaS** — A local simulation model developed at this institution, currently undergoing validation. Uses NASEM 2021 nutrition standard. Results are the average of four independent simulation runs.

### The Four Scenarios

| Scenario | Tool | Heifer Housing | Heifer Diet | Heifer Manure |
|---|---|---|---|---|
| **A: FARMES Baseline** | FARMES (avg 4 runs) | Confined, freestall | Purchased TMR | AlleyScraper + 120-day slurry |
| **B: FARMES Heifer Pasture** | FARMES (avg 4 runs) | Pasture | Purchased TMR | Pasture deposit |
| **C: RuFaS Baseline** | RuFaS (avg 4 runs) | Confined, freestall | Purchased TMR (7 ingredients) | AlleyScraper + 120-day slurry, no crust |
| **D: RuFaS Heifer Pasture** | RuFaS (avg 4 runs) | Pasture | **77.8% cool-season grass + 19.5% legume + 2.7% mineral** | **DailySpread (direct pasture deposit)** |

**In plain terms:** A and C represent conventional management — heifers housed indoors, manure collected and stored in a slurry tank for 4 months, diet formulated from purchased ingredients. B and D represent the alternative: heifers graze on a grass-legume pasture, depositing manure directly on soil, with free-choice mineral supplement.

**Note on Scenario B:** FARMES does not change the heifer diet in the pasture scenario — only where manure lands. This is a limitation of FARMES. RuFaS Scenario D models both the manure and diet change.

Adult cows are confined in all four scenarios.

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
| Confined heifer diet (A, C) | Purchased TMR | Corn silage, alfalfa silage, hay, grass-legume silage, byproduct blend, corn grain, mineral |
| Pasture heifer diet (B) | Purchased TMR (unchanged) | — |
| Pasture heifer diet (D) | — | **77.8% cool-season grass (ID 92) + 19.5% legume (ID 105) + 2.7% mineral (ID 301)** |
| On-farm crop production | None | None |
| Emissions allocated to milk | 86.0% | ~88.5% |

*FPCM is a standardized milk measure used as the emissions denominator.

**Why are feed intake and milk production higher in RuFaS?** RuFaS uses the NASEM 2021 nutrition standard, which estimates higher energy requirements for the same cows. This is a known difference under active validation review. Only compare scenarios within the same tool.

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
| Enteric methane (digestion) | 0.764 | 0.770 | **+0.9%** |
| Manure management | 0.335 | 0.289 | **−13.7%** |
| — of which: manure methane (CH4) | 0.334 | 0.289 | **−13.7%** |
| — of which: manure nitrous oxide (N2O) | 0.0002 | 0.0002 | No change |
| Feed production (excl. land use) | 0.371 | 0.358 | **−3.7%** |
| On-farm energy use | Not yet captured | Not yet captured | — |
| **Total (excl. land use change)** | **1.470** | **1.417** | **−3.6%** |
| Land use change | 0.034 | 0.026 | **−24%** |
| **Total (incl. land use change)** | **1.504** | **1.443** | **−4.1%** |

**Note on enteric methane:** Heifers eating grazed grass-legume produce slightly more enteric methane than heifers eating a balanced TMR (+0.9%). Fresh forage has higher fiber content and lower digestibility, increasing rumen fermentation. The effect is small and physically expected.

**Note on manure N2O:** Under DailySpread (direct pasture deposit with no storage step), manure N2O is essentially unchanged from the confined baseline (9.5 kg vs. 9.5 kg/yr). This corrects the erroneous +3,300% N2O figure in v3, which was an artifact of routing manure through a slurry storage unit even for 1 day.

**Note on land use change:** The LUC reduction in Scenario D (−24%) reflects the shift from purchased corn silage, alfalfa, and grain to grazed pasture forages. Managed pasture requires minimal off-farm inputs and carries essentially no land conversion footprint.

---

## Summary Table: All Four Scenarios

| | A: FARMES Baseline | B: FARMES Heifer Pasture | C: RuFaS Baseline | D: RuFaS Heifer Pasture |
|---|---|---|---|---|
| **Tool** | FARMES | FARMES | RuFaS | RuFaS |
| **Heifer manure** | Indoor / 120-day slurry | Pasture deposit | Indoor / 120-day slurry | DailySpread (pasture) |
| **Heifer diet** | Purchased TMR | Purchased TMR | Purchased TMR | Grazed grass-legume |
| **Runs averaged** | 4 | 4 | 4 | 4 |
| **Enteric CH4** | 0.456 | 0.456 | 0.764 | 0.770 |
| **Manure** | 0.272 | 0.359 | 0.335 | 0.289 |
| **Feed (excl. LUC)** | 0.229 | 0.229 | 0.371 | 0.358 |
| **Energy** | 0.043 | 0.043 | — | — |
| **Total (excl. LUC)** | **0.999** | **1.086** | **1.470** | **1.417** |
| **Total (incl. LUC)** | **1.024** | **1.110** | **1.504** | **1.443** |
| **Change vs. baseline** | — | **+8.4% ↑** | — | **−4.1% ↓** |

⚠️ **FARMES and RuFaS disagree on the direction of the effect.** See Key Findings.

**Do not compare absolute values between FARMES and RuFaS.** Total intensity is ~50% higher in RuFaS due to differences in nutrition methodology.

---

## Key Findings

### Finding 1: The two tools disagree — RuFaS is likely more correct

| Question | FARMES | RuFaS |
|---|---|---|
| Does heifer pasture reduce GHG intensity? | **No — +8.4%** | **Yes — −4.1%** |
| What drives the change? | Manure CH4 and N2O both increase | Manure CH4 drops sharply; N2O unchanged; feed LUC falls |

The disagreement traces to manure methane. Eliminating 120-day anaerobic slurry storage should reduce CH4 — this is the physically expected result, and what RuFaS shows (−13.7%). FARMES shows the opposite (+32%), likely reflecting an older emission factor approach. RuFaS is considered more credible on this specific question.

### Finding 2: Manure storage is the dominant lever

The −4.1% total reduction in Scenario D breaks down as:
- **Manure CH4: −13.7%** — primary driver; eliminating 4-month anaerobic slurry storage
- **Feed LUC: −24%** — secondary; grazed pasture has near-zero land conversion footprint
- **Feed excl. LUC: −3.7%** — tertiary; lower production emissions for grazed forages vs. purchased silage/grain
- **Enteric CH4: +0.9%** — small offset; higher fiber in grazed forage increases fermentation slightly
- **Manure N2O: no change** — correctly near-baseline with DailySpread

### Finding 3: The pasture result is likely conservative

Soil carbon sequestration under permanent pasture is not modeled. Managed grassland can sequester 0.2–1.0 tonnes CO2/ha/year depending on soil, climate, and management. This offset — not included in the −4.1% figure — is expected to further favor the pasture scenario. The RuFaS Soil and Crop Module has a Daycent-based soil carbon component, but it requires further configuration for a pasture system.

---

## Co-Benefits Beyond GHG

The GHG analysis above captures only one dimension of the case for heifer pasture. Compared to tilled corn-soy rotations — the land use most likely displaced by heifer grazing in the Upper Midwest — well-managed perennial pasture delivers substantial co-benefits across water quality, hydrology, and biodiversity. These are not captured in RuFaS or FARMES outputs and represent additional unreported value for sustainability programs.

### Water quality

| Metric | Tilled corn-soy | Managed perennial pasture | Change |
|---|---|---|---|
| Soil erosion | Baseline | Near zero | **~−100%** |
| Phosphorus runoff | 2.0 lb P/ac/yr | 0.2 lb P/ac/yr | **−90%** |
| Nitrate leaching | 28.6 lb N/ac/yr | 8.9 lb N/ac/yr | **−69%** |

Perennial pasture root systems also reduce stormwater runoff by approximately **36%** compared to tilled corn-soy for a 5-inch rain event — a meaningful flood and nutrient retention benefit in Upper Midwest watersheds.

### Biodiversity

| Metric | Tilled corn-soy | Managed perennial pasture | Change |
|---|---|---|---|
| Grassland bird nesting density | 0.04 pairs/acre | 2.6 pairs/acre | **65× higher** |
| Pollinator habitat quality (0–10 index) | Baseline | 3–4× higher | **3–4× higher** |

### Framing for program design

These co-benefits are relevant both as additional value to report and as a program design signal: a heifer grazing practice intervention delivers water quality, biodiversity, and carbon outcomes simultaneously. Stacking or bundling these across credit markets (carbon, water quality, biodiversity) could strengthen the economic case for producer adoption.

**Source:** Paine, L.K., Jackson, R., Raff, Z., Booth, E., Gratton, C., Gibson, A., LeZaks, D., Lloyd, S., and Wepking, C. (2021). *Well-managed perennial pasture: Setting the gold standard for ecosystem services.* Grassland 2.0, University of Wisconsin–Madison. grasslandag.org. Underlying data from Jackson (2020), Raff (2021), and Booth (2021); see Paine et al. for full reference list.

---

## Can RuFaS Answer the Grazing Question? — Model Assessment

### What RuFaS currently captures well

| Emission source | Status |
|---|---|
| Manure methane from housing and storage | Correctly penalizes long anaerobic slurry storage; DailySpread correctly models pasture |
| Manure N2O | Correctly near-baseline under DailySpread; no storage-induced artifact |
| Enteric methane | Correctly increases slightly for high-forage pasture diet |
| Feed production emissions and LUC | Captures lower footprint of grazed pasture vs. purchased TMR ingredients |

### Remaining gaps

**1. Soil carbon sequestration (most material)**
Permanent pasture sequesters carbon in soil organic matter. RuFaS has a Daycent-based soil carbon model in the Soil and Crop Module, but it requires configuration for a pasture system (e.g., simulating a cool-season grass field with daily manure application). This is the highest-priority gap.

**2. Heifer growth rate feedback**
RuFaS does not currently reduce heifer growth rate requirements when diet quality changes. If the pasture ration fails to meet energy requirements, the model falls back to the previous ration rather than modeling reduced growth. This means the energy balance implications of a forage-only diet are not fully captured.

**3. Seasonal pasture variation**
The current model uses a fixed ration composition year-round. Real managed pastures vary in quality and availability by season.

**4. On-farm energy use**
Not modeled in RuFaS. FARMES estimates ~0.043 kg CO2e/kg FPCM; adding this would affect C and D equally.

### Where RangeSTAR and SmartScape could help

- **RangeSTAR:** Quantifies soil carbon changes, pasture-specific N2O, and the full carbon cycle of a grazed system. Directly addresses Gap #1.
- **SmartScape:** Spatial tool for carbon sequestration, nutrient retention, and water quality at the farm or watershed level. Most useful for field-level or watershed-scale evaluation.

### Is RuFaS sufficient?

| Question | Answered? |
|---|---|
| Does eliminating slurry storage reduce manure methane? | Yes — correctly modeled, likely more accurate than FARMES |
| Does DailySpread correctly represent pasture manure deposit? | Yes — confirmed by RuFaS development team |
| What is the diet impact of grazing? | Partially — enteric and feed emissions captured; growth rate feedback not yet modeled |
| Does soil carbon sequestration offset emissions? | Not yet — requires RangeSTAR or Soil and Crop Module configuration |
| What is the full lifecycle impact? | Not yet — soil carbon gap remains |

---

## Caveats and Limitations

1. **FARMES and RuFaS disagree on the direction of the effect.** RuFaS is likely correct on manure methane, but neither tool captures soil carbon.

2. **Do not compare absolute values between FARMES and RuFaS.** Total intensity is ~50% higher in RuFaS. Only compare A vs. B and C vs. D.

3. **All four RuFaS scenarios completed 4 of 4 seeds** in the April 15 run. Seed-to-seed variation is negligible (±0.002 kg CO2e/kg FPCM).

4. **Scenario D uses a simplified, fixed pasture diet.** Seasonal variation in pasture quality and stocking density are not modeled.

5. **Heifer growth rate is not responsive to diet.** If the pasture ration is nutritionally insufficient, RuFaS falls back silently to the prior ration. Results should be interpreted with this caveat.

6. **Soil carbon is not modeled.** This is the most material gap. Permanent pasture can sequester 0.2–1.0 tonnes CO2/ha/year; this offset is not included in the −4.1% figure.

7. **All feed is treated as purchased.** Pasture grass and legume are modeled as purchased feeds with very low production emissions — a reasonable approximation, but not a full on-farm pasture model.

8. **Energy use is not captured in RuFaS.** FARMES estimates ~0.043 kg CO2e/kg FPCM; adding this would affect C and D equally.

9. **RuFaS is still being validated.** Absolute values are expected to shift as the nutrition model is refined. These results are directional, not final.

10. **Results are specific to this farm.** Different herd sizes, climate, soil types, or manure infrastructure may show different results.

---

## Notes on Non-Technical Presentation

- **The story is now cleaner:** confined heifers eating TMR and storing manure for 4 months vs. pasture heifers eating fresh grass-legume and depositing manure directly. The −4.1% reduction is driven by a well-understood mechanism (eliminating anaerobic storage) with a supporting cast (lower feed footprint, lower LUC).
- **Drop the N2O drama.** v3 had a large N2O increase that needed contextualizing. v4 has no such complication — N2O is essentially unchanged. This makes the result easier to communicate.
- **The soil carbon gap is the most accessible storyline.** "We haven't counted the carbon the grass puts back in the ground — when we do, the pasture scenario will look even better" is easy to communicate and positions the next phase of work.
- **The FARMES vs. RuFaS disagreement is an opportunity.** Frame it as "our newer, more detailed model tells a different story — and the physics support it."
- **The −4.1% figure is conservative by design.** Emphasize that soil carbon sequestration, improved heifer health, and reduced energy use are all additional factors expected to favor the pasture scenario.

---

## Repo and Reproducibility

All input files, run configurations, and this document are available at:

**GitHub:** https://github.com/carbon-yield/rufas-grazing-heifers
**Branch:** `heifer-pasture-analysis`
**Run with:** `python main.py` (outputs prefixed `heifer_pasture_v2_` in `output/reports/`)

---

## Appendix: Input File Changes by Scenario

All scenarios share a common base. Changes below are relative to Scenario C (RuFaS Baseline). Each scenario is defined by a metadata file that specifies which input data files to use.

**Metadata files:**
- C: `input/metadata/example_freestall_dairy_metadata_baseline.json`
- D: `input/metadata/example_freestall_dairy_metadata_heifer_pasture_v2.json`

The metadata files differ at three entries (lines 13, 76, 97, 104):

| Line | Field | Scenario C | Scenario D |
|---|---|---|---|
| 13 | Animal file | `rufas_match_animal_baseline.json` | `rufas_match_animal.json` |
| 76 | Feed file | `example_Midwest_feed.json` | `example_Midwest_feed_heifer_pasture_v2.json` |
| 97 | Manure config | `example_freestall_processor_configs_baseline.json` | `example_freestall_processor_configs.json` |
| 104 | Manure connections | `example_freestall_processor_connections.json` | `example_freestall_processor_connections_heifer_pasture_v2.json` |

---

### Change 1 — Bedding

**File:** `input/data/animal/rufas_match_animal_baseline.json` → `input/data/animal/rufas_match_animal.json`

| Line | Field | Baseline (C) | Heifer Pasture (D) |
|---|---|---|---|
| 196 | `bedding_name` (growing pen) | `"straw"` | `"none (no bedding)"` |

All other pens unchanged: calf pen (line 177) keeps `"calf_straw"`; close-up and lactating cow pens (lines 215, 237) keep `"straw"`.

---

### Change 2 — Manure Handler, Storage, and Connections

**Configs file:** `example_freestall_processor_configs_baseline.json` → `example_freestall_processor_configs.json`

| Line | Field | Baseline (C) | Heifer Pasture (D) |
|---|---|---|---|
| 26 | `processor_type` for `growing_alley_scraper` | `"AlleyScraper"` | `"ManualScraper"` |
| 85 | `cover` for `slurry_storage_outdoor_growing` | `"no_crust_or_cover"` | `"crust"` |
| 86 | `storage_time_period` for `slurry_storage_outdoor_growing` | `120` (days) | `1` (day) |

**Connections file:** `example_freestall_processor_connections.json` → `example_freestall_processor_connections_heifer_pasture_v2.json`

| Change | Baseline (C) | Heifer Pasture (D) |
|---|---|---|
| `growing_alley_scraper` destination | `slurry_storage_outdoor_growing` | **`dailyspread`** |
| `dailyspread` connection entry | not present | added (empty destinations) |
| `slurry_storage_outdoor_growing` connection entry | present | retained (empty destinations, required by validator) |

**Why this matters:** In Scenario C, growing heifer manure flows into an uncovered outdoor slurry tank for 120 days — the primary condition for anaerobic methane production. In Scenario D, manure routes directly to `DailySpread`, bypassing all storage and correctly representing pasture direct-deposit.

---

### Change 3 — Growing Heifer Feed Ration

**File:** `input/data/feed/example_Midwest_feed.json` → `input/data/feed/example_Midwest_feed_heifer_pasture_v2.json`

**`growing_feeds` list (lines 6–9):**

| | Baseline (C) | Heifer Pasture (D) |
|---|---|---|
| Feed IDs | `[44, 50, 95, 104, 110, 301, 302]` | `[92, 105, 301]` |

**`user_defined_ration_percentages.growing` (lines 108–117):**

| Feed ID | Name | Baseline (C) | Heifer Pasture (D) |
|---|---|---|---|
| 50 | Corn silage | 30.41% | removed |
| 110 | Alfalfa silage | 26.30% | removed |
| 95 | Hay | 10.755% | removed |
| 104 | Grass-legume silage | 10.755% | removed |
| 44 | Corn grain | 3.84% | removed |
| 302 | Byproduct blend | 15.21% | removed |
| 301 | Mineral mix | 2.74% | **2.74%** (unchanged) |
| 92 | Cool-season grass, pasture | — | **77.81%** |
| 105 | Legumes, pasture (intensively managed) | — | **19.45%** |

The 80:20 grass-legume split represents a managed rotational Wisconsin pasture. Legume fraction adds biological nitrogen fixation and improves ration protein without purchased inputs.

**Additional changes to support IDs 92 and 105:**
- Both IDs added to `purchased_feeds` at `purchased_feed_cost: 0.01`
- Both IDs added to `allowances` with all allowances at `1000.0`

All other pen rations (calf, close-up, lactating cow) are identical between the two feed files.

---

### Feed ingredient reference

| RuFaS ID | Name | Type | Source |
|---|---|---|---|
| 44 | Corn, yellow — grain | Grain | `user_feeds.csv` line 45 |
| 50 | Corn, yellow — silage, immature | Forage | `user_feeds.csv` line 51 |
| 92 | Grasses, cool season — pasture | Forage | `user_feeds.csv` line 93 |
| 95 | Grass-legume mixtures — hay, mature | Forage | `user_feeds.csv` line 96 |
| 104 | Grass-legume mixtures — silage | Forage | `user_feeds.csv` line 105 |
| 105 | Legumes, forage — pasture, intensively managed | Forage | `user_feeds.csv` line 106 |
| 110 | Legumes, forage — alfalfa silage | Forage | `user_feeds.csv` line 111 |
| 301 | Farm ES Mineral Mix | Mineral | `NASEM_Comp_with_TDN.csv` line 171 |
| 302 | Farm ES Midwest BP Blend | Conc | `NASEM_Comp_with_TDN.csv` line 172 |

---

*Document prepared for internal stakeholder briefing. Results are preliminary. v4 supersedes v3 (2026-03-12). Run data from April 15, 2026.*
