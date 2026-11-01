from fractions import Fraction as F
from itertools import combinations
from collections import deque

n = 7
d = 6
verts = list(range(n))
edges = list(combinations(verts, 2))
edge_index = {e: i for i, e in enumerate(edges)}
assert len(edges) == 21


def rank_q(M):
    A = [[F(x) for x in row] for row in M]
    if not A:
        return 0
    m = len(A)
    ncol = len(A[0])
    r = 0
    for c in range(ncol):
        piv = None
        for i in range(r, m):
            if A[i][c]:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [A[i][j] - q * A[r][j] for j in range(ncol)]
        r += 1
        if r == m:
            break
    return r


# Edge x vertex unsigned incidence matrix for K_7.
A = [[1 if v in e else 0 for v in verts] for e in edges]
rankA = rank_q(A)
assert rankA == 7
kernel_dim = len(edges) - rankA
assert kernel_dim == 14

# Trivial edge vector lies in the incidence image.
ones = [F(1) for _ in edges]
half_vertex = [F(1, 2) for _ in verts]
Ahalf = [sum(F(A[i][v]) * half_vertex[v] for v in verts) for i in range(len(edges))]
assert Ahalf == ones

# Image of the 6-dimensional vertex-standard subspace.
std = []
for r in range(6):
    vec = []
    for e in edges:
        vec.append(F((1 if r in e else 0) - (1 if 6 in e else 0)))
    std.append(vec)
assert rank_q(std) == 6
span_matrix = [[ones[i]] + [std[j][i] for j in range(6)] for i in range(21)]
assert rank_q(span_matrix) == 7

# S_7 generators and exact equivariance of the incidence representation.
cycle7 = {i: (i + 1) % 7 for i in range(7)}
swap01 = {i: (1 if i == 0 else 0 if i == 1 else i) for i in range(7)}


def edge_perm(p, e):
    a, b = p[e[0]], p[e[1]]
    return (a, b) if a < b else (b, a)


for p in [cycle7, swap01]:
    for e in edges:
        pe = edge_perm(p, e)
        for v in verts:
            assert (v in e) == (p[v] in pe)


def perm_matrix_edge(p):
    M = [[0] * 21 for _ in range(21)]
    for j, e in enumerate(edges):
        i = edge_index[edge_perm(p, e)]
        M[i][j] = 1
    return M


# Fixed subspace of the S_7 edge-permutation representation.
constraints = []
for p in [cycle7, swap01]:
    P = perm_matrix_edge(p)
    for i in range(21):
        constraints.append([P[i][j] - (1 if i == j else 0) for j in range(21)])
fixed_dim = 21 - rank_q(constraints)
assert fixed_dim == 1

# Full quartic cross-equation orbit under S_7 semidirect S_6^7.
states = [(a, b, i, j) for a, b in edges for i in range(d) for j in range(d)]
state_set = set(states)
assert len(states) == 756

cycle6 = {i: (i + 1) % 6 for i in range(6)}
swap6 = {i: (1 if i == 0 else 0 if i == 1 else i) for i in range(6)}


def act_basis(state, p):
    a, b, i, j = state
    aa, bb = p[a], p[b]
    if aa < bb:
        return (aa, bb, i, j)
    return (bb, aa, j, i)


def act_cols(state, k, p):
    a, b, i, j = state
    if a == k:
        i = p[i]
    if b == k:
        j = p[j]
    return (a, b, i, j)


gens = [lambda s, p=p: act_basis(s, p) for p in (cycle7, swap01)]
for k in range(7):
    for p in (cycle6, swap6):
        gens.append(lambda s, k=k, p=p: act_cols(s, k, p))

start = (0, 1, 0, 0)
seen = {start}
q = deque([start])
while q:
    s = q.popleft()
    for g in gens:
        t = g(s)
        assert t in state_set
        if t not in seen:
            seen.add(t)
            q.append(t)
assert len(seen) == 756

print("P21 S7 edge-module / cross-orbit exact checker: PASS")
print(f"blocks={len(edges)}, cross_equations={len(states)}")
print(f"edge_incidence_rank={rankA}, decomposition_dims=1+6+{kernel_dim}=21")
print(f"S7_edge_fixed_subspace_dim={fixed_dim}")
print(f"full_cross_equation_orbit_size={len(seen)}, orbit_count=1")
print("degree4 invariant cross-multiplier channel dimension=1 (permutation-module consequence)")
print("ALL_EXACT_CHECKS_PASS")
