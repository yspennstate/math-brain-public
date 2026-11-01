"""Check the public export's file hashes, row counts, and typed row digests.

Run from any working directory. This checks the released bytes, not the private
working store, source rights, theorem correctness, or benchmark contamination.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sqlite3
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'src'), str(ROOT / 'tools')]
from import_store import read_export, build_db, digest_failures
from math_brain.models import GraphEdge, EdgeKind, content_hash


def check():
    export = ROOT / 'export/population'
    manifest = json.loads((export / 'MANIFEST.json').read_text())
    errors = []
    counts = {}
    for table, expected in manifest['counts'].items():
        data = (export / f'{table}.jsonl').read_bytes()
        counts[table] = len(data.splitlines())
        if counts[table] != expected:
            errors.append({'table': table, 'check': 'row_count'})
        if hashlib.sha256(data).hexdigest() != manifest['digests'][table]:
            errors.append({'table': table, 'check': 'file_sha256'})
    with tempfile.TemporaryDirectory() as tmp:
        db = Path(tmp) / 'restored.sqlite3'
        build_db(db, read_export())
        bad_nodes, bad_manifests = digest_failures(db)
        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        failures = {'nodes': len(bad_nodes), 'bundle_manifests': len(bad_manifests)}
        for table in ('claims', 'evidence', 'mistakes', 'reflexes'):
            failures[table] = sum(
                content_hash(json.loads(row['payload_json'])) != row['digest']
                for row in conn.execute(f'SELECT * FROM {table}')
            )
        failures['edges'] = sum(
            GraphEdge(id=r['id'], source_id=r['source_id'], target_id=r['target_id'],
                kind=EdgeKind(r['kind']), rationale=r['rationale'], weight=r['weight'],
                metadata=json.loads(r['metadata_json']), created_at=r['created_at']).digest()
            != r['digest'] for r in conn.execute('SELECT * FROM edges')
        )
        fk = len(conn.execute('PRAGMA foreign_key_check').fetchall())
        integrity = conn.execute('PRAGMA integrity_check').fetchone()[0]
        conn.close()
    passed = not errors and not any(failures.values()) and fk == 0 and integrity == 'ok'
    result = {
        'passed': passed, 'counts': counts, 'tables': len(counts),
        'total_rows': sum(counts.values()), 'manifest_errors': errors,
        'row_digest_failures': failures, 'foreign_key_violations': fk,
        'sqlite_integrity': integrity,
        'scope': 'Released export only; not a private-store, rights, privacy, or evaluation certification.'
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(check())
