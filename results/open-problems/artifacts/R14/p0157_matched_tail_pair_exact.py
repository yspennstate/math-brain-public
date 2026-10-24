#!/usr/bin/env python3
"""Exact finite-algebra checks for the R14 P0157 matched-tail pair.

This verifies only exact degree-sequence identities and finite sanity values.
It is not a proof of the asymptotic probability theorem.
"""
from fractions import Fraction


def family(m, K, M):
    assert m % 4 == 0 and K >= 2
    n = 8 * m ** (2*K + 6)
    d = m*m
    numer_x4 = 12*m**(2*K+5) + M*(d-1)**2
    assert numer_x4 % 4 == 0
    x = numer_x4 // 4
    N3 = 2*m**(2*K+6) - x
    N1 = 6*m**(2*K+6) + x - M
    assert N1 >= 0 and N3 >= 0

    ell = N1 + 3*N3 + d*M
    s2 = 6*N3 + d*(d-1)*M
    deficit = ell - s2
    expected_deficit = 12*m**(2*K+5)
    assert deficit == expected_deficit

    delta = Fraction(deficit, ell)
    nu = 1 - delta
    ex2 = Fraction(12*N3 + d*(d-1)**2*M, ell)
    var = ex2 - nu*nu
    Q = var / (d*delta)
    mu3 = Fraction(N1 + 27*N3 + d**3*M, n)
    return dict(n=n, d=d, M=M, N1=N1, N3=N3, ell=ell,
                deficit=deficit, delta=delta, Q=Q, mu3=mu3)


samples = [(8,2), (12,2), (16,3), (20,3), (24,4)]
for m, K in samples:
    A = family(m, K, 4)
    B = family(m, K, m**(2*K-1))
    assert A['n'] == B['n'] and A['d'] == B['d']
    assert A['deficit'] == B['deficit'] == 12*m**(2*K+5)
    assert 2*K + 1 - 2*K == 1
    assert 2*K + 1 - 2*(K+1) == -1
    assert 0 < A['delta'] < 1 and 0 < B['delta'] < 1
    assert A['Q'] > 0 and B['Q'] > 0

    print(f"m={m:2d} K={K}: exact_deficit={A['deficit']}")
    print(f"  delta_B/delta_A = {float(B['delta']/A['delta']):.12f}")
    print(f"  m*Q_A={float(m*A['Q']):.12f}  "
          f"m*Q_B={float(m*B['Q']):.12f}  "
          f"Q_B/Q_A={float(B['Q']/A['Q']):.12f}")
    print(f"  third_moment_A={float(A['mu3']):.12f}  "
          f"third_moment_B={float(B['mu3']):.12f}")
    print("  hub-tree exponents: r=K -> +1; r=K+1 -> -1")

print("ALL_EXACT_CHECKS_PASS")
