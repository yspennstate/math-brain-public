# Cones over random d-regular graphs: LP value of F, two-length dual, hub bound, tau_2, ratios.
import sys, time, csv
from fractions import Fraction
import numpy as np
import networkx as nx
from af449lib import *

def nx_adj(G):
    G = nx.convert_node_labels_to_integers(G)
    return [sorted(G.neighbors(u)) for u in range(G.number_of_nodes())]

cases = [(3,20),(3,40),(3,80),(3,160),(3,320),(4,20),(4,40),(4,80),(4,160),(5,20),(5,40),(5,80),(5,160),(6,40),(6,80),(6,160),(3,640),(4,320)]
out = open("rr_lp_results.csv","a")
w = csv.writer(out)
for d,n in cases:
    seed = 1
    while True:
        H = nx.random_regular_graph(d, n, seed=seed)
        if nx.is_connected(H): break
        seed += 1
    adjH = nx_adj(H); adj = cone(adjH)
    muH = adjacency_eigs(adjH); mu2 = muH[1]
    t2 = (d+1)/(d+1-mu2)
    cnt = distance_distribution(adjH)
    best, rbest = best_two_length_dual_cone(cnt, n, d)
    ub = hub_routing_upper_bound(n, d)
    t0=time.time(); F = flow_parameter_lp(adj); dt=time.time()-t0
    diam = max(cnt)
    meand = sum(t*c for t,c in cnt.items())/sum(cnt.values())
    row = [d,n,seed,f"{mu2:.6f}",f"{t2:.6f}",diam,f"{meand:.3f}",f"{float(best):.6f}",rbest,f"{F:.6f}",f"{float(ub):.6f}",f"{F/(2*t2):.5f}",f"{d+1-mu2:.5f}",f"{dt:.1f}"]
    print("d n seed mu2 tau2 diamH meandistH twolen_dual r F_LP hubUB F/(tau2*Delta) d+1-mu2 secs", flush=True)
    print(*row, flush=True)
    w.writerow(row); out.flush()
