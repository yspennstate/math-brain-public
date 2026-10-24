#!/usr/bin/env python3
"""Exact verifier for HARD8-02 tensor absorbers.

Standard library only. No floating point, randomization, external solver, or timeout-based
mathematical inference.

Checks:
1. Closed-form endpoint-rooted path motifs and the odd tensor absorber.
2. Every labeled tree through order 6, every distinguished root for which exhaustive
   search finds an extremal-root graceful labeling, and k=0,...,4.
3. Exact suffix-root label coverage and exact internal/attachment spectra.
4. The block-separable sum obstruction on a deterministic parameter grid.
"""

from itertools import permutations, product
from collections import defaultdict
import heapq


def prufer_tree(seq, n):
    deg = [1] * n
    for x in seq:
        deg[x] += 1
    leaves = [i for i, d in enumerate(deg) if d == 1]
    heapq.heapify(leaves)
    edges = []
    for x in seq:
        leaf = heapq.heappop(leaves)
        edges.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
        if deg[x] == 1:
            heapq.heappush(leaves, x)
    a = heapq.heappop(leaves)
    b = heapq.heappop(leaves)
    edges.append((a, b))
    return edges


def bipartition(n, edges, root):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    col = [None] * n
    col[root] = 0
    stack = [root]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if col[v] is None:
                col[v] = 1 - col[u]
                stack.append(v)
    assert all(x in (0, 1) for x in col)
    return col


def is_graceful(n, edges, g):
    return sorted(g) == list(range(n)) and {
        abs(g[u] - g[v]) for u, v in edges
    } == set(range(1, n))


def find_extremal_graceful(n, edges, root):
    """Return one graceful labeling with root n-1, or None."""
    others = [v for v in range(n) if v != root]
    for p in permutations(range(n - 1)):
        g = [None] * n
        g[root] = n - 1
        for v, a in zip(others, p):
            g[v] = a
        if is_graceful(n, edges, g):
            return g
    return None


def verify_tensor(n, edges, root, g, k):
    assert is_graceful(n, edges, g)
    assert g[root] == n - 1
    c = 2 * k + 1
    col = bipartition(n, edges, root)

    lam = {}
    for r in range(c):
        tau = (2 * r) % c
        for v in range(n):
            pi = r if col[v] == 0 else tau
            lam[(r, v)] = c * g[v] + pi

    s = c * n
    assert set(lam.values()) == set(range(s))

    N = c * (n - 1)
    root_labels = {lam[(r, root)] for r in range(c)}
    assert root_labels == set(range(N, N + c))

    internal = []
    for r in range(c):
        for u, v in edges:
            internal.append(abs(lam[(r, u)] - lam[(r, v)]))
    assert len(internal) == N
    assert len(set(internal)) == N
    assert set(internal) == set(range(k + 1, k + N + 1))

    attachment = {k + 1 + x for x in root_labels}
    assert attachment == set(range(k + N + 1, k + N + c + 1))
    assert set(internal) | attachment == set(range(k + 1, k + s + 1))

    deviations = {(2 * r) % c - r for r in range(c)}
    assert deviations == set(range(-k, k + 1))


def path_motif(h):
    edges = [(i, i + 1) for i in range(h - 1)]
    g = []
    for i in range(h):
        if i % 2 == 0:
            g.append(h - 1 - i // 2)
        else:
            g.append((i - 1) // 2)
    assert is_graceful(h, edges, g)
    assert g[0] == h - 1
    return edges, g


def check_block_sum_identity():
    checks = 0
    forced = 0
    for c in range(1, 42):
        for k in range(0, 31):
            for d in range(1, 8):
                lifted_sum = c * c * d
                lo = k + (d - 1) * c + 1
                hi = k + d * c
                target_twice = c * (lo + hi)
                lifted_twice = 2 * lifted_sum
                equality = target_twice == lifted_twice
                assert equality == (c == 2 * k + 1)
                checks += 1
                forced += int(equality)
    return checks, forced


def main():
    path_checks = 0
    for h in range(2, 61):
        edges, g = path_motif(h)
        for k in range(0, 31):
            verify_tensor(h, edges, 0, g, k)
            path_checks += 1

    labeled_tree_counts = {}
    extremal_root_pairs = 0
    tensor_checks = 0

    for n in range(2, 7):
        seqs = [()] if n == 2 else product(range(n), repeat=n - 2)
        tree_count = 0
        rooted_supported = 0
        for seq in seqs:
            edges = prufer_tree(seq, n)
            tree_count += 1
            for root in range(n):
                g = find_extremal_graceful(n, edges, root)
                if g is None:
                    continue
                rooted_supported += 1
                extremal_root_pairs += 1
                for k in range(5):
                    verify_tensor(n, edges, root, g, k)
                    tensor_checks += 1
        labeled_tree_counts[n] = (tree_count, rooted_supported)

    sum_checks, sum_equalities = check_block_sum_identity()

    print("PATH_TENSOR_CHECKS", path_checks)
    print("LABELED_TREE_COUNTS", labeled_tree_counts)
    print("EXTREMAL_ROOTED_PAIRS", extremal_root_pairs)
    print("EXHAUSTIVE_TENSOR_CHECKS", tensor_checks)
    print("BLOCK_SUM_CHECKS", sum_checks)
    print("BLOCK_SUM_EQUALITIES", sum_equalities)
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
