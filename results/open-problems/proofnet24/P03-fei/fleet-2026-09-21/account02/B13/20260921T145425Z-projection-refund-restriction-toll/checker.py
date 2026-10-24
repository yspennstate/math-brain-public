#!/usr/bin/env python3
from fractions import Fraction
from math import log2

def wht_masses(vals):
    n=(len(vals)).bit_length()-1
    N=1<<n
    coeff=[]
    for s in range(N):
        sm=0
        for x,v in enumerate(vals):
            sm += v * (-1 if ((s & x).bit_count() & 1) else 1)
        coeff.append(Fraction(sm,N))
    return [c*c for c in coeff]

def upward(p,n):
    u=p[:]
    for bit in range(n):
        for m in range(1<<n):
            if not ((m>>bit)&1):
                u[m]+=u[m|(1<<bit)]
    return u

def marginal_drop(p,n,i):
    q=[Fraction(0) for _ in range(1<<(n-1))]
    for m,pm in enumerate(p):
        lo=m & ((1<<i)-1)
        hi=m>>(i+1)
        r=lo | (hi<<i)
        q[r]+=pm
    return q

def factor_int(x):
    out={}
    d=2
    while d*d<=x:
        while x%d==0:
            out[d]=out.get(d,0)+1
            x//=d
        d+=1
    if x>1:
        out[x]=out.get(x,0)+1
    return out

def add_log_rat(dst,weight,r):
    if not weight or r==1:
        return
    for p,e in factor_int(r.numerator).items():
        dst[p]=dst.get(p,Fraction(0))+weight*e
    for p,e in factor_int(r.denominator).items():
        dst[p]=dst.get(p,Fraction(0))-weight*e

def clean(d):
    return {p:c for p,c in d.items() if c}

def formal_bcan(p,n):
    u=upward(p,n)
    out={}
    for pm,um in zip(p,u):
        if pm:
            add_log_rat(out,pm,um/pm)
    return clean(out)

def lincomb(*terms):
    out={}
    for scalar,d in terms:
        for p,c in d.items():
            out[p]=out.get(p,Fraction(0))+scalar*c
    return clean(out)

def coordinate_rhs_formal(p,n,i):
    # Exact formal-log expansion of
    # sum_A [a log(q/a)+b log(q/b)+b log(w/v)].
    m=n-1
    a=[Fraction(0)]*(1<<m)
    b=[Fraction(0)]*(1<<m)
    for r in range(1<<m):
        lo=r & ((1<<i)-1)
        hi=r>>i
        m0=lo | (hi<<(i+1))
        m1=m0 | (1<<i)
        a[r]=p[m0]
        b[r]=p[m1]
    q=[x+y for x,y in zip(a,b)]
    v=upward(q,m)
    w=upward(b,m)
    out={}
    for A in range(1<<m):
        if a[A]:
            add_log_rat(out,a[A],q[A]/a[A])
        if b[A]:
            add_log_rat(out,b[A],q[A]/b[A])
            add_log_rat(out,b[A],w[A]/v[A])
    return clean(out)

def truth_from_id(fid,n):
    return [1 if ((fid>>x)&1) else -1 for x in range(1<<n)]

def ln_interval_integer(x,M=80):
    # ln x = 2 atanh((x-1)/(x+1)); truncation and tail are rational.
    y=Fraction(x-1,x+1)
    y2=y*y
    yp=y
    s=Fraction(0)
    for k in range(M):
        s += 2*yp/Fraction(2*k+1)
        yp *= y2
    rem = 2*yp/Fraction(2*M+1)/(1-y2)
    return s, s+rem

def linear_ln_interval(coeffs,M=80):
    lo=Fraction(0); hi=Fraction(0)
    for x,c in coeffs.items():
        a,b=ln_interval_integer(x,M)
        if c>=0:
            lo+=c*a; hi+=c*b
        else:
            lo+=c*b; hi+=c*a
    return lo,hi

# 1. Exhaustive formal-log coordinate projection identity through n=4,
# modulo global output sign.
checks=0
for n in range(1,5):
    N=1<<n
    for fid in range(1<<(N-1)):
        p=wht_masses(truth_from_id(fid,n))
        bp=formal_bcan(p,n)
        for i in range(n):
            q=marginal_drop(p,n,i)
            lhs=lincomb((Fraction(1),bp),(Fraction(-1),formal_bcan(q,n-1)))
            rhs=coordinate_rhs_formal(p,n,i)
            assert lhs==rhs, (n,fid,i,lhs,rhs)
            checks+=1

# 2. Genuine-Boolean counterexample to the proposed 3/ln(2)
# physical-restriction toll.  h is the four-bit threshold +1 iff |x|<=2;
# h' differs only at 0000; y selects h or h'.
h=[1 if x.bit_count()<=2 else -1 for x in range(16)]
hp=h[:]
hp[0]*=-1
f=[]
for z in range(32):
    y=z&1
    x=z>>1
    f.append(hp[x] if y else h[x])

ph=wht_masses(h)
php=wht_masses(hp)
pf=wht_masses(f)
Bh=formal_bcan(ph,4)
Bhp=formal_bcan(php,4)
Bf=formal_bcan(pf,5)
toll=lincomb((Fraction(1),Bf),(Fraction(-1,2),Bh),(Fraction(-1,2),Bhp))
expected={
    2:Fraction(279,256),
    3:Fraction(-3,64),
    5:Fraction(-77,64),
    7:Fraction(77,128),
    13:Fraction(25,256),
}
assert toll==expected, toll

Iy=sum(pf[m] for m in range(32) if m&1)
assert Iy==Fraction(1,16), Iy

# toll > (3/ln 2) I_y iff (toll in bits)*ln 2 > 3/16.
# The left side is the displayed linear combination of natural logarithms.
lo,hi=linear_ln_interval(expected,80)
assert lo > Fraction(3,16), (lo,hi)

def eval_formal(d):
    return sum(float(c)*log2(p) for p,c in d.items())

toll_float=eval_formal(toll)
ratio=toll_float/float(Iy)
print("projection_identity_formal_checks",checks)
print("witness_Iy",Iy)
print("witness_Bcan_h",eval_formal(Bh))
print("witness_Bcan_hprime",eval_formal(Bhp))
print("witness_Bcan_f",eval_formal(Bf))
print("witness_restriction_toll",toll_float)
print("witness_toll_over_Iy",ratio)
print("three_over_ln2",3/0.693147180559945309417232121458176568)
print("certified_natural_log_toll_lower",float(lo))
print("target_3_over_16",float(Fraction(3,16)))
print("certified_margin_lower",float(lo-Fraction(3,16)))
print("PASS")
