#!/usr/bin/env python3
"""Independent integer, labelled-state, and Bellman-certificate checks."""
from collections import Counter
from fractions import Fraction
from functools import cache
import itertools
import json
import math
from pathlib import Path
import resource
import time


def labelled_cost(k):
    """No symmetry reductions: enumerate partial assignments to 3**k bits."""
    n = 3**k

    def value(bits):
        while len(bits) > 1:
            bits = [int(sum(bits[i:i+3]) >= 2) for i in range(0, len(bits), 3)]
        return bits[0]

    @cache
    def total(state):
        unknown = [i for i, x in enumerate(state) if x == -1]
        low = [0 if x == -1 else x for x in state]
        high = [1 if x == -1 else x for x in state]
        if value(low) == value(high):
            return 0
        best = None
        for i in unknown:
            a, b = list(state), list(state)
            a[i], b[i] = 0, 1
            candidate = (1 << len(unknown)) + total(tuple(a)) + total(tuple(b))
            best = candidate if best is None else min(best, candidate)
        return best

    answer = Fraction(total((-1,)*n), 1 << n)
    return dict(k=k, cost=str(answer), labelled_states=total.cache_info().currsize)


class FixedTree:
    """Keep the original majority gates, including projections MAJ(0,1,a).

    Collapse only determined subtrees. This uses neither AND/OR conversion,
    associativity, nor deletion of projection gates from the main solver.
    """
    def __init__(self):
        self.nodes = [(), (), ()]  # constant 0, constant 1, unknown leaf
        self.ids = {}

    def gate(self, a):
        a = tuple(sorted(a))
        if a.count(0) >= 2:
            return 0
        if a.count(1) >= 2:
            return 1
        if a not in self.ids:
            self.ids[a] = len(self.nodes)
            self.nodes.append(a)
        return self.ids[a]

    @cache
    def moves(self, s):
        if s < 2:
            return ()
        if s == 2:
            return ((0, 1),)
        a = list(self.nodes[s])
        moves = set()
        for child in set(a):
            j = a.index(child)
            for low, high in self.moves(child):
                b, c = a.copy(), a.copy()
                b[j], c[j] = low, high
                moves.add((self.gate(b), self.gate(c)))
        return tuple(moves)

    @cache
    def leaves(self, s):
        return int(s == 2) if s <= 2 else sum(self.leaves(c) for c in self.nodes[s])

    @cache
    def total(self, s):
        # An integer value scaled by 2**(number of relevant unknown leaves).
        if s < 2:
            return 0
        m = self.leaves(s)
        return min((1 << m) +
                   (self.total(a) << (m-1-self.leaves(a))) +
                   (self.total(b) << (m-1-self.leaves(b)))
                   for a, b in self.moves(s))

    def run(self, k):
        root = 2
        for _ in range(k):
            root = self.gate((root,)*3)
        answer = Fraction(self.total(root), 1 << self.leaves(root))
        return dict(k=k, cost=str(answer), fixed_tree_states=self.total.cache_info().currsize)


def verify_certificate():
    record = json.loads(Path("data/bellman_certificate.json").read_text())
    nodes = record["nodes"]
    values = {int(s): Fraction(v) for s, v in record["costs"].items()}
    transitions = {int(s): tuple(map(tuple, a)) for s, a in record["transitions"].items()}
    assert values[0] == values[1] == 0
    for state, cost in values.items():
        if state < 2:
            assert not transitions[state]
            continue
        candidates = [1+(values[a]+values[b])/2 for a, b in transitions[state]]
        assert candidates and min(candidates) == cost
        chosen = tuple(record["actions"][str(state)])
        assert chosen in transitions[state]
        assert 1+(values[chosen[0]]+values[chosen[1]])/2 == cost
    # Reconstruct every permitted leaf query from formula occurrences, separate
    # from the exported list. Gate simplification is shared only for this check;
    # the fixed-tree and labelled checks above do not import the main solver.
    from exact_majority import Solver
    solver = Solver()
    mapping = {0: 0, 1: 1, 2: 2}

    def rebuild(s):
        if s not in mapping:
            op, *children = nodes[s]
            mapping[s] = solver.gate(op, [rebuild(c) for c in children])
        return mapping[s]

    for s in values:
        rebuild(s)
    reverse = {v: k for k, v in mapping.items()}
    for s in values:
        regenerated = {(reverse[a], reverse[b]) for a, b in solver.transitions(mapping[s])}
        assert regenerated == set(transitions[s])
    return dict(states=len(values), bellman_inequalities=sum(map(len, transitions.values())),
                all_actions_regenerated=True)


