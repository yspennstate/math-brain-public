"""ProofNet24 P17 M53 exact combinatorial certificate.

Supports:
  P17-M53-TORAL-PV-SUBCUBE-EXACT-49
  P17-M53-INTEGRAL-PV-LIFTING-HOMOTOPY-49

This script verifies the exterior-basis chain model for coordinate Pimsner-Voiculescu
maps of the source noncommutative torus.  It uses exact integer arithmetic only.
It does NOT diagonalize a Hamiltonian, does NOT certify a spectral gap, and does NOT
claim arbitrary-hull exactness.

Convention: for an increasing exterior monomial e_I and j in I, the right contraction
is
    R_j(e_I) = (-1)^(#{i in I: i>j}) e_{I\{j}}.
For a chosen set P of cut coordinates, the degree-k group has basis pairs (J,I),
where J subset P has |J|=k and I is disjoint from J with the K-parity appropriate to
that degree.  The differential sums R_j over j in P\J.

For a basis pair set
    U = I\P,
    S = J union (I intersection P).
Both U and S are differential invariants.  If S is nonempty, choosing s0=min(S)
gives a signed cubical contracting homotopy h with delta*h+h*delta=id.  If S is
empty the only state is in degree zero and is exactly the coordinate-subtorus
augmentation summand.
"""

from itertools import combinations


def all_subsets(items):
    items = tuple(sorted(items))
    for r in range(len(items) + 1):
        for c in combinations(items, r):
            yield frozenset(c)


def right_contraction_sign(I, j):
    """Coefficient of R_j(e_I), assuming j in I."""
    return -1 if sum(i > j for i in I) % 2 else 1


def basis_states(n, P, q, k):
    """Basis (J,I) of degree k in the q-parity PV subcube."""
    universe = set(range(1, n + 1))
    out = []
    for J_tuple in combinations(sorted(P), k):
        J = frozenset(J_tuple)
        for I in all_subsets(universe - set(J)):
            if len(I) % 2 == ((q - k) % 2):
                out.append((J, I))
    return out


def delta_state(P, state):
    """Exact differential of one basis state as an integer coefficient dictionary."""
    J, I = state
    out = {}
    for j in sorted(set(P) - set(J)):
        if j in I:
            target = (frozenset(set(J) | {j}), frozenset(set(I) - {j}))
            out[target] = out.get(target, 0) + right_contraction_sign(I, j)
    return {x: c for x, c in out.items() if c}


def invariant_US(P, state):
    J, I = state
    U = frozenset(set(I) - set(P))
    S = frozenset(set(J) | (set(I) & set(P)))
    return U, S


def homotopy_state(P, state):
    """Signed contraction h on every S!=empty summand; zero on S=empty."""
    J, I = state
    _, S = invariant_US(P, state)
    if not S:
        return {}
    s0 = min(S)
    if s0 not in J:
        return {}
    J_prev = frozenset(set(J) - {s0})
    I_prev = frozenset(set(I) | {s0})
    # This is the coefficient of the distinguished delta edge back to (J,I).
    eps = right_contraction_sign(I_prev, s0)
    return {(J_prev, I_prev): eps}


def add_term(out, state, coeff):
    out[state] = out.get(state, 0) + coeff
    if out[state] == 0:
        del out[state]


def delta_h_plus_h_delta(P, state):
    out = {}
    for hs, hc in homotopy_state(P, state).items():
        for ds, dc in delta_state(P, hs).items():
            add_term(out, ds, hc * dc)
    for ds, dc in delta_state(P, state).items():
        for hs, hc in homotopy_state(P, ds).items():
            add_term(out, hs, dc * hc)
    return out


def check_delta_squared(n, P, q):
    for k in range(len(P)):
        for state in basis_states(n, P, q, k):
            out = {}
            for mid, c1 in delta_state(P, state).items():
                for fin, c2 in delta_state(P, mid).items():
                    add_term(out, fin, c1 * c2)
            assert out == {}, ("delta^2 failure", n, P, q, k, state, out)


def check_homotopy(n, P, q):
    for k in range(len(P) + 1):
        for state in basis_states(n, P, q, k):
            _, S = invariant_US(P, state)
            got = delta_h_plus_h_delta(P, state)
            if S:
                assert got == {state: 1}, (
                    "homotopy failure", n, P, q, k, state, got
                )
            else:
                assert k == 0
                assert got == {}


def group_ranks(n, P, q):
    return [len(basis_states(n, P, q, k)) for k in range(len(P) + 1)]


def augmentation_rank(n, P, q):
    """Rank of K_q of the coordinate subtorus with all P-generators deleted."""
    remaining = n - len(P)
    return sum(
        1
        for I in all_subsets(range(1, remaining + 1))
        if len(I) % 2 == q
    )


def check_all(max_n=7):
    for n in range(1, max_n + 1):
        universe = set(range(1, n + 1))
        for P in all_subsets(universe):
            if not P:
                continue
            for q in (0, 1):
                check_delta_squared(n, P, q)
                check_homotopy(n, P, q)

    # Source n=4 rank calibrations.
    P_all = frozenset({1, 2, 3, 4})
    assert group_ranks(4, P_all, 0) == [8, 16, 12, 4, 1]
    assert group_ranks(4, P_all, 1) == [8, 16, 12, 4, 0]
    assert augmentation_rank(4, P_all, 0) == 1
    assert augmentation_rank(4, P_all, 1) == 0

    # Physical two-cut source square P={3,4}: M49 calibration.
    P_phys = frozenset({3, 4})
    assert group_ranks(4, P_phys, 0) == [8, 8, 2]
    assert group_ranks(4, P_phys, 1) == [8, 8, 2]
    assert augmentation_rank(4, P_phys, 0) == 2
    assert augmentation_rank(4, P_phys, 1) == 2

    # M50/M51 physical corner orientation calibration.
    e34 = frozenset({3, 4})
    e1234 = frozenset({1, 2, 3, 4})
    # R_4 R_3 means first R_3, then R_4.
    c34 = right_contraction_sign(e34, 3) * right_contraction_sign(
        frozenset({4}), 4
    )
    c1234 = right_contraction_sign(e1234, 3) * right_contraction_sign(
        frozenset({1, 2, 4}), 4
    )
    assert c34 == -1
    assert c1234 == -1

    print("PASS: delta^2=0 and integral contracting homotopy verified for n<=7")
    print("PASS: n=4 full-cut q=0 ranks [8,16,12,4,1], augmentation rank 1")
    print("PASS: n=4 full-cut q=1 ranks [8,16,12,4,0], augmentation rank 0")
    print("PASS: physical P={3,4} ranks [8,8,2] in both parities; augmentation rank 2")
    print("PASS: R_4 R_3(e_34)=-1 and R_4 R_3(e_1234)=-e_12")
    print("NO SPECTRAL GAP CLAIM; NO ARBITRARY-HULL EXACTNESS CLAIM")


if __name__ == "__main__":
    check_all()
