from fractions import Fraction


def forest_data(n, edges, weights, eidx, fidx):
    Z = Ze = Zf = Zef = Fraction(0)
    m = len(edges)
    for mask in range(1 << m):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        ok = True
        for i, (u, v) in enumerate(edges):
            if not (mask >> i) & 1:
                continue
            ru, rv = find(u), find(v)
            if ru == rv:
                ok = False
                break
            parent[rv] = ru
        if not ok:
            continue
        mon = Fraction(1)
        for i, w in enumerate(weights):
            if (mask >> i) & 1 and i not in (eidx, fidx):
                mon *= w
        Z += mon
        if (mask >> eidx) & 1:
            Ze += mon
        if (mask >> fidx) & 1:
            Zf += mon
        if (mask >> eidx) & 1 and (mask >> fidx) & 1:
            Zef += mon
    return Z, Ze, Zf, Zef, Ze * Zf - Z * Zef


base_edges = [(0, 1), (1, 2), (0, 2)]
base_w = [Fraction(1), Fraction(1), Fraction(2, 3)]
base = forest_data(3, base_edges, base_w, 0, 1)
assert base[-1] == Fraction(10, 9)

sub_edges = [(0, 1), (1, 2), (0, 3), (3, 2), (0, 4), (4, 2)]
sub_w = [Fraction(1)] * 6
sub = forest_data(5, sub_edges, sub_w, 0, 1)
D = Fraction(3**2)
assert sub[-1] == D * D * base[-1] == 90

edges = [(0, 2), (2, 3), (3, 1), (0, 4), (4, 1), (0, 1)]
weights = [Fraction(1), Fraction(1), Fraction(1), Fraction(2), Fraction(3), Fraction(5)]
direct = forest_data(5, edges, weights, 0, 1)
H1_edges = [(0, 2), (2, 3), (3, 1), (0, 1)]
H1_w = [Fraction(1), Fraction(1), Fraction(1), Fraction(6)]
h1 = forest_data(4, H1_edges, H1_w, 0, 1)
assert direct[-1] == Fraction(6**2) * h1[-1]

cross = forest_data(5, edges, weights, 0, 3)


def DC_and_derivs(n, edges, weights, mark, u, v):
    D = C = De = Ce = Fraction(0)
    m = len(edges)
    for mask in range(1 << m):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        ok = True
        mon = Fraction(1)
        for i, (a, b) in enumerate(edges):
            if not (mask >> i) & 1:
                continue
            ra, rb = find(a), find(b)
            if ra == rb:
                ok = False
                break
            parent[rb] = ra
            if i != mark:
                mon *= weights[i]
        if not ok:
            continue
        connected = find(u) == find(v)
        if connected:
            C += mon
            if (mask >> mark) & 1:
                Ce += mon
        else:
            D += mon
            if (mask >> mark) & 1:
                De += mon
    return D, C, De, Ce


B1e = [(0, 2), (2, 3), (3, 1)]
B1w = [Fraction(1)] * 3
D1, C1, D1e, C1e = DC_and_derivs(4, B1e, B1w, 0, 0, 1)
R1 = D1 * C1e - C1 * D1e
B2e = [(0, 4), (4, 1)]
B2w = [Fraction(2), Fraction(3)]
D2, C2, D2e, C2e = DC_and_derivs(5, B2e, B2w, 0, 0, 1)
R2 = D2 * C2e - C2 * D2e
assert cross[-1] == R1 * R2

print("theta_weighted_gap", base[-1])
print("theta_unit_gap", sub[-1])
print("theta_scale", D * D)
print("same_bridge_direct_gap", direct[-1])
print("same_bridge_virtual_gap", h1[-1])
print("same_bridge_scale", 36)
print("cross_direct_gap", cross[-1])
print("cross_R1", R1)
print("cross_R2", R2)
print("STATUS=PASS")
