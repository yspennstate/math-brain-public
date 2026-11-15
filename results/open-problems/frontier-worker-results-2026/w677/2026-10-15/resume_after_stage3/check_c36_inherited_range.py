"""Exact rational algebra and independent finite combinatorics for C36 v1."""
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path


def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def scale(a, c):
    return [c * x for x in a]


def power(a, k):
    out = [Q(1)]
    for _ in range(k):
        out = mul(out, a)
    return out


def ev(a, x):
    out = Q(0)
    for c in reversed(a):
        out = out * x + c
    return out


def main():
    p = Q(1, 5)
    P = [Q(1250), Q(-2125), Q(600), Q(240), Q(48)]
    f = [Q(2, 5), Q(8, 25), Q(24, 125), Q(48, 625), Q(48, 3125)]
    assert add(f, [0, -1]) == scale(P, Q(1, 3125))
    u = [Q(1), Q(-1)]
    low = add(add([13], scale(u, 13)), scale(power(u, 2), 1176))
    low = add(low, scale(mul(power(u, 2), [0, 1]), 432))
    low = add(low, scale(power(u, 4), 48))
    assert low == P
    t = [Q(-1), Q(1)]
    high = add(scale(power(t, 4), 48), scale(power(t, 3), 432))
    high = add(high, scale(power(t, 2), 1595))
    high = add(high, scale(power([Q(-3, 2), Q(1)], 2), 13))
    high = add(high, [Q(39, 4)])
    assert high == P
    # Enumerate actual ordered-child excursion paths, not falling factorials.
    total = Q(0)
    paths = set()
    counts = []
    for k in range(5):
        count = 0
        for choices in itertools.permutations(range(4), k):
            path = [(0,)]
            for child in choices:
                path.extend([(0, child), (0,)])
            path.append(())
            path = tuple(path)
            assert path not in paths
            paths.add(path)
            distinct_nonroot = len(set(path) - {()})
            steps = len(path) - 1
            total += 2 ** distinct_nonroot * p ** steps
            count += 1
        counts.append(count)
    assert counts == [1, 4, 12, 24, 24]
    assert len(paths) == 65
    assert total == ev(f, ev(f, Q(0)))
    # Independent tree-size count polynomial; x marks occupied vertices.
    a = [Q(0)]
    y = Q(0)
    sizes = []
    for height in range(1, 5):
        summed = [Q(0)]
        for k, count in enumerate(counts):
            summed = add(summed, scale(power(a, k), count))
        a = [Q(0)] + summed
        mass = sum((c * 2 ** n * p ** (2 * n - 1)
                    for n, c in enumerate(a) if n), Q(0))
        y = ev(f, y)
        assert mass == y
        assert y >= height * Q(39, 12500)
        sizes.append({"height": height, "largest_tree_vertices": len(a) - 1,
                      "weighted_mass": str(y), "size_count_terms": len(a)})
    proof = Path("proofs/C36_inherited_range_obstruction_v1.md")
    record = {"status": "PASS_exact_checks", "rigorous_arithmetic": True,
              "scope": "rational identities and finite excursion enumeration; global probability argument is the written unaudited proof",
              "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "certified_polynomial_lower_bound": "39/4 for y>=0, by the two written nonnegative decompositions",
              "iteration_drift": "39/12500", "explicit_excursions": len(paths),
              "child_order_counts": counts, "height_checks": sizes,
              "lean_compiled": False, "ordinary_T4_classification": "OPEN"}
    Path("C36_EXACT_CHECKS.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in record.items() if k != "height_checks"}))


if __name__ == "__main__":
    main()
