from fractions import Fraction
from itertools import combinations


def hermite_values(m, x):
    H = [0] * (m + 1)
    H[0] = 1
    if m >= 1:
        H[1] = x
    for j in range(1, m):
        H[j+1] = x * H[j] - j * H[j-1]
    return H


def kn_counts(n):
    H = hermite_values(n, n + 1)
    def D(j):
        return H[j] if j == 0 else H[j] - j * H[j-1]
    return {"Z": D(n), "E": D(n-2) if n >= 2 else 0,
            "Jadj": D(n-3) if n >= 3 else None,
            "Jdis": D(n-4) + 4 * H[n-4] if n >= 4 else None, "H": H}


def is_forest(n, edge_ids, edges):
    parent = list(range(n)); rank = [0] * n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for idx in edge_ids:
        a, b = edges[idx]; ra, rb = find(a), find(b)
        if ra == rb: return False
        if rank[ra] < rank[rb]: ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]: rank[ra] += 1
    return True


def brute_kn(n):
    edges = list(combinations(range(n), 2)); e = edges[0]
    adj = next((f for f in edges[1:] if len(set(e) & set(f)) == 1), None)
    dis = next((f for f in edges[1:] if len(set(e) & set(f)) == 0), None)
    Z = E = Ja = Jd = 0; ie = edges.index(e)
    ia = edges.index(adj) if adj is not None else None; idd = edges.index(dis) if dis is not None else None
    for mask in range(1 << len(edges)):
        ids = [i for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(n, ids, edges): continue
        Z += 1; he = (mask >> ie) & 1; E += he
        if ia is not None: Ja += he * ((mask >> ia) & 1)
        if idd is not None: Jd += he * ((mask >> idd) & 1)
    return Z, E, Ja, Jd


def clique_theta_graph(m, r):
    edges, blocks = [], []; nxt = 2
    for _ in range(r):
        priv = list(range(nxt, nxt + m - 2)); nxt += m - 2; verts = [0, 1] + priv; bedges = []
        for a, b in combinations(verts, 2):
            if {a, b} == {0, 1}: continue
            e = (min(a, b), max(a, b)); edges.append(e); bedges.append(e)
        blocks.append(bedges)
    return nxt, edges, blocks


def edge_type(e): return "adj" if (0 in e or 1 in e) else "dis"


def bridge_data(m, typ):
    c = kn_counts(m); Z, E = c["Z"], c["E"]; D = E; C = Z - 2 * E
    d = c["Jadj"] if typ == "adj" else c["Jdis"]; cc = E - 2 * d
    return Z, E, C, D, cc, d


def theta_formula_cross(m, r, typ_e, typ_f):
    Zm, E, C, D, ce, de = bridge_data(m, typ_e); _, _, _, _, cf, df = bridge_data(m, typ_f)
    Z = D**r + r * C * D**(r-1)
    Ze = de * (D**(r-1) + (r-1) * C * D**(r-2)) + ce * D**(r-1)
    Zf = df * (D**(r-1) + (r-1) * C * D**(r-2)) + cf * D**(r-1)
    if r == 2: Zef = de * df + ce * df + de * cf
    else: Zef = de * df * (D**(r-2) + (r-2) * C * D**(r-3)) + (ce * df + de * cf) * D**(r-2)
    Re = E * E - Zm * de; Rf = E * E - Zm * df; Delta = D**(2*r-4) * Re * Rf
    return Z, Ze, Zf, Zef, Delta, Fraction(C, D)


def brute_graph_counts(n, edges, e, f):
    ie, jf = edges.index(e), edges.index(f); Z = Ze = Zf = Zef = 0
    for mask in range(1 << len(edges)):
        ids = [i for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(n, ids, edges): continue
        Z += 1; he = (mask >> ie) & 1; hf = (mask >> jf) & 1; Ze += he; Zf += hf; Zef += he * hf
    return Z, Ze, Zf, Zef


def weighted_kn_gap(m, e, f, t, g=(0, 1)):
    edges = list(combinations(range(m), 2)); ie, jf, ig = edges.index(e), edges.index(f), edges.index(g)
    coeff = [[0, 0] for _ in range(4)]
    for mask in range(1 << len(edges)):
        ids = [i for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(m, ids, edges): continue
        gg = (mask >> ig) & 1; he = (mask >> ie) & 1; hf = (mask >> jf) & 1
        for q, val in enumerate((1, he, hf, he * hf)): coeff[q][gg] += val
    def ev(q): return Fraction(coeff[q][0]) + t * coeff[q][1]
    return ev(1) * ev(2) - ev(0) * ev(3)


for n in range(3, 7):
    b = brute_kn(n); c = kn_counts(n); f = (c["Z"], c["E"], c["Jadj"], c["Jdis"] or 0); assert b == f
print("BRUTE_KN_FORMULAS_PASS n=3..6")

for n in range(6, 2001):
    k, x = n - 4, n + 1; H = hermite_values(k, x); s = Fraction(k * H[k-1], H[k]); J = Fraction(k * x, x*x - (k-1))
    assert 0 < s < 1 and s >= J
    def G(q): return (5-n)*q*q + (n*n - 4*n - 6)*q - n*n + 9*n - 14
    rhs = Fraction(3*n**4 + 40*n**3 - 59*n**2 + 488*n - 280, (n*n + n + 6)**2)
    assert G(J) == rhs and G(J) > 0 and G(s) > 0
print("HERMITE_JENSEN_SIGN_PASS n=6..2000")

for m, r in [(3, 2), (4, 2), (4, 3), (5, 2)]:
    n, edges, blocks = clique_theta_graph(m, r); e = blocks[0][0]; f = next((q for q in blocks[1] if edge_type(q) == "dis"), blocks[1][0])
    brute = brute_graph_counts(n, edges, e, f); formula = theta_formula_cross(m, r, edge_type(e), edge_type(f)); assert brute == formula[:4]
    assert brute[1] * brute[2] - brute[0] * brute[3] == formula[4]
    print("THETA_CROSS_PASS", "m=", m, "r=", r, "N=", n, "M=", len(edges), "types=", edge_type(e), edge_type(f), "rho=", formula[5], "Delta=", formula[4])

for m, r in [(4, 2), (4, 3), (5, 2)]:
    n, edges, blocks = clique_theta_graph(m, r); e, f = blocks[0][0], blocks[0][1]
    brute = brute_graph_counts(n, edges, e, f); Delta = brute[1] * brute[2] - brute[0] * brute[3]; c = kn_counts(m)
    D, C = c["E"], c["Z"] - 2*c["E"]; lam = Fraction((r-1) * C, D); local = weighted_kn_gap(m, e, f, lam)
    assert Delta == D**(2*r-2) * local
    print("THETA_SAME_PASS", "m=", m, "r=", r, "lambda=", lam, "Delta=", Delta)

for m in (4, 5, 6, 10, 20, 50):
    c = kn_counts(m); rho = Fraction(c["Z"] - 2*c["E"], c["E"]); print("RHO", m, rho, float(rho))
print("ALL_CHECKS_PASS")
