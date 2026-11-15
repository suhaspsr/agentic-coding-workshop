# Synthetic orders

All records are fictional. `orders.csv` contains 16 orders across three stores and three dates.
Order IDs are unique across all statuses. Store IDs are strings; preserve leading zeros.
Amounts are nonnegative decimal values with two fractional digits. Zero-value orders are valid.
Dates are ISO calendar dates (`YYYY-MM-DD`). Status is `completed` or `cancelled`.

Sum completed orders only. Group by store_id and order_date.
Output columns: `store_id,order_date,total_sales`, sorted by date then store ID.
Overwrite the chosen output rather than appending so reruns do not duplicate results.
Reject missing columns, duplicate order IDs, empty required fields, invalid dates,
nonfinite/negative amounts and unknown statuses with clear errors.
Header-only input may produce header-only output; document it.

`expected_daily_sales.csv` contains seven expected summary rows, totaling 131.04.
For 2026-11-02: store 00101 has 20.25 and store 00103 has 30.50.
`invalid/` contains separate fixtures for duplicate IDs, an invalid amount and an invalid date.
These are input examples, not intentionally introduced code bugs. Do not mix them into the normal sample.
