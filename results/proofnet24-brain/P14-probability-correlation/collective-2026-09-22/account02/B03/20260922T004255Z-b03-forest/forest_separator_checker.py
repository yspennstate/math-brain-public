from fractions import Fraction
from itertools import combinations

def forest(vertices, edges):
    parent = {v:v for v in vertices}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u,v in edges:
        ru,rv = find(u),find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True

def conn(vertices, edges, s, t):
    parent = {v:v for v in vertices}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u,v in edges:
        ru,rv = find(u),find(v)
        if ru != rv:
            parent[ru] = rv
    return find(s) == find(t)

def all_forests(vertices, edges):
    edges = list(edges)
    ans = []
    for mask in range(1 << len(edges)):
        h = frozenset(edges[i] for i in range(len(edges)) if (mask >> i) & 1)
        if forest(vertices, h):
            ans.append(h)
    return ans

def side_counts(vertices, edges, mark, s, t):
    d = [0,0]
    c = [0,0]
    for h in all_forests(vertices, edges):
        i = int(mark in h)
        (c if conn(vertices,h,s,t) else d)[i] += 1
    return d,c

def cells(vertices, edges, e, f):
    m = [[0,0],[0,0]]
    for h in all_forests(vertices, edges):
        m[int(e in h)][int(f in h)] += 1
    return m

def weighted_cells(vertices, edges, e, f, weight):
    m = [[Fraction(0),Fraction(0)],[Fraction(0),Fraction(0)]]
    for h in all_forests(vertices, edges):
        w = Fraction(1)
        for x in h:
            w *= weight.get(x, Fraction(1))
        m[int(e in h)][int(f in h)] += w
    return m

def rayleigh(m):
    return m[1][0]*m[0][1] - m[0][0]*m[1][1]

# Diamond: two triangles/path channels share the separator {s,t}.
V = {0,1,2,3}
st = (0,1)
e = (0,2)
at = (1,2)
f = (0,3)
bt = (1,3)
A = {st,e,at}
B = {f,bt}
G = A | B

m = cells(V,G,e,f)
dA,cA = side_counts({0,1,2},A,e,0,1)
dB,cB = side_counts({0,1,3},B,f,0,1)
deltaA = dA[0]*cA[1]-dA[1]*cA[0]
deltaB = dB[0]*cB[1]-dB[1]*cB[0]
assert rayleigh(m) == deltaA*deltaB == 4

# Account01/B03 overlap-reconnection coordinates for the same marked pair.
K = G-{e,f}
nij = [[0,0],[0,0]]
q = 0
for h in all_forests(V,K):
    xe = forest(V, list(h)+[e])
    yf = forest(V, list(h)+[f])
    nij[int(xe)][int(yf)] += 1
    if xe and yf and not forest(V,list(h)+[e,f]):
        q += 1
N = sum(sum(row) for row in nij)
assert (N,nij,q) == (8,[[1,1],[1,5]],1)
assert nij[1][0]*nij[0][1]-nij[0][0]*nij[1][1]+N*q == 4

# Same-side marks.  The B path has D=3,C=1, hence lambda=C/D=1/3.
same = cells(V,G,e,at)
FB = all_forests({0,1,3},B)
D = sum(not conn({0,1,3},h,0,1) for h in FB)
C = len(FB)-D
lam = Fraction(C,D)
assert (D,C,lam) == (3,1,Fraction(1,3))
weighted = weighted_cells({0,1,2},A,e,at,{st:1+lam})
assert rayleigh(same) == D*D*rayleigh(weighted) == 28
unit_scaled = D*D*rayleigh(weighted_cells({0,1,2},A,e,at,{st:Fraction(1)}))
assert unit_scaled == 18

# Contracting e in a triangle produces two parallel copies, not one unit edge.
triangle = {st,e,at}
contain_e = sum(e in h for h in all_forests({0,1,2},triangle))
parallel_contraction_forests = 3 # empty, first copy, second copy
unit_simple_collapse_forests = 2 # empty, one merged unit edge
assert (contain_e,parallel_contraction_forests,unit_simple_collapse_forests) == (3,3,2)

