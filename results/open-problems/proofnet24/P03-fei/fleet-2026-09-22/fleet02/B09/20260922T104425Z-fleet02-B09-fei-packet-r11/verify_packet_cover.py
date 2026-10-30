#!/usr/bin/env python3
"""Deterministic diagnostics for FEI-SIGNED-PACKET-NONREUSE-v1.
No numerical output is used as proof. Standard library only.
"""
from math import log2, sqrt, log1p, expm1


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*log2(x)-(1.0-x)*log2(1.0-x)


def solve_c(r):
    mu=sum(r)
    if abs(mu-1.0) < 1e-14:
        return 0.0
    def F(c):
        logs=sum(log1p(-c*ri) for ri in r)
        return -expm1(logs)-c
    lo=1e-12
    while F(lo) <= 0.0 and lo < 1e-2:
        lo *= 10.0
    hi=1.0
    assert F(lo) > 0.0 and F(hi) <= 0.0
    for _ in range(220):
        mid=(lo+hi)/2.0
        if F(mid) > 0.0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0


def sparse(m):
    p=2.0**(1-m)
    B=(-16.0*(1-p)**(2*m)
       +24.0*(1-p)**m
       -8.0*(1+p-2*p*p)**m
       +(1+4*p-4*p*p)**m
       -1.0)
    theta=B/(2.0**m)
    packet=-0.5*log2(1.0-theta)
    Hg=(-(1-p)**2*log2((1-p)**2)
        +(2*p-p*p)*(2*m-2))
    K=m*h2(p)-Hg
    assert theta >= -1e-12 and theta < 1.0
    assert packet <= K + 2e-10
    return p,K,theta,packet,packet/K


def twoflip(n):
    q=2.0**(2-n)
    support=[s for s in range(1<<n) if s.bit_count() & 1]
    P={}
    sign={}
    for s in support:
        if s == 1:
            a=1.0-q
            sign[s]=1.0
        else:
            a=-q
            sign[s]=-1.0
        P[s]=a*a
    assert abs(sum(P.values())-1.0) < 2e-12
    r=[sum(v for s,v in P.items() if (s>>i)&1) for i in range(n)]
    c=solve_c(r)
    t=[c*ri for ri in r]
    Q={}
    for s in range(1,1<<n):
        z=1.0
        for i,ti in enumerate(t):
            z *= ti if ((s>>i)&1) else (1.0-ti)
        Q[s]=z/c
    assert abs(sum(Q.values())-1.0) < 2e-10
    K=sum(p*log2(p/Q[s]) for s,p in P.items())
    qA=sum(Q[s] for s in support)
    Ksupp=-log2(qA)
    Qbar={s:Q[s]/qA for s in support}
    theta=0.0
    for T in range(1,1<<n):
        active=[s for s in support if (s^T) in P]
        if not active:
            continue
        R=sum(sign[s]*sign[s^T]*sqrt(Qbar[s]*Qbar[s^T]) for s in active)
        theta += (R*R)/len(active)
    packet=-0.5*log2(1.0-theta)
    lower=Ksupp+packet
    assert theta >= -1e-12 and theta < 1.0
    assert lower <= K + 2e-9
    return c,K,Ksupp,theta,packet,lower,lower/K


print("SPARSE_SUSPENSION")
print("m p K theta packet_lb ratio")
for m in (4,6,8,10,12,14):
    p,K,theta,packet,ratio=sparse(m)
    print(m, f"{p:.12g}", f"{K:.12g}", f"{theta:.12g}",
          f"{packet:.12g}", f"{ratio:.12g}")

print("TWO_FLIP_NEAR_DICTATOR")
print("n c K Ksupport theta packet_shape total_lb ratio")
for n in range(3,11):
    vals=twoflip(n)
    print(n, *(f"{x:.12g}" for x in vals))

c3=3.0-sqrt(5.0)
t3=c3/2.0
kappa3=(3.0*h2(t3)-h2(c3))/c3-2.0
print("RM3_LOCAL_K", f"{kappa3:.15g}")
for m in (4,6,8,10,12):
    mu=1.5**m
    local=2.0*kappa3*(mu-1.0)
    source_K_lower=mu*(m-4.0)+2.0
    hierarchy_lower=source_K_lower-local
    print("RM3", m, f"mu={mu:.12g}", f"local={local:.12g}",
          f"K_source_lower={source_K_lower:.12g}",
          f"hierarchy_lower={hierarchy_lower:.12g}")

print("PASS")
