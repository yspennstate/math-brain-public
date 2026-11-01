"""Exact verifier for HARD8-04 Hadamard/Legendre-pair checkpoint.

No external packages are required. The script:
1. verifies the Legendre-pair -> Hadamard two-circulant-core construction;
2. verifies the exact defect-energy identities used in the report on small cases;
3. certifies a length-15 minimum-positive-energy state that has no strictly
   energy-decreasing move when each sequence may perform at most one balanced
   (+1 <-> -1) exchange, but that reaches a Legendre pair through one plateau
   move followed by a decrease.
"""

from itertools import combinations


def seq_from_plus(v, plus):
    s = set(plus)
    return [1 if i in s else -1 for i in range(v)]


def paf(a, t):
    v = len(a)
    return sum(a[i] * a[(i + t) % v] for i in range(v))


def defect_half(a, b):
    v = len(a)
    assert v % 2 == 1
    return [paf(a, t) + paf(b, t) + 2 for t in range(1, (v + 1) // 2)]


def defect_energy(a, b):
    return sum(x * x for x in defect_half(a, b))


def is_legendre(a, b):
    return all(x == 0 for x in defect_half(a, b))


def circulant(a):
    v = len(a)
    return [[a[(j - i) % v] for j in range(v)] for i in range(v)]


def transpose(M):
    return [list(row) for row in zip(*M)]


def matmul(A, B):
    BT = transpose(B)
    return [[sum(x * y for x, y in zip(r, c)) for c in BT] for r in A]


def build_hadamard_from_legendre(a, b):
    """Two-circulant-core construction for odd-length binary Legendre pair
    normalized so sum(a)=sum(b)=1.
    """
    v = len(a)
    assert len(b) == v and v % 2 == 1
    assert sum(a) == 1 and sum(b) == 1 and is_legendre(a, b)
    A = circulant(a)
    B = circulant(b)
    BT = transpose(B)
    AT = transpose(A)

    H = []
    H.append([1, 1] + [-1] * v + [-1] * v)
    H.append([1, -1] + [1] * v + [-1] * v)
    for i in range(v):
        H.append([1, 1] + A[i] + B[i])
    for i in range(v):
        H.append([1, -1] + [-x for x in BT[i]] + AT[i])
    return H


def verify_hadamard(H):
    n = len(H)
    assert all(len(r) == n for r in H)
    assert all(x in (-1, 1) for r in H for x in r)
    G = matmul(H, transpose(H))
    for i in range(n):
        for j in range(n):
            want = n if i == j else 0
            assert G[i][j] == want, (i, j, G[i][j], want)
    return True


def balanced_plus_sets(v):
    return list(combinations(range(v), (v + 1) // 2))


def balanced_exchange_neighbors(plus, v):
    S = set(plus)
    ans = {tuple(sorted(S))}
    for i in list(S):
        for j in range(v):
            if j not in S:
                ans.add(tuple(sorted((S - {i}) | {j})))
    return sorted(ans)


def min_joint_one_exchange_energy(Aplus, Bplus, v):
    best = None
    witness = None
    for Ap in balanced_exchange_neighbors(Aplus, v):
        a = seq_from_plus(v, Ap)
        for Bp in balanced_exchange_neighbors(Bplus, v):
            b = seq_from_plus(v, Bp)
            e = defect_energy(a, b)
            if best is None or e < best:
                best, witness = e, (Ap, Bp)
    return best, witness


def exhaustive_energy_counts(v):
    sets = balanced_plus_sets(v)
    counts = {}
    for A in sets:
        a = seq_from_plus(v, A)
        for B in sets:
            b = seq_from_plus(v, B)
            e = defect_energy(a, b)
            counts[e] = counts.get(e, 0) + 1
            d = defect_half(a, b)
            # Exact invariants proved in the accompanying report.
            assert all(x % 4 == 0 for x in d)
            assert sum(d) == 0
            if e != 0:
                assert e >= 32
    return counts


def main():
    expected = {
        3: {0: 9},
        5: {0: 50, 32: 50},
    }
    for v in (3, 5, 7, 9):
        counts = exhaustive_energy_counts(v)
        print("v", v, "energy_counts", dict(sorted(counts.items())))
        if v in expected:
            assert counts == expected[v]

    # Exact v=15 strict-descent obstruction.
    A0 = (0, 2, 4, 5, 6, 7, 11, 14)
    B0 = (3, 5, 7, 8, 10, 11, 13, 14)
    a0, b0 = seq_from_plus(15, A0), seq_from_plus(15, B0)
    assert sum(a0) == sum(b0) == 1
    assert defect_half(a0, b0) == [-4, 0, 4, 0, 0, 0, 0]
    assert defect_energy(a0, b0) == 32
    best, _ = min_joint_one_exchange_energy(A0, B0, 15)
    assert best == 32
    print("v15 strict one-exchange minimum energy:", best)

    # Plateau move followed by exact Legendre pair.
    A1 = A0
    B1 = (0, 5, 7, 8, 10, 11, 13, 14)
    A2 = (0, 4, 5, 6, 7, 9, 11, 14)
    B2 = (0, 2, 7, 8, 10, 11, 13, 14)
    a1, b1 = seq_from_plus(15, A1), seq_from_plus(15, B1)
    a2, b2 = seq_from_plus(15, A2), seq_from_plus(15, B2)
    assert defect_half(a1, b1) == [0, 0, 4, -4, 0, 0, 0]
    assert defect_energy(a1, b1) == 32
    assert is_legendre(a2, b2)
    assert defect_energy(a2, b2) == 0
    print("plateau path energies:", 32, 32, 0)

    # Build and exactly verify the resulting Hadamard matrix of order 32.
    H = build_hadamard_from_legendre(a2, b2)
    assert len(H) == 32
    assert verify_hadamard(H)
    print("verified exact Hadamard order:", len(H))


if __name__ == "__main__":
    main()
