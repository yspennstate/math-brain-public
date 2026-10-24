#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations

N = 9
# Transitive-reduction covers of the adversary.
COVERS = [
    (0,1),(0,5),(1,2),(2,6),(3,4),(3,5),
    (4,6),(4,7),(4,8),(5,8),
]
# Hard-corridor labels.
a,b,d,u1,u2 = 5,4,0,6,7


def closure(n, edges):
    r = [[False]*n for _ in range(n)]
    for x,y in edges:
        r[x][y] = True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]:
                        r[i][j] = True
    assert not any(r[i][i] for i in range(n))
    return r

R = closure(N, COVERS)


def count_extensions(extra=()):
    r = [row[:] for row in R]
    for x,y in extra:
        if x == y or r[y][x]:
            return 0
        r[x][y] = True
    for k in range(N):
        for i in range(N):
            if r[i][k]:
                for j in range(N):
                    if r[k][j]:
                        r[i][j] = True
    if any(r[i][i] for i in range(N)):
        return 0
    pred = []
    for y in range(N):
        m = 0
        for x in range(N):
            if r[x][y]:
                m |= 1 << x
        pred.append(m)

    @lru_cache(None)
    def dp(mask):
        if mask == (1 << N) - 1:
            return 1
        total = 0
        for v in range(N):
            if not ((mask >> v) & 1) and (pred[v] & ~mask) == 0:
                total += dp(mask | (1 << v))
        return total
    return dp(0)


def preds(v):
    return {x for x in range(N) if R[x][v]}


def succs(v):
    return {x for x in range(N) if R[v][x]}


def is_chain(S):
    return all(R[x][y] or R[y][x] for x,y in combinations(S,2))


def width():
    best = []
    for mask in range(1 << N):
        S = [x for x in range(N) if (mask >> x) & 1]
        if len(S) <= len(best):
            continue
        if all(not R[x][y] and not R[y][x] for x,y in combinations(S,2)):
            best = S
    return len(best), best


def connected(kind):
    seen = {0}
    stack = [0]
    while stack:
        x = stack.pop()
        for y in range(N):
            if y == x or y in seen:
                continue
            comparable = R[x][y] or R[y][x]
            edge = comparable if kind == 'comparability' else not comparable
            if edge:
                seen.add(y)
                stack.append(y)
    return len(seen) == N


def rel(x,y):
    if R[x][y]: return -1
    if R[y][x]: return 1
    return 0


def autonomous_sets():
    ans = []
    for mask in range(1, 1 << N):
        S = [x for x in range(N) if (mask >> x) & 1]
        if len(S) in (1,N):
            continue
        ok = True
        for z in range(N):
            if z in S:
                continue
            if len({rel(z,s) for s in S}) != 1:
                ok = False
                break
        if ok:
            ans.append((tuple(S), is_chain(S)))
    return ans

E = count_extensions()
assert E == 482
w,witness = width()
assert w == 3 and set(witness) == {1,4,5}
assert is_chain([0,1,2,6]) and is_chain([3,4,7]) and is_chain([5,8])
assert connected('comparability') and connected('incomparability')
autos = autonomous_sets()
assert autos == [((1,2), True)]

assert not R[a][b] and not R[b][a]
assert preds(b) < preds(a)
D = preds(a) - preds(b)
assert D == {d} and is_chain(D)
assert succs(a) < succs(b)
U = succs(b) - succs(a)
mins = {u for u in U if not any(v != u and R[v][u] for v in U)}
assert U == {u1,u2} and mins == {u1,u2}

# Endpoint and canonical reverse channels.
endpoint = count_extensions(((a,b),))
L = count_extensions(((b,d),))
U1 = count_extensions(((u1,a),))
U2 = count_extensions(((u2,a),))
assert (endpoint,L,U1,U2) == (154,70,50,116)
assert all(3*x < E for x in (endpoint,L,U1,U2))

# Static cross-group positive association fails for the lower channel and u1.
LU1 = count_extensions(((b,d),(u1,a)))
assert LU1 == 7
cov_num = LU1*E - L*U1
assert cov_num == -126 < 0

# The exact blocker-union identity remains correct.
LU2 = count_extensions(((b,d),(u2,a)))
U12 = count_extensions(((u1,a),(u2,a)))
LU12 = count_extensions(((b,d),(u1,a),(u2,a)))
assert (LU2,U12,LU12) == (30,30,5)
union = L + U1 + U2 - LU1 - LU2 - U12 + LU12
assert union == 174 == E - 2*endpoint

# This is not a POS3 counterexample: record every balanced escape pair.
balanced = []
for x in range(N):
    for y in range(x+1,N):
        if R[x][y] or R[y][x]:
            continue
        xy = count_extensions(((x,y),))
        if E <= 3*xy <= 2*E:
            balanced.append((x,y,xy))
assert balanced == [(0,3,248),(1,4,252),(2,5,174),(2,7,312),(6,8,210),(7,8,299)]

print('E', E)
print('width', w, 'antichain', witness, 'chain_cover', [[0,1,2,6],[3,4,7],[5,8]])
print('comparability_connected', True, 'incomparability_connected', True)
print('proper_nontrivial_autonomous_sets', autos)
print('corridor', 'a',a,'b',b,'D',sorted(D),'Umin',sorted(mins))
print('endpoint_a_before_b', endpoint, '/', E)
print('lower_b_before_d', L, '/', E)
print('upper_u1_before_a', U1, '/', E)
print('upper_u2_before_a', U2, '/', E)
print('intersection_lower_u1', LU1, '/', E)
print('cross_group_covariance_numerator', cov_num)
print('blocker_union', union, 'expected', E-2*endpoint)
print('balanced_escape_pairs', balanced)
print('POS3_CROSS_GROUP_STATIC_CORRELATION_REFUTED_PASS')
