# Trace-reinforced ants: equilibria of the mean-field flow w' = p(w) - w, where p_e(w) = P_w(walk from N crosses e before hitting F).
# 1. prune each (G,N,F) to H = edges on some simple N-F path (blocks on the N-F path of the block-cut tree);
#    dead-end edges have p_e = 0 whenever their weight is 0, and their linear rate at 0 is c = G(u)/W_u.
# 2. dedupe (H,N,F) up to isomorphism; for each class find fixed points of p(w)=w on H by
#    (a) damped flow + Newton on the detected support, (b) pure Newton from random interior starts (sees saddles).
# 3. at each fixed point: eigenvalues of Dp - I on the support, and the transverse rate c_e for every zero edge
#    (edge of H off the support, or dead-end edge of the original graph): c_e < 1 attracting, = 1 marginal, > 1 unstable.
# Usage: python ants_core.py NMIN NMAX STARTS WORKERS OUT.jsonl
import sys, itertools, json, os, time, numpy as np, networkx as nx
from multiprocessing import Pool

def pvals(n, E, w, N, F):
    W = np.zeros((n, n))
    for k, (u, v) in enumerate(E):
        W[u, v] += w[k]; W[v, u] += w[k]
    # keep only the support component of N (other positive edges are never reached)
    Hs = nx.Graph(); Hs.add_nodes_from(range(n)); Hs.add_edges_from(E[k] for k in range(len(E)) if w[k] > 0)
    comp = nx.node_connected_component(Hs, N)
    if F not in comp:
        return None
    mask = np.zeros(n, bool); mask[list(comp)] = True
    W[~mask, :] = 0; W[:, ~mask] = 0
    deg = W.sum(1)
    P = np.divide(W, deg[:, None], out=np.zeros_like(W), where=deg[:, None] > 0)
    P[F] = 0
    Q = np.eye(n) - P
    Gv = np.linalg.solve(Q.T, np.eye(n)[N])          # expected visits before F
    m = len(E); A = np.broadcast_to(Q, (m, n, n)).copy(); b = np.zeros((m, n))
    for k, (u, v) in enumerate(E):
        A[k, u, v] = 0; A[k, v, u] = 0; b[k, u] = P[u, v]; b[k, v] = P[v, u]
    A[:, F, :] = 0; A[:, F, F] = 1; b[:, F] = 0
    p = np.linalg.solve(A, b[..., None])[:, N, 0]
    return p, Gv, deg

def rate(Gv, deg, u, v, F):
    c = 0.0
    for x in (u, v):
        if x != F and deg[x] > 0:
            c += Gv[x] / deg[x]
    return c

def newton(n, E, w, S, N, F, it=60):
    w = w.copy()
    for _ in range(it):
        r = pvals(n, E, w, N, F)
        if r is None: return None
        R = (r[0] - w)[S]
        if np.abs(R).max() < 1e-13: return w
        J = np.zeros((len(S), len(S)))
        for j, s in enumerate(S):
            h = 1e-7 * max(w[s], 1e-3); x = w.copy(); x[s] += h
            rx = pvals(n, E, x, N, F)
            if rx is None: return None
            J[:, j] = ((rx[0] - x) - (r[0] - w))[S] / h
        try:
            d = np.linalg.solve(J, -R)
        except np.linalg.LinAlgError:
            return None
        t = 1.0
        while t > 1e-4:
            x = w.copy(); x[S] = w[S] + t * d
            if (x[S] > 0).all():
                rx = pvals(n, E, x, N, F)
                if rx is not None and np.abs((rx[0] - x)[S]).max() < np.abs(R).max() * (1 - 1e-4 * t) + 1e-15:
                    break
            t /= 2
        else:
            return None
        w = x
    r = pvals(n, E, w, N, F)
    return w if r is not None and np.abs((r[0] - w)[S]).max() < 1e-11 else None

