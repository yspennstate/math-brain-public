#!/usr/bin/env python3
"""Standard-library regression checks for QFORM-ZERO-PIVOT-DET-SMOOTHING-v1.

These checks verify algebra/constants only; the analytic concentration proof is in REPORT.md.
"""
from fractions import Fraction
import itertools
import math
import random


def det_zero_pivot(a, b, d, u, v):
    return -a*v*v + 2*b*u*v - d*u*u


def check_transform(trials=2000, seed=20260922):
    rng = random.Random(seed)
    for _ in range(trials):
        a, b, d, u, v = [rng.randint(-7, 7) for _ in range(5)]
        if u == 0:
            u = 1
        x, y, z = [rng.randint(-9, 9) for _ in range(3)]
        D = det_zero_pivot(a, b, d, u, v)
        ell = u*x + v*y
        lhs = a*x*x + 2*b*x*y + d*y*y + 2*u*x*z + 2*v*y*z
        rhs = (
            Fraction(a, u*u)*ell*ell
            + Fraction(2*(b*u-a*v), u*u)*ell*y
            - Fraction(D, u*u)*y*y
            + 2*ell*z
        )
        assert Fraction(lhs) == rhs
    return trials


def check_constant():
    # For F(L)=A sqrt(L)+1/(2L), minimizer solves A L^(3/2)=1.
    for D in [Fraction(1, 16), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(13)]:
        Df = float(D)
        A = 4*math.sqrt(2)/math.sqrt(Df)
        L = A**(-2/3)
        F = A*math.sqrt(L) + 1/(2*L)
        target = 3*(2**(2/3))*(Df**(-1/3))
        assert abs(F-target) <= 1e-12*max(1.0, abs(target))
    return True


def det3(M):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def mat_sub_lambda(M, lam):
    return [[M[i][j] - (lam if i == j else 0) for j in range(3)] for i in range(3)]


def check_triangle():
    B = [[0,1,1],[1,0,1],[1,1,0]]
    assert det3(B) == 2
    # Direct eigenvectors: (1,1,1) -> 2; (1,-1,0),(1,0,-1) -> -1.
    vecs = [((1,1,1),2), ((1,-1,0),-1), ((1,0,-1),-1)]
    for x, lam in vecs:
        y = tuple(sum(B[i][j]*x[j] for j in range(3)) for i in range(3))
        assert y == tuple(lam*t for t in x)
    bound = 3*(2**(1/3))
    assert bound < 3.780
    return bound


def main():
    n = check_transform()
    check_constant()
    bound = check_triangle()
    print(f"transform_checks={n}")
    print("optimization_constant_check=PASS")
    print(f"triangle_bound={bound:.12f}")
    print("QFORM_ZERO_PIVOT_DET_SMOOTHING_CHECK_PASS")


if __name__ == "__main__":
    main()
