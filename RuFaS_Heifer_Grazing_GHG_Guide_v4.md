# Quantifying GHG Impacts of Dairy Heifer Grazing in RuFaS
## A Guide for Carbon Programs, Corporate Sustainability Professionals, and Co-Ops

**Project:** Scaling Dairy Heifer Grazing: Engaging Market Actors and Ecosystem Services Value Chains
**Partners:** Carbon Yield & Grassland 2.0
**Funding:** Rural Climate Partners ($75,000)
**Analysis completed:** April 2026
**Repo:** https://github.com/carbon-yield/rufas-grazing-heifers (branch: `heifer-pasture-analysis`)

---

**Who This Guide Is For:** Carbon program staff and corporate sustainability professionals — co-op sustainability teams, Scope 3 program designers, and MRV methodology developers — who need to understand whether and how heifer grazing can be quantified as a GHG-reduction practice using industry-standard whole-farm models.

**What It Covers:** What we tested, what the model returned, what drove the result, what the model cannot capture, and how to reproduce the analysis.

**What It Isn't:** A claim that heifer grazing definitively reduces GHG intensity. It is an honest account of what the best available whole-farm tool currently shows — and what that means for program design.

---

## What Changed from v1 (March 2026)

| Item | v1 | v2 |
|---|---|---|
| Modeling method for pasture manure | Legacy workaround (manure briefly routed through storage) | **Correct method: DailySpread (direct pasture deposit, no storage)** |
| Heifer pasture diet | Pure cool-season grass (97.3%) | **Realistic 80:20 grass-legume mix** |
| Reported GHG reduction | −2.9% | **−4.1%** |
| Confirmed by RuFaS team | No | **Yes — GitHub discussion #2941** |

**The most important change:** The v2 manure methodology was confirmed correct by the RuFaS development team (DailySpread, bypassing storage entirely), and the pasture diet was updated to a realistic 80:20 grass-legume mix. Both changes produce a larger and cleaner reduction than v1.

---

## Background: Why Model Heifer Grazing?

Dairy sustainability programs increasingly promote heifer grazing as a land-use intervention. Evidence suggests that raising dairy replacement heifers on well-managed pasture can improve farm economics, water quality, and biodiversity. However, formal eligibility in GHG incentive programs requires quantified emission reductions using recognized tools.

**FARM-ES v3** is the dominant tool used by U.S. dairy co-ops and processors for Scope 3 GHG accounting. It runs on the **RuFaS** (Ruminant Farm Systems) simulation engine developed by Cornell University and NMPF. This project set out to model heifer grazing scenarios directly in RuFaS to understand what the model returns and why.

---

## The Four Scenarios

We modeled a representative Wisconsin freestall dairy (1,000 milking cows) under four scenarios. Adult cows are confined in all scenarios. Only the growing heifer enterprise changes.

| Label | Name | Tool | Heifer Housing | Heifer Diet | Heifer Manure |
|---|---|---|---|---|---|
| A | FARMES Baseline | FARMES | Confined | Purchased TMR | — |
| B | FARMES Heifer Pasture | FARMES | Pasture | Purchased TMR (unchanged) | Pasture deposit |
| C | RuFaS Baseline | RuFaS | Confined | Purchased TMR (7 ingredients) | AlleyScraper + 120-day slurry, no crust |
| D | RuFaS Heifer Pasture | RuFaS | Pasture | **80:20 grass-legume mix (ID 92: 77.8% + ID 105: 19.5% + ID 301: 2.7%)** | **DailySpread (direct pasture deposit, no storage)** |

**Note on Scenario B:** FARMES does not change the heifer diet in the pasture scenario — only where the manure lands. This understates the diet-related benefits of pasture and is a known limitation of the tool. RuFaS Scenario D models both changes.

In plain terms: A and C represent conventional management — heifers housed indoors, manure collected and stored in a slurry tank for 4 months, diet formulated from purchased ingredients. B and D represent the alternative: heifers graze a managed grass-legume pasture and deposit manure directly on soil.

---

## Key Results (April 2026 Run)

GHG intensity in kg CO₂e per kg Fat- and Protein-Corrected Milk (FPCM). **Lower is better.**

### RuFaS (Scenarios C and D)

| Scenario | Incl. LUC | Excl. LUC | vs. Baseline (incl. LUC) |
|---|---|---|---|
| C — RuFaS Baseline | 1.504 | 1.470 | — |
| D — RuFaS Heifer Pasture | **1.443** | **1.417** | **−4.1%** |

