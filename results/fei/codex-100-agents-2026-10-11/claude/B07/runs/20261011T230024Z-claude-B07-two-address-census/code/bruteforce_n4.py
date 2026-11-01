#!/usr/bin/env python
"""Independent completeness check of the N=4 census: all 65536 Boolean F(y1,y2,x1,x2), address (y1,y2).
Index bits: y1 = bit0, y2 = bit1, x1 = bit2, x2 = bit3. Slice J gathers coefficients T=J|(Tx<<2)."""
import sys, json, numpy as np
from fractions import Fraction
def popc(v): return bin(v).count('1')
Hm = np.array([[1-2*(popc(x&T)&1) for T in range(16)] for x in range(16)], dtype=np.int64)
k = np.arange(1<<16, dtype=np.int64)
F = 1 - 2*((k[:,None] >> np.arange(16)) & 1)
W = F @ Hm                      # 16 * fhat
C = W*W
count = 0; best = 0.0
for f in range(1<<16):
    ok = True
    for J in range(4):
        c = [int(C[f, J | (t<<2)]) for t in range(4)]   # t over (x1,x2) subsets
        if sum(c) and c[0]*c[3] != c[1]*c[2]:
            ok = False; break
    if ok:
        count += 1
        p = C[f]/256.0
        nz = p > 0
        H = float(-(p[nz]*np.log2(p[nz])).sum())
        I = float(sum(popc(T)*p[T] for T in range(16)))
        if I > 0: best = max(best, H/I)
res = {'boolean_functions': 1<<16, 'two_address_conditional_product': count, 'max_ratio_float': best}
print(res); json.dump(res, open(sys.argv[1], 'w'), indent=1)
