"""Exact eight-configuration controls for the conditional-cutset audit."""
from fractions import Fraction as Q
import itertools
import json
from pathlib import Path


def wired_path_distribution(q):
    # Physical path -1--0--1--2. The two end vertices are wired together.
    edges = [(0, 1), (1, 2), (2, 3)]
    weights = []
    for bits in itertools.product([0, 1], repeat=3):
        roots = list(range(4))

        def root(i):
            while roots[i] != i:
                i = roots[i]
            return i

        def union(i, j):
            roots[root(i)] = root(j)

        union(0, 3)
        for bit, (a, b) in zip(bits, edges):
            if bit:
                union(a, b)
        clusters = len({root(i) for i in range(4)})
        weights.append((bits, Q(q)**clusters, root(1) == root(3)))
    normalizer = sum(weight for _, weight, _ in weights)
    def event(predicate):
        return sum(weight for bits, weight, connected in weights if predicate(bits, connected)) / normalizer
    return {
        "ordinary_right": event(lambda bits, connected: bits[1] and bits[2]),
        "wired_right": event(lambda bits, connected: connected),
        "A1": event(lambda bits, connected: bits[0]),
        "A2": event(lambda bits, connected: bits[1] or bits[2]),
        "intersection": event(lambda bits, connected: bits[0] and (bits[1] or bits[2])),
    }


def run():
    p = Q(1, 2)
    results = []
    for q in [1, 3]:
        values = wired_path_distribution(q)
        assert values["ordinary_right"] <= p*p
        assert values["wired_right"] > p*p
        assert values["intersection"] <= p*(1-(1-p)**2)
        if q == 1:
            assert values["intersection"] == p*(1-(1-p)**2)
        else:
            assert values["wired_right"] == Q(7, 22)
            assert values["ordinary_right"] == Q(1, 11)
            assert values["intersection"] == Q(3, 22)
            assert values["A1"]*values["A2"] == Q(15, 121)
            assert values["intersection"] > values["A1"]*values["A2"]
        results.append({"q": q, "configurations": 8, **{key: str(value) for key, value in values.items()}, "valid_conditional_product_upper": str(p*(1-(1-p)**2)), "ordinary_two_cut_upper": str(p*p)})
    overlapping_actual = p
    overlapping_invalid_upper = p*p
    assert overlapping_actual > overlapping_invalid_upper
    q_below_one = Q(1, 2)
    single_edge_open = p / (p+q_below_one*(1-p))
    assert single_edge_open == Q(2, 3) > p
    receipt = {
        "finite_path_controls": results,
        "overlap_counterexample": {"q": 1, "p": "1/2", "same_edge_used_twice_actual": str(overlapping_actual), "invalid_product": str(overlapping_invalid_upper)},
        "q_below_one_counterexample": {"q": "1/2", "p": "1/2", "free_single_edge_open": str(single_edge_open), "invalid_upper": str(p)},
        "scientific_role": "Exact finite controls for assumptions; the written uniform-conditional argument proves the general scoped inequality.",
    }
    Path(__file__).with_name("PEER_AUDIT_MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    run()
