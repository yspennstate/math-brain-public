"""Authorized narrow handoff through the existing mesh; no agent is launched."""
from pathlib import Path
import json
import datetime as dt
import sys
import argparse

sys.dont_write_bytecode = True
sys.path.insert(0, '~/<private-repo>/12_cognitive_architecture/agent_mesh')
import team_comm

root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--phase', choices=('derivation','audit'), default='derivation')
phase = parser.parse_args().phase
artifact = root / 'INDEPENDENT_DERIVATION.md'
messages = {
    'w390': f'P0117 w391 found: independent derivation saved BEFORE your proof was read: {artifact.as_posix()}. Constant laws admit horizontal bigeodesics; a supercritical minimum-atom law also admits monotone bigeodesics. Independent finite-strip barrier uses expensive horizontal cut edges and cheap exterior detours. I am now auditing your precise proof; unrestricted confinement is the missing full-target bridge.',
    'w392': f'P0117 w391 review request: independently check C01-C03 in {(root / "CLAIMS.jsonl").as_posix()} and {artifact.as_posix()}. Most useful check: C03 concatenates independent forward/backward directed surviving minimum-weight rays; every segment is Manhattan optimal. Also check C02 cut counting despite backtracking and its simultaneous-strip quantifiers. No full-target or novelty claim; draft concepts only until your check.',
}
if phase == 'audit':
    messages = {
        'w390': f'P0117 w391 done: five scoped KEEP verdicts at {(root / "AUDIT_W390.jsonl").as_posix()}; packet {(root / "REVIEW_PACKET.md").as_posix()}. Cut/connector counts, disjoint supports, dyadic summability and simultaneous-ray quantifiers survive. Full-target confinement remains a gap. Own conditional minimum-atom and axial-staircase counterexamples strengthen boundary notes; they do not refute the nonatomic target. Finite tests NOT RUN because fresh resource gate reported distress/throttle.',
        'w392': f'P0117 w391 final review packet: {(root / "REVIEW_PACKET.md").as_posix()}. Five independent KEEP verdicts for w390 are saved in AUDIT_W390.jsonl. Please check own C01-C04, especially positive-survival minimum-atom C03 and the constant-law axial staircase C04. Four math-only DRAFT entries and seven relations were submitted, with reviewed/ingested/retrievable unverified. Review only these exact claims; no unrestricted proof or novelty claim.',
    }
receipt_file = root / 'PEER_DELIVERY.jsonl'
prior = [json.loads(line) for line in receipt_file.read_text(encoding='utf-8').splitlines()] if receipt_file.exists() else []
mesh = team_comm.mesh()
try:
    team_comm.ensure(mesh, 'w391')
    for recipient, body in messages.items():
        if any(row.get('recipient')==recipient and row.get('phase','derivation')==phase and row.get('state')=='sent' for row in prior):
            print(json.dumps({'recipient':recipient,'phase':phase,'state':'already-sent'}),flush=True)
            continue
        team_comm.ensure(mesh, recipient)
        receipt = mesh.send('w391', recipient, f'P0117/w391/{phase}', body, kind='request' if recipient == 'w392' else 'message')
        team_comm.ring(recipient)
        row = {'recipient': recipient, 'phase':phase, 'state': 'sent', 'at_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'receipt': receipt}
        with receipt_file.open('a', encoding='utf-8') as stream:
            stream.write(json.dumps(row, default=str) + '\n')
        print(json.dumps(row, default=str), flush=True)
finally:
    mesh.close()
