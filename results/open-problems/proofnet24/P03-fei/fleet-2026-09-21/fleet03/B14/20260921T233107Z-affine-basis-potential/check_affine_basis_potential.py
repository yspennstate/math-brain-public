#!/usr/bin/env python3
"""Finite falsification checks for fleet03/B14 affine-basis FEI potential.

Requires numpy.  This is finite evidence only; it does not prove the universal
selector inequality.
"""
from __future__ import annotations
import itertools, json, math
import numpy as np

def h2_np(p):
    p=np.asarray(p,dtype=float)
    out=np.zeros_like(p)
    m=(p>0)&(p<1)
    out[m]=-(p[m]*np.log2(p[m])+(1-p[m])*np.log2(1-p[m]))
    return out

def j_np(p):
    p=np.asarray(p,dtype=float)
    q=0.5+np.sqrt(np.maximum(0,p*(1-p)))
    return 1-h2_np(q)

def sylvester(n):
    H=np.array([[1]],dtype=np.int16)
    for _ in range(n): H=np.block([[H,H],[H,-H]])
    return H

def rank_gf2(vecs,n):
    piv=[0]*n; r=0
    for v in vecs:
        x=int(v)
        while x:
            k=x.bit_length()-1
            if piv[k]: x^=piv[k]
            else: piv[k]=x; r+=1; break
    return r

def bases_unordered(n):
    return [c for c in itertools.combinations(range(1,1<<n),n) if rank_gf2(c,n)==n]

def all_state(n,fixed_global_sign=False):
    N=1<<n; M=1<<(N-1) if fixed_global_sign else 1<<N
    masks=np.arange(M,dtype=np.uint64)
    if fixed_global_sign:
        T=np.zeros((M,N),dtype=np.int8)
        for x in range(1,N): T[:,x]=((masks>>(x-1))&1).astype(np.int8)
        codes=(masks<<1).astype(np.uint64)
    else:
        T=((masks[:,None]>>np.arange(N,dtype=np.uint64))&1).astype(np.int8); codes=masks
    f=1-2*T; W=f@sylvester(n).T; p=(W.astype(float)/N)**2
    with np.errstate(divide='ignore',invalid='ignore'):
        ent=np.where(p>0,-p*np.log2(p),0).sum(axis=1)
    inds=np.arange(N)
    infs=np.stack([np.mean(T != T[:,inds^v],axis=1) for v in range(1,N)],axis=1)
    weights=j_np(infs); bases=bases_unordered(n)
    bi=np.array([[v-1 for v in b] for b in bases],dtype=int)
    sums=np.zeros((M,len(bases)),dtype=float)
    for k in range(n): sums += weights[:,bi[:,k]]
    arg=np.argmin(sums,axis=1); pi=sums[np.arange(M),arg]
    return {'T':T,'codes':codes,'ent':ent,'pi':pi,'weights':weights,'bases':bases,'arg':arg,'infs':infs}

def exhaustive_n4():
    s3=all_state(3,False); s4=all_state(4,True)
    T=s4['T']; ent=s4['ent']; pi=s4['pi']; ent3=s3['ent']; pi3=s3['pi']
    best=np.full(len(ent),np.inf); bestell=np.zeros(len(ent),dtype=np.int16)
    powers=(1<<np.arange(8,dtype=np.uint64))
    for ell in range(1,16):
        pivot=(ell & -ell).bit_length()-1; kb=[]
        for i in range(4):
            if i==pivot: continue
            v=1<<i
            if (ell>>i)&1: v ^= 1<<pivot
            kb.append(v)
        idxs=[]
        for b in (0,1):
            x0=(1<<pivot) if b else 0; arr=[]
            for u in range(8):
                x=x0
                for k,v in enumerate(kb):
                    if (u>>k)&1: x^=v
                arr.append(x)
            idxs.append(arr)
        c0=(T[:,idxs[0]].astype(np.uint64)*powers).sum(axis=1).astype(int)
        c1=(T[:,idxs[1]].astype(np.uint64)*powers).sum(axis=1).astype(int)
        dH=ent-(ent3[c0]+ent3[c1])/2; dP=pi-(pi3[c0]+pi3[c1])/2
        r=np.full(len(ent),np.inf); np.divide(dH,dP,out=r,where=dP>1e-12)
        improve=r<best; best[improve]=r[improve]; bestell[improve]=ell
    valid=pi>1e-12
    assert int(valid.sum())==32752 and int(np.sum(valid & ~np.isfinite(best)))==0
    imax=int(np.argmax(np.where(valid,best,-np.inf)))
    return {'nonterminal_functions':int(valid.sum()),'no_positive_drop_selector':int(np.sum(valid & ~np.isfinite(best))),
            'max_best_ratio':float(best[imax]),'maximizer_truth_mask':int(s4['codes'][imax]),
            'maximizer_H':float(ent[imax]),'maximizer_Pi':float(pi[imax]),'best_query_mask':int(bestell[imax])}

def fwht(a):
    a=np.array(a,dtype=float,copy=True); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            x=a[i:i+h].copy(); y=a[i+h:i+2*h].copy(); a[i:i+h]=x+y; a[i+h:i+2*h]=x-y
        h*=2
    return a

