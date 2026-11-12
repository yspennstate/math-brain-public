"""Table 2: cones over random d-regular graphs (networkx.random_regular_graph, NetworkX 3.6.1; the first connected
graph from seed 1 upward, which is seed 1 for every size used):
the linear program for F, the best certificate of Lemma 3.3, the hub bound, tau_2 and the ratio."""
import time, csv
from fractions import Fraction
import numpy as np
import networkx as nx
from flowlib import *

def nx_adj(G):
    G = nx.convert_node_labels_to_integers(G)
    return [sorted(G.neighbors(u)) for u in range(G.number_of_nodes())]

cases = [(3,20),(3,40),(3,80),(3,160),(4,20),(4,40),(4,80),(5,20),(5,40),(5,80),(6,20),(6,40),(8,40)]
out = open("rr_lp_results.csv", "w", newline="")
w = csv.writer(out)
w.writerow("d,n,seed,mu2,tau2,diam_H,mean_dist_H,best_certificate,r,F_LP,hub_bound,F_over_tau2_Delta,d_plus_1_minus_mu2,seconds".split(","))
print("d n seed mu2 tau2 diam_H mean_dist_H best_certificate r F_LP hub_bound F_over_tau2_Delta d_plus_1_minus_mu2 seconds", flush=True)
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
    print(*row, flush=True)
    w.writerow(row); out.flush()
