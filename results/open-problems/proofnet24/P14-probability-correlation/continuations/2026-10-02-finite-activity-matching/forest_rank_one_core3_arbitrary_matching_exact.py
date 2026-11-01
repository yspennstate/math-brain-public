"""Exact checks for a three-vertex core, rank-one spokes, arbitrary matching.

Independent routes: original-graph subset enumeration for small cases;
explicit five-state connectivity transitions for arbitrary terminal counts;
the separate claimed nilpotent-exponential/Rayleigh certificate.
"""
from fractions import Fraction as F
from pathlib import Path
import json


STATES = ((0, 1, 2), (0, 0, 1), (0, 1, 0), (0, 1, 1), (0, 0, 0))


def core_data(columns, core):
    b0, b1, b2 = map(F, columns)
    p, q, r = map(F, core)
    B, J = b0 + b1 + b2, b0 * b1 * b2
    S = 1 + p + q + r + p * q + p * r + q * r
    L = b0 * b1 + b0 * b2 + b1 * b2
    L += p * b2 * (b0 + b1) + q * b1 * (b0 + b2) + r * b0 * (b1 + b2)
    assert L ** 2 - 2 * B * J * S > 0
    assert B * L > J
    return B, J, S, L


def formula_coefficients(rows, columns, core, other_matching):
    rows = list(map(F, rows))
    B, J, S, L = core_data(columns, core)
    d = lambda x: 1 + B * x
    alpha = lambda x: x ** 2 / d(x)
    gamma = lambda x: x ** 3 / d(x) ** 2
    D, U, G = F(1), F(0), F(0)
    occupied = set()
    for i, j, activity in other_matching:
        assert i >= 4 and j >= 4 and i != j
        assert i not in occupied and j not in occupied
        occupied.update((i, j))
        a, b, w = rows[i], rows[j], F(activity)
        assert w >= 0
        split, contracted = d(a) * d(b), d(a + b)
        K = split + w * contracted
        theta = w * contracted / K
        u0, u1 = alpha(a) + alpha(b), alpha(a + b)
        g0, g1 = gamma(a) + gamma(b), gamma(a + b)
        delta = u1 - u0
        effective_u = (1 - theta) * u0 + theta * u1
        effective_g = (1 - theta) * g0 + theta * g1 + B * theta * (1 - theta) * delta ** 2
        assert 0 <= effective_g <= effective_u / B
        D *= K
        U += effective_u
        G += effective_g
    for i, a in enumerate(rows):
        if i not in occupied:
            D *= d(a)
            U += alpha(a)
            G += gamma(a)
    base = S + L * U + J * G + B * J * U ** 2
    changes = []
    for i, j in ((0, 1), (2, 3)):
        a, b = rows[i], rows[j]
        delta = alpha(a + b) - alpha(a) - alpha(b)
        epsilon = gamma(a + b) - gamma(a) - gamma(b)
        factor = d(a + b) / (d(a) * d(b))
        increment = delta * (L + 2 * B * J * U) + J * epsilon + B * J * delta ** 2
        assert delta > 0 and epsilon > 0
        changes.append((delta, factor, increment))
    de, ce, Xe = changes[0]
    df, cf, Xf = changes[1]
    coefficients = [D * base, D * ce * (base + Xe), D * cf * (base + Xf),
                    D * ce * cf * (base + Xe + Xf + 2 * B * J * de * df)]
    rayleigh = D ** 2 * ce * cf * (Xe * Xf - 2 * B * J * de * df * base)
    assert 0 <= G <= U / B
    assert (L + 2 * B * J * U) ** 2 - 2 * B * J * base > 0
    assert rayleigh == coefficients[1] * coefficients[2] - coefficients[0] * coefficients[3] > 0
    return coefficients, rayleigh


def canonical(state):
    names = {}
    return tuple(names.setdefault(v, len(names)) for v in state)


def terminal_transfer(frontier, activity, columns):
    """Actual subset choices on the three spokes; no exponential formula."""
    following = {}
    activity = F(activity)
    columns = list(map(F, columns))
    for state, weight in frontier.items():
        for mask in range(8):
            indices = [i for i in range(3) if mask >> i & 1]
            selected = [state[i] for i in indices]
            if len(selected) != len(set(selected)):
                continue
            if selected:
                selected_set = set(selected)
                target = canonical([selected[0] if v in selected_set else v for v in state])
            else:
                target = state
            term = weight
            for i in indices:
                term *= activity * columns[i]
            following[target] = following.get(target, F(0)) + term
    return following


