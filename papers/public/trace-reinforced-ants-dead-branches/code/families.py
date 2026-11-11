# Structured families beyond the census of small graphs. For each (graph, N, F): many starts (uniform, log-uniform,
# and one-branch-heavy), damped flow + Newton on the detected support, then the stability data of each limit.
# A second limit here would contradict the first sentence of Conjecture 1.1 of Kious, Mailler and Schapira.
# Usage: python families.py STARTS OUT.jsonl [filter]
import sys, json, time, numpy as np, networkx as nx
from ants_core import pvals, newton, analyse, clean, flow_from

def theta(k, L):
    # k internally disjoint N-F paths, each with L edges; N=0, F=1
    G = nx.Graph(); G.add_nodes_from([0, 1]); nxt = 2
    for _ in range(k):
        prev = 0
        for j in range(L - 1):
            G.add_edge(prev, nxt); prev = nxt; nxt += 1
        G.add_edge(prev, 1)
    return G, 0, 1

def theta_mixed(Ls):
    G = nx.Graph(); G.add_nodes_from([0, 1]); nxt = 2
    for L in Ls:
        prev = 0
        for j in range(L - 1):
            G.add_edge(prev, nxt); prev = nxt; nxt += 1
        G.add_edge(prev, 1)
    return G, 0, 1

def cases():
    out = []
    for k in (2, 3, 4, 5, 6, 8):
        for L in (2, 3, 4, 5, 6, 8):
            if k * (L - 1) + 2 <= 34:
                out.append((f"theta_k{k}_L{L}",) + theta(k, L))
    for Ls in ((2, 3), (2, 4), (3, 4), (2, 2, 3), (2, 3, 4), (3, 3, 5), (2, 2, 2, 5), (1, 2), (1, 3), (1, 2, 3), (1, 4, 4)):
        out.append(("thetamix_" + "_".join(map(str, Ls)),) + theta_mixed(Ls))
    for a, b in ((2, 3), (3, 3), (3, 4), (4, 4), (3, 6), (5, 5)):
        G = nx.complete_bipartite_graph(a, b)
        out.append((f"K{a}_{b}_opp", G, 0, a))
        if a >= 2: out.append((f"K{a}_{b}_sameA", G, 0, 1))
        out.append((f"K{a}_{b}_sameB", G, a, a + 1))
    for n in (4, 5, 6, 7, 8, 9):
        out.append((f"K{n}", nx.complete_graph(n), 0, 1))
    for n in (5, 6, 8, 9, 12, 15):
        C = nx.cycle_graph(n)
        for F in sorted(set((1, n // 3, n // 2))):
            if F: out.append((f"C{n}_F{F}", C, 0, F))
    for a, b in ((2, 3), (2, 4), (2, 6), (3, 3), (3, 4), (4, 4), (3, 5)):
        G = nx.convert_node_labels_to_integers(nx.grid_2d_graph(a, b))
        out.append((f"grid{a}x{b}_corners", G, 0, a * b - 1))
        out.append((f"grid{a}x{b}_adj", G, 0, 1))
        out.append((f"grid{a}x{b}_mid", G, 0, (a * b) // 2))
    for d in (3, 4):
        G = nx.convert_node_labels_to_integers(nx.hypercube_graph(d))
        out.append((f"Q{d}_antipodal", G, 0, 2 ** d - 1)); out.append((f"Q{d}_adj", G, 0, 1))
    P = nx.petersen_graph(); out.append(("petersen_adj", P, 0, 1)); out.append(("petersen_far", P, 0, 7))
    for n in (6, 8, 10):
        W = nx.wheel_graph(n); out.append((f"wheel{n}_hub_rim", W, 0, 1)); out.append((f"wheel{n}_rim_rim", W, 1, 1 + (n - 1) // 2))
    for n in (4, 6, 8):
        L = nx.ladder_graph(n); out.append((f"ladder{n}_ends", L, 0, 2 * n - 1)); out.append((f"ladder{n}_rung", L, 0, n))
    return out

def run(name, G, N, F, starts, seed=1):
    n = G.number_of_nodes(); E = [tuple(e) for e in G.edges()]; m = len(E)
    rng = np.random.default_rng(seed)
    sols = []; fails = 0
    for s in range(starts):
        r = s % 3
        if r == 0: w0 = rng.uniform(0.02, 1, m)
        elif r == 1: w0 = np.exp(rng.uniform(-7, 0, m))
        else:
            # heavy on the edges of one random shortest-ish N-F path, light elsewhere
            w0 = np.exp(rng.uniform(-6, -3, m))
            H = G.copy()
            for (u, v) in H.edges(): H[u][v]["x"] = rng.uniform(0.5, 1.5)
            path = nx.shortest_path(H, N, F, weight="x")
            on = set(frozenset(e) for e in zip(path, path[1:]))
            for k, e in enumerate(E):
                if frozenset(e) in on: w0[k] = rng.uniform(0.5, 1)
        w = flow_from(n, E, w0, N, F, 4000)
        z = clean(n, E, w, N, F)
        if z is None:
            w = flow_from(n, E, w, N, F, 40000) if w is not None else None
            z = clean(n, E, w, N, F)
        if z is None:
            fails += 1; continue
        if not any(np.abs(z - x).max() < 1e-7 for x in sols): sols.append(z)
    rec = dict(name=name, n=n, m=m, N=N, F=F, starts=starts, fails=fails, nsol=len(sols), sols=[])
    for z in sols:
        maxre, trans, Gv, deg = analyse(n, E, z, N, F)
        rec["sols"].append(dict(w=[float(x) for x in z], maxre=maxre, trans=[float(t) for t in trans],
                                nzero=int((z == 0).sum()), distinct=sorted(set(round(float(x), 6) for x in z))))
    return rec

if __name__ == "__main__":
    starts = int(sys.argv[1]); out = sys.argv[2]; flt = sys.argv[3] if len(sys.argv) > 3 else ""
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception: pass
    with open(out, "a") as f:
        for name, G, N, F in cases():
            if flt and flt not in name: continue
            t = time.time(); rec = run(name, G, N, F, starts); rec["sec"] = round(time.time() - t, 1)
            f.write(json.dumps(rec) + "\n"); f.flush()
            s0 = rec["sols"][0] if rec["sols"] else None
            print(time.strftime("%H:%M:%S"), name, "n", rec["n"], "m", rec["m"], "limits", rec["nsol"], "fails", rec["fails"],
                  "maxRe", [round(s["maxre"], 4) for s in rec["sols"]],
                  "trans", [[round(t, 3) for t in s["trans"]] for s in rec["sols"]],
                  "w", s0["distinct"][:8] if s0 else None, rec["sec"], "s", flush=True)
