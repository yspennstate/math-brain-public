"""Exact independent checks for arbitrary terminal row activities.

Each terminal has three equal spoke activities within its row; different
rows may have arbitrary different positive activities.  This script uses
both direct subsets of the original uncontracted graph and an explicit
five-state connectivity transfer.  Neither calculation uses the claimed
nilpotent exponential formula to obtain A, B_e, B_f, or C.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


def alpha(x):
    return x ** 2 / (1 + 3 * x)


def gamma(x):
    return x ** 3 / (1 + 3 * x) ** 2


def formula_coefficients(rows, core):
    rows = [Q(x) for x in rows]
    p, q, r = map(Q, core)
    X, t = p + q + r, p * q + p * r + q * r
    L, S = 3 + 2 * X, 1 + X + t
    D = Q(1)
    for x in rows:
        D *= 1 + 3 * x
    U = sum(map(alpha, rows), Q(0))
    G = sum(map(gamma, rows), Q(0))
    F = S + L * U + G + 3 * U ** 2
    data = []
    for i, j in ((0, 1), (2, 3)):
        a, b = rows[i], rows[j]
        delta = alpha(a + b) - alpha(a) - alpha(b)
        epsilon = gamma(a + b) - gamma(a) - gamma(b)
        c = (1 + 3 * (a + b)) / ((1 + 3 * a) * (1 + 3 * b))
        increment = delta * (L + 6 * U) + epsilon + 3 * delta ** 2
        data.append((delta, epsilon, c, increment))
        assert delta > 0 and epsilon > 0
        assert delta == a * b * (2 + 3 * (a + b)) / ((1 + 3 * a) * (1 + 3 * b) * (1 + 3 * (a + b)))
    de, ee, ce, Xe = data[0]
    df, ef, cf, Xf = data[1]
    A = D * F
    Be, Bf = D * ce * (F + Xe), D * cf * (F + Xf)
    C = D * ce * cf * (F + Xe + Xf + 6 * de * df)
    rayleigh = D ** 2 * ce * cf * (Xe * Xf - 6 * de * df * F)
    assert rayleigh == Be * Bf - A * C
    assert 0 < G < U / 3
    assert (L + 6 * U) ** 2 - 6 * F > 0
    assert rayleigh > 0
    return [A, Be, Bf, C], rayleigh


def direct_subset_coefficients(rows, core):
    rows = list(map(Q, rows))
    p, q, r = map(Q, core)
    m = len(rows)
    n = m + 3
    edges = [(m, m + 1, p), (m, m + 2, q), (m + 1, m + 2, r)]
    edges += [(terminal, v, a) for terminal, a in enumerate(rows) for v in range(m, m + 3)]
    totals = [Q(0)] * 4
    for mask in range(1 << len(edges)):
        if mask.bit_count() > n - 1:
            continue
        parent = list(range(n))

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        weight = Q(1)
        for i, (u, v, w) in enumerate(edges):
            if mask >> i & 1:
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


def canonical(state):
    names = {}
    return tuple(names.setdefault(v, len(names)) for v in state)


def explicit_frontier_forest_sum(rows, core):
    """Actual connectivity transitions, without P, Q, alpha, or gamma."""
    p, q, r = map(Q, core)
    t = p * q + p * r + q * r
    frontier = {(0, 1, 2): Q(1), (0, 0, 1): p,
                (0, 1, 0): q, (0, 1, 1): r, (0, 0, 0): t}
    for a in map(Q, rows):
        following = {}
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
                following[target] = following.get(target, Q(0)) + weight * a ** len(indices)
        frontier = following
    return sum(frontier.values(), Q(0))


def explicit_frontier_coefficients(rows, core):
    a, b, c, d, *rest = map(Q, rows)
    return [explicit_frontier_forest_sum(rows, core),
            explicit_frontier_forest_sum([a + b, c, d] + rest, core),
            explicit_frontier_forest_sum([a, b, c + d] + rest, core),
            explicit_frontier_forest_sum([a + b, c + d] + rest, core)]


def encode_case(rows, core, coefficients, rayleigh):
    return {"m": len(rows), "rows": list(map(str, rows)), "core_p_q_r": list(map(str, core)),
            "A_Be_Bf_C": list(map(str, coefficients)), "rayleigh": str(rayleigh)}


def main():
    direct_cases = [
        ([1, 2, 3, 4], [2, 3, 5]),
        ([Q(1, 2), Q(2, 3), Q(3, 4), Q(4, 5)], [Q(1, 3), Q(2, 5), 0]),
        ([1, 2, 1, 3, 2], [1, 2, 3]),
    ]
    results = {"original_uncontracted_graph_checks": [], "explicit_frontier_checks": []}
    for rows, core in direct_cases:
        observed = direct_subset_coefficients(rows, core)
        formula, rayleigh = formula_coefficients(rows, core)
        frontier = explicit_frontier_coefficients(rows, core)
        assert observed == formula == frontier
        assert observed[1] * observed[2] - observed[0] * observed[3] == rayleigh > 0
        row = encode_case(rows, core, observed, rayleigh)
        results["original_uncontracted_graph_checks"].append(row)
        print(row, flush=True)
    for m in (4, 5, 6, 10, 25, 100):
        rows = [Q(1 + j % 7, 1 + j % 5) for j in range(m)]
        core = [Q(2, 3), Q(5, 7), Q(11, 13)]
        formula, rayleigh = formula_coefficients(rows, core)
        observed = explicit_frontier_coefficients(rows, core)
        assert observed == formula
        results["explicit_frontier_checks"].append(encode_case(rows, core, observed, rayleigh))
        print("Exact heterogeneous frontier check passed for m=" + str(m), flush=True)
    Path(__file__).with_name("forest_twin_matching_heterogeneous_core3_exact_results.json").write_text(json.dumps(results, indent=2) + "\n")


if __name__ == "__main__":
    main()
