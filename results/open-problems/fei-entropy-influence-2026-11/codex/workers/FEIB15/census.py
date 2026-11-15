#!/usr/bin/env python3
"""Exact integer structural census; floating point is used only for entropies.

Table t has f(x)=(-1)^((t>>x)&1); subset masks use the same coordinate order.
NA checks every pair of nonconstant increasing indicator events on disjoint
coordinate sets. Layer cake makes this equivalent to the full NA definition.
"""
import itertools, json, math, os, resource, time
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np

def spectrum(n):
    m=1<<n
    t=np.arange(1<<m,dtype=np.uint64)
    a=(1-2*((t[:,None]>>np.arange(m,dtype=np.uint64))&1).astype(np.int64))
    for b in range(n):
        v=a.reshape(len(t),-1,2,1<<b)
        x=v[:,:,0,:].copy(); y=v[:,:,1,:].copy()
        v[:,:,0,:]=x+y; v[:,:,1,:]=x-y
    return a, a*a

def upsets(block,n):
    coords=[i for i in range(n) if block>>i&1]
    k=len(coords); m=1<<k
    out=[]
    for t in range(1,(1<<m)-1):
        if all(not(t>>s&1) or all(t>>(s|(1<<i))&1 for i in range(k) if not s>>i&1) for s in range(m)):
            indices=[]
            for s in range(1<<n):
                z=sum(((s>>i)&1)<<j for j,i in enumerate(coords))
                if t>>z&1: indices.append(s)
            out.append(tuple(indices))
    return out

