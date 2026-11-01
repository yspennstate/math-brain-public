from itertools import combinations
from fractions import Fraction

def forest_data(n, edges, marked=(), terminals=None):
    """Enumerate all forests. Return counts by marked inclusion and optional terminal connectivity."""
    out = {}
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
            if (mask >> i) & 1:
                ru, rv = find(u), find(v)
                if ru == rv:
                    ok = False
                    break
                parent[ru] = rv
        if not ok:
            continue
        mark_bits = tuple(bool((mask >> i) & 1) for i in marked)
        conn = None if terminals is None else (find(terminals[0]) == find(terminals[1]))
        out[(mark_bits, conn)] = out.get((mark_bits, conn), 0) + 1
    return out

def affine_counts(n, edges, e_idx, f_idx, uv):
    d = forest_data(n, edges, (e_idx, f_idx), uv)
    # coefficient 0 = total forests in H; coefficient 1 = H-forests where u,v disconnected,
    # because those are exactly the forests to which a virtual edge uv may be added.
    vals = {name: [0, 0] for name in ("Z", "e", "f", "ef")}
    for (bits, conn), c in d.items():
        pe, pf = bits
        vals["Z"][0] += c
        if pe: vals["e"][0] += c
        if pf: vals["f"][0] += c
        if pe and pf: vals["ef"][0] += c
        if not conn:
            vals["Z"][1] += c
            if pe: vals["e"][1] += c
            if pf: vals["f"][1] += c
            if pe and pf: vals["ef"][1] += c
    return vals

def gap_coeff(vals):
    A, B = vals["Z"]
    a0, a1 = vals["e"]
    b0, b1 = vals["f"]
    c0, c1 = vals["ef"]
    D0 = a0*b0 - A*c0
    M = a0*b1 + a1*b0 - A*c1 - B*c0
    D1 = a1*b1 - B*c1
    return D0, M, D1

def all_positive(D0, M, D1):
    if D0 < 0 or D1 < 0:
        return False
    if D1 == 0:
        return M >= 0
    if M >= 0:
        return True
    return M*M <= 4*D0*D1

def theta_edges(k, m, u=0, v=1, next_vertex=2):
    edges = []
    z = next_vertex
    for _ in range(k):
        path = [u] + list(range(z, z+m-1)) + [v]
        z += m-1
        edges.extend(zip(path, path[1:]))
    return edges, z

# 1. Exhaustive virtual-edge envelope scan on every labelled simple core on <=5 vertices.
stats = {"cores": 0, "instances": 0, "negative_M": 0, "weighted_failures": 0}
max_rho = (Fraction(-1), None)
for n in range(2, 6):
    all_edges = list(combinations(range(n), 2))
    for graph_mask in range(1 << len(all_edges)):
        H = [all_edges[i] for i in range(len(all_edges)) if (graph_mask >> i) & 1]
        if len(H) < 2:
            continue
        nonedges = [g for g in all_edges if g not in H]
        if not nonedges:
            continue
        stats["cores"] += 1
        for uv in nonedges:
            for ei, fi in combinations(range(len(H)), 2):
                stats["instances"] += 1
                vals = affine_counts(n, H, ei, fi, uv)
                D0, M, D1 = gap_coeff(vals)
                if M < 0:
                    stats["negative_M"] += 1
                    if D0 > 0 and D1 > 0:
                        rho = Fraction(M*M, 4*D0*D1)
                        if rho > max_rho[0]:
                            max_rho = (rho, (n, H, uv, ei, fi, (D0, M, D1), vals))
                if not all_positive(D0, M, D1):
                    stats["weighted_failures"] += 1

print("EXHAUSTIVE_CORES", stats)
print("MAX_NEGATIVE_M_DISCRIMINANT_RATIO", max_rho[0])
n, H, uv, ei, fi, coeff, vals = max_rho[1]
print("MAX_RATIO_WITNESS", {
    "n": n, "H_edges": H, "virtual_uv": uv, "e": H[ei], "f": H[fi],
    "Q_coeff": coeff, "affine_counts": vals
})

# 2. Theta response formula. Direct-brute small theta cases.
for k in range(1, 4):
    for m in range(2, 4):
        E, nv = theta_edges(k, m)
        d = forest_data(nv, E, (), (0, 1))
        D = sum(c for (bits, conn), c in d.items() if conn is False)
        C = sum(c for (bits, conn), c in d.items() if conn is True)
        expect_D = (2**m - 1)**k
        expect_C = k * (2**m - 1)**(k-1)
        assert (D, C) == (expect_D, expect_C)
        print("THETA", k, m, "D", D, "C", C, "response", Fraction(C,D))

# 3. Exact gluing factorization on an overlapping-cycle / induced-parallel witness.
# Core H = K5 minus {12,34}; virtual terminals uv=12; marks e=13, f=24.
n0 = 5
H = [(0,1),(0,2),(0,3),(0,4),(1,3),(1,4),(2,3),(2,4)]
uv = (1,2)
e_idx = H.index((1,3))
f_idx = H.index((2,4))
vals = affine_counts(n0, H, e_idx, f_idx, uv)
D0, M, D1 = gap_coeff(vals)
assert (D0, M, D1) == (158, -14, 4)
print("CORE_Q", f"{D0} + ({M}) w + {D1} w^2")

# Glue Theta_{4,2} between terminals 1 and 2 using four fresh internal vertices.
theta = [(1,5),(5,2),(1,6),(6,2),(1,7),(7,2),(1,8),(8,2)]
G = H + theta
dataG = forest_data(9, G, (e_idx, f_idx), None)
Z = sum(dataG.values())
Ze = sum(c for (bits, conn), c in dataG.items() if bits[0])
Zf = sum(c for (bits, conn), c in dataG.items() if bits[1])
Zef = sum(c for (bits, conn), c in dataG.items() if bits[0] and bits[1])
Delta = Ze*Zf - Z*Zef
d = 2**2 - 1
N0 = d**4
w = Fraction(4, d)
Qw = Fraction(D0) + M*w + D1*w*w
rhs = N0*N0*Qw
assert Delta == rhs == 960822
print("GLUE_THETA_4_2", {"N0":N0, "response":str(w), "Q(response)":str(Qw),
                            "Delta_source_graph":Delta, "factorized":str(rhs)})

# 4. Repeated contractions of Theta_{k,m} can create an arbitrarily large parallel class.
# For Theta_{4,2}, contracting edges (1,5),(1,6),(1,7),(1,8) leaves four parallel 1--2 edges.
print("PARALLEL_CLASS_AFTER_CONTRACTIONS", 4)
print("PARALLEL_CLASS_UNIT_POLYNOMIAL", "1 + y1 + y2 + y3 + y4; aggregate Y=4 at unit weights")
print("STATUS=PASS")
