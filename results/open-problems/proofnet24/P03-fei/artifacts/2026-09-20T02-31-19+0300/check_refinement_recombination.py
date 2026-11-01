#!/usr/bin/env python3
"""Sanity checker for the P03 hereditary-refinement/recombination theorem.

This is a finite numerical check only.  The universal theorem is proved in the
corresponding run report.  We exhaust all Boolean functions through n=3 and
sample 50 n=4 functions with a fixed seed.  For every nonempty physical block
A and every ordering of A we check

  0 <= H(Z_A | Z_C) - R_pi <= (2/ln 2) I_A,

and the exact chain decomposition of the refinement gap, up to floating point
roundoff.  Here R_pi is the accumulated singleton erasure entropy along the
physical restriction order pi.
"""

from collections import defaultdict
import itertools
import json
import math
import random
import sys


def assignments(n):
    return list(itertools.product((-1, 1), repeat=n))


def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0.0)


def walsh_spectrum(vals, n):
    xs = assignments(n)
    coeff = []
    for mask in range(1 << n):
        total = 0.0
        for x in xs:
            chi = 1
            for i in range(n):
                if (mask >> i) & 1:
                    chi *= x[i]
            total += vals[x] * chi
        coeff.append(total / (1 << n))
    return [a * a for a in coeff]


def conditional_entropy_bit(p, n, bit):
    groups = defaultdict(lambda: [0.0, 0.0])
    for mask, prob in enumerate(p):
        rest = mask & ~(1 << bit)
        groups[rest][(mask >> bit) & 1] += prob
    ans = 0.0
    for a, b in groups.values():
        m = a + b
        if a:
            ans -= a * math.log2(a / m)
        if b:
            ans -= b * math.log2(b / m)
    return ans


def conditional_entropy_subset(p, n, A):
    A = set(A)
    C = set(range(n)) - A
    joint = defaultdict(float)
    cond = defaultdict(float)
    for mask, prob in enumerate(p):
        joint[tuple((mask >> i) & 1 for i in sorted(A | C))] += prob
        cond[tuple((mask >> i) & 1 for i in sorted(C))] += prob
    return entropy(joint.values()) - entropy(cond.values())


def restrict_func(vals, n, fixed):
    remaining = [i for i in range(n) if i not in fixed]
    out = {}
    for xr in assignments(len(remaining)):
        full = [None] * n
        for i, value in fixed.items():
            full[i] = value
        for j, i in enumerate(remaining):
            full[i] = xr[j]
        out[xr] = vals[tuple(full)]
    return out, remaining


def influence_i(vals, n, i):
    count = 0
    for x in assignments(n):
        y = list(x)
        y[i] *= -1
        if vals[x] != vals[tuple(y)]:
            count += 1
    return count / (1 << n)


def coarse_erasure(vals, n, A):
    return conditional_entropy_subset(walsh_spectrum(vals, n), n, A)


def sequential_stage_terms(vals, n, order):
    terms = []
    for t, coord in enumerate(order):
        prefix = order[:t]
        stage = 0.0
        for xp in assignments(len(prefix)):
            fixed = dict(zip(prefix, xp))
            branch, remaining = restrict_func(vals, n, fixed)
            p = walsh_spectrum(branch, len(remaining))
            stage += conditional_entropy_bit(p, len(remaining), remaining.index(coord)) / (1 << len(prefix))
        terms.append(stage)
    return terms


def coarse_chain_terms(vals, n, order, A):
    p = walsh_spectrum(vals, n)
    A = set(A)
    C = set(range(n)) - A
    terms = []
    for t, coord in enumerate(order):
        future = set(order[t + 1 :]) | C
        joint_coords = future | {coord}
        joint = defaultdict(float)
        cond = defaultdict(float)
        for mask, prob in enumerate(p):
            joint[tuple((mask >> j) & 1 for j in sorted(joint_coords))] += prob
            cond[tuple((mask >> j) & 1 for j in sorted(future))] += prob
        terms.append(entropy(joint.values()) - entropy(cond.values()))
    return terms


def check_case(vals, n, A, order, state, tol=2e-10):
    coarse = coarse_erasure(vals, n, A)
    sequential_terms = sequential_stage_terms(vals, n, order)
    sequential = sum(sequential_terms)
    chain_terms = coarse_chain_terms(vals, n, order, A)
    gap = coarse - sequential
    I_A = sum(influence_i(vals, n, i) for i in A)
    identity_error = abs(gap - sum(a - b for a, b in zip(chain_terms, sequential_terms)))

    state["cases"] += 1
    state["min_refinement_gap"] = min(state["min_refinement_gap"], gap)
    state["max_chain_identity_error"] = max(state["max_chain_identity_error"], identity_error)
    if I_A > 1e-15:
        state["max_gap_over_I_A"] = max(state["max_gap_over_I_A"], gap / I_A)

    upper = (2.0 / math.log(2.0)) * I_A
    if gap < -tol or gap > upper + tol or identity_error > tol:
        raise AssertionError(
            {"n": n, "A": A, "order": order, "coarse": coarse,
             "sequential": sequential, "gap": gap, "I_A": I_A,
             "upper": upper, "identity_error": identity_error}
        )


def main(output_path=None):
    state = {
        "cases": 0,
        "min_refinement_gap": float("inf"),
        "max_gap_over_I_A": 0.0,
        "max_chain_identity_error": 0.0,
    }

    for n in (1, 2, 3):
        xs = assignments(n)
        for truthbits in range(1 << (1 << n)):
            vals = {x: (1 if ((truthbits >> idx) & 1) else -1) for idx, x in enumerate(xs)}
            for r in range(1, n + 1):
                for A in itertools.combinations(range(n), r):
                    for order in itertools.permutations(A):
                        check_case(vals, n, A, order, state)

    rng = random.Random(1)
    n = 4
    xs = assignments(n)
    for _ in range(50):
        vals = {x: rng.choice((-1, 1)) for x in xs}
        for r in range(1, n + 1):
            for A in itertools.combinations(range(n), r):
                for order in itertools.permutations(A):
                    check_case(vals, n, A, order, state)

    result = {
        "status": "PASS",
        "exhaustive_dimensions": [1, 2, 3],
        "random_dimension_4_functions": 50,
        "random_seed": 1,
        "cases": state["cases"],
        "min_refinement_gap": state["min_refinement_gap"],
        "max_gap_over_I_A": state["max_gap_over_I_A"],
        "theorem_upper_constant_2_over_ln2": 2.0 / math.log(2.0),
        "max_chain_identity_error": state["max_chain_identity_error"],
        "note": "Floating-point sanity check only; universal claims use the written entropy/channel proof."
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if output_path:
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write(text)
    sys.stdout.write(text)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
