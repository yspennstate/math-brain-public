#!/usr/bin/env python3
"""Finite checks of the selector identities, using only the standard library.

The computations are consistency checks; the accompanying proofs do not
depend on them. Truth tables use x_i=(-1)^bit_i, with control bits first.
"""

import itertools
import json
import math
from pathlib import Path


TOL = 2e-10
COUNTS = {}
MAX_ERROR = 0.0


def close(a, b, label):
    global MAX_ERROR
    error = abs(a - b)
    MAX_ERROR = max(MAX_ERROR, error)
    if error > TOL * max(1.0, abs(a), abs(b)):
        raise AssertionError((label, a, b, error))


def entropy(weights):
    return math.fsum(-p * math.log2(p) for p in weights if p > 0)


def walsh(values):
    out = list(values)
    step = 1
    while step < len(out):
        for start in range(0, len(out), 2 * step):
            for i in range(start, start + step):
                a, b = out[i], out[i + step]
                out[i], out[i + step] = a + b, a - b
        step *= 2
    return [v / len(out) for v in out]


def stats(values):
    coeff = walsh(values)
    probabilities = [v * v for v in coeff]
    return {
        "coeff": coeff,
        "prob": probabilities,
        "H": entropy(probabilities),
        "I": math.fsum(mask.bit_count() * p for mask, p in enumerate(probabilities)),
        "mean": coeff[0],
    }


def character(n, mask):
    return [1 if (x & mask).bit_count() % 2 == 0 else -1 for x in range(1 << n)]


def check_selector(labels, leaves, name):
    nc = len(labels)
    ny = len(leaves[0])
    m = len(leaves)
    leaf_stats = [stats(g) for g in leaves]
    seen = set()
    for st in leaf_stats:
        close(st["mean"], 0, "balanced leaves")
        support = {mask for mask, v in enumerate(st["coeff"]) if v != 0}
        if seen & support:
            raise AssertionError("leaf Fourier supports overlap")
        seen |= support
    f = [leaves[labels[z]][y] for y in range(ny) for z in range(nc)]
    actual = stats(f)
    weights = [labels.count(j) / nc for j in range(m)]
    if min(weights) <= 0:
        raise AssertionError("empty selector cell")
    predicted_h = entropy(weights)
    predicted_i = 0.0
    d_sel = 0.0
    h_cell_plus = 0.0
    c_sel = 0.0
    c_sel_strong = 0.0
    for j, p in enumerate(weights):
        a = [int(label == j) for label in labels]
        a_coeff = walsh(a)
        q = [c * c / p for c in a_coeff]
        close(math.fsum(q), 1.0, "normalized indicator law")
        d = math.fsum(mask.bit_count() * mass for mask, mass in enumerate(q))
        predicted_h += p * (entropy(q) + leaf_stats[j]["H"])
        predicted_i += p * (d + leaf_stats[j]["I"])
        d_sel += p * d
        h = stats([2 * v - 1 for v in a])
        close(h["I"], 4 * p * d, "cell influence normalization")
        h_cell_plus += entropy(h["prob"][1:])
        if h["I"]:
            c_sel = max(c_sel, h["H"] / h["I"])
        cell_deficit = h["I"] - (1 - h["mean"] ** 2)
        if cell_deficit > TOL:
            c_sel_strong = max(c_sel_strong, entropy(h["prob"][1:]) / cell_deficit)
        else:
            close(entropy(h["prob"][1:]), 0, "zero cell deficit")
        if h["I"] + TOL < 2 * p * math.log2(1 / p):
            raise AssertionError("edge isoperimetric bound")
    close(actual["H"], predicted_h, name + ": entropy identity")
    close(actual["I"], predicted_i, name + ": influence identity")
    r = 2 * math.fsum(p * (1 - p) + p * p * math.log2(1 / p) for p in weights)
    leaf_h = math.fsum(p * st["H"] for p, st in zip(weights, leaf_stats))
    close(actual["H"] - leaf_h, 0.25 * h_cell_plus + r, "exact correction R")
    if r > 2 * entropy(weights) + TOL:
        raise AssertionError("R <= 2H(p)")
    if r > 4 * math.fsum(p * (1 - p) for p in weights) + TOL:
        raise AssertionError("R <= 4B")
    if entropy(weights) > 2 * d_sel + TOL:
        raise AssertionError("label entropy <= 2D")
    c_leaf = 0.0
    for st in leaf_stats:
        if st["I"] > 1 + TOL:
            c_leaf = max(c_leaf, st["H"] / (st["I"] - 1))
        else:
            close(st["H"], 0, "zero leaf deficit")
    if actual["H"] > max(c_sel + 4, c_leaf) * (actual["I"] - 1) + TOL:
        raise AssertionError("cell-FEI plus 4 closure")
    if actual["H"] > max(c_sel_strong, c_leaf, 4) * (actual["I"] - 1) + TOL:
        raise AssertionError("constant-preserving strong selector closure")
    COUNTS[name] = COUNTS.get(name, 0) + 1
    return actual


def check_all_three_cell_partitions():
    # All 5,796 surjections of a three-dimensional cube onto three labels.
    # The three leaves share two data variables but have disjoint spectra.
    leaves = [character(2, mask) for mask in (1, 2, 3)]
    for labels_tuple in itertools.product(range(3), repeat=8):
        if set(labels_tuple) == {0, 1, 2}:
            check_selector(list(labels_tuple), leaves, "all_three_cell_partitions")


