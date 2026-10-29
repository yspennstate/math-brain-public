"""Chain check for a C9 block tube made of a prefix log cut at a resume line plus one bresume piece (the brst runs: bfull14
rows 0..199, then brst10/brst40 from node 200). Checks: the prefix starts at node 0 and its rows k = 0..K are contiguous
with no failed segment; the piece starts at K+1, finished, with no failed segment; the piece's v_in dominates the prefix's
radii at line K block by block (bresume takes them from 'vx' or rounds the float up); block layouts agree. Prints v_end,
max a priori radius and r_end_exact (Euclidean bound |z| <= |v|) for the trap step.
usage: python c9_bcheck2.py PREFIX.jsonl K PIECE.jsonl"""
import json
import sys
from fractions import Fraction as F

from c9_blocks import norm_v

pre, K, piece = sys.argv[1], int(sys.argv[2]), sys.argv[3]
P = [json.loads(l) for l in open(pre)]
assert P[0]['piece'][0] == 0, 'prefix does not start at node 0'
rows = [r for r in P[1:] if 'k' in r and r['k'] <= K]
assert [r['k'] for r in rows] == list(range(K + 1)), 'prefix rows not contiguous 0..K'
assert not any(r.get('fail') for r in rows), 'failed segment in prefix'
last = rows[-1]
Q = [json.loads(l) for l in open(piece)]
head, tail = Q[0], Q[-1]
assert head['piece'][0] == K + 1, ('piece starts at', head['piece'][0])
assert 'piece_done' in tail, 'piece unfinished'
assert not any(r.get('fail') for r in Q), 'failed segment in piece'
vk = [F(x) for x in last['vx']] if 'vx' in last else [F(x) for x in last['v']]
vin = [F(x) for x in head['v_in']]
assert len(vk) == len(vin) and all(b >= a for a, b in zip(vk, vin)), 'v_in does not dominate the prefix radii'
assert [r['k'] for r in Q[1:-1]] == list(range(K + 1, tail['piece_done'][1])), 'piece rows not contiguous'
maxR = max(max(r['R']) for r in rows + Q[1:-1] if 'R' in r)
vend = [F(x) for x in tail['v_out']]
print('prefix rows', len(rows), 'piece', head['piece'][0], '..', tail['piece_done'][1], 'v_in/v_K max %.6f' %
      max(float(b / a) for a, b in zip(vk, vin) if a), 'blocks_out', tail['blocks_out'])
print('v_end', [float(x) for x in vend], 'max R', maxR, 'CHAIN OK')
print('r_end_exact', norm_v(vend))
