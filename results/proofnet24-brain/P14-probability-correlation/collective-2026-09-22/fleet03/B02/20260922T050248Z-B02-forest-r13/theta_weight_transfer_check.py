from fractions import Fraction


def is_forest(n, es):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for u, v in es:
        a, b = find(u), find(v)
        if a == b:
            return False
        p[b] = a
    return True


def unit_counts(n, edges, e, f):
    z = ze = zf = zef = 0
    m = len(edges)
    for mask in range(1 << m):
        F = [edges[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, F):
            continue
        z += 1
        if e in F:
            ze += 1
        if f in F:
            zf += 1
        if e in F and f in F:
            zef += 1
    return z, ze, zf, zef


def weighted_counts(n, edges, weights, e, f):
    z = ze = zf = zef = Fraction(0)
    m = len(edges)
    for mask in range(1 << m):
        F = [edges[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, F):
            continue
        w = Fraction(1)
        for ed in F:
            w *= weights.get(ed, Fraction(1))
        z += w
        if e in F:
            ze += w
        if f in F:
            zf += w
        if e in F and f in F:
            zef += w
    return z, ze, zf, zef


def gap(c):
    z, ze, zf, zef = c
    return ze * zf - z * zef


for a, k in [(2, 2), (2, 3), (3, 2)]:
    l0 = (2**a - 1) ** k
    l1 = k * (2**a - 1) ** (k - 1)
    assert Fraction(l1, l0) == Fraction(k, 2**a - 1)
    print("local", a, k, "L0", l0, "L1", l1, "q", Fraction(l1, l0))

base = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
g = (0, 1)
e = (0, 2)
f = (1, 3)
q = Fraction(2, 3)
wc = weighted_counts(4, base, {g: q}, e, f)
assert wc == (Fraction(100, 3), Fraction(38, 3), Fraction(38, 3), Fraction(14, 3))
assert gap(wc) == Fraction(44, 9)

rep = [ed for ed in base if ed != g] + [(0, 4), (4, 1), (0, 5), (5, 1)]
uc = unit_counts(6, rep, e, f)
assert uc == (300, 114, 114, 42)
assert gap(uc) == 396
l0 = (2**2 - 1) ** 2
assert Fraction(gap(uc), l0**2) == gap(wc)

print("weighted_base", wc, "gap", gap(wc))
print("replacement", uc, "gap", gap(uc), "scale", l0**2)
print("THETA_WEIGHT_TRANSFER_PASS")
