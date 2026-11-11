# Census of small graphs. For every connected graph and every (N,F) up to automorphism:
#  1. drop what the walk can never cross (vertices outside the component of N in G-F, and their edges);
#  2. from several interior starts run the mean-field flow w' = p(w) - w (Woodbury kernel, used for the flow only);
#  3. read the dying coordinates off the decay between time T and 2T (a coordinate going to a positive limit has
#     ratio -> 1, a marginal zero ~ 1/t has ratio -> 1/2, a hyperbolic zero has ratio -> 0), set them to 0 exactly and
#     polish the rest by Newton with the exact per-edge kernel;
#  4. at the limit: eigenvalues of Dp - I on the support, single-edge transverse rate of every zero edge.
# One limit shared by all starts = one attractor seen. Output: one json line per case.
# Usage: python ants_exact.py NMIN NMAX STARTS WORKERS OUT.jsonl [SHARD NSHARDS]   (resumable; STOP file; OUT.pid)
import sys, json, os, time, numpy as np, networkx as nx
from multiprocessing import Pool
import ants_core as A
from ants_fast import pvals as fast_pvals, enum_cases

def flow(n, E, w, N, F, steps):
    for _ in range(steps):
        r = fast_pvals(n, E, w, N, F)
        if r is None: return None
        w = np.maximum(w + 0.5 * (r[0] - w), 0.0)
        w[w < 1e-200] = 0.0
    return w

def reduce_graph(n, E, N, F):
    G = nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(E)
    H = G.copy(); H.remove_node(F); comp = nx.node_connected_component(H, N)
    keep = [k for k, (u, v) in enumerate(E) if (u in comp or u == F) and (v in comp or v == F)]
    return G, keep

def solve_case(n, E, N, F, starts, seed, T=2000):
    G, keep = reduce_graph(n, E, N, F)
    Er = [E[k] for k in keep]; m = len(Er)
    rng = np.random.default_rng(seed); found = []; flags = []
    for s in range(starts):
        r = s % 3
        if r == 0: w0 = rng.uniform(0.05, 1, m)
        elif r == 1: w0 = np.exp(rng.uniform(-6, 0, m))
        else:
            w0 = np.exp(rng.uniform(-6, -3, m)); Hh = nx.Graph(Er)
            for (u, v) in Hh.edges(): Hh[u][v]["x"] = rng.uniform(0.5, 1.5)
            path = nx.shortest_path(Hh, N, F, weight="x"); on = set(frozenset(e) for e in zip(path, path[1:]))
            for k, e in enumerate(Er):
                if frozenset(e) in on: w0[k] = rng.uniform(0.5, 1)
        w1 = flow(n, Er, w0, N, F, T)
        w2 = flow(n, Er, w1, N, F, T) if w1 is not None else None
        if w2 is None: flags.append("flow_none"); continue
        Z = [k for k in range(m) if w2[k] == 0 or (w2[k] < 0.1 and w2[k] < 0.8 * w1[k])]
        S = [k for k in range(m) if k not in Z]
        x = w2.copy(); x[Z] = 0
        z = A.newton(n, Er, x, S, N, F) if S else None
        if z is None or (z[S] <= 1e-9).any() or np.abs(z - x)[S].max() > 0.05:
            flags.append("polish_fail"); found.append(dict(w=w2, Z=Z, raw=True, starts=1)); continue
        for f in found:
            if not f.get("raw") and np.abs(f["w"] - z).max() < 1e-7: f["starts"] += 1; break
        else:
            found.append(dict(w=z, Z=Z, starts=1))
    sols = []
    for f in found:
        w = f["w"]; full = np.zeros(len(E)); full[keep] = w
        d = dict(w=full.tolist(), zero=[keep[k] for k in f["Z"]], starts=f["starts"], raw=bool(f.get("raw")))
        if not f.get("raw"):
            maxre, trans, Gv, deg = A.analyse(n, Er, w, N, F)
            d["maxre"] = maxre; d["trans"] = trans
        sols.append(d)
    return dict(unreach=[k for k in range(len(E)) if k not in keep], sols=sols, flags=flags)

def work(job):
    cid, gi, n, E, N, F, starts = job
    t = time.time()
    try:
        r = solve_case(n, E, N, F, starts, 1000 + cid)
    except Exception as ex:
        return dict(cid=cid, gi=gi, n=n, E=E, N=N, F=F, error=repr(ex))
    r.update(cid=cid, gi=gi, n=n, E=E, N=N, F=F, sec=round(time.time() - t, 2))
    return r

def main():
    try: os.nice(10)
    except Exception: pass
    NMIN, NMAX, STARTS, WORKERS, OUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    SH, NSH = (int(sys.argv[6]), int(sys.argv[7])) if len(sys.argv) > 7 else (0, 1)
    cases = enum_cases(NMIN, NMAX); done = set()
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

if __name__ == "__main__":
    main()
