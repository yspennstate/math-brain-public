import sys, time, csv
from fractions import Fraction
import numpy as np, networkx as nx
from af449lib import *
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
def nx_adj(G):
    G = nx.convert_node_labels_to_integers(G); return [sorted(G.neighbors(u)) for u in range(G.number_of_nodes())]
tag = sys.argv[1]; cases = [tuple(int(x) for x in c.split(',')) for c in sys.argv[2:]]
out = open(f"rr_lp_results_{tag}.csv","a"); w = csv.writer(out)
for d,n in cases:
    seed = 1
    while True:
        H = nx.random_regular_graph(d, n, seed=seed)
        if nx.is_connected(H): break
        seed += 1
    adjH = nx_adj(H); adj = cone(adjH)
    mu2 = adjacency_eigs(adjH)[1]; t2 = (d+1)/(d+1-mu2)
    cnt = distance_distribution(adjH); best, rbest = best_two_length_dual_cone(cnt, n, d); ub = hub_routing_upper_bound(n, d)
    t0=time.time(); F = flow_parameter_lp(adj); dt=time.time()-t0
    diam = max(cnt); meand = sum(t*c for t,c in cnt.items())/sum(cnt.values())
    row = [d,n,seed,f"{mu2:.6f}",f"{t2:.6f}",diam,f"{meand:.3f}",f"{float(best):.6f}",rbest,f"{F:.6f}",f"{float(ub):.6f}",f"{F/(2*t2):.5f}",f"{d+1-mu2:.5f}",f"{dt:.1f}"]
    print(*row, flush=True); w.writerow(row); out.flush()
