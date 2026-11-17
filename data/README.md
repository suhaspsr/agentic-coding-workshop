# Synthetic customer sessions

All records are fictional, generated with seed 42. No real customer data is used. The trigger-time values are a synthetic point-in-time assumption, not snapshots verified from event logs. Each feature is defined as if it were known at the first cart addition; real use requires event timestamps or equivalent evidence that every feature was available by that time.

- `sessions.csv`: 1,200 labeled rows, one unique session per unique customer. Every row is observed at that session's first cart addition.
- `new_sessions.csv`: 12 separately generated unlabeled sessions for batch prediction with distinct IDs. Evaluate the model on held-out labeled rows, not these examples.
- At the first cart addition, the session is still open and no order has been placed.
- Use only information available at or before that first cart addition. The event may occur at any point in the session; elapsed time is not a prediction feature or cutoff.
- `converted` is 1 if an order is placed after the first cart addition and before the session ends, and 0 if the session ends without a subsequent order.

| Column | Meaning | Role |
|---|---|---|
| session_id | Fictional session ID | Keep for output; exclude from features |
| customer_id | Fictional customer ID | Exclude from features |
| page_views_before_cart | Page views before the first cart addition | Numeric |
| product_views_before_cart | Product views before the first cart addition | Numeric; some missing |
| returning_customer | Whether the session is recognized as returning, for example by a cookie, at the trigger | Binary |
| device | mobile, desktop or tablet at the trigger | Categorical; some missing |
| is_logged_in | Whether the customer is signed in at the trigger | Binary |
| previous_visits | Visits before this session | Numeric; unknown for guests |
| previous_orders | Orders before this session, no greater than previous visits | Numeric; unknown for guests |
| loyalty_member | Whether the customer is a loyalty member at the trigger | Binary; unknown for guests |
| fulfillment_method | carryout or delivery if selected by the trigger | Categorical; empty if not yet selected |
| converted | Order after the first cart addition and before session end: 0 or 1 | Target; absent from new_sessions.csv |

Every row is conditioned on a first cart addition; sessions without one are outside this prediction task. Counts describe activity before the trigger, and no post-trigger activity or elapsed time is included. `returning_customer` is recognition by the session, while `previous_visits` is signed-in history; a customer with prior visits may not be recognized as returning. Empty cells mean unknown or not yet selected, not automatically zero or no. The customer ID is fictional bookkeeping, not a login credential; exclude both IDs and the target from features. Use the supplied data rather than regenerating it during the demo.
Split before fitting preprocessing and save the preprocessing with the model.
A stratified split is suitable for this synthetic one-session-per-customer exercise.
Real repeated-customer data needs an appropriate group split, a consistent definition of session end and completed sessions for labels.
Synthetic metrics demonstrate workflow mechanics, not real business performance or the effect of a discount.
