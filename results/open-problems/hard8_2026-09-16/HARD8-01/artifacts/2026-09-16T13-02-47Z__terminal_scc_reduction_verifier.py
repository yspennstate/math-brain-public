#!/usr/bin/env python3
"""Exact verifier for HARD8-01 checkpoint 8.

Exhaustive family:
  n=4;
  exactly one permutation letter p, ranging over all 24 permutations;
  an arbitrary nonempty subset of all 12 simple idempotents e_{s->t}.

For every synchronizing automaton, verify:
  * the permutation-orbit transfer digraph has one sink SCC;
  * the union U_C of that SCC is invariant;
  * the restricted core is synchronizing;
  * rt(A) <= rt(A_C) + sum_{outside orbits} m(m+1)/2.

All calculations are finite integer/set operations. No randomness, floating
point, external solver, or timeout inference is used.
"""
from collections import deque, Counter
from itertools import permutations


def apply_subset(mask, tr):
    out = 0
    m = mask
    while m:
        lb = m & -m
        i = lb.bit_length() - 1
        out |= 1 << tr[i]
        m -= lb
    return out


def reset_threshold(n, letters, start_mask=None):
    if start_mask is None:
        start_mask = (1 << n) - 1
    if start_mask & (start_mask - 1) == 0:
        return 0
    dist = {start_mask: 0}
    q = deque([start_mask])
    while q:
        S = q.popleft()
        d = dist[S]
        for tr in letters:
            T = apply_subset(S, tr)
            if T & (T - 1) == 0:
                return d + 1
            if T not in dist:
                dist[T] = d + 1
                q.append(T)
    return None


def cyclic_orbits(p):
    n = len(p)
    seen = [False] * n
    out = []
    for i in range(n):
        if seen[i]:
            continue
        cur = []
        x = i
        while not seen[x]:
            seen[x] = True
            cur.append(x)
            x = p[x]
        out.append(tuple(cur))
    return out


def sink_sccs(num_vertices, arcs):
    adj = [set() for _ in range(num_vertices)]
    radj = [set() for _ in range(num_vertices)]
    for a, b in arcs:
        if a == b:
            continue
        adj[a].add(b)
        radj[b].add(a)

    seen = set()
    order = []

    def dfs(v):
        seen.add(v)
        for w in adj[v]:
            if w not in seen:
                dfs(w)
        order.append(v)

    for v in range(num_vertices):
        if v not in seen:
            dfs(v)

    comp = [-1] * num_vertices
    comps = []

    def rdfs(v, c):
        comp[v] = c
        comps[c].append(v)
        for w in radj[v]:
            if comp[w] < 0:
                rdfs(w, c)

    for v in reversed(order):
        if comp[v] < 0:
            comps.append([])
            rdfs(v, len(comps) - 1)

    outgoing = [False] * len(comps)
    for a, b in arcs:
        if comp[a] != comp[b]:
            outgoing[comp[a]] = True

    return [comps[i] for i in range(len(comps)) if not outgoing[i]]


def main():
    n = 4
    perms = list(permutations(range(n)))
    idempotents = []
    meta = []
    for s in range(n):
        for t in range(n):
            if s == t:
                continue
            tr = list(range(n))
            tr[s] = t
            idempotents.append(tuple(tr))
            meta.append((s, t))

    checked = 0
    sync = 0
    theorem_cases = 0
    max_rt = 0
    sink_hist = Counter()
    strong_transfer = 0
    proper_cores = 0
    singleton_cores = 0
    min_slack = None
    max_slack = None

    for p in perms:
        orbits = cyclic_orbits(p)
        orbit_id = {}
        for j, O in enumerate(orbits):
            for x in O:
                orbit_id[x] = j
        arc_meta = [(orbit_id[s], orbit_id[t]) for s, t in meta]

        for emask in range(1, 1 << len(idempotents)):
            checked += 1
            chosen = [j for j in range(len(idempotents)) if (emask >> j) & 1]
            letters = [p] + [idempotents[j] for j in chosen]

            rt = reset_threshold(n, letters)
            if rt is None:
                continue
            sync += 1
            max_rt = max(max_rt, rt)

            arcs = [arc_meta[j] for j in chosen if arc_meta[j][0] != arc_meta[j][1]]
            sinks = sink_sccs(len(orbits), arcs)
            assert len(sinks) == 1
            C = sinks[0]
            sink_hist[len(C)] += 1
            if len(C) == len(orbits):
                strong_transfer += 1

            U = set()
            for oi in C:
                U.update(orbits[oi])
            m = len(U)
            if m < n:
                proper_cores += 1
            if m == 1:
                singleton_cores += 1

            U_mask = sum(1 << x for x in U)

            # Direct invariance check.
            for tr in letters:
                assert apply_subset(U_mask, tr) & ~U_mask == 0

            rt_core = reset_threshold(n, letters, U_mask)
            assert rt_core is not None

            outside_sizes = [len(O) for j, O in enumerate(orbits) if j not in C]
            bound = rt_core + sum(a * (a + 1) // 2 for a in outside_sizes)
            assert rt <= bound

            S = n - m
            coarse = rt_core + S * (S + 1) // 2
            assert bound <= coarse
            if rt_core <= (m - 1) ** 2:
                assert rt <= (n - 1) ** 2

            if m == 1:
                assert rt <= n * (n - 1) // 2

            slack = bound - rt
            min_slack = slack if min_slack is None else min(min_slack, slack)
            max_slack = slack if max_slack is None else max(max_slack, slack)
            theorem_cases += 1

    print("AUTOMATA_CHECKED", checked)
    print("SYNCHRONIZING", sync)
    print("THEOREM_CASES_VERIFIED", theorem_cases)
    print("MAX_RESET_THRESHOLD", max_rt)
    print("SINK_SCC_SIZE_DISTRIBUTION", sorted(sink_hist.items()))
    print("ORBIT_TRANSFER_STRONGLY_CONNECTED", strong_transfer)
    print("PROPER_TERMINAL_CORES", proper_cores)
    print("SINGLETON_TERMINAL_CORES", singleton_cores)
    print("MIN_BOUND_SLACK", min_slack)
    print("MAX_BOUND_SLACK", max_slack)
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
