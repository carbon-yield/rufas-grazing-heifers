# Heifer Pasture GHG Analysis — Internal Technical Guide
## RuFaS Implementation, Methodology, and Current State

**Version:** v2 (April 2026)
**Previous version:** v1 (March 2026) — superseded
**Audience:** Analysts, modelers, and future maintainers of this analysis
**Branch:** `heifer-pasture-analysis` of https://github.com/carbon-yield/rufas-grazing-heifers

---

## What Changed from v1

| Item | v1 | v2 |
|---|---|---|
| Pasture manure handler | `ManualScraper` + `slurry_storage_outdoor_growing` with 1-day storage / crust | **`DailySpread`** — confirmed correct v1.0 approach (RuFaS team, GitHub #2941) |
| Pasture heifer diet | ID 92 only (97.3% cool-season grass) | **80:20 grass-legume: ID 92 (77.81%) + ID 105 (19.45%) + ID 301 (2.74%)** |
| Connections file | Reused baseline connections | **New file:** `example_freestall_processor_connections_heifer_pasture_v2.json` |
| GHG intensity incl. LUC | 1.461 | **1.443** |
| GHG intensity excl. LUC | 1.437 | **1.417** |
| Change vs. baseline | −2.9% | **−4.1%** |
| Manure N2O | Reported +3,300% increase — stated as "physically correct" | **Retracted — artifact of slurry workaround; corrected to near-baseline (unchanged)** |
| Seeds completed (Scenario D) | 3 of 4 | **4 of 4** |
| Output prefix | `heifer_pasture_feed_` | **`heifer_pasture_v2_`** |

---

## Section 1 — Analysis Scenarios

### Scenario C: RuFaS Baseline

- Metadata: `input/metadata/example_freestall_dairy_metadata_baseline.json`
- Heifers confined in freestall, bedded with straw
- Growing pen manure: AlleyScraper → 120-day outdoor slurry, no crust
- Growing heifer diet: 7-ingredient purchased TMR (corn silage, alfalfa silage, hay, grass-legume silage, corn grain, byproduct blend, mineral)
- Output prefix: `baseline_`

### Scenario D: RuFaS Heifer Pasture (current final scenario)

- Metadata: `input/metadata/example_freestall_dairy_metadata_heifer_pasture_v2.json`
- Heifers on pasture, no bedding
- Growing pen manure: routed directly to `DailySpread` — no storage
- Growing heifer diet: 80:20 grass-legume (ID 92: 77.81% + ID 105: 19.45% + ID 301: 2.74%)
- Output prefix: `heifer_pasture_v2_`

### Intermediate scenarios (not used in final comparison)

- `heifer_pasture_` — feed only, no manure change (output prefix: `heifer_pasture_`)
- `heifer_pasture_feed_` — feed change + legacy ManualScraper workaround (output prefix: `heifer_pasture_feed_`)

These are included in the task file and output directory for reference but are **not** part of the C vs. D comparison.

---

## Section 2 — Input Files Changed Between C and D

All four changes are tracked in the metadata file diff between Scenario C and Scenario D metadata files.

### 2.1 Animal file — bedding change

| File | Baseline (C) | Heifer Pasture (D) |
|---|---|---|
| Animal config | `rufas_match_animal_baseline.json` | `rufas_match_animal.json` |

Change: Line 196, `bedding_name` for growing pen: `"straw"` → `"none (no bedding)"`

### 2.2 Feed file — growing heifer ration

| File | Baseline (C) | Heifer Pasture (D) |
|---|---|---|
| Feed config | `example_Midwest_feed.json` | `example_Midwest_feed_heifer_pasture_v2.json` |

Changes in `example_Midwest_feed_heifer_pasture_v2.json`:
- `growing_feeds`: `[44, 50, 95, 104, 110, 301, 302]` → `[92, 105, 301]`
- `user_defined_ration_percentages.growing`: replaced 7-ingredient TMR with ID 92 (77.81%) + ID 105 (19.45%) + ID 301 (2.74%)
- IDs 92 and 105 added to `purchased_feeds` (cost 0.01) and `allowances` (1000.0 each)
- All other pens (calf, close_up, lac_cow) unchanged

### 2.3 Manure processor configs — handler type and storage parameters

| File | Baseline (C) | Heifer Pasture (D) |
|---|---|---|
| Processor configs | `example_freestall_processor_configs_baseline.json` | `example_freestall_processor_configs.json` |

Changes in `example_freestall_processor_configs.json`:
- Line 26: `processor_type` for `growing_alley_scraper`: `"AlleyScraper"` → `"ManualScraper"`
- Line 85: `cover` for `slurry_storage_outdoor_growing`: `"no_crust_or_cover"` → `"crust"`
- Line 86: `storage_time_period` for `slurry_storage_outdoor_growing`: `120` → `1`

**Note:** The processor type in the configs file still shows `ManualScraper` and the slurry storage is retained (with 1-day/crust). This is because `example_freestall_processor_configs.json` was the pre-v2 config file. The actual routing (what matters for emissions) is now fully controlled by the connections file — `growing_alley_scraper` routes to `dailyspread`, so manure never reaches `slurry_storage_outdoor_growing` in Scenario D. The slurry storage entry is retained in configs to satisfy the RuFaS validator (every processor in configs must have a connection entry), not because it is used.

### 2.4 Manure connections file — routing to DailySpread

| File | Baseline (C) | Heifer Pasture (D) |
|---|---|---|
| Connections | `example_freestall_processor_connections.json` | `example_freestall_processor_connections_heifer_pasture_v2.json` |

This is a new file created for v2. Key change:

```json
// Baseline (C):
{
  "processor_name": "growing_alley_scraper",
  "destinations": [
    { "receiving_processor_name": "slurry_storage_outdoor_growing", "proportion": 1.0 }
  ]
}

// Heifer Pasture (D):
{
  "processor_name": "growing_alley_scraper",
  "destinations": [
    { "receiving_processor_name": "dailyspread", "proportion": 1.0 }
  ]
}
```

Additional entries in the v2 connections file (required by RuFaS validator):
- `slurry_storage_outdoor_growing`: retained with empty destinations
- `dailyspread`: added with empty destinations

---

## Section 3 — Why DailySpread (Not ManualScraper + Slurry)

The v1 analysis used `ManualScraper` with a 1-day slurry storage and crust cover as a workaround for modeling pasture direct-deposit. This was a pre-v1.0 approach. The RuFaS development team confirmed in GitHub discussion #2941 that `DailySpread` is the correct v1.0 processor for pasture manure. Key differences:

| Approach | v1 workaround | v2 DailySpread |
|---|---|---|
| Manure routing | AlleyScraper → 1-day slurry (crust) → land application | DailySpread (bypass all storage) |
| Storage-based emissions | Yes — even 1 day in slurry triggers storage N2O factors | None — no storage step |
| N2O result | Artifact spike (+3,300%) | Near-baseline (unchanged from C) |
| Confirmed by RuFaS team | No | Yes (#2941) |

The N2O spike in v1 was entirely an artifact of routing manure through a slurry storage unit. Slurry storage triggers storage-based N2O emission factors regardless of storage duration. DailySpread correctly bypasses storage and produces no such artifact.

---

## Section 4 — RuFaS Validator Behavior

RuFaS requires that **every processor defined in the configs file has a corresponding entry in the connections file**, even if that processor receives no inputs and routes nothing. Failure to include an entry produces:

```
ValueError: Undefined Routing Connections for {'processor_name'}
```

This caused 4 failed seeds during initial v2 testing when `slurry_storage_outdoor_growing` was not included in the new connections file. Fix: add the processor with empty destinations.

This requirement applies to both `processor_connections` and `separator_connections` lists.

---

## Section 5 — Running the Analysis

### Task file

`input/data/tasks/example_freestall_task.json`

Contains 16 tasks: 4 seeds × 4 scenarios. Runs with `parallel_workers: 4`.

```bash
python main.py input/data/tasks/example_freestall_task.json
```

### Known race condition

With `parallel_workers: 4`, one baseline seed occasionally fails silently. This is a known issue and has not been root-caused. Three completed seeds are sufficient for averaging (typical seed variance is ±0.002 kg CO2e/kg FPCM). To guarantee full completion, set `parallel_workers: 1`.

### Output location

`output/reports/`

Primary comparison: files prefixed `baseline_` vs. files prefixed `heifer_pasture_v2_`.

---

## Section 6 — Results Summary (April 2026)

### Component breakdown

| Emission Source | C: Baseline | D: Heifer Pasture | Change |
|---|---|---|---|
| Enteric CH4 | 0.764 | 0.770 | +0.9% |
| Manure CH4 | 0.334 | 0.289 | −13.7% |
| Manure N2O | 0.0002 | 0.0002 | No change |
| Feed excl. LUC | 0.371 | 0.358 | −3.7% |
| Land use change | 0.034 | 0.026 | −24% |
| **Total excl. LUC** | **1.470** | **1.417** | **−3.6%** |
| **Total incl. LUC** | **1.504** | **1.443** | **−4.1%** |

### Interpretation

- **Manure CH4 −13.7%:** Primary driver. Eliminates 4-month anaerobic slurry storage.
- **LUC −24%:** Grazed pasture has near-zero land conversion footprint vs. purchased corn silage/grain/alfalfa.
- **Feed −3.7%:** Lower production emissions for grazed forages vs. harvested feed.
- **Enteric +0.9%:** Expected. Fresh forage is higher in fiber, slightly more rumen fermentation.
- **N2O unchanged:** Correct under DailySpread. v1 spike was artifact.

---

## Section 7 — Open Items and Pending Work

### 7.1 Soil carbon sequestration (highest priority)

Not modeled. Permanent pasture sequesters 0.2–1.0 tonnes CO2/ha/year. This is the single largest unquantified benefit and is expected to further favor Scenario D.

**Path forward:** Configure the RuFaS Soil and Crop Module (Daycent-based) for a cool-season grass-legume system with daily manure application, or integrate RangeSTAR results. Requires coordination with the RuFaS development team or the RangeSTAR team.

### 7.2 Heifer growth rate feedback

RuFaS does not currently reduce heifer growth rates when diet quality changes. If the pasture ration is below energy requirements, the model falls back to the previous ration. The energy balance implications of a forage-only diet are not fully captured.

### 7.3 Sensitivity analysis — manure storage time

An OAT (one-at-a-time) sensitivity run on `storage_time_period` (60, 90, 120, 150 days) for the confined baseline would quantify how much the baseline result is driven by storage assumptions. Not started.

### 7.4 Seasonal pasture variation

Fixed annual ration. Real managed pastures vary in quality and availability. Not currently modeled.

### 7.5 On-farm energy use

Not captured in RuFaS. FARMES estimates ~0.043 kg CO2e/kg FPCM; adding this would affect C and D equally.

### 7.6 Co-benefits quantification (water quality, biodiversity)

The GHG modeling captures only one dimension of the heifer pasture practice. Paine et al. (2021) quantify the following co-benefits for well-managed perennial pasture vs. tilled corn-soy (most likely displaced land use in Upper Midwest):

| Metric | Tilled corn-soy | Pasture | Change |
|---|---|---|---|
| Phosphorus runoff | 2.0 lb P/ac/yr | 0.2 lb P/ac/yr | −90% |
| Nitrate leaching | 28.6 lb N/ac/yr | 8.9 lb N/ac/yr | −69% |
| Stormwater runoff (5-in event) | Baseline | −36% | −36% |
| Grassland bird nesting density | 0.04 pairs/ac | 2.6 pairs/ac | 65× |
| Pollinator habitat quality (0–10) | Baseline | 3–4× | 3–4× |

These are not modeled in RuFaS or FARMES and represent unreported program value. Tools that could quantify these include SmartScape (spatial water quality + carbon) and RangeSTAR (full carbon cycle + nutrient retention).

**Source:** Paine, L.K. et al. (2021). *Well-managed perennial pasture: Setting the gold standard for ecosystem services.* Grassland 2.0, UW–Madison. grasslandag.org.

### 7.7 PML conversation

Discuss with RuFaS leadership (via GitHub discussion #2941 contact) potential contribution of a grazing module. DailySpread is the current solution but a dedicated grazing module would support seasonal variation and growth rate feedback.

---

## Section 8 — Feed Ingredient Reference

| RuFaS ID | Name | Type | Source row |
|---|---|---|---|
| 44 | Corn, yellow — grain | Grain | `user_feeds.csv` line 45 |
| 50 | Corn, yellow — silage, immature | Forage | `user_feeds.csv` line 51 |
| 51 | Corn, yellow — silage, mature | Forage | `user_feeds.csv` line 52 |
| 92 | Grasses, cool season — pasture | Forage | `user_feeds.csv` line 93 |
| 95 | Grass-legume mixtures — hay, mature | Forage | `user_feeds.csv` line 96 |
| 104 | Grass-legume mixtures — silage | Forage | `user_feeds.csv` line 105 |
| 105 | Legumes, forage — pasture, intensively managed | Forage | `user_feeds.csv` line 106 |
| 107 | Legumes, forage — alfalfa hay | Forage | `user_feeds.csv` line 108 |
| 110 | Legumes, forage — alfalfa silage | Forage | `user_feeds.csv` line 111 |
| 167 | Legumes, forage — other hay | Forage | `user_feeds.csv` line 168 |
| 202 | Calf starter | Concentrate | `user_feeds.csv` line 203 |
| 216 | Whole milk | Liquid | `user_feeds.csv` line 217 |
| 301 | Farm ES Mineral Mix | Mineral | `NASEM_Comp_with_TDN.csv` line 171 |
| 302 | Farm ES Midwest BP Blend | Concentrate | `NASEM_Comp_with_TDN.csv` line 172 |

---

## Section 9 — Repository Structure

```
rufas-grazing-heifers/
├── main.py                          ← Entry point
├── requirements.txt
├── input/
│   ├── metadata/
│   │   ├── example_freestall_dairy_metadata_baseline.json        ← Scenario C
│   │   ├── example_freestall_dairy_metadata_heifer_pasture_v2.json  ← Scenario D
│   │   ├── example_freestall_dairy_metadata_heifer_pasture.json  ← Intermediate
│   │   └── example_freestall_dairy_metadata_heifer_pasture_feed.json  ← Intermediate
│   └── data/
│       ├── animal/
│       │   ├── rufas_match_animal_baseline.json                  ← C animal config
│       │   └── rufas_match_animal.json                           ← D animal config
│       ├── feed/
│       │   ├── example_Midwest_feed.json                         ← C feed
│       │   └── example_Midwest_feed_heifer_pasture_v2.json       ← D feed (80:20)
│       ├── manure/
│       │   ├── example_freestall_processor_configs_baseline.json ← C manure config
│       │   ├── example_freestall_processor_configs.json          ← D manure config
│       │   ├── example_freestall_processor_connections.json      ← C connections
│       │   └── example_freestall_processor_connections_heifer_pasture_v2.json  ← D connections
│       └── tasks/
│           └── example_freestall_task.json                       ← 16-task run file
├── output/
│   └── reports/                                                  ← Simulation outputs
│       ├── baseline_41_...
│       ├── baseline_42_...
│       ├── heifer_pasture_v2_41_...
│       └── ...
├── GHG_Intensity_Meeting_Brief_2026-04-15_v4.md                  ← Latest stakeholder brief
├── RuFaS_Heifer_Grazing_GHG_Guide_v2.md                          ← External guide (this repo)
├── RuFaS_Heifer_Grazing_Internal_Guide_v2.md                     ← This document
└── RuFaS_Heifer_Grazing_Reproduction_Guide.md                    ← Step-by-step run guide
```

---

## Section 10 — Context for Handoff

### What is done
- All four scenarios configured and running cleanly (4/4 seeds)
- v2 methodology confirmed with RuFaS development team
- N2O artifact identified, corrected, and documented
- Results written up in v4 stakeholder brief (April 15, 2026)
- Code pushed to GitHub: https://github.com/carbon-yield/rufas-grazing-heifers, branch `heifer-pasture-analysis`

### What requires the next person's attention
- **Soil carbon gap** — the most material remaining item. No soil C model is configured.
- **Sensitivity analysis** — storage time OAT runs (not started)
- **Heifer growth rate feedback** — RuFaS gap; needs upstream development or workaround
- **FARMES disagreement** — not resolved; likely requires a deeper look at FARMES emission factor assumptions

### How to pick this up
1. Read `GHG_Intensity_Meeting_Brief_2026-04-15_v4.md` for full context
2. Read this document for technical implementation details
3. Run `python main.py input/data/tasks/example_freestall_task.json` to reproduce results
4. Review GitHub discussion #2941 for RuFaS team guidance on DailySpread and legume addition

---

*Internal guide v2 — April 2026. Supersedes v1 (March 2026).*
*Branch: heifer-pasture-analysis | Repo: https://github.com/carbon-yield/rufas-grazing-heifers*
