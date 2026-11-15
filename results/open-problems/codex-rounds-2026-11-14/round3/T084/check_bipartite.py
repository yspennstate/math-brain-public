#!/usr/bin/env python3
"""Exact two-edge random-cluster counts. Standard library, one thread."""
import argparse
from collections import defaultdict
from functools import lru_cache
from math import comb
import json
import os
from pathlib import Path
import resource
import signal
import time


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(p, r, scale=1):
    out = defaultdict(int, p)
    for k, v in r.items():
        out[k] += scale * v
    return clean(out)


def mul(p, r):
    out = defaultdict(int)
    for (i, j), a in p.items():
        for (k, l), b in r.items():
            out[i+k, j+l] += a*b
    return clean(out)


def shift(p, di=0, dj=0):
    out = {(i+di, j+dj): v for (i, j), v in p.items()}
    assert all(i >= 0 and j >= 0 for i, j in out)
    return out


def edge_sectors(nv, edges, e, f):
    """Union-find enumeration, recording q^k w^(|A|-i-j)."""
    out = [defaultdict(int) for _ in range(4)]
    for mask in range(1 << len(edges)):
        parent = list(range(nv))
        k = nv
        for g, (u, v) in enumerate(edges):
            if not (mask >> g) & 1:
                continue
            while parent[u] != u:
                u = parent[u]
            while parent[v] != v:
                v = parent[v]
            if u != v:
                parent[u] = v
                k -= 1
        i, j = (mask >> e) & 1, (mask >> f) & 1
        out[i+2*j][k, mask.bit_count()-i-j] += 1
    return [dict(p) for p in out]


def vertex_partition(nv, edges):
    """Independent computation from connected induced-subgraph polynomials.

    C[S]=(1+w)^m(S)-sum C[T](1+w)^m(S minus T), where T contains
    the least vertex and is a proper subset of S. Then Z[S]=sum
    q C[T] Z[S minus T], with T any subset containing that vertex.
    """
    @lru_cache(None)
    def all_subgraphs(s):
        m = sum(bool(s & (1 << u) and s & (1 << v)) for u, v in edges)
        return {(0, j): comb(m, j) for j in range(m+1)}

    @lru_cache(None)
    def connected(s):
        p = all_subgraphs(s)
        root = s & -s
        t = (s-1) & s
        while t:
            if t & root:
                p = add(p, mul(connected(t), all_subgraphs(s ^ t)), -1)
            t = (t-1) & s
        return p

    @lru_cache(None)
    def partition(s):
        if not s:
            return {(0, 0): 1}
        root = s & -s
        p = {}
        t = s
        while t:
            if t & root:
                p = add(p, shift(mul(connected(t), partition(s ^ t)), di=1))
            t = (t-1) & s
        return p

    return partition((1 << nv)-1)


def independent_sectors(nv, edges, e, f):
    z = {}
    for forbidden in ((), (e,), (f,), (e, f)):
        z[forbidden] = vertex_partition(nv, [uv for i, uv in enumerate(edges)
                                                    if i not in forbidden])
    a = z[e, f]
    b = shift(add(z[f,], a, -1), dj=-1)
    c = shift(add(z[e,], a, -1), dj=-1)
    d = shift(add(add(add(z[()], z[e,], -1), z[f,], -1), a), dj=-2)
    return [a, b, c, d]


def uniform_counts(sectors, nv, forests):
    out = []
    for state, p in enumerate(sectors):
        marked = (state & 1) + (state >> 1)
        out.append(sum(v for (k, r), v in p.items()
                       if (k+r+marked == nv if forests else k == 1)))
    a, b, c, d = out
    return {"total": a+b+c+d, "edge_e": b+d, "edge_f": c+d,
            "both": d, "difference": b*c-a*d, "sectors": out}


def divide_one_minus_q(p):
    out = {}
    for j in sorted({j for i, j in p}):
        acc = 0
        for i in range(1 + max(i for i, jj in p if jj == j)):
            acc += p.get((i, j), 0)
            if acc:
                out[i, j] = acc
        assert acc == 0, ("not divisible by 1-q", j)
    return out


def transform(p, w_offset=0):
    """(1+t)^d p(t/(1+t), w_offset+x), d=degree_q(p)."""
    d = max(i for i, j in p)
    out = defaultdict(int)
    for (i, j), v in p.items():
        for a in range(d-i+1):
            for b in range(j+1):
                out[i+a, b] += v*comb(d-i, a)*comb(j, b)*w_offset**(j-b)
    return clean(out), d


def serial(p):
    return [[i, j, v] for (i, j), v in sorted(p.items())]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graphs", default="2,2;2,3;3,3;3,4")
    ap.add_argument("--mode", choices=["recheck", "certificate"], default="recheck")
    ap.add_argument("--output", default="")
    args = ap.parse_args()
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
    signal.alarm(1100)
    # This sandbox rejects setrlimit. Bound input size and report actual RSS.
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    print("nice_priority", os.getpriority(os.PRIO_PROCESS, 0), flush=True)
    start = time.monotonic()
    records = []
    for sizes in args.graphs.split(";"):
        m, n = map(int, sizes.split(","))
        assert m >= 2 and n >= 2 and m*n <= 16 and m+n <= 8
        edges = [(i, m+j) for i in range(m) for j in range(n)]
        # e=(0,0); same-left f=(0,1), same-right f=(1,0), disjoint f=(1,1).
        for name, f in [("same_left", 1), ("same_right", n), ("disjoint", n+1)]:
            s = edge_sectors(m+n, edges, 0, f)
            s2 = independent_sectors(m+n, edges, 0, f)
            assert s == s2, (m, n, name, "independent counts differ")
            row = {"m": m, "n": n, "orbit": name,
                   "forest": uniform_counts(s, m+n, True),
                   "connected": uniform_counts(s, m+n, False)}
            assert row["forest"]["difference"] > 0
            assert row["connected"]["difference"] > 0
            if args.mode == "certificate":
                a, b, c, d = s
                rayleigh = add(mul(b, c), mul(a, d), -1)
                qmin = min(i for i, j in rayleigh)
                wmin = min(j for i, j in rayleigh)
                reduced = shift(rayleigh, di=-qmin, dj=-wmin)
                reduced = divide_one_minus_q(reduced)
                row.update(q_power=qmin, w_power=wmin, reduced=serial(reduced))
                row["certificates"] = []
                for offset in [0, 1, 2]:
                    cert, degree = transform(reduced, offset)
                    bad = [(i, j, v) for (i, j), v in sorted(cert.items()) if v < 0]
                    row["certificates"].append({"offset": offset, "degree": degree,
                        "terms": len(cert), "negative_terms": len(bad),
                        "minimum": min(cert.values()), "polynomial": serial(cert)})
                    print("CERT", m, n, name, "offset", offset,
                          "terms", len(cert), "negative", len(bad),
                          "min", min(cert.values()), flush=True)
            print("COUNTS", m, n, name, "forest", row["forest"],
                  "connected", row["connected"], "independent_agreement=True", flush=True)
            records.append(row)
    if args.output:
        Path(args.output).write_text(json.dumps(records, indent=2)+"\n")
    print("elapsed_seconds", round(time.monotonic()-start, 3), flush=True)
    print("peak_rss_bytes", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, flush=True)


if __name__ == "__main__":
    main()
