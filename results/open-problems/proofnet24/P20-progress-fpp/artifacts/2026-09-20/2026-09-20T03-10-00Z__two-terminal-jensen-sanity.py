from fractions import Fraction
import heapq
import itertools

# Exact finite sanity check for the deterministic two-terminal residual/Jensen
# identities used in P20's 2026-09-20 T10 report.  This is not a proof of
# asymptotic FPP curvature and contains no sampled numerical curvature.

V = [(i, j) for i in range(5) for j in range(5)]
edges = []
k = 1
for i, j in V:
    for di, dj in [(1, 0), (0, 1)]:
        u = (i, j)
        v = (i + di, j + dj)
        if v in V:
            w = Fraction(1000 + k, 1000)
            edges.append((u, v, w))
            k += 1

adj = {v: [] for v in V}
for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))


def dijkstra(src, graph):
    dist = {v: None for v in graph}
    dist[src] = Fraction(0)
    pq = [(Fraction(0), src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if dist[v] is None or nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


A = (4, 0)
C = (4, 4)
s = (0, 0)
f = dijkstra(A, adj)
g = dijkstra(C, adj)
d = f[C]
theta = Fraction(2, 3)
h = {v: theta * f[v] + (1 - theta) * g[v] for v in V}
wenv = {
    v: min(f[v] + (1 - theta) * d, g[v] + theta * d)
    for v in V
}

# q_theta(x,y)=tau+h(y)-h(x), then exact residual distance to {A,C}.
qadj = {v: [] for v in V}
for x in V:
    for y, tau in adj[x]:
        q = tau + h[y] - h[x]
        assert q >= 0
        qadj[x].append((y, q))

radj = {v: [] for v in V}
for x in V:
    for y, q in qadj[x]:
        radj[y].append((x, q))

R = {v: None for v in V}
pq = []
for t in [A, C]:
    R[t] = Fraction(0)
    heapq.heappush(pq, (Fraction(0), t))
while pq:
    dd, u = heapq.heappop(pq)
    if dd != R[u]:
        continue
    for x, q in radj[u]:
        nd = dd + q
        if R[x] is None or nd < R[x]:
            R[x] = nd
            heapq.heappush(pq, (nd, x))

assert all(R[v] == wenv[v] - h[v] for v in V)
DA = f[s] + d - g[s]
DC = g[s] + d - f[s]
assert R[s] == min((1 - theta) * DA, theta * DC)
assert DA >= R[s] / (1 - theta)

# Exact finite-grid falsification check of the pointwise local Jensen-gap bound.
a = [Fraction(0), Fraction(1, 3), Fraction(7, 10), Fraction(6, 5)]
c = [Fraction(4, 5), Fraction(0), Fraction(1, 2), Fraction(11, 10)]
vals = [Fraction(1, 10), Fraction(1, 2), Fraction(1), Fraction(3, 2)]
count = 0
disagreements = 0
for E in itertools.product(vals, repeat=4):
    Xa = [E[i] + a[i] for i in range(4)]
    Xc = [E[i] + c[i] for i in range(4)]
    ia = min(range(4), key=lambda i: Xa[i])
    ic = min(range(4), key=lambda i: Xc[i])
    ma = min(Xa)
    mc = min(Xc)
    Xm = [theta * Xa[i] + (1 - theta) * Xc[i] for i in range(4)]
    kappa = min(Xm) - (theta * ma + (1 - theta) * mc)
    assert kappa >= 0
    if ia != ic:
        disagreements += 1
        Ga = sorted(Xa)[1] - sorted(Xa)[0]
        Gc = sorted(Xc)[1] - sorted(Xc)[0]
        assert kappa >= min(theta * Ga, (1 - theta) * Gc)
    count += 1

print(f"FINITE_GRAPH_VERTICES = {len(V)}")
print(f"FINITE_GRAPH_EDGES = {len(edges)}")
print(f"THETA = {theta}")
print(f"D_A_C = {d}")
print(f"D_A_START = {DA}")
print(f"D_C_START = {DC}")
print(f"R_THETA_START = {R[s]}")
print(f"ENVELOPE_MINUS_H_START = {wenv[s] - h[s]}")
print("RESIDUAL_IDENTITY_ALL_VERTICES = True")
print(f"LOCAL_GRID_CASES = {count}")
print(f"LOCAL_GRID_DISAGREEMENTS = {disagreements}")
print("LOCAL_POINTWISE_GAP_CHECK = True")
print("P20-T10-TWO-TERMINAL-JENSEN-SANITY: ALL_EXACT_CHECKS_PASS")
