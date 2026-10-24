#!/usr/bin/env python3
"""
ProofNet24 P17 M51 exact checker.

Scope:
- exact right-exterior-contraction signs in the calibrated Example-4.3.3
  noncommutative 4-torus model;
- permutation/anti-commutation signs for iterated PV contractions;
- six codimension-two corner classes z_ij;
- the integral six-corner tomography kernel/image constraints;
- physical (3,4) corner recovery of c34 and c1234.

This script uses integer arithmetic only.  It does NOT prove a spectral gap and
does NOT promote exterior contraction to a universal arbitrary-hull formula.
The arbitrary-hull statement in the run report is proved separately by
iterating the already established magnetic T-duality/restriction theorem.
"""

from itertools import combinations, permutations

GENS = (1, 2, 3, 4)
PAIRS = tuple(combinations(GENS, 2))
EVEN_BASIS = ((),) + PAIRS + ((1, 2, 3, 4),)

EXPECTED_EPS = {
    (1, 2): -1,
    (1, 3): +1,
    (1, 4): -1,
    (2, 3): -1,
    (2, 4): +1,
    (3, 4): -1,
}


def right_contract(term, j):
    """Return (sign, contracted term) for the retained right-contraction convention."""
    if j not in term:
        return 0, ()
    p = term.index(j) + 1
    k = len(term)
    sign = -1 if (k - p) % 2 else +1
    return sign, term[: p - 1] + term[p:]


def compose(term, order):
    coeff = 1
    out = term
    for j in order:
        sign, out2 = right_contract(out, j)
        if sign == 0:
            return 0, ()
        coeff *= sign
        out = out2
    return coeff, out


def permutation_sign_relative_to_sorted(order):
    ranks = {v: i for i, v in enumerate(sorted(order))}
    p = [ranks[v] for v in order]
    inversions = sum(
        1 for a in range(len(p)) for b in range(a + 1, len(p)) if p[a] > p[b]
    )
    return -1 if inversions % 2 else +1


def corner_coordinates(c):
    """Return z_ij=(a_ij,b_ij) with z_ij=a_ij[1]+b_ij[p_kl]."""
    ctop = c.get((1, 2, 3, 4), 0)
    out = {}
    for pair in PAIRS:
        a = -c.get(pair, 0)
        b = EXPECTED_EPS[pair] * ctop
        out[pair] = (a, b)
    return out


def delta_constraints(z):
    """Five image constraints: eps_ij*b_ij must be independent of ij."""
    ref = (1, 2)
    tref = EXPECTED_EPS[ref] * z[ref][1]
    return tuple(
        EXPECTED_EPS[p] * z[p][1] - tref
        for p in PAIRS
        if p != ref
    )


def main():
    # 1. Pairwise anti-commutation on every even basis monomial.
    for i, j in PAIRS:
        for term in EVEN_BASIS:
            c1, o1 = compose(term, (i, j))
            c2, o2 = compose(term, (j, i))
            assert c1 == -c2
            if c1:
                assert o1 == o2

    # 2. Full permutation sign rule for all 2-, 3-, and 4-fold contractions.
    top = (1, 2, 3, 4)
    for k in range(2, 5):
        for subset in combinations(GENS, k):
            base_coeff, base_out = compose(top, subset)
            for order in permutations(subset):
                coeff, out = compose(top, order)
                assert out == base_out
                assert coeff == permutation_sign_relative_to_sorted(order) * base_coeff

    # 3. Recover the exact M50 epsilon table from contractions.
    recovered_eps = {}
    for pair in PAIRS:
        scalar_coeff, scalar_out = compose(pair, pair)
        top_coeff, top_out = compose(top, pair)
        assert scalar_coeff == -1 and scalar_out == ()
        recovered_eps[pair] = top_coeff
        assert set(top_out) == set(GENS) - set(pair)
    assert recovered_eps == EXPECTED_EPS

    # 4. Six-corner tomography has kernel exactly the unit.
    test = {
        (): 17,
        (1, 2): 2,
        (1, 3): -3,
        (1, 4): 5,
        (2, 3): 7,
        (2, 4): -11,
        (3, 4): 13,
        top: -19,
    }
    z = corner_coordinates(test)
    assert all(v != (0, 0) for v in z.values())
    unit_only = {(): 23}
    assert all(v == (0, 0) for v in corner_coordinates(unit_only).values())

    # 5. Image compatibility and integral surjectivity of the constraint map.
    assert delta_constraints(z) == (0, 0, 0, 0, 0)
    common_top = EXPECTED_EPS[(1, 2)] * z[(1, 2)][1]
    assert common_top == test[top]
    assert all(EXPECTED_EPS[p] * z[p][1] == common_top for p in PAIRS)

    nonref = [p for p in PAIRS if p != (1, 2)]
    for target_index in range(5):
        fake = {p: (0, 0) for p in PAIRS}
        p = nonref[target_index]
        fake[p] = (0, EXPECTED_EPS[p])
        got = delta_constraints(fake)
        expected = tuple(1 if q == target_index else 0 for q in range(5))
        assert got == expected

    # 6. Physical pair (3,4): Theta_12=0.
    a34, b34 = z[(3, 4)]
    assert a34 == -test[(3, 4)]
    assert b34 == -test[top]
    recovered_c34 = -a34
    recovered_c1234 = -b34
    assert recovered_c34 == test[(3, 4)]
    assert recovered_c1234 == test[top]

    print("M51 exact checker: PASS")
    print("epsilon =", recovered_eps)
    print("six-corner kernel = Z[1]")
    print("image constraints = eps_ij*b_ij independent of ij (5 integral constraints)")
    print("physical z_34 recovers c34 and c1234 exactly")
    print("NO SPECTRAL GAP CLAIM")


if __name__ == "__main__":
    main()
