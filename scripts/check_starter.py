"""Validate checked-in workshop data; does not implement either exercise."""
import csv
from collections import defaultdict
from datetime import date
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rows(path):
    with (ROOT / path).open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def main():
    sessions = rows('mle/data/sessions.csv')
    assert len(sessions) == 1200
    for key in ('session_id', 'customer_id'):
        assert len({row[key] for row in sessions}) == len(sessions)
    assert {row['ordered_next_30m'] for row in sessions} == {'0', '1'}
    assert any(not row['device'] for row in sessions)
    assert any(not row['seconds_active_5m'] for row in sessions)
    assert all(0 <= int(row['seconds_active_5m']) <= 300 for row in sessions if row['seconds_active_5m'])
    new = rows('mle/data/new_sessions.csv')
    assert len(new) == 12 and 'ordered_next_30m' not in new[0]
    assert not {r['session_id'] for r in sessions} & {r['session_id'] for r in new}
    orders = rows('de/data/orders.csv')
    assert len(orders) == 16
    assert len({row['order_id'] for row in orders}) == len(orders)
    totals = defaultdict(Decimal)
    for row in orders:
        date.fromisoformat(row['order_date'])
        amount = Decimal(row['amount'])
        assert amount.is_finite() and amount >= 0
        assert row['store_id'].startswith('00')
        assert row['status'] in ('completed', 'cancelled')
        if row['status'] == 'completed':
            totals[(row['store_id'], row['order_date'])] += amount
    expected = rows('de/data/expected_daily_sales.csv')
    assert len(expected) == 7
    assert totals == {(r['store_id'], r['order_date']): Decimal(r['total_sales']) for r in expected}
    assert sum(totals.values()) == Decimal('131.04')
    duplicate = rows('de/data/invalid/duplicate_ids.csv')
    assert len({r['order_id'] for r in duplicate}) < len(duplicate)
    print('Starter checks passed: 1,200 labeled sessions, 12 new sessions, 16 orders, 7 expected totals (131.04).')


if __name__ == '__main__':
    main()
