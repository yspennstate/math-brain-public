from fractions import Fraction
import heapq
import random

# Supplementary exact sanity check for the identity used in the P20 T10
# monotone target-difference compiler.  This is NOT an asymptotic FPP proof.
# All edge weights and shortest-path calculations are exact Fractions.

V = [(x, y) for x in range(7) for y in range(-2, 3)]
VSET = set(V)
rng = random.Random(20260920)

edges = {}
for u in V:
    x, y = u
    for dx, dy in ((1, 0), (0, 1)):
        v = (x + dx, y + dy)
        if v in VSET:
            edges[frozenset((u, v))] = Fraction(rng.randrange(3, 250), 97)

adj = {u: [] for u in V}
for e, w in edges.items():
    u, v = tuple(e)
    adj[u].append((v, w))
    adj[v].append((u, w))


def distances(target):
    d = {u: None for u in V}
    d[target] = Fraction(0)
    pq = [(Fraction(0), target)]
    while pq:
        du, u = heapq.heappop(pq)
        if du != d[u]:
            continue
        for v, w in adj[u]:
            nd = du + w
            if d[v] is None or nd < d[v]:
                d[v] = nd
                heapq.heappush(pq, (nd, v))
    return d


o = (0, 0)
C = (6, 0)
A = (6, 2)
dC = distances(C)
dA = distances(A)

# Choose the lexicographically first C-geodesic if there is a tie.
gamma = [o]
u = o
while u != C:
    candidates = []
    for v, w in adj[u]:
        if w + dC[v] == dC[u]:
            candidates.append((v, w))
    assert candidates
    candidates.sort()
    v, _ = candidates[0]
    gamma.append(v)
    u = v

phi = {u: dA[u] - dC[u] for u in V}
sum_rA = Fraction(0)
rows = []
for u, v in zip(gamma, gamma[1:]):
    w = edges[frozenset((u, v))]
    rC = w + dC[v] - dC[u]
    rA = w + dA[v] - dA[u]
    dphi = phi[v] - phi[u]
    assert rC == 0
    assert rA == dphi
    assert dphi >= 0
    sum_rA += rA
    rows.append((u, v, w, rC, rA, dphi))

triangle = dC[o] + dA[C] - dA[o]
assert sum_rA == triangle
assert phi[C] - phi[o] == triangle

print("P20-T10-MONOTONE-TARGET-DIFFERENCE-SANITY")
print(f"vertices={len(V)} edges={len(edges)}")
print(f"origin={o} C={C} A={A}")
print(f"gamma={gamma}")
print(f"triangle_residual={triangle} = {float(triangle):.12f}")
print(f"phi_start={phi[o]} phi_end={phi[C]} increment={phi[C]-phi[o]}")
print(f"sum_rA_on_C_geodesic={sum_rA}")
for u, v, w, rC, rA, dphi in rows:
    print(f"{u}->{v} w={w} rC={rC} rA={rA} dphi={dphi}")
print("P20-T10-MONOTONE-TARGET-DIFFERENCE-SANITY: ALL_EXACT_CHECKS_PASS")
