import time
from fractions import Fraction
import networkx as nx
from af449lib import *
def nx_adj(G):
    G = nx.convert_node_labels_to_integers(G); return [sorted(G.neighbors(u)) for u in range(G.number_of_nodes())]
for n in [30, 60, 120]:
    adjH = nx_adj(nx.cycle_graph(n)); adj = cone(adjH); d = 2
    cnt = distance_distribution(adjH)
    # two-length certificate for d=2 (B_r = 2(r-1)); use the exact V_r routine
    best, r = best_two_length_dual_cone(cnt, n, d)
    t0 = time.time(); F = flow_parameter_lp(adj); dt = time.time() - t0
    print(f"wheel n={n}: F_LP={F:.5f}  two-length cert={float(best):.5f} (r={r})  hub UB={float(hub_routing_upper_bound(n,d)):.5f}  limit 2(d+1)=6   [{dt:.1f}s]", flush=True)
