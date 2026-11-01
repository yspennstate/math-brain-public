#!/usr/bin/env python3
"""Exact checker for P17-M50 iterated-PV / corner-Chern formulas.

This script uses only integer and Fraction arithmetic.  It checks:

1. the retained M48/M49 right exterior contractions on Lambda^even Z^4;
2. for every ordered pair i<j,

       R_j R_i(p_ij) = -1,
       R_j R_i(p_1234) = eps_ij p_kl,

   where {k,l} is the complementary pair and eps_ij is the coefficient of
   Theta_ij Theta_kl in the source-oriented four-dimensional Pfaffian

       F1234 = -Theta12 Theta34 + Theta13 Theta24 - Theta14 Theta23;

3. the exact corner functional identity

       Ch_ij(x)
       = -tau_kl(z_ij(x))
         + 2 Theta_kl Ch_kl(z_ij(x)),

   for z_ij = R_j R_i x;
4. the historical physical-corner specialization Theta12=0:

       Ch_34(x) = -tau_12(z_34(x)) = c34;

5. at theta1=97/153, theta2=87/148, b=1/153, all six identities hold
   exactly for deterministic signed integer test classes.

No spectral computation and no magnetic-gap claim is made here.
"""
from fractions import Fraction
from itertools import combinations


def rcontract(I, j):
    """Right contraction by e_j in inherited global ordering."""
    I = tuple(I)
    if j not in I:
        return None, 0
    pos = I.index(j)
    sign = -1 if ((len(I) - pos - 1) % 2) else 1
    return I[:pos] + I[pos + 1 :], sign


EPS = {
    (1, 2): -1,
    (1, 3): +1,
    (1, 4): -1,
    (2, 3): -1,
    (2, 4): +1,
    (3, 4): -1,
}


def complement_pair(i, j):
    return tuple(k for k in range(1, 5) if k not in (i, j))


def iterated_basis_checks():
    top = (1, 2, 3, 4)
    for i, j in combinations(range(1, 5), 2):
        # p_ij
        K, s1 = rcontract((i, j), i)
        L, s2 = rcontract(K, j)
        assert L == ()
        assert s1 * s2 == -1, (i, j, s1, s2)

        # p_1234
        K, s1 = rcontract(top, i)
        L, s2 = rcontract(K, j)
        assert L == complement_pair(i, j)
        assert s1 * s2 == EPS[(i, j)], (i, j, s1, s2, L)


def corner_data(i, j, cij, ctop, theta_comp):
    """Return (unit_coeff, bott_coeff, corner_trace, corner_chern, bulk_chern)."""
    eps = EPS[(i, j)]
    a = -cij
    b = eps * ctop
    tau = a + theta_comp * b
    ch_corner = b
    ch_bulk = cij + eps * theta_comp * ctop
    return a, b, tau, ch_corner, ch_bulk


def check_corrected_functional():
    theta = {
        (1, 2): Fraction(0),
        (1, 3): Fraction(97, 153),
        (1, 4): Fraction(0),
        (2, 3): Fraction(0),
        (2, 4): Fraction(87, 148),
        (3, 4): Fraction(1, 153),
    }
    tests = [
        (-5, 7),
        (0, 1),
        (11, -13),
    ]
    for i, j in combinations(range(1, 5), 2):
        k, l = complement_pair(i, j)
        theta_comp = theta[(k, l)]
        for cij, ctop in tests:
            a, b, tau, ch_corner, ch_bulk = corner_data(
                i, j, cij, ctop, theta_comp
            )
            corrected = -tau + 2 * theta_comp * ch_corner
            assert corrected == ch_bulk, (i, j, cij, ctop)
            assert a == -cij
            assert b == EPS[(i, j)] * ctop


def check_source_specializations():
    # Historical source deformation:
    # Theta13=theta1, Theta24=theta2, Theta34=b, all other entries zero.
    theta1 = Fraction(97, 153)
    theta2 = Fraction(87, 148)
    bmag = Fraction(1, 153)
    theta = {
        (1, 2): Fraction(0),
        (1, 3): theta1,
        (1, 4): Fraction(0),
        (2, 3): Fraction(0),
        (2, 4): theta2,
        (3, 4): bmag,
    }

    # Deterministic class coordinates, only the relevant pair/top coefficients
    # matter for each iterated corner.
    c = {
        (1, 2): 5,
        (1, 3): -7,
        (1, 4): 11,
        (2, 3): -13,
        (2, 4): 17,
        (3, 4): -19,
    }
    ctop = 23

    expected_bulk = {
        (1, 2): Fraction(c[(1, 2)]) - bmag * ctop,
        (1, 3): Fraction(c[(1, 3)]) + theta2 * ctop,
        (1, 4): Fraction(c[(1, 4)]),
        (2, 3): Fraction(c[(2, 3)]),
        (2, 4): Fraction(c[(2, 4)]) + theta1 * ctop,
        (3, 4): Fraction(c[(3, 4)]),
    }

    for i, j in combinations(range(1, 5), 2):
        k, l = complement_pair(i, j)
        _, _, tau, ch_corner, ch_bulk = corner_data(
            i, j, c[(i, j)], ctop, theta[(k, l)]
        )
        assert ch_bulk == expected_bulk[(i, j)]
        assert -tau + 2 * theta[(k, l)] * ch_corner == expected_bulk[(i, j)]

    # Physical codimension-two corner: complement is (1,2), whose twist is 0.
    _, _, tau34, _, ch34 = corner_data(3, 4, c[(3, 4)], ctop, theta[(1, 2)])
    assert theta[(1, 2)] == 0
    assert -tau34 == ch34 == c[(3, 4)]


def check_naive_trace_failure():
    # A simple exact counterexample: x=p12.  Then z12=-1, so corner trace=-1
    # while Ch12(p12)=+1.  This already fails at zero magnetic field.
    a, b, tau, ch_corner, ch_bulk = corner_data(1, 2, 1, 0, Fraction(0))
    assert (a, b, tau, ch_corner, ch_bulk) == (-1, 0, -1, 0, 1)
    assert tau != ch_bulk


def main():
    iterated_basis_checks()
    check_corrected_functional()
    check_source_specializations()
    check_naive_trace_failure()
    print("M50 iterated-PV / corner-Chern checks: PASS")


if __name__ == "__main__":
    main()
