#!/usr/bin/env python3
"""Exact finite checks for the concave Fourier restriction cap.

Python >=3.10 and NumPy. Assertions use integers and rational enclosures.
This is a self-check of REPORT.md, not a proof assistant or a full FEI proof.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
from pathlib import Path
import hashlib
import json
import numpy as np

Interval = tuple[F, F]
SEED = 2026092011

def add(a: Interval, b: Interval) -> Interval:
    return a[0]+b[0], a[1]+b[1]

def scale(c: F, a: Interval) -> Interval:
    return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])

@lru_cache(None)
def ln_range(x: F) -> Interval:
    assert 1 <= x <= 2
    z=(x-1)/(x+1); z2=z*z; power=z; total=F(0)
    terms=48
    for k in range(terms):
        total += 2*power/(2*k+1)
        power *= z2
    return total, total + 2*power/((2*terms+1)*(1-z2))

@lru_cache(None)
def log2(x: F) -> Interval:
    assert x > 0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    t=x/F(2)**k
    if t<1: k-=1; t*=2
    if t>=2: k+=1; t/=2
    a,b=ln_range(t); c,d=ln_range(F(2))
    return F(k)+a/d, F(k)+b/c

@lru_cache(None)
def hterm(t: F) -> Interval:
    return scale(t,log2(1/t)) if t else (F(0), F(0))

@lru_cache(None)
def h2(t: F) -> Interval:
    assert 0<=t<=1
    return add(hterm(t),hterm(1-t))

@lru_cache(None)
def cap(t: F) -> Interval:
    """Psi(t)=h2(t)+1-h2(1/2+sqrt(t(1-t)))."""
    assert 0<=t<=F(1,2)
    if not t: return F(0), F(0)
    if t==F(1,2): return F(2),F(2)
    z=t*(1-t); den=1<<180
    k=isqrt((z.numerator*den*den)//z.denominator)
    lo=F(k,den); hi=F(k+1,den)
    assert lo*lo<=z<=hi*hi
    qlo=F(1,2)+lo; qhi=min(F(1),F(1,2)+hi)
    # h2 decreases on [1/2,1].
    low,high=h2(t)
    return low+1-h2(qlo)[1],high+1-h2(qhi)[0]


def tables(n: int) -> np.ndarray:
    return ((np.arange(1<<(1<<n),dtype=np.uint64)[:,None] >>
             np.arange(1<<n,dtype=np.uint64)[None,:]) & 1).astype(np.int64)


def fwht(a: np.ndarray) -> np.ndarray:
    a=np.asarray(a,dtype=np.int64).copy()
    if a.ndim==1: a=a[None,:]
    N=a.shape[1]; assert N and not N&(N-1)
    for i in range(N.bit_length()-1):
        r=a.reshape(len(a),-1,2<<i)
        u=r[:,:,:1<<i].copy(); v=r[:,:,1<<i:].copy()
        r[:,:,:1<<i]=u+v; r[:,:,1<<i:]=u-v
    return a


def profile(u: np.ndarray, v: np.ndarray) -> tuple:
    a=np.minimum(abs(u),abs(v)); b=np.maximum(abs(u),abs(v))
    return tuple(sorted(Counter(zip(map(int,a),map(int,b))).items()))

@lru_cache(None)
def certify_profile(N: int, signature: tuple) -> tuple[F,F,bool]:
    mass=F(0); mean=F(0); second=F(0); delta=(F(0),F(0)); ts=set()
    for (u,v),count in signature:
        s=u*u+v*v
        if not s: continue
        w=F(count*s,N*N); t=F(u*u,s)
        mass+=w; mean+=w*t; second+=w*t*t; ts.add(t)
        if u==0: local=(F(0),F(0))
        elif u==v: local=(F(2*s,N*N),F(2*s,N*N))
        else:
            local=add(hterm(F(u*u,N*N)),hterm(F(v*v,N*N)))
            local=add(local,scale(F(-1,2),hterm(F((u+v)**2,N*N))))
            local=add(local,scale(F(-1,2),hterm(F((u-v)**2,N*N))))
        delta=add(delta,scale(F(count),local))
    assert mass==1 and 0<=mean<=F(1,2)
    variance=second-mean*mean
    assert variance>=0
    if len(ts)==1:
        # Exact equality from the homogeneous fibre formula; no interval sign test.
        assert not variance
        # Dyadic Parseval rigidity excludes a constant interior fibre ratio.
        assert mean in (F(0), F(1,2))
        return mean,variance,True
    bound=cap(mean)
    lnlo,lnhi=ln_range(F(2))
    margin=bound[0]-delta[1]-2*variance/lnlo
    assert margin>0, (N,signature,margin)
    return mean,variance,False


def exhaustive_splits() -> dict:
    functions=coordinates=equalities=0
    for n in range(1,5):
        N=1<<n; x=np.arange(N); tt=tables(n); ww=fwht(1-2*tt)
        assert np.all((ww*ww).sum(axis=1)==N*N)
        functions+=len(tt)
        for i in range(n):
            ids=x[(x&(1<<i))==0]
            for row,truth in zip(ww,tt):
                u=row[ids]; v=row[ids|(1<<i)]
                M,V,equal=certify_profile(N,profile(u,v))
                inf=F(int(np.count_nonzero(truth!=truth[x^(1<<i)])),N)
                assert F(int((v*v).sum()),N*N)==inf
                assert M<=min(inf,1-inf)
                equalities+=int(equal); coordinates+=1
    return dict(functions=functions,coordinate_splits=coordinates,
                equality_splits=equalities,distinct_profiles=certify_profile.cache_info().currsize,
                scope='All Boolean functions in dimensions 1--4; all coordinates; cap and explicit variance credit.')


def shared_product_checks() -> dict:
    parents=1-2*tables(3); cc=[]; pairs=0; direct_affinity=0
    for row in parents:
        a=fwht(row[::2])[0]; b=fwht(row[1::2])[0]
        affinity=F(int(np.abs(a*b).sum()),16)
        cc.append((a,b,affinity))
    distinct=set()
    for a,b,A in cc:
        for c,d,B in cc:
            p=np.outer(a,c).ravel(); q=np.outer(b,d).ravel()
            assert F(int(np.abs(p*q).sum()),256)==A*B
            M,V,equal=certify_profile(32,profile(p+q,p-q))
            assert M==(1-A*B)/2
            x,y=(1-A)/2,(1-B)/2
            distinct.add((x,y)); pairs+=1; direct_affinity+=1
    for x,y in distinct:
        star=x+y-2*x*y
        if not x or not y: assert star==x+y
        else: assert cap(star)[1] <= cap(x)[0]+cap(y)[0]
    rng=np.random.default_rng(SEED); multi=0
    for _ in range(80):
        count=int(rng.integers(3,6)); p=np.array([1]); q=np.array([1]); A=F(1); Ms=[]; childN=1
        for _ in range(count):
            a,b,B=cc[int(rng.integers(0,len(cc)))]
            p=np.outer(p,a).ravel();q=np.outer(q,b).ravel();A*=B;Ms.append((1-B)/2);childN*=4
        assert F(int(np.abs(p*q).sum()),childN*childN)==A
        M,V,equal=certify_profile(2*childN,profile(p+q,p-q))
        assert M==(1-A)/2
        bounds=[cap(x) for x in Ms]
        if sum(x!=0 for x in Ms)<=1: assert M==sum(Ms)
        else: assert cap(M)[1] <= sum(b[0] for b in bounds)
        multi+=1
    return dict(pair_cases=pairs,affinity_identities=direct_affinity,distinct_affinity_pairs=len(distinct),
                multifactor_cases=multi,scope='Every pair of three-variable Boolean parents sharing their control; 80 seeded products of 3--5 such parents.')


def scalar_checks() -> dict:
    value=scale(F(4),cap(F(1,4)))
    lo=F(58267968871754,10**13);hi=F(58267968871756,10**13)
    assert lo < value[0] <= value[1] < hi
    # Concavity/subadditivity on a finite rational grid, supplemented by the analytic proof.
    values=[F(i,64) for i in range(33)]; tests=0
    for x in values:
        for y in values:
            star=x+y-2*x*y
            if not x or not y: assert star==x+y
            else: assert cap(star)[1] <= cap(x)[0]+cap(y)[0]
            tests+=1
    return dict(compression_coefficient_interval=['5.8267968871754','5.8267968871756'],
                affinity_grid_comparisons=tests,full_FEI_constant_claimed=False)


def main() -> None:
    output={'status':'PASS','date':'2026-09-20','seed':SEED,'full_FEI_proved':False,
            'independent_audit':False,'formal_proof_assistant_used':False,
            'exhaustive_splits':exhaustive_splits(),
            'shared_products':shared_product_checks(),'scalar_checks':scalar_checks()}
    output['total_distinct_profiles']=certify_profile.cache_info().currsize
    output['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text=json.dumps(output,indent=2)+'\n'
    Path(__file__).with_name('verification.json').write_text(text)
    print(text,end='')

if __name__=='__main__': main()
