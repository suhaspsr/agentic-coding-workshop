# MLE track: conversion prediction

Open the **repository root**, not this folder, in Copilot. Both tracks share the root Poetry configuration and `.venv`. Run all commands from the repository root with `poetry run python`. Keep MLE code in `mle/`; do not create another Poetry project here.

Prepared inputs:

- `mle/data/sessions.csv`: 1,200 labeled sessions. Target: `ordered_next_30m`.
- `mle/data/new_sessions.csv`: 12 unlabeled rows for batch prediction.
- `mle/data/README.md`: schema, prediction boundary and missing-value semantics.

Build with Orca using `agentic-coding-workbook.html` at the repository root. Start with hello world, then ask for a plan. Use the supplied CSVs; do not replace them with a newly generated dataset.

Scope: at minute five, predict whether a still-open session with no prior order will convert in the next 30 minutes. Exclude both identifiers and the label from model features. Split before fitting preprocessing, handle numeric/categorical missing values, train logistic regression, evaluate against an always-no-order baseline, and persist preprocessing with the model. Use unittest for tests.

Write generated models under `mle/models/` and predictions/reports under `mle/outputs/` (both ignored by Git). Later add an adjustable prediction threshold with 0.5 as the default. No server or Docker is required.

Expected evidence: held-out metrics, a saved pipeline that predicts on unlabeled rows, missing-input handling, passing behavioral tests and usable run instructions. No fixed accuracy target is specified for this synthetic exercise.
