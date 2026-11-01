#!/usr/bin/env python3
"""Exact finite sanity checker for HARD7-04 collared lower-bound route.

Checks the two exact combinatorial identities used in the asymptotic proof:
(3.4) for E[T_k], and (6.2) for the factorial/joint moment of two
distinct tree components, by exhaustive enumeration of every perfect
matching for several small degree sequences.  Arithmetic is exact
fractions/integers throughout.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import factorial


def odd_df(n):
    if n <= 0:
        return 1
    out = 1
    for x in range(n, 0, -2):
        out *= x
    return out


def pairings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j+1:]
        for p in pairings(rest):
            yield ((a, b),) + p


def tree_counts(degs, pairing):
    owner = []
    for v, d in enumerate(degs):
        owner.extend([v] * d)
    n = len(degs)
    adj = [set() for _ in range(n)]
    edges = []
    for h1, h2 in pairing:
        u, v = owner[h1], owner[h2]
        edges.append((u, v))
        if u != v:
            adj[u].add(v)
            adj[v].add(u)
    seen = set()
    counts = defaultdict(int)
    for root in range(n):
        if root in seen:
            continue
        stack = [root]
        seen.add(root)
        comp = []
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        S = set(comp)
        e = sum(1 for u, v in edges if u in S and v in S)
        if len(comp) >= 2 and e == len(comp) - 1:
            counts[len(comp)] += 1
    return counts


def coeff_single(degs, k, K=None):
    if K is None:
        K = 10**9
    total = 0
    for S in combinations(range(len(degs)), k):
        ds = [degs[i] for i in S]
        if any(d > K for d in ds) or sum(ds) != 2*k - 2:
            continue
        prod = 1
        for d in ds:
            prod *= d
        total += prod
    return total


def coeff_joint(degs, k, ell, K=None):
    if K is None:
        K = 10**9
    n = len(degs)
    total = 0
    universe = tuple(range(n))
    for S in combinations(universe, k):
        if any(degs[i] > K for i in S):
            continue
        if sum(degs[i] for i in S) != 2*k - 2:
            continue
        Sset = set(S)
        rem = [i for i in universe if i not in Sset]
        for T in combinations(rem, ell):
            if any(degs[i] > K for i in T):
                continue
            if sum(degs[i] for i in T) != 2*ell - 2:
                continue
            prod = 1
            for i in S:
                prod *= degs[i]
            for i in T:
                prod *= degs[i]
            total += prod
    return total


def formula_ET(degs, k, K=None):
    L = sum(degs)
    C = coeff_single(degs, k, K)
    if L - 2*k + 2 < 0:
        return Fraction(0)
    return Fraction(
        factorial(k-2) * odd_df(L-2*k+1) * C,
        odd_df(L-1),
    )


def formula_joint(degs, k, ell, K=None):
    L = sum(degs)
    D = coeff_joint(degs, k, ell, K)
    if L - 2*k - 2*ell + 4 < 0:
        return Fraction(0)
    return Fraction(
        factorial(k-2) * factorial(ell-2)
        * odd_df(L-2*k-2*ell+3) * D,
        odd_df(L-1),
    )


def brute(degs):
    L = sum(degs)
    assert L % 2 == 0 and L <= 12
    ps = list(pairings(range(L)))
    denom = len(ps)
    ET = defaultdict(int)
    EJ = defaultdict(int)
    for p in ps:
        c = tree_counts(degs, p)
        for k in range(2, len(degs)+1):
            ET[k] += c[k]
        for k in range(2, len(degs)+1):
            for ell in range(2, len(degs)+1):
                EJ[(k, ell)] += c[k]*c[ell] - (c[k] if k == ell else 0)
    return (
        denom,
        {k: Fraction(v, denom) for k, v in ET.items()},
        {(k, ell): Fraction(v, denom) for (k, ell), v in EJ.items()},
    )


TESTS = [
    [1, 1, 2, 2, 2, 2],
    [1, 1, 1, 1, 3, 3],
    [1, 1, 1, 1, 2, 2],
    [1, 1, 1, 1, 1, 1, 3, 3],
]

all_ok = True
for degs in TESTS:
    denom, ET, EJ = brute(degs)
    print(f"degrees={degs} L={sum(degs)} pairings={denom}")
    for k in range(2, len(degs)+1):
        lhs = ET.get(k, Fraction(0))
        rhs = formula_ET(degs, k)
        if lhs != rhs:
            all_ok = False
            print("  SINGLE_FAIL", k, lhs, rhs)
        elif lhs:
            print("  single", k, lhs)
    for k in range(2, len(degs)+1):
        for ell in range(2, len(degs)+1):
            lhs = EJ.get((k, ell), Fraction(0))
            rhs = formula_joint(degs, k, ell)
            if lhs != rhs:
                all_ok = False
                print("  JOINT_FAIL", k, ell, lhs, rhs)
    print("  joint_identity=PASS")

# Genuine cutoff check (K=2): delete every tree using a degree-3 vertex.
degs = [1, 1, 1, 1, 3, 3]
K = 2
denom, _, _ = brute(degs)
ps = list(pairings(range(sum(degs))))
cut_ET = defaultdict(int)
owner = []
for v, d in enumerate(degs):
    owner.extend([v] * d)


def cutoff_tree_counts(pairing):
    n = len(degs)
    adj = [set() for _ in range(n)]
    edges = []
    for h1, h2 in pairing:
        u, v = owner[h1], owner[h2]
        edges.append((u, v))
        if u != v:
            adj[u].add(v)
            adj[v].add(u)
    seen = set()
    out = defaultdict(int)
    for root in range(n):
        if root in seen:
            continue
        stack = [root]
        seen.add(root)
        comp = []
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        S = set(comp)
        e = sum(1 for u, v in edges if u in S and v in S)
        if (len(comp) >= 2 and e == len(comp)-1
                and all(degs[v] <= K for v in comp)):
            out[len(comp)] += 1
    return out


for p in ps:
    c = cutoff_tree_counts(p)
    for k, v in c.items():
        cut_ET[k] += v
for k in range(2, len(degs)+1):
    lhs = Fraction(cut_ET[k], denom)
    rhs = formula_ET(degs, k, K=K)
    if lhs != rhs:
        all_ok = False
        print("CUTOFF_FAIL", k, lhs, rhs)
print("cutoff_identity=PASS" if all_ok else "cutoff_identity=FAIL")
print("ALL_EXACT_CHECKS_PASS =", all_ok)
if not all_ok:
    raise SystemExit(1)
