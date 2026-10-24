#!/usr/bin/env python3
"""
R07 I0077 run-53 exact arithmetic self-check.

This checks the finite Walsh/Rademacher orthogonality and weighted-energy
identities used for the dyadic quadratic variation of the explicit rough
Takagi template in the accompanying report.

It is a SELF-CHECK, not a proof for all N and not an audit of the theorem.
The all-N identity is proved symbolically in the report.
"""
from fractions import Fraction

MAX_N = 12


def sign(N: int, n: int, k: int) -> int:
    """Slope sign of phi(2^n t) on [k/2^N,(k+1)/2^N]."""
    block = 1 << (N - n - 1)
    return 1 if ((k // block) & 1) == 0 else -1


for N in range(1, MAX_N + 1):
    m = 1 << N

    # Exact orthogonality of slope-sign rows.
    for n in range(N):
        for j in range(N):
            dot = sum(sign(N, n, k) * sign(N, j, k) for k in range(m))
            expected = m if n == j else 0
            assert dot == expected, (N, n, j, dot, expected)

    # Exact numerator of V_N(Q):
    #   2^{-N} sum_{n=0}^{N-1} (n+1) 2^n
    numerator = sum((n + 1) * (1 << n) for n in range(N))
    closed_form_numerator = (N - 1) * (1 << N) + 1
    assert numerator == closed_form_numerator, (
        N, numerator, closed_form_numerator
    )

    qv = Fraction(numerator, m)
    closed_form_qv = Fraction(N - 1, 1) + Fraction(1, m)
    assert qv == closed_form_qv

    print(
        f"N={N:2d}  orthogonality=PASS  "
        f"V_N={qv}  closed_form={closed_form_qv}"
    )

print("PASS: all exact checks succeeded for N=1,...,12.")
