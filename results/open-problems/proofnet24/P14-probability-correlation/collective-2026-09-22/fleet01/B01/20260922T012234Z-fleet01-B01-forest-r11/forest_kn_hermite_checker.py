#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction


def is_forest(n, edges, mask):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True

    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1 and not union(u, v):
            return False
    return True


def brute_counts(n):
    edges = list(combinations(range(n), 2))
    idx = {e: i for i, e in enumerate(edges)}
    e = (0, 1)
    f_adj = (0, 2) if n >= 3 else None
    f_dis = (2, 3) if n >= 4 else None
    Z = E = Ja = Jd = 0
    ie = idx[e]
    ia = idx[f_adj] if f_adj else None
    idd = idx[f_dis] if f_dis else None
    for mask in range(1 << len(edges)):
        if not is_forest(n, edges, mask):
            continue
        Z += 1
        xe = (mask >> ie) & 1
        E += xe
        if ia is not None:
            Ja += xe * ((mask >> ia) & 1)
        if idd is not None:
            Jd += xe * ((mask >> idd) & 1)
    return Z, E, Ja, Jd


def hermites(kmax, x):
    H = [0] * (kmax + 1)
    H[0] = 1
    if kmax >= 1:
        H[1] = x
    for k in range(1, kmax):
        H[k + 1] = x * H[k] - k * H[k - 1]
    return H


def formula_counts(n):
    x = n + 1
    H = hermites(n, x)

    def D(k):
        if k < 0:
            return 0
        return H[k] - (k * H[k - 1] if k else 0)

    Z = D(n)
    E = D(n - 2)
    Ja = D(n - 3) if n >= 3 else 0
    if n >= 4:
        k = n - 4
        Jd = 5 * H[k] - (k * H[k - 1] if k else 0)
    else:
        Jd = 0
    return Z, E, Ja, Jd, H


def G_num(n, s):
    return (
        Fraction(5 - n) * s * s
        + Fraction(n * n - 4 * n - 6) * s
        + Fraction(-n * n + 9 * n - 14)
    )


def L(n):
    return Fraction((n - 4) * (n - 1) * (n + 4), (n + 1) ** 3)


def P(n):
    return (
        2 * n**6
        + 70 * n**5
        - 33 * n**4
        + 185 * n**3
        + 1369 * n**2
        - 3147 * n
        + 1170
    )


def Pshift(t):
    return (
        2 * t**6
        + 142 * t**5
        + 3147 * t**4
        + 33233 * t**3
        + 187651 * t**2
        + 551661 * t
        + 666396
    )


def main():
    print("FOREST K_n Hermite exact checker")
    print("brute/formula checks")
    for n in range(2, 7):
        b = brute_counts(n)
        f = formula_counts(n)[:4]
        print(f"n={n} brute={b} formula={f} match={b == f}")
        assert b == f

    print("small exact Rayleigh gaps")
    for n in range(3, 6):
        Z, E, Ja, Jd, _ = formula_counts(n)
        ga = E * E - Z * Ja
        gd = E * E - Z * Jd if n >= 4 else None
        print(
            f"n={n} Z={Z} E={E} J_adj={Ja} J_dis={Jd} "
            f"gap_adj={ga} gap_dis={gd}"
        )
        assert ga >= 0
        if gd is not None:
            assert gd >= 0

    print("symbolic-rational identities and bounds n=6..500")
    min_gap = None
    for n in range(6, 501):
        Z, E, Ja, Jd, H = formula_counts(n)
        k = n - 4
        a = H[k]
        assert a > 0
        s = Fraction(k * H[k - 1], H[k])
        assert Fraction(0) <= s < Fraction(1)
        assert s >= L(n)
        assert G_num(n, L(n)) == Fraction(P(n), (n + 1) ** 6)
        assert P(n) == Pshift(n - 6)
        assert P(n) > 0
        gd = E * E - Z * Jd
        ga = E * E - Z * Ja
        assert gd > 0 and ga > 0
        assert gd == a * a * G_num(n, s)
        assert Jd == Ja + a
        if min_gap is None or gd < min_gap[0]:
            min_gap = (gd, n)

    print("all n=6..500 exact checks PASS")
    print(
        "P(n) shift coefficients all positive: "
        "2,142,3147,33233,187651,551661,666396"
    )
    print(
        "minimum absolute disjoint gap over checked n=6..500 occurs at "
        f"n={min_gap[1]} and equals {min_gap[0]}"
    )
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
