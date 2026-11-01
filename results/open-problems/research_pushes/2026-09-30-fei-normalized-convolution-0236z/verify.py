#!/usr/bin/env python3
"""Exact polynomial checks; rational logarithm certificates; tagged exploration.

No FEI theorem is asserted. Python standard library only.
"""
from fractions import Fraction as F
from math import comb, log2
from functools import lru_cache
import json, hashlib, pathlib

def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
        h*=2
    return a

@lru_cache(None)
def ln_interval(x):
    assert x>0
    if x<1:
        lo,hi=ln_interval(1/x);return -hi,-lo
    power=x.numerator.bit_length()-x.denominator.bit_length()
    scale=F(2)**power
    if x<scale:power-=1;scale/=2
    y=x/scale
    assert 1<=y<2
    z=(y-1)/(y+1);z2=z*z;term=z;total=F(0)
    for j in range(48):
        total+=2*term/F(2*j+1);term*=z2
    err=2*term/(97*(1-z2))
    if power:
        l2,h2=ln_interval(F(2)) if x!=2 else (None,None)
        if x==2:
            # Special base: use the series directly at y=2, z=1/3.
            z=F(1,3);term=z;total=F(0)
            for j in range(48):total+=2*term/F(2*j+1);term/=9
            return total,total+2*term/(97*(1-F(1,9)))
        return total+power*l2,total+err+power*h2
    return total,total+err

def lg_interval(x):
    lo,hi=ln_interval(F(x));l2,h2=ln_interval(F(2))
    if lo>=0:return lo/h2,hi/l2
    return lo/l2,hi/h2

def entropy_interval(entries):
    lo=hi=F(0)
    for weight,count in entries:
        if not weight:continue
        a,b=lg_interval(1/weight);lo+=count*weight*a;hi+=count*weight*b
    return lo,hi

def encl(x):
    """Return endpoints outward as both binary floats and serialized decimal text."""
    from math import nextafter, inf
    lo=float(x[0]);hi=float(x[1])
    while F.from_float(lo)>x[0] or F(str(lo))>x[0]:lo=nextafter(lo,-inf)
    while F.from_float(hi)<x[1] or F(str(hi))<x[1]:hi=nextafter(hi,inf)
    assert F.from_float(lo)<=x[0]<=x[1]<=F.from_float(hi)
    assert F(str(lo))<=x[0]<=x[1]<=F(str(hi))
    return [lo,hi]

def test_enclosures():
    for x in (F(1,10),F(1,3),F(-1,3),F(0),F(1,2),F(7,11),F.from_float(0.1),F.from_float(-0.1)):
        lo,hi=encl((x,x))
        assert F.from_float(lo)<=x<=F.from_float(hi)
        assert F(str(lo))<=x<=F(str(hi))
    # A binary endpoint can be outward while its JSON decimal spelling is not.
    for v in (0.1630852002095617,0.1,-0.3333333333333333):
        x=(F.from_float(v)+F(str(v)))/2
        lo,hi=encl((x,x))
        assert F.from_float(lo)<=x<=F.from_float(hi)
        assert F(str(lo))<=x<=F(str(hi))


def onepoint_shell(m,t):
    return [(t**r*(1-t)**r*(2**r-4*(1-t)**(m-r))**2,comb(m,r)) for r in range(1,m+1)]

def complete_pair_shell(m,p):
    d=(1-p)**2+p*p;out=[]
    for s in range(m+1):
        for t in range(m-s+1):
            if s+t==0:continue
            k=s+2*t
            bracket=F(2)**k-4*(1-p)**(2*m-2*t) if s==0 else F(2)**k-4*F(2)**t*d**(m-s-t)+4*(1-p)**(2*m-s-2*t)
            q=(p*(1-p))**k*bracket**2
            out.append((q,comb(m,s)*comb(m-s,t)*2**s))
    return out

def correlation_square(signs,p,u):
    # Factor (sqrt(p(1-p)))^|u| before exact summation.
    n=(len(signs)-1).bit_length();outside=((1<<n)-1)^u;r=F(0)
    for s in range(1<<n):
        a=(s&outside).bit_count();b=outside.bit_count()-a
        r+=signs[s]*signs[s^u]*p**a*(1-p)**b
    return (p*(1-p))**u.bit_count()*r*r

def pair_signs(m):
    return [(-1 if s and all(((s>>(2*j))&3) in (0,3) for j in range(m)) else 1) for s in range(1<<(2*m))]

def numerical_metrics(m):
    p=F(1,2**(m-1));d=(1-p)**2+p*p;beta=p*p/d
    h=lambda x:-float(x)*(log2(x.numerator)-log2(x.denominator)) if x else 0.
    H=h((1-p)**2)+(2**m-1)*h(p*p)
    I=float(2*m*p)
    Kfull=2*m*(h(p)+h(1-p))-H
    Kshape=Kfull+m*log2(float(d))
    def tariff(shell):
        Z=F(1)+sum((q*c for q,c in shell),F(0))
        L=sum(c*h(q) for q,c in shell)
        return L/float(Z),float(Z)
    cond,zc=tariff(onepoint_shell(m,beta));uncond,zu=tariff(complete_pair_shell(m,p))
    return {'m':m,'p':str(p),'I':I,'H_over_I':H/I,'Kshape_over_I':Kshape/I,'support_KL_over_I':(Kfull-Kshape)/I,'conditioned_T_over_I':cond/I,'completed_T_quarter_minus_Kshape_over_I':(uncond/4-Kshape)/I,'Z_conditioned':zc,'Z_completed':zu}