def analyse(n, E, w, N, F):
    S = [k for k in range(len(E)) if w[k] > 0]
    r = pvals(n, E, w, N, F); p0, Gv, deg = r
    J = np.zeros((len(S), len(S)))
    for j, s in enumerate(S):
        h = 1e-7 * max(w[s], 1e-3); x = w.copy(); x[s] += h
        J[:, j] = (pvals(n, E, x, N, F)[0] - p0)[S] / h
    maxre = float(np.linalg.eigvals(J - np.eye(len(S))).real.max())
    trans = [rate(Gv, deg, E[k][0], E[k][1], F) for k in range(len(E)) if w[k] == 0]
    return maxre, trans, Gv, deg

def clean(n, E, w, N, F):
    if w is None: return None
    for _ in range(4):
        S = [k for k in range(len(E)) if w[k] > 1e-8 * max(w.max(), 1e-300)]
        x = w.copy(); x[[k for k in range(len(E)) if k not in S]] = 0
        z = newton(n, E, x, S, N, F)
        if z is None: return None
        if (z[S] > 1e-8).all(): return z
        w = z
    return None

def flow_from(n, E, w, N, F, steps):
    for _ in range(steps):
        r = pvals(n, E, w, N, F)
        if r is None: return None
        w = np.maximum(w + 0.5 * (r[0] - w), 0.0)
    return w

def returns(n, E, w, N, F, rng, eps=1e-3, steps=20000):
    # perturbed flow test for a marginal point: push every edge up by about eps, flow, compare distances
    x = w + eps * rng.uniform(0.5, 1, len(w))
    d0 = np.abs(x - w).max()
    y = flow_from(n, E, x, N, F, steps)
    return y is not None and np.abs(y - w).max() < 0.5 * d0

def solve_class(args):
    n, E, N, F, starts, seed = args
    rng = np.random.default_rng(seed); m = len(E); sols = []; notes = []
    def add(w, how):
        if w is None: return
        for x in sols:
            if np.abs(x["w"] - w).max() < 1e-6:
                x["how"].add(how); return
        sols.append(dict(w=w, how={how}))
    for s in range(starts):
        w0 = rng.uniform(0.05, 1, m) if s % 2 == 0 else np.exp(rng.uniform(-6, 0, m))
        w = flow_from(n, E, w0.copy(), N, F, 3000)
        z = clean(n, E, w, N, F)
        if z is None: notes.append("flow_clean_fail")
        add(z, "flow")
        add(clean(n, E, newton(n, E, w0, list(range(m)), N, F, it=80), N, F), "newton")
    out = []
    for sd in sols:
        w = sd["w"]; maxre, trans, Gv, deg = analyse(n, E, w, N, F)
        mt = max(trans) if trans else 0.0
        if maxre > 1e-7 or mt > 1 + 1e-7: kind = "unstable"
        elif maxre < -1e-7 and mt < 1 - 1e-7: kind = "stable"
        else: kind = "attract_marginal" if returns(n, E, w, N, F, rng) else "marginal_not_returning"
        out.append(dict(w=w.tolist(), maxre=maxre, trans=trans, kind=kind, how=sorted(sd["how"]),
                        gw=[(float(Gv[x] / deg[x]) if deg[x] > 0 and x != F else 0.0) for x in range(n)]))
    return out, notes

def core_blocks(G, N, F):
    cuts = set(nx.articulation_points(G)); T = nx.Graph()
    blocks = [list(b) for b in nx.biconnected_component_edges(G)]
    for i, b in enumerate(blocks):
        vs = {x for e in b for x in e}
        for x in vs:
            if x in cuts or x in (N, F): T.add_edge(("B", i), ("C", x))
    path = nx.shortest_path(T, ("C", N), ("C", F))
    keep = [e for node in path if node[0] == "B" for e in blocks[node[1]]]
    return keep

def core(G, N, F):
    # no pruning: a dead end can hold positive limit weight (pendant at N on N-x-F: weight 1/2)
    return list(G.edges())

