"""Read-only behavior and actual exact-ID retrieval; no SQLite fixtures are written."""
import json
from pathlib import Path
import sqlite3
import time
from unittest.mock import patch

from probability_target_lookup import lookup, target_id

ROOT = Path(__file__).resolve().parent
QUERY = 'P0117 planar iid first passage percolation bigeodesics proof mistakes'


def main():
    assertions = 0
    for query, expected in [
        (QUERY, 'P0117'), ('p0117, P0117', 'P0117'),
        ('P01170', None), ('xP0117', None), ('P0117x', None),
        ('P0117 P0113', None), ('bigeodesics', None),
    ]:
        assert target_id(query) == expected
        assertions += 1
    with patch('probability_target_lookup.sqlite3.connect', side_effect=AssertionError('Unexpected store open')):
        assert lookup('P0117 P0113')['cards'] == []
        assertions += 1
    missing = ROOT / 'never_created.sqlite3'
    assert not missing.exists()
    try:
        lookup('P0117', missing)
    except sqlite3.OperationalError:
        pass
    else:
        raise AssertionError('Missing read-only database should fail')
    assert not missing.exists()
    assertions += 2

    real_connect = sqlite3.connect
    connections = []
    def audited_connect(database_uri, **kwargs):
        assert database_uri.endswith('?mode=ro') and kwargs.get('uri') is True
        connections.append(database_uri)
        return real_connect(database_uri, **kwargs)
    started = time.monotonic()
    with patch('probability_target_lookup.sqlite3.connect', side_effect=audited_connect):
        result = lookup(QUERY)
    elapsed = time.monotonic() - started
    assert len(connections) == 1
    assert len(result['cards']) == 2
    assert result['current_openness'] == 'UNKNOWN'
    assert all(card['truth_status'] == 'unverified' and card['claim_kind'] == 'concept'
               for card in result['cards'])
    assert ':open-problem-p0117-' in result['cards'][0]['logical_id']
    assert ':attempt-p0117-' in result['cards'][1]['logical_id']
    assertions += 6
    (ROOT / 'target_lookup_after.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    before_text = (ROOT / 'recall_raw.txt').read_text(encoding='utf-8')
    expected_before_slugs = [
        'four_two_hour_transcripts_2026_09_16',
        'fpp_width3_strip_time_constant_solved_2026_07_12',
        'prob1000_proofs_directory_audit_what_is_spent_and_what_is_live_2026_09_08',
    ]
    assert all(slug in before_text for slug in expected_before_slugs)
    assert '[absent] no memory contains: p0117' in before_text
    assertions += 2
    measurement = {
        'query': QUERY, 'before_command': 'python -X utf8 run_recall.py',
        'after_command': 'python -X utf8 test_target_lookup.py',
        'before_top3_target_id_hits': 0, 'after_target_cards': 1, 'after_prior_attempt_cards': 1,
        'before_elapsed_seconds': json.loads((ROOT / 'recall_measurement.json').read_text())['elapsed_seconds'],
        'after_lookup_elapsed_seconds': round(elapsed, 6),
        'assertions_passed': assertions, 'live_changes': False,
        'scope': 'One exact-ID query on the named population store; opt-in local prototype, not a general recall benchmark.',
    }
    (ROOT / 'retrieval_measurement.json').write_text(json.dumps(measurement, indent=2), encoding='utf-8')
    print(json.dumps(measurement, indent=2))


if __name__ == '__main__':
    main()
