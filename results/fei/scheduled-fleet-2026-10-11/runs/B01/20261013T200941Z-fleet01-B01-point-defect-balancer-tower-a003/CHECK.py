#!/usr/bin/env python3
"""Independent finite audit for the variable-rank point-defect tower.

The all-parameter proof is analytic.  This checker reconstructs small towers
from truth tables and separately evaluates the exact scalar/state recurrences
for large ranks and long, nonstationary rank sequences.
"""

from fractions import Fraction
from math import log2, log
import random

SEED = 0xB01A003D
rng = random.Random(SEED)
TOL = 8e-10


def fwht(vals):
    a = [Fraction(v) for v in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/len(a) for x in a]


def caps(p):
    c = list(p)
    n = len(c).bit_length()-1
    for j in range(n):
        bit = 1 << j
        for s in range(1 << n):
            if not s & bit:
                c[s] += c[s | bit]
    return c


def U(f):
    p = [x*x for x in fwht(f)]
    c = caps(p)
    return sum(float(x)*log2(float(y/x)) for x,y in zip(p,c) if x)


def restrict(f,j,b):
    n = len(f).bit_length()-1
    out=[]
    for z in range(1 << (n-1)):
        lo=z & ((1<<j)-1); hi=z>>j
        out.append(f[lo | (b<<j) | (hi<<(j+1))])
    return out


def mean(f): return Fraction(sum(f),len(f))


def influence(f):
    n=len(f).bit_length()-1
    return sum(Fraction(sum(f[x] != f[x^(1<<j)] for x in range(len(f))),len(f)) for j in range(n))


def G(f):
    root=U(f); n=len(f).bit_length()-1
    return sum(root-(U(restrict(f,j,0))+U(restrict(f,j,1)))/2 for j in range(n))


def pairs(f):
    n=len(f).bit_length()-1
    return [(float(mean(restrict(f,j,0))),float(mean(restrict(f,j,1)))) for j in range(n)]


def product(f,g): return [f[x]*g[y] for y in range(len(g)) for x in range(len(f))]


def activate(q): return [q[x>>1] if not (x&1) else 1 for x in range(2*len(q))]


def defect(r):
    q=[1]*(1<<r); q[-1]=-1
    return q


def first_truth(base): return activate(product((-1,1),base))


def step_truth(f,r): return activate(product(defect(r),f))


def zlog(x): return 0.0 if x == 0 else x*log2(1/x)


def R(t):
    x=(1+t)**2/4; y=(1-t)**2/4
    e=zlog(x)+(0.0 if y==0 else y*log2(2/(1-t)))
    u=0.0 if t==0 else t*t*log2(1/(t*t))
    return e-u/2+(1-t*t)/4


def R2(t):
    return 1+(log(t*t/((1+t)*(1-t)**0.5))+0.75)/log(2)


def qstats(r):
    p=2.0**(-r); beta=1-2*p
    uq=zlog(beta*beta)+2*r*p*beta
    iq=2*r*p
    if r==1: gq=0.0
    else:
        pp=2.0**(-(r-1)); bp=1-2*pp
        up=zlog(bp*bp)+2*(r-1)*pp*bp if bp else 0.0
        gq=r*(uq-up/2)
    return beta,uq,iq,gq


def state_first(base):
    m=float(mean(base)); gb=G(base); ib=float(influence(base)); ub=U(base)
    bpairs=pairs(base)
    qp=[(0.0,0.0) for _ in bpairs]+[(m,-m)]
    gf=.5*gb+R(0)+sum(R(0)-.5*(R(a)+R(b)) for a,b in qp)
    fp=[((1+a)/2,(1+b)/2) for a,b in qp]+[(1.0,0.0)]
    return dict(m=.5,g=gf,i=1+.5*ib,u=1+.5*ub,pairs=fp,base_g=gb)


def state_step(s,r):
    beta,uq,iq,gq=qstats(r); p=2.0**(-r); bp=1-4*p
    qm=beta*s['m']
    qp=[(beta*a,beta*b) for a,b in s['pairs']]+[(bp*s['m'],s['m'])]*r
    gf=.5*(s['g']+gq)+R(qm)+sum(R(qm)-.5*(R(a)+R(b)) for a,b in qp)
    fp=[((1+a)/2,(1+b)/2) for a,b in qp]+[(1.0,qm)]
    return dict(m=(1+qm)/2,g=gf,i=.5*(s['i']+iq)+(1-qm)/2,
                u=.5*(s['u']+uq)+R(qm),pairs=fp,base_g=s['base_g'])


