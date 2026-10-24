#!/usr/bin/env python3
"""Directed-rounding certificate for the last two-bit half-tax corners.

Certifies -d_p >= 0.9 on p in [0.49,0.5], q in [0,0.01].
Together with the analytic p=1/2 edge and q<->1-q comparison in the
proof note, this covers both endpoint collars.  No binary float enters a
sign decision.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from hashlib import sha256

PREC=90
DOWN=Context(prec=PREC,rounding=ROUND_FLOOR)
UP=Context(prec=PREC,rounding=ROUND_CEILING)
Z,O,TWO,FOUR=D(0),D(1),D(2),D(4)

def dn(f):
    with localcontext(DOWN): return +f()
def up(f):
    with localcontext(UP): return +f()
def add(x,y): return dn(lambda:x[0]+y[0]),up(lambda:x[1]+y[1])
def neg(x): return -x[1],-x[0]
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    lo=[dn(lambda a=a,b=b:a*b) for a in x for b in y]
    hi=[up(lambda a=a,b=b:a*b) for a in x for b in y]
    return min(lo),max(hi)
def div(x,y):
    assert y[0]>0
    lo=[dn(lambda a=a,b=b:a/b) for a in x for b in y]
    hi=[up(lambda a=a,b=b:a/b) for a in x for b in y]
    return min(lo),max(hi)
def logp(x):
    assert x>0
    return dn(lambda:x.ln()),up(lambda:x.ln())
def logiv(x): return logp(x[0])[0],logp(x[1])[1]

def xlogx_point(x):
    if x==Z:return Z,Z
    l=logp(x)
    return dn(lambda:x*l[0]),up(lambda:x*l[1])
def xlogx_iv(x):
    # All uses lie in [0,0.04] subset [0,1/e], where x log x decreases.
    return xlogx_point(x[1])[0],xlogx_point(x[0])[1]

def h_point(x):
    if x==Z or x==O:return Z,Z
    lx=logp(x)
    om=(dn(lambda:O-x),up(lambda:O-x)); lom=logiv(om)
    z=add(mul((x,x),lx),mul(om,lom))
    return -z[1],-z[0]
def h_iv(x):
    # All uses lie in [0,1/2], where binary entropy is increasing.
    return h_point(x[0])[0],h_point(x[1])[1]

def dp_interval(pa,pb,qa,qb):
    p=(pa,pb); q=(qa,qb)
    om=(dn(lambda:O-pb),up(lambda:O-pa))
    one_minus_2p=(dn(lambda:O-TWO*pb),up(lambda:O-TWO*pa))
    pp=mul(p,om)
    s=(dn(lambda:FOUR*qa*(O-qa)),up(lambda:FOUR*qb*(O-qb)))
    c=(dn(lambda:FOUR*qa*qa),up(lambda:FOUR*qb*qb))
    sp=mul(s,p)
    b=(dn(lambda:O-sp[1]),up(lambda:O-sp[0]))
    a=div(mul(c,pp),b)
    R=add(mul(one_minus_2p,b),mul(s,pp))
    m=sub(b,mul(c,pp))

    # b*h'(a)*a' in a form continuous at q=0:
    # (cR/b)(ln m-ln p-ln(1-p))-(R/b)c ln c.
    smooth_log=sub(sub(logiv(m),logiv(p)),logiv(om))
    T=mul(div(mul(c,R),b),smooth_log)
    T=sub(T,mul(div(R,b),xlogx_iv(c)))

    ans=neg(mul(s,h_iv(a)))
    ans=add(ans,T)
    ans=add(ans,mul(s,h_iv(p)))
    ans=add(ans,mul(mul(s,p),sub(logiv(om),logiv(p))))
    # -s*h'(sp)=-s ln(1-sp)+s ln s+s ln p.
    ans=sub(ans,mul(s,logiv(b)))
    ans=add(ans,xlogx_iv(s))
    ans=add(ans,mul(s,logiv(p)))
    ans=add(ans,h_iv(s))
    ans=add(ans,mul((D('0.5'),D('0.5')),sub(logiv(om),logiv(p))))
    ans=sub(ans,div((D('0.5'),D('0.5')),om))
    return ans

def certify():
    target=D('-0.9')
    stack=[(D('0.49'),D('0.5'),Z,D('0.01'),0)]
    visited=leaves=maxdepth=0; max_upper=None; digest=sha256()
    while stack:
        pa,pb,qa,qb,depth=stack.pop(); visited+=1
        lo,hi=dp_interval(pa,pb,qa,qb)
        if hi<=target:
            leaves+=1; maxdepth=max(maxdepth,depth)
            max_upper=hi if max_upper is None else max(max_upper,hi)
            digest.update(f'{pa}|{pb}|{qa}|{qb}|{hi}\n'.encode())
            continue
        if depth>=60:
            raise AssertionError(('unresolved',pa,pb,qa,qb,lo,hi))
        pw=(pb-pa)/D('0.01'); qw=(qb-qa)/D('0.01')
        if pw>=qw:
            mid=(pa+pb)/TWO
            stack.extend([(pa,mid,qa,qb,depth+1),(mid,pb,qa,qb,depth+1)])
        else:
            mid=(qa+qb)/TWO
            stack.extend([(pa,pb,qa,mid,depth+1),(pa,pb,mid,qb,depth+1)])
    print('B17/A084 equality-corner derivative certificate: PASS')
    print('domain: p in [0.49,0.5], q in [0,0.01]')
    print('certified: partial_p d <= -0.9')
    print('precision:',PREC,'decimal digits with directed rounding')
    print('visited_boxes=',visited,sep='')
    print('accepted_leaves=',leaves,sep='')
    print('maximum_depth=',maxdepth,sep='')
    print('largest_certified_upper_endpoint=',max_upper,sep='')
    print('leaf_certificate_sha256=',digest.hexdigest(),sep='')
    print('unresolved_boxes=0')
    print('floating_point_used_for_sign_decisions=no')

if __name__=='__main__':certify()
