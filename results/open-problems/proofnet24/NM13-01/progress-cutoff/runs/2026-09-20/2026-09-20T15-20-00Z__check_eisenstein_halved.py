#!/usr/bin/env python3
from fractions import Fraction
from math import log
import numpy as np


def fano_incidence():
    # Cyclic Fano plane: lines i+{0,1,3} mod 7.
    B = np.zeros((7, 7), dtype=int)
    diff = {0, 1, 3}
    for i in range(7):
        for x in diff:
            B[(i + x) % 7, i] = 1
    return B


def check():
    # p=2 Eisenstein-halved constants.
    p = 2
    K = p**3
    k = p
    Q = K * k
    D = (K + 1) * k
    assert (K, k, Q, D) == (8, 2, 16, 18)

    v = Fraction(Q - 1, D)
    a = Fraction(Q + 1, D)
    assert v == Fraction(5, 6)
    assert a == Fraction(17, 18)

    # adj-Ramanujan upper endpoint on A_X^2 restricted to the left side.
    theta_top = K + k + 2 * p * p
    rho = Fraction(theta_top - (K + 1), D)
    assert theta_top == 18 and rho == Fraction(1, 2)
    assert 1 - rho == Fraction(1, 2)

    # Source-continuous-time profile, with time perturbation sqrt(log_2 n).
    center_log2 = Fraction(D, 4 * (Q - 1))
    c2_log2 = 4 * v**3 / a
    tau2_log2 = a / (4 * v**3)
    assert center_log2 == Fraction(3, 10)
    assert c2_log2 == Fraction(125, 51)
    assert tau2_log2 == Fraction(51, 125)
    assert c2_log2 * tau2_log2 == 1

    # Radial transition law away from the root in the halved (9,3)-tree.
    pplus = Fraction(Q, D)
    pzero = Fraction(k - 1, D)
    pminus = Fraction(1, D)
    assert pplus + pzero + pminus == 1
    assert pplus - pminus == v
    assert pplus + pminus == a
    assert (pplus, pzero, pminus) == (
        Fraction(8, 9), Fraction(1, 18), Fraction(1, 18)
    )

    # Sphere counts |S_r| = D Q^(r-1), r >= 1.
    spheres = [1] + [D * (Q ** (r - 1)) for r in range(1, 5)]
    assert spheres == [1, 18, 288, 4608, 73728]

    # Fixed-positive LRE fails because Q < D-1.
    beta = 0.5 * (1 - log(Q) / log(D - 1))
    assert beta > 0

    # Independent finite spectral sanity check.  The Fano incidence graph is
    # (3,3)-biregular of girth 6.  Its left halved graph obeys
    # A_H = B B^T - 3 I exactly (and is K_7).
    B = fano_incidence()
    assert np.all(B.sum(axis=0) == 3)
    assert np.all(B.sum(axis=1) == 3)
    C = B @ B.T
    AH = C - 3 * np.eye(7, dtype=int)
    assert np.all(np.diag(AH) == 0)
    assert np.all(AH == (np.ones((7, 7), dtype=int) - np.eye(7, dtype=int)))
    ev = np.linalg.eigvalsh(AH / 6.0)
    assert np.max(np.abs(np.sort(ev) - np.array([-1 / 6] * 6 + [1.0]))) < 1e-10

    # Generic spectral endpoint sanity at K=k=2.
    K0 = k0 = 2
    D0 = (K0 + 1) * k0
    theta0 = K0 + k0 + 2 * (K0 * k0) ** 0.5
    assert abs((theta0 - (K0 + 1)) / D0 - Fraction(5, 6)) < 1e-12

    print("EISENSTEIN_HALVED_EXACT_CONSTANTS")
    print(f"K={K} k={k} Q={Q} D={D}")
    print(f"v={v} a={a}")
    print(f"gap_lower={1-rho}")
    print("center=(3/10) log_2 n")
    print(f"profile_c_squared_on_sqrt_log2={c2_log2}")
    print(f"mixing_quantile_coeff_squared_on_sqrt_log2={tau2_log2}")
    print(f"non_LRE_beta={beta:.15f}")
    print(f"spheres_r0_to_r4={spheres}")
    print("FANO_SPECTRAL_IDENTITY_PASS")
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    check()
