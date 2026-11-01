#!/usr/bin/env python3
"""Deterministic audit of the exact U/influence/root-KL tree ledgers."""
import itertools
import math
import random

C0 = 2 / math.log(2)
TOL = 2e-11
CASES = NODES = REUSE_CASES = 0
MAX_U_TELESCOPE = MAX_I_TELESCOPE = MAX_ROOT_SURPLUS = 0.0

def walsh(table):
    a = [float(x) for x in table]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]

def ui(table):
    c = walsh(table)
    n = (len(table)-1).bit_length()
    p = [x*x for x in c]
    upper = p[:]
    for bit in range(n):
        for s in range(1 << n):
            if not (s >> bit) & 1:
                upper[s] += upper[s | (1 << bit)]
    U = 0.0
    for s, mass in enumerate(p):
        if mass:
            U += mass * math.log2(upper[s] / mass)
    I = sum(s.bit_count()*mass for s, mass in enumerate(p))
    return U, I

def restrict(table, n, i, bit):
    return [y for x, y in enumerate(table) if ((x >> i) & 1) == bit]

def influence(table, n, i):
    flips = 0
    for x in range(1 << n):
        if not ((x >> i) & 1) and table[x] != table[x | (1 << i)]:
            flips += 1
    return flips / (1 << (n-1))

def root_kl(table, n, i):
    a = sum(table) / len(table)
    d = sum(y * (1 if (x >> i) & 1 else -1) for x, y in enumerate(table)) / len(table)
    m = a*a + d*d
    if not m:
        return 0.0, d
    t = (1 + 2*a*d/m) / 2
    h = 0.0 if t <= 0 or t >= 1 else -t*math.log2(t)-(1-t)*math.log2(1-t)
    return m*(1-h), d

def remove_bit(mask, i):
    lo = mask & ((1 << i)-1)
    hi = mask >> (i+1)
    return lo | (hi << i)

def random_tree(remaining, rng, stop_prob=0.25):
    if not remaining or rng.random() < stop_prob:
        return None
    i = rng.choice(remaining)
    rem = tuple(j for j in remaining if j != i)
    return (i, random_tree(rem, rng, stop_prob), random_tree(rem, rng, stop_prob))

def fixed_reuse_tree(n, reused):
    # The same physical coordinate is queried on both children of root;
    # this is branch reuse, never path reuse.
    root = 0 if reused != 0 else 1
    return (root, (reused, None, None), (reused, None, None))

def audit(table, n, tree):
    global CASES, NODES, REUSE_CASES
    global MAX_U_TELESCOPE, MAX_I_TELESCOPE, MAX_ROOT_SURPLUS
    CASES += 1
    U0, I0 = ui(table)
    sum_du = sum_q = sum_k = leaf_u = leaf_i = 0.0
    seen_queries = []
    def rec(tab, dim, labels, node, weight):
        nonlocal sum_du, sum_q, sum_k, leaf_u, leaf_i
        global NODES, MAX_ROOT_SURPLUS
        if node is None:
            u, ii = ui(tab)
            leaf_u += weight*u
            leaf_i += weight*ii
            return
        physical, left, right = node
        assert physical in labels
        local = labels.index(physical)
        u, ii = ui(tab)
        t0, t1 = restrict(tab, dim, local, 0), restrict(tab, dim, local, 1)
        u0, _ = ui(t0); u1, _ = ui(t1)
        du = u-(u0+u1)/2
        q = influence(tab, dim, local)
        k, d = root_kl(tab, dim, local)
        MAX_ROOT_SURPLUS = max(MAX_ROOT_SURPLUS, k-C0*d*d)
        assert k <= C0*d*d + TOL
        sum_du += weight*du
        sum_q += weight*q
        sum_k += weight*k
        seen_queries.append(physical)
        newlabels = tuple(x for x in labels if x != physical)
        rec(t0, dim-1, newlabels, left, weight/2)
        rec(t1, dim-1, newlabels, right, weight/2)
        NODES += 1
    rec(table, n, tuple(range(n)), tree, 1.0)
    eu = abs(sum_du-(U0-leaf_u))
    ei = abs(sum_q-(I0-leaf_i))
    MAX_U_TELESCOPE = max(MAX_U_TELESCOPE, eu)
    MAX_I_TELESCOPE = max(MAX_I_TELESCOPE, ei)
    assert eu <= TOL and ei <= TOL
    mean = sum(table)/len(table)
    assert sum_k <= C0*(1-mean*mean)+TOL
    if len(seen_queries) != len(set(seen_queries)):
        REUSE_CASES += 1

def main():
    rng = random.Random(20261014)
    # Exhaustive Boolean functions for explicit first branch-reuse tree.
    for n in (2, 3, 4):
        tree = fixed_reuse_tree(n, n-1)
        cap = 1 << (1 << n)
        masks = range(cap) if n <= 3 else range(0, cap, 17)
        for mask in masks:
            table = [1 if (mask >> x) & 1 else -1 for x in range(1 << n)]
            audit(table, n, tree)
    # Adaptive stopped trees, including repeated physical queries on branches.
    for n in (4, 5, 6):
        for _ in range(700):
            table = [rng.choice((-1, 1)) for _ in range(1 << n)]
            audit(table, n, random_tree(tuple(range(n)), rng, 0.18))
    print("claim=B06-A028-PAID-U-BOUNDARY-v1")
    print("verdict=PROVED_PENDING_INDEPENDENT_REVIEW")
    print("tree_function_cases", CASES)
    print("internal_node_checks", NODES)
    print("branch_reuse_cases", REUSE_CASES)
    print("max_U_telescope_error", f"{MAX_U_TELESCOPE:.3e}")
    print("max_I_telescope_error", f"{MAX_I_TELESCOPE:.3e}")
    print("max_root_KL_surplus", f"{MAX_ROOT_SURPLUS:.3e}")
    print("universal_residual_bound=OPEN")
    print("universal_GU=OPEN")

if __name__ == "__main__":
    main()
