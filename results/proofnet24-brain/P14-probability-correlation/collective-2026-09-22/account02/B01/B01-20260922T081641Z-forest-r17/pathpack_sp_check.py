from fractions import Fraction

EDGES = [(0,2),(0,3),(1,2),(1,3),(2,3)]

def forest_conn(mask):
    parent = list(range(4))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a,b):
        a,b = find(a),find(b)
        if a == b:
            return False
        parent[b] = a
        return True
    for i,(a,b) in enumerate(EDGES):
        if (mask >> i) & 1:
            if not union(a,b):
                return False, False
    return True, find(0) == find(1)

forests = []
D = C = 0
for mask in range(1 << len(EDGES)):
    ok, conn = forest_conn(mask)
    if ok:
        forests.append(mask)
        if conn:
            C += 1
        else:
            D += 1

assert (D,C) == (14,10)
lam = Fraction(C,D)
assert lam == Fraction(5,7)

adj = {i: [] for i in range(4)}
for ei,(a,b) in enumerate(EDGES):
    adj[a].append((b,ei))
    adj[b].append((a,ei))

paths = []
def dfs(v, seen, eis):
    if v == 1:
        paths.append(tuple(eis))
        return
    for w,ei in adj[v]:
        if w not in seen:
            dfs(w, seen | {w}, eis + [ei])
dfs(0,{0},[])

N = {}
for P in paths:
    pmask = sum(1 << i for i in P)
    N[P] = sum(1 for m in forests if (m & pmask) == pmask)

assert sum(N.values()) == C
loads = {i: sum(N[P] for P in paths if i in P) for i in range(len(EDGES))}
assert all(v <= D for v in loads.values())
assert all((2**len(P)-1)*N[P] <= D for P in paths)

kappa = min(
    sum(1 for a,b in EDGES if ((a in S) != (b in S)))
    for S in ({0}, {0,2}, {0,3})
)
assert kappa == 2
assert lam <= kappa

vals = {1: {Fraction(1): "e"}}
target = Fraction(5,7)
first = None
for n in range(2,7):
    cur = {}
    for i in range(1,n):
        j = n-i
        for a,ea in vals[i].items():
            for b,eb in vals[j].items():
                par = a+b
                ser = a*b/(1+a+b)
                cur.setdefault(par, f"P({ea},{eb})")
                cur.setdefault(ser, f"S({ea},{eb})")
    vals[n] = cur
    if target in cur and first is None:
        first = n
assert first == 6
explicit = Fraction(1)*Fraction(5)/(1+Fraction(1)+Fraction(5))
assert explicit == target

print(f"K4_MINUS_UV D={D} C={C} RESPONSE={lam}")
print("PATH_COUNTS=" + ",".join(f"{P}:{N[P]}" for P in sorted(paths)))
print("EDGE_LOADS=" + ",".join(f"{i}:{loads[i]}" for i in sorted(loads)))
print(f"MINCUT={kappa}")
print(f"SP_MIN_COST={first}")
print(f"EXPLICIT_SERIES_EDGE_WITH_5_PARALLEL={explicit}")
print("STATUS=PASS")
