"""Control for Proposition 1.3: M_J = H(S cap J) - E_x H(f_{J,x}) <= (2/ln 2) sum_{i not in J} Inf_i(f), every J.
Random functions (several densities) and all functions of 4 variables."""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mslib import polite, restr_profile, basic
polite()
c = 2 / np.log(2)
rng = np.random.default_rng(11)
worst = -1e9; worst_ratio = 0.0
for trial in range(60):
    n = int(rng.integers(2, 10))
    N = 1 << n
    pr = rng.choice([0.5, 0.2, 0.05])
    tt = np.where(rng.random(N) < pr, -1, 1).astype(np.int64)
    EH, HT = restr_profile(tt, n, True)
    fh, p, H, inf = basic(tt, n)
    for J in range(N):
        out = sum(inf[i] for i in range(n) if not (J >> i) & 1)
        M = HT[J] - EH[J]
        worst = max(worst, M - c * out)
        if out > 1e-12:
            worst_ratio = max(worst_ratio, M / out)
print(f"random functions: max_J [M_J - (2/ln2) Inf(J^c)] = {worst:.3e};  max_J M_J / Inf(J^c) = {worst_ratio:.6f}  (bound 2/ln2 = {c:.6f})")
worst = -1e9; worst_ratio = 0.0
for code in range(1 << 16):
    tt = np.array([-1 if (code >> x) & 1 else 1 for x in range(16)], dtype=np.int64)
    EH, HT = restr_profile(tt, 4, True)
    fh, p, H, inf = basic(tt, 4)
    for J in range(16):
        out = sum(inf[i] for i in range(4) if not (J >> i) & 1)
        M = HT[J] - EH[J]
        worst = max(worst, M - c * out)
        if out > 1e-12:
            worst_ratio = max(worst_ratio, M / out)
print(f"all n=4 functions: max_J [M_J - (2/ln2) Inf(J^c)] = {worst:.3e};  max_J M_J / Inf(J^c) = {worst_ratio:.6f}")