def check_affine_and_subcube_examples():
    examples = []
    for k in range(1, 4):
        nleaves = 1 << k
        labels = list(range(nleaves))
        leaves = [character(nleaves, 1 << j) for j in range(nleaves)]
        st = check_selector(labels, leaves, "ordinary_addressing")
        close(st["H"], 2 * k, "address H")
        close(st["I"], 1 + k / 2, "address I")
        close(st["H"], 4 * (st["I"] - 1), "address sharp deficit")
        examples.append({"name": f"addressing_{k}", "H": st["H"], "I": st["I"]})

    # Unequal coordinate subcubes: x0=1; x0=-1,x1=1; x0=x1=-1.
    labels = [0 if not z & 1 else 1 if not z & 2 else 2 for z in range(4)]
    st = check_selector(labels, [character(3, b) for b in (1, 2, 4)], "unequal_subcubes")
    close(st["H"], 3, "unequal subcube H")
    close(st["I"], 1.75, "unequal subcube I")

    # Affine cells defined by parities on overlapping support coordinates.
    labels = [((z & 3).bit_count() & 1) + 2 * ((z & 12).bit_count() & 1) for z in range(16)]
    st = check_selector(labels, [character(3, b) for b in (1, 2, 3, 7)], "affine_partition")
    close(st["H"], 4, "affine H")
    close(st["I"], 3.75, "affine I")

    labels = [0 if not ((z & 3).bit_count() & 1) else 1 + ((z & 12).bit_count() & 1) for z in range(16)]
    st = check_selector(labels, [character(2, b) for b in (1, 2, 3)], "unequal_affine_partition")
    close(st["H"], 3, "unequal affine H")
    close(st["I"], 2.75, "unequal affine I")

    # Non-character balanced leaves: two majority-of-three functions.
    maj0 = [1 if 3 - 2 * (y & 7).bit_count() > 0 else -1 for y in range(64)]
    maj1 = [1 if 3 - 2 * ((y >> 3) & 7).bit_count() > 0 else -1 for y in range(64)]
    st = check_selector([0, 1], [maj0, maj1], "majority_leaves")
    close(st["H"], 4, "majority-leaf H")
    close(st["I"], 2, "majority-leaf I")
    return examples


def multiplexer(g):
    n = len(g)
    return [1 if not (y & (1 if g[x] == 1 else 2)) else -1 for y in range(4) for x in range(n)]


def check_balanced_mux_and_tensorization():
    for n in range(1, 4):
        size = 1 << n
        for truth in range(1 << size):
            f = [1 if not (truth >> x) & 1 else -1 for x in range(size)]
            fs = stats(f)
            if sum(f) == 0:
                ms = stats(multiplexer(f))
                close(ms["H"], 2 + fs["H"] / 2, "balanced mux H")
                close(ms["I"], 1 + fs["I"] / 2, "balanced mux I")
                COUNTS["balanced_mux"] = COUNTS.get("balanced_mux", 0) + 1
            # g_2=z f(x^(1))f(x^(2)); covers all f, including biased f.
            g = [(1 if z == 0 else -1) * f[x] * f[y]
                 for z in range(2) for y in range(size) for x in range(size)]
            gs = stats(g)
            close(gs["mean"], 0, "tensor balance")
            close(gs["H"], 2 * fs["H"], "tensor H")
            close(gs["I"], 2 * fs["I"] + 1, "tensor I")
            ms = stats(multiplexer(g))
            close(ms["H"], 2 + fs["H"], "tensor mux H")
            close(ms["I"], 1.5 + fs["I"], "tensor mux I")
            COUNTS["balanced_tensor_mux"] = COUNTS.get("balanced_tensor_mux", 0) + 1


def check_queue_addressing_bound():
    for m in range(1, 65):
        number_of_gates = 1 << m
        d = m + 1
        influence = 1 + m / 2
        normalization = number_of_gates * math.log1p(1 / (2 * number_of_gates)) / math.log(2)
        expected_cost = normalization + d + 1
        expected_cost += math.fsum(
            math.comb(m, t) / number_of_gates * (
                math.log2((t + 1) * (t + 2))
                + (t + 1) * math.log2(6 * math.e)
                + 1.2 * (t + 1) * math.log2(d / (t + 1)))
            for t in range(m + 1))
        coarse_cost = math.log2(math.e) / 2 + (16 / 5 + math.log2(18 * math.e)) * influence
        if expected_cost > coarse_cost + TOL or coarse_cost >= 10 * influence:
            raise AssertionError("addressing queue constant")
        if expected_cost < 2 * m - TOL:
            raise AssertionError("witness cost cannot undercut exact entropy")
        COUNTS["queue_addressing_bound"] = COUNTS.get("queue_addressing_bound", 0) + 1


def main():
    examples = check_affine_and_subcube_examples()
    check_all_three_cell_partitions()
    check_balanced_mux_and_tensorization()
    check_queue_addressing_bound()
    report = {"status": "PASS", "case_counts": COUNTS, "total_cases": sum(COUNTS.values()),
              "max_absolute_identity_error": MAX_ERROR, "addressing_examples": examples,
              "note": "Finite consistency checks; no universal inequality is established by enumeration."}
    rendered = json.dumps(report, indent=2)
    Path(__file__).with_name("selector_verification.json").write_text(rendered + "\n")
    print(rendered)


if __name__ == "__main__":
    main()
