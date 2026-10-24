"""Exact Bellman optimization and independent truth-table certificate, n=9.

Run: python -X utf8 check_majority.py
Writes only beside this script. Uniform iid inputs, zero-error query algorithms.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import math
import time

ROOT = Path(__file__).resolve().parent
N = 9
ALL = (1 << N) - 1
policy = {}
started = time.perf_counter()

def value(x):
    groups = [((x >> (3*j)) & 7).bit_count() >= 2 for j in range(3)]
    return sum(groups) >= 2

def forced(z, o):
    lo = sum(((o >> (3*j)) & 7).bit_count() >= 2 for j in range(3))
    hi = sum(((z >> (3*j)) & 7).bit_count() <= 1 for j in range(3))
    return lo >= 2 or hi <= 1

@lru_cache(None)
def total_cost(z, o):
    if forced(z, o):
        return 0
    free = ALL ^ (z | o)
    weight = 1 << free.bit_count()
    candidates = [(weight + total_cost(z | (1 << i), o)
                   + total_cost(z, o | (1 << i)), i)
                  for i in range(N) if free & (1 << i)]
    result, choice = min(candidates)
    policy[(z, o)] = choice
    return result

cost = Fraction(total_cost(0, 0), 1 << N)

# Independent termination test using the truth table, rather than group bounds.
ones = sum(1 << x for x in range(1 << N) if value(x))
universe = (1 << (1 << N)) - 1
leaf_one = [sum(1 << x for x in range(1 << N) if x & (1 << i))
            for i in range(N)]
stop_errors = bellman_errors = policy_errors = 0
for ternary in product(range(3), repeat=N):
    z = sum(1 << i for i, t in enumerate(ternary) if t == 1)
    o = sum(1 << i for i, t in enumerate(ternary) if t == 2)
    compatible = universe
    for i, t in enumerate(ternary):
        if t == 1:
            compatible &= universe ^ leaf_one[i]
        elif t == 2:
            compatible &= leaf_one[i]
    exact_stop = not (compatible & ones) or not (compatible & (universe ^ ones))
    stop_errors += exact_stop != forced(z, o)
    free = ALL ^ (z | o)
    if exact_stop:
        bellman_errors += total_cost(z, o) != 0
    else:
        candidates = {i: (1 << free.bit_count())
                      + total_cost(z | (1 << i), o)
                      + total_cost(z, o | (1 << i))
                      for i in range(N) if free & (1 << i)}
        bellman_errors += total_cost(z, o) != min(candidates.values())
        policy_errors += candidates[policy[(z, o)]] != total_cost(z, o)

lengths = []
for x in range(1 << N):
    z = o = q = 0
    while not forced(z, o):
        i = policy[(z, o)]
        if x & (1 << i):
            o |= 1 << i
        else:
            z |= 1 << i
        q += 1
    assert value(o) == value(x)
    lengths.append(q)
assert Fraction(sum(lengths), 1 << N) == cost
assert stop_errors == bellman_errors == policy_errors == 0

recursive = Fraction(25, 4)
delta = cost / 9
result = dict(problem_id='C0021', inputs=512, partial_states=3**N,
              exact_cost=str(cost), recursive_cost=str(recursive),
              exact_revealment=str(delta), recursive_revealment=str(Fraction(25, 36)),
              old_exponent=math.log(6/5)/math.log(3),
              block_exponent=-math.log(float(delta))/(2*math.log(3)),
              percent_cost_reduction=100*float((recursive-cost)/recursive),
              stop_errors=stop_errors, bellman_errors=bellman_errors,
              policy_errors=policy_errors, max_queries=max(lengths),
              seconds=time.perf_counter()-started)
(ROOT/'majority_measurements.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
(ROOT/'majority_policy.json').write_text(json.dumps(
    {f'{z},{o}': i for (z, o), i in policy.items()}, sort_keys=True), encoding='utf-8')
print(json.dumps(result, indent=2))
