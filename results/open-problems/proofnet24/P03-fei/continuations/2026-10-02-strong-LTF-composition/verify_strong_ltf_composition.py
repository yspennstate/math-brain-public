"""Independent finite checks for strengthened LTF FEI and balanced composition.

The universal near-dictator lemma is checked exhaustively on all monotone
functions through dimension five. These checks do not certify novelty or
replace the analytic proof.
"""

import json
import math
from pathlib import Path
import numpy as np

rng = np.random.default_rng(20261005)
report = {"status": "all assertions passed", "seed": 20261005,
          "scope": "finite checks; analytic proof is separate; no novelty certification",
          "monotone_functions": 0, "near_dictator_splits": 0,
          "LTFs": 0, "composition_nodes": 0, "formula_roots": 0,
          "maxima": {}}


def record(key, value):
    report["maxima"][key] = max(float(value), report["maxima"].get(key, -math.inf))


def fwht(values):
    v = np.array(values, dtype=float)
    step = 1
    while step < len(v):
        block = v.reshape(-1, 2 * step)
        a, b = block[:, :step].copy(), block[:, step:].copy()
        block[:, :step], block[:, step:] = a + b, a - b
        step *= 2
    degree = np.array([int(j).bit_count() for j in range(len(v))])
    return v * np.where(degree % 2, -1, 1) / len(v), degree


def stats(values):
    c, degree = fwht(values)
    p = c ** 2
    nonzero = p > 0
    H = float(-np.dot(p[nonzero], np.log2(p[nonzero])))
    I = float(np.dot(degree, p))
    V = float(1 - np.mean(values) ** 2)
    return H, I, V


def split(values, i):
    index = np.arange(len(values))
    lower = index[((index >> i) & 1) == 0]
    minus, plus = values[lower], values[lower | (1 << i)]
    A, B = (plus + minus) / 2, (plus - minus) / 2
    alpha = float(np.mean(B ** 2))
    deltaH = stats(values)[0] - (stats(plus)[0] + stats(minus)[0]) / 2
    variance_gap = stats(values)[2] - (stats(plus)[2] + stats(minus)[2]) / 2
    assert abs(variance_gap - np.mean(B) ** 2) < 1e-12
    if np.all(B >= 0):
        assert abs(variance_gap - alpha ** 2) < 1e-12
    if alpha > .5:
        delta = 1 - alpha
        if delta == 0:
            assert abs(deltaH) < 1e-12
        else:
            ac, _ = fwht(A)
            bc, _ = fwht(B)
            pair = ac ** 2 + bc ** 2
            use = pair > 0
            q = ac[use] ** 2 / pair[use]
            h = np.zeros(len(q))
            interior = (q > 0) & (q < 1)
            h[interior] = (-q[interior] * np.log2(q[interior])
                          - (1 - q[interior]) * np.log2(1 - q[interior]))
            conditional = float(np.dot(pair[use], h))
            assert pair[0] >= alpha ** 2 - 1e-14
            assert deltaH <= 2 * conditional + 1e-12
            assert conditional <= 2 * delta + 2 * delta ** 2 * math.log2(1 / delta) + delta ** 2 * math.log2(math.e) + 1e-12
            assert deltaH < 8 * delta + 1e-12
            record("universal_near_dictator_increment_over_delta", deltaH / delta)
            record("universal_near_dictator_conditional_entropy_over_delta", conditional / delta)
        report["near_dictator_splits"] += 1
    return alpha, deltaH


monotone = [np.array([False]), np.array([True])]
for n in range(1, 6):
    monotone = [np.r_[low, high] for low in monotone for high in monotone if np.all(low <= high)]
    for table in monotone:
        f = 2 * table.astype(float) - 1
        for i in range(n):
            split(f, i)
        report["monotone_functions"] += 1
assert len(monotone) == 7581


