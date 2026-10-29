"""Chain check for C9: pieces must tile [0, K] in order, every piece finished, and r_out(piece j) <= r_in(piece j+1).
Frames match by construction (a piece starting at node k0 > 0 uses frame(node k0), the frame run_chain ends a piece in).
usage: python c9_check.py piece1.jsonl piece2.jsonl ..."""
import sys, json
from fractions import Fraction as F
pieces = []
for p in sys.argv[1:]:
    rows = [json.loads(l) for l in open(p)]
    head, tail = rows[0], rows[-1]
    assert 'piece_done' in tail, (p, 'unfinished', tail)
    assert not any(r.get('fail') for r in rows), (p, 'failed segment')
    pieces.append((head['piece'][0], head['piece'][1], F(head['r_in']), F(tail['r_out']), p,
                   max(r['R'] for r in rows if 'R' in r), max(r['mu'] for r in rows if 'mu' in r)))
pieces.sort()
ok = pieces[0][0] == 0
for a, b in zip(pieces, pieces[1:]):
    ok &= a[1] == b[0] and a[3] <= b[2]
    print('%s -> %s  k %d  r_out %.3e <= r_in %.3e  %s' % (a[4], b[4], a[1], float(a[3]), float(b[2]), a[3] <= b[2]))
print('pieces', len(pieces), 'k range', pieces[0][0], pieces[-1][1], 'r_end', float(pieces[-1][3]), 'max R', max(x[5] for x in pieces),
      'max mu', max(x[6] for x in pieces), 'CHAIN OK' if ok else 'CHAIN FAIL')
print('r_end_exact', pieces[-1][3])