def main():
    test_enclosures()
    out={'status':'PASS','full_FEI':'OPEN','proof_scope':'Analytic theorems in REPORT.md; exact finite self-checks here, not an independent audit or formalization.'}
    # Actual Booleanity and Walsh pattern for the base and paired lift.
    actual=[]
    for m in range(2,7):
        N=1<<m;w=fwht([-1]+[1]*(N-1))
        assert w==[N-2]+[-2]*(N-1)
        n=2*m;vals=[]
        for x in range(1<<n):
            z=sum(((((x>>(2*j))^(x>>(2*j+1)))&1)<<j) for j in range(m))
            vals.append(-1 if z==0 else 1)
        W=fwht(vals)
        for s,v in enumerate(W):
            paired=all(((s>>(2*j))&3) in (0,3) for j in range(m))
            expected=(1<<n)-2*(1<<m) if s==0 else (-2*(1<<m) if paired else 0)
            assert v==expected
        actual.append({'m':m,'truth_table_size':1<<n,'signed_Walsh_coefficients_checked':len(W)})
    out['actual_boolean_checks']=actual
    surgery=[]
    for n in range(2,5):
        N=1<<n;count=0
        for truth in range(1<<N):
            vals=[-1 if truth>>x&1 else 1 for x in range(N)]
            W=fwht(vals)
            if all(W):continue
            assert truth.bit_count()%2==0
            assert all(w%4==0 for w in W)
            flipped=vals.copy();flipped[0]*=-1;Wp=fwht(flipped)
            assert all(Wp)
            for w,wp in zip(W,Wp):
                assert wp==w-2*vals[0]
                assert (w*wp>0) if w else (wp==-2*vals[0])
            count+=1
        surgery.append({'n':n,'zero_supported_sources_checked':count,'flip_point':0})
    out['exhaustive_surgery_checks']=surgery
    # Exact direct correlations compared with the analytic shell formulas.
    exact=[]
    for m in range(2,7):
        p=F(1,2**(m-1));d=(1-p)**2+p*p;beta=p*p/d
        signs=[1]+[-1]*((1<<m)-1)
        shell=onepoint_shell(m,beta)
        for u in range(1,1<<m):assert correlation_square(signs,beta,u)==shell[u.bit_count()-1][0]
        exact.append({'kind':'support_conditioned','m':m,'shifts':(1<<m)-1})
    for m in range(2,5):
        p=F(1,2**(m-1));d=(1-p)**2+p*p;sgn=pair_signs(m)
        for u in range(1,1<<(2*m)):
            s=sum(((u>>(2*j))&3) in (1,2) for j in range(m));t=sum(((u>>(2*j))&3)==3 for j in range(m));k=s+2*t
            bracket=F(2)**k-4*(1-p)**(2*m-2*t) if s==0 else F(2)**k-4*F(2)**t*d**(m-s-t)+4*(1-p)**(2*m-s-2*t)
            expected=(p*(1-p))**k*bracket**2
            assert correlation_square(sgn,p,u)==expected
        exact.append({'kind':'unconditioned_plus_completion','m':m,'shifts':(1<<(2*m))-1})
    out['exact_correlations']=exact
    # Exact tensor obstruction, certified entropy interval at k=32.
    base=onepoint_shell(3,F(1,4));Z=1+sum(q*c for q,c in base)
    assert [q for q,c in base]==[F(3,256),F(9,256),F(27,256)]
    assert Z==F(319,256)
    L=entropy_interval(base);log3=lg_interval(3);K=(2-F(9,8)*log3[1],2-F(9,8)*log3[0]);I=F(3,4)
    ratio=((Z**31*L[0]/4-K[1])/I,(Z**31*L[1]/4-K[0])/I)
    assert ratio[0]>328
    suspended=(ratio[0]*F(24,25),ratio[1]*F(24,25));assert suspended[0]>315
    out['tensor_certificate']={'base_Z':str(Z),'base_L_interval':encl(L),'base_K_interval':encl(K),'k':32,'(L_k/4-K_k)/I_k_interval':encl(ratio),'rigorous_lower_bound':328,'balanced_suspension_ratio_interval':encl(suspended),'suspended_rigorous_lower_bound':315}
    # Additional direct tensor identity using exact weights and interval entropy.
    weights=[F(1)]+[F(3,256)]*3+[F(9,256)]*3+[F(27,256)]
    for k in (2,3):
        vals=[F(1)]
        for _ in range(k):vals=[x*y for x in vals for y in weights]
        assert sum(vals)==Z**k
        direct=entropy_interval([(x,1) for x in vals]);pred=(k*Z**(k-1)*L[0],k*Z**(k-1)*L[1])
        assert max(direct[0],pred[0])<=min(direct[1],pred[1])
    out['tensor_entropy_identity_checks']=[2,3]
    out['asymptotic_examples_FLOAT_NOT_CERTIFICATES']=[numerical_metrics(m) for m in (3,4,6,8,12,16,24,32)]
    out['script_sha256']=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    pathlib.Path('verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
