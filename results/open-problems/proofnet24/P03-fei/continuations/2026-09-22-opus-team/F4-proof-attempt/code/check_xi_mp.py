"""50-digit check of the stable erasure increment Xi_j(c^2) on Numaro's g, and H(g)/(I(g)-1) of the 4-variable seed."""
import sys, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *
from tower_stable import E_stable
from mpmath import mp, mpf, log as mlog
set_polite()
mp.dps = 50
g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy"))
gh = wht(g[None, :].astype(float))[0]
kint = np.rint(gh * 2 ** 18).astype(np.int64)
S = np.arange(1 << 18)
def ph(x):
    return -x * mlog(x, 2) if x > 0 else mpf(0)
for j, c2 in ((0, 1e-20), (12, 3e-12)):
    lo = S[((S >> j) & 1) == 0]
    ex = mpf(0)
    for x, y in zip(kint[lo], kint[lo | (1 << j)]):
        a = mpf(int(x)) ** 2 / mpf(2) ** 36; b = mpf(int(y)) ** 2 / mpf(2) ** 36 * mpf(c2)
        ex += ph(a) + ph(b) - ph(a + b)
    st = float(E_stable(gh[lo] ** 2, c2 * gh[lo | (1 << j)] ** 2).sum())
    print(f"Xi_{j}(c2={c2}): mpmath {float(ex):.15e}  stable {st:.15e}", flush=True)
code = 60104
tt = np.array([1 - 2 * ((code >> x) & 1) for x in range(16)], dtype=np.int8)
fh = wht(tt[None, :].astype(float))[0]; p = fh ** 2
H = float(entropy(p)); I = float(total_influence(p[None, :], 4)[0])
print("seed code 60104 truth table", tt.tolist(), " H =", H, " I =", I, " H/(I-1) =", H / (I - 1))
