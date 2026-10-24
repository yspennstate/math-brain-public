from pathlib import Path
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MESH_ROOT = Path('~/<private-repo>/12_cognitive_architecture/agent_mesh')
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
validation = json.loads((ROOT / 'measurements/packet_validation.json').read_text(encoding='utf-8'))
assert validation['status'] == 'PASS' and validation['claim_rows'] == 10
assert validation['peer_KEEPs'] == 13 and validation['historical_FIXs'] == 1

for recipient, body in [
    ('w348', 'DONE referee packet: ~/brain_workers/w350/REVIEW_PACKET.md. Current L1-L4 KEEP, original L4 FIX repaired by the U_2/T_2 moment-domain split. Exact tensor sharpness and product support/factorial calculations independently reproduced. Use my verdicts on your author bundle; my duplicate lemma copy stays unsubmitted. No universal Taylor input or parent proof certified.'),
    ('w349', 'DONE independent checks C001-C007, C009, C010: ~/brain_workers/w350/reviews/w349_verdicts.jsonl. C008/W remains UNPROVED. C006 strict posterior factorization and C007 conditional whitening bridge checked analytically; no quadrature number certified. My new counterargument concerns only your stronger operator-norm surrogate and awaits w353: OPERATOR_WEIGHTED_COUNTEREXAMPLE.md.'),
]:
    p = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(MESH_ROOT / 'team_comm.py'), 'say', '--as', 'w350', '--to', recipient, '--kind', 'done', body], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=45, env=env)
    receipt = {'recipient': recipient, 'kind': 'done', 'command': 'team_comm.py say', 'body': body, 'returncode': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}
    with (ROOT / 'COMM_RECEIPTS.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(receipt) + '\n')
    print(recipient, 'TEAM_DONE_EXIT', p.returncode, p.stdout[:500], p.stderr[:300], flush=True)
    if p.returncode:
        # Explicitly named-peer mesh is authorized by this worker brief; no agents are started.
        q = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(MESH_ROOT / 'agent_mesh.py'), 'send', '--agent', 'w350', '--to', recipient, '--topic', 'P0017-proofswarm', '--kind', 'message', '--body', body], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=45, env=env)
        with (ROOT / 'COMM_RECEIPTS.jsonl').open('a', encoding='utf-8') as f:
            f.write(json.dumps({'recipient': recipient, 'kind': 'done-fallback', 'body': body, 'returncode': q.returncode, 'stdout': q.stdout, 'stderr': q.stderr}) + '\n')
        print(recipient, 'DIRECT_DONE_EXIT', q.returncode, q.stdout[:500], q.stderr[:300], flush=True)

packet_path = ROOT / 'REVIEW_PACKET.json'
packet = json.loads(packet_path.read_text(encoding='utf-8'))
packet['new_counterexample_review_request'] = {'reviewer': 'w353', 'message_id': 'msg-372c00540a', 'status': 'PENDING', 'claim_ids': ['w350-C005', 'w350-C006'], 'artifact': str(ROOT / 'OPERATOR_WEIGHTED_COUNTEREXAMPLE.md')}
packet['statement_correction_review_request'] = {'reviewer': 'claude-4a88bc43', 'message_id': 'msg-312a2dc8e5', 'status': 'PENDING', 'artifact': str(ROOT / 'reviews/L4_DOMAIN_FIX.md')}
packet['completion_state'] = 'NEEDS_REVIEW'
packet_path.write_text(json.dumps(packet, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
(ROOT / 'context/final_mesh_read.txt').write_text('2026-10-10 final read: w348 and w349 announced their complete P0017 author packets. Requested L4 domain repair and w349 C006/C007/C009/C010 checks are covered by the saved independent verdicts. No w353 audit of the new author reductions or counterargument was received. Replies and audit-request receipts are in COMM_RECEIPTS.jsonl.\n', encoding='utf-8')
progress_path = ROOT / 'PROGRESS_PENDING.json'
progress = json.loads(progress_path.read_text(encoding='utf-8'))
progress['final_event'] = 'w350 P0017: 13 scoped KEEP + 1 repaired historical FIX; exact checks and 15 quoted relations PASS; 6 concept/definition cards queued, 4 peer lemmas and 2 own counterargument drafts held .part; own review pending, no parent proof.'
progress_path.write_text(json.dumps(progress, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

status_path = ROOT / 'STATUS.md'
lines = status_path.read_text(encoding='utf-8').splitlines()
lines[0] = 'STATE: NEEDS_REVIEW'
next_line = 'NEXT: w353 audit Claims A-B and C005-C006: adjoint domains, ORIGINAL-posterior weighting and compact-isotropic transfer; reviewer check U_2/T_2 repair before integration.'
for i, line in enumerate(lines):
    if line.startswith('NEXT:'):
        lines[i] = next_line
        break
lines += ['', '2026-10-10: Referee deliverables complete and measured: 13 KEEP plus one repaired historical FIX, 10 claim rows, 15 relations with both ends quoted, three draft bundles validated PASS. Six cards submitted; four peer lemmas and two own author drafts remain unsubmitted .part. w353 request msg-372c00540a and Claude statement-correction request msg-312a2dc8e5 delivered. Own proof review, ingestion and retrieval remain unverified. Universal retention and actual (W) are unproved in this packet. Optional CPU gate preserved; no live store writes or parent-proof claim.']
status_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('STATE: NEEDS_REVIEW', flush=True)
print(next_line, flush=True)
