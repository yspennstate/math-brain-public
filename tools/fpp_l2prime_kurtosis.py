"""Conditional kurtosis of the block-resampling increment in planar first-passage
percolation - the (L2') ladder, extendable past the sizes measured on 2026-08-15.

The campaign's settled row (U[1,2] weights on Z^2, exact Dijkstra, axis blocks,
four occupation points between 3.95 and 14.05 edges) reads the per-block
conditional kurtosis A4/(A2^+)^2 as SATURATING near 6.2 rather than growing, and
the earlier "growth" reading as a moving baseline. Nothing at those sizes bounds
anything asymptotic; what a larger ladder can do is confirm or break the
saturation reading itself. This tool reproduces the measurement so it can be
run at larger sizes on a research box.

Quantities, following the decomposition in the settled row. Fix a box of side n
with the passage time X from the left edge midpoint to the right edge midpoint
(exact Dijkstra on the edge weights). Choose an axis block L of side b centred on
the straight line between the endpoints at horizontal offset c. Resampling the
weights inside L gives X^L; the increment is Delta = X^L - X and only its
positive part is consumed by the engine. U_L is the event that the geodesic of
X touches L. Conditioned on U_L we estimate

    m2 = E[(Delta^+)^2 | U_L],  m4 = E[(Delta^+)^4 | U_L],  kurt = m4 / m2^2,

together with the occupation (mean number of geodesic edges inside L on U_L),
p_L = P(U_L), and the reroute fraction P(Delta^+ > 0 | U_L).

The read is pre-registered by the caller, not by this file: fix the occupation
ladder and the acceptance interval before looking at any output.
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
import random
import time


def _edges(n: int):
    """Undirected edges of the (n+1) x (n+1) grid, keyed (x, y, d) with d in {0, 1}
    for the edge from (x, y) to (x+1, y) or to (x, y+1)."""
    for x in range(n + 1):
        for y in range(n + 1):
            if x < n:
                yield (x, y, 0)
            if y < n:
                yield (x, y, 1)


def _neighbours(x: int, y: int, n: int):
    if x < n:
        yield (x + 1, y), (x, y, 0)
    if x > 0:
        yield (x - 1, y), (x - 1, y, 0)
    if y < n:
        yield (x, y + 1), (x, y, 1)
    if y > 0:
        yield (x, y - 1), (x, y - 1, 1)


def dijkstra(weights: dict, n: int, source, target):
    """Exact passage time and one geodesic (as an edge list) from source to target."""
    dist = {source: 0.0}
    prev = {}
    heap = [(0.0, source)]
    while heap:
        d, v = heapq.heappop(heap)
        if v == target:
            break
        if d > dist.get(v, math.inf):
            continue
        x, y = v
        for w, e in _neighbours(x, y, n):
            nd = d + weights[e]
            if nd < dist.get(w, math.inf):
                dist[w] = nd
                prev[w] = (v, e)
                heapq.heappush(heap, (nd, w))
    path = []
    v = target
    while v != source:
        u, e = prev[v]
        path.append(e)
        v = u
    return dist[target], path


def block_edges(n: int, b: int, cx: int, cy: int):
    """Edges with both endpoints inside the closed square [cx, cx+b] x [cy, cy+b]."""
    out = set()
    for x in range(cx, min(cx + b, n)):
        for y in range(cy, cy + b + 1):
            if y <= n:
                out.add((x, y, 0))
    for x in range(cx, cx + b + 1):
        for y in range(cy, min(cy + b, n)):
            if x <= n:
                out.add((x, y, 1))
    return out


def one_sample(rng: random.Random, n: int, b: int, offset: int, lo: float, hi: float):
    weights = {e: rng.uniform(lo, hi) for e in _edges(n)}
    mid = n // 2
    source, target = (0, mid), (n, mid)
    x_time, path = dijkstra(weights, n, source, target)
    cx = mid + offset - b // 2
    cy = mid - b // 2
    inside = block_edges(n, b, cx, cy)
    touched = [e for e in path if e in inside]
    if not touched:
        return None
    resampled = dict(weights)
    for e in inside:
        resampled[e] = rng.uniform(lo, hi)
    x_new, _ = dijkstra(resampled, n, source, target)
    delta_plus = max(0.0, x_new - x_time)
    return {"occupation": len(touched), "delta_plus": delta_plus}


def measure(n: int, b: int, offset: int, samples: int, seed: int, lo: float, hi: float):
    rng = random.Random(seed)
    touched = []
    trials = 0
    t0 = time.time()
    while len(touched) < samples:
        trials += 1
        s = one_sample(rng, n, b, offset, lo, hi)
        if s is not None:
            touched.append(s)
    d = [s["delta_plus"] for s in touched]
    m2 = sum(v * v for v in d) / len(d)
    m4 = sum(v ** 4 for v in d) / len(d)
    return {
        "n": n, "block": b, "offset": offset, "samples": len(d), "trials": trials,
        "p_touch": len(d) / trials,
        "occupation_mean": sum(s["occupation"] for s in touched) / len(d),
        "m2": m2, "m4": m4,
        "kurtosis": (m4 / (m2 * m2)) if m2 > 0 else None,
        "reroute_fraction": sum(1 for v in d if v > 0) / len(d),
        "seconds": round(time.time() - t0, 1),
    }


def bootstrap_kurtosis(deltas, reps: int, seed: int):
    rng = random.Random(seed)
    out = []
    k = len(deltas)
    for _ in range(reps):
        sample = [deltas[rng.randrange(k)] for _ in range(k)]
        m2 = sum(v * v for v in sample) / k
        m4 = sum(v ** 4 for v in sample) / k
        if m2 > 0:
            out.append(m4 / (m2 * m2))
    out.sort()
    return out[int(0.025 * len(out))], out[int(0.975 * len(out))]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--n", type=int, required=True, help="box side (edges)")
    ap.add_argument("--block", type=int, required=True, help="block side (edges)")
    ap.add_argument("--offset", type=int, default=0,
                    help="block centre offset along the axis from the box centre")
    ap.add_argument("--samples", type=int, default=200,
                    help="touched samples to collect (untouched trials are discarded)")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--lo", type=float, default=1.0)
    ap.add_argument("--hi", type=float, default=2.0)
    ap.add_argument("--bootstrap", type=int, default=0,
                    help="bootstrap replicates for a kurtosis interval (0 = none)")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    touched = []
    trials = 0
    t0 = time.time()
    while len(touched) < args.samples:
        trials += 1
        s = one_sample(rng, args.n, args.block, args.offset, args.lo, args.hi)
        if s is not None:
            touched.append(s)
    d = [s["delta_plus"] for s in touched]
    m2 = sum(v * v for v in d) / len(d)
    m4 = sum(v ** 4 for v in d) / len(d)
    out = {
        "n": args.n, "block": args.block, "offset": args.offset,
        "law": f"U[{args.lo},{args.hi}]", "seed": args.seed,
        "samples": len(d), "trials": trials, "p_touch": len(d) / trials,
        "occupation_mean": sum(s["occupation"] for s in touched) / len(d),
        "m2": m2, "m4": m4,
        "kurtosis": (m4 / (m2 * m2)) if m2 > 0 else None,
        "reroute_fraction": sum(1 for v in d if v > 0) / len(d),
        "seconds": round(time.time() - t0, 1),
    }
    if args.bootstrap:
        out["kurtosis_ci95"] = bootstrap_kurtosis(d, args.bootstrap, args.seed + 1)
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
