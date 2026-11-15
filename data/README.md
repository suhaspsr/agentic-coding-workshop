# Synthetic customer sessions

All records are fictional, generated with seed 42. No real customer data is used.

- `sessions.csv`: 1,200 labeled rows, one unique session per unique customer.
- `new_sessions.csv`: 12 unlabeled rows for batch prediction with distinct IDs.
- Every session is still open at minute five, with no order yet.
- The label is whether an order is placed in the next 30 minutes.

| Column | Meaning | Role |
|---|---|---|
| session_id | Fictional session ID | Keep for output; exclude from features |
| customer_id | Fictional customer ID | Exclude from features |
| page_views_5m | Page views in the first five minutes | Numeric |
| product_views_5m | Product views in the first five minutes | Numeric; some missing |
| cart_additions_5m | Cart additions in the first five minutes | Numeric |
| seconds_active_5m | Active seconds in the first five minutes, at most 300 | Numeric; some missing |
| returning_customer | 0 or 1 | Binary |
| device | mobile, desktop or tablet | Categorical; some missing |
| ordered_next_30m | Conversion: 0 or 1 | Target; absent from new_sessions.csv |

Empty cells mean missing values. Use the supplied data rather than regenerating it during the demo.
Split before fitting preprocessing and save the preprocessing with the model.
A stratified split is suitable for this synthetic one-session-per-customer exercise.
Real repeated-customer or temporal data needs an appropriate group/time split and complete label windows.
Synthetic metrics demonstrate workflow mechanics, not real business performance.