### FARMES (Scenarios A and B)

| Scenario | Incl. LUC | Excl. LUC | vs. Baseline (incl. LUC) |
|---|---|---|---|
| A — FARMES Baseline | 1.024 | 0.999 | — |
| B — FARMES Heifer Pasture | 1.110 | 1.086 | +8.4% |

**FARMES and RuFaS disagree on the direction of the effect.** See below.

> **Do not compare absolute values between FARMES and RuFaS.** Total intensity is ~50% higher in RuFaS due to differences in nutrition methodology (NASEM 2021 vs. older standards). Only compare A vs. B and C vs. D.

---

## Detailed Component Breakdown (RuFaS C vs. D)

| Emission Source | C: Baseline | D: Heifer Pasture | Change |
|---|---|---|---|
| Enteric methane | 0.764 | 0.770 | +0.9% |
| Manure CH4 | 0.334 | 0.289 | **−13.7%** |
| Manure N2O | 0.0002 | 0.0002 | No change |
| Feed production (excl. LUC) | 0.371 | 0.358 | −3.7% |
| Land use change | 0.034 | 0.026 | **−24%** |
| **Total (incl. LUC)** | **1.504** | **1.443** | **−4.1%** |

---

## What Drove the Reduction — and What Didn't

### The primary driver is the manure system, not the feed

The −4.1% reduction is primarily attributable to the change in heifer manure management:

- **Baseline (C):** Growing heifer manure is handled by an AlleyScraper and stored in an outdoor slurry pit for 120 days with no crust or cover, generating substantial methane from anaerobic decomposition during storage.
- **Pasture (D):** Heifers deposit manure directly on pasture. This is modeled using **DailySpread** — the correct v1.0 RuFaS processor for direct pasture deposition — which routes manure to the field without any storage step.

Switching from 120-day uncovered slurry storage to direct pasture deposition is the dominant signal. The secondary contribution comes from land use change: grazed grass-legume pasture carries near-zero land conversion footprint compared to purchased corn silage, alfalfa, and grain.

### Enteric methane ticks slightly upward

Heifer enteric methane increases by approximately +0.9% in Scenario D. This result is expected: pasture forage (cool-season grass + legume) is higher in fiber than the baseline TMR, which increases methanogenesis per unit of feed consumed. The manure savings of grazing heifers more than offset the small increase in enteric methane.

### What this means for program design

**Manure savings are the strongest quantifiable benefit from grazing heifers.** The quantifiable benefit in RuFaS comes from the manure system change — heifer grazing enables direct-deposition management, eliminating methane emissions from stored manure. Programs that focus only on feed change will not capture the primary mechanism.

The secondary benefit — land use change reduction from shifting heifers off purchased corn and alfalfa — is real and captured, but smaller than the manure pathway.

### Why the two tools disagree

FARMES shows +8.4%; RuFaS shows −4.1%. The disagreement is centered on manure methane. Eliminating 120-day anaerobic storage should reduce CH4 — this is the physically expected result, confirmed by the RuFaS result (−13.7%). FARMES shows the opposite (+32%), likely reflecting an older emission factor approach. **The RuFaS result is considered more physically credible for this specific question.**

---

## What RuFaS Does Not Capture — Critical Caveats

These limitations are significant and must be disclosed in any program materials citing this analysis.

### 1. No dedicated grazing module

RuFaS does not simulate the grazing process itself — paddock rotation, forage growth, grazing behavior, or pasture-specific nutrient cycling. We modeled the pasture scenario by substituting a grass-legume pasture ration (IDs 92 + 105 + 301) as the feed input and using the DailySpread processor for manure. The Cornell/RuFaS team has acknowledged this limitation. A grazing module is on their long-term roadmap.

### 2. Steady-state assumption — no soil organic carbon

RuFaS initializes a herd at steady state and simulates forward from that starting point. It does not model soil carbon dynamics. **Soil organic carbon (SOC) sequestration is widely cited as one of the most significant long-term climate benefits of converting cropland to managed pasture,** with estimates ranging from −11% (Cool Farm Tool) to −55% (IFSM, per-acre accounting) in other models. RuFaS returns none of this benefit. The −4.1% result is a lower bound of what RuFaS can see, not a complete picture of the practice's climate value.

