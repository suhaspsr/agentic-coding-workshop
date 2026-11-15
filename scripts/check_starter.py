"""Validate supplied synthetic input data; does not implement the exercise."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rows(path):
    with (ROOT / path).open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def main():
    sessions = rows('data/sessions.csv')
    assert len(sessions) == 1200
    for key in ('session_id', 'customer_id'):
        assert len({r[key] for r in sessions}) == len(sessions)
    assert {r['ordered_next_30m'] for r in sessions} == {'0', '1'}
    for key in ('device', 'seconds_active_5m', 'product_views_5m'):
        assert any(not r[key] for r in sessions), key
    assert all(0 <= int(r['seconds_active_5m']) <= 300 for r in sessions if r['seconds_active_5m'])
    new = rows('data/new_sessions.csv')
    assert len(new) == 12
    assert set(new[0]) == set(sessions[0]) - {'ordered_next_30m'}
    assert not {r['session_id'] for r in sessions} & {r['session_id'] for r in new}
    assert not {r['customer_id'] for r in sessions} & {r['customer_id'] for r in new}
    print('Starter checks passed: 1,200 labeled sessions and 12 unlabeled prediction rows.')


if __name__ == '__main__':
    main()
