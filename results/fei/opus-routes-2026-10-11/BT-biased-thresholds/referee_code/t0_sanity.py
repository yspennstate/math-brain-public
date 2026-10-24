"""Sanity: butterfly spectrum == direct definition (exact), Parseval, MAJ3, AND2 sharpness."""
import random
from fractions import Fraction as Fr
import mpmath
from bfcore import *

random.seed(11)


def rq():
    return Fr(random.randint(1, 999), 1000)


bad = 0
cnt = 0
for n in range(1, 5):
    for trial in range(60 if n < 4 else 30):
        T = [random.randint(0, 1) for _ in range(1 << n)]
        f = [2 * t - 1 for t in T]
        qs = [rq() for _ in range(n)]
        P1 = spectrum(f, qs)
        P2 = spectrum_direct(f, qs)
        cnt += 1
        if P1 != P2 or sum(P1) != 1:
            bad += 1
print("butterfly vs direct, Parseval: cases", cnt, "mismatches", bad)

# MAJ3 uniform
qs = [Fr(1, 2)] * 3
T = threshold_table([1, 1, 1], 2)
P = spectrum([2 * t - 1 for t in T], qs)
V, I, D, J = metrics_exact(P)
E = corrected_entropy(P, qs)
print("MAJ3 uniform: H+ bits", E / mpmath.log(2), "I", I, "V", V, "ratio", E / mpmath.log(2) / mpq(D))

# AND2 near sharpness: OR2 with q->0 should approach 2+4/ln2
for q in [Fr(1, 10), Fr(1, 100), Fr(1, 10000)]:
    qs = [q, q]
    T = threshold_table([1, 1], 1)  # OR2
    P = spectrum([2 * t - 1 for t in T], qs)
    V, I, D, J = metrics_exact(P)
    E = corrected_entropy(P, qs)
    print("OR2 q=", q, "H+/Delta =", mpmath.nstr(E / mpmath.log(2) / mpq(D), 12), " target", mpmath.nstr(2 + 4 / mpmath.log(2), 12))
