from fractions import Fraction

def is_forest(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return True

def counts_and_cov(n, edges, i, j):
    Z = Ze = Zf = Zef = 0
    for mask in range(1 << len(edges)):
        if not is_forest(n, edges, mask):
            continue
        Z += 1
        a = (mask >> i) & 1
        b = (mask >> j) & 1
        Ze += a
        Zf += b
        Zef += a * b
    cov = Fraction(Zef, Z) - Fraction(Ze, Z) * Fraction(Zf, Z)
    gap = Ze * Zf - Z * Zef
    return Z, Ze, Zf, Zef, gap, cov

def theta3_expand(n, edges):
    expanded = []
    distinguished = []
    nv = n
    for u, v in edges:
        distinguished.append(len(expanded))
        for _ in range(3):
            w = nv
            nv += 1
            expanded.append((u, w))
            expanded.append((w, v))
    return nv, expanded, distinguished

cases = [
    ("triangle", 3, [(0,1), (1,2), (0,2)], 0, 1),
    ("triple_parallel", 2, [(0,1), (0,1), (0,1)], 0, 1),
]

for name, n, edges, e, f in cases:
    base = counts_and_cov(n, edges, e, f)
    nn, ee, d = theta3_expand(n, edges)
    lift = counts_and_cov(nn, ee, d[e], d[f])
    ratio = lift[5] / base[5]
    print(
        f"{name}: "
        f"base=(Z={base[0]},Ze={base[1]},Zf={base[2]},Zef={base[3]},gap={base[4]},cov={base[5]}); "
        f"theta3=(Z={lift[0]},Ze={lift[1]},Zf={lift[2]},Zef={lift[3]},gap={lift[4]},cov={lift[5]}); "
        f"cov_ratio={ratio}"
    )
    assert ratio == Fraction(4,81)

# Two-side, two-cut-edge C4 example. Side forest counts are
# Z_L=Z_R=2 and connected counts C_L=C_R=1, so N B = 4.
c4_edges = [(0,1), (2,3), (0,2), (1,3)]
c4 = counts_and_cov(4, c4_edges, 2, 3)
print(
    f"two_cut_C4: Z={c4[0]},Ze={c4[1]},Zf={c4[2]},Zef={c4[3]},"
    f"gap={c4[4]},expected_gap=4"
)
assert c4[4] == 4

print("THETA3_AND_CUT2_REGRESSION_PASS")
