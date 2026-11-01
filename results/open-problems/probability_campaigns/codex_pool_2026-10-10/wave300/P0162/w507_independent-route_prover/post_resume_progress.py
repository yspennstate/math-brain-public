from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess
import sys

root = Path(__file__).resolve().parent
comm_dir = Path('~/<private-repo>/12_cognitive_architecture/agent_mesh')
sys.path.insert(0, str(comm_dir))
import team_comm as tc

receipt = {'utc': datetime.now(timezone.utc).isoformat(), 'agent': 'w507',
    'authorization': 'Current user contract explicitly names the hooks1000 proposal path and pd_progress event command.',
    'hook': {'state': 'LOCAL_PROPOSAL'}, 'progress': {'posted': False}}
receipt_path = root / 'PROGRESS_RECEIPT.json'

def save():
    receipt_path.write_text(json.dumps(receipt, indent=2, default=str) + '\n', encoding='utf-8')

save()
proposal_lines = (root / 'proposals/math-w507.jsonl').read_text(encoding='utf-8').splitlines()
assert len(proposal_lines) == 1
proposal = json.loads(proposal_lines[0])
required = {'id', 'area', 'event', 'cue', 'fire_when', 'silent_when', 'text', 'evidence', 'proposer'}
assert required <= proposal.keys() and proposal['proposer'] == 'w507'
assert len(proposal['text']) <= 300
assert proposal['area'] == 'math' and proposal['event'] == 'stage-start'
resource = 'topic:hooks1000:math-w507'
mesh = None
claim = None
try:
    mesh = tc.mesh()
    claim = mesh.claim('w507', [resource], 'exclusive', 'Append one measured parity-influence guard to the w507 proposal file', 600)
    assert claim.get('acquired')
    receipt['hook']['claim'] = claim
    save()
    destination = Path('~/primary_directive/hooks1000/proposals/math-w507.jsonl')
    assert destination.parent.is_dir()
    existing = []
    if destination.exists():
        existing = [json.loads(line) for line in destination.read_text(encoding='utf-8').splitlines() if line.strip()]
    duplicate = [row for row in existing if row.get('id') == proposal['id']]
    if duplicate:
        assert all(row == proposal for row in duplicate), 'Same hook ID already has different content; no overwrite authorized.'
        receipt['hook']['state'] = 'ALREADY_PRESENT'
    else:
        with destination.open('a', encoding='utf-8') as out:
            out.write(json.dumps(proposal, ensure_ascii=False) + '\n')
        receipt['hook']['state'] = 'SUBMITTED_PROPOSAL'
    receipt['hook'].update({'path': str(destination), 'id': proposal['id'], 'audited': False, 'deployed': False})
except Exception as exc:
    receipt['hook']['error'] = str(exc)
finally:
    if mesh is not None:
        if claim is not None:
            try:
                receipt['hook']['release'] = mesh.release('w507', [resource])
            except Exception as exc:
                receipt['hook']['release_error'] = str(exc)
        mesh.conn.close()
    save()

event = ('P0162 w507: w509 KEEP L1-L7; exact bent-splice range and five-bit H>2I; '
    '7 draft entries/9 relations routed to codex-01a12190. Global FEI unproved; model and ingestion gates unverified.')
args = [sys.executable, '-B', '-X', 'utf8', '~/primary_directive/pd_progress.py',
    '--event', event, '--agent', 'w507', '--row', 'S1.P0162.w507', '--evidence', str(root / 'INTEGRATION_HANDOFF.json')]
result = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace')
receipt['progress'] = {'command': args, 'exit_code': result.returncode, 'stdout': result.stdout,
    'stderr': result.stderr, 'posted': result.returncode == 0}
save()

handoff_path = root / 'INTEGRATION_HANDOFF.json'
handoff = json.loads(handoff_path.read_text(encoding='utf-8'))
handoff['hook'] = receipt['hook']
handoff['progress_receipt'] = str(receipt_path)
handoff['delivery_receipt'] = str(root / 'PEER_DELIVERY_RESUMED.json')
handoff_path.write_text(json.dumps(handoff, indent=2) + '\n', encoding='utf-8')
with (root / 'RESUME_RESULTS.jsonl').open('a', encoding='utf-8') as out:
    out.write(json.dumps({'utc': datetime.now(timezone.utc).isoformat(), 'result': 'rolling hook and progress event',
        'hook': receipt['hook']['state'], 'progress_posted': receipt['progress']['posted'], 'receipt': str(receipt_path)}) + '\n')
print(json.dumps({'hook': receipt['hook']['state'], 'progress_posted': receipt['progress']['posted'],
    'receipt': 'PROGRESS_RECEIPT.json'}))
