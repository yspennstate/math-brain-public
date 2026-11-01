#!/usr/bin/env python3
"""Finite-state certificate for HARD10-03 NEW-L49/50/51.

This is a sanity checker, not a proof of the infinite-volume theorem. It
enumerates all permutations and set partitions of C4, then exactly checks the
deterministic Möbius identity / balanced crossing structure and numerically
checks the probability-level merge-defect bounds under the beta=1 interchange
semigroup.
"""

import itertools
import json
import math
import numpy as np
from scipy.linalg import expm

N = 4
EDGES = [(0,1),(1,2),(2,3),(3,0)]
BETA = 1.0
A = tuple(range(N))


def set_partitions(seq):
    seq = list(seq)
    if not seq:
        yield tuple()
        return
    first = seq[0]
    for rest in set_partitions(seq[1:]):
        yield tuple(sorted(((first,),) + rest))
        for i in range(len(rest)):
            blocks = [tuple(b) for b in rest]
            blocks[i] = tuple(sorted(blocks[i] + (first,)))
            yield tuple(sorted(blocks))


def canon(part):
    return tuple(sorted(tuple(sorted(b)) for b in part))


PARTS = sorted(set(canon(p) for p in set_partitions(A)), key=lambda p: (len(p), p))
TOP = (A,)


def refines(pi, sig):
    return all(any(set(b) <= set(c) for c in sig) for b in pi)


def join(pi, rho):
    parent = list(range(N))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for part in (pi, rho):
        for b in part:
            for x in b[1:]:
                union(b[0], x)
    groups = {}
    for x in A:
        groups.setdefault(find(x), []).append(x)
    return canon(tuple(tuple(v) for v in groups.values()))


def mob_to_top(pi):
    k = len(pi)
    return (-1) ** (k - 1) * math.factorial(k - 1)


def all_perms(n):
    return list(itertools.permutations(range(n)))


PS = all_perms(N)
IDX = {p: i for i, p in enumerate(PS)}


def ring(p, edge):
    u, v = edge
    q = list(p)
    for i, x in enumerate(q):
        if x == u:
            q[i] = v
        elif x == v:
            q[i] = u
    return tuple(q)


Q = np.zeros((len(PS), len(PS)))
for i, p in enumerate(PS):
    for e in EDGES:
        q = ring(p, e)
        Q[i, IDX[q]] += 1.0
        Q[i, i] -= 1.0
MU = expm(BETA * Q)[IDX[tuple(range(N))]]

L = np.zeros((N, N))
for u, v in EDGES:
    L[u, v] += 1.0
    L[v, u] += 1.0
    L[u, u] -= 1.0
    L[v, v] -= 1.0
K = expm(BETA * L)


def cycles_partition(p):
    seen = set()
    blocks = []
    for x in A:
        if x in seen:
            continue
        cyc = []
        y = x
        while y not in seen:
            seen.add(y)
            cyc.append(y)
            y = p[y]
        blocks.append(tuple(sorted(cyc)))
    return canon(tuple(blocks))


def event_E(p, pi):
    for b in pi:
        sb = set(b)
        if {p[x] for x in b} != sb:
            return False
    return True


def block_idx(pi, x):
    for i, b in enumerate(pi):
        if x in b:
            return i
    raise KeyError(x)


def block_graph_info(p, pi):
    k = len(pi)
    edges = []
    indeg = [0] * k
    outdeg = [0] * k
    adj = [set() for _ in range(k)]
    for x in A:
        i = block_idx(pi, x)
        j = block_idx(pi, p[x])
        if i != j:
            edges.append((i, j, x, p[x]))
            outdeg[i] += 1
            indeg[j] += 1
            adj[i].add(j)
            adj[j].add(i)
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j in adj[i]:
            if j not in seen:
                seen.add(j)
                stack.append(j)
    return edges, indeg, outdeg, len(seen) == k


max_det_error = 0
bad_balance = 0
bad_conn_equiv = 0
bad_edgecount = 0
for p in PS:
    rho = cycles_partition(p)
    for pi0 in PARTS:
        lhs = sum(
            mob_to_top(sig) * (1 if event_E(p, sig) else 0)
            for sig in PARTS
            if refines(pi0, sig)
        )
        rhs = 1 if join(pi0, rho) == TOP else 0
        max_det_error = max(max_det_error, abs(lhs - rhs))
        if len(pi0) >= 2:
            edges, indeg, outdeg, conn = block_graph_info(p, pi0)
            jconn = join(pi0, rho) == TOP
            if indeg != outdeg:
                bad_balance += 1
            if conn != jconn:
                bad_conn_equiv += 1
            if jconn and len(edges) < len(pi0):
                bad_edgecount += 1

R = {
    pi: sum(float(pr) for p, pr in zip(PS, MU) if event_E(p, pi))
    for pi in PARTS
}
mob_prob = sum(mob_to_top(pi) * R[pi] for pi in PARTS)
actual_one = sum(float(pr) for p, pr in zip(PS, MU) if len(cycles_partition(p)) == 1)

max_one_violation = -1e99
max_two_violation = -1e99
n_adj = 0
max_defect = 0.0
for pi in PARTS:
    if len(pi) < 2:
        continue
    for a in range(len(pi)):
        for b in range(a + 1, len(pi)):
            B = set(pi[a])
            C = set(pi[b])
            blocks = [set(x) for x in pi]
            merged = B | C
            new = [blocks[i] for i in range(len(blocks)) if i not in (a, b)] + [merged]
            pip = canon(tuple(tuple(sorted(x)) for x in new))
            defect = R[pip] - R[pi]
            max_defect = max(max_defect, defect)
            one = sum(K[x, y] for x in B for y in C)
            two = 0.0
            for x in B:
                for c in C:
                    for y in C:
                        for z in B:
                            two += sum(
                                float(pr)
                                for p, pr in zip(PS, MU)
                                if p[x] == y and p[c] == z
                            )
            max_one_violation = max(max_one_violation, defect - one)
            max_two_violation = max(max_two_violation, defect - two)
            n_adj += 1

result = {
    "graph": "C4",
    "beta": BETA,
    "num_permutations": len(PS),
    "num_partitions": len(PARTS),
    "NEW_L49_max_deterministic_error": max_det_error,
    "NEW_L51_bad_balance_count": bad_balance,
    "NEW_L51_bad_connectivity_equivalence_count": bad_conn_equiv,
    "NEW_L51_bad_min_cross_edge_count": bad_edgecount,
    "probability_one_cycle_actual": actual_one,
    "probability_one_cycle_mobius": mob_prob,
    "probability_mobius_error": abs(actual_one - mob_prob),
    "adjacent_partition_pairs_checked": n_adj,
    "NEW_L50_max_one_particle_bound_violation": max_one_violation,
    "NEW_L50_max_two_tag_bound_violation": max_two_violation,
    "NEW_L50_max_defect": max_defect,
    "PASS": bool(
        max_det_error == 0
        and bad_balance == 0
        and bad_conn_equiv == 0
        and bad_edgecount == 0
        and abs(actual_one - mob_prob) < 1e-12
        and max_one_violation < 1e-12
        and max_two_violation < 1e-12
    ),
}
print(json.dumps(result, indent=2, sort_keys=True))
