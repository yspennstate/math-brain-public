import time, sys
from fractions import Fraction
import numpy as np
import networkx as nx
from af449lib import *

def nx_adj(G):
    G = nx.convert_node_labels_to_integers(G)
    return [sorted(G.neighbors(u)) for u in range(G.number_of_nodes())]

print("== sanity: complete graphs, F = 2(n-1)/n")
for n in [3,4,5,6]:
    F = flow_parameter_lp(nx_adj(nx.complete_graph(n)))
    print(n, F, 2*(n-1)/n)

print("== worker's SRG cone formula F = 2(r+1)(2q-r-1)/(q(r+2)) and wheel W_6 = 21/10")
for name, H, (q,r) in [("C5", nx.cycle_graph(5), (5,2)), ("Petersen", nx.petersen_graph(), (10,3)),
                       ("Paley13", nx.paley_graph(13).to_undirected(), (13,6)), ("Clebsch", nx.LCF_graph(16,[5,-5],8) if False else None, (16,5))]:
    if H is None: continue
    adj = cone(nx_adj(H))
    F = flow_parameter_lp(adj)
    print(name, "LP F =", F, " formula =", Fraction(2*(r+1)*(2*q-r-1), q*(r+2)), float(Fraction(2*(r+1)*(2*q-r-1), q*(r+2))))

print("== spectrum check: cone over random 3-regular graph on 20 vertices")
H = nx.random_regular_graph(3, 20, seed=1)
adjH = nx_adj(H); adj = cone(adjH)
muH = adjacency_eigs(adjH)
t2, ev = tau2(adj)
pred = sorted(list(muH[1:]/4.0) + [1.0, -0.25])[::-1]
print("max |eig(P) - predicted| =", max(abs(a-b) for a,b in zip(ev, pred)))
print("tau2 =", t2, " (d+1)/(d+1-mu2) =", 4/(4-muH[1]))

print("== PG(2,q) cones: LP F vs worker two-length dual L(s) and tau2 = (s+2)/(s+2-sqrt s)")
for (p,k) in [(2,1),(3,1),(2,2),(5,1),(7,1)]:
    adjH, Npts = pg2_incidence_graph(p,k); s = p**k
    adj = cone(adjH)
    t0=time.time(); F = flow_parameter_lp(adj); dt=time.time()-t0
    Ls = Fraction((s+2)*(5*s**3+19*s**2+13*s+8), (s+3)*(s+4)*(s*s+s+1))
    t2, ev = tau2(adj)
    n = 2*Npts; d = s+1
    cnt = distance_distribution(adjH)
    best, rbest = best_two_length_dual_cone(cnt, n, d)
    print(f"q={s}: |V|={n+1} F_LP={F:.9f}  worker L(s)={float(Ls):.9f}  best two-length dual={float(best):.9f} (r={rbest})  hub UB={float(hub_routing_upper_bound(n,d)):.6f}  tau2={t2:.6f} pred={(s+2)/(s+2-s**0.5):.6f}  F/(2 tau2)={F/(2*t2):.5f}  [{dt:.1f}s]")
