"""Independent exact controls for C0048 peer review. No store access or writes."""

from decimal import Decimal, localcontext
from fractions import Fraction
from collections import Counter
import json


def component_count(mask):
    parent = list(range(3))

    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for bit, (u, v) in enumerate(((0, 1), (1, 2), (2, 0))):
        if mask & (1 << bit):
            parent[root(u)] = root(v)
    return len({root(x) for x in range(3)})


def ladder_components_and_root_reach(mask):
    # Independent BFS implementation, not the author's union-find checker.
    edges = ((0, 1), (2, 3), (4, 5), (0, 2), (1, 3), (2, 4), (3, 5))
    adj = [set() for _ in range(6)]
    for i, (u, v) in enumerate(edges):
        if mask & (1 << i):
            adj[u].add(v)
            adj[v].add(u)
    seen = set()
    components = 0
    root_reaches_end = False
    for start in range(6):
        if start in seen:
            continue
        components += 1
        frontier = [start]
        group = set()
        while frontier:
            u = frontier.pop()
            if u in group:
                continue
            group.add(u)
            frontier.extend(adj[u] - group)
        seen.update(group)
        if 0 in group and (4 in group or 5 in group):
            root_reaches_end = True
    return components, root_reaches_end


def main():
    # p=1/2 makes every triangle edge configuration's p factor equal.
    weights = [3 ** component_count(mask) for mask in range(8)]
    total = sum(weights)
    single = Fraction(sum(weights[m] for m in range(8) if m & 1), total)
    pair = Fraction(sum(weights[m] for m in range(8) if m & 3 == 3), total)
    assert (total, single, pair) == (66, Fraction(3, 11), Fraction(1, 11))
    assert pair > single * single  # Marginals cannot simply be multiplied.
    assert pair <= Fraction(1, 4)  # w462's conditional p^2 bound.

    # The two cuts are the two pairs of longitudinal ladder edges.
    first_cut, second_cut = 0b0011000, 0b1100000
    polynomial = Counter()
    z = closed_first = closed_second = closed_both = ordinary = 0
    for mask in range(128):
        k, root_reaches_end = ladder_components_and_root_reach(mask)
        polynomial[k] += 1
        weight = 3**k
        z += weight
        closed_first += weight * (mask & first_cut == 0)
        closed_second += weight * (mask & second_cut == 0)
        closed_both += weight * (mask & (first_cut | second_cut) == 0)
        ordinary += weight * root_reaches_end
    assert dict(polynomial) == {6: 1, 5: 7, 4: 21, 3: 37, 2: 39, 1: 23}
    assert (z, closed_first, closed_second, closed_both) == (5550, 3096, 3096, 1728)
    cut_marginal = Fraction(z - closed_first, z)
    cut_joint = Fraction(z - closed_first - closed_second + closed_both, z)
    assert (cut_marginal, cut_joint) == (Fraction(409, 925), Fraction(181, 925))
    assert cut_joint - cut_marginal**2 == Fraction(144, 855625)
    assert Fraction(ordinary, z) == Fraction(88, 925)

    with localcontext() as ctx:
        ctx.prec = 70
        log2, log3 = Decimal(2).ln(), Decimal(3).ln()
        barrier = log3 - Decimal(19) * log2 / Decimal(12)
        allowance_d3_lower = 4 * log2 / 9
        threshold = 4 * log2 / (3 * barrier)
        assert barrier > 0
        assert 3**12 - 2**19 == 7153
        assert 3**(12*818) <= 2**(19*818+16)
        assert 3**(12*819) > 2**(19*819+16)
        assert Decimal(818) < threshold < Decimal(819)
        result = {
            "triangle_q3_p_half": {
                "partition_integer_weight": total,
                "P_edge": str(single),
                "P_two_edges": str(pair),
                "product_of_marginals": str(single * single),
                "conditional_P_second_given_first": str(pair / single),
                "w462_conditional_product_upper": "1/4",
            },
            "ladder_q3_p_half": {
                "partition_polynomial_coefficients_by_cluster_count": dict(sorted(polynomial.items(), reverse=True)),
                "partition_integer_weight": z,
                "closed_first_cut_weight": closed_first,
                "closed_both_cuts_weight": closed_both,
                "P_each_cut_crossed": str(cut_marginal),
                "P_both_cuts_crossed": str(cut_joint),
                "joint_minus_marginal_product": str(cut_joint - cut_marginal**2),
                "ordinary_root_to_end_path_probability": str(Fraction(ordinary, z)),
            },
            "w463_barrier": {
                "exact": "log(3)-(19/12)log(2)",
                "decimal": str(barrier),
                "integer_positivity_difference": 7153,
                "d3_BC_allowance_lower": str(allowance_d3_lower),
                "allowance_to_barrier_lower_ratio": str(allowance_d3_lower / barrier),
                "necessary_dimension_threshold": str(threshold),
                "integer_adjacent_check": "fails at 818; passes at 819",
            },
        }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
