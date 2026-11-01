# Exact check of the composition recursion  H+(F) = LHS+_f(eta) + sum_i (Inf_i^eta(f)/sigma_i^2) H+(g_i)
# for F = f(g_1,...,g_k) on disjoint uniform variables (all logs natural).
import mpmath as mp, itertools, random
from isoper3 import biased_P
mp.mp.dps = 40
def walsh_P(vals):          # uniform spectrum of a 0/1 function given as a list over {0,1}^n
    n = len(vals).bit_length() - 1
    return biased_P(vals, [0.5] * n)
def Hplus(P):
    return mp.fsum(v * mp.log(1 / v) for v in P[1:] if v > 0)
def I_of(P):
    return mp.fsum(bin(A).count('1') * v for A, v in enumerate(P))
def check(fvals, gs):
    # gs: list of (vals, nvars)
    k = len(gs); ns = [n for _, n in gs]; N = sum(ns)
    offs = [sum(ns[:i]) for i in range(k)]
    F = []
    for x in range(1 << N):
        ys = 0
        for i, (vals, n) in enumerate(gs):
            sub = (x >> offs[i]) & ((1 << n) - 1)
            if vals[sub]: ys |= 1 << i
        F.append(fvals[ys])
    PF = walsh_P(F)
    q = [mp.mpf(sum(vals)) / len(vals) for vals, _ in gs]
    Pf = biased_P(fvals, q)
    sig2 = [4 * qq * (1 - qq) for qq in q]
    lhs_f = mp.fsum(v * mp.log(mp.fprod(sig2[i] for i in range(k) if A >> i & 1) / v) for A, v in enumerate(Pf) if A and v > 0)
    Inf = [mp.fsum(v for A, v in enumerate(Pf) if A >> i & 1) for i in range(k)]
    rhs = lhs_f + mp.fsum(Inf[i] / sig2[i] * Hplus(walsh_P(gs[i][0])) for i in range(k))
    IF = I_of(PF); IFr = mp.fsum(Inf[i] / sig2[i] * I_of(walsh_P(gs[i][0])) for i in range(k))
    return float(Hplus(PF)), float(rhs), float(IF), float(IFr)
AND2 = [0, 0, 0, 1]; OR2 = [0, 1, 1, 1]; X = [0, 1]
MAJ3 = [1 if bin(y).count('1') >= 2 else 0 for y in range(8)]
T24 = [1 if bin(y).count('1') >= 2 else 0 for y in range(16)]
AND3 = [1 if y == 7 else 0 for y in range(8)]
print(check(MAJ3, [(AND2, 2), (OR2, 2), (X, 1)]))
print(check(T24, [(AND2, 2), (OR2, 2), (X, 1), (AND3, 3)]))
print(check(AND2, [(MAJ3, 3), (OR2, 2)]))
