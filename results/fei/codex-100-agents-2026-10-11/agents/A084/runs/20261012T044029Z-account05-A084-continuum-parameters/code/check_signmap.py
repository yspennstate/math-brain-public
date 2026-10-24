"""Exact log/sqrt certificates plus separate numerical geometric reconstruction.

Numerical angles do not enter certified sign or threshold decisions.
"""
from fractions import Fraction as R
from functools import lru_cache
from math import isqrt
from pathlib import Path
import math,json,time
ROOT=Path(__file__).resolve().parents[1]
N=24; BITS=80; SCALE=1<<BITS
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    vals=[x*y for x in a for y in b];return min(vals),max(vals)
def down(x):return R(x.numerator*SCALE//x.denominator,SCALE)
def up(x):return -down(-x)
def series(x):
    z=(x-1)/(x+1);z2=z*z;term=z;s=R(0)
    for j in range(N):s+=term/(2*j+1);term*=z2
    err=2*abs(term)/((2*N+1)*(1-z2))
    return 2*s-err,2*s+err
L2=series(R(2))
@lru_cache(maxsize=20000)
def log2(x):
    assert x>0;k=0
    while x<1:x*=2;k-=1
    while x>2:x/=2;k+=1
    ln=series(x);vals=[a/b+k for a in ln for b in L2]
    return down(min(vals)),up(max(vals))
@lru_cache(maxsize=20000)
def phi(x):
    if not x or x==1:return R(0),R(0)
    return mul((-x,-x),log2(x))
def h(x):return add(phi(x),phi(1-x))
def hi(a):
    b=h(a[0]);c=h(a[1]);return min(b[0],c[0]),R(1) if a[0]<=R(1,2)<=a[1] else max(b[1],c[1])
def sqrt_bounds(x):
    z=x.numerator*SCALE*SCALE//x.denominator;k=isqrt(z)
    lo=R(k,SCALE)
    exact=k*k*x.denominator==x.numerator*SCALE*SCALE
    return lo,lo if exact else R(k+1,SCALE)
def K(p):
    c=sqrt_bounds(1-p);v=((1-c[1])/2,(1-c[0])/2)
    return sub(mul((R(2),R(2)),hi(v)),h(p))
def F(p,q):
    r=4*q*(1-q);t=p*r
    mass=((1-2*p*q)**2,4*p*(1-p)*q*q,p*p*r,p*(1-p)*r)
    assert sum(mass)==1
    H=(R(0),R(0))
    for x in mass:H=add(H,phi(x))
    return sub(sub(mul((R(2),R(2)),h(t)),mul((p,p),h(r))),H)
def conditional_F(p,q):
    r=4*q*(1-q);w=1-p*r
    u=p*(1-2*q)**2/w;v=4*p*(1-p)*q*q/w
    assert 0<=u<=1 and 0<=v<=1
    return mul((w,w),sub(sub(h(p),h(u)),h(v)))
def sign(a):return 1 if a[0]>0 else -1 if a[1]<0 else 0
def dump(name,obj):
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2),encoding='utf-8')
def hn(x):
    if x<=0 or x>=1:return 0.
    return -x*math.log2(x)-(1-x)*math.log2(1-x)
