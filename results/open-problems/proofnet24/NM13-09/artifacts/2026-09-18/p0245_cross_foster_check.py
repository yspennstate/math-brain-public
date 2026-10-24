from sympy import symbols, Matrix, expand, factor
from itertools import combinations

a,b,c,d,e,f = symbols("a b c d e f")
edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
vals = [a,b,c,d,e,f]
w = dict(zip(edges, vals))

def W(i,j):
    if i == j:
        return 0
    return w[tuple(sorted((i,j)))]

deg = [sum(W(i,j) for j in range(4) if j != i) for i in range(4)]
L = Matrix([[deg[i] if i==j else -W(i,j) for j in range(4)] for i in range(4)])
tau = expand(L[:3,:3].det())

def forest_poly(i,j):
    ans = 0
    for es in combinations(edges,2):
        parent = list(range(4))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        ok = True
        for u,v in es:
            ru,rv = find(u),find(v)
            if ru == rv:
                ok = False
                break
            parent[rv] = ru
        if not ok or len({find(x) for x in range(4)}) != 2 or find(i) == find(j):
            continue
        wt = 1
        for ed in es:
            wt *= W(*ed)
        ans += wt
    return expand(ans)

F = {(i,j): forest_poly(i,j) for i,j in edges}

def rdel(i):
    v = [x for x in range(4) if x != i]
    x,y,z = v
    return expand(W(x,y)*W(x,z) + W(x,y)*W(y,z) + W(x,z)*W(y,z))

r = [rdel(i) for i in range(4)]

# All-minors identity and exact harmonic orientation-bias identity.
for k,l in edges:
    u,v = [x for x in range(4) if x not in (k,l)]
    p = W(u,v)
    det = expand(deg[u]*deg[v] - p*p)
    assert expand(det - F[(k,l)]) == 0
    ru = W(u,k) - W(u,l)
    rv = W(v,k) - W(v,l)
    gu_num = expand(ru*deg[v] + p*rv)
    gv_num = expand(deg[u]*rv + p*ru)
    # If g=2 P(T_k<T_l)-1 on the two interior vertices, then
    # F_kl * (g_u+g_v)/2 = r_l-r_k.
    assert expand((gu_num + gv_num) - 2*(r[l]-r[k])) == 0

# Cross-Foster identity. For the opposite edge e* of e,
# O = sum_e w_e R_{e*}, and R_ij=F_ij/tau.
O_num = 0
for i,j in edges:
    k,l = [x for x in range(4) if x not in (i,j)]
    O_num += W(i,j)*F[tuple(sorted((k,l)))]

lhs = expand(O_num - 3*tau)
rhs = expand(
    (b+e+c+d)*(a-f)**2
    + (a+f+c+d)*(b-e)**2
    + (a+f+b+e)*(c-d)**2
    - 3*(a-f)*(b-e)*(c-d)
)
assert expand(lhs-rhs) == 0

print("P0245 loopless-4 cross-Foster exact self-check")
print("tau =", factor(tau))
print("all_minors_F_equals_killed_det = PASS (all 6 pairs)")
print("last_pair_harmonic_bias = PASS (all 6 pairs)")
print("cross_Foster_polynomial_identity = PASS")
print("ALL_EXACT_CHECKS_PASS")
