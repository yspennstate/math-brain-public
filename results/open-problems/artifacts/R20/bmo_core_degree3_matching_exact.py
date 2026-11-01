#!/usr/bin/env python3
"""
Exact self-check for the R20 structural theorem candidate:

If G is a nice finite simple graph with maximum degree at most 3 and, in
the 2-core C of G, the vertices of C-degree 3 induce a matching, then G
admits a proper pushing scheme with all pushes in {0,1,2,3}.

The infinite theorem is proved in the run report.  This script checks the
closed-form degree-two-chain formulas and the resulting constructive scheme
on every eligible connected graph in NetworkX's complete unlabeled graph
atlas through seven vertices.  All pushing sums are integers.
"""

from itertools import product
from collections import Counter, deque
import networkx as nx


def sigma_values(G, rho):
    return {
        u: G.degree(u) * (1 + rho[u]) + sum(rho[v] for v in G.neighbors(u))
        for u in G.nodes()
    }


def is_proper(G, rho):
    s = sigma_values(G, rho)
    return all(s[u] != s[v] for u, v in G.edges())


def brute_witness(G, bound):
    nodes = list(G.nodes())
    if G.number_of_edges() == 0:
        return {u: 0 for u in nodes}
    for values in product(range(bound + 1), repeat=len(nodes)):
        rho = dict(zip(nodes, values))
        if is_proper(G, rho):
            return rho
    return None


def long_chain_word(k):
    assert k >= 3
    if k == 3:
        return [1, 0, 1]
    if k == 4:
        return [1, 0, 1, 1]
    if k % 4 == 1:
        t = (k - 1) // 4
        return [1] + [0, 0, 0, 1] * t
    if k % 4 == 2:
        t = (k - 2) // 4
        return [1] + [0, 0, 0, 1] * t + [1]
    if k % 4 == 3:
        t = (k - 3) // 4
        return [1] + [0, 0, 0, 1] * t + [1, 1]
    t = k // 4
    return [1] + [0, 0, 0, 1] * (t - 1) + [0, 2, 1]


def chain_sums(alpha, beta, word):
    k = len(word)
    out = []
    for i, x in enumerate(word):
        left = alpha if i == 0 else word[i - 1]
        right = beta if i == k - 1 else word[i + 1]
        out.append(2 * (1 + x) + left + right)
    return out


def check_chain_formulas():
    checked = 0
    max_sigma = 0
    for alpha, beta in product((2, 3), repeat=2):
        vals = chain_sums(alpha, beta, [1])
        max_sigma = max(max_sigma, *vals)
        checked += 1

    rules = {
        (3, 3): ([1, 2],),
        (2, 3): ([1, 1],),
        (3, 2): ([1, 1],),
        (2, 2): ([1, 2], [2, 1]),
    }
    for (alpha, beta), words in rules.items():
        for word in words:
            vals = chain_sums(alpha, beta, list(word))
            assert vals[0] != vals[1]
            max_sigma = max(max_sigma, *vals)
            checked += 1

    for k in range(3, 1001):
        word = long_chain_word(k)
        assert len(word) == k
        assert word[0] == 1 and word[-1] == 1
        for alpha, beta in product((2, 3), repeat=2):
            vals = chain_sums(alpha, beta, word)
            assert all(vals[i] != vals[i + 1] for i in range(k - 1))
            assert max(vals) <= 10
            max_sigma = max(max_sigma, *vals)
            checked += 1
    return checked, max_sigma


def core_matching_condition(G):
    if max((d for _, d in G.degree()), default=0) > 3:
        return False
    C = nx.k_core(G, k=2)
    B = [u for u in C if C.degree(u) == 3]
    D = C.subgraph(B)
    return max((d for _, d in D.degree()), default=0) <= 1


def extract_chains(C, B):
    B = set(B)
    R = set(C.nodes()) - B
    H = C.subgraph(R)
    chains = []
    for comp in nx.connected_components(H):
        S = set(comp)
        sub = C.subgraph(S)
        if len(S) == 1:
            order = [next(iter(S))]
            bnds = [v for v in C.neighbors(order[0]) if v in B]
            assert len(bnds) == 2
            b0, b1 = bnds
        else:
            ends = [u for u in S if sub.degree(u) == 1]
            assert len(ends) == 2
            order = list(nx.shortest_path(sub, ends[0], ends[1]))
            left = [v for v in C.neighbors(order[0]) if v in B]
            right = [v for v in C.neighbors(order[-1]) if v in B]
            assert len(left) == len(right) == 1
            b0, b1 = left[0], right[0]
        chains.append({"nodes": order, "b0": b0, "b1": b1})
    return chains


