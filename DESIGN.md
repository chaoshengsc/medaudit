# MedAudit v0.2.0

MedAudit accepts a JSON configuration, a row-aligned manifest CSV, and a
precomputed `features.npy` matrix. `medaudit audit` then produces a plain-text
report from two checks:

1. an attribute probe, overall and within each evaluable diagnostic class; and
2. a leakage screen for supplied split assignments, group overlap, and
   embedding-similarity candidates.

The package does not extract features, train a classifier, or make a clinical
validation claim. Its metrics module also exposes AUROC, ECE, Brier,
reliability curves, and cluster bootstrap primitives for use in separate
analyses.

## Current input and output

The manifest requires `path` and `label`. A `group` column enables patient/case
aware splitting and inference; without it, each row is treated as its own group.
Each `attr_*` column is an attribute that can be probed. A `split` column is
optional: when supplied, the leakage check evaluates that assignment; otherwise
MedAudit creates a split for the current inputs and labels group-leakage
assessment as unassessed for any earlier pipeline split.

```text
audit.json + manifest.csv + features.npy
                    |
                    v
        attribute probe + leakage screen
                    |
                    v
              plain-text report
```

The report uses candidate language for cosine-similarity pairs. It cannot
establish image identity. Attribute decodability shows that information is in
the supplied features; it does not show that an original classifier used it.

## Implemented modules

| Module | Current role |
|---|---|
| `medaudit.manifest` | Load and validate the CSV input |
| `medaudit.splits` | Group-aware generated split and overlap utilities |
| `medaudit.audits.probe` | Group-aware, out-of-fold linear attribute probes |
| `medaudit.audits.leakage` | Group-overlap check and cosine-similarity screen |
| `medaudit.audit` / `medaudit.cli` | JSON-configured orchestration and text report |
| `medaudit.metrics` | Reusable metric primitives |

## Planned modules

Feature extraction, calibration reports, prevalence-shift analysis, external
evaluation, and HTML reporting are not part of v0.2.0.
