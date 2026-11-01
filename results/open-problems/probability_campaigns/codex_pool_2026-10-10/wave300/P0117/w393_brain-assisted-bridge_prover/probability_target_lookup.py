"""Bounded exact-ID fallback for probability problems; read-only and opt-in.

This returns source cards with their existing status, not a proof or an openness
certificate. It deliberately does not run general lexical or graph recall.
"""
from __future__ import annotations

import argparse
from contextlib import closing
import json
from pathlib import Path
import re
import sqlite3
from urllib.parse import quote

DEFAULT_DATABASE = Path('~/math-brain-build/local/population/brain.sqlite3')
ID_PATTERN = re.compile(r'(?<![A-Za-z0-9])P[0-9]{4}(?![A-Za-z0-9])', re.IGNORECASE)


def target_id(query: str) -> str | None:
    identifiers = {match.group(0).upper() for match in ID_PATTERN.finditer(query)}
    return identifiers.pop() if len(identifiers) == 1 else None


def lookup(query: str, database: Path = DEFAULT_DATABASE) -> dict:
    identifier = target_id(query)
    result = {'query': query, 'target_id': identifier, 'database': str(database),
              'current_openness': 'UNKNOWN', 'cards': [], 'read_only': True}
    if identifier is None:
        result['reason'] = 'Need exactly one complete probability problem ID.'
        return result
    pid = identifier.lower()
    uri = 'file:' + quote(database.resolve().as_posix(), safe='/:') + '?mode=ro'
    with closing(sqlite3.connect(uri, uri=True, timeout=2)) as connection:
        connection.row_factory = sqlite3.Row
        connection.execute('PRAGMA query_only=ON')
        rows = connection.execute(
            '''SELECT id, title, body, metadata_json FROM nodes
               WHERE json_valid(metadata_json) AND
                 (json_extract(metadata_json, '$.bundle_entry_key') IN (?, ?)
                  OR lower(json_extract(metadata_json, '$.logical_id')) GLOB ?
                  OR lower(json_extract(metadata_json, '$.logical_id')) GLOB ?)
               ORDER BY CASE WHEN lower(json_extract(metadata_json, '$.logical_id'))
                                      GLOB ? THEN 0 ELSE 1 END, id
               LIMIT 3''',
            (f'op-{pid}', f'at-{pid}', f'*:open-problem-{pid}-*',
             f'*:attempt-{pid}-*', f'*:open-problem-{pid}-*'),
        ).fetchall()
    for row in rows:
        metadata = json.loads(row['metadata_json'])
        result['cards'].append({
            'id': row['id'], 'logical_id': metadata.get('logical_id'),
            'title': row['title'], 'statement_and_assumptions': row['body'],
            'truth_status': metadata.get('truth_status', 'unverified'),
            'claim_kind': metadata.get('claim_kind'), 'source_id': metadata.get('source_id'),
            'source_revision': metadata.get('source_revision'),
        })
    result['reason'] = ('Exact target/attempt cards; inspect their full hypotheses and primary sources.'
                        if result['cards'] else 'No matching exact-ID card in this named store.')
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query')
    parser.add_argument('--database', type=Path, default=DEFAULT_DATABASE)
    args = parser.parse_args()
    try:
        result = lookup(args.query, args.database)
    except (OSError, sqlite3.Error, ValueError) as error:
        print(json.dumps({'error': type(error).__name__, 'reason': str(error),
                          'current_openness': 'UNKNOWN', 'cards': []}))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
