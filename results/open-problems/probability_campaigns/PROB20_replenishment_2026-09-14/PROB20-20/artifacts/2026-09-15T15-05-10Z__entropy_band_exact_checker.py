"""Finite-model reproducibility check for the PROB20-20 entropy-band report.

This script is NOT evidence for the asymptotic conjecture.  It checks the exact
finite-n algebra used in Lemma 4.1 / Theorem 5.1 of the run report:

    b = -log P(S_n=m) >= n D(mu || pi)

and, for a band B=(K,L],

    D(mu || pi) >= Phi(a,Q)/L,

where
    a = E_mu[X 1_B],
    Q = E_pi[X 1_B],
    Phi(a,Q) = a log(a/Q)-a+Q when a>Q, else 0.

The conditional law is computed by exhaustive enumeration, so the only
numerical approximation is floating-point evaluation of products/logarithms.
"""

import itertools
import math
from collections import defaultdict


def verify_case(pi, n, m, K, L, tol=1e-12):
    support = [k for k, p in enumerate(pi) if p > 0.0]

    atom = 0.0
    accepted = []
    for y in itertools.product(support, repeat=n):
        if sum(y) != m:
            continue
        w = 1.0
        for k in y:
            w *= pi[k]
        atom += w
        accepted.append((y, w))

    if atom <= 0.0:
        raise ValueError("conditioning atom is zero")

    marginal = defaultdict(float)
    for y, w in accepted:
        marginal[y[0]] += w / atom

    b = -math.log(atom)
    kl = sum(mu * math.log(mu / pi[k]) for k, mu in marginal.items())

    a = sum(k * mu for k, mu in marginal.items() if K < k <= L)
    Q = sum(k * pi[k] for k in support if K < k <= L)
    phi = 0.0 if a <= Q else a * math.log(a / Q) - a + Q

    tensor_gap = b - n * kl
    band_gap = kl - phi / L

    if tensor_gap < -tol:
        raise AssertionError(("tensorization failed", tensor_gap))
    if band_gap < -tol:
        raise AssertionError(("band entropy bound failed", band_gap))

    return {
        "n": n,
        "m": m,
        "K": K,
        "L": L,
        "P(S_n=m)": atom,
        "b": b,
        "D(mu||pi)": kl,
        "a": a,
        "Q": Q,
        "Phi(a,Q)": phi,
        "b-nD": tensor_gap,
        "D-Phi/L": band_gap,
    }


def main():
    # Finite toy law; asymptotic radius-one behavior is irrelevant for this
    # algebraic check.
    pi = [0.35, 0.25, 0.15, 0.10, 0.07, 0.04, 0.025, 0.015]
    assert abs(sum(pi) - 1.0) < 1e-15

    cases = [
        (5, 12, 1, 5),
        (6, 15, 1, 5),
        (6, 18, 2, 6),
    ]

    for case in cases:
        result = verify_case(pi, *case)
        print("PASS", result)


if __name__ == "__main__":
    main()
