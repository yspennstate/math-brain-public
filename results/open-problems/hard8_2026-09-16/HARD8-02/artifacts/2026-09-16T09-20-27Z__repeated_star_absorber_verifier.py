#!/usr/bin/env python3
"""Exact verifier for HARD8-02 repeated-star one-gap absorbers.

Standard library only.  No floating point, randomized search, solver, or timeout-based
mathematical inference.

Checks the closed-form suffix-root absorber for c=2k+1 copies of an h-vertex
star rooted at its centre, the exact sum obstruction for arbitrary multiplicity c,
the pinned augmentation, and both low/high one-gap root-transfer formulas.
"""

from itertools import permutations


def irange(a, b):
    """Inclusive integer range as a set; empty when b<a."""
    return set(range(a, b + 1)) if b >= a else set()


def repeated_star_absorber(k, h):
    assert k >= 0 and h >= 2
    c = 2 * k + 1
    t = h - 1
    N = c * t
    s = c * h

    labels = {}
    roots = []
    edges = []
    root_of_leaf = {}

    for j in range(c):
        v = ("R", j)
        roots.append(v)
        labels[v] = N + j

    seen_j = set()
    for r in range(c):
        sigma = (r + k) % c
        j = r + sigma - k
        assert 0 <= j < c
        seen_j.add(j)
        for b in range(t):
            leaf = ("L", b, r)
            labels[leaf] = b * c + r
            root = ("R", j)
            edges.append((root, leaf))
            root_of_leaf[leaf] = root

    assert seen_j == set(range(c))
    return {
        "k": k,
        "h": h,
        "c": c,
        "t": t,
        "N": N,
        "s": s,
        "labels": labels,
        "roots": roots,
        "edges": edges,
        "root_of_leaf": root_of_leaf,
    }


def check_absorber(k, h):
    A = repeated_star_absorber(k, h)
    c, t, N, s = A["c"], A["t"], A["N"], A["s"]
    labels, roots, edges = A["labels"], A["roots"], A["edges"]

    assert len(labels) == s
    assert set(labels.values()) == set(range(s))
    assert {labels[r] for r in roots} == irange(s - c, s - 1)

    deg = {r: 0 for r in roots}
    for u, v in edges:
        if u in deg:
            deg[u] += 1
        if v in deg:
            deg[v] += 1
    assert set(deg.values()) == {t}

    internal = [abs(labels[u] - labels[v]) for u, v in edges]
    assert len(internal) == N
    assert len(set(internal)) == N
    assert set(internal) == irange(k + 1, k + N)

    attach = [k + 1 + labels[r] for r in roots]
    assert len(set(attach)) == c
    assert set(attach) == irange(k + N + 1, k + s)

    all_new = internal + attach
    assert len(all_new) == s
    assert len(set(all_new)) == s
    assert set(all_new) == irange(k + 1, k + s)

    K = k + s - c
    assert K == k + N
    assert labels[("R", k)] == K
    assert 2 * K + 1 == (2 * h - 1) * (2 * k + 1)
    return A


def sum_obstruction(c, h, k):
    """Return actual and required internal-difference sums under suffix-root labels."""
    assert c >= 1 and h >= 2 and k >= 0
    t = h - 1
    N = c * t
    sum_roots = c * N + c * (c - 1) // 2
    sum_leaves = N * (N - 1) // 2
    actual = t * sum_roots - sum_leaves
    required = N * (2 * k + N + 1) // 2
    # Avoid relying on parity in the displayed half-factor formula.
    assert 2 * (actual - required) == c * (h - 1) * (c - 2 * k - 1)
    assert (actual == required) == (c == 2 * k + 1)
    return actual, required


def edge_difference_map(edges, labels):
    out = {}
    for u, v in edges:
        d = abs(labels[u] - labels[v])
        assert d not in out, ("duplicate difference", d, out[d], (u, v))
        out[d] = (u, v)
    return out


def crossing_vector(edges, labels, threshold):
    by_diff = edge_difference_map(edges, labels)
    if not by_diff:
        return []
    m = max(by_diff)
    assert set(by_diff) == set(range(1, m + 1))
    vec = []
    for d in range(1, m + 1):
        u, v = by_diff[d]
        cross = (labels[u] < threshold) != (labels[v] < threshold)
        vec.append(int(cross))
    return vec


def low_base(k):
    root = ("O", "r")
    labels = {root: 0}
    edges = []
    if k > 0:
        for d in range(1, k + 1):
            leaf = ("O", "l", d)
            labels[leaf] = d
            edges.append((root, leaf))
    L = k + 1
    assert set(labels.values()) == set(range(k + 1))
    assert set(edge_difference_map(edges, labels)) == irange(1, k)
    assert crossing_vector(edges, labels, L) == [0] * k
    assert labels[root] == L - k - 1
    return root, labels, edges, L


