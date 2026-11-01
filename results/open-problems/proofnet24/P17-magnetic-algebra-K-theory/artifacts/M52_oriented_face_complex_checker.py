#!/usr/bin/env python3
"""Exact sign checks for ProofNet24 P17 M52.

This artifact verifies only finite combinatorial sign identities used in the
orientation-normalized iterated PV/face-complex argument.  It performs no
spectral computation and makes no magnetic-gap claim.
"""

from itertools import combinations, permutations


def parity_of_permutation(seq):
    inv = sum(1 for a in range(len(seq)) for b in range(a + 1, len(seq)) if seq[a] > seq[b])
    return -1 if inv % 2 else 1


def incidence_sign(J, j):
    """Sign from appending j after increasing J, then sorting increasingly."""
    return -1 if sum(1 for i in J if i > j) % 2 else 1


def right_contract(I, j):
    """M48/M50 right exterior contraction R_j on an ordered basis monomial.

    Returns (coefficient, remaining_tuple).  The coefficient is 0 if j is
    absent.  For I=(i_1<...<i_m) and j=i_s, coefficient=(-1)^(m-s).
    """
    if j not in I:
        return 0, ()
    m = len(I)
    pos = I.index(j)  # zero based, so s=pos+1
    coeff = -1 if (m - (pos + 1)) % 2 else 1
    return coeff, I[:pos] + I[pos + 1 :]


def iter_contract(I, order):
    coeff = 1
    cur = tuple(I)
    for j in order:
        c, cur = right_contract(cur, j)
        if c == 0:
            return 0, ()
        coeff *= c
    return coeff, cur


def check_incidence_squares(max_d=8):
    for d in range(2, max_d + 1):
        coords = tuple(range(1, d + 1))
        for k in range(d - 1):
            for J in combinations(coords, k):
                rem = [x for x in coords if x not in J]
                for i, j in combinations(rem, 2):
                    Ji = tuple(sorted(J + (i,)))
                    Jj = tuple(sorted(J + (j,)))
                    route_i_j = incidence_sign(J, i) * incidence_sign(Ji, j)
                    route_j_i = incidence_sign(J, j) * incidence_sign(Jj, i)
                    assert route_i_j == -route_j_i, (d, J, i, j)


def check_right_contraction_anticommutation(max_d=7):
    for d in range(2, max_d + 1):
        coords = tuple(range(1, d + 1))
        for r in range(d + 1):
            for I in combinations(coords, r):
                for i, j in combinations(coords, 2):
                    c_ij, out_ij = iter_contract(I, (i, j))
                    c_ji, out_ji = iter_contract(I, (j, i))
                    assert out_ij == out_ji or (c_ij == c_ji == 0)
                    assert c_ij == -c_ji, (d, I, i, j, c_ij, c_ji)


def check_oriented_order_independence(max_d=7):
    """Contraction sign times normal-orientation sign is permutation invariant."""
    for d in range(1, max_d + 1):
        coords = tuple(range(1, d + 1))
        for k in range(1, d + 1):
            for J in combinations(coords, k):
                # Test on the top monomial containing J; any extra indices are okay.
                I = coords
                base_order = tuple(J)
                base_c, base_out = iter_contract(I, base_order)
                for p in permutations(J):
                    c, out = iter_contract(I, p)
                    perm_sign = parity_of_permutation(p)
                    # Wedge orientation e_{p1}^...^e_{pk} has perm_sign relative to sorted J.
                    assert out == base_out
                    assert c * perm_sign == base_c, (d, J, p, c, base_c)


def check_source_physical_corner():
    # z_34 = R_4 R_3.  It sends e_34 -> -1 and e_1234 -> -e_12.
    c34, out34 = iter_contract((3, 4), (3, 4))
    ctop, outtop = iter_contract((1, 2, 3, 4), (3, 4))
    assert (c34, out34) == (-1, ())
    assert (ctop, outtop) == (-1, (1, 2))


def main():
    check_incidence_squares()
    check_right_contraction_anticommutation()
    check_oriented_order_independence()
    check_source_physical_corner()
    print("M52 exact sign checks: PASS")
    print("incidence sign: (-1)^{#{i in J : i>j}}")
    print("all tested cubical squares cancel; oriented iterated corners are order independent")
    print("source calibration: R4 R3(e34)=-1, R4 R3(e1234)=-e12")
    print("NO SPECTRAL OR GAP CLAIM")


if __name__ == "__main__":
    main()
