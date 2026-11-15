#!/usr/bin/env python3
"""Finite-state recursive algorithms with exact rational supersolution proof.

Types are the 46 restrictions of the top two levels. To evaluate one, open
one further level, then choose between evaluating a proper descendant by an
already defined recursive routine and opening a bottom macro-bit. Policies
are optimized by Bellman recursion. Only an exact rational certificate counts
as an asymptotic bound; floating point is used to search for one.
"""
from fractions import Fraction as Q
from functools import cache
from itertools import combinations_with_replacement
import argparse
import json
import math
import os
from pathlib import Path
import resource
import time


class Model:
    def __init__(self):
        self.nodes = [(), (), ()]  # 0, 1, unknown macro-bit
        self.ids = {}
        self.levels = [[0, 1, 2]]
        for _ in range(3):
            self.levels.append(sorted({self.gate(a) for a in
                combinations_with_replacement(self.levels[-1], 3)}))
        self.types = self.levels[2]
        self.full1 = self.gate((2, 2, 2))
        self.full2 = self.gate((self.full1,)*3)
        self.type_index = {s: i for i, s in enumerate(self.types)}
        self.root_index = self.type_index[self.full2]
        self.expanded = {s: self.expand(s) for s in self.types}
        self.actions = {}
        for state in self.levels[3]:
            self.actions[state] = self.make_actions(state)
        self.order = sorted(self.levels[3], key=self.leaf_count)

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
    def expand(self, s):
        if s < 2:
            return s
        if s == 2:
            return self.full1
        return self.gate(tuple(self.expand(x) for x in self.nodes[s]))

    @cache
    def leaf_count(self, s):
        return int(s == 2) if s <= 2 else sum(self.leaf_count(c) for c in self.nodes[s])

    @cache
    def probability(self, s):
        if s < 2:
            return Q(s)
        if s == 2:
            return Q(1, 2)
        a, b, c = map(self.probability, self.nodes[s])
        return a*b+a*c+b*c-2*a*b*c

    def replace(self, s, path, bit):
        if not path:
            return bit
        a = list(self.nodes[s])
        a[path[0]] = self.replace(a[path[0]], path[1:], bit)
        return self.gate(a)

    def make_actions(self, s):
        if s < 2:
            return []
        actions = set()

        def walk(sub, path):
            if sub < 2:
                return
            depth = len(path)
            if path:
                if depth == 1:
                    routine_type = sub  # remaining skeleton has depth 2
                elif depth == 2:
                    routine_type = self.expand(sub)  # pad depth 1 to depth 2
                else:
                    assert depth == 3 and sub == 2
                    routine_type = self.full2
                actions.add((self.type_index[routine_type], depth,
                             self.probability(sub),
                             self.replace(s, path, 0), self.replace(s, path, 1)))
            if sub > 2:
                for i, child in enumerate(self.nodes[sub]):
                    walk(child, path+(i,))
        walk(s, ())
        return sorted(actions)

    def apply(self, weights, lam, exact=False, export=False):
        values = {0: Q(0) if exact else 0., 1: Q(0) if exact else 0.}
        policy = {}
        inverse = {j: lam**(-j) for j in (1, 2, 3)}
        for s in self.order:
            if s < 2:
                continue
            candidates = []
            for i, depth, prob, low, high in self.actions[s]:
                p = prob if exact else float(prob)
                candidate = weights[i]*inverse[depth] + (1-p)*values[low] + p*values[high]
                candidates.append(candidate)
            value = min(candidates)
            values[s] = value
            if export:
                policy[s] = candidates.index(value)
        result = [values[self.expanded[s]] for s in self.types]
        return (result, policy, values) if export else result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", default="123/50")
    parser.add_argument("--iterations", type=int, default=40)
    args = parser.parse_args()
    started = time.monotonic()
    model = Model()
    lam = Q(args.lam)
    weights = [float(model.leaf_count(s)) / 9 for s in model.types]
    ratios = []
    for _ in range(args.iterations):
        image = model.apply(weights, float(lam))
        ratio = image[model.root_index]
        weights = [x / ratio for x in image]
        ratios.append(ratio)
    # Small-denominator rationalization plus exact Bellman check.
    rational_weights = [Q(round(w*10**10), 10**10) for w in weights]
    image, policy, values = model.apply(rational_weights, lam, exact=True, export=True)
    slacks = {str(s): rational_weights[i]-image[i] for i, s in enumerate(model.types)}
    verified = all(x >= 0 for x in slacks.values())
    output = dict(lambda_rational=str(lam), lambda_decimal=float(lam),
                  sigma=math.log(3/float(lam), 3), verified=verified,
                  last_ratios=ratios[-5:], type_count=len(model.types),
                  expanded_state_count=len(model.levels[3]),
                  weights={str(s): str(rational_weights[i]) for i, s in enumerate(model.types)},
                  slacks={s: str(v) for s, v in slacks.items()},
                  nodes=model.nodes, types=model.types, full2=model.full2,
                  root_index=model.root_index,
                  policy={str(s): [model.types[a[0]], a[1], str(a[2]), a[3], a[4]]
                          for s, index in policy.items()
                          for a in [model.actions[s][index]]},
                  elapsed_seconds=time.monotonic()-started,
                  max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  nice=os.getpriority(os.PRIO_PROCESS, 0))
    filename = "data/recursive_bound_"+args.lam.replace("/", "_")+".json"
    Path(filename).write_text(json.dumps(output, separators=(",", ":"))+"\n")
    print(json.dumps({k: v for k, v in output.items() if k not in
        {"nodes", "types", "weights", "slacks", "policy"}}, indent=2), flush=True)
    if not verified:
        print("No bound certified at this lambda.", flush=True)


if __name__ == "__main__":
    main()
