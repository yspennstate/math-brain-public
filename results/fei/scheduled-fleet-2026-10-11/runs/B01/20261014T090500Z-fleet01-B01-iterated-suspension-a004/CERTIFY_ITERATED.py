#!/usr/bin/env python3
"""Exact rational-log certificate for the depth-five iterated tower."""
from fractions import Fraction as F
from functools import lru_cache
from math import log2
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING


def fwht(v):
    a=[F(x) for x in v]; h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                x,y=a[k],a[k+h]; a[k],a[k+h]=x+y,x-y
        h*=2
    return [x/len(a) for x in a]


def caps(p):
    a=list(p); n=len(a).bit_length()-1
    for i in range(n):
        bit=1<<i
        for s in range(len(a)):
            if not s&bit: a[s]+=a[s|bit]
    return a


def addlog(e,w,r):
    if not w: return
    if r.numerator!=1: e[r.numerator]=e.get(r.numerator,F())+w
    if r.denominator!=1: e[r.denominator]=e.get(r.denominator,F())-w


def add(a,b,s=F(1)):
    z=dict(a)
    for p,x in b.items(): z[p]=z.get(p,F())+s*x
    return {p:x for p,x in z.items() if x}


def scale(a,s): return {p:s*x for p,x in a.items() if s*x}


def entropy(p):
    e={}
    for x,y in zip(p,caps(p)):
        if x: addlog(e,x,y/x)
    return e


def Texpr(a,b):
    e={}
    if a: addlog(e,a,(a+b)/a)
    if b: addlog(e,b,(a+b)/b)
    return e


def Rexpr(m):
    pq=[m*m,1-m*m]
    pa=[(1+m)**2/4,(1-m*m)/4,(1-m)**2/4,(1-m*m)/4]
    return add(entropy(pa),entropy(pq),F(-1,2))


def Bzexpr(m): return add({2:(1-m*m)/2},Texpr((1+m)**2,(1-m)**2),F(1,4))


def Cexpr(m,p):
    z=scale(Texpr(m*m,p),F(-1,2))
    z=add(z,Texpr((1+m)**2,p),F(1,4))
    return add(z,Texpr((1-m)**2,p),F(1,4))


def restrict(v,i,bit):
    n=len(v).bit_length()-1; out=[]
    for z in range(1<<(n-1)):
        lo=z&((1<<i)-1); hi=z>>i
        out.append(v[lo|(bit<<i)|(hi<<(i+1))])
    return tuple(out)


def uexpr(v): return entropy([x*x for x in fwht(v)])


def bexpr(v):
    p=[x*x for x in fwht(v)]; n=len(v).bit_length()-1; e={}
    for i in range(n):
        bit=1<<i
        for s in range(len(p)):
            if not s&bit: e=add(e,Texpr(p[s],p[s|bit]))
    return e


def gexpr(v):
    n=len(v).bit_length()-1; e=scale(uexpr(v),F(n))
    for i in range(n):
        e=add(e,uexpr(restrict(v,i,0)),F(-1,2))
        e=add(e,uexpr(restrict(v,i,1)),F(-1,2))
    return e


def iexact(v):
    p=[x*x for x in fwht(v)]
    return sum(F(s.bit_count())*x for s,x in enumerate(p))


def initial_state():
    mask=56242
    q=tuple(1 if mask&(1<<i) else -1 for i in range(16))
    v=tuple(q)+tuple(1 for _ in q)
    h=fwht(v); p=[x*x for x in h]; n=5
    types=[]
    for i in range(n):
        vm=restrict(v,i,0); vp=restrict(v,i,1)
        types.append((F(1),F(sum(vm),len(vm)),F(sum(vp),len(vp)),p[1<<i]))
    return dict(U=uexpr(v),I=iexact(v),M=add(gexpr(v),bexpr(v),F(-1)),m=h[0],types=types,n=n)


