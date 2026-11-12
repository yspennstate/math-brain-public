"""Exact check of edge negative correlation for weighted random forests on K_n, n=3..7.
Counts forests by size: Z(t)=sum t^|F|, Ne(t), Nf(t), Nef(t) for an incident and a disjoint pair.
D(t) = Nef*Z - Ne*Nf must be <0 for every t>0. Checked by exact real-root isolation (sympy)."""
import itertools, sys
import sympy as sp

def forests_by_size(n):
    edges = list(itertools.combinations(range(n), 2))
    m = len(edges)
    # DFS over edges with union-find, recording counts by size and pair membership
    pairs = {"inc": (edges.index((0, 1)), edges.index((0, 2)))}
    if n >= 4:
        pairs["dis"] = (edges.index((0, 1)), edges.index((2, 3)))
    Z = [0] * n; N = {k: ([0] * n, [0] * n, [0] * n) for k in pairs}
    parent = list(range(n))
    def find(a):
        while parent[a] != a:
            a = parent[a]
        return a
    chosen = []
    def rec(i, size):
        if i == m:
            Z[size] += 1
            s = set(chosen)
            for k, (e, f) in pairs.items():
                ie, iff = e in s, f in s
                if ie: N[k][0][size] += 1
                if iff: N[k][1][size] += 1
                if ie and iff: N[k][2][size] += 1
            return
        rec(i + 1, size)
        a, b = edges[i]
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb; chosen.append(i)
            rec(i + 1, size + 1)
            chosen.pop(); parent[ra] = ra
    rec(0, 0)
    return Z, N

t = sp.symbols("t", positive=True)
ok = True
for n in range(3, int(sys.argv[1]) + 1 if len(sys.argv) > 1 else 8):
    Z, N = forests_by_size(n)
    P = lambda c: sum(ci * t**i for i, ci in enumerate(c))
    assert Z[n - 1] == n ** (n - 2), "Cayley"
    for k, (ne, nf, nef) in N.items():
        D = sp.expand(P(nef) * P(Z) - P(ne) * P(nf))
        poly = sp.Poly(D, t)
        pos = [r for r in sp.real_roots(poly) if r > 0]
        val = D.subs(t, 1)
        good = (not pos) and val < 0
        ok &= good
        print(f"n={n} {k}: deg {poly.degree()}, positive roots {len(pos)}, D(1)={val}, D<0 on t>0: {good}")
print("ALL OK" if ok else "FAIL")
