"""Exact checks for the two-site trap example.

For small m and rational e this script builds the weighted graph directly,
solves the meeting-time equations of two independent walkers on all ordered
pairs, and solves the full coalescing chain on occupied subsets, all in exact
rational arithmetic. It compares the results with the closed forms of
Section 2 and with the bounds of Theorem 3.1.
"""
from fractions import Fraction as F
from itertools import combinations


def graph(m, e):
    n = m + 2
    a = (1 - 2 * e / m) / (m - 1)
    nu = [[F(0)] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == y:
                continue
            if x < m and y < m:
                nu[x][y] = a
            elif x >= m and y >= m:
                nu[x][y] = 1 - e
            else:
                nu[x][y] = e / m
    return n, a, nu


def solve(A, b):
    """Gaussian elimination over the rationals."""
    k = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(k):
        p = next(r for r in range(c, k) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        piv = M[c][c]
        M[c] = [v / piv for v in M[c]]
        for r in range(k):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [vr - f * vc for vr, vc in zip(M[r], M[c])]
    return [M[i][k] for i in range(k)]


def pair_means(m, e):
    n, a, nu = graph(m, e)
    pairs = [(x, y) for x in range(n) for y in range(n) if x != y]
    idx = {p: i for i, p in enumerate(pairs)}
    k = len(pairs)
    A = [[F(0)] * k for _ in range(k)]
    for (x, y), i in idx.items():
        for z in range(n):
            for (u, v, w) in ((z, y, nu[x][z]), (x, z, nu[y][z])):
                q = w / 2
                if q == 0:
                    continue
                A[i][i] += q
                if u != v:
                    A[i][idx[(u, v)]] -= q
    h = solve(A, [F(1)] * k)
    return n, a, {p: h[idx[p]] for p in pairs}


def closed_forms(m, e):
    n = m + 2
    a = (1 - 2 * e / m) / (m - 1)
    b = 2 * e / m
    d = m + 2 - e
    D = a * d + b * (3 - e)
    A = (m + 6 - e + 2 * e / m) / D
    B = ((m - 1) * A + 2 * m / e + 1) / d
    C = 1 + e * B
    tau = (m * (m - 1) * A + 4 * m * B + 2 * C) / n ** 2
    return A, B, C, tau


def coalescence_mean(m, e):
    """E T from full occupancy, by first-step analysis on occupied sets."""
    n, a, nu = graph(m, e)
    sets = [frozenset(c) for s in range(2, n + 1) for c in combinations(range(n), s)]
    idx = {s: i for i, s in enumerate(sets)}
    k = len(sets)
    A = [[F(0)] * k for _ in range(k)]
    death_ok = True
    for s, i in idx.items():
        death = F(0)
        for x in s:
            for z in range(n):
                q = nu[x][z] / 2
                if q == 0 or z == x:
                    continue
                t = (s - {x}) | {z}
                A[i][i] += q
                if len(t) >= 2:
                    A[i][idx[t]] -= q
                if z in s:
                    death += q
        if len(s) >= 3 and a > 0 and death < a * len(s) * (len(s) - 1) / 6:
            death_ok = False
    sol = solve(A, [F(1)] * k)
    return sol[idx[frozenset(range(n))]], death_ok


def symbolic():
    """The identities of Sections 2 and 3, for symbolic m and e (requires sympy)."""
    import sympy as sp
    m, e = sp.symbols("m e", positive=True)
    a = (1 - 2 * e / m) / (m - 1)
    b = 2 * e / m
    d = m + 2 - e
    D = a * d + b * (3 - e)
    A = (m + 6 - e + 2 * e / m) / D
    B = ((m - 1) * A + 2 * m / e + 1) / d
    C = 1 + e * B
    eqs = [(a + b) * A - b * B - 1,
           -e * (m - 1) * A / (2 * m) + e * (m + 2) * B / (2 * m) - e * C / (2 * m) - 1,
           C - e * B - 1]
    P = (m - 2 * e) * d + 2 * e * (m - 1) * (3 - e)
    NA = (m - 1) * (m ** 2 + 6 * m - e * m + 2 * e)
    NB = (m + 2 * e * (m - 2)) * (2 * m + e) + e * m * (m - 1) ** 2
    checks = {
        "pair system (2.2) solved by (2.3)": all(sp.simplify(q) == 0 for q in eqs),
        "A = N_A/P": sp.simplify(A - NA / P) == 0,
        "B = N_B/(eP)": sp.simplify(B - NB / (e * P)) == 0,
        "identity (2.5)": sp.expand(NB - e * NA - (m - (m + 1) * e) * (2 * m - (m - 2) * e)) == 0,
        "1-e-a formula": sp.simplify(1 - e - a - (m - 2) * (m - (m + 1) * e) / (m * (m - 1))) == 0,
        "B-C decomposition": sp.simplify((B - C) - ((1 - e - a) * B + (a + b) * (B - A))) == 0,
        "R formula": sp.simplify(1 - e - a + 2 * e / m - ((m - 2) - e * (m - 3)) / (m - 1)) == 0,
    }
    k = sp.symbols("k", positive=True)
    death = lambda kk, j: a * kk * (kk - 1) / 2 + (1 - e) * j * (j - 1) / 2 + e * kk * j / m
    s = lambda kk, j: kk + j
    checks["death j=0"] = sp.simplify(death(k, 0) - a * s(k, 0) * (s(k, 0) - 1) / 6 - a * k * (k - 1) / 3) == 0
    checks["death j=1"] = sp.simplify(death(k, 1) - a * s(k, 1) * (s(k, 1) - 1) / 6
                                      - (a * k * (k - 2) / 3 + e * k / m)) == 0
    R = 1 - e - a + 2 * e / m
    checks["death j=2"] = sp.simplify(death(k, 2) - a * s(k, 2) * (s(k, 2) - 1) / 6
                                      - (a * (k - 1) * (k - 2) / 3 + R + 2 * e * (k - 1) / m)) == 0
    for name, ok in checks.items():
        print("  %-36s %s" % (name, "ok" if ok else "FAIL"))
    return sum(not ok for ok in checks.values())


def main():
    bad = symbolic()
    cases = [(m, e) for m in (2, 3, 4, 5) for e in (F(1, 10), F(1, 3), F(1, 2), F(1))]
    cases += [(6, F(1, 7)), (6, F(1, 50))]
    print("m  e      A        B        C        tau      E_T      M<=E_T<=L  death>=a s(s-1)/6")
    for m, e in cases:
        n, a, h = pair_means(m, e)
        A, B, C, tau = closed_forms(m, e)
        core = [h[(x, y)] for x in range(m) for y in range(m) if x != y]
        mixed = [h[(x, y)] for x in range(n) for y in range(n) if (x < m) != (y < m)]
        trap = [h[(m, m + 1)], h[(m + 1, m)]]
        ok = set(core) == {A} and set(mixed) == {B} and set(trap) == {C}
        tau_direct = sum(h.values()) / n ** 2
        ok = ok and tau_direct == tau
        line = "%d  %-5s  %-8.4f %-8.4f %-8.4f %-8.4f" % (m, e, float(A), float(B), float(C), float(tau))
        if m <= 5:
            ET, death_ok = coalescence_mean(m, e)
            M = max(A, B, C)
            if a > 0:
                L = M + (6 / a) * (F(1, 2) - F(1, n))
                bounds = M <= ET <= L
            else:
                bounds = M <= ET
            line += " %-8.4f %-10s %s" % (float(ET), bounds, death_ok)
            ok = ok and bounds and death_ok
        print(line, "" if ok else "  FAIL")
        bad += not ok
    print("all checks passed" if bad == 0 else "%d case(s) failed" % bad)
    return bad


if __name__ == "__main__":
    raise SystemExit(main())
