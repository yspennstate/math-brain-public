"""Exact corroboration for the PROB20-13 distance-biregular radial-flow theorem.

This script is NOT the proof.  It uses exact rational arithmetic to:
  * verify the distance-biregular shell/intersection-array property of test graphs;
  * build the stationary-shell radial source flows;
  * verify div f^x = delta_x - pi exactly;
  * verify weighted absolute edge loads are exactly equal;
  * verify psi = 2 E_{pi x pi} dist exactly.

The main nonregular test is the subdivision graph of the Petersen graph, a
standard distance-biregular example.

Requires networkx.  numpy is used only for the optional floating-point
relaxation-time diagnostic.
"""

from fractions import Fraction
import networkx as nx


def subdivision_graph(G):
    H = nx.Graph()
    H.add_nodes_from(("v", v) for v in G.nodes())
    for j, (u, v) in enumerate(G.edges()):
        e = ("e", j)
        H.add_node(e)
        H.add_edge(("v", u), e)
        H.add_edge(e, ("v", v))
    return H


def bipartition(G):
    color = nx.bipartite.color(G)
    X0 = [v for v, c in color.items() if c == 0]
    X1 = [v for v, c in color.items() if c == 1]
    return color, X0, X1


def intersection_array_at(G, x):
    """Return (b_r),(c_r),(k_r) if every distance layer is equitable."""
    dist = nx.single_source_shortest_path_length(G, x)
    D = max(dist.values())
    layers = {r: [v for v, d in dist.items() if d == r] for r in range(D + 1)}
    b, c, k = [], [], []
    for r in range(D + 1):
        local = []
        for y in layers[r]:
            cin = sum(1 for z in G.neighbors(y) if r > 0 and dist[z] == r - 1)
            bout = sum(1 for z in G.neighbors(y) if r < D and dist[z] == r + 1)
            local.append((cin, bout))
        if len(set(local)) != 1:
            return None
        c.append(local[0][0])
        b.append(local[0][1])
        k.append(len(layers[r]))
    return tuple(b), tuple(c), tuple(k)


def verify_distance_biregular(G):
    """Check that bases in each color class share one intersection array."""
    _, X0, X1 = bipartition(G)
    out = {}
    for eps, X in [(0, X0), (1, X1)]:
        arrays = [intersection_array_at(G, x) for x in X]
        if any(a is None for a in arrays) or len(set(arrays)) != 1:
            return False, None
        out[eps] = arrays[0]
    return True, out


def radial_family_exact(G):
    """Construct exact radial source flows using stationary shell masses."""
    nodes = list(G.nodes())
    edges = list(G.edges())
    m = G.number_of_edges()
    pi = {v: Fraction(G.degree(v), 2 * m) for v in nodes}
    flows = {}

    for x in nodes:
        dist = nx.single_source_shortest_path_length(G, x)
        D = max(dist.values())
        layers = {r: [v for v in nodes if dist[v] == r] for r in range(D + 1)}
        q = {}
        for r in range(D):
            M = sum(
                pi[v]
                for t in range(r + 1, D + 1)
                for v in layers[t]
            )
            E = sum(
                1
                for u, v in edges
                if sorted((dist[u], dist[v])) == [r, r + 1]
            )
            q[r] = M / E

        f = {}
        for j, (u, v) in enumerate(edges):
            du, dv = dist[u], dist[v]
            if abs(du - dv) == 1:
                r = min(du, dv)
                f[j] = q[r] if du < dv else -q[r]
            else:
                f[j] = Fraction(0)
        flows[x] = f

    # Exact divergence check.
    for x, f in flows.items():
        div = {v: Fraction(0) for v in nodes}
        for j, (u, v) in enumerate(edges):
            div[u] += f[j]
            div[v] -= f[j]
        for v in nodes:
            target = (Fraction(1) if v == x else Fraction(0)) - pi[v]
            assert div[v] == target, (x, v, div[v], target)

    loads = [
        sum(pi[x] * abs(flows[x][j]) for x in nodes)
        for j in range(len(edges))
    ]
    assert len(set(loads)) == 1, "weighted edge loads are not constant"

    avg_distance = sum(
        pi[x] * pi[y] * nx.shortest_path_length(G, x, y)
        for x in nodes
        for y in nodes
    )
    psi = loads[0] / Fraction(1, 2 * m)
    assert psi == 2 * avg_distance

    return {
        "pi": pi,
        "common_edge_load": loads[0],
        "mean_stationary_distance": avg_distance,
        "psi": psi,
    }


def optional_tau_rel(G):
    try:
        import numpy as np
    except ImportError:
        return None
    A = nx.to_numpy_array(G, dtype=float)
    deg = A.sum(axis=1)
    S = A / np.sqrt(np.outer(deg, deg))
    vals = np.linalg.eigvalsh(S)
    vals = np.sort(vals)[::-1]
    return 1.0 / (1.0 - vals[1])


def run_case(name, G):
    ok, arrays = verify_distance_biregular(G)
    assert ok, f"{name} failed distance-biregular check"
    result = radial_family_exact(G)
    print(name)
    print("  |V|, |E|, D =", G.number_of_nodes(), G.number_of_edges(), nx.diameter(G))
    print("  two color intersection arrays =", arrays)
    print("  common weighted edge load =", result["common_edge_load"])
    print("  E_pi,pi distance =", result["mean_stationary_distance"])
    print("  psi =", result["psi"])
    tau = optional_tau_rel(G)
    if tau is not None:
        print("  tau_rel ~=", tau)
        print("  2 tau_rel D ~=", 2 * tau * nx.diameter(G))


if __name__ == "__main__":
    # Standard nonregular distance-biregular example.
    run_case("subdivision(Petersen)", subdivision_graph(nx.petersen_graph()))

    # Complete bipartite controls.
    run_case("K_2,3", nx.complete_bipartite_graph(2, 3))
    run_case("star K_1,5", nx.star_graph(5))
