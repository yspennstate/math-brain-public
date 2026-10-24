#!/usr/bin/env python3
from fractions import Fraction
import itertools, math
import sympy as sp

def K4():
    V=list(range(4))
    E=[tuple(e) for e in itertools.combinations(V,2)]
    return V,E

def K33():
    V=list(range(6))
    E=[(u,v) for u in range(3) for v in range(3,6)]
    return V,E

def build(V,E):
    E=[tuple(sorted(e)) for e in E]
    idxE={e:i for i,e in enumerate(E)}
    adj={u:set() for u in V}
    for u,v in E:
        adj[u].add(v); adj[v].add(u)
    ds={len(adj[u]) for u in V}
    assert len(ds)==1
    d=ds.pop(); q=d-1
    arcs=[]
    for u,v in E:
        arcs.extend([(u,v),(v,u)])
    idxA={a:i for i,a in enumerate(arcs)}
    n=len(V); m=len(E); N=len(arcs)

    P=sp.zeros(n,n)
    for u in V:
        for v in adj[u]:
            P[u,v]=sp.Rational(1,d)

    QL=sp.zeros(m,m)
    for i,(u,v) in enumerate(E):
        neigh=set()
        for w in adj[u]:
            ee=tuple(sorted((u,w)))
            if ee != (u,v): neigh.add(ee)
        for w in adj[v]:
            ee=tuple(sorted((v,w)))
            if ee != (u,v): neigh.add(ee)
        assert len(neigh)==2*q
        for ee in neigh:
            QL[i,idxE[ee]]=sp.Rational(1,2*q)

    QA=sp.zeros(N,N)
    for i,(u,v) in enumerate(arcs):
        neigh=[]
        for w in adj[v]:
            if w!=u: neigh.append((v,w))
        for w in adj[u]:
            if w!=v: neigh.append((w,u))
        assert len(neigh)==2*q and len(set(neigh))==2*q
        for b in neigh:
            QA[i,idxA[b]]=sp.Rational(1,2*q)

    Lift=sp.zeros(N,m)
    for i,a in enumerate(arcs):
        Lift[i,idxE[tuple(sorted(a))]]=1
    assert QA*Lift == Lift*QL

    J=sp.zeros(N,N)
    for i,(u,v) in enumerate(arcs):
        J[i,idxA[(v,u)]]=1
    assert QA*J == J*QA
    assert J*J == sp.eye(N)

    Div=sp.zeros(n,N)
    Grad=sp.zeros(N,n)
    for i,(u,v) in enumerate(arcs):
        Div[u,i]=1
        Grad[i,v]=1
        Grad[i,u]=-1
    assert Div*Grad == d*(P-sp.eye(n))

    # Verify odd formula on antisymmetric basis f_e.
    for u,v in E:
        f=sp.zeros(N,1)
        f[idxA[(u,v)],0]=1
        f[idxA[(v,u)],0]=-1
        assert J*f == -f
        lhs=QA*f
        rhs=sp.Rational(1,q)*f + sp.Rational(1,2*q)*Grad*(Div*f)
        assert lhs==rhs

    # Predicted spectrum, including multiplicities.
    base=P.eigenvals()
    predicted={}
    def add(ev,mul):
        ev=sp.simplify(ev)
        predicted[ev]=predicted.get(ev,0)+mul
    # even: base modes plus extra line-graph kernel modes
    for lam,mul in base.items():
        add((d*lam+d-2)/(2*q), mul)
    add(sp.Rational(-1,q), m-n)
    # odd gradients: omit constant lambda=1 mode because gradient vanishes
    for lam,mul in base.items():
        if sp.simplify(lam-1)!=0:
            add((d*lam-(d-2))/(2*q), mul)
    add(sp.Rational(1,q), m-n+1)
    actual={sp.simplify(k):v for k,v in QA.eigenvals().items()}
    assert actual==predicted, (actual,predicted)

    # Hodge projection for one oriented edge: cycle part is divergence-free.
    u,v=E[0]
    f=sp.zeros(N,1)
    f[idxA[(u,v)],0]=1
    f[idxA[(v,u)],0]=-1
    b=Div*f
    # solve d(P-I)g=b with gauge g[last]=0
    A=d*(P-sp.eye(n))
    # replace last equation by gauge
    Ag=A.copy(); bg=b.copy()
    for j in range(n): Ag[n-1,j]=0
    Ag[n-1,n-1]=1; bg[n-1,0]=0
    g=Ag.inv()*bg
    cyc=f-Grad*g
    assert Div*cyc==sp.zeros(n,1)
    assert sp.simplify(QA*cyc-sp.Rational(1,q)*cyc)==sp.zeros(N,1)

    return d,q,n,m,N,P,QL,QA,cyc

def eigfmt(M):
    items=sorted([(str(sp.simplify(k)),v) for k,v in M.eigenvals().items()])
    return ", ".join(f"{k}^{v}" for k,v in items)

for name,fn in [("K4",K4),("K3,3",K33)]:
    V,E=fn()
    d,q,n,m,N,P,QL,QA,cyc=build(V,E)
    print(f"{name}: d={d}, q={q}, |E|={m}, |arcs|={N}")
    print("  base spectrum:",eigfmt(P))
    print("  line spectrum:",eigfmt(QL))
    print("  arc spectrum: ",eigfmt(QA))
    print("  exact projection/lumping: PASS")
    print("  exact odd Hodge formula: PASS")
    print("  exact cycle eigenvalue 1/q: PASS")
    print("  cycle projection l1:",sp.simplify(sum(abs(x) for x in cyc)))

# Degree-six explicit theorem arithmetic.
d=6; q=5
center=sp.Rational(2*q,q-1)
odd_rate=sp.Rational(q-1,q)
assert center==sp.Rational(5,2)
assert sp.simplify(odd_rate*center-2)==0
gap_even=sp.Rational(d,2*q)*(1-sp.sqrt(5)/3)
gap_claim=(3-sp.sqrt(5))/5
assert sp.simplify(gap_even-gap_claim)==0
assert gap_claim>0
assert sp.Rational(q-1,q)>gap_claim
assert 2*q-1>q
print("degree-6 explicit family:")
print("  output degree =",2*q)
print("  center coefficient =",center,"for log_5 n")
print("  odd decay rate =",odd_rate)
print("  odd exponent at center =",sp.simplify(odd_rate*center),"* log_5 n")
print("  spectral-gap lower bound =",gap_claim)
print("  LRE branching separation:",2*q-1,">",q)

# Root-stabilizer quotient stress test: Q_3 Hamming-weight quotient.
d=3
sizes=[1,3,3,1]
c=[]
for k in range(4):
    row=[0]*4
    if k>0: row[k-1]=k
    if k<3: row[k+1]=3-k
    c.append(row)
for i in range(4):
    assert sum(c[i])==d
    for j in range(4):
        if c[i][j]:
            assert sizes[i]*c[i][j]==sizes[j]*c[j][i]
            assert Fraction(sizes[j],sizes[i])==Fraction(c[i][j],c[j][i])
            assert Fraction(1,d)<=Fraction(sizes[j],sizes[i])<=d
print("Q3 stabilizer quotient:")
print("  orbit sizes =",sizes)
print("  neighbor counts =",c)
print("  integer transition alphabet/local-ratio identities: PASS")

print("ALL_EXACT_CHECKS_PASS")
