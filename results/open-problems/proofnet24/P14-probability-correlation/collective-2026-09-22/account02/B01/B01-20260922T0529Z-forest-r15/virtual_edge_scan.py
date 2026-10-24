#!/usr/bin/env python3
"""Exact finite regression for the one-virtual-edge 2-cut scalar.

For fixed terminals 0,1 and each orbit of two marked physical edges e,f,
this enumerates every labelled simple graph B on n vertices, n=6,7. It
computes exact forest counts by subset zeta transform and tests whether the
Rayleigh gap for e,f can become negative when a NEW virtual terminal edge
gets arbitrary activity s>=0 while every physical edge has activity 1.

This is only finite regression evidence; it is not universal closure.
"""
from itertools import combinations, permutations
import numpy as np


def forest_masks(n):
    edges = list(combinations(range(n), 2))
    masks, conn = [], []
    for k in range(n):
        for comb in combinations(range(len(edges)), k):
            parent = list(range(n)); mask = 0; ok = True
            def find(a):
                while parent[a] != a:
                    parent[a] = parent[parent[a]]; a = parent[a]
                return a
            for j in comb:
                u, v = edges[j]; ru, rv = find(u), find(v)
                if ru == rv:
                    ok = False; break
                parent[ru] = rv; mask |= 1 << j
            if ok:
                masks.append(mask); conn.append(find(0) == find(1))
    return edges, np.asarray(masks, dtype=np.int64), np.asarray(conn, dtype=bool)


def pair_orbit_reps(n, edges):
    edge_index = {e:i for i,e in enumerate(edges)}; group = []
    for swap in (False, True):
        for pints in permutations(range(2, n)):
            mp = {0:1 if swap else 0, 1:0 if swap else 1}
            for old, new in zip(range(2, n), pints): mp[old] = new
            group.append(mp)
    unseen = set(combinations(range(len(edges)), 2)); reps = []
    while unseen:
        pair = next(iter(unseen)); orbit = set()
        for mp in group:
            mapped = []
            for idx in pair:
                a,b = edges[idx]
                mapped.append(edge_index[tuple(sorted((mp[a],mp[b])))])
            orbit.add(tuple(sorted(mapped)))
        reps.append(pair); unseen -= orbit
    return reps


def zeta_inplace(arr, m):
    for bit in range(m):
        step = 1 << bit
        view = arr.reshape(arr.shape[0], -1, 2*step)
        view[:,:,step:] += view[:,:,:step]


def scan(n):
    edges, fm, connected = forest_masks(n)
    m, N = len(edges), 1 << len(edges)
    reps = pair_orbit_reps(n, edges); failures = []
    masks = np.arange(N, dtype=np.int64)
    for ei, fi in reps:
        arr = np.zeros((8, N), dtype=np.int32)
        eb = ((fm >> ei) & 1).astype(np.int8)
        fb = ((fm >> fi) & 1).astype(np.int8)
        cls = connected.astype(np.int8)*4 + eb*2 + fb
        for k in range(8): arr[k, fm[cls == k]] = 1
        zeta_inplace(arr, m)
        d00,d01,d10,d11,c00,c01,c10,c11 = [arr[k].astype(np.int64, copy=False) for k in range(8)]
        q2 = d10*d01 - d00*d11
        q1 = d10*c01 + c10*d01 - d00*c11 - c00*d11
        q0 = c10*c01 - c00*c11
        valid = (((masks >> ei) & 1) != 0) & (((masks >> fi) & 1) != 0)
        r1 = q2 + q1 + q0
        disc = q1*q1 - 4*q2*q0
        bad = valid & ((q2 < 0) | ((q2 == 0) & (q1 < 0)) | ((q2 > 0) & (q1 < -2*q2) & (disc > 0)) | (r1 < 0))
        where = np.flatnonzero(bad)
        if len(where):
            g = int(where[0]); failures.append((ei,fi,g,int(q0[g]),int(q1[g]),int(q2[g]))); break
    instances = (m*(m-1)//2) * (1 << (m-2))
    print(f"n={n} edges={m} forest_masks={len(fm)} graph_masks={N} pair_orbits={len(reps)} marked_graph_pair_instances={instances} weighted_virtual_failures={len(failures)}")
    if failures:
        print("FIRST_FAILURE", failures[0]); raise SystemExit(1)


if __name__ == "__main__":
    scan(6); scan(7); print("VIRTUAL_EDGE_N7_EXACT_SCAN_PASS")
