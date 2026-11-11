# Fast kernel. p_e(w) = P_w(walk from N crosses e before hitting F) from ONE Green's matrix:
# with G = (I - P)^-1 (row F of P zero), a = P[u,v], b = P[v,u], g = G[N,:],
#   p_e = ( a g_u (1 + b (G_uv - G_vv)) + b g_v (1 + a (G_vu - G_uu)) ) / ( (1 + a G_vu)(1 + b G_uv) - a b G_uu G_vv )
# (Woodbury on the chain killed at its first crossing of e). Checked against the per-edge solve in ants_core.pvals.
# Usage: python ants_fast.py test
#        python ants_fast.py NMIN NMAX STARTS WORKERS OUT.jsonl [SHARD NSHARDS]     (resumable: skips cases already in OUT)
import sys, itertools, json, os, time, numpy as np, networkx as nx
from multiprocessing import Pool
import ants_core as A

_slow = A.pvals

def pvals(n, E, w, N, F):
    Ea = np.asarray(E); u = Ea[:, 0]; v = Ea[:, 1]
    W = np.zeros((n, n)); np.add.at(W, (u, v), w); np.add.at(W, (v, u), w)
    if (np.asarray(w) <= 0).any():
        adj = W > 0; reach = np.zeros(n, bool); reach[N] = True
        for _ in range(n):
            new = reach | (adj[:, reach].any(1))
            if (new == reach).all(): break
            reach = new
        if not reach[F]: return None
        W[~reach, :] = 0; W[:, ~reach] = 0
    deg = W.sum(1)
    P = np.divide(W, deg[:, None], out=np.zeros_like(W), where=deg[:, None] > 0)
    P[F] = 0
    try:
        G = np.linalg.inv(np.eye(n) - P)
    except np.linalg.LinAlgError:
        return None
    g = G[N]
    a = P[u, v]; b = P[v, u]
    det = (1 + a * G[v, u]) * (1 + b * G[u, v]) - a * b * G[u, u] * G[v, v]
    p = (a * g[u] * (1 + b * (G[u, v] - G[v, v])) + b * g[v] * (1 + a * (G[v, u] - G[u, u]))) / det
    return p, g.copy(), deg

# The Woodbury kernel carries ~1e-10 cancellation noise, enough to create spurious roots at marginal zeros.
# Classification runs use the exact per-edge solve unless ANTS_KERNEL=fast is set.
if os.environ.get("ANTS_KERNEL", "slow") == "fast":
    A.pvals = pvals

def selftest():
    rng = np.random.default_rng(7); worst = 0.0; k = 0
    atlas = [G for G in nx.graph_atlas_g()[1:] if 3 <= G.number_of_nodes() <= 7 and nx.is_connected(G)]
    for _ in range(3000):
        G = atlas[rng.integers(len(atlas))]; n = G.number_of_nodes(); E = [tuple(e) for e in G.edges()]
        N, F = rng.choice(n, 2, replace=False)
        w = np.exp(rng.uniform(-6, 0, len(E)))
        if rng.random() < 0.4: w[rng.random(len(E)) < 0.3] = 0.0
        r1 = _slow(n, E, w, int(N), int(F)); r2 = pvals(n, E, w, int(N), int(F))
        if (r1 is None) != (r2 is None): print("None mismatch", E, w, N, F); return
        if r1 is None: continue
        k += 1
        worst = max(worst, np.abs(r1[0] - r2[0]).max(), np.abs(r1[1] - r2[1]).max(), np.abs(r1[2] - r2[2]).max())
    t = time.time()
    for _ in range(2000): pvals(n, E, w, int(N), int(F))
    tf = (time.time() - t) / 2000; t = time.time()
    for _ in range(200): _slow(n, E, w, int(N), int(F))
    ts = (time.time() - t) / 200
    print("compared", k, "worst abs diff", worst, "fast", round(tf * 1e6), "us slow", round(ts * 1e6), "us")

