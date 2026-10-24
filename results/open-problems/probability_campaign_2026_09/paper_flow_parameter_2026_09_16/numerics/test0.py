import time
from fractions import Fraction
import networkx as nx
from af449lib import *
def nx_adj(G):
    G = nx.convert_node_labels_to_integers(G)
    return [sorted(G.neighbors(u)) for u in range(G.number_of_nodes())]
for n in [3,4,5,6]:
    t0=time.time(); F = flow_parameter_lp(nx_adj(nx.complete_graph(n))); print("K",n, F, 2*(n-1)/n, f"{time.time()-t0:.2f}s", flush=True)
for name, H, (q,r) in [("C5", nx.cycle_graph(5), (5,2)), ("Petersen", nx.petersen_graph(), (10,3)), ("Paley13", nx.paley_graph(13).to_undirected(), (13,6))]:
    adj = cone(nx_adj(H)); t0=time.time(); F = flow_parameter_lp(adj)
    print(name, "LP F =", F, " formula =", Fraction(2*(r+1)*(2*q-r-1), q*(r+2)), float(Fraction(2*(r+1)*(2*q-r-1), q*(r+2))), f"{time.time()-t0:.2f}s", flush=True)
for (p,k) in [(2,1),(3,1)]:
    adjH, Npts = pg2_incidence_graph(p,k); s=p**k; adj = cone(adjH)
    t0=time.time(); F = flow_parameter_lp(adj); print("PG q=",s, "|V|=",len(adj), "F=",F, f"{time.time()-t0:.2f}s", flush=True)