def run(n):
    start=time.monotonic(); a,w=spectrum(n); N,m=w.shape; D=m*m
    assert np.all(w.sum(axis=1)==D)
    masks=list(range(m)); deg=np.array([s.bit_count() for s in masks])
    inf=np.array([w[:,[s for s in masks if s>>i&1]].sum(axis=1) for i in range(n)]).T
    It=(w*deg).sum(axis=1); I=It/D; p=w/D
    with np.errstate(divide='ignore',invalid='ignore'):
        H=np.where(p>0,-p*np.log2(p),0).sum(axis=1)
    E=np.zeros((N,n)); G=np.zeros(N)
    for i in range(n):
        lo=[s for s in masks if not s>>i&1]; hi=[s|(1<<i) for s in lo]
        x=p[:,lo]; y=p[:,hi]; z=x+y
        with np.errstate(divide='ignore',invalid='ignore'):
            E[:,i]=np.where(x>0,x*np.log2(np.divide(z,x,where=x>0,out=np.ones_like(x))),0).sum(axis=1)+np.where(y>0,y*np.log2(np.divide(z,y,where=y>0,out=np.ones_like(y))),0).sum(axis=1)
            G+=np.where(y>0,y*np.log2(np.divide(z,y,where=y>0,out=np.ones_like(y))),0).sum(axis=1)
    Em=E.sum(axis=1)
    # Full global lattice definition, including all zero-mass pairs.
    lsub=np.ones(N,bool); lsuper=np.ones(N,bool)
    for s in masks:
        for t in range(s+1,m):
            if (s&t)==s or (s&t)==t: continue
            x=w[:,s]*w[:,t]; y=w[:,s&t]*w[:,s|t]
            lsub &= x>=y; lsuper &= x<=y
    pairnc=np.ones(N,bool)
    for i in range(n):
        for j in range(i+1,n):
            both=w[:,[s for s in masks if s>>i&1 and s>>j&1]].sum(axis=1)
            pairnc &= both*D<=inf[:,i]*inf[:,j]
    # Check all increasing events on disjoint blocks (not just pairs of bits).
    na=np.ones(N,bool); event_cache={b:upsets(b,n) for b in range(1,m)}
    checks=0; na_witness=None
    for b in range(1,m):
        for c in range(b+1,m):
            if b&c: continue
            for A in event_cache[b]:
                ma=w[:,A].sum(axis=1)
                for B in event_cache[c]:
                    mb=w[:,B].sum(axis=1); AB=tuple(sorted(set(A)&set(B)))
                    mab=w[:,AB].sum(axis=1) if AB else np.zeros(N,dtype=np.int64)
                    fail=mab*D>ma*mb
                    if na_witness is None and np.any(fail & pairnc):
                        t=int(np.flatnonzero(fail & pairnc)[0])
                        na_witness=dict(table=t,blocks=[b,c],events=[A,B],covariance_numerator=int((mab*D-ma*mb)[t]),denominator=D*D)
                    na &= ~fail; checks+=1
    assert np.all(~na|pairnc)
    ranks=np.array([w[:,deg==k].sum(axis=1) for k in range(n+1)]).T
    ranklc=np.ones(N,bool); ulc=np.ones(N,bool); noholes=np.ones(N,bool)
    for k in range(1,n):
        ranklc &= ranks[:,k]**2>=ranks[:,k-1]*ranks[:,k+1]
        ulc &= ranks[:,k]**2*math.comb(n,k-1)*math.comb(n,k+1)>=ranks[:,k-1]*ranks[:,k+1]*math.comb(n,k)**2
        noholes &= ~((ranks[:,:k].sum(axis=1)>0)&(ranks[:,k]==0)&(ranks[:,k+1:].sum(axis=1)>0))
    ranklc &= noholes; ulc &= noholes
    # Independence of bits, with degenerate marginals allowed, checked exactly.
    prod=np.ones(N,bool)
    for s in masks:
        rhs=np.ones(N,dtype=np.int64)
        for i in range(n): rhs*=inf[:,i] if s>>i&1 else D-inf[:,i]
        prod &= w[:,s]*(D**(n-1))==rhs
    # Fourier input classification is literal monotonicity in 0/1 inputs.
    mono=np.ones(N,bool)
    tables=np.arange(N,dtype=np.uint64)
    for i in range(n):
        for x in masks:
            if not x>>i&1:
                mono &= ((tables>>np.uint64(x))&1)<=((tables>>np.uint64(x|(1<<i)))&1)
    positive=I>0
    def extremum(v,mask=positive):
        ii=np.flatnonzero(mask); t=int(ii[np.argmax(v[ii])])
        return dict(table=t,value=float(v[t]),I=float(I[t]),H=float(H[t]),erasure=float(Em[t]))
    ratio=np.divide(Em,I,out=np.zeros(N),where=positive)
    with np.errstate(divide='ignore',invalid='ignore'):
        jensen=np.where(positive,I*np.log2(math.e*n/np.where(positive,I,1)),0)
    checks_num={
        'max_erasure_minus_H_bits':float(np.max(Em-H)),
        'max_erasure_minus_jensen_bits':float(np.max(Em-jensen)),
        'min_erasure_minus_G_bits':float(np.min(Em-G)),
        'max_erasure_minus_G_minus_I_over_ln2_bits':float(np.max(Em-G-I/math.log(2)))
    }
    classes={'NA':na,'pairwise_NC':pairnc,'global_log_submodular':lsub,'global_log_supermodular':lsuper,'rank_log_concave_no_holes':ranklc,'ULC_no_holes':ulc,'product':prod}
    results=dict(n=n,functions=N,denominator=D,na_event_pair_checks=checks,counts={k:int(v.sum()) for k,v in classes.items()},monotone_counts={k:int((v&mono).sum()) for k,v in classes.items()},monotone_total=int(mono.sum()),max_erasure_over_I=extremum(ratio),max_erasure_over_I_NA=extremum(ratio,na&positive),pairwise_NC_not_NA_witness=na_witness,numerical_checks=checks_num,NA_nonproduct_tables=[int(t) for t in np.flatnonzero(na&~prod)[:20]],log_submodular_nonproduct_tables=[int(t) for t in np.flatnonzero(lsub&~prod)[:20]],seconds=time.monotonic()-start)
    np.savez_compressed(f'census_n{n}.npz',weights=w,NA=na,pairwise_NC=pairnc,logsub=lsub,logsuper=lsuper,ranklc=ranklc,ULC=ulc,product=prod,erasure=Em,I=I,H=H)
    return results

if __name__=='__main__':
    allresults=[run(n) for n in range(1,5)]
    out=dict(convention='f(x)=(-1)^((table>>x)&1), characters=(-1)^popcount(S&x)',census=allresults,max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with open('census.json','w') as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))
