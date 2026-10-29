"""Audit of the Bernstein certificate: (1) exact enumeration on K6 vs the polynomial, both pairs; (2) the polynomial at n = 10 vs the
independent mpmath code (kn_gibbs / kn_gibbs_disjoint) through 1 - Z Z_ef/Z_e^2 = N/Z_e^2 sign and value; (3) the Bernstein
expansion re-summed reproduces N/u exactly at rational points."""
import itertools
from fractions import Fraction as Fr
from math import comb
from sympy import Rational
from mpmath import mpf, mp
import kn_poly_adjacent as PA, kn_poly_disjoint as PD, kn_bernstein as KB, kn_gibbs as GA, kn_gibbs_disjoint as GD
from kn_poly_adjacent import lam, u
from kn_poly_check import ncomp

n = 6; E = list(itertools.combinations(range(n), 2)); L, U = Fr(2, 7), Fr(3, 5); q = 1 - U
acc = {"adj": [Fr(0)] * 4, "dis": [Fr(0)] * 4}
pairs = {"adj": ((0, 1), (1, 2)), "dis": ((0, 1), (2, 3))}
for m in range(1 << len(E)):
    A = set(E[i] for i in range(len(E)) if m >> i & 1)
    w = L ** len(A) * q ** ncomp(n, list(A))
    for k, (e, f) in pairs.items():
        a = acc[k]; a[0] += w; a[1] += w * (e in A); a[2] += w * (f in A); a[3] += w * (e in A and f in A)
for k, M in (("adj", PA), ("dis", PD)):
    Z, Ze, Zf, Zef = acc[k]; b = Ze * Zf - Z * Zef
    p = M.numerator(n).eval({lam: Rational(2, 7), u: Rational(3, 5)})
    print("K6 enumeration", k, "match" if Rational(b.numerator, b.denominator) == p else "MISMATCH")
mp.dps = 60
for k, M, G in (("adj", PA, GA), ("dis", PD, GD)):
    for Lr, Ur in ((Rational(1, 50), Rational(1, 2)), (Rational(1, 3), Rational(9, 10))):
        N = M.numerator(10)
        # Z_e at the same point from the mp code is not exposed; compare signs and the ratio of N to (1 - R) via a second point-free check:
        r = G.run(10, mpf(1) - mpf(Ur.p) / Ur.q, mpf(Lr.p) / Lr.q)
        print("n=10", k, "poly N sign", "+" if N.eval({lam: Lr, u: Ur}) > 0 else "-", "| mp 1-R", r["one_minus_ratio"])
for k in ("adj", "dis"):
    d, B = KB.bern(8, 0, k); N = (PA if k == "adj" else PD).numerator(8)
    for x, y in ((Fr(1, 3), Fr(2, 5)), (Fr(7, 4), Fr(1, 9))):
        s = sum(comb(d, j) * c * x ** i * y ** j * (1 - y) ** (d - j) for j, bj in enumerate(B) for i, c in bj.items()) * y
        p = N.eval({lam: Rational(x.numerator, x.denominator), u: Rational(y.numerator, y.denominator)})
        print("Bernstein resum n=8", k, "exact" if Rational(s.numerator, s.denominator) == p else ("DIFF", float(s), float(p)))
