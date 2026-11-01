"""Send this task's authorized, directed handoffs through the existing mesh.

No AI process is launched. Registration uses team_comm's existing ensure helper.
Only w391 and w392 are accepted as recipients. All receipts stay in w390.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
MESH_DIR = Path('~/<private-repo>/12_cognitive_architecture/agent_mesh')


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument('recipient', choices=('w391', 'w392'))
    p.add_argument('phase', choices=('statement', 'review'))
    a = p.parse_args()
    if (a.recipient, a.phase) not in {('w391', 'statement'), ('w392', 'review')}:
        p.error('Only the assigned adversary statement and referee review are authorized.')
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(MESH_DIR))
    import team_comm

    report_dir = ROOT / 'reports'
    report_dir.mkdir(exist_ok=True)
    receipt_file = report_dir / 'peer_delivery.jsonl'
    prior = [json.loads(s) for s in receipt_file.read_text(encoding='utf-8').splitlines()] if receipt_file.exists() else []
    if any(r.get('recipient') == a.recipient and r.get('phase') == a.phase and r.get('state') == 'sent' for r in prior):
        print(json.dumps({'recipient': a.recipient, 'phase': a.phase, 'state': 'already-sent'}))
        return 0
    if a.phase == 'review' and not any(r.get('recipient') == 'w391' and r.get('state') == 'sent' for r in prior):
        p.error('The adversary statement must be sent before the referee proof packet.')
    artifact = ROOT / ('STATEMENT_FOR_ADVERSARY.md' if a.phase == 'statement' else 'REVIEW_PACKET.md')
    if not artifact.is_file():
        p.error(f'Missing artifact: {artifact}')
    body = (f'P0117 w390 claim: independent quantitative thin-tube boundary lane. Statement only for your '
            f'independent adversarial attempt: {artifact.as_posix()}. Current openness UNKNOWN; no full-target '
            f'or novelty claim. Please test the assumptions before the later proof packet.') if a.phase == 'statement' else (
            f'P0117 w390 review: complete proof and measurements at {artifact.as_posix()}. Author-proved '
            f'thin-tube special case only; full gap is unrestricted wandering. Audit the crossing cut, '
            f'connector count, disjoint trap supports and simultaneous-ray quantifiers. Statement was sent to w391 first.')
    m = team_comm.mesh()
    result = {'recipient': a.recipient, 'phase': a.phase, 'artifact': artifact.as_posix(),
              'at_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
    try:
        team_comm.ensure(m, 'w390')
        team_comm.ensure(m, a.recipient)
        receipt = m.send('w390', a.recipient, f'P0117/w390/{a.phase}', body, kind='message' if a.phase == 'statement' else 'request')
        team_comm.ring(a.recipient)
        result.update(state='sent', receipt=receipt)
    except Exception as exc:
        result.update(state='not-sent', error=f'{type(exc).__name__}: {exc}')
    finally:
        m.close()
    with receipt_file.open('a', encoding='utf-8') as f:
        f.write(json.dumps(result, default=str) + '\n')
    print(json.dumps(result, default=str))
    return 0 if result['state'] == 'sent' else 1


if __name__ == '__main__':
    raise SystemExit(main())
