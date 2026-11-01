#!/usr/bin/env python3
from fractions import Fraction
import heapq
import itertools
import sympy as sp

print("R07 weighted-overlap / R08 audit exact checker")
print("seed: deterministic / no randomness")

# ------------------------------------------------------------
# 1) Exact finite product-refresh derivative identity on {0,1}^3.
# ------------------------------------------------------------
rho = sp.symbols('rho')
states = list(itertools.product([0,1], repeat=3))
# fixed rational-valued test function, deliberately non-additive
vals = {
    x: sp.Rational(
        3*x[0] + 5*x[1] - 2*x[2] + 7*x[0]*x[1] - 4*x[1]*x[2] + 9*x[0]*x[1]*x[2],
        11
    )
    for x in states
}
Ef = sum(vals[x] for x in states) / 8
fc = {x: sp.simplify(vals[x]-Ef) for x in states}

def trans_prob(x,y):
    # each coordinate: survive with prob rho, else resample fair bit
    p = sp.Integer(1)
    for xi,yi in zip(x,y):
        if xi == yi:
            p *= rho + (1-rho)/2
        else:
            p *= (1-rho)/2
    return sp.expand(p)

C = sp.Integer(0)
for x in states:
    for y in states:
        C += sp.Rational(1,8)*trans_prob(x,y)*fc[x]*fc[y]
C = sp.factor(sp.expand(C))

# D_i f(x) = f(x)-E_i f conditioned on the other bits
Ds = []
for i in range(3):
    Di = {}
    for x in states:
        x0=list(x); x1=list(x)
        x0[i]=0; x1[i]=1
        avg=(vals[tuple(x0)]+vals[tuple(x1)])/2
        Di[x]=sp.simplify(vals[x]-avg)
    Ds.append(Di)

rhs = sp.Integer(0)
for i in range(3):
    for x in states:
        for y in states:
            rhs += sp.Rational(1,8)*trans_prob(x,y)*Ds[i][x]*Ds[i][y]
rhs = sp.factor(sp.expand(rhs))
lhs = sp.factor(sp.expand(rho*sp.diff(C,rho)))
assert sp.simplify(lhs-rhs) == 0
print("finite refresh derivative identity: PASS")
print("  C(rho) =", C)
print("  rho*C'(rho) =", lhs)

# ------------------------------------------------------------
# 2) Exact algebraic covariance-kernel decomposition.
# For 0<=r<=s, let a=e^{-r}, b=e^{-s}. Formula:
# kappa=1-(r+1)a+(1-r)b-ab
# q(r)=1-2 r a-a^2
# kappa-q=(a-b)(r-1+a)
# ------------------------------------------------------------
r,a,b = sp.symbols('r a b')
kappa = 1-(r+1)*a+(1-r)*b-a*b
q = 1-2*r*a-a*a
assert sp.expand(kappa-q-(a-b)*(r-1+a)) == 0
print("kernel decomposition algebra: PASS")

# ------------------------------------------------------------
# Helpers for exact rational Dijkstra on a 2-row ladder.
# ------------------------------------------------------------
def build_ladder(m, horiz, eps):
    # vertices (0..L) x {0,1}; L=m+1
    L=m+1
    verts=[(i,j) for i in range(L+1) for j in (0,1)]
    idx={v:k for k,v in enumerate(verts)}
    edges=[]; adj=[[] for _ in verts]
    H=Fraction(10*L+10,1)+eps
    def add(u,v,w,tag):
        eid=len(edges)
        edges.append((idx[u],idx[v],w,tag,u,v))
        adj[idx[u]].append((eid,idx[v],w))
        adj[idx[v]].append((eid,idx[u],w))
    for i in range(L):
        add((i,0),(i+1,0),horiz,("bottom",i))
        add((i,1),(i+1,1),horiz,("top",i))
    add((0,0),(0,1),eps/2,("rung",0))
    add((L,0),(L,1),eps/2,("rung",L))
    for i in range(1,L):
        add((i,0),(i,1),H,("rung",i))
    return L,verts,idx,edges,adj

def dij(adj,s,t,removed=None):
    n=len(adj)
    INF=None
    dist=[INF]*n
    count=[0]*n
    dist[s]=Fraction(0); count[s]=1
    pq=[(Fraction(0),s)]
    while pq:
        du,u=heapq.heappop(pq)
        if du != dist[u]: continue
        for eid,v,w in adj[u]:
            if eid == removed: continue
            nd=du+w
            if dist[v] is None or nd<dist[v]:
                dist[v]=nd; count[v]=count[u]; heapq.heappush(pq,(nd,v))
            elif nd==dist[v]:
                count[v]+=count[u]
    return dist[t],count[t]

def edge_id(edges, tag):
    for eid,e in enumerate(edges):
        if e[3]==tag:
            return eid
    raise KeyError(tag)

# ------------------------------------------------------------
# 3) Independent exact audit of R08-X001.
# ------------------------------------------------------------
eps_list=[Fraction(1,7),Fraction(2,5),Fraction(3,2),Fraction(17,13)]
cases=0
for m in range(1,21):
    for eps in eps_list:
        L,verts,idx,edges,adj=build_ladder(m,Fraction(1),eps)
        s=idx[(0,0)]; t=idx[(L,0)]
        d,c=dij(adj,s,t)
        assert d==L and c==1
        for i in range(m):
            eid=edge_id(edges,("bottom",i))
            dd,cc=dij(adj,s,t,removed=eid)
            assert dd==Fraction(L)+eps
            assert cc==1
        cases+=1
print(f"R08-X001 independent audit: PASS ({cases} parameter cases)")

# ------------------------------------------------------------
# 4) Shallow-overlap ladder: m common geodesic edges, but each
# off-edge cavity threshold R_e = 2/m. Analytic q(R)<=R^3 then gives
# sum q(R_e)<=8/m^2.
# ------------------------------------------------------------
for m in range(2,41):
    a0=Fraction(1,m)
    eps=a0
    L,verts,idx,edges,adj=build_ladder(m,a0,eps)
    s=idx[(0,0)]; t=idx[(L,0)]
    d,c=dij(adj,s,t)
    assert d==Fraction(L,m) and c==1
    for i in range(m):
        eid=edge_id(edges,("bottom",i))
        A,_=dij(adj,s,t,removed=eid)  # avoid e
        # best "using e" cost excluding its own weight: bottom route minus a0
        B=d-a0
        R=A-B
        assert R==Fraction(2,m)
    exact_bound=Fraction(8,m*m)
    assert exact_bound == m*Fraction(2,m)**3
print("shallow-overlap thresholds / 8 m^{-2} bound: PASS")

print("PASS")
