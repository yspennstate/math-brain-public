"""H/I of read-once k-CNFs AND_m(OR_k, ..., OR_k): degree-k PTFs (and intersections of m halfspaces).
Exact Walsh values for small n; exact product formula for all m:
F true iff every clause true; with p = 1 - 2^{-k} = Pr[clause true], the nonempty spectrum of F is
T ~ independent Bernoulli(1-p) over clauses (conditioned T nonempty), each chosen clause contributing
a uniformly random nonempty subset of its k variables."""
import numpy as np
from math import comb, log2
from fei_lib import coords, wht, HI

def walsh_ratio(m, k):
    n = m * k
    X = coords(n)
    true = np.ones(X.shape[0], dtype=bool)
    for j in range(m):
        true &= (X[:, j * k:(j + 1) * k] < 0).any(1)   # x = -1 means "true"
    f = np.where(true, -1.0, 1.0)
    c = wht(f)
    H, I = HI(c, n)
    return H / I

def formula_ratio(m, k):
    """Exact H/I from the product structure, computed in log form (no underflow)."""
    p = 1 - 2.0 ** (-k)
    q = 1 - p
    lP = m * log2(p)                 # log2 Pr[F true]
    P = 2.0 ** lP
    e0 = (1 - 2 * P) ** 2
    Vn = 1 - e0                      # total nonempty weight = 4P(1-P)
    Et = m * q / (1 - p ** m)        # E|T| given T nonempty, T ~ Bin(m, q)
    # -log2(weight of one spectral set with |T| = t) = -2 - 2 lP - t log2(q/p) + t log2(2^k - 1)
    Hn = (-2 - 2 * lP) + Et * (-log2(q / p) + log2(2 ** k - 1))
    from math import log1p, log
    # H/I = (H0/Vn + Hn) / (Et * mean clause-set size); H0/Vn -> 1/ln 2 when P underflows
    if P > 0:
        if abs(1 - 2 * P) < 1e-300:
            lg = 0.0
        elif P < 0.25:
            lg = log1p(-2 * P)
        else:
            lg = log(abs(1 - 2 * P))
        H0_over_Vn = -(1 - 2 * P) ** 2 * 2 * lg / log(2) / (4 * P * (1 - P))
    else:
        H0_over_Vn = 1 / log(2)
    return (H0_over_Vn + Hn) / (Et * (k * 2 ** (k - 1) / (2 ** k - 1)))


with open("../logs/cnf_ratio.log", "w") as lg:
    for k, ms in ((2, (2, 4, 6, 8, 10)), (3, (2, 4, 6))):
        for m in ms:
            print("k=%d m=%2d n=%2d  Walsh H/I=%.6f  formula %.6f" % (k, m, m * k, walsh_ratio(m, k), formula_ratio(m, k)), file=lg)
    for k in (2, 3, 4):
        for m in (20, 50, 100, 1000, 10000):
            print("k=%d m=%5d formula H/I=%.6f" % (k, m, formula_ratio(m, k)), file=lg)
        p = 1 - 2.0 ** (-k); q = 1 - p
        h = -q * log2(q) - p * log2(p)
        lim = (log2(1 / p) + h + q * log2(2 ** k - 1)) / (q * k * 2 ** (k - 1) / (2 ** k - 1))
        print("k=%d limit m->inf: %.6f" % (k, lim), file=lg)
print(open("../logs/cnf_ratio.log").read())
