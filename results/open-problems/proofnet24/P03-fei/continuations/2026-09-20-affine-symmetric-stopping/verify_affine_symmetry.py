#!/usr/bin/env python3
"""Exact finite checks for affine images of symmetric Boolean products.
Proofs are in REPORT.md. Requires Python >=3.10 and NumPy.
No floating-point comparison is used for any assertion.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import hashlib,json
import numpy as np

SEED=2026092021

@lru_cache(None)
def log2(q:F):
    assert q>0
    k=q.numerator.bit_length()-q.denominator.bit_length();t=q/F(2)**k
    if t<1:k-=1;t*=2
    if t>=2:k+=1;t/=2
    def ln(x):
        z=(x-1)/(x+1);z2=z*z;power=z;v=F(0);M=48
        for j in range(M):v+=2*power/(2*j+1);power*=z2
        return v,v+2*power/((2*M+1)*(1-z2))
    a,b=ln(t);c,d=ln(F(2));return F(k)+a/d,F(k)+b/c

@lru_cache(None)
def factors(k:int):
    ans=[];p=2
    while p*p<=k:
        c=0
        while k%p==0:k//=p;c+=1
        if c:ans.append((p,c))
        p+=1
    if k>1:ans.append((k,1))
    return tuple(ans)

def clean(d):return {p:c for p,c in d.items() if c}
def linadd(a,b,c=F(1)):
    r=a.copy()
    for p,v in b.items():r[p]=r.get(p,F(0))+c*v
    return clean(r)

def entropy_form(vals,weights,N):
    assert sum(int(w)*int(v)**2 for v,w in zip(vals,weights))==N*N
    r={2:F(2*(N.bit_length()-1))}
    for v,count in zip(vals,weights):
        v=abs(int(v));count=int(count)
        if v:
            for p,power in factors(v):r[p]=r.get(p,F(0))-F(2*count*v*v*power,N*N)
    return clean(r)

def interval(form):
    lo=hi=F(0)
    for p,c in form.items():
        a,b=log2(F(p));lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi

def leq(form,bound):
    diff=linadd({2:F(bound)},form,F(-1))
    if diff:assert interval(diff)[0]>0,(form,bound,interval(diff))

def fwht(a):
    a=np.asarray(a,dtype=np.int64).copy();N=a.shape[-1]
    assert N>0 and not N&(N-1)
    for i in range(N.bit_length()-1):
        r=a.reshape(-1,2<<i);u=r[:,:1<<i].copy();v=r[:,1<<i:].copy()
        r[:,:1<<i]=u+v;r[:,1<<i:]=u-v
    return a

def rank(rows):
    piv={}
    for v in rows:
        v=int(v)
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return len(piv)

def basis_cost(costs):
    n=(len(costs)-1).bit_length();rows=[];val=0
    for v in sorted(range(1,len(costs)),key=lambda v:(int(costs[v]),v)):
        if rank(rows+[v])>len(rows):rows.append(v);val+=int(costs[v])
        if len(rows)==n:break
    assert len(rows)==n
    return val

def affine_cost(f):
    N=len(f);w=fwht(f);c=fwht(w*w)
    nums=N*N-np.abs(c)
    assert np.all(nums%(2*N)==0)
    return F(basis_cost(nums//(2*N)),N)

@lru_cache(None)
def kraw(n):
    out=[]
    for k in range(n+1):
        out.append([sum((-1)**j*comb(k,j)*comb(n-k,w-j)
                        for j in range(max(0,w-(n-k)),min(k,w)+1)) for w in range(n+1)])
    return np.array(out,dtype=np.int64)

def symmetric_data(signs):
    n=len(signs)-1;N=1<<n;W=kraw(n)@np.array(signs,dtype=np.int64)
    multiplicities=[comb(n,k) for k in range(n+1)]
    assert sum(m*int(w)**2 for m,w in zip(multiplicities,W))==N*N
    c=kraw(n)@(W*W);nums=N*N-c
    assert np.all(nums%(2*N)==0)
    alpha=nums//(2*N);j=np.minimum(alpha,N-alpha)
    # Rank of a complete fixed-weight orbit: n for an odd interior weight,
    # n-1 for an even interior weight; the all-ones orbit has rank one.
    full=even=ones=False;prev=val=0
    for k in sorted(range(1,n+1),key=lambda k:(int(j[k]),k)):
        if k==n:ones=True
        elif k%2:full=True
        else:even=True
        new=n if full else (n-1+int(ones and n%2==1) if even else int(ones))
        val+=(new-prev)*int(j[k]);prev=new
    assert prev==n or n==0
    return W,alpha,j,F(val,N),entropy_form(W,multiplicities,N)


def symmetric_checks():
    functions=swaps=ranks=parity=0;max_n=12
    for n in range(1,max_n+1):
        N=1<<n
        for code in range(1<<(n+1)):
            s=[1-2*((code>>i)&1) for i in range(n+1)]
            W,alpha,j,M,H=symmetric_data(s);functions+=1
            if n>=2:
                beta=F(int(alpha[2]),N)
                for k in range(1,n):assert alpha[2]<=2*j[k];swaps+=1
                assert M>=F(n-1,2)*beta
                leq(H,F(401,25)*(n-1)*beta) # 16.04=12.04+4
                leq(H,F(802,25)*M)          # 32.08=2(12.04+4)
                child=[]
                for b in (0,1):
                    t=[s[w+((w+b)&1)] for w in range(n)]
                    D=symmetric_data(t);child.append(D)
                avgI=F(n-1,2)*(F(int(child[0][1][1]),N//2)+F(int(child[1][1][1]),N//2))
                assert avgI==(n-1)*beta
                Dh=linadd(linadd(H,child[0][4],F(-1,2)),child[1][4],F(-1,2))
                var0=1-F(int(child[0][0][0])**2,(N//2)**2)
                var1=1-F(int(child[1][0][0])**2,(N//2)**2)
                leq(Dh,2*max(var0,var1));parity+=1
            else:assert not H
            if n<=5:
                cv=[int(j[v.bit_count()]) for v in range(N)]
                assert F(basis_cost(cv),N)==M;ranks+=1
    return dict(symmetric_truth_tables=functions,max_dimension=max_n,
                directional_swap_inequalities=swaps,parity_section_identities=parity,
                exact_orbit_rank_vs_vector_greedy=ranks)

@lru_cache(None)
def scalar_pair(u,v,N):
    u,v=sorted((abs(int(u)),abs(int(v))))
    if u==0 or u==v:return
    # Homogeneous entropy identity. The four weights sum on each side, so
    # normalization logarithms cancel exactly.
    def hform(k):
        if not k:return {}
        ans={2:F(2*(N.bit_length()-1)*k*k,N*N)}
        for p,pow in factors(abs(k)):ans[p]=ans.get(p,F(0))-F(2*k*k*pow,N*N)
        return clean(ans)
    d=linadd(hform(u),hform(v))
    d=linadd(d,hform(u+v),F(-1,2));d=linadd(d,hform(v-u),F(-1,2))
    leq(d,F(4*u*v,N*N))


def arbitrary_split_checks():
    functions=splits=0
    for n in range(1,5):
        N=1<<n;x=np.arange(N)
        for start in range(0,1<<N,2048):
            code=np.arange(start,min(start+2048,1<<N),dtype=np.uint64)
            truth=1-2*((code[:,None]>>np.arange(N,dtype=np.uint64))&1).astype(np.int64)
            W=fwht(truth);assert np.all((W*W).sum(axis=1)==N*N)
            functions+=len(code)
            for i in range(n):
                ids=x[(x&(1<<i))==0];U=W[:,ids];V=W[:,ids|(1<<i)]
                bound=2*N*N-2*np.minimum((U[:,0]+V[:,0])**2,(U[:,0]-V[:,0])**2)
                assert np.all(4*np.abs(U*V).sum(axis=1)<=bound)
                for u,v in set(zip(np.abs(U).ravel().tolist(),np.abs(V).ravel().tolist())):scalar_pair(u,v,N)
                splits+=len(code)
    return dict(functions=functions,physical_splits=splits,
                distinct_scalar_pair_calls=scalar_pair.cache_info().currsize,
                scope='All Boolean functions in dimensions 1--4; coefficientwise entropy/variation inequality plus exact variation-to-variance bound.')


def lifted_products():
    rng=np.random.default_rng(SEED);cases=0;largest=0;factor_checks=0
    for m in range(2,11):
        for rep in range(12):
            cuts=sorted(set([0,m]+rng.integers(1,m,size=int(rng.integers(0,4))).tolist()))
            blocks=[b-a for a,b in zip(cuts,cuts[1:])]
            y=np.arange(1<<m);f=np.ones(1<<m,dtype=np.int64);targetM=F(0);targetH={};off=0
            for b in blocks:
                s=rng.choice([-1,1],b+1).tolist();D=symmetric_data(s)
                targetM+=D[3];targetH=linadd(targetH,D[4]);factor_checks+=1
                mask=(1<<b)-1;f*=np.array([s[((int(v)>>off)&mask).bit_count()] for v in y]);off+=b
            assert affine_cost(f)==targetM
            Ndim=m+rep%3;N=1<<Ndim;x=np.arange(N);rows=[]
            while len(rows)<m:
                row=int(rng.integers(1,N))
                if rank(rows+[row])>len(rows):rows.append(row)
            shift=int(rng.integers(0,1<<m));mapped=np.full(N,shift,dtype=np.int64)
            for j,row in enumerate(rows):mapped^=np.array([(int(v)&row).bit_count()%2 for v in x])<<j
            g=f[mapped];character=int(rng.integers(0,N));g=g*np.array([1-2*((int(v)&character).bit_count()%2) for v in x])
            W=fwht(g);Hg=entropy_form(W,np.ones(N,dtype=int),N)
            assert Hg==targetH
            assert affine_cost(g)==targetM
            pnums=W*W;Jnum=sum(min(int(pnums[(x&(1<<i))!=0].sum()),int(pnums[(x&(1<<i))==0].sum())) for i in range(Ndim))
            J=F(Jnum,N*N);assert targetM<=J
            leq(Hg,F(802,25)*targetM);cases+=1;largest=max(largest,Ndim)
    return dict(product_lift_cases=cases,symmetric_factors=factor_checks,max_physical_dimension=largest,
                exact_entropy_invariance=True,exact_minimum_affine_influence_tensorization=True,
                scope='Seeded products, full-row-rank affine input maps including redundant domain coordinates, and arbitrary output characters; not dependent/non-surjective maps.')


def main():
    out=dict(status='PASS',date='2026-09-20',seed=SEED,full_FEI_proved=False,
             independent_audit=False,proof_assistant_used=False,
             arbitrary_splits=arbitrary_split_checks(),symmetric=symmetric_checks(),
             affine_products=lifted_products())
    out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text=json.dumps(out,indent=2)+'\n';Path(__file__).with_name('verification.json').write_text(text);print(text,end='')
if __name__=='__main__':main()
