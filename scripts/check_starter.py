"""Validate supplied synthetic first-cart data; does not implement the exercise."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_COLUMNS = {
    'session_id', 'customer_id', 'page_views_before_cart',
    'product_views_before_cart', 'returning_customer', 'device',
    'is_logged_in', 'previous_visits', 'previous_orders', 'loyalty_member',
    'fulfillment_method',
}


def rows(path):
    with (ROOT / path).open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def main():
    sessions = rows('data/sessions.csv')
    assert len(sessions) == 1200
    assert set(sessions[0]) == INPUT_COLUMNS | {'converted'}
    for key in ('session_id', 'customer_id'):
        assert len({r[key] for r in sessions}) == len(sessions)
    assert {r['converted'] for r in sessions} == {'0', '1'}
    for key in ('device', 'product_views_before_cart'):
        assert any(not r[key] for r in sessions), key

    new = rows('data/new_sessions.csv')
    assert len(new) == 12
    assert set(new[0]) == INPUT_COLUMNS
    for key in ('session_id', 'customer_id'):
        assert len({r[key] for r in new}) == len(new)
        assert not {r[key] for r in sessions} & {r[key] for r in new}
    assert {r['is_logged_in'] for r in sessions} == {'0', '1'}
    assert {r['fulfillment_method'] for r in sessions} == {'', 'carryout', 'delivery'}
    assert {r['loyalty_member'] for r in sessions} == {'', '0', '1'}

    for data in (sessions, new):
        for row in data:
            assert row['returning_customer'] in {'0', '1'}
            assert row['is_logged_in'] in {'0', '1'}
            assert row['device'] in {'', 'mobile', 'desktop', 'tablet'}
            assert row['fulfillment_method'] in {'', 'carryout', 'delivery'}
            assert row['loyalty_member'] in {'', '0', '1'}
            assert int(row['page_views_before_cart']) >= 0
            if row['product_views_before_cart']:
                assert 0 <= int(row['product_views_before_cart']) <= int(row['page_views_before_cart'])
            if row['is_logged_in'] == '0':
                assert not row['previous_visits'] and not row['previous_orders']
                assert not row['loyalty_member']
            else:
                visits = int(row['previous_visits'])
                orders = int(row['previous_orders'])
                assert 0 <= orders <= visits
                assert row['loyalty_member'] in {'0', '1'}
    print('Starter checks passed: 1,200 labeled first-cart sessions and 12 unlabeled prediction rows.')


if __name__ == '__main__':
    main()