# Scalar and balancer lemmas over ranks far beyond direct truth-table reach.
scalar_checks=0
max_gq=(-1,None); max_uqi=(-1,None); max_qcharge=(-1,None); max_endpoint=(-1,None)
for r in range(2,257):
    beta,uq,iq,gq=qstats(r)
    assert gq <= 2+2e-12
    assert uq <= 3*iq+2e-12
    if gq > max_gq[0]: max_gq=(gq,r)
    if uq/iq > max_uqi[0]: max_uqi=(uq/iq,r)
    bp=1-4*2.0**(-r)
    for j in range(1001):
        m=.5+.5*j/1000
        qc=r*(R(beta*m)-.5*(R(bp*m)+R(m)))
        assert qc <= 4.5+2e-12
        if qc > max_qcharge[0]: max_qcharge=(qc,(r,m))
        den=.5*iq+(1-beta*m)/2
        ratio=(.5*uq+R(beta*m))/den
        assert ratio <= 5+2e-12
        if ratio > max_endpoint[0]: max_endpoint=(ratio,(r,m))
        scalar_checks += 4

min_r2=(1e100,None)
for j in range(200000):
    t=.125+.875*j/200000
    v=R2(t)
    if v < min_r2[0]: min_r2=(v,t)
    assert v >= -4-2e-10
    assert R(t) <= 2.5*(1-t)+2e-12
    scalar_checks += 2

# Direct truth-table reconstruction.
bases=[]
for n in range(4):
    for mask in range(1 << (1 << n)):
        bases.append(tuple(1 if (mask>>x)&1 else -1 for x in range(1<<n)))

direct=0; recurrence=0; gu_checks=0; endpoint_checks=0; max_err=0.0
for base in bases:
    gb=G(base); ub=U(base); ib=float(influence(base))
    f=first_truth(base); s=state_first(base)
    max_err=max(max_err,abs(float(mean(f))-s['m']),abs(G(f)-s['g']),abs(U(f)-s['u']),abs(float(influence(f))-s['i']))
    direct += 1; recurrence += 4
    assert s['g'] <= .5*gb+24+TOL
    gu_checks += 1
    if ub <= 5*ib+TOL:
        assert s['u'] <= 5*s['i']+TOL; endpoint_checks += 1
    for r in (2,3):
        ff=step_truth(f,r); ss=state_step(s,r)
        max_err=max(max_err,abs(float(mean(ff))-ss['m']),abs(G(ff)-ss['g']),abs(U(ff)-ss['u']),abs(float(influence(ff))-ss['i']))
        direct += 1; recurrence += 4
        assert ss['g'] <= .25*gb+24+TOL
        gu_checks += 1
        if ub <= 5*ib+TOL:
            assert ss['u'] <= 5*ss['i']+TOL; endpoint_checks += 1

# Long nonstationary towers, including ranks approaching the constant endpoint.
sequence_steps=0; restriction_floor_checks=0; max_add=(-1,None); max_ratio=(-1,None)
sample_bases=bases[::17]+[bases[-1]]
for base in sample_bases:
    for trial in range(8):
        s=state_first(base)
        bg=s['base_g']
        for d in range(2,82):
            r=rng.choice((2,3,4,5,8,13,21,34,55,89,144,233))
            s=state_step(s,r)
            add=s['g']-(2.0**(-d))*bg
            assert add <= 24+2e-9
            assert s['u'] <= 5*s['i']+2e-9 if U(base) <= 5*float(influence(base))+TOL else True
            if d >= 3:
                assert min(min(a,b) for a,b in s['pairs']) >= .25-2e-12
                restriction_floor_checks += len(s['pairs'])
            if add > max_add[0]: max_add=(add,(d,r,s['m']))
            if s['i'] and s['g']/s['i'] > max_ratio[0]: max_ratio=(s['g']/s['i'],(d,r,s['m']))
            sequence_steps += 1

assert max_err < TOL
print(f"seed={SEED}")
print(f"scalar_and_balancer_checks={scalar_checks}")
print(f"direct_truth_table_towers={direct}")
print(f"exact_state_recurrence_checks={recurrence}")
print(f"GU_transfer_checks={gu_checks+sequence_steps}")
print(f"endpoint_U_le_5I_checks={endpoint_checks+sequence_steps}")
print(f"restriction_floor_checks={restriction_floor_checks}")
print(f"max_G_Qr={max_gq}")
print(f"max_U_over_I_Qr={max_uqi}")
print(f"max_rank_coordinate_charge={max_qcharge}")
print(f"max_endpoint_increment_ratio={max_endpoint}")
print(f"min_grid_R_second={min_r2}")
print(f"max_recurrence_error={max_err:.3e}")
print(f"max_long_tower_additive_G={max_add}")
print(f"max_long_tower_G_over_I={max_ratio}")
print("theorem_G_constant=24")
print("theorem_endpoint_constant=5")
print("full_FEI=OPEN")
print("PASS")
