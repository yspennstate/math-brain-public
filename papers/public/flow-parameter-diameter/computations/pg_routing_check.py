"""Exact check of the routing in the proof of Proposition 5.1 on cones over Inc(PG(2,s)), s = 2, 3, 4, 5:
every flow is a unit flow to pi, and 2m sum_a pi_a |f^(a)_e| = V_3 on every edge e."""
from fractions import Fraction as Fr
from collections import defaultdict
from flowlib import pg2_incidence_graph, cone, bfs_dist, flow_parameter_lp


def check(p, k=1):
    adjH, N = pg2_incidence_graph(p, k)
    s = p ** k
    n = 2 * N
    G = cone(adjH)
    h = n
    deg = [len(a) for a in G]
    twom = sum(deg)
    pi = [Fr(x, twom) for x in deg]
    theta = Fr(3 * (s * s + 3 * s + 1), s * (s + 2) * (s + 4))
    load = defaultdict(Fr)          # undirected edge -> sum_a pi_a |f^(a)_e|
    for a in range(n + 1):
        f = defaultdict(Fr)         # arc (u,v) -> flow of source a
        def push(path, mass):
            for u, v in zip(path, path[1:]):
                f[(u, v)] += mass
                f[(v, u)] -= mass
        if a == h:
            for v in range(n):
                push([h, v], pi[v])
        else:
            dist = bfs_dist(adjH, a)
            push([a, h], pi[h])
            for v in range(n):
                if v == a:
                    continue
                if dist[v] == 1:
                    push([a, v], pi[v])
                elif dist[v] == 2:
                    mid = [x for x in adjH[a] if v in adjH[x]]
                    assert len(mid) == 1
                    push([a, mid[0], v], pi[v])
                else:
                    assert dist[v] == 3
                    push([a, h, v], theta * pi[v])
                    paths = [(x, y) for x in adjH[a] for y in adjH[x] if v in adjH[y]]
                    assert len(paths) == s + 1, len(paths)
                    for x, y in paths:
                        push([a, x, y, v], (1 - theta) * pi[v] / (s + 1))
        # conservation: net outflow at i is 1_(i=a) - pi_i
        for i in range(n + 1):
            out = sum(f[(i, j)] for j in G[i])
            assert out == (1 if i == a else 0) - pi[i], (a, i, out)
        for u in range(n + 1):
            for v in G[u]:
                if u < v:
                    load[(u, v)] += pi[a] * abs(f[(u, v)])
    psi = twom * max(load.values())
    mn = twom * min(load.values())
    V3 = Fr((s + 2) * (5 * s**3 + 19 * s**2 + 13 * s + 8), (s + 3) * (s + 4) * (s * s + s + 1))
    print(f"s={s}: |V|={n+1} psi={psi} (min edge {mn}) V3={V3} equal={psi == V3 and mn == V3}")
    if n + 1 <= 30:
        print("   LP:", flow_parameter_lp(G), float(V3))


for p, k in [(2, 1), (3, 1), (2, 2), (5, 1)]:
    check(p, k)
