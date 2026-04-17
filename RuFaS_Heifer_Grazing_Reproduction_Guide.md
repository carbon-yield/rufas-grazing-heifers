# Reproducing the Heifer Pasture GHG Analysis
## Step-by-Step Guide for New Users

**Version:** v1 (April 2026)
**Repo:** https://github.com/carbon-yield/rufas-grazing-heifers
**Branch:** `heifer-pasture-analysis`

---

## Prerequisites

| Requirement | Notes |
|---|---|
| Python 3.9+ | Tested on Python 3.10 |
| Git | Any recent version |
| ~2 GB disk space | For outputs |
| 4+ CPU cores | Recommended for parallel runs |

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/carbon-yield/rufas-grazing-heifers.git
cd rufas-grazing-heifers
```

---

## Step 2 — Check Out the Analysis Branch

```bash
git checkout heifer-pasture-analysis
```

Verify you are on the right branch:

```bash
git branch
# Should show: * heifer-pasture-analysis
```

---

## Step 3 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

If a virtual environment is preferred:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

---

## Step 4 — Confirm Input Files Are Present

The four scenarios in this analysis require the following input files. All are included in the repo.

### Metadata files (top-level orchestrators)

| Scenario | Metadata file |
|---|---|
| C: RuFaS Baseline | `input/metadata/example_freestall_dairy_metadata_baseline.json` |
| D: RuFaS Heifer Pasture | `input/metadata/example_freestall_dairy_metadata_heifer_pasture_v2.json` |

### Key data files changed between C and D

| File | Path |
|---|---|
| Animal config (heifer bedding) | `input/data/animal/rufas_match_animal.json` |
| Feed ration (heifer growing pen) | `input/data/feed/example_Midwest_feed_heifer_pasture_v2.json` |
| Manure processor configs | `input/data/manure/example_freestall_processor_configs.json` |
| Manure processor connections | `input/data/manure/example_freestall_processor_connections_heifer_pasture_v2.json` |

Quick check (run from the repo root):

```bash
ls input/metadata/example_freestall_dairy_metadata_heifer_pasture_v2.json
ls input/data/manure/example_freestall_processor_connections_heifer_pasture_v2.json
```

---

## Step 5 — Run the Analysis

The task file runs 16 total simulations: 4 seeds × 4 scenarios (baseline, heifer_pasture, heifer_pasture_feed, heifer_pasture_v2). The primary comparison is **baseline** (Scenario C) vs. **heifer_pasture_v2** (Scenario D).

```bash
python main.py input/data/tasks/example_freestall_task.json
```

Expected runtime: 15–30 minutes on a 4-core machine with `parallel_workers: 4`.

### What to expect during the run

- Progress is logged to the console.
- Each task prints its output prefix and seed number when it completes.
- Occasional single-seed failures on `baseline` are a known race condition and are acceptable — the remaining 3 seeds are sufficient for averaging.

---

## Step 6 — Locate the Output Files

Results are written to `output/reports/`. Each scenario produces a set of files prefixed with the scenario name.

| Scenario | Output prefix | Files |
|---|---|---|
| C: RuFaS Baseline | `baseline_` | `baseline_41_...csv`, `baseline_42_...csv`, etc. |
| D: RuFaS Heifer Pasture | `heifer_pasture_v2_` | `heifer_pasture_v2_41_...csv`, etc. |

The primary output file for GHG results is the summary CSV ending in `_ghg_intensity.csv` (or equivalent — check the filenames produced in your run).

---

## Step 7 — Compare Results

The expected results from the April 2026 reference run:

| Metric | C: RuFaS Baseline | D: RuFaS Heifer Pasture | Change |
|---|---|---|---|
| GHG intensity incl. LUC (kg CO2e/kg FPCM) | 1.504 | 1.443 | **−4.1%** |
| GHG intensity excl. LUC | 1.470 | 1.417 | **−3.6%** |
| Manure CH4 | 0.334 | 0.289 | −13.7% |
| Manure N2O | 0.0002 | 0.0002 | No change |
| Enteric CH4 | 0.764 | 0.770 | +0.9% |
| Feed (excl. LUC) | 0.371 | 0.358 | −3.7% |
| Land use change | 0.034 | 0.026 | −24% |

Seed-to-seed variation is typically ±0.002 kg CO2e/kg FPCM. Your results should match these values closely (within ±0.005).

---

## Step 8 — Review the Meeting Brief

The full analysis writeup is in:

```
GHG_Intensity_Meeting_Brief_2026-04-15_v4.md
```

This document contains scenario descriptions, input comparison table, all GHG results, key findings, model gaps, and the full appendix of input file changes.

---

## Troubleshooting

### `ValueError: Undefined Routing Connections`

Every processor defined in the manure configs file must have a corresponding entry in the connections file, even if it routes nothing. If you add a new processor to `example_freestall_processor_configs.json`, add it with empty destinations to the connections file as well.

```json
{
  "processor_name": "your_new_processor",
  "destinations": []
}
```

### One baseline seed crashes silently

This is a known race condition with `parallel_workers: 4`. Three completed seeds are sufficient for averaging. If reproducibility matters, set `parallel_workers: 1` in the task file to serialize execution.

### `ModuleNotFoundError` on startup

Confirm you are in the repo root and your virtual environment is activated. Run `pip install -r requirements.txt` again.

---

## File Map — Analysis-Specific Files

The following files were created for this analysis (not part of the original RuFaS distribution):

```
input/
  metadata/
    example_freestall_dairy_metadata_heifer_pasture_v2.json   ← Scenario D metadata
    example_freestall_dairy_metadata_heifer_pasture_feed.json ← Scenario intermediate (not used in final comparison)
    example_freestall_dairy_metadata_heifer_pasture.json      ← Scenario intermediate (not used in final comparison)
  data/
    feed/
      example_Midwest_feed_heifer_pasture_v2.json             ← 80:20 grass-legume ration
    manure/
      example_freestall_processor_connections_heifer_pasture_v2.json  ← DailySpread connections

GHG_Intensity_Meeting_Brief_2026-04-15_v4.md                 ← Latest results document
```

---

*Reproduction guide v1 — April 2026. Questions: file an issue at https://github.com/carbon-yield/rufas-grazing-heifers/issues*
