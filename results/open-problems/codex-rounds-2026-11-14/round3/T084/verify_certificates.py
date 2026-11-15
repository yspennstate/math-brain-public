#!/usr/bin/env python3
"""Independent certificate audit using flood-fill counts and dense polynomials.

No imports from the generator. Identities are checked after transforming
each sector separately, without division by q or (1-q).
"""
import argparse
from collections import Counter, defaultdict
import json
from math import comb
import os
from pathlib import Path
import resource
import signal
import time


def plus(a, b, sign=1):
    out = [r[:] for r in a]
    for i, row in enumerate(b):
        for j, v in enumerate(row):
            out[i][j] += sign*v
    return out


def product(a, b, height, width):
    out = [[0]*width for _ in range(height)]
    for i, row in enumerate(a):
        for j, u in enumerate(row):
            if not u:
                continue
            for k, other in enumerate(b):
                for l, v in enumerate(other):
                    if v:
                        assert i+k < height and j+l < width
                        out[i+k][j+l] += u*v
    return out


def counts(nv, edges, marked):
    sectors = [Counter() for _ in range(4)]
    for mask in range(2**len(edges)):
        adjacency = [0]*nv
        present = [g for g in range(len(edges)) if mask & (1 << g)]
        for g in present:
            u, v = edges[g]
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
        unseen, components = (1 << nv)-1, 0
        while unseen:
            components += 1
            frontier = unseen & -unseen
            unseen ^= frontier
            while frontier:
                u = (frontier & -frontier).bit_length()-1
                frontier &= frontier-1
                new = adjacency[u] & unseen
                unseen ^= new
                frontier |= new
        i, j = [int(g in present) for g in marked]
        sectors[i+2*j][components, len(present)-i-j] += 1
    return sectors


def left_partitions(m):
    def generate(v, blocks):
        if v == m:
            yield blocks
            return
        for i in range(len(blocks)):
            yield from generate(v+1, blocks[:i]+[blocks[i]+[v]]+blocks[i+1:])
        yield from generate(v+1, blocks+[[v]])
    yield from generate(0, [])


def potts_counts(m, n, e, f):
    """Third exact count for K_5,5, by the polynomial Potts spin identity.

    Sum over equality partitions pi of the left spins:
    (q)_{|pi|} product_right [q-|pi| + sum_B product_left_in_B (1+x_lr)].
    This holds for every integer q >= m and hence as a polynomial in q.
    Marked-edge monomials are represented by a two-bit mask.
    """
    def times(a, b):
        out = defaultdict(int)
        for (i,j,state), u in a.items():
            for (k,l,extra), v in b.items():
                assert not state & extra
                out[i+k,j+l,state | extra] += u*v
        return {key: v for key,v in out.items() if v}

    total = defaultdict(int)
    partition_count = 0
    for blocks in left_partitions(m):
        partition_count += 1
        p = {(0,0,0): 1}
        for k in range(len(blocks)):
            factor = {(1,0,0): 1}
            if k:
                factor[0,0,0] = -k
            p = times(p, factor)
        for right in range(n):
            factor = defaultdict(int, {(1,0,0): 1})
            for block in blocks:
                marked_here = [bit for bit, (left,col) in enumerate((e,f))
                               if col == right and left in block]
                plain = len(block)-len(marked_here)
                for sub in range(1 << len(marked_here)):
                    state = sum(1 << bit for i,bit in enumerate(marked_here)
                                if sub & (1 << i))
                    for r in range(plain+1):
                        if state or r:
                            factor[0,r,state] += comb(plain,r)
            p = times(p, factor)
        for key, v in p.items():
            total[key] += v
    assert partition_count == 52
    sectors = [Counter() for _ in range(4)]
    for (q_degree, weight_degree, state), v in total.items():
        assert v >= 0
        if v:
            sectors[state][q_degree,weight_degree] = v
    return sectors


def transform_sector(s, nv, height, width):
    out = [[0]*width for _ in range(height)]
    for (k, r), count in s.items():
        for j in range(nv-k+1):
            out[k+j][r] += count*comb(nv-k, j)
    return out


def endpoint_sector(s, nv, state, forests, width):
    p = [[0]*width]
    marked = (state & 1) + (state >> 1)
    for (k, r), count in s.items():
        if k+r+marked == nv if forests else k == 1:
            p[0][r] += count
    return p


