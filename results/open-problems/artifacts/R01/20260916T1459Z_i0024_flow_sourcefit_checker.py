#!/usr/bin/env python3
"""R01/I0024 run-3 exact self-check.

Checks the state-to-stationarity Gram-flow formula and compares a concrete
path-routing operator with the two Aldous-Fill Theorem 4.32 congestion
majorants on exact rational weighted graphs.  Finite checks do not replace
the universal proof in the run report.
"""
import sympy as sp
import random
Q=sp.Rational
SEED=202609161459
rng=random.Random(SEED)

def graph_data(weights):
    n=max(max(e) for e in weights)+1
    deg=[sum(w for (i,j),w in weights.items() if i==v or j==v) for v in range(n)]
    W=sum(deg)
    pi=[sp.simplify(d/W) for d in deg]
    edges=sorted(weights)
    B=sp.zeros(n,len(edges))
    for k,(i,j) in enumerate(edges): B[i,k]=1; B[j,k]=-1
    C=sp.diag(*[sp.simplify(weights[e]/W) for e in edges])
    Pi=sp.diag(*pi)
    P=sp.zeros(n)
    for (i,j),ww in weights.items():
        P[i,j]=sp.simplify(ww/deg[i]); P[j,i]=sp.simplify(ww/deg[j])
    L=sp.simplify(B*C*B.T)
    assert L==sp.simplify(Pi*(sp.eye(n)-P))
    J=sp.ones(n,n)
    Lp=sp.simplify((L+J/Q(n)).inv()-J/Q(n))
    return n,W,pi,edges,B,C,Pi,P,Lp

def h0_basis(n):
    K=sp.zeros(n,n-1)
    for i in range(n-1): K[i,i]=1; K[n-1,i]=-1
    return K

def centered_h_basis(pi):
    n=len(pi); H=sp.zeros(n,n-1)
    for i in range(n-1): H[i,i]=1; H[n-1,i]=-pi[i]/pi[n-1]
    assert sp.Matrix([pi])*H==sp.zeros(1,n-1)
    return H

def geigs(M,N):
    lam=sp.symbols('lam'); poly=sp.factor((M-lam*N).det())
    return [sp.simplify(x) for x in sp.solve(sp.Eq(poly,0),lam)],poly

def tau_from_P(P):
    ev=[]
    for z,m in P.eigenvals().items(): ev += [sp.simplify(z)]*m
    ev=sorted(ev,key=lambda z:float(sp.N(z)),reverse=True)
    return sp.simplify(1/(1-ev[1]))

def gram_check(weights):
    n,W,pi,edges,B,C,Pi,P,Lp=graph_data(weights)
    pivec=sp.Matrix(pi); R=sp.simplify(C*B.T*Lp)
    Psi=sp.zeros(len(edges),n)
    for x in range(n):
        d=sp.zeros(n,1); d[x]=1; d-=pivec
        Psi[:,x]=sp.simplify(R*d)
        assert sp.simplify(B*Psi[:,x]-d)==sp.zeros(n,1)
    assert sp.simplify(Psi*pivec)==sp.zeros(len(edges),1)
    G=sp.simplify(Psi.T*C.inv()*Psi); H=centered_h_basis(pi)
    vals,poly=geigs(sp.simplify(H.T*Pi*G*Pi*H),sp.simplify(H.T*Pi*H))
    tau=tau_from_P(P)
    assert any(sp.simplify(v-tau)==0 for v in vals)
    assert max(float(sp.N(v)) for v in vals)==float(sp.N(tau))
    return tau,vals,poly

def path_flow(path,edges):
    idx={e:k for k,e in enumerate(edges)}; f=sp.zeros(len(edges),1)
    for a,b in zip(path,path[1:]):
        if a<b: f[idx[(a,b)]]+=1
        else: f[idx[(b,a)]]-=1
    return f

