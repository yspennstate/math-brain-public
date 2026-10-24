"""(1) mpmath cross-check of the stable erasure increment Xi_j(c^2) on Numaro's g at tiny c^2;
(2) tower limits (H/I, B/I, existential B ratio, rho_0) for several balanced monotone seeds."""
import sys, os, json, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *
from tower_stable import run, E_stable
from mpmath import mp, mpf, log as mlog
set_polite()
mp.dps = 50
g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy"))
gh = wht(g[None, :].astype(float))[0]
kint = np.rint(gh * 2 ** 18).astype(np.int64)
S = np.arange(1 << 18)
for j, c2 in ((0, 1e-20), (12, 3e-12)):
    lo = S[((S >> j) & 1) == 0]
    a = [mpf(int(x)) ** 2 / mpf(2) ** 36 for x in kint[lo]]
    b = [mpf(int(x)) ** 2 / mpf(2) ** 36 * mpf(c2) for x in kint[lo | (1 << j)]]
    def ph(x):
        return -x * mlog(x, 2) if x > 0 else mpf(0)
    ex = sum(ph(x) + ph(y) - ph(x + y) for x, y in zip(a, b))
    st = float(E_stable((gh[lo] ** 2), c2 * gh[lo | (1 << j)] ** 2).sum())
    print(f"Xi_{j}(c2={c2}): mpmath {float(ex):.15e}  stable {st:.15e}")

def monotone(tt, n):
    for x in range(1 << n):
        for i in range(n):
            if not (x >> i) & 1 and tt[x] == -1 and tt[x | (1 << i)] == 1:
                return False
    return True

seeds = {}
# balanced monotone, all variables relevant, not odd: first few on 4 and 5 variables by code order
for n in (4, 5):
    got = 0
    for code in range(1 << (1 << n)) if n == 4 else np.random.default_rng(3).integers(0, 1 << 32, 400000):
        code = int(code)
        tt = np.array([1 - 2 * ((code >> x) & 1) for x in range(1 << n)], dtype=np.int8)
        if tt.sum() != 0 or not monotone(tt, n): continue
        fh = wht(tt[None, :].astype(float))[0]
        cq = coord_quantities(fh[None, :], n)
        if (cq["Inf"][0] < 1e-12).any() or cq["B"][0].sum() < 1e-9: continue
        seeds[f"n{n}_code{code}"] = (tt, n); got += 1
        if got >= 3: break
# tribes-like balanced monotone: OR of two AND2 with a third variable ... use Maj of (x1, x2&x3, x4|x5)-type read-once
def ro(bits):
    x = bits
    return (x[0] and (x[1] or x[2])) or (x[3] and x[4]) if False else ((x[0] and x[1]) or (x[2] and (x[3] or x[4])))
tt = tt_from_func(5, lambda b: -1 if ro(list(map(bool, b))) else 1)
print("read-once seed balanced?", tt.sum())
if tt.sum() == 0:
    seeds["readonce5"] = (tt, 5)
seeds["numaro18"] = (g, 18)
out = {}
for name, (tt, n) in seeds.items():
    print("seed", name)
    rows = run(tt, n, 9 if n < 18 else 8)
    out[name] = rows[-1]
json.dump(out, open(os.path.join(HERE, "..", "logs", "tower_seeds.json"), "w"), indent=1)
print(json.dumps(out, indent=1))
