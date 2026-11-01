import exact as x
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[2];START=time.monotonic();PILOT='--pilot' in sys.argv;C=Q(21,4);N={};POL=0;NODE=0;LEAF=0
def ck(v,k):
    assert v,k
    N[k]=N.get(k,0)+1
    assert time.monotonic()-START<(60 if PILOT else 240),'runtime cap'
def add(*v):return x.add(*v)
def num(q):return {2:Q(q)} if q else {}
def log(q):return add((1,x.factor(q.numerator)),(-1,x.factor(q.denominator)))
def enc(e):return {'prime_log':{str(k):str(v) for k,v in e.items()},'interval':[str(v) for v in x.bounds(e)]}
def pos(e,k,strict=False):ck(x.bounds(e)[0]>0 if strict else x.bounds(e)[0]>=0,k)
def G(a,d):return add((d,x.Hplus(a)),(1,x.R(x.neg(a),d)))
def Gp(a,t):
    p=x.neg(a);V=4*p*(1-p)
    return add((1,x.Hplus(a)),(4*(1-2*t),x.eta(p*p)),(2*(1-2*t)*V,num(1)),(-4*V*t,log(t)),(8*p*(1-2*p*t),log(1-2*p*t)),(-8*p*(1-2*t),log(1-2*t)))
t=Q(1,16)
def T(a,d):return add((1,G(a,t)),(d-t,Gp(a,t)))
def U(a,d):return add((1,G(a,d)),(-1,T(a,d)))
def S(f):return add((1,num(C*x.I(f))),(-1,x.H(f)))
u=(-1,)+(1,)*15;a=tuple(-1 if j.bit_count()>=2 else 1 for j in range(8));F=x.activate(u,a)
v=(-1,)+(1,)*7;acs=[x.restrict(a,((0,b),)) for b in (0,1)];fs=[x.activate(v,b) for b in acs]
for b in (0,1):ck(fs[b]==x.restrict(F,((0,0),(4,b))),'actual prefix selected restriction')
coremargin=add((1,num(C*Q(1,16))),(Q(-1,2),x.H(u)),(Q(1,4),x.H(v)))
old=Q(1,64);pos(add((1,coremargin),(-1,num(old))),'old debit funded ONCE by original core margin',True)
aa=add((1,T(a,Q(1,8))),(Q(-1,2),T(acs[0],Q(1,8))),(Q(-1,2),T(acs[1],Q(1,8))))
controlmargin=add((1,num(C*Q(1,32))),(Q(-1,2),aa));pos(controlmargin,'actual old control tangent margin')
Bs=[add((Q(1,4),S(f)),(Q(1,4),U(ac,Q(1,8)))) for f,ac in zip(fs,acs)]
Bvac=add((Q(1,2),U(a,Q(0))))
for e in [Bvac]+Bs:pos(e,'every retained signed terminal account paid')
pos(add((1,Bs[1]),(-1,num(Q(1,64)))),'selected ORIGINAL account exceeds1/64',True)
ck(S(F)==add((1,coremargin),(1,controlmargin),(1,Bvac),(1,Bs[0]),(1,Bs[1])),'full SAME original signed surplus decomposition')
ck(x.I(F)==Q(11,32),'actual root influence11/32')
ck(x.I(F)==Q(1,16)+Q(1,32)+sum(x.I(f)/4 for f in fs),'full original physical influence partition')

