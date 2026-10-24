from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
manifest = json.loads((base / 'ARTIFACT_HASHES.json').read_text(encoding='utf-8'))
proof_sha = next(row['sha256'] for row in manifest['artifacts'] if row['path'].endswith('ATTEMPT.md'))
submission = json.loads((base / 'SUBMISSION_RECEIPT.json').read_text(encoding='utf-8'))
mesh = '~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
messages = [
    ('w500', 'C0120 w499 independent B2 review ready: ~/brain_workers/w499/REVIEW_PACKET.md; proof ATTEMPT.md SHA256 ' + proof_sha + '. New complete-layered Gaussian graph preserves Theta(n/log n) variance yet path changes with probability tending to one at OU N^-1/2 and overlap/n tends to one. Check uniform gap density and top-two reversal event independently. Graph degree grows; no planar-lattice refutation. Three claims, four scoped mathematical KEEP verdicts on w498; proof/served-model/login gates pending. ARTIFACT_HASHES.json freezes exact files.'),
    ('w498', 'Scoped mathematical KEEP for L1/L1M/L2/L3: ~/brain_workers/w499/AUDIT_W498.jsonl and PEER_INPUT_HASHES.json. Disjoint stronger bridge B2 now fully written in ATTEMPT.md SHA256 ' + proof_sha + ': complete layered graph, Theta(n/log n) variance, polynomial OU path change, overlap/n ->1. Extra logarithmic premise cannot rescue a general event-based bridge; fixed planar geometry not covered. w500 review requested, served identity/login evidence unavailable.'),
    ('codex-01a12190', 'C0120 boundary adversary w499 review-ready: ~/brain_workers/w499/REVIEW_PACKET.md and ARTIFACT_HASHES.json; ATTEMPT.md SHA256 ' + proof_sha + '. Scoped KEEP: w498 L1/L1M/L2/L3 mathematical content only. Own new B2 general layered-graph bridge counterexample is author proof pending w500; exact full-lattice gap unresolved. Draft ' + submission['bundle_path'] + ' holds concept material only. Response-side served-model/login evidence unavailable, no promotion or parent-solved claim. Source PDF digest verified; source scope patch read-only apply check passes.'),
]
receipts = []
for peer, body in messages:
    # The brief explicitly authorizes the existing mesh for these named peers.
    # Direct mesh routing avoids a nonexistent/stale team membership lookup.
    args = [sys.executable, '-X', 'utf8', mesh, 'send', '--agent', 'w499', '--to', peer, '--topic', 'probability300-C0120-boundary', '--kind', 'message', '--body', body]
    try:
        run = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
        row = {'peer': peer, 'exit_code': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr, 'delivered': run.returncode == 0}
    except subprocess.TimeoutExpired:
        row = {'peer': peer, 'delivered': False, 'status': 'TIMEOUT_60S'}
    receipts.append(row)
    (base / 'FINAL_NOTIFICATION_RECEIPTS.json').write_text(json.dumps(receipts, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(row), flush=True)

jobs = [
    [sys.executable, '-X', 'utf8', '~/primary_directive/pd_progress.py', '--event', 'C0120 stronger layered-graph bridge counterexample and source-scope patch ready; 84 finite checks, 6 scalar cases; draft submitted, w500 review pending.', '--agent', 'w499', '--row', 'S1.C0120.B2', '--evidence', str(base / 'CLAIMS.jsonl')],
    [sys.executable, '-X', 'utf8', '~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py', 'read', '--as', 'w499'],
]
for index, args in enumerate(jobs):
    try:
        run = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
        row = {'job': 'progress' if index == 0 else 'team_read', 'exit_code': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr}
    except subprocess.TimeoutExpired:
        row = {'job': 'progress' if index == 0 else 'team_read', 'status': 'TIMEOUT_60S'}
    receipts.append(row)
    (base / 'FINAL_NOTIFICATION_RECEIPTS.json').write_text(json.dumps(receipts, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(row), flush=True)
