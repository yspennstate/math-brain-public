"""MG3: geodesic disorder-chaos measurement for bond FPP on a Z^2 strip.

Single file, numpy + stdlib. Dijkstra on the implicit strip graph with
predecessor tracking; resample a Bernoulli(t) mask of edges; overlap of the
two geodesics' edge sets. Checkpointed one json line per completed cell-pair;
resume reconciles from the OUTPUT file (never a status stamp).

Usage:
  python mg3_chaos.py --law exp --n 128 --t 0.01 --pairs 3 --out results.jsonl [--seed-base 1000]
Weights: exp = Exp(1); uni = Uniform[0.5, 1.5]. Strip half-width 4*n^{0.75} (clipped
geodesics are voided and reported). Ties: continuous weights, measure-zero; no
explicit topmost tie-break (recorded as a modeling note).
"""
import argparse
import heapq
import json
import os

import numpy as np


def gen_weights(rng, law, shape):
    if law == "exp":
        return rng.exponential(1.0, shape).astype(np.float32)
    if law == "uni":
        return rng.uniform(0.5, 1.5, shape).astype(np.float32)
    raise ValueError(law)


def dijkstra_geodesic(H, V, n, W):
    """Source (0, W) -> target (n, W) in array coords (y shifted by +W).
    H[x, y]: edge (x,y)->(x+1,y), x in [0,n); V[x, y]: edge (x,y)->(x,y+1), y in [0,2W).
    Returns (time, set of edge ids, touched_boundary)."""
    ny = 2 * W + 1
    dist = np.full((n + 1, ny), np.inf, dtype=np.float64)
    pred = np.full((n + 1, ny), -1, dtype=np.int8)  # 0:from left,1:from right,2:from below,3:from above
    src = (0, W)
    dist[src] = 0.0
    pq = [(0.0, 0, W)]
    tx, ty = n, W
    while pq:
        d, x, y = heapq.heappop(pq)
        if d > dist[x, y]:
            continue
        if (x, y) == (tx, ty):
            break
        if x < n:
            nd = d + H[x, y]
            if nd < dist[x + 1, y]:
                dist[x + 1, y] = nd
                pred[x + 1, y] = 0
                heapq.heappush(pq, (nd, x + 1, y))
        if x > 0:
            nd = d + H[x - 1, y]
            if nd < dist[x - 1, y]:
                dist[x - 1, y] = nd
                pred[x - 1, y] = 1
                heapq.heappush(pq, (nd, x - 1, y))
        if y < ny - 1:
            nd = d + V[x, y]
            if nd < dist[x, y + 1]:
                dist[x, y + 1] = nd
                pred[x, y + 1] = 2
                heapq.heappush(pq, (nd, x, y + 1))
        if y > 0:
            nd = d + V[x, y - 1]
            if nd < dist[x, y - 1]:
                dist[x, y - 1] = nd
                pred[x, y - 1] = 3
                heapq.heappush(pq, (nd, x, y - 1))
    # walk back
    edges = set()
    x, y = tx, ty
    touched = False
    while (x, y) != (0, W):
        p = pred[x, y]
        if p == -1:
            raise RuntimeError("no predecessor on geodesic walk-back")
        if y in (0, ny - 1):
            touched = True
        if p == 0:
            edges.add(("H", x - 1, y)); x -= 1
        elif p == 1:
            edges.add(("H", x, y)); x += 1
        elif p == 2:
            edges.add(("V", x, y - 1)); y -= 1
        else:
            edges.add(("V", x, y)); y += 1
    return float(dist[tx, ty]), edges, touched


def run_pair(law, n, t, seed):
    W = max(8, int(4 * n ** 0.75))
    rng = np.random.default_rng(seed)
    H = gen_weights(rng, law, (n, 2 * W + 1))
    V = gen_weights(rng, law, (n + 1, 2 * W))
    T1, g1, b1 = dijkstra_geodesic(H, V, n, W)
    rng2 = np.random.default_rng(seed + 10 ** 9)
    if t > 0:
        mH = rng2.random(H.shape) < t
        mV = rng2.random(V.shape) < t
        H2 = H.copy(); V2 = V.copy()
        H2[mH] = gen_weights(rng2, law, (int(mH.sum()),))
        V2[mV] = gen_weights(rng2, law, (int(mV.sum()),))
    else:
        H2, V2 = H, V
    T2, g2, b2 = dijkstra_geodesic(H2, V2, n, W)
    ov = len(g1 & g2) / max(len(g1), len(g2))
    return {"law": law, "n": n, "t": t, "seed": seed, "T1": T1, "T2": T2,
            "len1": len(g1), "len2": len(g2), "overlap": round(ov, 6),
            "boundary": bool(b1 or b2)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--law", choices=["exp", "uni"], required=True)
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--t", type=float, required=True)
    ap.add_argument("--pairs", type=int, default=200)
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed-base", type=int, default=1000)
    a = ap.parse_args()
    done = set()
    if os.path.exists(a.out):
        with open(a.out, encoding="utf-8") as f:
            for ln in f:
                try:
                    r = json.loads(ln)
                    done.add((r["law"], r["n"], r["t"], r["seed"]))
                except (ValueError, KeyError):
                    pass
    with open(a.out, "a", encoding="utf-8") as out:
        for i in range(a.pairs):
            seed = a.seed_base + i
            if (a.law, a.n, a.t, seed) in done:
                continue
            rec = run_pair(a.law, a.n, a.t, seed)
            out.write(json.dumps(rec) + "\n")
            out.flush()
    print("done", a.law, a.n, a.t, "pairs", a.pairs)


if __name__ == "__main__":
    main()