def main():
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    NMIN, NMAX, STARTS, WORKERS, OUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    cases = []; reps = {}; classes = []
    for gi, G in enumerate(nx.graph_atlas_g()[1:]):
        n = G.number_of_nodes()
        if n < NMIN or n > NMAX or not nx.is_connected(G): continue
        auts = list(nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter()); seen = set()
        for N, F in itertools.permutations(G.nodes(), 2):
            key = min((a[N], a[F]) for a in auts)
            if key in seen: continue
            seen.add(key)
            keep = core(G, N, F); H = nx.Graph(keep)
            for x in H: H.nodes[x]["t"] = "N" if x == N else ("F" if x == F else "")
            h = nx.weisfeiler_lehman_graph_hash(H, node_attr="t")
            cid = None
            for c in reps.get(h, []):
                gm = nx.algorithms.isomorphism.GraphMatcher(classes[c][0], H, node_match=lambda a, b: a["t"] == b["t"])
                if gm.is_isomorphic():
                    cid = c; mp = gm.mapping; break   # rep node -> H node
            if cid is None:
                cid = len(classes); classes.append((H, N, F)); reps.setdefault(h, []).append(cid)
                mp = {x: x for x in H}
            dead = [(u, v) for u, v in G.edges() if not H.has_edge(u, v)]
            att = [x for e in dead for x in e if x in H]       # attachment vertices (one endpoint per dead edge at most)
            inv = {b: a for a, b in mp.items()}
            cases.append(dict(gi=gi, n=n, N=N, F=F, cls=cid, m=G.number_of_edges(), mH=H.number_of_edges(),
                              att=[inv[x] for x in att]))
    print(time.strftime("%H:%M:%S"), "cases", len(cases), "classes", len(classes), flush=True)
    jobs = []
    for c, (H, N, F) in enumerate(classes):
        V = sorted(H.nodes()); idx = {v: i for i, v in enumerate(V)}
        E = [(idx[u], idx[v]) for u, v in H.edges()]
        jobs.append((len(V), E, idx[N], idx[F], STARTS, 1000 + c))
    with Pool(WORKERS) as pool:
        res = pool.map(solve_class, jobs, chunksize=4)
    print(time.strftime("%H:%M:%S"), "solved", flush=True)
    with open(OUT, "w") as f:
        for c, (H, N, F) in enumerate(classes):
            V = sorted(H.nodes())
            f.write(json.dumps(dict(kind="class", cls=c, nodes=V, edges=[list(e) for e in H.edges()], N=N, F=F,
                                    sols=res[c][0], notes=res[c][1])) + "\n")
        # per original case: dead-end transverse rates at each fixed point of its class
        worst_dead = 0.0; ncases_multi = 0; nunstable = 0; nmarg = 0
        for cs in cases:
            H, N, F = classes[cs["cls"]]; V = sorted(H.nodes()); idx = {v: i for i, v in enumerate(V)}
            sols = res[cs["cls"]][0]
            if len([x for x in sols if x["kind"] in ("stable", "attract_marginal")]) != 1: ncases_multi += 1
            for s in sols:
                if s["kind"] not in ("stable", "attract_marginal"): continue
                dr = [s["gw"][idx[x]] for x in cs["att"]]
                cs.setdefault("dead_rates", []).append(dr)
                if dr: worst_dead = max(worst_dead, max(dr))
            f.write(json.dumps(dict(kind="case", **cs)) + "\n")
    # summary
    att = lambda r: [s for s in r[0] if s["kind"] in ("stable", "attract_marginal")]
    ncls_multi = sum(1 for r in res if len(att(r)) != 1)
    nfail = sum(1 for r in res if r[1])
    allsols = [s for r in res for s in r[0]]
    from collections import Counter
    A = [s for s in allsols if s["kind"] in ("stable", "attract_marginal")]
    print("classes", len(classes), "with !=1 attractor", ncls_multi, "classes with flow notes", nfail)
    print("fixed points", len(allsols), dict(Counter(s["kind"] for s in allsols)))
    print("attractors: max Re", max(s["maxre"] for s in A),
          "largest transverse rates at attractors", sorted(Counter(round(t, 6) for s in A for t in s["trans"]).items())[-4:])
    print("cases", len(cases), "cases with !=1 attractor", ncases_multi, "max dead-end rate at an attractor", worst_dead)
    print("support sizes: interior", sum(1 for s in allsols if not s["trans"]), "boundary", sum(1 for s in allsols if s["trans"]))

if __name__ == "__main__":
    main()
