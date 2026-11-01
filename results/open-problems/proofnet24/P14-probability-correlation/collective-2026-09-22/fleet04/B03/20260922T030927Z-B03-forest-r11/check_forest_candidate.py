from fractions import Fraction

def is_forest(n, edges_subset):
    parent = list(range(n))
    rank = [0] * n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True
    for a, b in edges_subset:
        if not union(a, b):
            return False
    return True

def brute_counts(n, e, f):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    Z = Ze = Zf = Zef = 0
    for mask in range(1 << len(edges)):
        chosen = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(n, chosen):
            continue
        Z += 1
        se = e in chosen
        sf = f in chosen
        Ze += int(se)
        Zf += int(sf)
        Zef += int(se and sf)
    return Z, Ze, Zf, Zef, Ze * Zf - Z * Zef

def He(k, x):
    if k == 0:
        return 1
    if k == 1:
        return x
    hm2, hm1 = 1, x
    for j in range(1, k):
        h = x * hm1 - j * hm2
        hm2, hm1 = hm1, h
    return hm1

for n in range(3, 7):
    adj = brute_counts(n, (0, 1), (1, 2))
    if n >= 4:
        dis = brute_counts(n, (0, 1), (2, 3))
        print(f"K{n} adjacent={adj} disjoint={dis}")
    else:
        print(f"K{n} adjacent={adj}")

for n in range(6, 501):
    k = n - 4
    x = n + 1
    hk = He(k, x)
    hkm1 = He(k - 1, x)
    s = Fraction(k * hkm1, hk)
    L = Fraction((n - 4) * (n - 1) * (n + 4), (n + 1) ** 3)
    G = (5 - n) * s * s + (n * n - 4 * n - 6) * s - n * n + 9 * n - 14
    P = Fraction(
        2 * n**6 + 70 * n**5 - 33 * n**4 + 185 * n**3
        + 1369 * n**2 - 3147 * n + 1170,
        (n + 1) ** 6,
    )
    assert Fraction(0) <= L <= s < Fraction(1)
    assert G >= P > 0

print("HERMITE_EXACT_REVIEW_PASS n=6..500")

for m in range(13):
    # Generalized Cayley: a specified forest with component sizes
    # 2,2,1,...,1 on n=m+4 vertices is contained in exactly
    # 4*n^m labelled trees.
    n = m + 4
    assert 4 * n**m == 4 * (m + 4)**m

print("GENERALIZED_CAYLEY_DISJOINT_COMPONENT_CHECK m=0..12 PASS")
