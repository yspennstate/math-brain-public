# Census table of Section 4. Usage: python3 table.py ../data/ex5.jsonl ../data/ex6.jsonl [../data/ex7.jsonl]
# Each input line is one case (G, N, F) written by ants_exact.py. A case is reduced if the walk can cross every edge.
# For each case the zero set of the limit of the flow is compared with the set D(G, N, F) of Conjecture 9.
import sys, json, networkx as nx
from collections import Counter
from dead_set import dead_set, branch_edges, has_shadowed_neighbour

tab = Counter(); maxre = {}; minpos = {}; seen = set()
for fn in sys.argv[1:]:
    for l in open(fn):
        r = json.loads(l)
        if (r["n"], r["cid"], fn) in seen: continue
        seen.add((r["n"], r["cid"], fn))
        n = r["n"]; E = [tuple(e) for e in r["E"]]; N, F = r["N"], r["F"]
        G = nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(E)
        d = "N~F" if G.has_edge(N, F) else "d>=2"
        red = not r.get("unreach")
        keys = [("all", d), (n, d)]
        for key in keys:
            tab[key + ("cases",)] += 1
            if red: tab[key + ("reduced",)] += 1
        if "sols" not in r: tab[("all", d, "ERROR")] += 1; continue
        good = [s for s in r["sols"] if not s["raw"]]
        if not (len(r["sols"]) == 1 and len(good) == 1):
            tab[("all", d, "NOT ONE LIMIT")] += 1; continue
        s = good[0]; U = set(frozenset(E[k]) for k in r["unreach"]); obs = set(frozenset(E[k]) for k in s["zero"])
        pred = dead_set(G, N, F) - U; thm2 = branch_edges(G, N, F) - U
        kappa = nx.node_connectivity(G)
        for key in keys:
            tab[key + ("one limit",)] += 1
            if obs == pred: tab[key + ("zero set = D",)] += 1
            if not red: continue
            if obs: tab[key + ("reduced, a zero edge",)] += 1
            if obs and kappa >= 2: tab[key + ("reduced, a zero edge, 2-connected",)] += 1
            if obs and kappa >= 3: tab[key + ("reduced, a zero edge, 3-connected",)] += 1
            if thm2: tab[key + ("reduced, Theorem 2 applies",)] += 1
            if thm2 and kappa >= 2: tab[key + ("reduced, Theorem 2 applies, 2-connected",)] += 1
            if thm2 and not thm2 <= obs: tab[key + ("THEOREM 2 EDGE ALIVE",)] += 1
            if has_shadowed_neighbour(G, N, F):
                tab[key + ("reduced, Theorem 5 applies",)] += 1
                if not obs: tab[key + ("THEOREM 5 BUT ALL POSITIVE",)] += 1
                if kappa >= 2: tab[key + ("reduced, Theorem 5 applies, 2-connected",)] += 1
                if kappa >= 3: tab[key + ("reduced, Theorem 5 applies, 3-connected",)] += 1
        maxre[d] = max(maxre.get(d, -9), s["maxre"])
        minpos[d] = min([minpos.get(d, 9)] + [x for k, x in enumerate(s["w"]) if k not in s["zero"] and k not in r["unreach"]])
for k in sorted(tab, key=str): print(k, tab[k])
print("largest real part of an eigenvalue of Dp - I on the support:", maxre)
print("smallest positive limit weight:", minpos)