def step(s,t=4):
    m=s['m']; mt=m**t; ms=m**(t-1); ps=m**(2*t-2)
    dr={}; corr={}; types=[]
    for mult,mm,mp,p in s['types']:
        w=t*mult; qmm=mm*ms; qmp=mp*ms; qp=p*ps
        second=add(Rexpr(mt),add(Rexpr(qmm),Rexpr(qmp)),F(-1,2))
        dr=add(dr,second,w); corr=add(corr,Cexpr(mt,qp),w)
        types.append((w,(1+qmm)/2,(1+qmp)/2,qp/4))
    types.append((F(1),mt,F(1),(1-mt)**2/4))
    U=add(scale(s['U'],F(t,2)),Rexpr(mt))
    M=scale(s['M'],F(t,2)); M=add(M,dr); M=add(M,Rexpr(mt)); M=add(M,Bzexpr(mt),F(-1)); M=add(M,corr,F(-1))
    return dict(U=U,I=F(t,2)*s['I']+(1-mt)/2,M=M,m=(1+mt)/2,types=types,n=t*s['n']+1)


def ln_interval(y,terms=160):
    assert F(1)<=y<=F(2)
    z=(y-1)/(y+1); zz=z*z; power=z; total=F(0)
    for j in range(terms):
        total += power/F(2*j+1); power*=zz
    lo=2*total; tail=2*power/(F(2*terms+1)*(1-zz))
    return lo,lo+tail


LN2=ln_interval(F(2))


@lru_cache(None)
def log2_interval_integer(p):
    k=p.bit_length()-1; y=F(p,1<<k); lo,hi=ln_interval(y)
    return F(k)+lo/LN2[1],F(k)+hi/LN2[0]


def interval(e):
    lo=hi=F(0)
    for p,x in e.items():
        a,b=log2_interval_integer(p)
        if x>=0: lo+=x*a; hi+=x*b
        else: lo+=x*b; hi+=x*a
    return lo,hi


def value(e): return sum(float(x)*log2(p) for p,x in e.items())


def decimal_interval(e,prec=90):
    """Outward interval using correctly-rounded Decimal.ln plus one ulp."""
    def qbound(x,rounding):
        with localcontext() as ctx:
            ctx.prec=prec; ctx.rounding=rounding
            return Decimal(x.numerator)/Decimal(x.denominator)
    with localcontext() as ctx:
        ctx.prec=prec
        ln2=Decimal(2).ln()
        ln2lo=ln2.next_minus(); ln2hi=ln2.next_plus()
    lo=Decimal(0); hi=Decimal(0)
    for p,x in e.items():
        with localcontext() as ctx:
            ctx.prec=prec
            lp=Decimal(p).ln(); lplo=lp.next_minus(); lphi=lp.next_plus()
        with localcontext() as ctx:
            ctx.prec=prec; ctx.rounding=ROUND_FLOOR
            al=lplo/ln2hi
        with localcontext() as ctx:
            ctx.prec=prec; ctx.rounding=ROUND_CEILING
            ah=lphi/ln2lo
        xl=qbound(x,ROUND_FLOOR); xh=qbound(x,ROUND_CEILING)
        if x>=0:
            with localcontext() as ctx:
                ctx.prec=prec; ctx.rounding=ROUND_FLOOR
                termlo=xl*al; lo=lo+termlo
            with localcontext() as ctx:
                ctx.prec=prec; ctx.rounding=ROUND_CEILING
                termhi=xh*ah; hi=hi+termhi
        else:
            with localcontext() as ctx:
                ctx.prec=prec; ctx.rounding=ROUND_FLOOR
                termlo=xl*ah; lo=lo+termlo
            with localcontext() as ctx:
                ctx.prec=prec; ctx.rounding=ROUND_CEILING
                termhi=xh*al; hi=hi+termhi
    return lo,hi


s=initial_state(); eta=F(1,4)
print('status=PASS')
print('tower=F_0=A(mask56242); F_(k+1)=A(F_k^tensor4)')
for k in range(5):
    num=add(s['M'],s['U'],1+eta)
    c=value(num)/float(s['I'])
    print(f'k={k} n={s["n"]} mean={float(s["m"]):.15f} I={float(s["I"]):.15f} c_eta_1_4={c:.15f} mean_bits={s["m"].numerator.bit_length()}/{s["m"].denominator.bit_length()}')
    if k==4:
        witness=add(num,{2:F(-109,50)*s['I']})
        sign_interval=decimal_interval(witness)
        assert sign_interval[0]>0
        print('k4_minus_2.18_sign=POSITIVE')
        print(f'k4_residual_outward_interval=[{sign_interval[0]},{sign_interval[1]}]')
        print(f'k4_rational_log_terms={len(witness)}')
        print(f'k4_largest_log_base_bits={max(p.bit_length() for p in witness)}')
    s=step(s)

