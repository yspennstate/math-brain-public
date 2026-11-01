"""Exact finite-alphabet checks for the set-valued recursion.

We compare its singleton canonical fixed law with its spurious ordinary-
percolation set fixed law. Neither a finite truncation nor a set-valued
fixed point is taken as a solution of the original infinite-time question.
"""
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import itertools
import json

INF = None

def chi(tau, kappa, x, y):
    if kappa == 1:
        return x if x is not INF and tau < x else INF
    if x is INF:
        return y
    if y is INF:
        return x
    return min(x, y)

def image(A, B, tau, kappa):
    return frozenset(chi(tau, kappa, x, y) for x in A for y in B)

def transform(law, times):
    result = defaultdict(Q)
    cuts = sorted({Q(0), Q(1), *times})
    for A, pa in law.items():
        for B, pb in law.items():
            for left, right in zip(cuts, cuts[1:]):
                tau = (left + right) / 2
                result[image(A, B, tau, 1)] += pa * pb * (right-left)/2
            result[image(A, B, Q(0), 2)] += pa * pb / 2
    return {s:p for s,p in result.items() if p}

def encode(law):
    return [{"set": sorted(str(x) if x is not INF else 'inf' for x in s),
             "mass": str(p)} for s, p in law.items()]

results = []
membership_cases = 0
inflation_cases = 0
for theta in [Q(1, 4), Q(1, 2), Q(3, 4)]:
    times = sorted([Q(1), theta, theta*theta])
    states = times + [INF]
    subsets = [frozenset(states[j] for j in range(len(states)) if mask >> j & 1)
               for mask in range(1, 1 << len(states))]
    def inflate(x):
        return frozenset([Q(1), INF]) if x == Q(1) else frozenset([x])
    cuts = sorted({Q(0), Q(1), *times})
    for x, y in itertools.product(states, repeat=2):
        for left, right in zip(cuts, cuts[1:]):
            tau = (left+right)/2
            for kappa in [1, 2]:
                assert image(inflate(x), inflate(y), tau, kappa) == inflate(
                    chi(tau, kappa, x, y))
                inflation_cases += 1
    for A, B in itertools.product(subsets, repeat=2):
        im = image(A, B, Q(0), 2)
        for t in times:
            rhs = ((t in A and any(y is INF or y >= t for y in B)) or
                   (t in B and any(x is INF or x >= t for x in A)))
            assert (t in im) == rhs
            membership_cases += 1

    # Source finite-time canonical CDF recursion: F(t)=max(Fprev,t-Fprev).
    canonical = {}
    cdf = Q(0)
    for t in times:
        new_cdf = max(cdf, t-cdf)
        if new_cdf > cdf:
            canonical[frozenset([t])] = new_cdf-cdf
        cdf = new_cdf
    canonical[frozenset([INF])] = 1-cdf

    # Ordinary percolation events are nested and have probability t.
    relaxed = {}
    prev = Q(0)
    for t in times:
        relaxed[frozenset([INF, *[u for u in times if u >= t]])] = t-prev
        prev = t

    assert sum(canonical.values()) == sum(relaxed.values()) == 1
    assert transform(canonical, times) == canonical
    assert transform(relaxed, times) == relaxed
    assert all(len(s) == 1 for s in canonical)
    assert all(len(s) >= 2 for s in relaxed)
    inflated = {inflate(next(iter(s))): p for s,p in canonical.items()}
    assert transform(inflated, times) == inflated
    for t in times:
        assert sum(p for s,p in inflated.items() if t in s) == sum(
            p for s,p in canonical.items() if t in s)
    results.append({"theta": str(theta), "times": list(map(str,times)),
                    "canonical_singleton_fixed_law": encode(canonical),
                    "relaxed_nonsingleton_fixed_law": encode(relaxed),
                    "inflated_fixed_law_with_same_finite_presence": encode(inflated),
                    "both_fixed_point_equalities_exact": True})

output = {"branching_membership_cases": membership_cases,
          "inflation_intertwining_cases": inflation_cases,
          "examples": results,
          "limitation": "Relaxed sets describe local-recursion states, "
                        "not genuine frozen solutions. Finite freezing "
                        "sets are uniquely solvable; these nonsingleton "
                        "set fixed laws do not contradict that fact."}
Path(__file__).with_name('feasible_set_checks.json').write_text(
    json.dumps(output, indent=2), encoding='utf8')
print(json.dumps(output, indent=2))
