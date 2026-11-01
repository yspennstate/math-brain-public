"""Chain check for C9 block pieces: pieces tile [0, K] in order, every piece finished with no failed segment,
blocks_out(j) == blocks_in(j+1) and v_out(j) <= v_in(j+1) block by block. Prints r_end_exact = Euclidean bound of
the end radius vector (|z| <= |v|), the radius the trap step takes in frame(node K) coordinates.
usage: python c9_bcheck.py piece1.jsonl piece2.jsonl ..."""
import sys, json
from fractions import Fraction as F
from c9_blocks import norm_v
pieces = []
for p in sys.argv[1:]:
    rows = [json.loads(l) for l in open(p)]
    head, tail = rows[0], rows[-1]
    assert 'piece_done' in tail, (p, 'unfinished', tail)
    assert not any(r.get('fail') for r in rows), (p, 'failed segment')
    pieces.append((head['piece'][0], head['piece'][1], [F(x) for x in head['v_in']], [F(x) for x in tail['v_out']],
                   head['blocks_in'], tail['blocks_out'], p, max(max(r['R']) for r in rows if 'R' in r)))
pieces.sort(key=lambda x: x[0])
ok = pieces[0][0] == 0
for a, b in zip(pieces, pieces[1:]):
    c = a[1] == b[0] and a[5] == b[4] and all(x <= y for x, y in zip(a[3], b[2]))
    ok &= c
    print('%s -> %s  k %d  max v_out/v_in %.3f  %s' % (a[6], b[6], a[1], max(float(x / y) for x, y in zip(a[3], b[2])), c))
r_end = norm_v(pieces[-1][3])
print('pieces', len(pieces), 'k range', pieces[0][0], pieces[-1][1], 'v_end', [float(x) for x in pieces[-1][3]],
      'max R', max(x[7] for x in pieces), 'CHAIN OK' if ok else 'CHAIN FAIL')
print('r_end_exact', r_end)
