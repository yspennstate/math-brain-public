#!/usr/bin/env python3
"""
Exact self-check for the R20 theorem:
Every nice subcubic graph whose degree-3 vertices are independent
admits a proper pushing scheme with max rho <= 3.

This does NOT prove the infinite theorem; the report contains the proof.
The checker verifies:
  (1) the closed-form chain templates for k=1..1000 by exact integer sums;
  (2) the constructive core + leaf-extension algorithm on every connected
      graph in NetworkX's complete graph atlas (all unlabeled graphs <=7)
      that lies in the theorem's class.
All arithmetic is integer/exact.
"""
from collections import Counter, deque
import itertools
import networkx as nx

def sigma(G, rho, u):
    return G.degree(u) * (1 + rho[u]) + sum(rho[v] for v in G.neighbors(u))

def is_proper(G, rho):
    return all(sigma(G, rho, u) != sigma(G, rho, v) for u, v in G.edges())

def template(k):
    assert k >= 1
    if k == 1:
        return [1]
    if k == 2:
        return [1, 2]
    if k == 3:
        return [1, 0, 1]
    if k == 4:
        return [1, 0, 1, 1]
    r = k % 4
    if r == 1:
        t = (k - 1) // 4
        w = [1] + [0, 0, 0, 1] * t
    elif r == 2:
        t = (k - 2) // 4
        w = [1] + [0, 0, 0, 1] * t + [1]
    elif r == 3:
        t = (k - 3) // 4
        w = [1] + [0, 0, 0, 1] * t + [1, 1]
    else:
        t = k // 4
        assert t >= 2
        w = [1] + [0, 0, 0, 1] * (t - 1) + [0, 2, 1]
    assert len(w) == k
    return w

def chain_sums(w):
    # Both branch endpoints have push 3.
    out = []
    for i, x in enumerate(w):
        left = 3 if i == 0 else w[i - 1]
        right = 3 if i + 1 == len(w) else w[i + 1]
        out.append(2 * (1 + x) + left + right)
    return out

def brute_witness(G, bound):
    nodes = list(G.nodes())
    for vals in itertools.product(range(bound + 1), repeat=len(nodes)):
        rho = dict(zip(nodes, vals))
        if is_proper(G, rho):
            return rho
    return None

def construct(G):
    """Construct the theorem witness for a connected eligible atlas graph."""
    Delta = max((G.degree(v) for v in G), default=0)
    if Delta <= 2:
        # Known source case; brute force only for finite atlas validation.
        return brute_witness(G, Delta)
    assert Delta == 3
    assert all(not (G.degree(u) == 3 and G.degree(v) == 3) for u, v in G.edges())

    if nx.is_tree(G):
        # Known source theorem for trees; brute force only for atlas validation.
        return brute_witness(G, 3)

    core = nx.k_core(G, k=2)
    assert len(core) > 0

    if max(dict(core.degree()).values()) <= 2:
        # The core is a cycle, a known source case.
        rho_core = brute_witness(core, 2)
        assert rho_core is not None
    else:
        B = {v for v in core if core.degree(v) == 3}
        assert B
        for u, v in core.edges():
            assert not (u in B and v in B)

        rho_core = {b: 3 for b in B}
        D = set(core.nodes()) - B

        for C in nx.connected_components(core.subgraph(D)):
            HC = core.subgraph(C)
            ends = []
            for x in C:
                for b in core.neighbors(x):
                    if b in B:
                        ends.append((x, b))
            # Every maximal degree-2 chain in a connected 2-core with B nonempty
            # has exactly two branch incidences, counting a possible return
            # to the same branch twice.
            assert len(ends) == 2, (C, ends)
            x0, b0 = ends[0]
            x1, b1 = ends[1]
            if len(C) == 1:
                assert x0 == x1
                order = [x0]
            else:
                order = nx.shortest_path(HC, x0, x1)
                assert len(order) == len(C)
            w = template(len(order))
            for x, a in zip(order, w):
                assert x not in rho_core
                rho_core[x] = a

        assert set(rho_core) == set(core.nodes())
        assert max(rho_core.values()) <= 3
        assert is_proper(core, rho_core)

    # Reattach the pruned forest one vertex at a time, outward from the core.
    rho = dict(rho_core)
    S = set(core.nodes())
    dist = {v: 0 for v in core.nodes()}
    q = deque(core.nodes())
    while q:
        u = q.popleft()
        for v in G.neighbors(u):
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)

    outside = sorted((v for v in G if v not in S), key=lambda v: (dist[v], v))
    H = G.subgraph(S).copy()
    assert is_proper(H, rho)

    for w in outside:
        parents = [u for u in G.neighbors(w) if u in S]
        assert len(parents) == 1
        u = parents[0]
        assert H.degree(u) <= 2

        H2 = H.copy()
        H2.add_node(w)
        H2.add_edge(u, w)

        chosen = None
        for x in range(4):
            rho[w] = x
            if is_proper(H2, rho):
                chosen = x
                break
        assert chosen is not None
        H = H2
        S.add(w)

    assert set(H.nodes()) == set(G.nodes())
    assert set(map(frozenset, H.edges())) == set(map(frozenset, G.edges()))
    assert max(rho.values(), default=0) <= 3
    assert is_proper(G, rho)
    return rho

# Part 1: exact chain-template validation.
max_k = 1000
max_chain_sum = 0
for k in range(1, max_k + 1):
    w = template(k)
    assert all(0 <= x <= 3 for x in w)
    assert w[0] >= 1 and w[-1] >= 1
    ss = chain_sums(w)
    assert all(ss[i] != ss[i + 1] for i in range(len(ss) - 1))
    max_chain_sum = max(max_chain_sum, max(ss))
assert max_chain_sum <= 14

# Part 2: complete unlabeled atlas through order 7.
eligible = []
counts = Counter()
failures = []
for G in nx.graph_atlas_g():
    n = len(G)
    if n == 0 or not nx.is_connected(G):
        continue
    if n == 2 and G.number_of_edges() == 1:
        continue  # not nice
    Delta = max(dict(G.degree()).values())
    if Delta > 3:
        continue
    if any(G.degree(u) == 3 and G.degree(v) == 3 for u, v in G.edges()):
        continue
    eligible.append(G)
    counts[n] += 1
    try:
        rho = construct(G)
        if rho is None or not is_proper(G, rho):
            failures.append(nx.to_graph6_bytes(G, header=False).decode().strip())
    except Exception:
        failures.append(nx.to_graph6_bytes(G, header=False).decode().strip())

print(f"chain_templates_checked=1..{max_k}")
print(f"max_chain_sigma_seen={max_chain_sum}")
print(f"atlas_eligible_connected_nice_subcubic_independent_deg3={len(eligible)}")
print("atlas_counts_by_order=" + repr(dict(sorted(counts.items()))))
print(f"atlas_failures={len(failures)}")
if failures:
    print("failure_graph6=" + repr(failures))
    raise SystemExit(1)
print("VERDICT=PASS")
print("STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_BMO_CONJECTURE_2_6")
