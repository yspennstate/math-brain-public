from fractions import Fraction
from itertools import combinations


def He(j, x):
    if j == 0:
        return 1
    if j == 1:
        return x
    a, b = 1, x
    for r in range(1, j):
        a, b = b, x*b - r*a
    return b


def all_edges(n):
    return [(i, j) for i in range(n) for j in range(i+1, n)]


def is_forest(n, edge_list):
    p = list(range(n))
    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x
    for a, b in edge_list:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        p[rb] = ra
    return True


def counts(n, edges, e, f):
    ie, jf = edges.index(e), edges.index(f)
    Z = Ze = Zf = Zef = 0
    for mask in range(1 << len(edges)):
        chosen = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(n, chosen):
            continue
        he = (mask >> ie) & 1
        hf = (mask >> jf) & 1
        Z += 1
        Ze += he
        Zf += hf
        Zef += he*hf
    return Z, Ze, Zf, Zef, Ze*Zf - Z*Zef


def orbit(g, e, f):
    G, E, F = set(g), set(e), set(f)
    te, tf = bool(G & E), bool(G & F)
    adj = bool(E & F)
    if te and tf:
        if not adj:
            return "C"
        if len(G | E | F) == 3:
            return "B"
        return "A"
    if te or tf:
        return "D" if adj else "E"
    return "F" if adj else "G"


def normalized_gaps(n):
    m = n - 4
    x = n + 1
    h = He(m, x)
    s = Fraction(0) if m == 0 else Fraction(m*He(m-1, x), h)
    A = m*m - 5*m*s + 13*m + 4*s*s - 25*s + 28
    B = (m+1)*(m*s - s*s + 4*s + 4)
    C = 4*(-m*s + m + s*s - 5*s + 1)
    D = m*m - 5*m*s + 11*m + 4*s*s - 23*s + 18
    out = {"A": A, "B": B, "C": C, "D": D}
    if m >= 1:
        E = Fraction(2, m)*(-m*m*s + m*m + m*s*s - 3*m - 5*s*s + 24*s)
        F = Fraction(1, m)*(m**3 - 3*m*m*s + 9*m*m + 2*m*s*s - 3*m*s
                            + 9*m - 10*s*s + 48*s)
        out.update({"E": E, "F": F})
    if m >= 2:
        G = Fraction(1, m*(m-1))*(-m**3*s + m**3 + m*m*s*s + 5*m*m*s
                                   - 6*m*m - 10*m*s*s + 2*m*s + 39*m
                                   + 45*s*s - 216*s)
        out["G"] = G
    return h, s, out


def predicted_gap(n, typ):
    if n == 3:
        assert typ == "B"
        return 0
    h, _, A = normalized_gaps(n)
    return A[typ] * h*h


def brute_audit():
    for n in range(3, 7):
        g = (0, 1)
        edges = [e for e in all_edges(n) if e != g]
        orbit_gaps = {}
        for e, f in combinations(edges, 2):
            typ = orbit(g, e, f)
            actual = counts(n, edges, e, f)[-1]
            expected = predicted_gap(n, typ)
            assert actual == expected, (n, typ, e, f, actual, expected)
            orbit_gaps.setdefault(typ, set()).add(actual)
        assert all(len(v) == 1 for v in orbit_gaps.values())
        print("BRUTE", n, {k: next(iter(v)) for k, v in sorted(orbit_gaps.items())})


def symbolic_integer_audit(limit=1000):
    # Regression only. The proof in report.md is symbolic.
    for n in range(4, limit+1):
        m = n - 4
        h, s, A = normalized_gaps(n)
        assert h > 0
        if m >= 1:
            assert 0 < s < Fraction(m, m+4)
        for typ, val in A.items():
            assert val > 0, (n, typ, val)
    print("FORMULA_POSITIVITY_EXACT", f"n=4..{limit}", "PASS")


if __name__ == "__main__":
    brute_audit()
    symbolic_integer_audit(1000)
    print("ALL_EXACT_CHECKS_PASS")
