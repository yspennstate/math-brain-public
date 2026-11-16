"""Exact degree-two Taylor coefficients in Q(sqrt(5)) or Q(sqrt(15))."""
import sys
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb
from functools import lru_cache
from collar_boxes import point_bank

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from exact_bernstein import data
from quadratic_field import add,mul,power,ZERO,ONE,sign

ALPHAS=[m for m in product(range(3),repeat=6)if sum(m)<=2]
Z=(0,)*6

def minus(x):return -x[0],-x[1]
def divide(x,y,d):
    a,b=y;norm=a*a-d*b*b
    assert norm
    return mul(x,(a/norm,-b/norm),d)

def jet(poly,point,d):
    out={}
    powers=[[power(x,k,d)for k in range(9)]for x in point]
    for alpha in ALPHAS:
        value=ZERO
        for mon,c in poly.items():
            if any(a>m for a,m in zip(alpha,mon)):continue
            w=(F(c),F(0))
            for i,(a,m) in enumerate(zip(alpha,mon)):
                if a:w=(w[0]*comb(m,a),w[1]*comb(m,a))
                if m>a:w=mul(w,powers[i][m-a],d)
            value=add(value,w)
        if value!=ZERO:out[alpha]=value
    return out

def jmul(a,b,d):
    out={}
    for m,c in a.items():
        for n,e in b.items():
            key=tuple(i+j for i,j in zip(m,n))
            if sum(key)<=2:out[key]=add(out.get(key,ZERO),mul(c,e,d))
    return {m:c for m,c in out.items()if c!=ZERO}

def jdiv(a,b,d):
    b0=b[Z];out={}
    for mon in sorted(ALPHAS,key=lambda a:(sum(a),a)):
        value=a.get(mon,ZERO)
        for n,c in b.items():
            if n==Z or any(i>j for i,j in zip(n,mon)):continue
            k=tuple(i-j for i,j in zip(mon,n))
            value=add(value,minus(mul(c,out.get(k,ZERO),d)))
        value=divide(value,b0,d)
        if value!=ZERO:out[mon]=value
    assert jmul(out,b,d)==a
    return out

def encode(j):return [[list(m),[str(c[0]),str(c[1])]]for m,c in sorted(j.items())]

@lru_cache(None)
def expansions():
    target,gs=data();out=[]
    # D and tau are recovered directly from the defining zero-face ring.
    from zero_face import construct
    rr,t,V,R,M,delta,Q,tau,D,edges,Pi,num=construct()
    dic=lambda p:{m[:6]:int(c)for m,c in p.items()}
    for node,info in sorted(point_bank().items()):
        d=info['radicand'];point=[tuple(map(F,x))for x in info['point']]
        tj=jet(target,point,d);dj=jet(dic(D),point,d);delta_j=jet(dic(delta),point,d)
        den=jmul(jmul(dj,dj,d),delta_j,d)
        den={m:(F(9,16)*c[0],F(9,16)*c[1])for m,c in den.items()}
        T=jdiv(tj,den,d)
        assert T.get(Z,ZERO)==ZERO
        active={};inactive={}
        for name,g in gs.items():
            if name in ('scale_guard','scale14'):continue
            gj=jet(g,point,d)
            constant=gj.get(Z,ZERO)
            assert sign(constant,d)>=0
            if constant==ZERO:active[name]=encode(gj)
            else:inactive[name]=list(map(str,constant))
        # connected is quadratic at a double zero eigenvalue.
        assert all(sum(m)>=2 for m,c in jet(gs['connected'],point,d).items())
        out.append(dict(node=node,**info,T5_jet=encode(T),target_jet=encode(tj),
                        active_constraint_jets=active,inactive_constraint_values=inactive))
    return out
