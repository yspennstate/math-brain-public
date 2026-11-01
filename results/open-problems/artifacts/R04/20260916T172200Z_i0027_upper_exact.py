import sympy as sp
import networkx as nx

print("R04 I0027 upper-bound algebra checker")
print("SELF-CHECK: verifies reductions/constants; Mukwembi 2012 theorem is external input")

def exact_indices(G):
    G=nx.convert_node_labels_to_integers(G,ordering="sorted")
    n=G.number_of_nodes(); m=G.number_of_edges()
    L=sp.zeros(n,n); deg=[G.degree(i) for i in range(n)]
    for i in range(n):
        L[i,i]=deg[i]
    for i,j in G.edges():
        L[i,j]-=1; L[j,i]-=1
    ds=dict(nx.all_pairs_shortest_path_length(G))
    R=L[:n-1,:n-1].inv()
    rstar=sp.Rational(0); gut=sp.Rational(0)
    for i in range(n):
        for j in range(i+1,n):
            if j==n-1: rij=R[i,i]
            elif i==n-1: rij=R[j,j]
            else: rij=R[i,i]+R[j,j]-2*R[i,j]
            rstar += deg[i]*deg[j]*rij
            gut += deg[i]*deg[j]*ds[i][j]
    K=sp.cancel(rstar/(2*m))
    return K,gut,m,n

atlas=nx.graph_atlas_g()
checked=0
for G in atlas:
    if 2<=G.number_of_nodes()<=7 and nx.is_connected(G):
        K,gut,m,n=exact_indices(G)
        assert K <= gut/(2*m)
        assert K <= (n-1)*m
        checked+=1
print("finite_graph_checks",checked,"PASS")

# Asymptotic envelope from Mukwembi 2012:
# Gut(G) <= (2^4/5^5)n^5 + O(n^4), alpha=m/n^2.
# Thus K/n^3 <= min(alpha, (2^3/5^5)/alpha)+o(1).
c=sp.Rational(2**3,5**5)
U=sp.sqrt(c)
assert sp.simplify(U-2*sp.sqrt(10)/125)==0
L=sp.Rational(1,54)
oldU=sp.Rational(2,27)
oldW=sp.simplify(oldU-L)
newW=sp.simplify(U-L)
assert oldW==sp.Rational(1,18)
assert sp.simplify(newW-(108*sp.sqrt(10)-125)/6750)==0
assert sp.N(U) < sp.N(oldU)
print("new_U",U,"approx",sp.N(U,15))
print("L",L,"old_U",oldU)
print("old_width",oldW,"approx",sp.N(oldW,15))
print("new_width",newW,"approx",sp.N(newW,15))
print("width_ratio",sp.N(newW/oldW,15))
print("RESULT PASS")