def frontier_forest_sum(rows, columns, core, other_matching, contracts):
    p, q, r = map(F, core)
    frontier = dict(zip(STATES, (F(1), p, q, r, p * q + p * r + q * r)))
    used = set()
    for pair, is_contracted in zip(((0, 1), (2, 3)), contracts):
        i, j = pair
        used.update(pair)
        if is_contracted:
            frontier = terminal_transfer(frontier, rows[i] + rows[j], columns)
        else:
            frontier = terminal_transfer(terminal_transfer(frontier, rows[i], columns), rows[j], columns)
    for i, j, w in other_matching:
        used.update((i, j))
        split = terminal_transfer(terminal_transfer(frontier, rows[i], columns), rows[j], columns)
        contracted = terminal_transfer(frontier, rows[i] + rows[j], columns)
        frontier = {state: split.get(state, F(0)) + F(w) * contracted.get(state, F(0))
                    for state in set(split) | set(contracted)}
    for i, activity in enumerate(rows):
        if i not in used:
            frontier = terminal_transfer(frontier, activity, columns)
    return sum(frontier.values(), F(0))


def frontier_coefficients(rows, columns, core, other_matching):
    rows = list(map(F, rows))
    return [frontier_forest_sum(rows, columns, core, other_matching, contracts)
            for contracts in ((False, False), (True, False), (False, True), (True, True))]


def direct_subset_coefficients(rows, columns, core, other_matching):
    m, n = len(rows), len(rows) + 3
    rows, columns, core = [list(map(F, values)) for values in (rows, columns, core)]
    p, q, r = core
    edges = [(m, m + 1, p), (m, m + 2, q), (m + 1, m + 2, r)]
    edges += [(j, m + i, a * b) for j, a in enumerate(rows) for i, b in enumerate(columns)]
    edges += [(i, j, F(w)) for i, j, w in other_matching]
    totals = [F(0)] * 4
    for mask in range(1 << len(edges)):
        if mask.bit_count() > n - 1:
            continue
        parent = list(range(n))

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        weight = F(1)
        for k, (u, v, w) in enumerate(edges):
            if mask >> k & 1:
                if not w:
                    break
                u, v = root(u), root(v)
                if u == v:
                    break
                parent[u] = v
                weight *= w
        else:
            totals[0] += weight
            u, v, x, y = (root(i) for i in range(4))
            if u != v:
                totals[1] += weight
            if x != y:
                totals[2] += weight
            if u != v and x != y and {u, v} != {x, y}:
                totals[3] += weight
    return totals


def encode_case(rows, columns, core, matching, coefficients, rayleigh):
    return {"m": len(rows), "rows": list(map(str, rows)), "columns": list(map(str, columns)),
            "core_p_q_r": list(map(str, core)),
            "other_matching": [[i, j, str(w)] for i, j, w in matching],
            "A_Be_Bf_C": list(map(str, coefficients)), "rayleigh": str(rayleigh)}


def main():
    direct_cases = [
        ([1, 2, 3, 4], [2, 3, 5], [2, 3, 5], []),
        ([F(1, 2), F(2, 3), F(3, 4), F(4, 5)], [F(1, 2), F(2, 3), F(3, 4)], [F(1, 3), F(2, 5), 0], []),
        ([1, 2, 1, 3, 2], [2, 1, 3], [1, 2, 3], []),
    ]
    results = {"original_graph_subset_checks": [], "explicit_frontier_checks": []}
    for rows, columns, core, matching in direct_cases:
        direct = direct_subset_coefficients(rows, columns, core, matching)
        frontier = frontier_coefficients(rows, columns, core, matching)
        formula, rayleigh = formula_coefficients(rows, columns, core, matching)
        assert direct == frontier == formula
        row = encode_case(rows, columns, core, matching, direct, rayleigh)
        results["original_graph_subset_checks"].append(row)
        print(row, flush=True)
    frontier_cases = [
        ([1, 2, 3, 4, 5, 6], [2, 3, 5], [2, 3, 5], [(4, 5, 2)]),
        ([F(1, 2), F(2, 3), F(3, 4), F(4, 5), 0, 2], [F(1, 2), F(2, 3), F(3, 4)], [F(1, 3), F(2, 5), 0], [(4, 5, F(7, 3))]),
    ]
    for m in (8, 10, 25, 100):
        rows = [F(1 + j % 7, 1 + j % 5) for j in range(m)]
        matching = [(j, j + 1, F(j + 1, j + 3)) for j in range(4, m - 1, 2)]
        frontier_cases.append((rows, [F(2, 3), F(5, 7), F(11, 13)], [F(2, 5), 0, F(7, 11)], matching))
    for rows, columns, core, matching in frontier_cases:
        frontier = frontier_coefficients(rows, columns, core, matching)
        formula, rayleigh = formula_coefficients(rows, columns, core, matching)
        assert frontier == formula
        results["explicit_frontier_checks"].append(encode_case(rows, columns, core, matching, frontier, rayleigh))
        print("Exact arbitrary-matching rank-one frontier check passed for m=" + str(len(rows)), flush=True)
    Path(__file__).with_name("forest_rank_one_core3_arbitrary_matching_exact_results.json").write_text(json.dumps(results, indent=2) + "\n")


if __name__ == "__main__":
    main()
