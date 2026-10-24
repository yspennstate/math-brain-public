from fractions import Fraction
from itertools import combinations


def graph_from_edges(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def direct_minimum_horizon_cover_probability(adj, start=0):
    """Exact P_start(C <= n-1) by enumerating all length-(n-1) walks."""
    n = len(adj)
    total = Fraction(0, 1)

    def rec(v, step, seen, prob):
        nonlocal total
        if step == n - 1:
            if len(seen) == n:
                total += prob
            return
        for w in adj[v]:
            rec(
                w,
                step + 1,
                seen | {w},
                prob * Fraction(1, len(adj[v])),
            )

    rec(start, 0, {start}, Fraction(1, 1))
    return total


def hamiltonian_path_weight(adj, start=0):
    """Sum product 1/deg(v_k) over oriented Hamilton paths starting at start."""
    n = len(adj)
    count = 0
    total = Fraction(0, 1)

    def rec(v, path, prob):
        nonlocal count, total
        if len(path) == n:
            count += 1
            total += prob
            return
        seen = set(path)
        for w in adj[v]:
            if w not in seen:
                rec(
                    w,
                    path + [w],
                    prob * Fraction(1, len(adj[v])),
                )

    rec(start, [start], Fraction(1, 1))
    return count, total


def run_case(name, adj, start=0):
    direct = direct_minimum_horizon_cover_probability(adj, start)
    hp_count, hp_weight = hamiltonian_path_weight(adj, start)
    assert direct == hp_weight

    degrees = {len(x) for x in adj}
    regular_check = "NA"
    if len(degrees) == 1:
        d = next(iter(degrees))
        expected = Fraction(hp_count, d ** (len(adj) - 1))
        assert hp_weight == expected
        regular_check = f"{hp_count}/{d}^{len(adj)-1}={expected}"

    print(
        f"{name}: hp_count={hp_count} hp_weight={hp_weight} "
        f"direct={direct} regular_formula={regular_check} PASS"
    )


def main():
    cases = {
        "P4": graph_from_edges(4, [(0, 1), (1, 2), (2, 3)]),
        "C4": graph_from_edges(4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
        "K4": graph_from_edges(4, list(combinations(range(4), 2))),
        "K3,3": graph_from_edges(
            6, [(a, b) for a in range(3) for b in range(3, 6)]
        ),
        "K1,3": graph_from_edges(4, [(0, 1), (0, 2), (0, 3)]),
    }
    for name, adj in cases.items():
        run_case(name, adj, 0)
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
