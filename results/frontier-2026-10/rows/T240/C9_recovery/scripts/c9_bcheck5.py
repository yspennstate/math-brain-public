"""Chain check for the four-part C9 block tube (agent H, 18 Oct 2026): bfull14 rows 0..K1, brst10 rows K1+1..K2,
flow599 (flow frame, C9_DELTA 0.02) rows K2+1..K3, then plain888g8 (plain clustered frame, C9_DELTA 0.01, no resets,
grouped comparison C9_LNSUB=8) from K3+1 to the last node. Junctions 1 and 2 as in c9_bcheck3. Junction 3 changes frame:
the radii are carried from the flow frame (DELTA 0.02) into the plain frame (DELTA 0.01) at node K3+1 by switch(), from
flow599's exact 'vx' at line K3, and must equal the logged v_in and blocks_in. Past t ~ 421 every eigenvalue is negative,
so the last piece needs no section reset; the flow-frame pieces from K3 on (flow599d) are not used.
Run with the bresume env (C9_ARB C9_CLUSTER C9_U C9_KAPPA C9_FACE C9_HMAX).
usage: python c9_bcheck5.py logs/bfull14.jsonl 199 logs/brst10.jsonl 599 logs/flow599.jsonl 887 logs/plain888g8.jsonl [--partial]"""
import json
import os
import sys
from fractions import Fraction as F

PARTIAL = '--partial' in sys.argv  # dry run on a live last piece: skips the finished / reaches-the-end checks
sys.argv = [a for a in sys.argv if a != '--partial']
pre, K1, mid, K2, p3, K3, p4 = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), sys.argv[5], int(sys.argv[6]), sys.argv[7]


def load(p):
    return [json.loads(l) for l in open(p, encoding='utf-8')]


def rows_upto(L, k0, k1):
    rs = [r for r in L[1:] if 'k' in r and k0 <= r['k'] <= k1]
    assert [r['k'] for r in rs] == list(range(k0, k1 + 1)), ('rows not contiguous', k0, k1)
    assert not any(r.get('fail') for r in rs), ('failed segment', k0, k1)
    return rs


def vx(r):
    return [F(x) for x in r['vx']] if 'vx' in r else None


A, B, C, D = load(pre), load(mid), load(p3), load(p4)
assert A[0]['piece'][0] == 0
ra = rows_upto(A, 0, K1)
assert B[0]['piece'][0] == K1 + 1, B[0]['piece']
va, vb = vx(ra[-1]) or [F(x) for x in ra[-1]['v']], [F(x) for x in B[0]['v_in']]
assert len(va) == len(vb) and all(b >= a for a, b in zip(va, vb)), 'brst10 v_in does not dominate bfull14 at K1'
rb = rows_upto(B, K1 + 1, K2)
assert 'vx' in rb[-1], 'line K2 has no exact radii'
assert C[0]['piece'][0] == K2 + 1, C[0]['piece']
rc = rows_upto(C, K2 + 1, K3)
assert 'vx' in rc[-1], 'line K3 has no exact radii'
assert D[0]['piece'][0] == K3 + 1, D[0]['piece']
tail = D[-1]
if PARTIAL:
    D = D + [{'piece_done': [K3 + 1, D[-1]['k'] + 1], 'v_out': D[-1].get('vx', [str(v) for v in D[-1]['v']]), 'blocks_out': None}]
    tail = D[-1]
assert 'piece_done' in tail, 'last piece unfinished'
assert not any(r.get('fail') for r in D), 'failed segment in last piece'
assert [r['k'] for r in D[1:-1]] == list(range(K3 + 1, tail['piece_done'][1])), 'last piece rows not contiguous'

os.environ['C9_FLOWCOL'] = '1'
os.environ.pop('C9_DELTA', None)
sys.argv = ['c9_run.py', 'check', '820', '0.004']
import c9_run
import c9_blocks as CB
import c9_cluster
from c9_flow import fdrive, fl, ETA_F
_, _, _, tq, nodes, _ = c9_run.setup('820', '0.004')

# junction 2: plain frame -> flow frame at node K2+1, both at DELTA 0.02 (as flow599 ran)
c9_cluster.DELTA = 0.02
x = nodes[K2 + 1]
P0, Pinv0, b0 = CB.frame_b(fdrive.jac(fl(x), ETA_F))
P1, Pinv1, b1 = CB.frame_b(fdrive.jac(fl(x), ETA_F), x)
vsw = CB.switch(Pinv1, b1, P0, b0, vx(rb[-1]))
assert b1 == C[0]['blocks_in'], ('blocks', b1, C[0]['blocks_in'])
assert vsw == [F(s) for s in C[0]['v_in']], 'junction 2: recomputed switched radii differ from the logged v_in'

# junction 3: flow frame (DELTA 0.02) -> plain clustered frame (DELTA 0.01) at node K3+1, recomputed as bresume does it
x = nodes[K3 + 1]
os.environ['C9_FLOWCOL'] = '1'; c9_cluster.DELTA = 0.02
Ps, Pinvs, bs = CB.frame_b(fdrive.jac(fl(x), ETA_F), x)
assert len(bs) == len(vx(rc[-1]))
os.environ['C9_FLOWCOL'] = '0'; c9_cluster.DELTA = 0.01
Pp, Pinvp, bp = CB.frame_b(fdrive.jac(fl(x), ETA_F))
assert bp == D[0]['blocks_in'], ('junction 3 blocks', bp, D[0]['blocks_in'])
assert CB.switch(Pinvp, bp, Ps, bs, vx(rc[-1])) == [F(s) for s in D[0]['v_in']], 'junction 3: recomputed switched radii differ from the logged v_in'
assert PARTIAL or tail['piece_done'][1] == len(tq) - 1, ('tube does not reach the last node', tail['piece_done'][1], len(tq) - 1)
maxR = max(max(r['R']) for r in ra + rb + rc + D[1:-1] if 'R' in r)
vend = [F(s) for s in tail['v_out']]
print('rows', len(ra), len(rb), len(rc), len(D) - 2, 'junction K1 ratio %.6f' % max(float(b / a) for a, b in zip(va, vb) if a),
      'switch exact', 'flow-to-plain switch exact', 'blocks_out', tail['blocks_out'])
print('v_end', [float(s) for s in vend], 'max R', maxR, 'CHAIN OK')
print('r_end_exact', CB.norm_v(vend))
