#!/usr/bin/env python3
"""Exact self-checks for Boolean Fourier packet bounds; NOT a full FEI proof.
Python 3.10+ and NumPy. All assertion arithmetic is integer/Fraction or
outward rational logarithm enclosures. No floating-point inequality tests.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import hashlib, json
import numpy as np

SEED = 2026092053

@lru_cache(None)
def lnrange(t:F):
    assert 1<=t<=2
    z=(t-1)/(t+1); z2=z*z; power=z; total=F(0); terms=48
    for k in range(terms):
        total += 2*power/(2*k+1); power *= z2
    return total,total+2*power/((2*terms+1)*(1-z2))

@lru_cache(None)
def log2(x:F):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length(); t=x/F(2)**k
    if t<1:k-=1;t*=2
    if t>=2:k+=1;t/=2
    lo,hi=lnrange(t); l2,u2=lnrange(F(2))
    return F(k)+lo/u2,F(k)+hi/l2

@lru_cache(None)
def pair(u:int,v:int):
    """E(u^2,v^2), before normalizing Walsh coefficients."""
    if not u or not v:return F(0),F(0)
    x,y=u*u,v*v
    a,b=log2(F(x+y,x));c,d=log2(F(x+y,y))
    return x*a+y*c,x*b+y*d

@lru_cache(None)
def factor(n:int):
    assert n>0
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            k=0
            while n%p==0:n//=p;k+=1
            out.append((p,k))
        p=3 if p==2 else p+2
    if n>1:out.append((n,1))
    return tuple(out)

def expr_add(out,terms,weight=F(1)):
    out=dict(out)
    for p,c in terms.items():
        out[p]=out.get(p,F(0))+weight*c
        if not out[p]:del out[p]
    return out

@lru_cache(None)
def pair_expr(u:int,v:int):
    if not u or not v:return {}
    x,y=u*u,v*v;out={}
    for n,weight in ((x+y,x+y),(x,-x),(y,-y)):
        out=expr_add(out,dict(factor(n)),F(weight))
    return out

def fwht(a):
    a=np.asarray(a,dtype=np.int64).copy()
    if a.ndim==1:a=a[None,:]
    N=a.shape[1];assert N and not N&(N-1)
    for i in range(N.bit_length()-1):
        r=a.reshape(len(a),-1,2<<i);u=r[:,:,:1<<i].copy();v=r[:,:,1<<i:].copy()
        r[:,:,:1<<i]=u+v;r[:,:,1<<i:]=u-v
    return a

def all_tables(n):
    return (1-2*((np.arange(1<<(1<<n),dtype=np.uint64)[:,None]
           >>np.arange(1<<n,dtype=np.uint64)[None,:])&1).astype(np.int64))

def profile(a,b):
    a=np.abs(a);b=np.abs(b)
    A=int(a.sum());B=int(b.max(axis=0).sum()) if len(a) else 0
    E=int((b*b).sum());L=int((a[:,None]*b).sum())
    cnt=Counter(tuple(sorted((int(u),int(v)))) for u,row in zip(a,b) for v in row)
    return A,B,E,L,tuple(sorted(cnt.items()))

@lru_cache(None)
def certify(signature):
    A,B,E,L,cnt=signature
    assert L<=A*B
    lo=F(0);hi=F(0)
    for (u,v),count in cnt:
        x,y=pair(u,v);lo+=count*x;hi+=count*y
        # An asymmetric scalar estimate; the symmetric pairing is used
        # only for entropy evaluation, not to assert a global power payment.
    if not A or not B or not E:
        assert lo==hi==0;return lo,hi
    assert hi*hi < 16*A*B*E
    # Sharp logarithmic envelope at the ACTUAL overlap L.
    if L<=E:
        cap_lo=cap_hi=F(2*L);cap_expr={2:F(2*L)} if L else {}
    else:
        x,y=pair(L,E);cap_lo,cap_hi=x/E,y/E
        cap_expr={p:c/E for p,c in pair_expr(L,E).items()}
    if hi>cap_lo:
        actual={}
        for (u,v),count in cnt:
            actual=expr_add(actual,pair_expr(u,v),F(count))
        assert expr_add(cap_expr,actual,F(-1))=={}, (signature,'unresolved cap comparison')
    l2,u2=lnrange(F(2));qlo,qhi=log2(1+F(L,E))
    lower_rhs=F(E)/u2+2*E*qlo
    assert hi<lower_rhs
    return lo,hi

def exhaust():
    functions=coefficients=packets=low_bands=0
    for n in range(1,5):
        N=1<<n;x=np.arange(N);tt=all_tables(n);ww=fwht(tt)
        assert np.all((ww*ww).sum(axis=1)==N*N)
        infcounts=np.stack([np.count_nonzero(tt!=tt[:,x^(1<<i)],axis=1) for i in range(n)],axis=1)
        functions+=len(tt)
        for i in range(n):
            labels=x[(x&(1<<i))!=0]
            assert np.all(np.abs(ww[:,labels])<=infcounts[:,i,None])
            coefficients+=len(tt)*len(labels)
        for row,ic in zip(ww,infcounts):
            for k in range(1,n):
                C=[1<<j for j in range(k)];D=list(range(k,n))
                a=row[C];b=np.array([[row[c|(1<<i)] for i in D] for c in C])
                sig=profile(a,b);A,B,E,_,_=sig
                assert A<=int(ic[:k].sum()) and B<=int(ic[k:].sum()) and E<=N*N
                certify(sig);packets+=1
            if n>=2:
                a=row[[1<<i for i in range(n)]]
                b=np.array([[row[(1<<j)|(1<<i)] if i!=j else 0 for i in range(n)] for j in range(n)])
                sig=profile(a,b);A,B,E,_,_=sig
                assert A<=int(ic.sum()) and B<=int(ic.sum())
                assert E==2*sum(int(row[s])**2 for s in range(N) if s.bit_count()==2)
                certify(sig)
                # The empty/singleton band is paid by 2 |a_empty| sum |a_i|.
                lo=F(0);hi=F(0)
                for u in a:
                    r,s=pair(abs(int(row[0])),abs(int(u)));lo+=r;hi+=s
                bound=2*abs(int(row[0]))*int(np.abs(a).sum())
                if not bound:assert lo==hi==0
                elif hi>bound:
                    # Exact scalar equality only for identical nonzero amplitudes.
                    assert all(not u or abs(int(u))==abs(int(row[0])) for u in a)
                low_bands+=1
    return dict(boolean_functions=functions,coefficient_capacity_assertions=coefficients,
                singleton_control_packets=packets,first_two_erasure_band_checks=low_bands,
                scope='All Boolean functions on 1--4 bits; canonical control/data splits, and all first two level bands.')

def sampled():
    rng=np.random.default_rng(SEED);cases=0;overlap_cases=0;wide_cases=0;edges=0
    for n in range(4,11):
        N=1<<n;x=np.arange(N)
        for rep in range(70):
            if rep%4==0:
                truth=np.ones(N,dtype=np.int64)
                truth[rng.choice(N,size=int(rng.integers(1,max(2,N//5))),replace=False)]=-1
            elif rep%4==1:
                truth=rng.choice([-1,1],size=N)
            else:
                bits=np.zeros(N,dtype=np.int64)
                for _ in range(int(rng.integers(1,n+3))):
                    mon=int(rng.integers(1,N));bits^=((x&mon)==mon)
                truth=1-2*bits
            row=fwht(truth)[0]
            ic=[int(np.count_nonzero(truth!=truth[x^(1<<i)])) for i in range(n)]
            c=int(rng.integers(1,n));D=list(range(c,n))
            possible=list(range(1,1<<c))
            C=list(map(int,rng.choice(possible,size=min(len(possible),int(rng.integers(1,15))),replace=False)))
            a=row[C];b=np.array([[row[s|(1<<i)] for i in D] for s in C]);sig=profile(a,b)
            A,B,E,_,_=sig
            loads=[sum((F(1,s.bit_count()) for s in C if (s>>j)&1),F(0)) for j in range(c)]
            cap=sum((loads[j]*ic[j] for j in range(c)),F(0));Lambda=max(loads)
            assert A<=cap<=Lambda*sum(ic[:c]) and B<=sum(ic[c:]) and E<=N*N
            certify(sig);cases+=1;edges+=sum(int(u!=0 and v!=0) for u,rr in zip(a,b) for v in rr)
            overlap_cases+=int(any(sum((s>>j)&1 for s in C)>1 for j in range(c)))
            wide_cases+=int(min(s.bit_count() for s in C)>=2)
    return dict(cases=cases,with_overlapping_centres=overlap_cases,all_centres_width_at_least_two=wide_cases,
                positive_selected_edges=edges,scope='Seeded Boolean truth tables, rare sets and polynomial phases in dimensions 4--10; arbitrary overlapping centres.')

def scalar():
    checks=0
    for u in range(33):
        for v in range(33):
            lo,hi=pair(u,v)
            if not u or not v:assert hi==0
            else:assert hi*hi<16*u*v**3
            checks+=1
    # Entirely rational endpoint constants used by the analytic proof.
    assert lnrange(F(2))[0]>F(2,3)
    return dict(asymmetric_scalar_pairs=checks,logarithm_terms=48)

def prior_addressing():
    """Test exact coefficients against an actual Boolean truth table at m=2.
    The all-m family and its power obstruction are prior work, not new here.
    """
    m=2;K=1<<m;n=m+1+K;N=1<<n;truth=[]
    for x in range(N):
        address=x&3;z=(x>>m)&1
        truth.append((-1 if (address&1) and (address&2) else 1) if z==0 else (1-2*((x>>(m+1+address))&1)))
    row=fwht(np.array(truth))[0];data=list(range(m+1,n))
    centres=list(range(1<<(m+1)))
    a=row[centres];b=np.array([[row[s|(1<<i)] for i in data] for s in centres])
    sig=profile(a,b);A,B,E,L,_=sig;lo,hi=certify(sig)
    assert F(A,N)==2 and F(B,N)==F(1,2) and F(E,N*N)==F(1,2) and F(L,N*N)==1
    assert all(row[s]==0 for s in range(N) if (s>>(m+1)).bit_count()>=2)
    # New logarithmic packet envelope on the inherited family:
    # E=1/2, L=AB=sqrt(K)/2, hence cost <=1/(2 ln2)+log2(1+sqrt(K)).
    symbolic=[]
    for m in (2,4,8,16,32,64):
        K=1<<m;root=1<<(m//2);I=F(m+2,2)
        l2,u2=lnrange(F(2));qlo,qhi=log2(F(1+root))
        assert F(1,2*l2)+qhi <= I+F(1)
        if m%4==0:
            power=F(1<<(m//4),2)
            symbolic.append({'address_bits':m,'exact_data_power_sum':str(power),'influence':str(I)})
    return dict(actual_truth_table_dimension=n,truth_table_entries=N,
                exact_packet_A='2',exact_packet_B='1/2',exact_packet_E='1/2',
                symbolic_cases=symbolic,scope='Only the seven-bit truth table is enumerated. Large entries evaluate inherited exact formulas; not a new obstruction or full FEI proof.')

def retention():
    out=[]
    for k in (1,2,4,8,16):
        K=4**k;root=2**k;eps=F(1,8*root)
        for w in (2,4):
            retained_centre=F(15,16)*eps/(4*K)
            lower=w*K*retained_centre
            real_upper=F(w)+F(3,4);real_upper/=256*K*K*(1-eps)
            ratio=lower/real_upper
            expected=F(15,2)*F(4*w,4*w+3)*(1-eps)*root**3
            assert ratio==expected
            out.append({'K':str(K),'w':w,'boolean_control_influence_lower':str(lower),
                        'real_energy_upper':str(real_upper),'ratio_lower':str(ratio)})
    return {'cases':out,'scope':'Analytic Fourier-retention implications applied to the prior square-root family; no Boolean function matching all coefficients is asserted to exist.'}

def main():
    out={'status':'PASS','date':'2026-09-20','seed':SEED,'full_FEI_proved':False,
         'independent_audit':False,'proof_assistant_used':False,'exhaustive':exhaust(),
         'sampled_packets':sampled(),'scalar':scalar(),'inherited_addressing':prior_addressing(),
         'spectral_retention':retention()}
    out['distinct_exact_packet_signatures']=certify.cache_info().currsize
    out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text=json.dumps(out,indent=2)+'\n';Path(__file__).with_name('verification.json').write_text(text);print(text,end='')
if __name__=='__main__':main()
