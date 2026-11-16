"""Validate supplied synthetic input data; does not implement the exercise."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_COLUMNS = {
    'session_id', 'customer_id', 'page_views_5m', 'product_views_5m',
    'cart_additions_5m', 'seconds_active_5m', 'returning_customer', 'device',
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
    for key in ('device', 'seconds_active_5m', 'product_views_5m'):
        assert any(not r[key] for r in sessions), key

    new = rows('data/new_sessions.csv')
    assert len(new) == 12
    assert set(new[0]) == INPUT_COLUMNS
    for key in ('session_id', 'customer_id'):
        assert len({r[key] for r in new}) == len(new)
        assert not {r[key] for r in sessions} & {r[key] for r in new}
    activity_names = (
        'page_views_5m', 'product_views_5m', 'cart_additions_5m',
        'seconds_active_5m', 'returning_customer', 'device',
    )
    training_activity = {tuple(r[name] for name in activity_names) for r in sessions}
    assert all(tuple(r[name] for name in activity_names) not in training_activity for r in new)

    for data in (sessions, new):
        assert {r['is_logged_in'] for r in data} == {'0', '1'}
        assert {r['fulfillment_method'] for r in data} == {'', 'carryout', 'delivery'}
        assert {r['loyalty_member'] for r in data} == {'', '0', '1'}
        assert all(0 <= int(r['seconds_active_5m']) <= 300 for r in data if r['seconds_active_5m'])
        for row in data:
            assert row['returning_customer'] in {'0', '1'}
            if row['is_logged_in'] == '0':
                assert not row['previous_visits'] and not row['previous_orders']
                assert not row['loyalty_member']
            else:
                visits = int(row['previous_visits'])
                orders = int(row['previous_orders'])
                assert 0 <= orders <= visits
                assert (visits > 0) == (row['returning_customer'] == '1')
                assert row['loyalty_member'] in {'0', '1'}
    print('Starter checks passed: 1,200 labeled conversion sessions and 12 unlabeled prediction rows.')


if __name__ == '__main__':
    main()