# Exhaustive cross-separator factorization for all edge-disjoint sides
# with one private vertex per side; boundary edge, when present, is owned by A.
potA = [(0,1),(0,2),(1,2)]
potB = [(0,3),(1,3)]
cross_cases = 0
cross_fail = 0
for ma in range(1 << len(potA)):
    AA = {potA[i] for i in range(len(potA)) if (ma >> i) & 1}
    for mb in range(1 << len(potB)):
        BB = {potB[i] for i in range(len(potB)) if (mb >> i) & 1}
        for ee in AA:
            for ff in BB:
                cross_cases += 1
                da,ca = side_counts({0,1,2},AA,ee,0,1)
                db,cb = side_counts({0,1,3},BB,ff,0,1)
                lhs = rayleigh(cells(V,AA|BB,ee,ff))
                rhs = (da[0]*ca[1]-da[1]*ca[0])*(db[0]*cb[1]-db[1]*cb[0])
                if lhs != rhs:
                    cross_fail += 1
assert cross_fail == 0

# Exhaustive same-side weighted compression in the same tiny separator universe.
same_cases = 0
same_fail = 0
for ma in range(1 << len(potA)):
    AA = {potA[i] for i in range(len(potA)) if (ma >> i) & 1}
    ordinary = [x for x in AA if x != st]
    if len(ordinary) < 2:
        continue
    for ee,ff in combinations(ordinary,2):
        for mb in range(1 << len(potB)):
            BB = {potB[i] for i in range(len(potB)) if (mb >> i) & 1}
            FB = all_forests({0,1,3},BB)
            DD = sum(not conn({0,1,3},h,0,1) for h in FB)
            CC = len(FB)-DD
            ll = Fraction(CC,DD)
            lhs = rayleigh(cells(V,AA|BB,ee,ff))
            if st in AA:
                rhs_cells = weighted_cells({0,1,2},AA,ee,ff,{st:1+ll})
            else:
                rhs_cells = weighted_cells({0,1,2},AA|{st},ee,ff,{st:ll})
            rhs = DD*DD*rayleigh(rhs_cells)
            same_cases += 1
            if lhs != rhs:
                same_fail += 1
assert same_fail == 0

# k internally-disjoint two-edge channels in parallel:
# each path has response 1/3, so lambda=k/3.  With the triangle A above,
# the original st edge acquires total weight 1+k/3.
theta_rows = []
for k in range(1,6):
    Db = 3**k
    Cb = k*3**(k-1)
    ll = Fraction(Cb,Db)
    w = 1+ll
    # triangle Rayleigh for the two non-boundary edges is w(1+w)
    RG = Db*Db*w*(1+w)
    formula = 9**(k-1)*(k+3)*(k+6)
    assert ll == Fraction(k,3)
    assert RG == formula
    theta_rows.append((k,ll,RG))

print("diamond cross cells", m, "R", rayleigh(m), "side deltas", deltaA, deltaB)
print("diamond overlap reduction N,nij,q", N, nij, q)
print("naive side-product", len(all_forests({0,1,2},A))*len(all_forests({0,1,3},B)),
      "minus incompatible both-connected", 4, "=", len(all_forests(V,G)))
print("same-side diamond: D,C,lambda", D,C,lam,
      "global R", rayleigh(same), "weighted-side R", rayleigh(weighted),
      "D^2*R", D*D*rayleigh(weighted))
print("unit-weight collapse would give", unit_scaled, "instead of", rayleigh(same))
print("triangle contraction: exact containing count", contain_e,
      "parallel contraction forests", parallel_contraction_forests,
      "unit-simple collapse", unit_simple_collapse_forests)
print("exhaustive cross-separator cases", cross_cases, "failures", cross_fail)
print("exhaustive same-side weighted-compression cases", same_cases, "failures", same_fail)
print("theta parallel-path responses", theta_rows)
