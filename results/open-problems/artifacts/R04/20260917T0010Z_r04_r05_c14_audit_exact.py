#!/usr/bin/env python3
from fractions import Fraction
import sympy as sp
import networkx as nx

print("R04 independent audit of R05-I0030-C14")
print("SELF-CHECK: finite/symbolic core only; general Hausdorff-moment proof audited on page")

def qmatrix(G, h):
    G=nx.convert_node_labels_to_integers(G)
    n=G.number_of_nodes()
    ds={G.degree(v) for v in G}
    assert len(ds)==1
    d=next(iter(ds))
    A=sp.zeros(n,n)
    for u,v in G.edges():
        A[u,v]=A[v,u]=1
    hs=sp.Rational(h.numerator,h.denominator)
    return hs*sp.eye(n)+(1-hs)*A/sp.Integer(d)

def check_graph(G, name, h, steps=8):
    G=nx.convert_node_labels_to_integers(G)
    x,y=next(iter(G.edges()))
    Q=qmatrix(G,h)
    vals=[]
    M=sp.eye(G.number_of_nodes())
    for m in range(steps):
        vals.append(sp.cancel(M[x,y]/M[x,x]))
        M=M*Q
    for a,b in zip(vals, vals[1:]):
        assert sp.simplify(b-a) >= 0
    print(name, "h=", h, "ratios=", vals, "NONDECREASING PASS")

tests=[
    ("K2", nx.complete_graph(2)),
    ("C5", nx.cycle_graph(5)),
    ("K4", nx.complete_graph(4)),
    ("Q3", nx.convert_node_labels_to_integers(nx.hypercube_graph(3))),
    ("Petersen", nx.petersen_graph()),
]
for name,G in tests:
    for h in (Fraction(1,2), Fraction(3,4)):
        check_graph(G,name,h)

h=sp.symbols("h", positive=True)
c=2*h-1
r1=(1-c)/(1+c)
r2=(1-c**2)/(1+c**2)
diff=sp.factor(r1-r2)
assert sp.simplify(diff-(h-1)*(2*h-1)/(h*(2*h**2-2*h+1)))==0
print("K2 r1-r2 =", diff)
print("For 0<h<1/2 both (h-1) and (2h-1) are negative and denominator positive: r1>r2 PASS")

Q=qmatrix(nx.complete_graph(2), Fraction(1,2))
assert Q**2 == Q
assert Q[0,1]/Q[0,0] == 1
print("K2 h=1/2 idempotent boundary equality after first step PASS")

for name,G in tests:
    G=nx.convert_node_labels_to_integers(G)
    x,y=next(iter(G.edges()))
    hq=Fraction(3,4)
    Q=qmatrix(G,hq)
    M=sp.eye(G.number_of_nodes())
    hs=sp.Rational(3,4)
    for m in range(6):
        lhs=(M*Q)[x,x]
        rhs=hs*M[x,x]+(1-hs)*M[x,y]
        assert sp.simplify(lhs-rhs)==0
        M=M*Q
print("C14.1 one-step identity exact sample checks PASS")

print("AUDIT RESULT: PASS_MATH for R05-I0030-C14; novelty not audited")
