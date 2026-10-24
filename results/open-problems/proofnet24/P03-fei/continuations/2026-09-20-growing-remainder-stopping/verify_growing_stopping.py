#!/usr/bin/env python3
"""Exact finite checks for growing-depth arithmetic-remainder stopping.
Python >=3.10 and NumPy. All pass/fail inequalities use integer/rational arithmetic.
The all-dimensional arguments are in REPORT.md; no full FEI proof is claimed.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial
from collections import Counter, defaultdict
from pathlib import Path
import hashlib, json
import numpy as np


def nu2(a):
    a=abs(int(a)); assert a
    return (a&-a).bit_length()-1

def plus(a,b): return a[0]+b[0],a[1]+b[1]
def times(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def outward(a,bits=96):
    D=1<<bits
    return (F(a[0].numerator*D//a[0].denominator,D),
            F(-((-a[1].numerator*D)//a[1].denominator),D))
@lru_cache(None)
def ln_unit(x):
    assert F(1)<=x<=F(2)
    z=(x-1)/(x+1); zz=z*z; p=z; s=F(0); M=48
    for j in range(M): s+=2*p/(2*j+1); p*=zz
    return s,s+2*p/((2*M+1)*(1-zz))
@lru_cache(None)
def log2(x):
    x=F(x); assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length(); u=x/F(2)**k
    if u<1: k-=1;u*=2
    if u>=2:k+=1;u/=2
    if u==1:return F(k),F(k)
    # Monotone range enclosure before the series avoids giant denominators.
    D=1<<160; lo=F(u.numerator*D//u.denominator,D);hi=min(F(2),lo+F(1,D))
    assert lo<=u<=hi
    a=ln_unit(lo)[0];b=ln_unit(hi)[1]; c,d=ln_unit(F(2))
    return outward((k+a/d,k+b/c))
def h(x):return times(x,log2(1/x)) if x else (F(0),F(0))
def show(a):return [str(x) for x in outward(a,72)]

def fwht(a):
    a=np.array(a,dtype=np.int64); n=len(a).bit_length()-1
    for j in range(n):
        v=a.reshape(-1,2<<j);l=v[:,:1<<j].copy();r=v[:,1<<j:].copy()
        v[:,:1<<j]=l+r;v[:,1<<j:]=l-r
    return a

def data(f):
    N=len(f);n=N.bit_length()-1;W=fwht(f); R=F(0);H=(F(0),F(0))
    assert int(np.sum(W*W))==N*N
    for a,c in Counter(map(int,abs(W))).items():
        if not a:continue
        V=fwht(np.where(abs(W)==a,np.sign(W),0))
        r=min(nu2(v) for v in V if v)
        p=F(c*a*a,N*N);R+=p*r;H=plus(H,times(c,h(F(a*a,N*N))))
    I=F(sum(int(a)**2*s.bit_count() for s,a in enumerate(W)),N*N)
    return H,R,I

def elementary_value(N,M,b,w):
    return sum(comb(w,j)*comb(M-w,b-j)*(N-1)**j*(-1)**(b-j)
               for j in range(max(0,b-(M-w)),min(w,b)+1))

def exact_R(k,M):
    N=1<<k;q=F(N-1,N)
    return sum((F(4*nu2(comb(M,b))*comb(M,b)*(N-1)**(2*M-b),N**(2*M))
                for b in range(1,M+1)),F(0))

def entropy_formula(k,M):
    N=1<<k;q=F(N-1,N);z=q**M
    A=plus(times(-2*q*q,log2(q)),(2*q*k/N,2*q*k/N))
    C=plus(h((2*z-1)**2),times(-4,h(z*z)))
    C=plus(C,(-8*(z-z*z),-8*(z-z*z)))
    return plus(times(4*M*q**(M-1),A),C)

def exact_masks():
    masks=values=carry=0
    for k in range(2,6):
        N=1<<k
        for M in range(1,N):
            for b in range(M+1):
                V=[elementary_value(N,M,b,w) for w in range(M+1)]
                observed=min(nu2(v) for v in V if v)
                assert observed==nu2(comb(M,b))<k
                assert observed==min(k*j+nu2(comb(M-j,b-j)) for j in range(b+1))
                masks+=1;values+=len(V)
        L=1
        while L<N-1:
            M=N-1-L
            for b in range(M+1):
                assert nu2(comb(M,b))==nu2(1+b//L)
                carry+=1
            L*=2
    truth=[]
    for k,M in ((2,3),(3,3),(3,4),(4,2),(4,3)):
        x=np.arange(1<<(k*M)); a=np.ones(len(x),dtype=bool)
        for j in range(M):a&=((x>>(k*j))&((1<<k)-1))!=0
        H,R,I=data(2*a.astype(np.int64)-1)
        assert R==exact_R(k,M)
        N=1<<k;q=F(N-1,N)
        assert I==F(2*k*M,N)*q**(M-1)
        HH=entropy_formula(k,M)
        assert max(H[0],HH[0])<=min(H[1],HH[1])
        truth.append(dict(k=k,blocks=M,dimension=k*M,R=str(R),I=str(I),H=show(H)))
    return dict(masks=masks,physical_zero_count_values=values,carry_formula_cases=carry,
                actual_truth_tables=truth)

def target(N):
    L=1
    while factorial(L)<N:L*=2
    return L

def query_law(k,L,cap):
    # State is (number of cleared blocks, preceding zero bits in current block).
    # Each fresh queried bit is fair. A k-zero block terminates at a constant leaf.
    state={(0,0):F(1)};success=death=fail=expected=F(0);states=0
    for depth in range(cap):
        expected+=sum(state.values());states+=len(state);new=defaultdict(F)
        for (cleared,zeros),p in state.items():
            if cleared+1==L:success+=p/2
            else:new[(cleared+1,0)]+=p/2
            if zeros+1==k:death+=p/2
            else:new[(cleared,zeros+1)]+=p/2
        state=dict(new)
        if not state:break
    fail=sum(state.values())
    assert success+death+fail==1
    return success,death,fail,expected,states

def stopping_checks():
    rows=[];mask_count=0
    for k in range(6,11):
        N=1<<k;m=N-1;q=F(N-1,N);L=target(N);M=m-L
        assert 8<=L<=N//8 and L<=2*k and factorial(L)>=N
        Q=F(2*k*L,N)*q**(m-1)
        R=exact_R(k,M)
        assert R<=4*q**M/F(factorial(L))
        assert q**L*R<=F(2,k*L)*Q
        H=entropy_formula(k,m);HC=entropy_formula(k,M)
        drop=plus(H,times(-q**L,HC))
        assert drop[1]<8*Q
        Ddrop=plus(times(F(1,2),drop),(q**L*R,q**L*R))
        assert Ddrop[1]<=F(17,4)*Q
        d=4*L+8*k; assert d<=16*k
        success,death,fail,expected,states=query_law(k,L,d)
        assert fail<=F(1,N**4) and expected<=2*L
        s0,z0,f0,e0,st0=query_law(k,L,k*L)
        assert f0==0 and s0==q**L and e0<=2*L
        error=F(k*(N-1),N**4)
        assert error/Q<F(1,16)
        assert (F(17,4)*Q+error)/(Q-error)<5
        # Parametric upper/lower sandwich also calibrates the factorial rate.
        leading=F(4*comb(M,L)*(N-1)**(2*M-L),N**(2*M))
        assert leading<=R<=leading*(1+F(3,L))
        mask_count+=M+1
        rows.append(dict(k=k,N=N,physical_dimension=k*m,L=L,
                         full_H_loss_per_Q=show(times(1/Q,drop)),
                         full_D_loss_per_Q=show(times(1/Q,Ddrop)),
                         R_leaf=show((R,R)),max_depth=d,
                         expected_queries_upper=2*L,
                         actual_query_expectation=show((expected,expected)),
                         exact_capping_probability=show((fail,fail)),
                         query_states=states,cap_D_loss_per_Q_upper=show(((F(17,4)*Q+error)/(Q-error),)*2)))
    # Larger dimensions: exact small-state query laws and rational truncation bounds,
    # not giant Walsh transforms or enormous binomial-polynomial expansions.
    large=[]
    for k in (12,16,20,32,64):
        N=1<<k;L=target(N);d=4*L+8*k
        s,z,p,e,states=query_law(k,L,d)
        assert p<=F(1,N**4) and e<=2*L and L<=2*k and L<=N//8
        assert F(3,2*L*N*N)<F(1,16)
        assert factorial(L)>=N
        large.append(dict(k=k,L=L,max_depth=d,expected_queries_upper=2*L,
                          exact_capping_probability=show((p,p)),query_states=states))
    return dict(exact_entropy_and_remainder_parameter_cases=len(rows),rows=rows,
                larger_query_law_cases=large)

def lower_depth_checks():
    # The asymptotic lower-depth proof is analytic. Here its explicit finite
    # inequalities are checked at growing k and growing depth, with true quantifiers.
    rows=[]
    for k in (16,32,64,128,256,512):
        N=1<<k;d=max(1,k//(4*k.bit_length()))
        assert N>=16*(d+1)
        ratio=F(N,4*d*factorial(d)*8**d)
        assert ratio>1
        rows.append(dict(k=k,depth=d,uniform_D_drop_per_Q_lower=str(ratio)))
    return dict(cases=rows,scope='Finite certificates only; no extrapolated proof claim.')

def kl_checks():
    # Exact identity for B_i through normalized minority/co-minority distributions.
    # Finite entropy identities use rational outward intervals, plus exact endpoint handling.
    rng=np.random.default_rng(20260920);cases=0;zero=0
    for n in range(1,7):
        for rep in range(10):
            N=1<<n;f=1-2*rng.integers(0,2,size=N,dtype=np.int64)
            if rep==0:f=np.ones(N,dtype=np.int64);f[0]=-1
            W=fwht(f);x=np.arange(N)
            for i in range(n):
                ids=x[(x&(1<<i))==0];u=W[ids];v=W[ids|(1<<i)]
                ws=[F(int(a*a+b*b),N*N) for a,b in zip(u,v)]
                ms=[F(min(int(a*a),int(b*b)),N*N) for a,b in zip(u,v)]
                M=sum(ms)
                if M==0:zero+=1;continue
                B=(F(0),F(0));K=(F(0),F(0));Kc=(F(0),F(0))
                for w,m in zip(ws,ms):
                    if not w:continue
                    B=plus(B,plus(h(m),h(w-m)));B=plus(B,times(-1,h(w)))
                    if m:K=plus(K,times(m/M,log2(m/(M*w))))
                    if w>m:Kc=plus(Kc,times((w-m)/(1-M),log2((w-m)/((1-M)*w))))
                rhs=plus(h(M),h(1-M));rhs=plus(rhs,times(-M,K));rhs=plus(rhs,times(-(1-M),Kc))
                assert max(B[0],rhs[0])<=min(B[1],rhs[1])
                cases+=1
    return dict(exact_identity_comparisons=cases,zero_minority_cases=zero,
                universal_KL_lower_bound_proved=False)

def main():
    out=dict(status='PASS',full_FEI_proved=False,independent_review=False,formal_proof_assistant=False,
             exact_mask_formula=exact_masks(),stopping=stopping_checks(),
             growing_lower_depth=lower_depth_checks(),normalized_spectral_information=kl_checks())
    out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text=json.dumps(out,indent=2)+'\n';Path(__file__).with_name('verification.json').write_text(text)
    print(text)
if __name__=='__main__':main()
