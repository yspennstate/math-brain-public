"""Submit this task's explicitly authorized DRAFT inbox file after lease assertion."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

root = Path(__file__).resolve().parent
mesh = '~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
inbox = Path('~/math-brain-inbox/w531')
target = inbox / 'bundle_001.json'
draft = root / 'drafts/bundle_001.json'
data = draft.read_bytes()
parsed = json.loads(data)
assert parsed['spec'] == 'mathbrain-draft-v1' and parsed['author_agent'] == 'w531'
assert len(parsed['entries']) == 4 and len(parsed['relations']) == 4
assert all(e['kind'] in {'concept', 'definition'} for e in parsed['entries'])
assert all(e['source']['license'] == 'owner-own-work' for e in parsed['entries'])
command = [sys.executable, '-X', 'utf8', mesh, 'assert', '--agent', 'w531', '--resource', str(inbox)]
receipt = subprocess.run(command, capture_output=True, text=True)
if receipt.returncode:
    if 'locked' in (receipt.stdout + receipt.stderr).lower():
        raise RuntimeError('Mesh database locked: no inbox mutation and no lease bypass.')
    # Reacquire an expired lease, without forcing or bypassing a conflicting holder.
    subprocess.run([sys.executable, '-X', 'utf8', mesh, 'claim', '--agent', 'w531',
                    '--resource', str(inbox), '--mode', 'write', '--purpose',
                    'Finish own P0309 review-only DRAFT submission', '--ttl', '15m'], check=True)
    receipt = subprocess.run(command, capture_output=True, text=True, check=True)
inbox.mkdir(parents=True, exist_ok=True)
resolved = inbox.resolve()
part = inbox / 'bundle_001.w531.part'
assert target.resolve().parent == resolved and part.resolve().parent == resolved
if target.exists():
    if target.read_bytes() != data:
        raise RuntimeError('Existing draft differs; preserved it without overwrite.')
else:
    with part.open('xb') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    part.rename(target)
if target.read_bytes() != data:
    raise RuntimeError('Draft copy differs from local review artifact.')
submission = json.loads((root / 'BRAIN_SUBMISSION.json').read_text(encoding='utf-8'))
submission['submitted'] = {'state': 'FILE_COMPLETE', 'path': str(target),
                           'time_utc': datetime.now(timezone.utc).isoformat(),
                           'lease_assertion': 'passed', 'entries': 4, 'relations': 4}
(root / 'BRAIN_SUBMISSION.json').write_text(json.dumps(submission, indent=2), encoding='utf-8')
status = json.loads((root / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status['brain_states'] = {'prepared': True, 'submitted': True, 'reviewed': False,
                         'ingested': None, 'retrievable': None}
status['proof_status'] = 'Author-proved conditional pressure/entropy reductions and harmonic reference lemmas; no independently checked Riesz crystallization proof'
(root / 'SOURCE_STATUS.json').write_text(json.dumps(status, indent=2), encoding='utf-8')
gate = {'author': {'agent': 'w531', 'served_model_status': 'UNKNOWN',
                   'response_side_evidence': None,
                   'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
                   'requested_service_tier': 'Fast',
                   'requested_settings_are_not_served_model_evidence': True},
        'referee': {'agent': 'w533', 'served_model_status': 'UNKNOWN',
                    'response_side_evidence': None, 'verdict': 'PENDING'},
        'scoped_keeps': [], 'parent_problem_solved_claim': False,
        'current_openness': 'UNKNOWN', 'promotion': 'DRAFT concepts only',
        'formal_check': None}
(root / 'review_packet/REVIEW_GATES.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')

# Keep the historical first-run claim bound to the archived passing receipt.
ledger = [json.loads(s) for s in (root / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
for row in ledger:
    if row['id'] == 'w531-P0309-M1':
        row['source']['path'] = str(root / 'verification_initial/control_results.json')
        row['proof_or_counterexample'] = 'Initial command: python -X utf8 ~/brain_workers/w531/check_controls.py; the exact 295-check source, PASS receipt and admitting gate are archived in verification_initial. The later root receipt is a separate GATED attempt.'
(root / 'CLAIMS.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in ledger), encoding='utf-8')
report = (root / 'REPORT.md').read_text(encoding='utf-8')
report = report.replace('Measured command:', 'Measured initial command:')
report = report.replace('The fresh governor/direct resource gate is in compute_gate_receipt.json.',
                        'The passing fresh resource gate is archived in verification_initial/compute_gate_receipt.json.')
report += '\nSubmission: completed review-only DRAFT at ~/math-brain-inbox/w531/bundle_001.json (4 entries, 4 relations). Review pending; ingestion and retrieval not verified. No scoped KEEP or response-side served-model evidence is yet available; review_packet/REVIEW_GATES.json records those gates.\n'
(root / 'REPORT.md').write_text(report, encoding='utf-8')
readme = (root / 'review_packet/README.md').read_text(encoding='utf-8')
readme += '\nThe shared DRAFT mirror is ~/math-brain-inbox/w531/bundle_001.json. REVIEW_GATES.json records no scoped KEEP and UNKNOWN author/referee served identity. Requested settings are not response-side served-model evidence. The model/independent-review gates remain for the validating coordinator.\n'
(root / 'review_packet/README.md').write_text(readme, encoding='utf-8')
# These identify the review files only; no store digest/seal/MAC or draft manifest is built.
identities = {'meaning': 'Review-file identity only, not a mathematical proof or a store manifest', 'files': []}
for name in ['PRESSURE_ROUTE.md', 'CLAIMS.jsonl', 'review_packet/README.md', 'verification_initial/control_results.json']:
    p = root / name
    identities['files'].append({'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
(root / 'review_packet/REVIEW_FILE_IDENTITIES.json').write_text(json.dumps(identities, indent=2), encoding='utf-8')
with (root / 'HANDOFF_LOG.jsonl').open('a', encoding='utf-8') as f:
    f.write(json.dumps({'date': '2026-10-10', 'kind': 'draft-submission',
                        'state': 'FILE_COMPLETE', 'path': str(target), 'entries': 4,
                        'relations': 4, 'reviewed': False, 'ingested': 'NOT_VERIFIED',
                        'retrievable': 'NOT_VERIFIED'}) + '\n')
print(json.dumps({'draft_submitted': str(target), 'claims': len(ledger), 'entries': 4,
                  'relations': 4, 'scoped_keeps': 0, 'ingestion': 'NOT_VERIFIED',
                  'pressure_route_sha256': identities['files'][0]['sha256']}))
