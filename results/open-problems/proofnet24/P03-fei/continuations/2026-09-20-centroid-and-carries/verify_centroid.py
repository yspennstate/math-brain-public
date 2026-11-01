#!/usr/bin/env python3
"""Integer finite checks for the support-pairing theorem and Walsh carry barrier.
Python 3.10+ and NumPy. This is not a proof assistant or a full FEI proof.
"""
from __future__ import annotations
from collections import Counter
from pathlib import Path
from math import comb
import hashlib, json
import numpy as np
SEED=2026092071

def anf(a):
    a=np.asarray(a,dtype=np.uint8).copy()
    if a.ndim==1:a=a[None,:]
    N=a.shape[1]
    if len(a)==0:return a
    for j in range(N.bit_length()-1):
        v=a.reshape(len(a),-1,2<<j);v[:,:,1<<j:]^=v[:,:,:1<<j]
    return a

def degrees(a):
    c=anf(a);wt=np.array([x.bit_count() for x in range(c.shape[1])])
    return np.where(c!=0,wt,-1).max(axis=1)

def fwht(a):
    a=np.asarray(a,dtype=np.int64).copy()
    if a.ndim==1:a=a[None,:]
    for j in range(a.shape[1].bit_length()-1):
        v=a.reshape(len(a),-1,2<<j);u=v[:,:,:1<<j].copy();w=v[:,:,1<<j:].copy()
        v[:,:,:1<<j]=u+w;v[:,:,1<<j:]=u-w
    return a

def all_tables(n):
    return ((np.arange(1<<(1<<n),dtype=np.uint64)[:,None]>>np.arange(1<<n,dtype=np.uint64))&1).astype(np.uint8)

def check_supports(tables, degree, centers):
    """Check every reversed ordered distance pair, not just the average."""
    N=tables.shape[1];n=N.bit_length()-1;x=np.arange(N)
    m=tables.sum(axis=1).astype(int);keep=m>0
    a=tables[keep];d=np.asarray(degree)[keep];m=m[keep]
    count=0;pairs=0
    rev=np.maximum(0,m[:,None]-1-x)
    for center in centers:
        wt=np.array([(int(z)^int(center)).bit_count() for z in x])
        s=np.sort(np.where(a,wt,n+1),axis=1)
        sr=np.take_along_axis(s,rev,axis=1)
        valid=x[None,:]<m[:,None]
        assert np.all((s+sr>=n-d[:,None])|~valid)
        assert np.all(2*(a*wt).sum(axis=1)>=(n-d)*m)
        count+=len(a);pairs+=int(m.sum())
    return {'nonzero_supports':len(a),'center_profiles':count,'ordered_pair_assertions':pairs}

def gf2_rank(rows):
    piv={}
    for u in rows:
        while u:
            j=u.bit_length()-1
            if j in piv:u^=piv[j]
            else:piv[j]=u;break
    return len(piv)

def rank_checks(tables):
    N=tables.shape[1];n=N.bit_length()-1;wt=np.array([x.bit_count() for x in range(N)])
    ranks=orthogonality=0
    for table in tables:
        A=np.flatnonzero(table);m=len(A)
        if not m:continue
        d=int(degrees(table)[0]);k=n-d
        rows=[];h=[]
        for a in range(n+1):
            for mon in np.flatnonzero(wt==a):
                rows.append(sum(int((int(x)&int(mon))==int(mon))<<j for j,x in enumerate(A)))
            h.append(gf2_rank(rows));ranks+=1
            assert h[-1]>=int(np.count_nonzero(wt[A]<=a))
        for a in range(k):
            for b in range(k-a):
                assert h[a]+h[b]<=m;orthogonality+=1
    return {'evaluation_rank_checks':ranks,'orthogonal_dimension_checks':orthogonality}

def polynomial_checks():
    out={};total=Counter()
    for n in range(1,5):
        t=all_tables(n);r=check_supports(t,degrees(t),range(1<<n));out['all_n'+str(n)]=r;total.update(r)
    n=5;N=1<<n;mons=[x for x in range(N) if x.bit_count()<=2]
    c=np.zeros((1<<len(mons),N),dtype=np.uint8)
    c[:,mons]=((np.arange(len(c),dtype=np.uint64)[:,None]>>np.arange(len(mons),dtype=np.uint64))&1).astype(np.uint8)
    t=anf(c);r=check_supports(t,degrees(t),range(N));out['all_degree_le_2_n5']=r;total.update(r)
    rng=np.random.default_rng(SEED);rank_inputs=[]
    for n in range(5,11):
        N=1<<n;wt=np.array([x.bit_count() for x in range(N)])
        c=np.zeros((100,N),dtype=np.uint8)
        for row in c:
            d=int(rng.integers(1,min(5,n)+1));allowed=np.flatnonzero(wt<=d)
            chosen=rng.choice(allowed,size=min(len(allowed),int(rng.integers(1,25))),replace=False);row[chosen]=1
        t=anf(c);r=check_supports(t,degrees(t),rng.choice(N,8,replace=False));out['sample_n'+str(n)]=r;total.update(r)
        if n==5:rank_inputs=t[:24]
    out['totals_over_overlapping_families']=dict(total)
    out['rank_certificates']=rank_checks(rank_inputs)
    return out

