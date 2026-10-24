"""Use the installed named-peer registration fallback; do not launch an agent."""
import json
import os
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
peer = Path('~/brain_workers/w434')
receipt = {'sender': 'w432', 'recipient': 'w434', 'child_agents_started': 0, 'status': 'NOT_SENT'}
try:
    state = (peer / 'STATUS.md').read_text(encoding='utf-8').splitlines()[0]
    if state == 'STATE: DONE':
        raise RuntimeError('Referee session is DONE; do not revive it')
    sys.path.insert(0, '~/<private-repo>/12_cognitive_architecture/agent_mesh')
    from team_comm import mesh, ensure, ring
    m = mesh()
    ensure(m, 'w432')
    # This is the installed communication fallback for an unregistered existing worker.
    # It creates mesh presence metadata, never a process, service, session, or AI worker.
    previous_directory = os.getcwd()
    try:
        os.chdir(peer)
        ensure(m, 'w434')
    finally:
        os.chdir(previous_directory)
    body = ('Latest P0043 proof packet: ~/brain_workers/w432/REVIEW_PACKET.md. '
            'Eight partial author proofs L01-L08; w433 reviewed L02-L06 and tightened the regular-tree bound 27 to 12, independently rederived here. '
            'Only G01 remains unproved. Two source corrections. Numerical checks HELD by distress gate. '
            'Latest inbox draft bundle_002.json contains nine concepts and nine relations; old bundle_001 is preserved. '
            'Please KEEP/FIX/DROP exact rows; no full-target solution or novelty claimed.')
    result = m.send('w432', 'w434', 'P0043', body, kind='request')
    ring('w434')
    receipt.update({'status': 'SENT', 'message': result, 'peer_state': state})
except Exception as exc:
    receipt['error'] = str(exc)
(root / 'REFEREE_HANDOFF.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt, ensure_ascii=False))