def psi(x):return hn(math.sin(x)**2)
def gn(s,x):return psi(x)+psi(s-x)-psi(s)
def root_a(s):
    # Only called with K(s)>0. Initial negative sign is analytic; fixed tiny
    # endpoint is used only for a numerical reconstruction away from bifurcation.
    lo=s*1e-8;hi=s/2
    assert gn(s,lo)<0 and gn(s,hi)>0
    for _ in range(55):
        mid=(lo+hi)/2
        if gn(s,mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2
def geometric_sign(p,q):
    theta=math.asin(math.sqrt(p));alpha=math.atan(math.sqrt(p/(1-p))*(1-2*q))
    if q==.5:return 0
    if q<.5:
        if p>=.5:return -1
        s=theta;x=alpha
    elif p<=.5:return -1
    else:
        q0=1/(2*p)
        if q>q0:return -1
        if q==q0:return 0
        s=math.pi/2-theta;x=-alpha
    if 2*psi(s/2)-psi(s)<0:return 1
    a=root_a(s)
    return -1 if a<x<s-a else 1
def main():
    start=time.perf_counter()
    lo=R(1,4);high=R(49,100);assert sign(K(lo))==-1 and sign(K(high))==1
    records=[]
    while high-lo>R(1,10**8):
        mid=(lo+high)/2;iv=K(mid);s=sign(iv)
        assert s!=0,('precision insufficient',str(mid),iv)
        records.append({'p':str(mid),'K_interval':[str(x) for x in iv],'sign':s})
        if s>0:high=mid
        else:lo=mid
    cert={'threshold_definition':'K(p)=2h((1-sqrt(1-p))/2)-h(p)=0; analytic proof establishes unique interior root p in (0,1/2)','bracket':[str(lo),str(high)],'decimal_display_only':[float(lo),float(high)],'endpoint_K_intervals':[[str(x) for x in K(lo)],[str(x) for x in K(high)]],'records':records,'arithmetic':'Fraction, 24-term atanh logarithm; outward 80-bit rational sqrt using isqrt; entropy concavity'}
    dump('THRESHOLD_CERTIFICATE.json',cert)
    print('threshold bracket:',float(lo),float(high),flush=True)
    checks=0;rows=[];zeros=0
    for i in range(1,32):
        for j in range(1,32):
            p=R(i,32);q=R(j,32);iv=F(p,q);cv=conditional_F(p,q)
            assert max(iv[0],cv[0])<=min(iv[1],cv[1]);checks+=1
            exactsign=sign(iv);pred=geometric_sign(float(p),float(q))
            if q==R(1,2):
                assert iv[0]<=0<=iv[1] and pred==0;zeros+=1
            else:assert exactsign!=0 and exactsign==pred,(p,q,iv,pred)
            checks+=1
            theta=math.asin(math.sqrt(float(p)));alpha=math.atan(math.sqrt(float(p/(1-p)))*float(1-2*q));w=float(1-4*p*q*(1-q))
            geo=w*(psi(theta)-psi(alpha)-psi(theta-alpha))
            assert abs(geo-float((iv[0]+iv[1])/2))<1e-12;checks+=1
            rows.append({'p':str(p),'q':str(q),'F_interval':[str(x) for x in iv],'certified_sign':exactsign,'geometry_prediction_evidence':pred})
    dump('GRID_CHECKS.json',{'domain':'p,q=j/32, 1<=j<=31','rows':rows,'checks':checks,'exact_zero_line_points':zeros,'role':'Exact point signs and ledger cross-check; universal proof is PROOF.md, not this grid.'})
    zero_fixtures=[]
    for p in [R(2,3),R(3,4),R(4,5),R(5,8),R(9,10),R(7,8)]:
        q=1/(2*p);r=4*q*(1-q);w=1-p*r
        assert (1-2*p*q)==0
        assert p*(1-2*q)**2/w==1-p and 4*p*(1-p)*q*q/w==1
        iv=F(p,q);assert iv[0]<=0<=iv[1];checks+=3
        zero_fixtures.append({'p':str(p),'q':str(q),'F_interval':[str(x) for x in iv],'identity':'u=1-p,v=1, F=w[h(p)-h(1-p)-h(1)]=0'})
    dump('HYPERBOLA_ZERO_FIXTURES.json',zero_fixtures)
    # Proof-backed counts; numerical a(s) values are descriptive and separately
    # checked against rigorous signs just outside each displayed root.
    root_examples=[]
    for p in [R(7,16),R(15,32),R(17,32),R(9,16),R(3,4)]:
        theta=math.asin(math.sqrt(float(p)));lowhalf=p<R(1,2)
        s=theta if lowhalf else math.pi/2-theta
        roots=[.5]
        if not lowhalf:roots.append(float(1/(2*p)))
        if 2*psi(s/2)>psi(s):
            a=root_a(s)
            if lowhalf:roots.extend([(1-math.tan(s-a)/math.tan(theta))/2,(1-math.tan(a)/math.tan(theta))/2])
            else:roots.extend([(1+math.tan(a)/math.tan(theta))/2,(1+math.tan(s-a)/math.tan(theta))/2])
        root_examples.append({'p':str(p),'interior_q_zeros_display_only':sorted(roots),'count_proved_by_analytic_classification':len(roots)})
    dump('ZERO_COUNT_EXAMPLES.json',root_examples)
    result={'checks_passed':checks,'dyadic_points':961,'zero_hyperbola_fixtures':6,'threshold_bisections':len(records),'runtime_seconds':time.perf_counter()-start,'analytic_target':'FULL_INTERIOR_SIGN_MAP_PROVED_AUTHOR_LEVEL','review':'pending; numerical geometry checks are evidence only','memory_estimate_mb':80}
    dump('RESULT.json',result);print(json.dumps(result),flush=True)
if __name__=='__main__':main()
