# First-cart prediction review — cycle 1

## Review scope

- Repository: `suhaspsr/agentic-coding-workshop`
- Base revision: `5e1fc366e9bbf44de952451870325766ee716292`
- HEAD: unchanged from base; working-tree changes were uncommitted.
- Reviewed files: `README.md`, `agentic-coding-workbook.html`, `data/README.md`, `data/new_sessions.csv`, `data/sessions.csv`, `scripts/check_starter.py`.
- Workstream: `first-cart-data-adoption-20261116-001-review`
- Reviewer: Titan Reviewer
- Configured model: `claude-haiku-5.5`
- Runtime model evidence: unavailable
- Disposition: **APPROVE WITH CHANGES**

## Acceptance criteria

1. At the first cart addition, predict whether an order will be placed after that addition and before the session ends, regardless of elapsed session time.
2. Use only features available at or before the first-cart trigger; do not use elapsed-time or post-trigger activity features.
3. Provide 1,200 labeled synthetic examples and 12 unlabeled first-cart prediction examples, with IDs excluded from features and the target absent from the unlabeled file.
4. Describe the same trigger, inputs, target, and data assumptions consistently across the README, data guide, workbook, CSV schemas, and starter validator.

## Review evidence and limits

The reviewer reported reading the current contents of the six scoped files, all 12 unlabeled rows, and approximately the first 200 labeled rows, with pattern searches and the supplied validator result for the remainder. The reviewer could not execute commands, inspect the Git diff, or hash files; therefore, the cycle-1 changed-file inventory and hashes were not independently verified. Runtime model telemetry was unavailable.

Orca validation before this review:

- `python3 scripts/check_starter.py` — passed.
- Workbook JavaScript syntax and project configuration JSON parse — passed.
- Search for five-minute wording and old `_5m` fields — no matches.

## Findings and dispositions

| Finding | Disposition | Resolution |
|---|---|---|
| F1: Point-in-time semantics were asserted but not reproducible or clearly marked as synthetic. | Accepted | Added `scripts/generate_starter.py` with seed 42, documented that trigger-time values are a synthetic assumption rather than event-log-verified snapshots, and stated the evidence required for real data. |
| F2: The loyalty field lacked a trigger-time qualifier. | Accepted | Clarified that `loyalty_member` is known at the trigger. |
| F3: The validator required returning recognition to equal signed-in visit history. | Accepted | Removed that equality check and documented that cookie/session recognition may differ from signed-in visit history. |
| F4: The optional join prompt described the starter join as many-to-one despite one session per customer. | Accepted | Clarified the starter's one-to-one relationship and when a customer lookup is many-to-one. |
| F5: The data-check instructions said any Python interpreter but invoked `poetry run`. | Accepted | Changed the command to `python scripts/check_starter.py` and noted it uses only the standard library. |
| F6: The validator did not check device categories. | Accepted | Added allowed-value checks for blank, mobile, desktop, and tablet. |

## Audit

- Session-relative timestamp: implementation review cycle 1.
- Event: `lock_issued`, then `lock_closed`.
- Validation outcome: pass with required repairs recorded above.
- Failure code: null.
- Repair/re-review authorization: Orca-authorized bounded implementation repair and cycle-2 review.
