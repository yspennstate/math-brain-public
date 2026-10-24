#!/usr/bin/env python3
"""Deterministic sanity checker for the B16 all-constraint Boolean projection theorem. Standard library only; not the analytic proof."""
from itertools import product
from math import sqrt, log, prod
from random import Random
LN2=log(2.0)
def bits_index(bits):
    k=len(bits); return sum(bits[i]<<(k-1-i) for i in range(k))
def phi(mask,bits,p):
    z=1.0
    for i in range(len(p)):
        if mask&(1<<i): z*=(bits[i]-p[i])/sqrt(p[i]*(1-p[i]))
    return z
def fourier(truth,p):
    k=len(p); probs={}
    for bits in product((0,1),repeat=k):
        pr=1.0
        for i,x in enumerate(bits): pr*=p[i] if x else 1-p[i]
        probs[bits]=pr
    a={m:sum(pr*truth[bits_index(bits)]*phi(m,bits,p) for bits,pr in probs.items()) for m in range(1<<k)}
    return a,probs
def conditional_product(y):
    k=len(y); Z=prod(1+t for t in y)-1
    return {s:prod(y[i] for i in range(k) if s&(1<<i))/Z for s in range(1,1<<k)}
def one_case(truth,p,y):
    k=len(p); a,probs=fourier(truth,p); parse=sum(z*z for z in a.values()); m=a[0]; v=1-m*m
    if v<1e-13: return None
    w={s:a[s]*a[s]/v for s in range(1,1<<k)}; nu=conditional_product(y); b={0:m}
    for s in range(1,1<<k): b[s]=(1 if a[s]>=0 else -1)*sqrt(v*nu[s])
    eabs=eb2=egb=0.0
    for bits,pr in probs.items():
        B=sum(b[s]*phi(s,bits,p) for s in range(1<<k)); g=truth[bits_index(bits)]
        eabs+=pr*abs(B); eb2+=pr*B*B; egb+=pr*g*B
    bc=sum(sqrt(w[s]*nu[s]) for s in w); bcfull=(1-v)+v*bc
    D=sum(w[s]*log(w[s]/nu[s],2) for s in w if w[s]>0); lower=-2*log(eabs,2)/v; q=2*(1-eabs)
    err=max(abs(parse-1),abs(eb2-1),abs(egb-bcfull),abs(q-2*(1-eabs)))
    return D,lower,eabs,q,err
def solve_c(r):
    def F(c): return 1-c-prod(1-c*x for x in r)
    lo=1e-14; prev=F(lo); xp=lo
    for j in range(1,100001):
        x=j/100000; cur=F(x)
        if prev*cur<=0:
            a,b=xp,x; fa=prev
            for _ in range(100):
                m=(a+b)/2; fm=F(m)
                if fa*fm<=0: b=m
                else: a=m; fa=fm
            return (a+b)/2
        prev=cur; xp=x
    raise RuntimeError
def witness4():
    nums=[0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0]; a=[z/16 for z in nums]
    r=[sum(a[s]*a[s] for s in range(16) if s&(1<<i)) for i in range(4)]; c=solve_c(r); t=[c*x for x in r]; Q={}
    for s in range(1,16):
        z=1.0
        for i,ti in enumerate(t): z*=ti if s&(1<<i) else 1-ti
        Q[s]=z/c
    P={s:a[s]*a[s] for s in range(1,16)}; K=sum(P[s]*log(P[s]/Q[s],2) for s in P if P[s]>0); b={0:0.0}
    for s in range(1,16): b[s]=(1 if a[s]>=0 else -1)*sqrt(Q[s])
    vals=[sum(b[s]*((-1.0)**((s&x).bit_count())) for s in range(16)) for x in range(16)]
    eabs=sum(abs(z) for z in vals)/16; proj=-2*log(eabs,2); comp=prod(ti*(1-ti) for ti in t)/(c*c*LN2)
    return r,c,K,eabs,proj,comp,min(vals),max(vals)
def main():
    n=0; worst=1e100; maxerr=0.0
    for k in (1,2,3):
        p=[0.23+0.11*i for i in range(k)]; y=[0.17+0.09*i for i in range(k)]
        for mask in range(1<<(1<<k)):
            truth=[1 if (mask>>j)&1 else -1 for j in range(1<<k)]; out=one_case(truth,p,y)
            if out is None: continue
            D,lb,_,_,err=out; n+=1; worst=min(worst,D-lb); maxerr=max(maxerr,err)
            if D+2e-12<lb: raise AssertionError((k,mask,D,lb))
    rng=Random(20260922); nr=0; rw=1e100
    for _ in range(2000):
        k=rng.choice((2,3,4)); p=[0.05+0.9*rng.random() for _ in range(k)]; y=[10**rng.uniform(-1.5,1.5) for _ in range(k)]
        mask=rng.randrange(1<<(1<<k)); truth=[1 if (mask>>j)&1 else -1 for j in range(1<<k)]; out=one_case(truth,p,y)
        if out is None: continue
        D,lb,_,_,err=out; nr+=1; rw=min(rw,D-lb); maxerr=max(maxerr,err)
        if D+2e-11<lb: raise AssertionError((k,mask,D,lb))
    r,c,K,eabs,proj,comp,vmin,vmax=witness4()
    assert proj>comp and K>=proj
    print('PASS'); print('exhaustive_nonconstant_cases =',n); print('exhaustive_min_KL_minus_projection =',format(worst,'.17g'))
    print('deterministic_random_nonconstant_cases =',nr); print('random_min_KL_minus_projection =',format(rw,'.17g')); print('max_identity_error =',format(maxerr,'.17g'))
    print('prime4_influences =',r); print('prime4_c =',format(c,'.17g')); print('prime4_Kocc =',format(K,'.17g')); print('prime4_EabsB =',format(eabs,'.17g'))
    print('prime4_projection_KL_lower =',format(proj,'.17g')); print('prime4_complement_parity_lower =',format(comp,'.17g')); print('prime4_projection_over_complement =',format(proj/comp,'.17g')); print('prime4_B_range =',format(vmin,'.17g'),format(vmax,'.17g'))
if __name__=='__main__': main()
