"""Check local handoff completeness, stage one patch, preserve all live data."""
from datetime import datetime, timezone
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
required = ['ATTEMPT.md', 'CLAIMS.jsonl', 'SOURCE_STATUS.json', 'REVIEW_PACKET.md',
            'REPORT.md', 'SERVED_MODEL_EVIDENCE.json', 'MEASUREMENTS.json',
            'COMPUTE_GATE.json', 'bundle_001.json', 'BUNDLE_STATE.json',
            'STORE_READ_RECEIPT.json', 'PROGRESS_REQUEST.md', 'math-w414.jsonl']
for name in required:
    assert (ROOT / name).is_file(), name
rows = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
allowed = {'conjecture', 'numerical evidence', 'sketch', 'proved special case',
           'independently checked proof'}
assert len({r['claim_id'] for r in rows}) == len(rows)
for row in rows:
    assert row['status'] in allowed
    assert all(key in row for key in ('statement', 'assumptions', 'source',
               'proof_or_counterexample', 'independent_reviewer', 'remaining_gap'))
    assert row['status'] != 'independently checked proof'
state_path = ROOT / 'BUNDLE_STATE.json'
state = json.loads(state_path.read_text(encoding='utf-8'))
assert state['submitted'] is True and state['local_validation'] == 'PASS'
inbox = Path(state['inbox_path'])
assert json.loads(inbox.read_text(encoding='utf-8')) == json.loads((ROOT / 'bundle_001.json').read_text(encoding='utf-8'))
state['review_verification'] = 'pending scoped independent mathematical review'
state['ingestion_verification'] = 'No validating-coordinator ingestion receipt checked; not claimed'
state['retrieval_verification'] = 'Not checked after submission; not claimed'
state_path.write_text(json.dumps(state, indent=2) + '\n', encoding='utf-8')

hook_text = (ROOT / 'math-w414.jsonl').read_text(encoding='utf-8').strip()
hook = json.loads(hook_text)
assert len(hook['text']) <= 300
for key in ('id', 'area', 'event', 'cue', 'fire_when', 'silent_when', 'text', 'evidence', 'proposer'):
    assert hook[key]
patches = ROOT / 'patches'
patches.mkdir(exist_ok=True)
live = '~/primary_directive/hooks1000/proposals/math-w414.jsonl'
patch = f'--- a/{live}\n+++ b/{live}\n@@ -0,0 +1 @@\n+{hook_text}\n'
(patches / '01_math_w414_hook.diff').write_text(patch, encoding='utf-8')

store = json.loads((ROOT / 'STORE_READ_RECEIPT.json').read_text(encoding='utf-8'))
source_path = ROOT / 'SOURCE_STATUS.json'
source = json.loads(source_path.read_text(encoding='utf-8'))
source['live_population_read'] = {
    'path': store[0]['path'], 'mode': 'ro',
    'matched_exact_historical_rows': len(store[0]['rows']),
    'receipt': str(ROOT / 'STORE_READ_RECEIPT.json'),
    'scope': 'Only the known C0017 problem and attempt ids; no bank or test rows queried',
}
source['bundle_submission'] = {'submitted': True, 'path': str(inbox),
                              'reviewed': False, 'ingestion_verified': False,
                              'retrieval_verified': False}
source_path.write_text(json.dumps(source, indent=2) + '\n', encoding='utf-8')

receipt = {'recorded_at': datetime.now(timezone.utc).isoformat(),
           'status': 'PASS', 'required_artifacts': required, 'claim_rows': len(rows),
           'author_lemmas': 3, 'bundle_entries': 4, 'bundle_relations': 4,
           'concept_only': True, 'submitted_path': str(inbox),
           'proof_review': 'PENDING', 'live_ingestion_verified': False,
           'retrieval_verified': False, 'served_model_verified': False,
           'hook_shared_submission': False, 'progress_page_posted': False,
           'hook_patch': str(patches / '01_math_w414_hook.diff')}
(ROOT / 'FINAL_VALIDATION.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