def entropy_table(tab):
    W=fwht(tab)/len(tab); p=W*W; m=p>0
    return float(-(p[m]*np.log2(p[m])).sum())

def basis_add(piv,v):
    x=v
    for b in piv: x=min(x,x^b)
    if x==0: return piv,False
    q=piv+[x]; out=[]
    for y in sorted(q,reverse=True):
        z=y
        for b in out: z=min(z,z^b)
        if z: out.append(z)
    return out,True

def pi_table(tab):
    N=len(tab); n=N.bit_length()-1; idx=np.arange(N); cand=[]
    for v in range(1,N):
        p=float(np.mean(tab != tab[idx^v])); cand.append((float(j_np(np.array([p]))[0]),v,p))
    cand.sort(); piv=[]; pick=[]
    for w,v,p in cand:
        new,ok=basis_add(piv,v)
        if ok:
            piv=new; pick.append((w,v,p))
            if len(pick)==n: break
    return sum(w for w,_,_ in pick),pick

def restrict_parity(tab,ell,b):
    n=len(tab).bit_length()-1; pivot=(ell & -ell).bit_length()-1; kb=[]
    for i in range(n):
        if i==pivot: continue
        v=1<<i
        if (ell>>i)&1: v^=1<<pivot
        kb.append(v)
    out=np.empty(1<<(n-1),dtype=np.int8); x0=(1<<pivot) if b else 0
    for u in range(1<<(n-1)):
        x=x0
        for k,v in enumerate(kb):
            if (u>>k)&1: x^=v
        out[u]=tab[x]
    return out

def basis_query_ratios(tab):
    H=entropy_table(tab); P,pick=pi_table(tab); B=[v for _,v,_ in pick]; n=len(B); rows=[]
    for qi in range(n):
        childs=[]
        for bit in (0,1):
            vals=[]
            for u in range(1<<(n-1)):
                x=0; k=0
                for r,v in enumerate(B):
                    z=bit if r==qi else ((u>>k)&1)
                    if r!=qi: k+=1
                    if z: x^=v
                vals.append(tab[x])
            childs.append(np.array(vals,dtype=np.int8))
        dH=H-sum(entropy_table(c) for c in childs)/2
        dP=P-sum(pi_table(c)[0] if len(c)>1 else 0.0 for c in childs)/2
        rows.append((dH/dP if dP>1e-12 else math.inf,dH,dP,B[qi]))
    return H,P,min(rows),rows

def one_point(n):
    t=np.ones(1<<n,dtype=np.int8); t[0]=-1; return t

def majority(n):
    return np.array([-1 if x.bit_count()>=(n+1)//2 else 1 for x in range(1<<n)],dtype=np.int8)

def tribes2(m):
    return np.array([-1 if any(((x>>(2*k))&3)==3 for k in range(m)) else 1 for x in range(1<<(2*m))],dtype=np.int8)

def addressing(k):
    n=k+(1<<k); vals=[]
    for x in range(1<<n):
        a=x&((1<<k)-1); vals.append(-1 if ((x>>(k+a))&1) else 1)
    return np.array(vals,dtype=np.int8)

def bent_plus_flip(m):
    assert m%2==0
    n=m+1; h=m//2; out=[]
    for x in range(1<<n):
        z=(x>>m)&1; lo=x&((1<<h)-1); hi=(x>>h)&((1<<h)-1)
        val=-1 if ((lo&hi).bit_count()&1) else 1
        if z and (x&((1<<m)-1))==0: val=-val
        out.append(val)
    return np.array(out,dtype=np.int8)

def structured_checks():
    ans={'one_point':{},'tribes2':{},'addressing':{},'majority':{},'bent_plus_flip':[]}
    for n in (3,4,5,6,8,10): ans['one_point'][str(n)]=basis_query_ratios(one_point(n))[2][0]
    for m in (2,3,4,5): ans['tribes2'][str(m)]=basis_query_ratios(tribes2(m))[2][0]
    for k in (2,3): ans['addressing'][str(k)]=basis_query_ratios(addressing(k))[2][0]
    for n in (5,7,9): ans['majority'][str(n)]=basis_query_ratios(majority(n))[2][0]
    for m in (2,4,6,8,10):
        tab=bent_plus_flip(m); H,P,best,_=basis_query_ratios(tab); ell=1<<m
        c0=restrict_parity(tab,ell,0); c1=restrict_parity(tab,ell,1)
        dH=H-(entropy_table(c0)+entropy_table(c1))/2; dP=P-(pi_table(c0)[0]+pi_table(c1)[0])/2
        ans['bent_plus_flip'].append({'m':m,'H_over_Pi':H/P,'best_min_basis_query_ratio':best[0],'appended_z_query_ratio':dH/dP})
    return ans

if __name__=='__main__':
    out={'exhaustive_n4':exhaustive_n4(),'structured':structured_checks()}
    assert abs(out['exhaustive_n4']['max_best_ratio']-1.4541800170075352)<1e-12
    assert out['exhaustive_n4']['no_positive_drop_selector']==0
    print(json.dumps(out,indent=2,sort_keys=True))
