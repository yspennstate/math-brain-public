from fractions import Fraction
from math import comb, factorial


def tree_count(s):
    return 1 if s == 1 else s ** (s - 2)


def forest_numbers(N):
    """Number F[n] of labelled unrooted forests on [n]."""
    F = [0] * (N + 1)
    F[0] = 1
    for n in range(1, N + 1):
        # Choose the component containing label 0, then a tree on it.
        F[n] = sum(
            comb(n - 1, s - 1) * tree_count(s) * F[n - s]
            for s in range(1, n + 1)
        )
    return F


def hermites(m, x):
    """Probabilists' Hermite He_0,...,He_m at integer x."""
    H = [1]
    if m >= 1:
        H.append(x)
    for j in range(1, m):
        H.append(x * H[j] - j * H[j - 1])
    return H


def q_adj_component(n, F):
    """Exact overlap reservoir q for e=ab,f=ac in K_n."""
    total = 0
    # Q means a is in one component and b,c are in a second component.
    # r is the size of the a-component, s the size of the bc-component.
    for r in range(1, n - 1):
        for s in range(2, n - r + 1):
            rem = n - r - s
            if rem < 0:
                continue
            ways = factorial(n - 3) // (
                factorial(r - 1) * factorial(s - 2) * factorial(rem)
            )
            total += ways * tree_count(r) * tree_count(s) * F[rem]
    return total


def q_dis_component(n, F):
    """Exact overlap reservoir q for e=ab,f=cd in K_n."""
    total = 0
    # Q has one of two cross pairings ac|bd or ad|bc in distinct components.
    for r in range(2, n - 1):
        for s in range(2, n - r + 1):
            rem = n - r - s
            if rem < 0:
                continue
            ways = factorial(n - 4) // (
                factorial(r - 2) * factorial(s - 2) * factorial(rem)
            )
            total += 2 * ways * tree_count(r) * tree_count(s) * F[rem]
    return total


def q_adj_hermite(n):
    m = n - 3
    return hermites(m, n + 1)[m]


def q_dis_hermite(n):
    m = n - 4
    H = hermites(m, n + 1)
    value = 2 * factorial(m) * sum(
        Fraction(H[j], factorial(j)) for j in range(m + 1)
    )
    assert value.denominator == 1
    return value.numerator


def components(n, edges):
    parent = list(range(n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        parent[b] = a
        return True

    for a, b in edges:
        if not union(a, b):
            return None
    return [find(i) for i in range(n)]


def state_counts(n, e, f):
    """Partner A_ij/q counts in K_n-{e,f}, by exact subset enumeration."""
    all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    e, f = tuple(sorted(e)), tuple(sorted(f))
    base = [g for g in all_edges if g not in (e, f)]
    n00 = n10 = n01 = n11 = q = 0
    for mask in range(1 << len(base)):
        edges = [base[k] for k in range(len(base)) if (mask >> k) & 1]
        c = components(n, edges)
        if c is None:
            continue
        X = c[e[0]] != c[e[1]]
        Y = c[f[0]] != c[f[1]]
        if not X and not Y:
            n00 += 1
        elif X and not Y:
            n10 += 1
        elif not X and Y:
            n01 += 1
        else:
            n11 += 1
            if {c[e[0]], c[e[1]]} == {c[f[0]], c[f[1]]}:
                q += 1
    return n00, n10, n01, n11, q


def full_counts(n, e, f):
    """(Z,E,J) on K_n, where E=Z_e and J=Z_ef."""
    all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    e, f = tuple(sorted(e)), tuple(sorted(f))
    Z = E = J = 0
    for mask in range(1 << len(all_edges)):
        edges = [all_edges[k] for k in range(len(all_edges)) if (mask >> k) & 1]
        if components(n, edges) is None:
            continue
        Z += 1
        edge_set = set(edges)
        if e in edge_set:
            E += 1
        if e in edge_set and f in edge_set:
            J += 1
    return Z, E, J


def main():
    max_formula_n = 20
    F = forest_numbers(max_formula_n)
    print("FOREST component-reservoir exact checker")
    print("All arithmetic integer/rational; no randomization.\n")

    for kind in ("adjacent", "disjoint"):
        ns = range(3, 7) if kind == "adjacent" else range(4, 7)
        print(f"[{kind}]")
        for n in ns:
            e = (0, 1)
            f = (0, 2) if kind == "adjacent" else (2, 3)
            st = state_counts(n, e, f)
            Z, E, J = full_counts(n, e, f)
            n00, n10, n01, n11, q = st
            q_component = q_adj_component(n, F) if kind == "adjacent" else q_dis_component(n, F)
            q_hermite = q_adj_hermite(n) if kind == "adjacent" else q_dis_hermite(n)

            assert q == q_component == q_hermite
            assert n11 == J + q
            assert n10 == E - 2 * J - q
            assert n01 == E - 2 * J - q
            assert n00 == Z - 4 * E + 4 * J + q
            N = sum(st[:4])
            assert N == Z - 2 * E + J
            partner_gap = n10 * n01 - n00 * n11 + N * q
            orbit_gap = E * E - Z * J
            assert partner_gap == orbit_gap

            print(
                f"n={n} states={st} full=(Z={Z},E={E},J={J}) "
                f"q_component={q_component} q_hermite={q_hermite} gap={orbit_gap}"
            )
        print()

    for n in range(3, max_formula_n + 1):
        assert q_adj_component(n, F) == q_adj_hermite(n)
    for n in range(4, max_formula_n + 1):
        assert q_dis_component(n, F) == q_dis_hermite(n)

    print(f"FORMULA_CROSSCHECK_PASS adjacent n=3..{max_formula_n}; disjoint n=4..{max_formula_n}")
    print("BRUTE_PARTNER_RECONSTRUCTION_PASS adjacent n=3..6; disjoint n=4..6")
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
