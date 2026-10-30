import itertools
import sympy as sp

n, s, t = sp.symbols("n s t", integer=True)
J = 5 - s
E = 2*n + 6 - 3*s
Z = n**2 + 3*n + 10 - (n+4)*s
G = sp.expand(E**2 - Z*J)
L = (n-4)*(n-1)*(n+4)/(n+1)**3
P = sp.expand(sp.together(G.subs(s, L)*(n+1)**6))
Pshift = sp.expand(P.subs(n, t+6))

print("G=", G)
print("P=", P)
print("P(n=t+6)=", Pshift)

def is_forest(v, es):
    parent = list(range(v))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True
    return all(union(a,b) for a,b in es)

for v in range(3, 7):
    edges = list(itertools.combinations(range(v), 2))
    forests = []
    for mask in range(1 << len(edges)):
        chosen = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if is_forest(v, chosen):
            forests.append(mask)
    e = edges.index((0,1))
    a = edges.index((0,2))
    d = edges.index((2,3)) if v >= 4 else None
    z = len(forests)
    one = sum((m >> e) & 1 for m in forests)
    adj = sum(bool((m >> e) & 1) and bool((m >> a) & 1) for m in forests)
    dis = None if d is None else sum(bool((m >> e) & 1) and bool((m >> d) & 1) for m in forests)
    gap_adj = one*one - z*adj
    gap_dis = None if dis is None else one*one - z*dis
    print(v, z, one, adj, dis, gap_adj, gap_dis)
