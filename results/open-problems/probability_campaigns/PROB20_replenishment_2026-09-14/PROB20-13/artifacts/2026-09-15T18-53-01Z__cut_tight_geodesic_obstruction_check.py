"""Exact rational checker for the PROB20-13 family

    G_a = K_1 join (K_{1,a} disjoint_union K_{2a}).

The script verifies, using Fraction arithmetic only:
  * the explicit product-demand path routing in the 2026-09-15T18-50-54Z report;
  * every unordered commodity has scaled demand d_u d_v;
  * the maximum scaled edge load is R = 4 a (3a+1);
  * hence F(G_a) = R/m once combined with the cut lower bound;
  * every geodesic-only routing has edge h-x load at least
        W = (a+1)(4a^2+3a+1),
    so F_geo >= W/m.

This is corroborative code, not an independent proof.
"""

from collections import defaultdict
from fractions import Fraction


def edge(u, v):
    return tuple(sorted((u, v), key=str))


def certificate(a: int):
    assert a >= 1

    h, x = "h", "x"
    leaves = [f"l{i}" for i in range(1, a + 1)]
    clique = [f"c{j}" for j in range(1, 2 * a + 1)]
    vertices = [h, x] + leaves + clique

    edges = set()
    for v in vertices:
        if v != h:
            edges.add(edge(h, v))
    for l in leaves:
        edges.add(edge(x, l))
    for i in range(len(clique)):
        for j in range(i + 1, len(clique)):
            edges.add(edge(clique[i], clique[j]))

    deg = {v: 0 for v in vertices}
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1

    m = len(edges)
    assert m == (a + 1) * (2 * a + 1)
    assert deg[h] == 3 * a + 1
    assert deg[x] == a + 1
    assert all(deg[l] == 2 for l in leaves)
    assert all(deg[c] == 2 * a for c in clique)

    T = 4 * a * a + 3 * a + 1
    W = (a + 1) * T
    p = (3 * a + 1) ** 2
    D0 = 2 * (a - 1) * (2 * a + 1)
    assert p + a * D0 == W

    routes = defaultdict(list)

    def add_route(u, v, amount, path):
        routes[edge(u, v)].append((Fraction(amount), path))

    # Effective h-x demand: split every constituent commodity in the
    # same proportions p/W and D0/W through each leaf.
    whx = deg[h] * deg[x]
    add_route(h, x, Fraction(whx * p, W), [h, x])
    for l in leaves:
        add_route(h, x, Fraction(whx * D0, W), [h, l, x])

    for c in clique:
        w = deg[c] * deg[x]
        add_route(c, x, Fraction(w * p, W), [c, h, x])
        for l in leaves:
            add_route(c, x, Fraction(w * D0, W), [c, h, l, x])

    # Other cross-clique commodities.
    for c in clique:
        add_route(c, h, deg[c] * deg[h], [c, h])
        for l in leaves:
            add_route(c, l, deg[c] * deg[l], [c, h, l])

    # Book-internal commodities.
    for l in leaves:
        add_route(h, l, deg[h] * deg[l], [h, l])
        add_route(x, l, deg[x] * deg[l], [x, l])

    for i in range(a):
        for j in range(i + 1, a):
            add_route(
                leaves[i], leaves[j],
                deg[leaves[i]] * deg[leaves[j]],
                [leaves[i], x, leaves[j]],
            )

    # Clique-internal commodities.
    for i in range(len(clique)):
        for j in range(i + 1, len(clique)):
            add_route(
                clique[i], clique[j],
                deg[clique[i]] * deg[clique[j]],
                [clique[i], clique[j]],
            )

    all_pairs = {
        edge(u, v)
        for i, u in enumerate(vertices)
        for v in vertices[i + 1 :]
    }
    assert set(routes) == all_pairs

    loads = {e: Fraction(0) for e in edges}
    for uv, path_list in routes.items():
        u, v = uv
        total = sum((amount for amount, _ in path_list), Fraction(0))
        assert total == deg[u] * deg[v]

        for amount, path in path_list:
            assert {path[0], path[-1]} == {u, v}
            for s, t in zip(path, path[1:]):
                e = edge(s, t)
                assert e in edges
                loads[e] += amount

    R = 4 * a * (3 * a + 1)
    assert max(loads.values()) == R

    for c in clique:
        assert loads[edge(h, c)] == R
    for l in leaves:
        assert loads[edge(h, l)] == R

    assert loads[edge(h, x)] == (3 * a + 1) ** 2
    for l in leaves:
        assert loads[edge(x, l)] == 4 * a * a + 4 * a - 4
    for i in range(len(clique)):
        for j in range(i + 1, len(clique)):
            assert loads[edge(clique[i], clique[j])] == 4 * a * a

    # Forced geodesic load on h-x: the adjacent h-x demand plus every
    # c_j-x demand, whose unique common neighbor is h.
    forced_geodesic_hx = (
        deg[h] * deg[x]
        + sum(deg[c] * deg[x] for c in clique)
    )
    assert forced_geodesic_hx == (a + 1) * (4 * a * a + 3 * a + 1)

    return {
        "a": a,
        "m": m,
        "R": R,
        "F": Fraction(R, m),
        "geodesic_lower_bound": Fraction(forced_geodesic_hx, m),
        "geodesic_to_optimum_ratio_lower_bound": Fraction(
            forced_geodesic_hx, R
        ),
    }


if __name__ == "__main__":
    for a in range(1, 51):
        certificate(a)
    print("Exact certificate checks passed for a = 1,...,50")

    for a in (1, 2, 3, 10, 50):
        out = certificate(a)
        print(
            f"a={a}: F={out['F']}, "
            f"F_geo>={out['geodesic_lower_bound']}, "
            f"ratio>={out['geodesic_to_optimum_ratio_lower_bound']}"
        )
