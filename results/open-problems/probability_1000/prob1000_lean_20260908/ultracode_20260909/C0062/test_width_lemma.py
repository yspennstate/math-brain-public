# Test: if lambda_1 >= l(lambda) + 2, does moving the corner box at the end of the
# top block of full-length rows, i.e. c = (r, lambda_1) with r = lambda'_{lambda_1},
# to a new last row (l+1, 1) strictly increase dim?  Also: does SOME single-box move?
import math, sys
from fractions import Fraction
from enum_maxdim import hooks_dim, conjugate

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k): yield (k,) + rest

def single_moves(lam):
    lam = list(lam) + [0]
    for i in range(len(lam) - 1):
        if lam[i] > lam[i + 1]:
            for k in range(len(lam)):
                if k != i and (k == 0 or lam[k - 1] > lam[k]):
                    mu = lam[:]; mu[i] -= 1; mu[k] += 1
                    mu = tuple(x for x in mu if x > 0)
                    if list(mu) == sorted(mu, reverse=True): yield mu

N = int(sys.argv[1])
failA = []; failB = []; tested = 0; ratios_min = 10.0
for n in range(3, N + 1):
    for lam in partitions(n):
        l = len(lam)
        if lam[0] < l + 2: continue
        tested += 1
        r = sum(1 for x in lam if x == lam[0])  # rows of full length; corner at (r, lam1)
        mu = list(lam); mu[r - 1] -= 1; mu.append(1); mu = tuple(x for x in mu if x > 0)
        assert list(mu) == sorted(mu, reverse=True)
        d0, _ = hooks_dim(lam); d1, _ = hooks_dim(mu)
        ratios_min = min(ratios_min, d1 / d0)
        if d1 <= d0:
            failA.append((n, lam, mu, d0, d1))
            if not any(hooks_dim(nu)[0] > d0 for nu in single_moves(lam)):
                failB.append((n, lam))
print("tested", tested, "failA", len(failA), "failB", len(failB), "min ratio", ratios_min)
for f in failA[:15]: print("  A fails:", f)
for f in failB[:15]: print("  B fails (no single move helps):", f)
