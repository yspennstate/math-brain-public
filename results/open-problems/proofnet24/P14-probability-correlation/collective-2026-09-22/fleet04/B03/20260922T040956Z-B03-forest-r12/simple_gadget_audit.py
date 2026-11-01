from fractions import Fraction

def is_forest(vertices, edges):
    p = {v: v for v in vertices}
    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        p[b] = a
        return True
    return all(union(u, v) for u, v in edges)

def counts(vertices, edges, eidx, fidx, weights=None):
    m = len(edges)
    if weights is None:
        weights = [Fraction(1) for _ in edges]
    Z = Ze = Zf = Zef = Fraction(0)
    for mask in range(1 << m):
        chosen = [edges[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(vertices, chosen):
            continue
        w = Fraction(1)
        for i in range(m):
            if (mask >> i) & 1:
                w *= weights[i]
        Z += w
        if (mask >> eidx) & 1:
            Ze += w
        if (mask >> fidx) & 1:
            Zf += w
        if ((mask >> eidx) & 1) and ((mask >> fidx) & 1):
            Zef += w
    return (Z, Ze, Zf, Zef, Ze * Zf - Z * Zef)

def expand(vertices, edges, specs):
    V = list(vertices)
    E = []
    literal = {}
    for i, (u, v) in enumerate(edges):
        if i not in specs:
            literal[i] = len(E)
            E.append((u, v))
            continue
        k, a = specs[i]
        assert a >= 2 and k >= 1
        for r in range(k):
            last = u
            for j in range(a - 1):
                w = ("new", i, r, j)
                V.append(w)
                E.append((last, w))
                last = w
            E.append((last, v))
    return V, E, literal

V = [0, 1, 2, 3]
E = [(0,1), (2,3), (0,2), (0,3), (1,2), (1,3)]
eidx, fidx = 0, 1
weights = [
    Fraction(1), Fraction(1), Fraction(2,3),
    Fraction(3,7), Fraction(1), Fraction(1)
]
base = counts(V, E, eidx, fidx, weights)

specs = {2: (2,2), 3: (3,3)}
Vx, Ex, literal = expand(V, E, specs)
expanded = counts(Vx, Ex, literal[eidx], literal[fidx])
C = (2**2 - 1)**2 * (2**3 - 1)**3

print("SIMPLE_GADGET_GLOBALIZATION_AUDIT")
print("base =", base)
print("expanded =", expanded)
print("C =", C)
print("C_times_base_first_four =", tuple(C*x for x in base[:4]))
print("C2_times_base_delta =", C*C*base[4])
print("identity_first_four =", tuple(C*x for x in base[:4]) == expanded[:4])
print("identity_delta =", C*C*base[4] == expanded[4])
print("expanded_vertices =", len(Vx))
print("expanded_edges =", len(Ex))
print("simple_expansion =", len({frozenset(e) for e in Ex}) == len(Ex))
