# DE track: daily sales pipeline

Open this folder as the working project. Keep the existing Poetry configuration and use `poetry run python` for Python commands. Python standard-library modules are sufficient.

Prepared inputs:

- `data/orders.csv`: 16 valid orders across three stores and three dates.
- `data/expected_daily_sales.csv`: seven exact expected rows, totaling 131.04.
- `data/invalid/`: separate fixtures for duplicate order IDs, invalid amounts and invalid dates.
- `data/README.md`: schema and transformation rules.

Build with Orca using the HTML workbook in the repository's parent directory. Start with hello world, then ask for a plan. Use the supplied files rather than generating replacements.

Sum completed orders only, group by store and date, preserve leading zeros in store IDs, and use Decimal for money. Match the expected output's schema and ordering. Add CLI input/output paths, clear input-validation errors and unittest checks. Later add an optional date filter while preserving the all-dates default.

Write generated summaries under `outputs/` (ignored by Git). Rerunning the same input into the same output should replace it rather than append duplicates. No pandas, database, server or Docker is required.