for n in [1, 2, 3, 4, 6, 8, 10, 12, 14]:
    index = np.arange(1 << n)
    x = 2 * ((index[:, None] >> np.arange(n)) & 1) - 1
    for family in ["equal", "binary", "near_dictator", "normal", "lognormal"]:
        if family == "equal":
            w = np.ones(n)
        elif family == "binary":
            w = 2. ** np.arange(n)
        elif family == "near_dictator":
            w = np.r_[n - 1 if n > 1 else 1, np.ones(n - 1)]
        elif family == "normal":
            w = np.maximum(1., np.rint(1000 * abs(rng.normal(size=n))))
        else:
            w = np.maximum(1., np.rint(10000 * rng.lognormal(0, 3, n)))
        scores = x @ w
        distinct = np.unique(scores)
        indices = np.unique(np.r_[0, len(distinct) - 2, np.linspace(0, len(distinct) - 2, 13).astype(int)])
        for j in indices:
            if not 0 <= j < len(distinct) - 1:
                continue
            f = np.where(scores > distinct[j], 1., -1.)
            H, I, V = stats(f)
            gap = I - V
            if gap > 1e-12:
                record("LTF_entropy_over_I_minus_variance", H / gap)
            else:
                assert H < 1e-12
            alpha, dh = split(f, int(np.argmax(w)))
            if 0 < alpha < 1:
                record("LTF_increment_over_alpha_one_minus_alpha", dh / (alpha * (1 - alpha)))
            report["LTFs"] += 1


class Node:
    def __init__(self, children=None, weights=None, theta=0):
        if children is None:
            self.values = np.array([-1., 1.])
            self.n = 1
            self.statistics = stats(self.values)
            return
        children = list(children)
        self.n = sum(child.n for child in children)
        m = len(children)
        gindex = np.arange(1 << m)
        gx = 2 * ((gindex[:, None] >> np.arange(m)) & 1) - 1
        g = np.where(gx @ weights > theta, 1., -1.)
        gs = stats(g)
        index = np.arange(1 << self.n)
        offset = 0
        gate_index = np.zeros(len(index), dtype=int)
        for i, child in enumerate(children):
            assert np.mean(child.values) == 0
            local_index = (index >> offset) & ((1 << child.n) - 1)
            gate_index |= (child.values[local_index] == 1).astype(int) << i
            offset += child.n
        self.values = g[gate_index]
        self.statistics = stats(self.values)
        gate_influences = np.array([np.mean(g != g[gindex ^ (1 << i)]) for i in range(m)])
        predicted_H = gs[0] + sum(gate_influences[i] * children[i].statistics[0] for i in range(m))
        predicted_I = sum(gate_influences[i] * children[i].statistics[1] for i in range(m))
        errors = [abs(self.statistics[0] - predicted_H), abs(self.statistics[1] - predicted_I), abs(self.statistics[2] - gs[2])]
        assert max(errors) < 1e-10
        record("balanced_composition_identity_error", max(errors))
        report["composition_nodes"] += 1


for trial in range(15):
    # Different depths: one child has five leaves, another three, the third five.
    grandchild = Node([Node(), Node(), Node()], [1, 1, 1])
    child1 = Node([grandchild, Node(), Node()], rng.choice([1, 3, 5], 3))
    child2 = Node([Node(), Node(), Node()], rng.choice([1, 3, 5], 3))
    child3 = Node([Node() for _ in range(5)], rng.choice([1, 3, 5], 5))
    root_weights = rng.integers(1, 9, 3)
    for theta in [-sum(root_weights), -1, 0, 1, sum(root_weights) - 1, sum(root_weights)]:
        root = Node([child1, child2, child3], root_weights, theta)
        H, I, V = root.statistics
        if I - V > 1e-12:
            record("formula_entropy_over_I_minus_variance", H / (I - V))
        else:
            assert H < 1e-12
        report["formula_roots"] += 1

Path(__file__).with_name("strong_ltf_composition_checks.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
