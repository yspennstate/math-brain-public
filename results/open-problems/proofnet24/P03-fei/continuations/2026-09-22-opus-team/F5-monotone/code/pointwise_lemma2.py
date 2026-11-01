"""Exact check of the POINTWISE claim inside Lemma 2: for every x,
Pr[g(y) != 0 | x] <= (2/sqrt(pi)) c^{-1/2}, where y flips each j in U_i w.p. c/(2N) (N = |U_i|+1).
Also checks the structural identity I(E_1 f) = I(D_1 f) at the heaviest coordinate (Section 4.3)."""
import itertools, math
import numpy as np
from ltf_core import ltf_table, spectrum, popcount

rng = np.random.default_rng(11)
worst = 0.0; arg = None; ident = 0.0
for trial in range(160):
    n = int(rng.integers(3, 9))
    kind = trial % 4
    if kind == 0: w = rng.uniform(1, 2, n)
    elif kind == 1: w = rng.integers(1, 5, n).astype(float)
    elif kind == 2: w = np.exp(rng.normal(0, 1.2, n))
    else: w = np.ones(n)
    th = float(rng.normal() * np.linalg.norm(w)) + 1e-9
    a = np.abs(w)
    for i in range(n):
        U = [j for j in range(n) if j != i and a[j] >= a[i] - 1e-12]
        N = len(U) + 1
        if N < 2: continue
        rest = [j for j in range(n) if j != i]
        for c in [0.3, 1.0, N / 2.0, float(N)]:
            if c > N: continue
            q = c / (2 * N)
            bound = (2 / math.sqrt(math.pi)) / math.sqrt(c)
            for xs in itertools.product([-1, 1], repeat=n - 1):
                x = dict(zip(rest, xs))
                L0 = sum(w[j] * x[j] for j in rest)
                pr = 0.0
                for flips in itertools.product([0, 1], repeat=len(U)):
                    k = sum(flips)
                    p = q ** k * (1 - q) ** (len(U) - k)
                    L = L0 - 2 * sum(w[j] * x[j] for j, fl in zip(U, flips) if fl)
                    if th - a[i] < L <= th + a[i]:
                        pr += p
                if pr / bound > worst:
                    worst = pr / bound; arg = (np.round(w, 3).tolist(), round(th, 3), i, c)
    # structural identity at the heaviest coordinate
    h = int(np.argmax(a)); f = ltf_table(w, th); cc = spectrum(f); b = 1 << h
    Is = sum(popcount(S) * cc[S] ** 2 for S in range(1 << n) if not S & b)
    ID = sum(popcount(S) * cc[S | b] ** 2 for S in range(1 << n) if not S & b)
    ident = max(ident, abs(Is - ID))
print("max over x of Pr[g(y)!=0|x] / bound =", round(worst, 4), "at", arg)
print("max |I(E_1 f) - I(D_1 f)| at the heaviest coordinate =", ident)
