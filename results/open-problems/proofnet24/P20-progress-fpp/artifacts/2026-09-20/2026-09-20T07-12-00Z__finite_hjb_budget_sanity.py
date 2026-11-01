from fractions import Fraction
import heapq

# Supplementary exact-rational sanity check for the finite-target HJB residual
# identities used in the accompanying P20 report. This is NOT an asymptotic
# FPP proof and does not use sampled curvature.

verts = [(x, y) for x in range(5) for y in range(-4, 5)]
V = set(verts)
w = {}
idx = 0
for x, y in verts:
    for dx, dy in [(1, 0), (0, 1)]:
        z = (x + dx, y + dy)
        if z in V:
            e = tuple(sorted(((x, y), z)))
            if e not in w:
                # Positive rational weights with tiny dyadic perturbations.
                w[e] = Fraction(2 + ((idx * 17 + 5) % 13), 10) + Fraction(1, 2 ** (idx + 20))
                idx += 1

adj = {v: [] for v in V}
for e, ww in w.items():
    u, v = e
    adj[u].append((v, ww))
    adj[v].append((u, ww))


def edge_weight(u, v):
    return w[tuple(sorted((u, v)))]


def dijkstra(start, cost):
    dist = {v: None for v in V}
    prev = {v: None for v in V}
    dist[start] = Fraction(0)
    pq = [(Fraction(0), start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, _ in adj[u]:
            nd = d + cost(u, v)
            if dist[v] is None or nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, prev


def distances_to(target):
    return dijkstra(target, lambda u, v: edge_weight(u, v))[0]


o = (0, 0)
b = (4, 0)
A = (4, 4)
C = (4, -4)
dA = distances_to(A)
dC = distances_to(C)


def Bz(dz, x, y):
    return dz[x] - dz[y]


def q(x, y):
    return edge_weight(x, y) - (Bz(dA, x, y) + Bz(dC, x, y)) / 2


all_nonnegative = all(q(x, y) >= 0 for x in V for y, _ in adj[x])

dq, _ = dijkstra(o, q)
dT, prevT = dijkstra(o, lambda u, v: edge_weight(u, v))
rhs = dT[b] - (Bz(dA, o, b) + Bz(dC, o, b)) / 2

path = []
cur = b
while True:
    path.append(cur)
    if cur == o:
        break
    cur = prevT[cur]
path.reverse()

sum_q = sum(q(path[i], path[i + 1]) for i in range(len(path) - 1))
kappa = {x: min(q(x, y) for y, _ in adj[x]) for x in V}
sum_kappa = sum(kappa[x] for x in path[:-1])


def residual(dz, x, y):
    return edge_weight(x, y) + dz[y] - dz[x]


def winner(dz, x):
    vals = sorted((residual(dz, x, y), y) for y, _ in adj[x])
    return vals[0][1]


bad = []
agreements = 0
disagreements = 0
for x in V - {A, C}:
    agree = winner(dA, x) == winner(dC, x)
    if (kappa[x] == 0) != agree:
        bad.append(x)
    agreements += int(agree)
    disagreements += int(not agree)

print("P20-T10-FINITE-HJB-BUDGET-SANITY")
print(f"vertices={len(V)} undirected_edges={len(w)}")
print(f"targets A={A} C={C} origin={o} axis_endpoint={b}")
print(f"all_oriented_q_nonnegative={all_nonnegative}")
print(f"Q_identity_pass={dq[b] == rhs}")
print(f"Q_exact={dq[b].numerator}/{dq[b].denominator}")
print(f"T_geodesic_q_sum_equals_Q={sum_q == dq[b]}")
print(f"kappa_path_sum_le_Q={sum_kappa <= sum_q}")
print(f"kappa_path_sum_exact={sum_kappa.numerator}/{sum_kappa.denominator}")
print(f"policy_agreement_iff_kappa_zero_pass={len(bad) == 0}")
print(f"checked_nonterminal_vertices={agreements + disagreements} agreements={agreements} disagreements={disagreements}")
assert all_nonnegative
assert dq[b] == rhs
assert sum_q == dq[b]
assert sum_kappa <= sum_q
assert not bad
print("P20-T10-FINITE-HJB-BUDGET-SANITY: ALL_EXACT_CHECKS_PASS")
