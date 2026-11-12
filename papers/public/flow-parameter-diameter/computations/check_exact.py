"""Exact checks: Table 1 at s = 49, the certificate V_3 on PG(2,s) cones, the Dijkstra certificate
evaluator, the spectrum of Lemma 3.1, and the hub routing of Lemma 3.2."""
from fractions import Fraction as Fr
import numpy as np, networkx as nx
from flowlib import *
def nx_adj(G):
    G = nx.convert_node_labels_to_integers(G); return [sorted(G.neighbors(u)) for u in range(G.number_of_nodes())]
def Lw(s): return Fr((s+2)*(5*s**3+19*s**2+13*s+8), (s+3)*(s+4)*(s*s+s+1))
# 1. The closed form at s = 49 (Table 1)
s=49; t=7
tau = Fr(t*t+2, t*t+2-t); print("tau_rel(49) =", tau, "== 51/44:", tau==Fr(51,44))
print("L(49) =", Lw(49), "== 10786653/2251652:", Lw(49)==Fr(10786653,2251652), " gap =", Lw(49)-4*tau, "== 3818931/24768172:", Lw(49)-4*tau==Fr(3818931,24768172))
print("ratio F/(tau D) >=", float(Lw(49)/(2*tau)), " limit of L(s)/(2 tau) as t->inf: 5/2")
# 2. The certificate V_3 of Lemma 3.3 on PG(2,s) cones equals the closed form L(s) of Proposition 5.1
#    (ordered pairs at distance 1, 2, 3: n(s+1), n s(s+1), n s^2)
for s in [2,3,4,5,7,8,9,11,13,49]:
    N=s*s+s+1; n=2*N; d=s+1
    cnt={1:n*(s+1), 2:n*s*(s+1), 3:n*s*s}
    v3 = two_length_dual_cone(cnt,n,d,3)
    best,r = best_two_length_dual_cone(cnt,n,d)
    print(f"s={s}: two-length r=3 value {v3} == L(s): {v3==Lw(s)};  best r={r} value={float(best):.6f}")
# 3. generic exact Dijkstra dual evaluator agrees with the closed form on a small cone
H = nx.random_regular_graph(3, 30, seed=3); adjH=nx_adj(H); adj=cone(adjH); n=30; d=3
cnt=distance_distribution(adjH)
for r in [2,3,4,5]:
    b=Fr(2*(d+2), r+d); L=Fr((d+2)*r, r+d)
    lengths={e:(L if n in e else b) for e in edges_of(adj)}
    assert sum(lengths.values()) == n*(d+2)
    v_generic = dual_value_exact(adj, lengths); v_closed = two_length_dual_cone(cnt,n,d,r)
    print(f"r={r}: generic Dijkstra dual = {float(v_generic):.9f}  closed form = {float(v_closed):.9f}  equal: {v_generic==v_closed}  >= ball bound {float(ball_bound_lower(n,d,r)):.6f}: {v_closed>=ball_bound_lower(n,d,r)}")
# 4. spectrum of cone vs formula, incl. bipartite base
for name,H in [("rr(4,50)", nx.random_regular_graph(4,50,seed=2)), ("PG(2,3) incidence", None), ("Petersen", nx.petersen_graph())]:
    if H is None: adjH,_ = pg2_incidence_graph(3,1)
    else: adjH = nx_adj(H)
    d=len(adjH[0]); adj=cone(adjH); mu=adjacency_eigs(adjH); ev=srw_eigs(adj)
    pred=sorted(list(mu[1:]/(d+1))+[1.0,-1.0/(d+1)])[::-1]
    print(name, "max|eig P - pred| =", max(abs(a-b) for a,b in zip(ev,pred)), " lambda2 =", ev[1], " mu2/(d+1) =", mu[1]/(d+1))
# 5. hub routing exact check by building the flow and evaluating psi directly
adjH=nx_adj(nx.random_regular_graph(3,12,seed=5)); adj=cone(adjH); n=12; d=3; N=n+1; h=n
deg=[len(a) for a in adj]; twom=sum(deg); pi=[Fr(x,twom) for x in deg]
load={}
for a in range(N):
    f={}
    if a==h:
        for w in range(n): f[(h,w)]=pi[w]
    else:
        f[(a,h)]=1-pi[a]
        for w in range(n):
            if w!=a: f[(h,w)]=pi[w]
    for (i,j),val in f.items():
        e=(min(i,j),max(i,j)); load[e]=load.get(e,0)+pi[a]*abs(val)
psi=max(load.values())*twom
print("hub routing psi =", psi, " formula 2(d+1)(1-pi_v) =", hub_routing_upper_bound(n,d), psi==hub_routing_upper_bound(n,d))
