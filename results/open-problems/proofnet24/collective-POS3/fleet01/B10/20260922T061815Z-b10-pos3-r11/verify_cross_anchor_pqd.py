from itertools import combinations

N = 10
REL = {
    (0,1),
    (0,3),
    (0,4),
    (0,5),
    (0,6),
    (0,7),
    (0,8),
    (0,9),
    (1,5),
    (1,7),
    (1,8),
    (1,9),
    (2,3),
    (2,5),
    (2,6),
    (2,7),
    (2,8),
    (2,9),
    (3,6),
    (3,7),
    (3,9),
    (4,8),
    (4,9),
    (5,8),
    (6,7),
    (6,9),
    (7,9)
}

def transitive_closure(n, rel):
    reach = [[False]*n for _ in range(n)]
    for i,j in rel:
        reach[i][j] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    if reach[k][j]:
                        reach[i][j] = True
    return {(i,j) for i in range(n) for j in range(n) if reach[i][j]}

assert transitive_closure(N, REL) == REL
assert all((j,i) not in REL for i,j in REL)

def width(n, rel):
    ans = 0
    witness = ()
    for r in range(1,n+1):
        for S in combinations(range(n), r):
            if all((x,y) not in rel and (y,x) not in rel for x,y in combinations(S,2)):
                ans = r
                witness = S
    return ans, witness

def count_extensions(n, rel):
    preds = [0]*n
    for i,j in rel:
        preds[j] |= 1<<i
    dp = [0]*(1<<n)
    dp[0] = 1
    for mask in range(1<<n):
        if dp[mask] == 0:
            continue
        for x in range(n):
            if not ((mask>>x)&1) and (preds[x] & ~mask) == 0:
                dp[mask | (1<<x)] += dp[mask]
    return dp[-1]

def add_order(rel, x, y):
    if x == y or (y,x) in rel:
        return None
    return transitive_closure(N, set(rel) | {(x,y)})

def count_event(*orders):
    r = set(REL)
    for x,y in orders:
        r = add_order(r, x, y)
        if r is None:
            return 0
    if any((j,i) in r for i,j in r):
        return 0
    return count_extensions(N, r)

def canonical_sets(a,b):
    assert (a,b) not in REL and (b,a) not in REL
    pred_a = {x for x in range(N) if (x,a) in REL}
    pred_b = {x for x in range(N) if (x,b) in REL}
    assert pred_b <= pred_a
    D = pred_a - pred_b
    T = sorted(x for x in D if not any((x,y) in REL for y in D if y != x))
    S = {z for z in range(N) if (b,z) in REL and (a,z) not in REL and (z,a) not in REL}
    U = sorted(x for x in S if not any((y,x) in REL for y in S if y != x))
    return D,T,S,U

def connected(edges):
    adj=[set() for _ in range(N)]
    for i,j in edges:
        adj[i].add(j); adj[j].add(i)
    seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); stack.append(w)
    return len(seen)==N

E = count_extensions(N, REL)
w, aw = width(N, REL)
assert E == 461
assert w == 3

# Nested endpoint and two cross-anchor reverse channels.
a,b,t,u = 5,4,2,9
D,T,S,U = canonical_sets(a,b)
assert D == {1,2}
assert T == [1,2]
assert S == {9}
assert U == [9]

Np = count_event((a,b))
A1 = count_event((b,1))
A2 = count_event((b,2))
B  = count_event((9,a))
A2B = count_event((b,2),(9,a))
assert (Np,A1,A2,B,A2B) == (136,152,61,39,5)

# Every local reverse channel and the endpoint are below 1/3.
assert 3*Np < E
assert 3*A1 < E and 3*A2 < E and 3*B < E

# But the cross-anchor pair A2={b<t}, B={u<a} is negatively correlated.
defect = A2B*E - A2*B
assert defect == -74

# The witness is still a POS3-positive instance; this only refutes the local
# cross-anchor correlation lemma.
balanced = []
for i,j in combinations(range(N),2):
    if (i,j) in REL or (j,i) in REL:
        continue
    c = count_event((i,j))
    if 3*c >= E and 3*c <= 2*E:
        balanced.append((i,j,c,E-c))
assert balanced

comp_edges={(i,j) for i in range(N) for j in range(i+1,N)
            if (i,j) in REL or (j,i) in REL}
inc_edges={(i,j) for i in range(N) for j in range(i+1,N)
           if (i,j) not in REL and (j,i) not in REL}
assert connected(comp_edges)
assert connected(inc_edges)

print("extensions", E)
print("width", w, "antichain_witness", aw)
print("nested_endpoint", (a,b), "D", sorted(D), "T", T, "S", sorted(S), "U", U)
print("counts", "Pnum(a<b)", Np, "A1", A1, "A2", A2, "B", B, "A2_and_B", A2B)
print("third_tests", 3*Np, 3*A1, 3*A2, 3*B, "<", E)
print("cross_anchor_covariance_numerator", defect)
print("connected_comparability", connected(comp_edges))
print("connected_incomparability", connected(inc_edges))
print("balanced_examples", balanced[:3])
print("POS3_CROSS_ANCHOR_PQD_COUNTEREXAMPLE_PASS")
