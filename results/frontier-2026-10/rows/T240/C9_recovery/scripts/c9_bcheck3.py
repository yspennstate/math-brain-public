"""Chain check for the three-part C9 block tube: bfull14 rows 0..K1, brst10 (bresume from K1) rows K1+1..K2, then a
flow-frame bresume piece (C9_FLOWCOL=1) from K2. Same checks as c9_bcheck2 for each junction, except the last: there the
radii change frame, so v_in of the last piece is recomputed exactly as bresume does it (switch() from the plain frame at
node K2+1 into the flow frame at the same node, from brst10's logged 'vx' at line K2) and must equal the logged v_in.
Rows of brst10 after K2 (it failed at k854) are not used. Run with the bresume env (C9_ARB C9_CLUSTER C9_U C9_KAPPA
C9_FACE C9_HMAX) so setup() rebuilds the same nodes.
usage: python c9_bcheck3.py logs/bfull14.jsonl 199 logs/brst10.jsonl 599 logs/flow599.jsonl"""
import json
import os
import sys
from fractions import Fraction as F

PARTIAL = '--partial' in sys.argv  # dry run on a live piece: skips the finished / reaches-the-end checks
sys.argv = [a for a in sys.argv if a != '--partial']
pre, K1, mid, K2, piece = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), sys.argv[5]


def load(p):
    return [json.loads(l) for l in open(p, encoding='utf-8')]


def rows_upto(L, k0, k1):
    rs = [r for r in L[1:] if 'k' in r and k0 <= r['k'] <= k1]
    assert [r['k'] for r in rs] == list(range(k0, k1 + 1)), ('rows not contiguous', k0, k1)
    assert not any(r.get('fail') for r in rs), ('failed segment', k0, k1)
    return rs


def vx(r):
    return [F(x) for x in r['vx']] if 'vx' in r else None


A, B, C = load(pre), load(mid), load(piece)
assert A[0]['piece'][0] == 0
ra = rows_upto(A, 0, K1)
assert B[0]['piece'][0] == K1 + 1, B[0]['piece']
va, vb = vx(ra[-1]) or [F(x) for x in ra[-1]['v']], [F(x) for x in B[0]['v_in']]
assert len(va) == len(vb) and all(b >= a for a, b in zip(va, vb)), 'brst10 v_in does not dominate bfull14 at K1'
rb = rows_upto(B, K1 + 1, K2)
assert 'vx' in rb[-1], 'line K2 has no exact radii'
assert C[0]['piece'][0] == K2 + 1, C[0]['piece']
tail = C[-1]
if PARTIAL:
    C = C + [{'piece_done': [K2 + 1, C[-1]['k'] + 1], 'v_out': C[-1].get('vx', [str(v) for v in C[-1]['v']]), 'blocks_out': None}]
    tail = C[-1]
assert 'piece_done' in tail, 'last piece unfinished'
assert not any(r.get('fail') for r in C), 'failed segment in last piece'
assert [r['k'] for r in C[1:-1]] == list(range(K2 + 1, tail['piece_done'][1])), 'last piece rows not contiguous'

os.environ['C9_FLOWCOL'] = '1'
sys.argv = ['c9_run.py', 'check', '820', '0.004']
import c9_run
import c9_blocks as CB
from c9_flow import fdrive, fl, ETA_F
_, _, _, tq, nodes, _ = c9_run.setup('820', '0.004')
x = nodes[K2 + 1]
P0, Pinv0, b0 = CB.frame_b(fdrive.jac(fl(x), ETA_F))
P1, Pinv1, b1 = CB.frame_b(fdrive.jac(fl(x), ETA_F), x)
vsw = CB.switch(Pinv1, b1, P0, b0, vx(rb[-1]))
vin = [F(s) for s in C[0]['v_in']]
assert b1 == C[0]['blocks_in'], ('blocks', b1, C[0]['blocks_in'])
assert vsw == vin, 'recomputed switched radii differ from the logged v_in'
assert PARTIAL or tail['piece_done'][1] == len(tq) - 1, ('tube does not reach the last node', tail['piece_done'][1], len(tq) - 1)
maxR = max(max(r['R']) for r in ra + rb + C[1:-1] if 'R' in r)
vend = [F(s) for s in tail['v_out']]
print('rows', len(ra), len(rb), len(C) - 2, 'junction K1 ratio %.6f' % max(float(b / a) for a, b in zip(va, vb) if a),
      'switch exact', 'blocks_out', tail['blocks_out'])
print('v_end', [float(s) for s in vend], 'max R', maxR, 'CHAIN OK')
print('r_end_exact', CB.norm_v(vend))
