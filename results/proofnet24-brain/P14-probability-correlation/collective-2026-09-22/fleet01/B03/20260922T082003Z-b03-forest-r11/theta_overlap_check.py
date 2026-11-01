from fractions import Fraction


def is_forest(n, edges, mask):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for i, (u, v) in enumerate(edges):
        if not (mask >> i) & 1:
            continue
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        p[rv] = ru
    return True


def gap(n, edges, e, f):
    Z = Ze = Zf = Zef = 0
    for mask in range(1 << len(edges)):
        if not is_forest(n, edges, mask):
            continue
        Z += 1
        ie = (mask >> e) & 1
        jf = (mask >> f) & 1
        Ze += ie
        Zf += jf
        Zef += ie * jf
    return Z, Ze, Zf, Zef, Ze * Zf - Z * Zef


def theta(lengths):
    edges = []
    paths = []
    nxt = 2
    for a in lengths:
        vs = [0]
        for _ in range(a - 1):
            vs.append(nxt)
            nxt += 1
        vs.append(1)
        path = []
        for x, y in zip(vs, vs[1:]):
            path.append(len(edges))
            edges.append((x, y))
        paths.append(path)
    return nxt, edges, paths


def theta_gap_formula(lengths, i, j):
    ds = [2**a - 1 for a in lengths]
    D = 1
    for d in ds:
        D *= d
    if i != j:
        return Fraction(
            D * D * (ds[i] + 1) * (ds[j] + 1),
            4 * ds[i] ** 2 * ds[j] ** 2,
        )
    T = sum(Fraction(1, ds[k]) for k in range(len(ds)) if k != i)
    return Fraction(D * D * (ds[i] + 1), 4 * ds[i] ** 2) * T * (1 + T)


cases = [
    ([2, 2], 0, 1),
    ([2, 3], 0, 1),
    ([3, 4, 2], 0, 1),
    ([2, 2, 3, 4], 0, 1),
    ([1, 3, 4], 0, 1),
]
for lengths, i, j in cases:
    n, edges, paths = theta(lengths)
    got = gap(n, edges, paths[i][0], paths[j][-1])[-1]
    want = theta_gap_formula(lengths, i, j)
    assert got == want, (lengths, "different", got, want)

same_cases = [
    ([2, 2], 0),
    ([2, 3], 0),
    ([3, 4, 2], 0),
    ([2, 2, 3, 4], 0),
    ([1, 3, 4], 1),
]
for lengths, i in same_cases:
    n, edges, paths = theta(lengths)
    got = gap(n, edges, paths[i][0], paths[i][1])[-1]
    want = theta_gap_formula(lengths, i, i)
    assert got == want, (lengths, "same", got, want)


def three_terminal_partition(n, edges, a=0, b=1, c=2):
    out = [0, 0, 0, 0, 0]  # A,B,C,D,E
    for mask in range(1 << len(edges)):
        p = list(range(n))

        def find(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x

        ok = True
        for i, (u, v) in enumerate(edges):
            if not (mask >> i) & 1:
                continue
            ru, rv = find(u), find(v)
            if ru == rv:
                ok = False
                break
            p[rv] = ru
        if not ok:
            continue
        aa, bb, cc = find(a), find(b), find(c)
        if aa == bb == cc:
            out[0] += 1
        elif aa == bb:
            out[1] += 1
        elif aa == cc:
            out[2] += 1
        elif bb == cc:
            out[3] += 1
        else:
            out[4] += 1
    return tuple(out)


# A five-vertex exact witness showing that the stronger shortcut
# AE <= (B+D)(C+D) is false even though the actual FOREST comparison holds.
witness_edges = [(0, 3), (0, 4), (1, 3), (2, 3), (3, 4)]
A, B, C, D, E = three_terminal_partition(5, witness_edges)
assert (A, B, C, D, E) == (4, 4, 4, 3, 13)
assert A * E > (B + D) * (C + D)
assert A * E <= B * C + D * (B + C + D + E)

print("THETA_FORMULAS=PASS")
print("ADJACENT_PARTITION_WITNESS", (A, B, C, D, E))
print("STRONGER_AE_LE_BD_CD=REFUTED")
print("TARGET_ADJACENT_COMPARISON=PASS_ON_WITNESS")
