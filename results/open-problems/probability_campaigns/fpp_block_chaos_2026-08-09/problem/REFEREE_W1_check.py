# D1 witness check (2026-08-12): is the 9.5 support identity really false, and is the
# factor-2 bracket p*m_k <= E[Delta^k] <= 2*p*m_k really two-sided?
# Bond FPP on a 13x13 vertex grid, U[1,2] iid weights, exact Dijkstra, X = T((0,0),(12,12)).
# For each block Lambda: U = {geodesic of omega uses an edge of Lambda}, Delta = X^Lambda - X.
# Claims tested:
#   (W)  P(U^c and Delta < 0) > 0            -- the witness that "Delta = 0 off U" is false
#   (B2) p*m2 <= E[Delta^2] <= 2*p*m2        -- factor-2 bracket, second moment
#   (B4) p*m4 <= E[Delta^4] <= 2*p*m4        -- factor-2 bracket, fourth moment
#   (L43) Delta <= 0 on U^c pointwise         -- Lemma 4.3 invariant (harness sanity; must be exact)
import heapq, json, random, sys

try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

N = 12  # vertices (i,j), 0..N in each coordinate
SEED = 20260812
REPS = 6000

def edges_all():
    es = []
    for i in range(N + 1):
        for j in range(N + 1):
            if i < N: es.append(((i, j), (i + 1, j)))
            if j < N: es.append(((i, j), (i, j + 1)))
    return es

EDGES = edges_all()
EIDX = {e: k for k, e in enumerate(EDGES)}
ADJ = {}
for (u, v) in EDGES:
    ADJ.setdefault(u, []).append((v, EIDX[(u, v)]))
    ADJ.setdefault(v, []).append((u, EIDX[(u, v)]))

def dijkstra(w, src, dst):
    dist = {src: 0.0}
    prev = {}
    pq = [(0.0, src)]
    done = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in done: continue
        done.add(u)
        if u == dst: break
        for v, ei in ADJ[u]:
            nd = d + w[ei]
            if v not in dist or nd < dist[v] - 1e-15:
                dist[v] = nd
                prev[v] = (u, ei)
                heapq.heappush(pq, (nd, v))
    # recover geodesic edge set
    path_edges = set()
    cur = dst
    while cur != src:
        u, ei = prev[cur]
        path_edges.add(ei)
        cur = u
    return dist[dst], path_edges

def block_edges(i0, i1, j0, j1):
    # all edges with BOTH endpoints in [i0,i1]x[j0,j1]
    out = []
    for e, k in EIDX.items():
        (a, b) = e
        if i0 <= a[0] <= i1 and j0 <= a[1] <= j1 and i0 <= b[0] <= i1 and j0 <= b[1] <= j1:
            out.append(k)
    return out

BLOCKS = {
    "center_on_axis": block_edges(5, 7, 5, 7),    # diagonal corridor - p should be sizable
    "near_off_axis":  block_edges(5, 7, 8, 10),   # 3 above the corridor
    "far_corner":     block_edges(1, 3, 9, 11),   # well off - p small
}

rng = random.Random(SEED)
SRC, DST = (0, 0), (N, N)

acc = {name: {"p_cnt": 0, "s2": 0.0, "s4": 0.0, "s2_U": 0.0, "s4_U": 0.0,
              "off_neg_cnt": 0, "off_s2": 0.0, "off_max": 0.0, "l43_viol": 0}
       for name in BLOCKS}

for rep in range(REPS):
    w = [1.0 + rng.random() for _ in EDGES]
    X, geo = dijkstra(w, SRC, DST)
    for name, bl in BLOCKS.items():
        touched = any(ei in geo for ei in bl)
        w2 = list(w)
        for ei in bl:
            w2[ei] = 1.0 + rng.random()
        XL, _ = dijkstra(w2, SRC, DST)
        d = XL - X
        a = acc[name]
        a["s2"] += d * d
        a["s4"] += d ** 4
        if touched:
            a["p_cnt"] += 1
            a["s2_U"] += d * d
            a["s4_U"] += d ** 4
        else:
            if d > 1e-9:
                a["l43_viol"] += 1
            if d < -1e-12:
                a["off_neg_cnt"] += 1
                a["off_s2"] += d * d
                a["off_max"] = max(a["off_max"], -d)

out = {"seed": SEED, "reps": REPS, "grid": f"{N+1}x{N+1}", "blocks": {}}
for name, a in acc.items():
    p = a["p_cnt"] / REPS
    E2 = a["s2"] / REPS
    E4 = a["s4"] / REPS
    pm2 = a["s2_U"] / REPS          # = p * m2 by construction
    pm4 = a["s4_U"] / REPS
    out["blocks"][name] = {
        "n_edges": len(BLOCKS[name]),
        "p": round(p, 4),
        "E_D2": E2, "p_m2": pm2, "ratio2_E_over_pm2": (E2 / pm2 if pm2 > 0 else None),
        "E_D4": E4, "p_m4": pm4, "ratio4_E_over_pm4": (E4 / pm4 if pm4 > 0 else None),
        "witness_offU_neg_frac": a["off_neg_cnt"] / REPS,
        "witness_offU_E2_share_of_E_D2": (a["off_s2"] / a["s2"] if a["s2"] > 0 else None),
        "witness_offU_max_drop": a["off_max"],
        "lemma43_violations": a["l43_viol"],
    }
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "d1_witness_results.json", "w", encoding="utf-8"), indent=1)
for name, b in out["blocks"].items():
    print(f"{name}: p={b['p']}  E[D^2]/pm2={b['ratio2_E_over_pm2'] and round(b['ratio2_E_over_pm2'],4)}  "
          f"E[D^4]/pm4={b['ratio4_E_over_pm4'] and round(b['ratio4_E_over_pm4'],4)}  "
          f"offU-neg frac={b['witness_offU_neg_frac']:.4f}  offU share of E[D^2]={b['witness_offU_E2_share_of_E_D2'] and round(b['witness_offU_E2_share_of_E_D2'],4)}  "
          f"L4.3 viol={b['lemma43_violations']}")
