import os
"""Correct per-word localized computations (profiles are NOT dihedral
invariant - the earlier orbit-based t_k(x) were wrong from k=3 on).
Recompute F_k(x) and t_k(x) = F_k(x)/Cat_k per-word for k <= 5 at
x = 0, 1/4, 1/2; redo the Stieltjes minors; and the corrected integer
sequence sum_pi k! f_pi(0)."""
import sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import tk_core
from exact_volume import volume_from_halfspaces
from fractions import Fraction as Fr
from math import comb, factorial

def cat(k):
    return comb(2*k, k)//(k+1)

def section(pm, x):
    rows = tk_core.dedupe_rows(tk_core.toeplitz_forms(pm))
    k = len(pm)//2
    hs = []
    for r in rows:
        c = tuple(r[1:])
        hs.append((c, Fr(x)))
        hs.append((tuple(-v for v in c), 1 - Fr(x)))
    return volume_from_halfspaces(hs, [(-1, 1)]*k)

xs = {"0": Fr(0), "1/4": Fr(1,4), "1/2": Fr(1,2)}
res = {nm: [Fr(1)] for nm in xs}
ints = [1]
for k in range(1, 6):
    tots = {nm: Fr(0) for nm in xs}
    for pm in tk_core.all_pairings(2*k):
        for nm, x in xs.items():
            tots[nm] += section(pm, x)
    for nm in xs:
        res[nm].append(tots[nm])
    ints.append(int(tots["0"]*factorial(k)))
    print(f"k={k} done: F(0)={tots['0']} F(1/4)={tots['1/4']} F(1/2)={tots['1/2']}", flush=True)

print("corrected integer sequence k! F_k(0):", ints, flush=True)
for nm in xs:
    t = [res[nm][k]/cat(k) for k in range(6)]
    print(f"x={nm}: t_k = " + ", ".join(str(v) for v in t), flush=True)
    for shift, hname in ((0, "H0"), (1, "H1")):
        n = len(t)
        tmax = (n-1-shift)//2
        mins = []
        for tt in range(0, tmax+1):
            sz = tt+1
            A = [[t[i+j+shift] for j in range(sz)] for i in range(sz)]
            det = Fr(1)
            for c in range(sz):
                piv = next((r for r in range(c, sz) if A[r][c] != 0), None)
                if piv is None:
                    det = Fr(0); break
                if piv != c:
                    A[c], A[piv] = A[piv], A[c]; det = -det
                det *= A[c][c]
                for r in range(c+1, sz):
                    if A[r][c]:
                        fq = A[r][c]/A[c][c]
                        for cc in range(c, sz):
                            A[r][cc] -= fq*A[c][cc]
            mins.append(det)
        ok = all(m2 > 0 for m2 in mins)
        print(f"   {hname}: " + ", ".join(str(m2) for m2 in mins) +
              ("  ALL POSITIVE" if ok else "  HAS NONPOSITIVE"), flush=True)
