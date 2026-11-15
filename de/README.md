# DE track: daily sales pipeline

Open the **repository root**, not this folder, in Copilot. Both tracks share the root Poetry configuration and `.venv`. Run all commands from the repository root with `poetry run python`. Keep DE code in `de/`; do not create another Poetry project here.

Prepared inputs:

- `de/data/orders.csv`: 16 valid orders across three stores and three dates.
- `de/data/expected_daily_sales.csv`: seven exact expected rows, totaling 131.04.
- `de/data/invalid/`: separate fixtures for duplicate order IDs, invalid amounts and invalid dates.
- `de/data/README.md`: schema and transformation rules.

Build with Orca using `agentic-coding-workbook.html` at the repository root. Start with hello world, then ask for a plan. Use the supplied files rather than generating replacements.

Sum completed orders only, group by store and date, preserve leading zeros in store IDs, and use Decimal for money. Match the expected output's schema and ordering. Add CLI input/output paths, clear input-validation errors and unittest checks. Later add an optional date filter while preserving the all-dates default.

Write generated summaries under `de/outputs/` (ignored by Git). Rerunning the same input into the same output should replace it rather than append duplicates. No pandas, database, server or Docker is required.
