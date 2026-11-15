#!/usr/bin/env python3
"""Verify a recursive algorithm certificate without importing its search code.

Decode trees into nested tuples, enumerate actual node paths, check every
chosen action against the corresponding subtree, and evaluate the policy
using exact rational arithmetic. Search-time Bellman values are not used.
"""
from fractions import Fraction as Q
from functools import cache
from itertools import combinations_with_replacement
import hashlib
import json
from pathlib import Path
import resource
import time


def gate(children):
    children = tuple(sorted(children, key=repr))
    if children.count(0) >= 2:
        return 0
    if children.count(1) >= 2:
        return 1
    return children


@cache
def grow(tree):
    return gate((2, 2, 2)) if tree == 2 else (
        tree if isinstance(tree, int) else gate(tuple(grow(c) for c in tree)))


@cache
def probability(tree):
    if isinstance(tree, int):
        return Q(1, 2) if tree == 2 else Q(tree)
    a, b, c = map(probability, tree)
    return a*b+b*c+a*c-2*a*b*c


@cache
def leaf_count(tree):
    return int(tree == 2) if isinstance(tree, int) else sum(map(leaf_count, tree))


def paths(tree, prefix=()):
    if tree in (0, 1):
        return
    if prefix:
        yield prefix, tree
    if isinstance(tree, tuple):
        for i, child in enumerate(tree):
            yield from paths(child, prefix+(i,))


def replace(tree, path, bit):
    if not path:
        return bit
    children = list(tree)
    children[path[0]] = replace(children[path[0]], path[1:], bit)
    return gate(children)


def main():
    started = time.monotonic()
    source = Path("data/recursive_bound_246003_100000.json")
    data = json.loads(source.read_text())
    lam = Q(data["lambda_rational"])
    raw_nodes = data["nodes"]

    @cache
    def decode(i):
        return i if i <= 2 else gate(tuple(decode(c) for c in raw_nodes[i]))

    types = {decode(s) for s in data["types"]}
    weights = {decode(int(s)): Q(v) for s, v in data["weights"].items()}
    levels = [{0, 1, 2}]
    for _ in range(3):
        levels.append({gate(t) for t in combinations_with_replacement(
            sorted(levels[-1], key=repr), 3)})
    assert types == levels[2] and len(types) == 46
    full = grow(grow(2))
    assert decode(data["full2"]) == full and weights[full] == 1
    assert weights[0] == weights[1] == 0
    assert all(weights[t] > 0 for t in types if t not in (0, 1))
    policy = {}
    for state_id, action in data["policy"].items():
        state = decode(int(state_id))
        type_id, depth, prob, low, high = action
        target_type, p = decode(type_id), Q(prob)
        low, high = decode(low), decode(high)
        assert state not in policy
        legal = False
        for path, subtree in paths(state):
            if len(path) != depth:
                continue
            if depth == 1:
                routine_type = subtree
            elif depth == 2:
                routine_type = grow(subtree)
            else:
                assert depth == 3 and subtree == 2
                routine_type = full
            if (routine_type == target_type and probability(subtree) == p
                    and replace(state, path, 0) == low
                    and replace(state, path, 1) == high):
                legal = True
                break
        assert legal, state_id
        assert leaf_count(low) < leaf_count(state)
        assert leaf_count(high) < leaf_count(state)
        policy[state] = (target_type, depth, p, low, high)
    assert set(policy) == levels[3] - {0, 1}

    @cache
    def evaluate(state):
        if state in (0, 1):
            return Q(0)
        kind, depth, p, low, high = policy[state]
        return weights[kind]/lam**depth + (1-p)*evaluate(low) + p*evaluate(high)

    slacks = {t: weights[t]-evaluate(grow(t)) for t in types}
    assert all(s >= 0 for s in slacks.values())
    positive_slacks = [slacks[t] for t in types if t not in (0, 1)]
    minimum_weight = min(weights[t] for t in types if t not in (0, 1))
    # For heights 2,3,4 querying all leaves costs <=3**h. This K dominates
    # all these base cases, without solving depth 4 optimally.
    prefactor = (Q(3)/lam)**4/minimum_weight
    result = dict(verified=True, certificate_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  lambda_rational=str(lam), type_inequalities=len(types),
                  independently_validated_actions=len(policy),
                  minimum_positive_slack=str(min(positive_slacks)),
                  minimum_weight=str(minimum_weight), prefactor_K=str(prefactor),
                  prefactor_K_decimal=float(prefactor),
                  elapsed_seconds=time.monotonic()-started,
                  max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    Path("data/recursive_verification.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
