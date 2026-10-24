"""The chain F_{m+1} = g(F_m on all nine core inputs, fresh single variables on the nine auxiliaries), started from a
seed F_0 of truth probability p_0.  Exact composition identities (disjoint fresh copies):
    I_{m+1} = sum_core It_i/V_m * I_m + sum_aux It_i,   H_{m+1} = Htilde(p) + sum_core It_i/V_m (H_m - h(V_m)),
with p = (p_m on core, 1/2 on aux).  Prints p_m, I_m, H_m, H_m/I_m and the slack C I_m - H_m against the best known
slack V(p_m) (saved fixed point), to see what the chain does away from 1/2.
Usage: python chain_core.py <vig npz> p0 [seed: 'var' | 'and']"""
import sys, math
import numpy as np
import fast_gate as FG
from opt18 import Pricer, h2s

pr = Pricer(sys.argv[1]); C = pr.C
p0 = float(sys.argv[2])
# seed: a function of truth probability p0 with slack V(p0) (its I is irrelevant for the slack recursion; take I = 1 scale)
p = p0; s = pr.V(p0)          # track slack only: s_{m+1} = sum_core It/V (s_m + h(V_m)) + C*sum_aux It - Htilde
print("C = %.12f" % C)
for m in range(12):
    q = np.array([p] * 9 + [0.5] * 9)
    Ht, It, po, c = FG.evaluate(q)
    V = 4 * p * (1 - p)
    s_new = It[:9].sum() / V * (s + h2s(V)) + C * It[9:].sum() - Ht
    print("m=%2d p=%.6f s=%.8f  V(p)=%.8f s-V(p)=%+.3e  -> p_out=%.6f s_out=%.8f  V(p_out)=%.8f  D=%+.3e" % (
        m, p, s, pr.V(p), s - pr.V(p), po, s_new, pr.V(po), s_new - pr.V(po)))
    p, s = po, s_new
    if p < 1e-6 or p > 1 - 1e-6:
        break
