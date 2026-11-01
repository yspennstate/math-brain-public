from itertools import combinations, permutations


def exact_selector(n, k, edges, order=None):
    """Exact checker for the degree-binomial(k,2) signed selector theorem.

    The proof-level polynomial is
        I_j = product_{e in E(S_j)} Y_e,
        h_j = w_j (I_j - 2 * sum_{ell<j} I_ell),
        f_i = sum_{j:i in S_j} h_j,
    with geometrically decreasing positive weights w_j.
    On Boolean inputs, thresholding f_i at 1 should return exactly the first
    k-clique in the chosen candidate ordering, or the empty set if none exists.
    All arithmetic here is integer/exact.
    """
    subsets = list(combinations(range(n), k))
    if order is not None:
        subsets = [subsets[i] for i in order]

    M = len(subsets)
    R = 8 * M * M
    indicators = [
        int(all(tuple(sorted(e)) in edges for e in combinations(S, 2)))
        for S in subsets
    ]
    weights = [2 * (R ** (M - 1 - j)) for j in range(M)]

    prefix = 0
    h = []
    for j in range(M):
        h_j = weights[j] * (indicators[j] - 2 * prefix)
        h.append(h_j)
        prefix += indicators[j]

    f = [
        sum(h[j] for j, S in enumerate(subsets) if i in S)
        for i in range(n)
    ]
    threshold_set = {i for i, value in enumerate(f) if value >= 1}

    first_clique = set()
    for j, value in enumerate(indicators):
        if value:
            first_clique = set(subsets[j])
            break

    return threshold_set, first_clique


def all_graphs(n):
    edges = list(combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        yield {
            edges[j]
            for j in range(len(edges))
            if (mask >> j) & 1
        }


def main():
    for n, k in [(4, 2), (5, 3)]:
        total = 0
        for E in all_graphs(n):
            A, first = exact_selector(n, k, E)
            assert A == first, (n, k, E, A, first)
            total += 1
        print(f"PASS all {total} graphs for n={n}, k={k}")

    n, k = 4, 2
    subsets = list(combinations(range(n), k))
    orders = 0
    graph_count = 1 << len(list(combinations(range(n), 2)))
    for order in permutations(range(len(subsets))):
        for E in all_graphs(n):
            A, first = exact_selector(n, k, E, order)
            assert A == first, (order, E, A, first)
        orders += 1
    print(
        f"PASS all {orders} candidate orderings x {graph_count} graphs "
        f"for n={n},k={k}"
    )
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
