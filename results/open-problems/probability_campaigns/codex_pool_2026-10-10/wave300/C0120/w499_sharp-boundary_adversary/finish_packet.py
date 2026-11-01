from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import runpy
import subprocess
import sys

base = Path(__file__).resolve().parent
runpy.run_path(str(base / 'build_packet.py'), run_name='__main__')
required = ['STATUS.md', 'SOURCE_STATUS.json', 'ATTEMPT.md', 'CLAIMS.jsonl', 'REVIEW_PACKET.md', 'REPORT.md']
assert all((base / name).is_file() for name in required)
claims = [json.loads(line) for line in (base / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
assert len(claims) == 3 and len({row['id'] for row in claims}) == 3
for row in claims:
    assert row['parent_problem_solved'] is False
    assert row['independent_reviewer']['id'] == 'w500'
    assert row['remaining_gap']
    assert row['status'] in {'conjecture', 'numerical evidence', 'sketch', 'proved special case', 'independently checked proof'}
peer_rows = [json.loads(line) for line in (base / 'review_input/w498_CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
peer_ids = {row['id'] for row in peer_rows}
verdicts = [json.loads(line) for line in (base / 'AUDIT_W498.jsonl').read_text(encoding='utf-8').splitlines() if line]
assert all(row['id'] in peer_ids for row in verdicts)
assert len(verdicts) == 4

patch_path = base / 'patches/01_C0120_source_scope.diff'
patch = patch_path.read_text(encoding='utf-8').splitlines()
assert patch[0].startswith('--- a/06_math_research/') and patch[1].startswith('+++ b/06_math_research/')
new = json.loads(patch[4][1:])
assert new['problem_id'] == 'C0120' and new['current_status'] == 'unverified'
assert 'ground-state' in new['status_search'] and 'UNKNOWN' in new['status_search']
check = subprocess.run(['git', '-C', '~/<private-repo>', 'apply', '--check', '--unidiff-zero', str(patch_path)], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30)
if check.returncode:
    raise RuntimeError('Read-only source patch check failed: ' + check.stderr)
source = json.loads((base / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
assert source['primary_source']['matches_intake_digest'] is True
measurements = json.loads((base / 'MEASUREMENTS.json').read_text(encoding='utf-8'))
bridge = json.loads((base / 'BRIDGE_MEASUREMENTS.json').read_text(encoding='utf-8'))
assert measurements['cases'] == 80 and measurements['status'] == 'PASS'
assert bridge['finite_identity_cases'] == 4 and bridge['paths_enumerated'] <= 256
assert bridge['scalar_event_cases'] == 6 and bridge['status'] == 'PASS'
assert 'every fixed' in next(row['statement'] for row in claims if row['id'].endswith('B2'))
validation = {'at_utc': datetime.now(timezone.utc).isoformat(), 'status': 'PASS', 'complete_required_deliverables': True, 'claim_rows': len(claims), 'scoped_peer_verdicts': len(verdicts), 'primary_pdf_digest_matches_intake': True, 'source_patch_check': {'command': 'git -C ~/<private-repo> apply --check --unidiff-zero ' + str(patch_path), 'exit_code': check.returncode, 'mutation': False}, 'layer_identity_cases': 80, 'complete_layer_cases': 4, 'paths_enumerated': bridge['paths_enumerated'], 'scalar_event_cases': 6, 'formal_proof_check': 'NOT_RUN', 'mathematical_proof_review': 'PENDING_W500', 'served_model_and_login_gate': 'UNVERIFIED'}
(base / 'VALIDATION.json').write_text(json.dumps(validation, indent=2) + '\n', encoding='utf-8')
runpy.run_path(str(base / 'publish_drafts.py'), run_name='__main__')
receipt = json.loads((base / 'SUBMISSION_RECEIPT.json').read_text(encoding='utf-8'))
with (base / 'REPORT.md').open('a', encoding='utf-8') as output:
    output.write('\nSubmitted DRAFT: ' + receipt['bundle_path'] + '; hook: ' + receipt['hook_path'] + '. Independent proof review pending; ingested=false; retrievable=UNKNOWN. Source patch passed git apply --check --unidiff-zero.\n')

names = ['SOURCE_STATUS.json', 'ATTEMPT.md', 'CLAIMS.jsonl', 'REVIEW_PACKET.md', 'REPORT.md', 'AUDIT_W498.jsonl', 'PEER_INPUT_HASHES.json', 'INDEPENDENT_BOUNDARY_20261010.md', 'INDEPENDENT_ZERO_TEMPERATURE_20261010.md', 'MEASUREMENTS.json', 'BRIDGE_MEASUREMENTS.json', 'VALIDATION.json', 'DRAFT_BUNDLE.json', 'DRAFT_HOOK.jsonl', 'SUBMISSION_RECEIPT.json', 'patches/01_C0120_source_scope.diff']
hashes = {'purpose': 'Review artifact hashes; not a store source manifest or integration receipt', 'at_utc': datetime.now(timezone.utc).isoformat(), 'artifacts': []}
for name in names:
    artifact = base / name
    raw = artifact.read_bytes()
    hashes['artifacts'].append({'path': str(artifact), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
submitted = Path(receipt['bundle_path'])
raw = submitted.read_bytes()
hashes['artifacts'].append({'path': str(submitted), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
(base / 'ARTIFACT_HASHES.json').write_text(json.dumps(hashes, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'validation': validation, 'submitted_bundle': receipt['bundle_path'], 'review_packet': str(base / 'REVIEW_PACKET.md'), 'proof_sha256': next(row['sha256'] for row in hashes['artifacts'] if row['path'].endswith('ATTEMPT.md'))}, indent=2), flush=True)
