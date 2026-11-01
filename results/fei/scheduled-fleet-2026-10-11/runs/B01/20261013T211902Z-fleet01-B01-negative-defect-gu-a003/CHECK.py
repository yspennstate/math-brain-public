#!/usr/bin/env python3
"""Finite audit for the sign-flipped point-defect GU' theorem.

The all-rank/depth result is analytic in PROOF.md.  This checker reconstructs
small Boolean towers from truth tables and independently follows the exact
mean-pair recurrence for long nonstationary towers.
"""
from fractions import Fraction
from math import log2, log
import random

SEED = 0xB01A003E
rng = random.Random(SEED)
TOL = 1e-9

def fwht(vals):
    a=[Fraction(v) for v in vals]; h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return [x/len(a) for x in a]

def caps(p):
    c=list(p); n=len(c).bit_length()-1
    for j in range(n):
        bit=1<<j
        for s in range(1<<n):
            if not s&bit: c[s]+=c[s|bit]
    return c

def U(f):
    p=[x*x for x in fwht(f)]; c=caps(p)
    return sum(float(x)*log2(float(y/x)) for x,y in zip(p,c) if x)

def restrict(f,j,b):
    n=len(f).bit_length()-1; out=[]
    for z in range(1<<(n-1)):
        lo=z&((1<<j)-1); hi=z>>j
        out.append(f[lo|(b<<j)|(hi<<(j+1))])
    return out

def mean(f): return Fraction(sum(f),len(f))
def influence(f):
    n=len(f).bit_length()-1
    return sum((Fraction(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f)) for j in range(n)),Fraction(0))
def G(f):
    root=U(f); n=len(f).bit_length()-1
    return sum(root-(U(restrict(f,j,0))+U(restrict(f,j,1)))/2 for j in range(n))
def pairs(f):
    n=len(f).bit_length()-1
    return [(float(mean(restrict(f,j,0))),float(mean(restrict(f,j,1)))) for j in range(n)]
def product(f,g): return [f[x]*g[y] for y in range(len(g)) for x in range(len(f))]
def activate(q): return [q[x>>1] if not(x&1) else 1 for x in range(2*len(q))]
def neg_defect(r):
    q=[-1]*(1<<r); q[-1]=1; return q
def first_truth(base): return activate(product((-1,1),base))
def step_truth(f,r): return activate(product(neg_defect(r),f))

def zlog(x): return 0.0 if x==0 else x*log2(1/x)
def R(t):
    x=(1+t)**2/4; y=(1-t)**2/4
    e=zlog(x)+(0.0 if y==0 else y*log2(2/(1-t)))
    u=0.0 if t==0 else t*t*log2(1/(t*t))
    return e-u/2+(1-t*t)/4
def R2(t):
    return 1+(log(t*t/((1+t)*(1-t)**0.5))+.75)/log(2)

def qstats(r):
    p=2.0**(-r); beta=1-2*p
    uq=zlog(beta*beta)+2*r*p*beta; iq=2*r*p
    if r==2: gq=2.0
    else:
        pp=2.0**(-(r-1)); bp=1-2*pp
        up=zlog(bp*bp)+2*(r-1)*pp*bp if bp else 0.0
        gq=r*(uq-up/2)
    return beta,uq,iq,gq

def state_first(base):
    m=float(mean(base)); bp=pairs(base)
    qp=[(0.0,0.0) for _ in bp]+[(m,-m)]
    return dict(m=.5,g=.5*G(base)+R(0)+sum(R(0)-.5*(R(a)+R(b)) for a,b in qp),
                i=1+.5*float(influence(base)),u=1+.5*U(base),
                pairs=[((1+a)/2,(1+b)/2) for a,b in qp]+[(1.0,0.0)],
                base_g=G(base),base_i=float(influence(base)),base_u=U(base))

def state_step(s,r):
    beta,uq,iq,gq=qstats(r); p=2.0**(-r); t=-beta*s['m']
    qp=[(-beta*a,-beta*b) for a,b in s['pairs']]+[((-(1-4*p)*s['m']),-s['m'])]*r
    g=.5*(s['g']+gq)+R(t)+sum(R(t)-.5*(R(a)+R(b)) for a,b in qp)
    return dict(m=(1+t)/2,g=g,i=.5*(s['i']+iq)+(1-t)/2,
                u=.5*(s['u']+uq)+R(t),
                pairs=[((1+a)/2,(1+b)/2) for a,b in qp]+[(1.0,t)],
                base_g=s['base_g'],base_i=s['base_i'],base_u=s['base_u'])