def mns_evaluate(bits):
    """Literal deterministic-order version of Algorithms 1 and 2, for k=2."""
    if len(bits) == 1:
        return bits[0], 1
    size = len(bits)//3
    groups = [bits[i*size:(i+1)*size] for i in range(3)]
    if size == 1:
        if bits[0] == bits[1]:
            return bits[0], 2
        return bits[2], 3
    x = [mns_evaluate(g[:size//3]) for g in groups[:2]]
    total = sum(v[1] for v in x)
    if x[0][0] != x[1][0]:
        y3, cost = mns_evaluate(groups[2]); total += cost
        b = 0 if x[0][0] == y3 else 1
        yb, cost = mns_complete(groups[b], x[b][0]); total += cost
        if yb == y3:
            return y3, total
        other, cost = mns_complete(groups[1-b], x[1-b][0])
        return other, total+cost
    y1, cost = mns_complete(groups[0], x[0][0]); total += cost
    if y1 == x[0][0]:
        y2, cost = mns_complete(groups[1], x[1][0]); total += cost
        if y2 == y1:
            return y1, total
        y3, cost = mns_evaluate(groups[2])
        return y3, total+cost
    y3, cost = mns_evaluate(groups[2]); total += cost
    if y3 == y1:
        return y1, total
    y2, cost = mns_complete(groups[1], x[1][0])
    return y2, total+cost


def mns_complete(bits, known):
    size = len(bits)//3
    groups = [bits[i*size:(i+1)*size] for i in range(3)]
    if size == 1:
        if bits[1] == known:
            return known, 1
        return bits[2], 2
    x2, total = mns_evaluate(groups[1][:size//3])
    if known != x2:
        y3, cost = mns_evaluate(groups[2]); total += cost
        if known == y3:
            return known, total
        y2, cost = mns_complete(groups[1], x2)
        return y2, total+cost
    y2, cost = mns_complete(groups[1], x2); total += cost
    if known == y2:
        return known, total
    y3, cost = mns_evaluate(groups[2])
    return y3, total+cost


def main():
    started = time.monotonic()
    labelled = [labelled_cost(k) for k in (1, 2)]
    fixed = FixedTree()
    fixed_rows = [fixed.run(k) for k in (1, 2, 3)]
    certificate = verify_certificate()
    optimal = json.loads(Path("data/exact_results.json").read_text())["results"]
    by_k = {r["k"]: r["cost"] for r in optimal}
    for row in labelled + fixed_rows:
        assert row["cost"] == by_k[row["k"]]
    histogram = Counter()
    for bits in itertools.product((0, 1), repeat=9):
        output, queries = mns_evaluate(bits)
        expected = int(sum(int(sum(bits[j:j+3]) >= 2) for j in (0, 3, 6)) >= 2)
        assert output == expected
        histogram[queries] += 1
    mns_cost = Fraction(sum(q*c for q, c in histogram.items()), 512)
    assert mns_cost == Fraction(by_k[2])
    report = dict(labelled=labelled, fixed_tree=fixed_rows, certificate=certificate,
                  mns_height_2_cost=str(mns_cost), mns_height_2_histogram=dict(histogram),
                  elapsed_seconds=time.monotonic()-started,
                  max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  nice=__import__("os").getpriority(__import__("os").PRIO_PROCESS, 0))
    Path("data/verification.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
