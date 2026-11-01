"""Test an enlarged classical random-permutation channel, not a DPP theorem."""
import json,itertools,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

def data(n):
    return ((np.arange(2**n)[:,None]>>np.arange(n))&1).astype(float)

def channel(n,perms,weights):
    bits=data(n);C=np.zeros((2**n,2**n))
    for perm,w in zip(perms,weights):
        to=(bits[:,perm]@(2**np.arange(n))).astype(int)
        C[to,np.arange(2**n)]+=w
    return C

def curv(p,C,bits):
    a=np.prod(np.where(bits,p,1-p),axis=1)
    s=(bits-p)/(p*(1-p))
    da=a[:,None]*s
    d2=a[:,None,None]*s[:,:,None]*s[:,None,:]
    d2[:,np.arange(len(p)),np.arange(len(p))]=0
    b=C@a;db=C@da;d2b=(C@d2.reshape(len(a),-1)).reshape(d2.shape)
    Q=db.T@(db/b[:,None])+np.einsum('s,sij->ij',np.log(b),d2b)
    return (Q+Q.T)/2

def main():
    rng=np.random.default_rng(20260917);out=[];start=time.time()
    for n,count in [(3,1000),(4,3000),(5,2000),(6,1000)]:
        bits=data(n);best=100;rec=None
        for k in range(count):
            m=2 if k%2==0 else 3
            perms=[rng.permutation(n) for _ in range(m)];weights=rng.dirichlet(np.ones(m))
            C=channel(n,perms,weights);p=rng.uniform(.003,.997,n)
            if k%3==0:p=1/(1+np.exp(rng.uniform(-8,8,n)))
            Q=curv(p,C,bits);w,V=np.linalg.eigh(Q)
            if w[0]<best:
                best=float(w[0]);rec=dict(n=n,k=k,p=p.tolist(),perms=[x.tolist() for x in perms],weights=weights.tolist(),min_curvature=best,direction=V[:,0].tolist())
            if best< -1e-6:break
        out.append(rec);print(json.dumps(rec),flush=True)
        Path('shuffle_search.json').write_text(json.dumps(dict(records=out,elapsed=time.time()-start),indent=2))

if __name__=='__main__':main()