### 3. No on-farm land-use conversion benefit

The model does not account for the long-term carbon dynamics of converting corn/soy acres to perennial pasture. LUC figures in the results above reflect purchased feed LUC only — the emissions avoided by not buying corn silage and alfalfa — not the on-farm land conversion benefit.

### Summary table

| What RuFaS captures | What RuFaS misses |
|---|---|
| Enteric methane from feed | Soil organic carbon sequestration |
| Manure storage CH4 and N2O | Pasture-specific nutrient cycling |
| Purchased feed LUC | On-farm land-use conversion benefits |
| Direct pasture deposition (DailySpread) | Native grazing behavior / paddock dynamics |

### How to communicate results responsibly

When sharing these results with co-op partners, brands, or program administrators, we recommend the following framing:

> "RuFaS modeling of a representative Wisconsin dairy shows heifer grazing reduces GHG intensity by approximately 4%, driven primarily by eliminating 4-month anaerobic manure storage. This is likely a lower bound: RuFaS does not model soil carbon sequestration, which other tools suggest could represent an additional 10–50% reduction depending on land-use baseline and time horizon. Programs seeking to credit heifer grazing should consider how to account for both manure and soil carbon benefits."

---

## Context: How RuFaS Results Compare to Other Models

RuFaS is not the only tool used to estimate heifer grazing GHG impacts. The range of estimates across tools is wide and reflects genuine differences in accounting boundaries and model capabilities — not just parameter choices.

| Model | Estimated reduction | Accounting method | Notes |
|---|---|---|---|
| Cool Farm Tool | ~11% | Carbon intensity (per kg milk) | Includes SOC; primarily European farming contexts |
| Randy Jackson (literature) | ~25% | Per-acre accounting | Includes soil carbon; different boundary than intensity |
| IFSM | ~55% | Carbon intensity (per kg milk) | Includes SOC and full land-use change |
| **RuFaS (this analysis)** | **~4%** | **Carbon intensity (per kg FPCM)** | **No SOC; no dedicated grazing module** |

RuFaS returns the most conservative figure because it does not model soil carbon — the mechanism most responsible for the larger estimates in other tools. This does not mean RuFaS is wrong; it is modeling what it can see. The −4.1% figure represents what is currently verifiable and reproducible using the industry's standard tool.

---

## Co-Benefits Beyond GHG

The GHG analysis above captures only one dimension of the case for heifer pasture. Compared to tilled corn-soy rotations — the land use most likely displaced by heifer grazing in the Upper Midwest — well-managed perennial pasture delivers substantial additional benefits across water quality, hydrology, and biodiversity. None of these are captured in RuFaS or FARMES outputs.

### Water quality and hydrology

| Metric | Tilled corn-soy | Managed perennial pasture | Change |
|---|---|---|---|
| Soil erosion | Baseline | Near zero | **~−100%** |
| Phosphorus runoff | 2.0 lb P/ac/yr | 0.2 lb P/ac/yr | **−90%** |
| Nitrate leaching | 28.6 lb N/ac/yr | 8.9 lb N/ac/yr | **−69%** |
| Stormwater runoff (5-inch event) | Baseline | −36% | **−36%** |

Perennial root systems maintain year-round soil structure, dramatically reducing the volume and nutrient load of runoff — a material benefit in Upper Midwest watersheds where phosphorus and nitrate loading are ongoing concerns.

### Biodiversity

| Metric | Tilled corn-soy | Managed perennial pasture | Change |
|---|---|---|---|
| Grassland bird nesting density | 0.04 pairs/acre | 2.6 pairs/acre | **65× higher** |
| Pollinator habitat quality (0–10 index) | Baseline | 3–4× higher | **3–4× higher** |

### Why this matters for program design

These co-benefits represent additional unreported value in the GHG-only analysis. A heifer grazing practice intervention delivers water quality, biodiversity, and carbon outcomes simultaneously. Programs that can stack or bundle these across markets (carbon, water quality, biodiversity offsets) will present a much stronger economic case to producers than a GHG-only framing.

**Source:** Paine, L.K., Jackson, R., Raff, Z., Booth, E., Gratton, C., Gibson, A., LeZaks, D., Lloyd, S., and Wepking, C. (2021). *Well-managed perennial pasture: Setting the gold standard for ecosystem services.* Grassland 2.0, University of Wisconsin–Madison. grasslandag.org. Underlying data from Jackson (2020), Raff (2021), and Booth (2021).

