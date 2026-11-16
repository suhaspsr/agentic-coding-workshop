"""Generate the synthetic first-cart datasets used by the workshop."""
import csv
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = 42
LABELED_ROWS = 1200
PREDICTION_ROWS = 12
INPUT_COLUMNS = [
    'session_id', 'customer_id', 'page_views_before_cart',
    'product_views_before_cart', 'returning_customer', 'device',
    'is_logged_in', 'previous_visits', 'previous_orders', 'loyalty_member',
    'fulfillment_method',
]


def make_session(rng, prefix, number, labeled):
    logged_in = int(rng.random() < 0.7)
    page_views = rng.randint(1, 9)
    product_views = rng.randint(1, min(page_views, 5))
    device = rng.choices(['mobile', 'desktop', 'tablet'], weights=[5, 4, 1])[0]
    if rng.random() < 0.04:
        device = ''
    observed_product_views = '' if rng.random() < 0.05 else product_views

    if logged_in:
        visits = rng.randint(0, 12)
        orders = rng.randint(0, visits)
        loyalty = str(int(rng.random() < 0.4))
        returning = int(rng.random() < (0.9 if visits else 0.05))
        previous_visits, previous_orders, loyalty_member = visits, orders, loyalty
    else:
        returning = int(rng.random() < 0.2)
        previous_visits = previous_orders = loyalty_member = ''
        orders, loyalty = 0, '0'

    fulfillment = rng.choice(['carryout', 'delivery']) if rng.random() < 0.3 else ''
    row = {
        'session_id': f'{prefix}{number:05d}',
        'customer_id': f'C{prefix}{number:05d}',
        'page_views_before_cart': page_views,
        'product_views_before_cart': observed_product_views,
        'returning_customer': returning,
        'device': device,
        'is_logged_in': logged_in,
        'previous_visits': previous_visits,
        'previous_orders': previous_orders,
        'loyalty_member': loyalty_member,
        'fulfillment_method': fulfillment,
    }

    if labeled:
        log_odds = (
            -3.7 + 0.25 * product_views + 0.18 * page_views
            + 0.45 * logged_in + 0.35 * returning + 0.28 * orders
            + 0.45 * int(loyalty) + 0.28 * int(bool(fulfillment))
        )
        probability = 1 / (1 + math.exp(-log_odds))
        row['converted'] = int(rng.random() < probability)
    return row


def write_rows(path, rows, columns):
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    rng = random.Random(SEED)
    sessions = [
        make_session(rng, 'S', number, labeled=True)
        for number in range(1, LABELED_ROWS + 1)
    ]
    new_sessions = [
        make_session(rng, 'N', number, labeled=False)
        for number in range(1, PREDICTION_ROWS + 1)
    ]
    write_rows(ROOT / 'data/sessions.csv', sessions, INPUT_COLUMNS + ['converted'])
    write_rows(ROOT / 'data/new_sessions.csv', new_sessions, INPUT_COLUMNS)
    converted = sum(row['converted'] for row in sessions)
    print(
        f'Generated {len(sessions)} labeled sessions '
        f'({converted} conversions) and {len(new_sessions)} prediction rows.'
    )


if __name__ == '__main__':
    main()
