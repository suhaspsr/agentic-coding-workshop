# First-cart prediction review — cycle 2

## Review scope

- Repository: `suhaspsr/agentic-coding-workshop`
- Base revision and HEAD: `5e1fc366e9bbf44de952451870325766ee716292`; changes remain uncommitted.
- Workstream: `first-cart-data-adoption-20261116-001-review-cycle-2`
- Reviewer: Titan Reviewer
- Configured model: `claude-haiku-5.5`
- Runtime model evidence: unavailable
- Orca authorization: `ORCA-AUTH-first-cart-data-adoption-cycle-2`
- Disposition: **MAJOR REVISION REQUIRED** (workflow disposition: **REQUIRES CHANGES**)

## Acceptance criteria

1. At the first cart addition, predict whether an order will be placed after that addition and before the session ends, regardless of elapsed session time.
2. Use only features available at or before the first-cart trigger; do not use elapsed-time or post-trigger activity features.
3. Provide 1,200 labeled synthetic examples and 12 unlabeled first-cart prediction examples, with IDs excluded from features and the target absent from the unlabeled file.
4. Describe the same trigger, inputs, target, and data assumptions consistently across the README, data guide, workbook, CSV schemas, and validator.

## Review evidence and limits

The reviewer inspected the changed generator and validator in full, the data guide, cycle-1 artifact, all 12 prediction rows, the first 12 labeled rows, and targeted README/workbook content. It used searches to check the CSV row/column counts and both label classes. It could not execute commands, inspect the Git diff, verify Git state, or compute hashes; validation and hash results below are Orca-reported, not independently verified by the reviewer.

Orca validation after cycle-1 repairs:

- `python3 scripts/check_starter.py` — passed; 1,200 labeled rows and 12 unlabeled rows.
- Re-running the seeded generator produced identical hashes for both CSVs.
- Workbook JavaScript syntax and project configuration JSON parse — passed.
- Search for old minute-five and `_5m` assumptions — no matches.
- `git diff --check` — passed.

## Cycle-1 findings and dispositions

All six earlier findings were resolved:

| Finding | Disposition | Evidence |
|---|---|---|
| F1: Point-in-time semantics were asserted but not reproducible or marked synthetic. | Accepted, resolved | The data guide marks the snapshot as a synthetic assumption; the seed-42 generator is present. |
| F2: Loyalty table lacked a trigger-time qualifier. | Accepted, resolved | The data guide says loyalty membership is known at the trigger. |
| F3: Returning recognition was conflated with signed-in visit history. | Accepted, resolved | The validator no longer equates them; the guide explains the distinction. |
| F4: Join prompt described the starter relationship as many-to-one. | Accepted, resolved | The workbook says the starter is one-to-one and explains when a customer lookup is many-to-one. |
| F5: README said any Python but invoked `poetry run`. | Accepted, resolved | README now uses the standard-library `python scripts/check_starter.py` command. |
| F6: Device values were not validated. | Accepted, resolved | The validator checks the allowed device values in both CSVs. |

## Current acceptance status and findings

- AC1: Met.
- AC2: Met as an explicit synthetic point-in-time assumption; real use requires timestamped or equivalent evidence.
- AC3: Met.
- AC4: **Not fully met; blocks completion.**

**R1 — Incomplete feature inventory (Low; confirmed; blocking).** The workbook's scope lists inputs but omits `device` and `returning_customer`; the README's input summary also omits those fields. This can lead participants to drop two features present in the data schema. Add them explicitly or refer readers to the complete `data/README.md` feature list.

**R2 — Synthetic timing cannot be verified from the CSVs (Low; confirmed).** The workbook asks participants to verify that each row is a point-in-time snapshot. The guide says the data is synthetic and cannot prove that. Reword the check to ask participants to confirm the documented assumption, and note the synthetic data cannot verify it.

**R3 — Logged-in history validation (Low; missing validation; non-blocking).** The validator can raise `ValueError` for blank logged-in history and does not reject negative counts. Deferred as a low-severity validation enhancement outside the confirmed acceptance blockers.

**R4 — Poetry lockfile note (Low; suspected; non-blocking).** The README says no shared lockfile is included, while the initial workspace inventory contained `poetry.lock`. Deferred as a likely pre-existing documentation issue outside the first-cart scope; the reviewer did not compare against the base.

## Audit

- Session-relative timestamp: implementation review cycle 2.
- Event: `lock_issued`, then `lock_closed`.
- Validation outcome: pass (review route completed); workflow disposition remains **REQUIRES CHANGES**.
- Failure code: null.
- Further repair/re-review: not authorized; the bounded repair cycle was used. Orca must ask the user for direction before another cycle.
