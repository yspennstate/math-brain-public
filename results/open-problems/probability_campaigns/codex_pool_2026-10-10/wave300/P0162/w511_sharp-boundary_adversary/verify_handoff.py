"""Verify a saved reviewed handoff without changing a live store or running tests."""
import hashlib
import json
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
SUBMITTED = Path('~/math-brain-inbox/w511/bundle_002.json')
REFEREE = Path('~/brain_workers/w512/VERDICTS.jsonl')
STORE = Path('~/math-brain-build/local/population/brain.sqlite3')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(result):
    (BASE / 'INTEGRATION_CHECK.json').write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

bundle = json.loads((BASE / 'bundle_002.json').read_text(encoding='utf-8'))
receipt = json.loads((BASE / 'REVIEW_RECEIPT.json').read_text(encoding='utf-8'))
local_claims = receipt['claims']
targets = {row['target'] for row in local_claims}
referee_rows = [json.loads(line) for line in REFEREE.read_text(encoding='utf-8').splitlines()
                if line.strip()]
selected = [row for row in referee_rows if row.get('target') in targets]
receipt_matches = len(selected) == 4 and all(row in selected for row in local_claims)
evidence_files = ['bundle_002.json', 'REVIEW_RECEIPT.json', 'ATTEMPT.md',
                  'CLAIMS.jsonl', 'SOURCE_STATUS.json', 'measurements.json',
                  'affine_audit_measurements.json', 'REPORT.md']
result = {
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'task': 'P0162-w511 reviewed bundle handoff',
    'operation': 'file hashes and bounded read-only lookup; no new experiment',
    'bundle_slug': bundle['bundle_slug'],
    'submitted_path': str(SUBMITTED),
    'local_submitted_byte_match': (BASE / 'bundle_002.json').read_bytes() == SUBMITTED.read_bytes(),
    'sha256': {str(BASE / name): digest(BASE / name) for name in evidence_files},
    'submitted_sha256': digest(SUBMITTED),
    'referee_verdicts_path': str(REFEREE),
    'scoped_receipt_matches_referee_file': receipt_matches,
    'scoped_keep_count': sum(row.get('verdict') == 'KEEP' for row in selected),
    'expected_entries': [{'key': entry['key'], 'logical_name': entry['logical_name'],
                          'kind': entry['kind'], 'title': entry['title']}
                         for entry in bundle['entries']],
    'ingestion': {'status': 'not yet checked'},
    'retrieval': {'status': 'not checked; store lookup is not a recall-quality measurement'},
    'served_model_evidence': {'author': 'UNVERIFIED', 'referee': 'UNVERIFIED',
                             'reason': 'No response-side transcript receipt saved in this packet.'},
    'scope': 'Four reviewed auxiliary claims; no full FEI or novelty certification.',
}
save(result)
start = time.monotonic()
conn = None
try:
    conn = sqlite3.connect(f'file:{STORE.as_posix()}?mode=ro', uri=True, timeout=2)
    conn.row_factory = sqlite3.Row
    conn.set_progress_handler(lambda: int(time.monotonic() - start > 8), 1000)
    titles = [entry['title'] for entry in bundle['entries']]
    placeholders = ','.join('?' for _ in titles)
    rows = [dict(row) for row in conn.execute(
        f'SELECT id,kind,title,metadata_json FROM nodes WHERE title IN ({placeholders}) LIMIT 21',
        titles)]
    result['ingestion'] = {
        'status': 'candidate cards observed' if rows else 'no exact-title cards observed in checked store',
        'store': str(STORE), 'mode': 'ro',
        'matched_titles': len({row['title'] for row in rows}),
        'expected_titles': len(titles), 'nodes': rows,
        'limitations': 'Exact-title lookup only; other stores, altered titles and integration receipts not checked.'}
except (sqlite3.Error, OSError) as exc:
    result['ingestion'] = {'status': 'UNCONFIRMED', 'store': str(STORE), 'mode': 'ro',
                           'error': str(exc)}
finally:
    if conn is not None:
        conn.close()
result['lookup_seconds'] = time.monotonic() - start
save(result)
row = {'id': 'S1.P0162.w511.handoff-resume', 'type': 'handoff-verification',
       'checked_at_utc': result['checked_at_utc'],
       'submission_sha256': result['submitted_sha256'],
       'local_submitted_byte_match': result['local_submitted_byte_match'],
       'scoped_keep_count': result['scoped_keep_count'],
       'scoped_receipt_matches_referee_file': receipt_matches,
       'ingestion_observation': result['ingestion']['status'],
       'evidence': str(BASE / 'INTEGRATION_CHECK.json'),
       'remaining_gap': 'Coordinator integration/provenance and retrieval receipt; served-model evidence.'}
with (BASE / 'HANDOFF_ROWS.jsonl').open('a', encoding='utf-8') as handle:
    handle.write(json.dumps(row, ensure_ascii=False) + '\n')
print(json.dumps(row, ensure_ascii=False))