def walsh_layer_checks():
    out=Counter();plateau_by_n={}
    for n in range(1,5):
        t=all_tables(n);W=fwht(1-2*t.astype(np.int64));N=1<<n
        assert np.all((W*W).sum(axis=1)==N*N)
        r=np.full(len(W),n,dtype=int)
        for j in range(n):
            hit=np.any((W%(1<<(j+1)))!=0,axis=1);r[hit]=np.minimum(r[hit],j)
        aff=r==n;Q=((W//(1<<r[:,None]))&1).astype(np.uint8)
        assert np.all(degrees(Q[~aff])<=r[~aff]-1)
        res=check_supports(Q[~aff],r[~aff]-1,range(N))
        out['functions']+=len(W);out['nonaffine_odd_layer_profiles']+=res['center_profiles']
        sq=W*W;mx=sq.max(axis=1);flat=np.all((sq==0)|(sq==mx[:,None]),axis=1)&~aff
        count=int(flat.sum());plateau_by_n[str(n)]=count;out['nonaffine_plateaued']+=count
        for row,rr in zip(W[flat],r[flat]):
            k=n-int(rr);p=row*row;alpha=[]
            for j in range(n):alpha.append(int(p[[s for s in range(N) if s&(1<<j)]].sum()))
            Jnum=sum(min(v,N*N-v) for v in alpha)
            assert 2*Jnum>=(k+1)*N*N
            assert np.count_nonzero(row)==1<<(2*k)
    return {'totals':dict(out),'nonaffine_plateaued_by_n':plateau_by_n,
            'scope':'All Boolean functions through n=4; exact bottom-layer degree, all centers, and plateaued folded bound.'}

def carry_checks():
    records=[];total=0
    for n in (5,7,9,11,13,17):
        N=1<<n;wt=np.array([x.bit_count() for x in range(N)],dtype=np.int64)
        f=np.where(wt==1,-1,1);W=fwht(f)[0]
        expected=-2*(n-2*wt);expected[0]+=N
        assert np.array_equal(W,expected)
        b=W//2;assert np.all(b%2!=0)
        dd=[]
        for ell in range(1,n-1):
            m=1<<(ell-1)
            if m>n:break
            digit=((b>>ell)&1).astype(np.uint8);deg=int(degrees(digit)[0]);assert deg==m
            c=(n+1)//2
            coeff=[(comb(c+m-j-1,m-j)&1) for j in range(m+1)]
            values=np.array([sum(coeff[j]*(comb(int(t),j)&1) for j in range(min(int(t),m)+1))&1 for t in wt],dtype=np.uint8)
            assert np.array_equal(digit,values)
            dd.append({'digit_index':ell,'exact_degree':deg});total+=1
        records.append({'n':n,'minimum_walsh_valuation':1,'digits':dd})
    return {'cases':records,'exact_digit_polynomial_identities':total,
            'scope':'Actual Walsh transforms through n=17 and exact generalized-binomial digit formulas; no full FEI counterexample.'}

def addressing_checks():
    out=[]
    for k in (1,2,3):
        n=k+(1<<k);N=1<<n;f=np.empty(N,dtype=np.int64)
        for x in range(N):
            address=x&((1<<k)-1);f[x]=1-2*((x>>(k+address))&1)
        W=fwht(f)[0];p=W*W
        assert np.count_nonzero(W)==1<<(2*k)
        assert set(abs(int(z)) for z in W if z)=={1<<(n-k)}
        Inum=sum(s.bit_count()*int(p[s]) for s in range(N))
        assert 2*Inum==(k+2)*N*N
        out.append({'k':k,'dimension':n,'support_size':1<<(2*k),'entropy_bits':2*k,'influence_twice':k+2})
    return out

def anisotropic_checks():
    rng=np.random.default_rng(SEED+1);roots=costs=profiles=pairs=0
    for n in range(4,10):
        N=1<<n;xx=np.arange(N)
        bits=((xx[:,None]>>np.arange(n))&1).astype(np.int64)
        for _ in range(40):
            coeff=np.zeros(N,dtype=np.uint8)
            allowed=[j for j in range(N) if j.bit_count()<=min(4,n)]
            chosen=rng.choice(allowed,size=min(len(allowed),int(rng.integers(1,15))),replace=False);coeff[chosen]=1
            table=anf(coeff)[0];A=np.flatnonzero(table);assert len(A)>0;roots+=1
            for rep in range(3):
                c=rng.integers(0,8,size=n);moncost=bits@c
                D=int(moncost[coeff!=0].max());threshold=int(c.sum())-D;costs+=1
                marginal=bits[A].sum(axis=0)
                assert int(c@np.abs(len(A)-2*marginal))<=D*len(A)
                for b in rng.choice(N,4,replace=False):
                    dist=moncost[A^int(b)];dist=np.sort(dist)
                    assert np.all(dist+dist[::-1]>=threshold)
                    assert 2*int(dist.sum())>=threshold*len(A)
                    profiles+=1;pairs+=len(A)
    return {'polynomial_cases':roots,'nonnegative_integer_cost_vectors':costs,'center_profiles':profiles,
            'ordered_pair_assertions':pairs,'scope':'Seeded weighted-degree tests including zero coordinate costs, dimensions 4--9.'}

def main():
    out={'status':'PASS','seed':SEED,'full_FEI_proved':False,'priority_cleared':False,
         'independent_audit':False,'proof_assistant_used':False,
         'polynomial_supports':polynomial_checks(),'bottom_walsh_layers':walsh_layer_checks(),
         'carry_barrier':carry_checks(),'addressing_calibration':addressing_checks(),
         'anisotropic_supports':anisotropic_checks()}
    out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text=json.dumps(out,indent=2)+'\n';Path(__file__).with_name('verification.json').write_text(text);print(text,end='')
if __name__=='__main__':main()
