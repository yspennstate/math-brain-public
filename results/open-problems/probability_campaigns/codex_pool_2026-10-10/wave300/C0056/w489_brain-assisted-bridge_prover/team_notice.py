"""Supported team_comm API with a longer bounded SQLite contention wait.

Does not modify the shared communication code or database configuration.
Run only for the owner's explicitly authorised named-peer notices.
"""
from pathlib import Path
import argparse
import json
import sys

sys.path.insert(0, '~/<private-repo>/12_cognitive_architecture/agent_mesh')
import team_comm

team_comm.mesh = lambda: team_comm.Mesh(team_comm.DB, busy_timeout_ms=15000)

def direct_notice(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--as', dest='sender', required=True)
    parser.add_argument('--to', required=True)
    parser.add_argument('--kind', choices=tuple(team_comm.KINDS), required=True)
    parser.add_argument('text')
    args = parser.parse_args(argv)
    if args.sender != 'w489' or args.to not in ('w490', 'w491', 'w483', 'codex-01a12190'):
        raise ValueError('This task authorises notices only from w489 to its named peers/integrator.')
    if len(args.text) > team_comm.MAX_TEXT:
        raise ValueError('Notice exceeds the supported team text limit.')
    m = team_comm.mesh()
    try:
        team_comm.ensure(m, args.sender)
        team_comm.ensure(m, args.to)
        result = m.send(args.sender, args.to, 'probability300/C0056/' + args.kind,
                        args.text, kind=team_comm.KINDS[args.kind])
        team_comm.ring(args.to)
        receipt = {'sender': args.sender, 'recipient': args.to, 'kind': args.kind,
                   'text': args.text, 'api_result': result,
                   'state': 'queued through supported Mesh API; recipient read not asserted'}
        with (Path(__file__).resolve().parent / 'COMMUNICATION_RECEIPTS.jsonl').open('a', encoding='utf-8') as handle:
            handle.write(json.dumps(receipt, ensure_ascii=False, default=str) + '\n')
        print(json.dumps(receipt, ensure_ascii=False, default=str))
        return 0
    finally:
        m.conn.close()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'direct':
        raise SystemExit(direct_notice(sys.argv[2:]))
    raise SystemExit(team_comm.main())
