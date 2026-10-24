import sympy as sp
import networkx as nx

print("R04 I0027 diameter-profile upper-bound exact checker")
print("SELF-CHECK: verifies finite reductions and symbolic optimization; Mukwembi 2012 diameter-sensitive Gutman theorem is external input.")

def exact_data(G):
    G=nx.convert_node_labels_to_integers(G,ordering="sorted")
    n=G.number_of_nodes()
    m=G.number_of_edges()
    deg=[G.degree(i) for i in range(n)]
    d=nx.diameter(G)
    L=sp.zeros(n,n)
    for i in range(n):
        L[i,i]=deg[i]
    for i,j in G.edges():
        L[i,j]-=1
        L[j,i]-=1
    R=L[:n-1,:n-1].inv()
    dist=dict(nx.all_pairs_shortest_path_length(G))
    rstar=sp.Rational(0)
    gut=sp.Rational(0)
    for i in range(n):
        for j in range(i+1,n):
            if j==n-1:
                rij=R[i,i]
            elif i==n-1:
                rij=R[j,j]
            else:
                rij=R[i,i]+R[j,j]-2*R[i,j]
            rstar += deg[i]*deg[j]*rij
            gut += deg[i]*deg[j]*dist[i][j]
    K=sp.cancel(rstar/(2*m))
    return n,m,d,K,gut

atlas=nx.graph_atlas_g()
count=0
max_ratio=sp.Rational(0)
max_ratio_data=None
for G in atlas:
    if 2<=G.number_of_nodes()<=7 and nx.is_connected(G):
        n,m,d,K,gut=exact_data(G)
        # Exact universal inequalities used in the proof.
        assert K <= d*m
        assert 2*m*K <= gut
        # Counterexample search only (NOT used as theorem): K <= m*diam/2.
        # Verify exactly on the full Graph Atlas connected class through n=7.
        assert 2*K <= m*d
        rr=sp.cancel(2*K/(m*d))
        if rr > max_ratio:
            max_ratio=rr
            max_ratio_data=(n,m,d,K,nx.to_graph6_bytes(nx.convert_node_labels_to_integers(G),header=False).decode().strip())
        count += 1
print("finite_connected_graphs_checked",count,"PASS")
print("finite_counterexample_search_K_le_md_over_2", "PASS", "max_ratio_2K_over_md", max_ratio, "at", max_ratio_data)

delta=sp.symbols('delta', nonnegative=True)
profile=delta*(1-delta)**2/sp.sqrt(32)
deriv=sp.factor(sp.diff(profile,delta))
assert deriv == sp.sqrt(2)*(delta-1)*(3*delta-1)/8
Unew=sp.simplify(profile.subs(delta,sp.Rational(1,3)))
assert Unew == sp.sqrt(2)/54

# Endpoint and critical-point comparison on [0,1].
assert profile.subs(delta,0)==0
assert profile.subs(delta,1)==0
assert Unew>0

L=sp.Rational(1,54)
Uold=2*sp.sqrt(10)/125
Wold=sp.simplify(Uold-L)
Wnew=sp.simplify(Unew-L)
assert sp.simplify(Uold-Unew)>0
assert Wnew == (sp.sqrt(2)-1)/54
ratio=sp.N(Wnew/Wold,20)

print("U_old",Uold,"approx",sp.N(Uold,20))
print("U_new",Unew,"approx",sp.N(Unew,20))
print("L",L,"approx",sp.N(L,20))
print("width_old",Wold,"approx",sp.N(Wold,20))
print("width_new",Wnew,"approx",sp.N(Wnew,20))
print("new_over_old_width",ratio)
print("relative_narrowing",sp.N(1-Wnew/Wold,20))
print("RESULT PASS")
