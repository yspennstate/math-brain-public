#!/usr/bin/env python3
"""Exact uniform-average decision tree DP for read-once ternary majority.

Every possible next relevant leaf is considered, including interleaving subtrees.
States are read-once restricted formulas modulo child permutations and elementary
constant simplifications. Separate occurrences of the same subtree ID denote
independent copies with distinct leaves, never shared input variables.
"""
import argparse
from fractions import Fraction
from functools import cache
import json
import math
import os
from pathlib import Path
import resource
import time

ZERO, ONE, LEAF, AND, OR, MAJ = range(6)


class Solver:
    def __init__(self):
        self.nodes = [(ZERO,), (ONE,), (LEAF,)]
        self.intern = {s: i for i, s in enumerate(self.nodes)}
        self.values = {ZERO: Fraction(0), ONE: Fraction(0)}
        self.actions = {}
        self.transitions_count = 0

    def gate(self, op, children):
        children = list(children)
        if op == MAJ:
            if children.count(ZERO) >= 2:
                return ZERO
            if children.count(ONE) >= 2:
                return ONE
            if ZERO in children and ONE in children:
                return next(x for x in children if x not in (ZERO, ONE))
            if ZERO in children:
                children.remove(ZERO)
                return self.gate(AND, children)
            if ONE in children:
                children.remove(ONE)
                return self.gate(OR, children)
        else:
            absorbing, identity = (ZERO, ONE) if op == AND else (ONE, ZERO)
            if absorbing in children:
                return absorbing
            children = [x for x in children if x != identity]
            flat = []
            for x in children:
                flat.extend(self.nodes[x][1:] if self.nodes[x][0] == op else [x])
            children = flat
            if not children:
                return identity
            if len(children) == 1:
                return children[0]
        key = (op, *sorted(children))
        if key not in self.intern:
            self.intern[key] = len(self.nodes)
            self.nodes.append(key)
        return self.intern[key]

    def full(self, depth):
        state = LEAF
        for _ in range(depth):
            state = self.gate(MAJ, [state] * 3)
        return state

    @cache
    def transitions(self, state):
        """All distinct ordered (zero-successor, one-successor) query pairs."""
        if state < LEAF:
            return ()
        if state == LEAF:
            return ((ZERO, ONE),)
        op, *children = self.nodes[state]
        pairs = set()
        for child in set(children):
            i = children.index(child)
            for low, high in self.transitions(child):
                a = children.copy()
                b = children.copy()
                a[i], b[i] = low, high
                pairs.add((self.gate(op, a), self.gate(op, b)))
        self.transitions_count += len(pairs)
        return tuple(sorted(pairs))

    def cost(self, state):
        if state not in self.values:
            if len(self.values) % 1000 == 0:
                # Darwin reports bytes. Leave over 2 GB for interpreter/output
                # overhead even if a new experiment reaches the guard.
                if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1536 * 1024**2:
                    raise MemoryError("1.5 GB RSS guard reached")
            candidates = [(1 + (self.cost(a) + self.cost(b)) / 2, (a, b))
                          for a, b in self.transitions(state)]
            value, pair = min(candidates)
            self.values[state] = value
            self.actions[state] = pair
        return self.values[state]

    def export(self, roots, path):
        # A full Bellman certificate, not merely the reachable optimal policy.
        path.write_text(json.dumps(dict(
            roots=roots, nodes=self.nodes,
            costs={str(s): str(v) for s, v in self.values.items()},
            actions=self.actions,
            transitions={str(s): list(self.transitions(s)) for s in self.values},
        ), separators=(",", ":")) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-depth", type=int, default=3)
    args = parser.parse_args()
    # The launcher already gives nice 15. Raising priority is forbidden and
    # unnecessary: verify >=10 rather than calling macOS nice(0).
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    if priority < 10:
        os.setpriority(os.PRIO_PROCESS, 0, 10)
    # This sandbox rejects setrlimit changes; enforce a conservative RSS guard
    # inside the DP. No numerical libraries or auxiliary worker processes.
    solver = Solver()
    rows, roots = [], {}
    started = time.monotonic()
    for depth in range(args.max_depth + 1):
        root = solver.full(depth)
        cost = solver.cost(root)
        roots[str(depth)] = root
        delta = cost / 3**depth
        row = dict(k=depth, n=3**depth, cost=str(cost), cost_decimal=float(cost),
                   revealment=str(delta), revealment_decimal=float(delta),
                   directional_cost=str(Fraction(5, 2)**depth),
                   effective_base=float(cost)**(1/depth) if depth else None,
                   effective_sigma=-math.log(float(delta), 3)/depth if depth else None,
                   states=len(solver.values), interned_nodes=len(solver.nodes),
                   transition_pairs=solver.transitions_count,
                   elapsed_seconds=time.monotonic()-started)
        rows.append(row)
        print(json.dumps(row), flush=True)
        Path("data/exact_results.json").write_text(json.dumps(dict(
            arithmetic="fractions.Fraction", nice=priority, threads=1,
            rss_guard_bytes=1536*1024**2, results=rows,
            max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        ), indent=2) + "\n")
        solver.export(roots, Path("data/bellman_certificate.json"))


if __name__ == "__main__":
    main()
