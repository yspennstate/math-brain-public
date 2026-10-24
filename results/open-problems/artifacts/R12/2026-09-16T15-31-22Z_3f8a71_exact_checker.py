#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import sympy as sp

PRIMES=[13,17,29,41,53]

def paley(p):
    Q={x*x%p for x in range(1,p)}
    adj=[set() for _ in range(p)]
    for u in range(p):
        for v in range(u+1,p):
            if (u-v)%p in Q:
                adj[u].add(v); adj[v].add(u)
    return adj

def h2_graph(adj):
    p=len(adj)
    edges=[(u,v) for u in range(p) for v in adj[u] if u<v]
    H=[set() for _ in edges]
    for i,e in enumerate(edges):
        se=set(e)
        for j in range(i+1,len(edges)):
            f=edges[j]
            U=se|set(f)
            ok=True
            for a,b in combinations(sorted(U),2):
                if b not in adj[a]:
                    ok=False; break
            if ok:
                H[i].add(j); H[j].add(i)
    return edges,H

for p in PRIMES:
    adj=paley(p)
    d=(p-1)//2
    lam=(p-5)//4
    assert all(len(a)==d for a in adj)
    for u in range(p):
        for v in adj[u]:
            assert len(adj[u]&adj[v])==lam

    edges,H=h2_graph(adj)
    n=len(edges)
    assert n==p*(p-1)//4
    degs={len(a) for a in H}
    assert len(degs)==1
    dh=next(iter(degs))
    dmax=(p*p+2*p-35)//32
    assert dh<=dmax

    S=[i for i,e in enumerate(edges) if 0 in e]
    s=len(S)
    assert s==d
    Sset=set(S)
    assert all(len(H[i]&Sset)==lam for i in S)

    x=[(n-s if i in Sset else -s) for i in range(n)]
    assert sum(x)==0
    q=sum(x[i]*sum(x[j] for j in H[i]) for i in range(n))
    norm=sum(z*z for z in x)
    R=Fraction(q,norm)
    R2=(Fraction(lam,1)-Fraction(dh*s,n))/(Fraction(1,1)-Fraction(s,n))
    assert R==R2
    lower=Fraction((3*p-7)*(p-5),16*(p-2))
    assert R>=lower
    print(f"p={p} |E|={n} dH={dh} dmax={dmax} star={s} lambda={lam} "
          f"Rayleigh={R}={float(R):.9f} lower={lower}={float(lower):.9f}")

p=sp.symbols('p', positive=True)
lam=(p-5)/4
dmax=(p**2+2*p-35)/32
s_over_n=2/p
lower_expr=sp.factor((lam-dmax*s_over_n)/(1-s_over_n))
assert sp.simplify(lower_expr-(3*p-7)*(p-5)/(16*(p-2)))==0
print("C07 symbolic Rayleigh lower factorization: PASS")

n,d,L,t=sp.symbols('n d L t', positive=True)
const=sp.expand(t*(1+d)+(1-t)*n)
branch=sp.expand(t*(1+L))
tstar=sp.solve(sp.Eq(const,branch),t)[0]
V=sp.factor(branch.subs(t,tstar))
assert sp.simplify(tstar-n/(n-d+L))==0
assert sp.simplify(V-n*(1+L)/(n-d+L))==0
print("X04 adjacency-algebra intersection formula: PASS")

T,P2,P3,P4,c,p=sp.symbols('T P2 P3 P4 c p')
E=sp.symbols('E', positive=True)
k0=((2-4*c)*P2+6*P3+c**2*T)/p
k1=((1-c)**2*P2+3*(3-2*c)*P3+12*P4)/E

tt=sp.symbols('t', positive=True)
subs={
    T:tt,
    P2:tt*(tt-1)/2,
    P3:tt*(tt-1)*(tt-2)/6,
    P4:tt*(tt-1)*(tt-2)*(tt-3)/24,
    E:p*(p-1)/4,
}
k0t=sp.factor(k0.subs(subs))
k1t=sp.factor(k1.subs(subs))
assert sp.simplify(k0t-tt*(-c+tt-1)**2/p)==0

sqrtp=sp.symbols('r', positive=True)
expr0=sp.factor((k0t+((p-1)/2)*k1t).subs(p,sqrtp**2))
exprp=sp.factor((k0t+((sqrtp-1)/2)*k1t).subs(p,sqrtp**2))
exprm=sp.factor((k0t-((sqrtp+1)/2)*k1t).subs(p,sqrtp**2))
target0=tt**2*(-c+tt-1)**2/sqrtp**2
targetp=tt*(sqrtp+tt)*(-c+tt-1)**2/(sqrtp**2*(sqrtp+1))
targetm=tt*(sqrtp-tt)*(-c+tt-1)**2/(sqrtp**2*(sqrtp-1))
assert sp.simplify(expr0-target0)==0
assert sp.simplify(exprp-targetp)==0
assert sp.simplify(exprm-targetm)==0
print("X05 aggregate Gram eigenvalue factorizations: PASS")
print("ALL_EXACT_CHECKS_PASS")
