# Synthetic customer sessions

All records are fictional, generated with seed 42. No real customer data is used.

- `sessions.csv`: 1,200 labeled rows, one unique session per unique customer.
- `new_sessions.csv`: 12 separately generated unlabeled sessions for batch prediction with distinct IDs. Evaluate the model on held-out labeled rows, not these examples.
- Every session is still open at minute five, with no order yet.
- Use only information available by minute five.
- `converted` is 1 if an order is placed before the session ends, and 0 if the session ends without an order. It is not a 30-minute deadline.

| Column | Meaning | Role |
|---|---|---|
| session_id | Fictional session ID | Keep for output; exclude from features |
| customer_id | Fictional customer ID | Exclude from features |
| page_views_5m | Page views in the first five minutes | Numeric |
| product_views_5m | Product views in the first five minutes | Numeric; some missing |
| cart_additions_5m | Cart additions in the first five minutes | Numeric |
| seconds_active_5m | Active seconds in the first five minutes, at most 300 | Numeric; some missing |
| returning_customer | Whether the session is recognized as returning, for example by a cookie | Binary |
| device | mobile, desktop or tablet | Categorical; some missing |
| is_logged_in | Whether the customer is signed in by minute five | Binary |
| previous_visits | Visits before this session | Numeric; unknown for guests |
| previous_orders | Orders before this session, no greater than previous visits | Numeric; unknown for guests |
| loyalty_member | Whether the customer is a loyalty member | Binary; unknown for guests |
| fulfillment_method | carryout or delivery if selected by minute five | Categorical; empty if not yet selected |
| converted | Order before session end: 0 or 1 | Target; absent from new_sessions.csv |

Empty cells mean unknown or not yet selected, not automatically zero or no. The customer ID is fictional bookkeeping, not a login credential; exclude both IDs and the target from features. Use the supplied data rather than regenerating it during the demo.
Split before fitting preprocessing and save the preprocessing with the model.
A stratified split is suitable for this synthetic one-session-per-customer exercise.
Real repeated-customer or temporal data needs an appropriate group/time split, a consistent session-end definition and completed sessions for labels.
Synthetic metrics demonstrate workflow mechanics, not real business performance or the effect of a discount.
