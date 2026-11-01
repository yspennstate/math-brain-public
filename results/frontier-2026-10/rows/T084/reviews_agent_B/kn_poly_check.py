"""Check kn_poly_adjacent.numerator against direct enumeration of every edge set of K_n (n = 4, 5; adjacent and disjoint pairs) at exact rational points."""
import itertools
from fractions import Fraction as Fr
from sympy import Rational
import kn_poly_adjacent, kn_poly_disjoint
from kn_poly_adjacent import lam, u


def ncomp(n, A):
    p = list(range(n)); k = n
    def f(x):
        while p[x] != x: p[x] = p[p[x]]; x = p[x]
        return x
    for a, b in A:
        ra, rb = f(a), f(b)
        if ra != rb: p[ra] = rb; k -= 1
    return k


for n, pair in ((4, "adj"), (5, "adj"), (4, "dis"), (5, "dis")):
    E = list(itertools.combinations(range(n), 2)); e, f = ((0, 1), (1, 2)) if pair == "adj" else ((0, 1), (2, 3))
    N = (kn_poly_adjacent if pair == "adj" else kn_poly_disjoint).numerator(n)
    for L, U in ((Fr(1, 3), Fr(1, 2)), (Fr(5, 2), Fr(9, 10)), (Fr(1, 20), Fr(1, 7))):
        q = 1 - U; Z = Ze = Zf = Zef = Fr(0)
        for m in range(1 << len(E)):
            A = [E[i] for i in range(len(E)) if m >> i & 1]
            w = L ** len(A) * q ** ncomp(n, A)
            Z += w; Ze += w * (e in A); Zf += w * (f in A); Zef += w * (e in A and f in A)
        brute = Ze * Zf - Z * Zef
        poly = N.eval({lam: Rational(L.numerator, L.denominator), u: Rational(U.numerator, U.denominator)})
        print(n, pair, L, U, "match" if Rational(brute.numerator, brute.denominator) == poly else ("MISMATCH", brute, poly))
