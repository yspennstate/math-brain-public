"""Referee spot-check of the identities used in SEL-4: for balanced g on k bits,
M_g(x,y1,y2) = ((1+g(x))/2) y1 + ((1-g(x))/2) y2 has H = 2 + H(g)/2, I = 1 + I(g)/2, I_sel = I(g)/2
(selector = the k inputs of g, branches the dictators y1, y2); exact influences, float entropies."""
import numpy as np
from fractions import Fraction
from rlib import wht, ent, popcount_table, I_exact
rng = np.random.default_rng(4)
worst = 0.0; bad = 0
for trial in range(300):
    k = int(rng.integers(1, 7))
    g = np.ones(1 << k, dtype=np.int64); g[rng.choice(1 << k, size=1 << (k - 1), replace=False)] = -1
    N = 1 << k
    # data y1 (bit k), y2 (bit k+1); index x + N*(y1bit + 2*y2bit)
    F = np.empty(4 * N, dtype=np.int64)
    for yi in range(4):
        y1 = -1 if yi & 1 else 1; y2 = -1 if yi & 2 else 1
        F[yi * N:(yi + 1) * N] = np.where(g == 1, y1, y2)
    P = (wht(F).astype(np.float64) / (4 * N)) ** 2
    Pg = (wht(g).astype(np.float64) / N) ** 2
    HF, Hg = float(ent(P)), float(ent(Pg))
    IF, Ig = I_exact(F, k + 2), I_exact(g, k)
    idx = np.arange(4 * N)
    Isel = sum(Fraction(int(np.sum(F != F[idx ^ (1 << i)])), 4 * N) for i in range(k))
    worst = max(worst, abs(HF - (2 + Hg / 2)))
    bad += (IF != 1 + Ig / 2) + (Isel != Ig / 2)
print("M_g identities on 300 random balanced g (k<=6): max |H - (2+H(g)/2)| = %.2e, exact influence failures = %d" % (worst, bad))