---

## What's Next

This analysis establishes that heifer grazing produces a measurable, directionally consistent GHG reduction in RuFaS (~4%), identifies the manure management pathway as the mechanism RuFaS can currently quantify, and makes clear what the tool cannot yet see. Programs seeking to credit heifer grazing formally should consider the following paths forward:

1. **Use RuFaS/FARM-ES for manure pathway credit.** The ~4% reduction is real and reproducible. Programs can credit the manure management benefit now, subject to the caveats above.

2. **Engage the RuFaS team on a grazing module.** Cornell and NMPF are aware of the model limitations. A dedicated grazing module capturing direct deposition, pasture nutrient cycling, and forage production dynamics would substantially improve the model's ability to represent this practice. We have initiated outreach via the RuFaS GitHub discussion board (discussion #2941).

3. **Consider a complementary SOC accounting method.** Programs that want to credit the full land-use benefit should use a supplementary SOC quantification method (e.g., RangeSTAR/RCTM, IFSM, or a literature-based emission-factor approach) in conjunction with RuFaS results to capture what RuFaS cannot currently see.

---

## How to Reproduce This Analysis

Full step-by-step instructions are in `RuFaS_Heifer_Grazing_Reproduction_Guide.md` in the same repository. Quick version:

```bash
git clone https://github.com/carbon-yield/rufas-grazing-heifers.git
cd rufas-grazing-heifers
git checkout heifer-pasture-analysis
pip install -r requirements.txt
python main.py input/data/tasks/example_freestall_task.json
```

Reports appear in `output/reports/` as CSVs prefixed `baseline_` (Scenario C) or `heifer_pasture_v2_` (Scenario D).

A successful run should return Scenario D at approximately **1.443 kg CO₂e/kg FPCM (incl. LUC)** and **1.417 excl. LUC**. All 4 seeds should complete. Occasional single-seed failure on the baseline run is a known race condition and does not affect the result.

---

## Questions and Reuse

This analysis is open-source. All model inputs, configuration files, and this guide are available at:
**https://github.com/carbon-yield/rufas-grazing-heifers** (branch: `heifer-pasture-analysis`)

For questions about this analysis: Carbon Yield
For questions about the RuFaS model itself: Cornell PRO-DAIRY / NMPF FARM program

---

## Key Terms

- **GHG intensity** — emissions per unit of output (here, per kg of milk), vs. total emissions
- **LUC (Land Use Change)** — emissions from converting land from one use to another
- **Soil Organic Carbon (SOC)** — the carbon stored in soil; the big mechanism RuFaS cannot currently see
- **Methanogenesis** — the biological process that produces methane in the gut and in manure storage
- **Direct deposition** — manure deposited straight onto pasture vs. collected and stored
- **DailySpread** — the RuFaS v1.0 processor that correctly models direct pasture deposition by routing manure to the field with no storage step
- **Scope 3 emissions** — indirect emissions in a company's supply chain (i.e., what co-ops are accounting for)
- **RuFaS** — Ruminant Farm Systems; the underlying simulation engine developed by Cornell University and NMPF
- **FARM-ES** — the co-op-facing GHG accounting tool that runs on RuFaS
- **Process-based model** — a model that simulates biological and chemical processes vs. using emission factor averages
- **Steady-state assumption** — the model starts at equilibrium and does not account for change over time (e.g., soil carbon buildup)
- **MRV** — Monitoring, Reporting, and Verification; standard carbon program language
- **FPCM (Fat and Protein Corrected Milk)** — the standardized milk measure used as the emissions denominator to compare across farms
- **TMR (Total Mixed Ration)** — the conventional confined feeding approach being compared against pasture
- **Slurry storage** — liquid manure storage; the primary emissions source the model captures
- **Cool-season grass (ID 92)** — RuFaS's perennial cool-season grass entry; the pasture grass proxy used in this model. Represents managed rotational pasture grass in Wisconsin conditions.
- **Legumes, pasture (ID 105)** — RuFaS's intensively managed pasture legume entry; added in v2 to represent a realistic grass-legume mixed sward

---

*v2 — April 2026. Supersedes v1 (March 2026).*
*GitHub: https://github.com/carbon-yield/rufas-grazing-heifers | Branch: heifer-pasture-analysis*