def path_check(weights,paths):
    n,W,pi,edges,B,C,Pi,P,Lp=graph_data(weights); pivec=sp.Matrix(pi)
    for x in range(n):
        for y in range(n): assert paths[(y,x)]==list(reversed(paths[(x,y)]))
    Psi=sp.zeros(len(edges),n)
    for x in range(n):
        col=sp.zeros(len(edges),1)
        for y in range(n):
            if x!=y: col += pi[y]*path_flow(paths[(x,y)],edges)
        Psi[:,x]=sp.simplify(col)
        rhs=sp.zeros(n,1); rhs[x]=1; rhs-=pivec
        assert sp.simplify(B*Psi[:,x]-rhs)==sp.zeros(n,1)
    assert sp.simplify(Psi*pivec)==sp.zeros(len(edges),1)
    K=h0_basis(n)
    vals,_=geigs(sp.simplify(K.T*Psi.T*C.inv()*Psi*K),sp.simplify(K.T*Pi.inv()*K))
    rc=max(vals,key=lambda z:float(sp.N(z)))
    L1={}; L2={}
    for (i,j),wij in weights.items():
        for arc in ((i,j),(j,i)):
            a=b=Q(0)
            for x in range(n):
                for y in range(n):
                    if x==y: continue
                    path=paths[(x,y)]; steps=list(zip(path,path[1:]))
                    if arc not in steps: continue
                    resistance=sum(Q(1,1)/weights[tuple(sorted(e))] for e in steps)
                    a += pi[x]*pi[y]*resistance
                    b += pi[x]*pi[y]*len(steps)
            L1[arc]=sp.simplify(a); L2[arc]=sp.simplify(b)
    k1=sp.simplify(W*max(L1.values(),key=lambda z:float(sp.N(z))))
    k2=sp.simplify(W*max([L2[a]/weights[tuple(sorted(a))] for a in L2],key=lambda z:float(sp.N(z))))
    tau=tau_from_P(P)
    assert float(sp.N(tau))<=float(sp.N(rc))+1e-14
    assert float(sp.N(rc))<=float(sp.N(k1))+1e-14
    assert float(sp.N(rc))<=float(sp.N(k2))+1e-14
    return tau,rc,k1,k2,vals

P4={(0,1):Q(1),(1,2):Q(1),(2,3):Q(1)}
p4={}
for x in range(4):
    for y in range(4): p4[(x,y)]=list(range(x,y+1)) if x<=y else list(range(x,y-1,-1))
K3={(0,1):Q(1),(0,2):Q(1),(1,2):Q(1)}
k3={(x,y):([x] if x==y else [x,y]) for x in range(3) for y in range(3)}
WT={(0,1):Q(1),(0,2):Q(2),(1,2):Q(3)}
wt={(x,y):([x] if x==y else [x,y]) for x in range(3) for y in range(3)}
for name,w,p in (("P4",P4,p4),("K3",K3,k3),("weighted_triangle_1_2_3",WT,wt)):
    tau,vals,poly=gram_check(w)
    print("GRAM",name,"tau=",tau,"generalized_eigs=",vals,"charpoly=",poly)
    tau,rc,k1,k2,vals=path_check(w,p)
    print("PATH",name,"tau=",tau,"route_cost=",rc,"AF_kappa1=",k1,"AF_kappa2=",k2,"route_eigs=",vals)

# Projection lemma for antisymmetric kernels D_xy=-D_yx.
for _ in range(250):
    n=rng.randint(2,6); raw=[rng.randint(1,9) for _ in range(n)]; den=sum(raw)
    pi=[Q(x,den) for x in raw]; D=sp.zeros(n,n)
    for i in range(n):
        for j in range(i+1,n):
            v=Q(rng.randint(-9,9),rng.randint(1,9)); D[i,j]=v; D[j,i]=-v
    g=D*sp.Matrix(pi)
    assert sp.simplify((sp.Matrix([pi])*g)[0])==0
    var=sp.simplify(sum(pi[i]*g[i]**2 for i in range(n)))
    ed2=sp.simplify(sum(pi[i]*pi[j]*D[i,j]**2 for i in range(n) for j in range(n)))
    assert sp.simplify(ed2-2*var)>=0
print("ANTISYMMETRIC PROJECTION FACTOR PASS trials=250")
print("SEED =",SEED)
print("ALL CHECKS PASS")
