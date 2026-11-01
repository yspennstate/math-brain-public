#!/usr/bin/env python3
from fractions import Fraction
from collections import deque
import itertools, math, mpmath as mp

mp.mp.dps=80

def graph(n):
    V=[(i,j) for i in range(2*n+1) for j in range(n+1)]
    E=[]
    for i in range(2*n):
        for j in range(n+1):
            E.append(((i,j),(i+1,j)))
    for i in range(2*n+1):
        for j in range(n):
            E.append(((i,j),(i,j+1)))
    return V,E

def lr_crossing(n, E, mask):
    adj={}
    for v in [(i,j) for i in range(2*n+1) for j in range(n+1)]:
        adj[v]=[]
    for k,e in enumerate(E):
        if (mask>>k)&1:
            a,b=e
            adj[a].append(b); adj[b].append(a)
    q=deque((0,j) for j in range(n+1))
    seen=set(q)
    while q:
        v=q.popleft()
        if v[0]==2*n:
            return True
        for w in adj[v]:
            if w not in seen:
                seen.add(w); q.append(w)
    return False

# Structural finite checks n=1..8.
for n in range(1,9):
    V,E=graph(n)
    rows=[]
    for j in range(n+1):
        row={tuple(sorted(((i,j),(i+1,j)))) for i in range(2*n)}
        assert len(row)==2*n
        rows.append(row)
    for a,b in itertools.combinations(rows,2):
        assert a.isdisjoint(b)

    cuts=[]
    for i in range(2*n):
        cut={tuple(sorted(((i,j),(i+1,j)))) for j in range(n+1)}
        assert len(cut)==n+1
        cuts.append(cut)
    for a,b in itertools.combinations(cuts,2):
        assert a.isdisjoint(b)
print("STRUCTURE n=1..8: PASS")

# Exhaustive n=1 exact enumeration: 7 edges, 128 states.
n=1
V,E=graph(n)
assert len(E)==7
cross_count=0
all_row_implies=True
cross_implies_every_cut=True
for mask in range(1<<len(E)):
    cross=lr_crossing(n,E,mask)
    if cross:
        cross_count+=1

    def open_edge(e):
        ee=tuple(sorted(e))
        for k,f in enumerate(E):
            if tuple(sorted(f))==ee:
                return bool((mask>>k)&1)
        raise RuntimeError

    allrow=False
    for j in range(n+1):
        if all(open_edge(((i,j),(i+1,j))) for i in range(2*n)):
            allrow=True
            break
    if allrow and not cross:
        all_row_implies=False

    if cross:
        for i in range(2*n):
            if not any(open_edge(((i,j),(i+1,j))) for j in range(n+1)):
                cross_implies_every_cut=False

assert all_row_implies
assert cross_implies_every_cut
p1=Fraction(cross_count,1<<len(E))
ell1=1-(1-Fraction(1,2**(2*n)))**(n+1)
u1=(1-Fraction(1,2**(n+1)))**(2*n)
assert ell1 <= p1 <= u1
print("N=1 exhaustive: PASS")
print("cross_count =", cross_count, "of", 1<<len(E))
print("p1 =", p1, "=", float(p1))
print("ell1 =", ell1, "u1 =", u1)

# Cardy normalization for aspect ratio width/height=2.
K=lambda m: mp.ellipk(m)
eta=mp.findroot(lambda x: K(1-x)/K(x)-2, (mp.mpf("0.01"),mp.mpf("0.05")))
C=(3*mp.gamma(mp.mpf(2)/3)/(mp.gamma(mp.mpf(1)/3)**2)
   *eta**(mp.mpf(1)/3)
   *mp.hyp2f1(mp.mpf(1)/3,mp.mpf(2)/3,mp.mpf(4)/3,eta))
print("eta2 =", mp.nstr(eta,60))
print("Cardy_C2 =", mp.nstr(C,60))

def bounds(n):
    ell=mp.mpf(1)-(mp.mpf(1)-mp.power(2,-2*n))**(n+1)
    u=(mp.mpf(1)-mp.power(2,-(n+1)))**(2*n)
    b=max(abs(ell-C),abs(u-C))
    return ell,u,b

for n in [1,2,4,8,16,32,64,128]:
    ell,u,b=bounds(n)
    print("n=%d delta=%s ell=%s u=%s b=%s" %
          (n, mp.nstr(mp.mpf(1)/n,12), mp.nstr(ell,20),
           mp.nstr(u,20), mp.nstr(b,20)))

limit_b=max(C,1-C)
assert abs(limit_b-(1-C)) < mp.mpf("1e-70")
print("lim_b =", mp.nstr(limit_b,60))
print("PASS")