def nonzero_univariate(p):
    return [[j, v] for j, v in enumerate(p[0]) if v]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="certificates.json")
    ap.add_argument("--summary", default="verified_summary.json")
    args = ap.parse_args()
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
    signal.alarm(1100)
    print("nice_priority", os.getpriority(os.PRIO_PROCESS, 0), flush=True)
    start = time.monotonic()
    data = json.loads(Path(args.input).read_text())
    summaries = []
    for row in data:
        m, n, name = row["m"], row["n"], row["orbit"]
        assert (m*n <= 16 and m+n <= 8) or (m,n) == (5,5)
        nv = m+n
        edges = [(i, m+j) for i in range(m) for j in range(n)]
        f = {"same_left": 1, "same_right": n, "disjoint": n+1}[name]
        if (m,n) == (5,5):
            marked_f = {"same_left": (0,1), "same_right": (1,0), "disjoint": (1,1)}[name]
            sectors = potts_counts(m,n,(0,0),marked_f)
            stored = [dict(((i,j),v) for i,j,v in s) for s in row["sectors"]]
            assert sectors == stored, "Potts/transfer/vertex counts differ"
        else:
            sectors = counts(nv, edges, (0, f))
        width, height = 2*len(edges)+1, 2*nv+1
        # A*,B*,C*,D* = (1+t)^nv A,B,C,D evaluated at q=t/(1+t).
        transformed = [transform_sector(s, nv, height, width) for s in sectors]
        a, b, c, d = transformed
        lhs = plus(product(b, c, height, width), product(a, d, height, width), -1)
        cert = row["certificates"][0]
        assert cert["offset"] == 0
        assert row["q_power"] == 2 and row["w_power"] == 2
        degree = cert["degree"]
        assert degree == 2*nv-6
        rhs = [[0]*width for _ in range(height)]
        exponent = 2*nv - row["q_power"] - 1 - degree
        assert exponent == 3
        entries = cert["polynomial"]
        assert len({(i, j) for i, j, v in entries}) == len(entries)
        assert len(entries) == cert["terms"]
        assert min(v for i, j, v in entries) == cert["minimum"]
        assert all(v > 0 for i, j, v in entries)
        assert cert["negative_terms"] == 0
        assert max(i for i, j, v in entries) == degree
        for i, j, v in entries:
            for k in range(exponent+1):
                rhs[i+row["q_power"]+k][j+row["w_power"]] += v*comb(exponent, k)
        assert lhs == rhs, (m, n, name, "certificate identity")

        endpoints = {}
        for forests in [True, False]:
            parts = [endpoint_sector(s, nv, state, forests, width)
                     for state, s in enumerate(sectors)]
            a, b, c, d = parts
            difference = plus(product(b, c, 1, width), product(a, d, 1, width), -1)
            coefficients = nonzero_univariate(difference)
            assert coefficients and all(v > 0 for j, v in coefficients)
            predicted = [[0]*width]
            if forests:
                assert min(i+j for i, j, v in entries) == degree
                for i, j, v in entries:
                    if i+j == degree:
                        predicted[0][j+2] += v
            else:
                for i, j, v in entries:
                    if i == 0:
                        predicted[0][j+2] += v
            assert difference == predicted, (m, n, name, "endpoint extraction")
            # Independent magnitude check from the complete-bipartite tree kernel.
            tau = m**(n-1)*n**(m-1)
            numerator = {"same_left": m-1, "same_right": n-1,
                         "disjoint": -1}[name]
            tree_difference = tau*tau*numerator*numerator // ((m*n)**2)
            assert tau*tau*numerator*numerator % ((m*n)**2) == 0
            assert difference[0][2*nv-4] == tree_difference
            if forests:
                four_cycles = {"same_left": m-1, "same_right": n-1,
                               "disjoint": 1}[name]
                assert difference[0][2] == four_cycles
            label = "forest" if forests else "connected"
            # Recheck every reported uniform count from independently counted sectors.
            a0, b0, c0, d0 = [sum(p[0]) for p in parts]
            computed = {"total": a0+b0+c0+d0, "edge_e": b0+d0,
                        "edge_f": c0+d0, "both": d0,
                        "difference": b0*c0-a0*d0, "sectors": [a0,b0,c0,d0]}
            assert computed == row[label]
            assert sum(v for j, v in coefficients) == row[label]["difference"]
            endpoints[label] = coefficients
        summary = {"m": m, "n": n, "orbit": name, "degree": degree,
                   "terms": len(entries), "minimum": min(v for i,j,v in entries),
                   "endpoints": endpoints}
        summaries.append(summary)
        print("VERIFIED", m, n, name, "identity=True", "degree", degree,
              "positive_terms", len(entries), "endpoints", endpoints, flush=True)
    # Transposition symmetry on the two balanced graphs is an additional audit.
    for m, n in [(3,3),(4,4),(5,5)]:
        rows = [r for r in data if (r["m"],r["n"]) == (m,n)]
        if rows:
            assert rows[0]["certificates"][0] == rows[1]["certificates"][0]
    Path(args.summary).write_text(json.dumps(summaries, indent=2)+"\n")
    print("ALL_PASSED", len(summaries), flush=True)
    print("elapsed_seconds", round(time.monotonic()-start, 3), flush=True)
    print("peak_rss_bytes", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, flush=True)


if __name__ == "__main__":
    main()