def high_base(k):
    root = ("O", "r")
    labels = {root: k}
    edges = []
    if k > 0:
        for i in range(k):
            leaf = ("O", "l", i)
            labels[leaf] = i
            edges.append((root, leaf))
    L = 0
    assert set(labels.values()) == set(range(k + 1))
    assert set(edge_difference_map(edges, labels)) == irange(1, k)
    assert crossing_vector(edges, labels, L) == [0] * k
    assert labels[root] == L + k
    return root, labels, edges, L


def graft_and_check(k, h, branch):
    A = check_absorber(k, h)
    c, s, N = A["c"], A["s"], A["N"]
    lam, roots, fedges = A["labels"], A["roots"], A["edges"]
    K = k + N

    if branch == "low":
        old_root, old_labels, old_edges, L = low_base(k)
        labels = dict(old_labels)
        # L is above every old label in this base, so the block insertion shifts none.
        for v, x in lam.items():
            labels[("F",) + v] = L + x
        edges = list(old_edges)
        edges.extend((("F",) + u, ("F",) + v) for u, v in fedges)
        edges.extend((old_root, ("F",) + r) for r in roots)
        threshold = L
        new_root = ("F", "R", k)
        assert labels[new_root] == threshold + K
    elif branch == "high":
        old_root, old_labels, old_edges, L = high_base(k)
        labels = {v: x + s for v, x in old_labels.items()}
        for v, x in lam.items():
            labels[("F",) + v] = L + (s - 1 - x)
        edges = list(old_edges)
        edges.extend((("F",) + u, ("F",) + v) for u, v in fedges)
        edges.extend((old_root, ("F",) + r) for r in roots)
        threshold = L + s
        new_root = ("F", "R", k)
        assert labels[new_root] == threshold - K - 1
    else:
        raise ValueError(branch)

    total_edges = k + s
    assert len(labels) == total_edges + 1
    assert set(labels.values()) == set(range(total_edges + 1))
    by_diff = edge_difference_map(edges, labels)
    assert set(by_diff) == set(range(1, total_edges + 1))
    vec = crossing_vector(edges, labels, threshold)
    assert vec == [0] * K + [1] * (total_edges - K)
    return total_edges, K


def pinned_augmentation_check(k, h):
    A = check_absorber(k, h)
    lam, roots, fedges, s = A["labels"], A["roots"], A["edges"], A["s"]
    apex = ("A",)
    labels = {apex: 0}
    edges = []
    for i in range(1, k + 1):
        p = ("P", i)
        labels[p] = i
        edges.append((apex, p))
    for v, x in lam.items():
        labels[("F",) + v] = k + 1 + x
    edges.extend((("F",) + u, ("F",) + v) for u, v in fedges)
    edges.extend((apex, ("F",) + r) for r in roots)
    m = k + s
    assert set(labels.values()) == set(range(m + 1))
    assert set(edge_difference_map(edges, labels)) == set(range(1, m + 1))
    return m


def tiny_exhaustive_check():
    """For k=1,h=2 compare c=2 failure with c=3 constructive success."""
    k = 1
    h = 2
    # c=2: roots forced to labels 2,3; leaves 0,1. No matching gives {2,3}.
    roots = [2, 3]
    leaves = [0, 1]
    successes = 0
    for perm in permutations(leaves):
        ds = {roots[i] - perm[i] for i in range(2)}
        if ds == {2, 3}:
            successes += 1
    assert successes == 0
    # c=3 is the theorem's c=2k+1 case.
    A = check_absorber(1, 2)
    assert A["c"] == 3
    return successes


def main():
    absorber_cases = 0
    graft_cases = 0
    pinned_cases = 0
    sum_cases = 0

    # Closed-form construction and both transfer branches.
    for k in range(0, 21):
        for h in range(2, 21):
            check_absorber(k, h)
            absorber_cases += 1
            pinned_augmentation_check(k, h)
            pinned_cases += 1
            graft_and_check(k, h, "low")
            graft_and_check(k, h, "high")
            graft_cases += 2

    # Exact necessity identity on a broader independent parameter grid.
    for c in range(1, 42):
        for h in range(2, 18):
            for k in range(0, 21):
                sum_obstruction(c, h, k)
                sum_cases += 1

    tiny = tiny_exhaustive_check()

    print("PASS")
    print("absorber_cases", absorber_cases)
    print("pinned_augmentation_cases", pinned_cases)
    print("graft_transfer_cases", graft_cases)
    print("sum_identity_cases", sum_cases)
    print("tiny_c2_successes", tiny)
    print("max_k", 20)
    print("max_h_construction", 20)
    print("max_c_sum_grid", 41)


if __name__ == "__main__":
    main()