# Scalar lemmas and reflection inequality.
scalar=0; min_curv=(1e9,None); max_ref=(-1,None); max_endpoint=(-1,None)
for j in range(400001):
    t=-.5+(.5-1/16)*j/400000
    v=R2(t); min_curv=min(min_curv,(v,t))
    assert v>=-6-2e-10; scalar+=1
for j in range(300001):
    t=j/300000
    d=R(-t)-R(t); max_ref=max(max_ref,(d,t))
    assert d<=2e-11; scalar+=1
for r in range(2,257):
    beta,uq,iq,gq=qstats(r)
    assert uq<=2*iq+2e-12 and gq<=2+2e-12
    for j in range(1001):
        m=.25+.25*j/1000; t=beta*m
        den=.5*iq+(1+t)/2
        ratio=(.5*uq+R(-t))/den
        max_endpoint=max(max_endpoint,(ratio,(r,m)))
        assert ratio<=56/27+2e-10; scalar+=3

# Exhaustive small Boolean bases and direct Walsh reconstruction.
bases=[]
for n in range(4):
    for mask in range(1<<(1<<n)):
        bases.append(tuple(1 if (mask>>x)&1 else -1 for x in range(1<<n)))
direct=recurrence=gu_checks=endpoint_checks=0; max_err=0.0
for base in bases:
    f=first_truth(base); s=state_first(base)
    max_err=max(max_err,abs(float(mean(f))-s['m']),abs(G(f)-s['g']),abs(U(f)-s['u']),abs(float(influence(f))-s['i']))
    direct+=1; recurrence+=4
    for r in (2,3):
        ff=step_truth(f,r); ss=state_step(s,r)
        max_err=max(max_err,abs(float(mean(ff))-ss['m']),abs(G(ff)-ss['g']),abs(U(ff)-ss['u']),abs(float(influence(ff))-ss['i']))
        assert ss['g']<=.25*G(base)+34+TOL; gu_checks+=1
        if U(base)<=56/27*float(influence(base))+TOL:
            assert ss['u']<=56/27*ss['i']+TOL; endpoint_checks+=1
        direct+=1; recurrence+=4

# Long arbitrary-rank towers and pair-floor classification.
steps=pair_checks=0; max_add=(-1,None); max_ratio=(-1,None)
sample=bases[::17]+[bases[-1]]
for base in sample:
    for trial in range(10):
        s=state_first(base)
        for depth in range(2,92):
            r=rng.choice((2,3,4,5,8,13,21,34,55,89,144,233))
            s=state_step(s,r); steps+=1
            add=s['g']-2.0**(-depth)*s['base_g']
            assert add<=34+2e-9; gu_checks+=1
            if s['base_u']<=56/27*s['base_i']+TOL:
                assert s['u']<=56/27*s['i']+2e-9; endpoint_checks+=1
            # At most three coordinate pairs lie outside the safe interval.
            bad=sum(not(1/8-2e-12<=min(a,b) and max(a,b)<=.5+2e-12) for a,b in s['pairs'])
            assert bad<=3; pair_checks+=len(s['pairs'])
            max_add=max(max_add,(add,(depth,r,s['m'],bad)))
            max_ratio=max(max_ratio,(s['g']/s['i'],(depth,r,s['m'],bad)))

assert max_err<TOL
print(f"seed={SEED}")
print(f"scalar_checks={scalar}")
print(f"direct_truth_table_towers={direct}")
print(f"exact_recurrence_checks={recurrence}")
print(f"GU_transfer_checks={gu_checks}")
print(f"endpoint_checks={endpoint_checks}")
print(f"pair_classification_checks={pair_checks}")
print(f"min_R_second_negative_safe={min_curv}")
print(f"max_R_negative_minus_positive={max_ref}")
print(f"max_endpoint_increment_ratio={max_endpoint}")
print(f"max_recurrence_error={max_err:.3e}")
print(f"max_long_tower_additive_G={max_add}")
print(f"max_long_tower_G_over_I={max_ratio}")
print("theorem_G_constant=34")
print("theorem_endpoint_constant=56/27")
print("full_FEI=OPEN")
print("PASS")
