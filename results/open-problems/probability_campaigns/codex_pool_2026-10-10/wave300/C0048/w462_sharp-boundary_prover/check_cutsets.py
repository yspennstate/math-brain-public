"""Bounded, exact FK check. This is a regression receipt, not a formal proof."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import platform
import time

ROOT = Path(__file__).resolve().parent
EDGES = [(0, 1), (2, 3), (4, 5), (0, 2), (1, 3), (2, 4), (3, 5)]
CUTS = [(1 << 3) | (1 << 4), (1 << 5) | (1 << 6)]
PARTITIONS = {
    "free": [],
    "wired_both_ends": [[0, 1, 4, 5]],
    "wired_each_end_separately": [[0, 1], [4, 5]],
}


def components(mask, groups=()):
    parent = list(range(6))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    for group in groups:
        for x in group[1:]:
            union(group[0], x)
    for i, (x, y) in enumerate(EDGES):
        if mask & (1 << i):
            union(x, y)
    return [find(x) for x in range(6)]


def as_fraction(x):
    return f"{x.numerator}/{x.denominator}"


def main():
    gate = json.loads((ROOT / "compute_gate.json").read_text(encoding="utf-8"))
    started = time.perf_counter()
    count = defaultdict(int)
    measurements = []
    witnesses = []
    for q, p_text, (bc, groups) in product(
        gate["q_values"], gate["p_values"], PARTITIONS.items()
    ):
        p = Fraction(p_text)
        a, b = p.numerator, p.denominator - p.numerator
        weights = []
        for mask in range(1 << len(EDGES)):
            k = len(set(components(mask, groups)))
            n = mask.bit_count()
            weights.append(a**n * b ** (len(EDGES) - n) * q**k)
        count["weighted_configurations"] += len(weights)
        assert count["weighted_configurations"] <= gate["max_enumerated_weighted_configurations"]
        assert len(weights) <= gate["max_states_per_measure"]
        total = sum(weights)
        rho = 1 - (1 - p) ** 2

        for e, (x, y) in enumerate(EDGES):
            bit = 1 << e
            for mask in range(len(weights)):
                if mask & bit:
                    continue
                observed = Fraction(weights[mask | bit], weights[mask] + weights[mask | bit])
                cc = components(mask, groups)
                expected = p if cc[x] == cc[y] else p / (p + q * (1 - p))
                assert observed == expected and observed <= p, (q, p_text, bc, e, mask)
                count["single_edge_conditionals"] += 1

        for cut in CUTS:
            conditional = defaultdict(lambda: [0, 0])
            for mask, weight in enumerate(weights):
                row = conditional[mask & ~cut]
                row[1] += weight
                if not mask & cut:
                    row[0] += weight
            for closed, denominator in conditional.values():
                assert Fraction(closed, denominator) >= (1 - p) ** cut.bit_count()
                count["full_cut_conditionals"] += 1

        for i, cut in enumerate(CUTS):
            for history in product([False, True], repeat=i):
                denominator = closed = 0
                for mask, weight in enumerate(weights):
                    if all(bool(mask & CUTS[j]) == value for j, value in enumerate(history)):
                        denominator += weight
                        if not mask & cut:
                            closed += weight
                assert denominator > 0
                assert Fraction(closed, denominator) >= (1 - p) ** cut.bit_count()
                count["partial_history_conditionals"] += 1

        marginals = [
            Fraction(sum(w for mask, w in enumerate(weights) if mask & cut), total)
            for cut in CUTS
        ]
        joint = Fraction(
            sum(w for mask, w in enumerate(weights) if all(mask & cut for cut in CUTS)), total
        )
        assert joint <= rho**2
        count["joint_product_upper_bounds"] += 1
        if q == 1:
            assert joint == rho**2 == marginals[0] * marginals[1]
            count["bernoulli_sharp_equalities"] += 1

        ordinary_numerator = 0
        for mask, weight in enumerate(weights):
            # Deliberately omit the boundary partition here: physical paths use only E.
            cc = components(mask)
            if cc[0] in (cc[4], cc[5]):
                ordinary_numerator += weight
        ordinary_path = Fraction(ordinary_numerator, total)
        assert ordinary_path <= rho**2
        count["ordinary_path_upper_bounds"] += 1
        if bc == "wired_both_ends":
            assert all(components(mask, groups)[0] == components(mask, groups)[4]
                       for mask in range(len(weights)))
            assert ordinary_path < 1
            count["boundary_identification_distinguished_from_path"] += 1

        invalid_bound = marginals[0] * marginals[1]
        fails = joint > invalid_bound
        count["invalid_marginal_product_failures"] += int(fails)
        count["invalid_marginal_product_cases"] += 1
        row = {
            "q": q, "p": p_text, "boundary": bc,
            "cut_marginals": [as_fraction(x) for x in marginals],
            "joint_crossed_cuts": as_fraction(joint),
            "marginal_product": as_fraction(invalid_bound),
            "correct_conditional_upper_bound": as_fraction(rho**2),
            "ordinary_path_probability": as_fraction(ordinary_path),
        }
        measurements.append(row)
        if q == 3 and p == Fraction(1, 2) and bc == "free":
            assert fails, "Required genuine, disjoint-cut dependence witness absent"
            row["positive_excess"] = as_fraction(joint - invalid_bound)
            witnesses.append(row)
    elapsed = time.perf_counter() - started
    assert elapsed < gate["timeout_seconds"]
    assert len(witnesses) == 1
    result = {
        "status": "PASS", "formal_check": False,
        "command": "python -X utf8 ~/brain_workers/w462/check_cutsets.py",
        "python_version": platform.python_version(), "elapsed_seconds": elapsed,
        "arithmetic": "integers and fractions; no floating point in mathematical checks",
        "counts": dict(count), "witness": witnesses[0], "measurements": measurements,
        "proof_scope": "Finite ladder regressions only. General L1-L3 are proved in ATTEMPT.md, pending independent review.",
    }
    (ROOT / "CHECK_RESULTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["status", "elapsed_seconds", "counts", "witness"]}, indent=2))


if __name__ == "__main__":
    main()
