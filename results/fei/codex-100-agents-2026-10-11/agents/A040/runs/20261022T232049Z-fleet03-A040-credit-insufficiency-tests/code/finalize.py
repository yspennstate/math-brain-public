"""Local schema and byte receipts; does not certify mathematical conclusions."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT.parents[1]
BASE = Path('~/brain_workers/FEI100_20261011')
PROTOCOL = Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def receipt(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

protocol = read(PROTOCOL)['required_per_run']
claims = read(ROOT / 'CLAIMS.json')
assert isinstance(claims, list), type(claims)
for claim in claims:
    assert set(claim) == set(protocol['claim_fields']), claim['claim_id']
    statement = claim['exact_statement']
    assert isinstance(statement, str)
    assert hashlib.sha256(statement.encode('utf-8')).hexdigest() == claim['statement_sha256'], claim['claim_id']
progress = read(ROOT / 'PROGRESS.json')
expected = {x.split(' (')[0] for x in protocol['progress_fields']}
assert set(progress) == expected, (set(progress) - expected, expected - set(progress))
assert progress['packet_ids'] == ['A040']
assert (ROOT / 'PROGRESS.json').read_bytes() == (ROOT / 'PACKET_DELTA.json').read_bytes()
report = (ROOT / 'REPORT.md').read_text(encoding='utf-8')
for heading in protocol['report_fields']:
    assert heading in report, heading
assert '## Universal bridge\n' in report
assert len(report.split('## Universal bridge\n')[-1].strip().split('\n\n')) == 1
status = (AGENT / 'STATUS.md').read_text(encoding='utf-8').splitlines()
assert len(status) == 2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
outputs = [read(ROOT / 'out' / name) for name in ('RESULT.json', 'SINGLETON.json', 'INDEPENDENT_AUDIT.json')]
assert all(item['status'] == 'PASS' for item in outputs)
assert [item['checks'] for item in outputs] == [3041, 180, 104]
lean = read(ROOT / 'out/LEAN_RESULT.json')
assert 'SETUP_UNVERIFIED' in json.dumps(lean)
assert 'false' in json.dumps(lean).lower()
source = BASE / 'agents/A046/runs/20261021T192754Z-fleet03-A046-current-candidate-intake'
sources = [PROTOCOL, BASE / 'BOARD.md', BASE / 'claude/B08/STREAM_NOTES.md']
sources += [source / name for name in ('REPORT.md', 'PROOF.md', 'CLAIMS.json')]
save(ROOT / 'out/SOURCE_MANIFEST.json', {
    'purpose': 'Byte identities of reviewed sources; receipts are not proof acceptance.',
    'sources': [receipt(path) for path in sources]})
destination = ROOT / 'out/PERSISTENCE_RECEIPTS.json'
files = sorted(path for path in ROOT.rglob('*') if path.is_file() and path != destination)
assert all(path.stat().st_size < 20 * 1024 * 1024 for path in files)
save(destination, {
    'status': 'PASS', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'schema_fields': 'exact protocol sets', 'claims_checked': len(claims),
    'exact_assertions_passed': 3325, 'formal_target_verified': False,
    'lean_status': 'SETUP_UNVERIFIED', 'persistence_scope': 'local files only',
    'mirror_copy_verified': False, 'new_claim_independent_review': 'pending',
    'full_fei_status': 'OPEN', 'self_receipt_excluded': True,
    'artifacts': [receipt(path) for path in files],
    'rolling_files': [receipt(AGENT / name) for name in ('STATUS.md', 'WORKLOG.md', 'LEARNED.md')]})
print(json.dumps({'status': 'PASS', 'claims': len(claims), 'exact_checks': 3325,
                  'files_receipted': len(files), 'max_file_bytes': max(path.stat().st_size for path in files),
                  'receipt': str(destination), 'full_fei': 'OPEN'}))
