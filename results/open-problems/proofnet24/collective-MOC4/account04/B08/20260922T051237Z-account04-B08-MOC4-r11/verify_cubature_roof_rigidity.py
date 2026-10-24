from itertools import permutations, combinations
from fractions import Fraction

G = list(permutations(range(4)))
e = (0, 1, 2, 3)


def comp(g, h):
    return tuple(g[h[i]] for i in range(4))


def generated(gens):
    H = {e}
    changed = True
    while changed:
        changed = False
        for a in list(H):
            for b in list(H) + list(gens):
                for c in (comp(a, b), comp(b, a)):
                    if c not in H:
                        H.add(c)
                        changed = True
    return frozenset(H)


def t(i, j):
    p = list(e)
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def cyc4(a, b, c, d):
    p = list(e)
    p[a] = b
    p[b] = c
    p[c] = d
    p[d] = a
    return tuple(p)


def left_cosets(H):
    unused = set(G)
    out = []
    while unused:
        x = next(iter(unused))
        C = frozenset(comp(h, x) for h in H)
        out.append(C)
        unused -= C
    return out


def right_cosets(H):
    unused = set(G)
    out = []
    while unused:
        x = next(iter(unused))
        C = frozenset(comp(x, h) for h in H)
        out.append(C)
        unused -= C
    return out


def orbit_partition(items, act):
    unused = set(items)
    out = []
    while unused:
        x = min(unused)
        O = set(act(x))
        out.append(tuple(sorted(O)))
        unused -= O
    return tuple(sorted(out, key=lambda z: (len(z), z)))


H1 = generated([t(0, 3), t(1, 2)])
H2 = generated([t(0, 1), cyc4(0, 2, 1, 3)])
H3 = generated([t(1, 2), t(1, 3)])
H4 = generated([t(0, 1), t(2, 3)])
H5 = generated([t(0, 2)])
H6 = generated([t(0, 3), cyc4(0, 1, 3, 2)])
H7 = generated([t(0, 1), t(0, 3)])
Hs = [H1, H2, H3, H4, H5, H6, H7]
assert [len(H) for H in Hs] == [4, 8, 6, 4, 2, 8, 6]

point_parts = []
for H in Hs:
    part = orbit_partition(range(4), lambda i, H=H: {h[i] for h in H})
    point_parts.append(part)

expected_point_sizes = [(2, 2), (4,), (1, 3), (2, 2), (1, 1, 2), (4,), (1, 3)]
assert [tuple(sorted(map(len, p))) for p in point_parts] == expected_point_sizes

subs = list(combinations(range(4), 2))
pair_parts = {}
for idx in (1, 5):
    H = Hs[idx]
    part = orbit_partition(
        subs,
        lambda I, H=H: {tuple(sorted(h[i] for i in I)) for h in H},
    )
    pair_parts[idx] = part
    assert tuple(sorted(map(len, part))) == (2, 4)


def marginal_1(C):
    return [
        [Fraction(sum(1 for g in C if g[i] == j), len(C)) for j in range(4)]
        for i in range(4)
    ]


def marginal_2(C):
    return {
        (I, J): Fraction(
            sum(1 for g in C if tuple(sorted(g[i] for i in I)) == J), len(C)
        )
        for I in subs
        for J in subs
    }


def bipartite_component_row_sizes(P):
    rows = range(len(P))
    cols = range(len(P[0]))
    unvisited = {("r", i) for i in rows} | {("c", j) for j in cols}
    sizes = []
    while unvisited:
        seed = next(iter(unvisited))
        stack = [seed]
        component = set()
        while stack:
            v = stack.pop()
            if v in component:
                continue
            component.add(v)
            unvisited.discard(v)
            typ, k = v
            if typ == "r":
                for j in cols:
                    if P[k][j] > 0 and ("c", j) not in component:
                        stack.append(("c", j))
            else:
                for i in rows:
                    if P[i][k] > 0 and ("r", i) not in component:
                        stack.append(("r", i))
        rcount = sum(1 for typ, _ in component if typ == "r")
        if rcount:
            sizes.append(rcount)
    return tuple(sorted(sizes))


# For nontransitive point actions every left/right coset has exactly the same
# block-size pattern in its singleton marginal. These are the zero patterns
# used in the proof to force a coordinate block of U from nonnegative averages.
for H, expected in zip(Hs, expected_point_sizes):
    if expected != (4,):
        for C in left_cosets(H) + right_cosets(H):
            assert bipartite_component_row_sizes(marginal_1(C)) == expected

# H2 and H6 are transitive on points, so level one is uninformative. Their
# two-subset marginals nevertheless split exactly into 2+4 components.
for idx in (1, 5):
    H = Hs[idx]
    for C in left_cosets(H) + right_cosets(H):
        R = marginal_2(C)
        matrix = [[R[(I, J)] for J in subs] for I in subs]
        assert bipartite_component_row_sizes(matrix) == (2, 4)


def zmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


# The exact hard spectra used by the lead and assigned partner.
a = [(-4, 4), (0, -1), (-3, 2), (-4, -4)]
b = [(-4, -4), (2, -1), (2, -4), (4, -1)]


def endpoint(sig):
    z = (1, 0)
    for i in range(4):
        z = zmul(z, zadd(a[i], b[sig[i]]))
    return z


Hval = {g: endpoint(g)[0] for g in G}


def roof_and_gap(H, side):
    Cs = left_cosets(H) if side == "left" else right_cosets(H)
    vals = sorted(
        (sum(Fraction(Hval[g]) for g in C) / len(C) for C in Cs),
        reverse=True,
    )
    return vals[0], vals[0] - vals[1]


left = [roof_and_gap(H, "left") for H in Hs]
right = [roof_and_gap(H, "right") for H in Hs]

assert [x[0] for x in left] == [
    Fraction(-47, 2),
    Fraction(-7, 2),
    Fraction(32),
    Fraction(58),
    Fraction(231),
    Fraction(-68),
    Fraction(-134, 3),
]
assert [x[1] for x in left] == [
    Fraction(29, 2),
    Fraction(45, 2),
    Fraction(160, 3),
    Fraction(95, 2),
    Fraction(44),
    Fraction(54),
    Fraction(64, 3),
]
assert [x[0] for x in right] == [
    Fraction(58),
    Fraction(-26),
    Fraction(-104, 3),
    Fraction(21, 2),
    Fraction(248),
    Fraction(-7, 2),
    Fraction(138),
]
assert [x[1] for x in right] == [
    Fraction(96),
    Fraction(42),
    Fraction(10),
    Fraction(3, 2),
    Fraction(78),
    Fraction(132),
    Fraction(200),
]
assert all(gap > 0 for _, gap in left + right)

print("PASS MOC4-CUBATURE-ROOF-RIGIDITY-v1")
print("singleton_orbit_sizes =", [list(x) for x in expected_point_sizes])
print("H2_pair_orbit_sizes =", list(sorted(map(len, pair_parts[1]))))
print("H6_pair_orbit_sizes =", list(sorted(map(len, pair_parts[5]))))
print("hard_left_roof_gaps =", [str(x[1]) for x in left])
print("hard_right_roof_gaps =", [str(x[1]) for x in right])