def enum_cases(NMIN, NMAX):
    out = []
    for gi, G in enumerate(nx.graph_atlas_g()[1:], start=1):
        n = G.number_of_nodes()
        if n < NMIN or n > NMAX or not nx.is_connected(G): continue
        auts = list(nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter()); seen = set()
        for N, F in itertools.permutations(G.nodes(), 2):
            key = min((a[N], a[F]) for a in auts)
            if key in seen: continue
            seen.add(key)
            out.append((gi, n, [tuple(e) for e in G.edges()], N, F))
    return out

def work(job):
    cid, gi, n, E, N, F, starts = job
    t = time.time()
    try:
        sols, notes = A.solve_class((n, E, N, F, starts, 1000 + cid))
    except Exception as ex:
        return dict(cid=cid, gi=gi, n=n, E=E, N=N, F=F, error=repr(ex))
    for s in sols: s.pop("gw", None)
    return dict(cid=cid, gi=gi, n=n, E=E, N=N, F=F, sols=sols, notes=notes, sec=round(time.time() - t, 2))

def summary(OUT):
    from collections import Counter
    rows = [json.loads(l) for l in open(OUT)]
    att = lambda r: [s for s in r.get("sols", []) if s["kind"] in ("stable", "attract_marginal")]
    kinds = Counter(s["kind"] for r in rows for s in r.get("sols", []))
    bad = [r for r in rows if "error" in r or len(att(r)) != 1]
    print("cases", len(rows), "by n", dict(sorted(Counter(r["n"] for r in rows).items())), "cases with != 1 attractor", len(bad))
    print("kinds", dict(kinds), "with notes", sum(1 for r in rows if r.get("notes")), "errors", sum(1 for r in rows if "error" in r))
    A_ = [s for r in rows for s in att(r)]
    if A_:
        print("attractors: max Re(Dp-I)", max(s["maxre"] for s in A_), "max transverse", max([max(s["trans"]) for s in A_ if s["trans"]] or [0]),
              "with zero edges", sum(1 for s in A_ if s["trans"]), "marginal", sum(1 for s in A_ if s["kind"] == "attract_marginal"))
    for r in bad[:10]: print("BAD", r["cid"], r["gi"], r["n"], r["E"], r["N"], r["F"], r.get("error"), [(s["kind"], [round(x, 5) for x in s["w"]]) for s in r.get("sols", [])])
    print("total sec", round(sum(r.get("sec", 0) for r in rows)))

def main():
    if sys.argv[1] == "test": return selftest()
    if sys.argv[1] == "summary": return summary(sys.argv[2])
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        try: os.nice(10)
        except Exception: pass
    NMIN, NMAX, STARTS, WORKERS, OUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    SH, NSH = (int(sys.argv[6]), int(sys.argv[7])) if len(sys.argv) > 7 else (0, 1)
    cases = enum_cases(NMIN, NMAX)
    done = set()
    if os.path.exists(OUT):
        for l in open(OUT):
            try: done.add(json.loads(l)["cid"])
            except Exception: pass
    jobs = [(cid, gi, n, E, N, F, STARTS) for cid, (gi, n, E, N, F) in enumerate(cases) if cid % NSH == SH and cid not in done]
    print(time.strftime("%H:%M:%S"), "cases", len(cases), "this shard todo", len(jobs), "done before", len(done), flush=True)
    k = 0; stop = os.path.join(os.path.dirname(os.path.abspath(OUT)), "STOP")
    open(OUT + ".pid", "w").write(str(os.getpid()))
    with Pool(WORKERS) as pool, open(OUT, "a") as f:
        for r in pool.imap_unordered(work, jobs, chunksize=2):
            f.write(json.dumps(r) + "\n"); f.flush(); k += 1
            if k % 200 == 0: print(time.strftime("%H:%M:%S"), k, "of", len(jobs), flush=True)
            if os.path.exists(stop):
                print("STOP file seen", flush=True); pool.terminate(); return
    print(time.strftime("%H:%M:%S"), "DONE", flush=True)
    summary(OUT)

if __name__ == "__main__":
    main()