def construct_matching_core_scheme(G):
    Delta = max((d for _, d in G.degree()), default=0)

    if Delta <= 2 or nx.is_tree(G):
        return brute_witness(G, Delta)

    C = nx.k_core(G, k=2)
    if C.number_of_nodes() == 0:
        return brute_witness(G, Delta)

    B = [u for u in C if C.degree(u) == 3]
    if not B:
        return brute_witness(G, Delta)

    D = C.subgraph(B)
    assert max((d for _, d in D.degree()), default=0) <= 1

    rho = {b: 3 for b in B}
    for u, v in D.edges():
        rho[max(u, v)] = 2

    chains = extract_chains(C, B)
    special = []
    for i, ch in enumerate(chains):
        if (
            len(ch["nodes"]) == 2
            and rho[ch["b0"]] == 2
            and rho[ch["b1"]] == 2
        ):
            special.append(i)

    receiver = {}
    found = False
    for bits in product((0, 1), repeat=len(special)):
        indeg = Counter()
        trial = {}
        ok = True
        for i, bit in zip(special, bits):
            ch = chains[i]
            rec = ch["b1"] if bit else ch["b0"]
            indeg[rec] += 1
            trial[i] = rec
            if indeg[rec] > 1:
                ok = False
                break
        if ok:
            receiver = trial
            found = True
            break
    assert found

    for i, ch in enumerate(chains):
        nodes = ch["nodes"]
        k = len(nodes)
        a, b = ch["b0"], ch["b1"]
        alpha, beta = rho[a], rho[b]

        if k == 1:
            word = [1]
        elif k == 2:
            if alpha == beta == 2:
                rec = receiver[i]
                if a == b or rec == b:
                    word = [1, 2]
                else:
                    word = [2, 1]
            elif alpha == beta == 3:
                word = [1, 2]
            else:
                word = [1, 1]
        else:
            word = long_chain_word(k)

        for x, value in zip(nodes, word):
            rho[x] = value

    assert set(rho) == set(C.nodes())
    assert max(rho.values()) <= 3
    assert is_proper(C, rho)

    if C.number_of_nodes() < G.number_of_nodes():
        dist = {u: 0 for u in C}
        q = deque(C.nodes())
        while q:
            u = q.popleft()
            for v in G.neighbors(u):
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q.append(v)

        current = set(C.nodes())
        for d in range(1, max(dist.values()) + 1):
            for w in sorted(u for u in G if dist[u] == d):
                parents = [v for v in G.neighbors(w) if v in current]
                assert len(parents) == 1
                u = parents[0]
                H = G.subgraph(current)
                assert H.degree(u) <= 2

                chosen = None
                for x in range(4):
                    trial = dict(rho)
                    trial[w] = x
                    Hnew = G.subgraph(current | {w})
                    if is_proper(Hnew, trial):
                        chosen = x
                        break
                assert chosen is not None
                rho[w] = chosen
                current.add(w)

    assert set(rho) == set(G.nodes())
    assert max(rho.values()) <= Delta
    assert is_proper(G, rho)
    return rho


def atlas_check():
    counts = Counter()
    kinds = Counter()
    failures = []
    eligible = 0

    for G in nx.graph_atlas_g():
        n = G.number_of_nodes()
        if n == 0 or n > 7:
            continue
        if not nx.is_connected(G):
            continue
        if n == 2 and G.number_of_edges() == 1:
            continue
        if max((d for _, d in G.degree()), default=0) > 3:
            continue
        if not core_matching_condition(G):
            continue

        eligible += 1
        counts[n] += 1
        C = nx.k_core(G, k=2)
        B = [u for u in C if C.degree(u) == 3]
        D = C.subgraph(B)

        if nx.is_tree(G):
            kind = "tree"
        elif not B:
            kind = "cycle_core"
        elif D.number_of_edges() == 0:
            kind = "branch_independent_core"
        else:
            kind = "branch_matching_core"
        kinds[kind] += 1

        rho = construct_matching_core_scheme(G)
        if rho is None or not is_proper(G, rho):
            failures.append((n, nx.to_graph6_bytes(G, header=False).decode().strip()))

    return eligible, counts, kinds, failures


if __name__ == "__main__":
    chain_checked, max_chain_sigma = check_chain_formulas()
    eligible, counts, kinds, failures = atlas_check()

    print(f"networkx_version={nx.__version__}")
    print(f"chain_boundary_instances_checked={chain_checked}")
    print("chain_lengths_closed_form_checked=3..1000")
    print(f"max_chain_sigma_seen={max_chain_sigma}")
    print(f"atlas_eligible_connected_nice_subcubic_core_matching={eligible}")
    print("atlas_counts_by_order=" + repr(dict(sorted(counts.items()))))
    print("atlas_counts_by_kind=" + repr(dict(sorted(kinds.items()))))
    print(f"atlas_failures={len(failures)}")
    if failures:
        print("FAILURES=" + repr(failures))
        raise SystemExit(1)
    print("VERDICT=PASS")
    print("STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_BMO_CONJECTURE_2_6")
