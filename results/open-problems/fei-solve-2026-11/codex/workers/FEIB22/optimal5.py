"""Exact n=25 subset shortest paths, using verified geometric symmetries."""
import study as s
import numpy as np
import time
import sys

L=5;n=25;t=time.time();mu=s.spectrum(L)
def orbit(k):
    r,c=divmod(k,L)
    return sorted({r*L+c,c*L+r,(L-1-r)*L+L-1-c,(L-1-c)*L+L-1-r})

# Verify both generating permutations on every spectral coefficient.
checks=[]
for name,perm in [('transpose',[c*L+r for r in range(L) for c in range(L)]),('half_turn',[n-1-k for k in range(n)])]:
    err=0.
    for a in range(0,1<<n,1<<18):
        idx=np.arange(a,min(a+(1<<18),1<<n),dtype=np.uint32);mapped=np.zeros_like(idx)
        for k,j in enumerate(perm):mapped|=((idx>>k)&1)<<j
        err=max(err,float(abs(mu[idx]-mu[mapped]).max()))
    assert err<1e-15
    checks.append(dict(symmetry=name,maximum_error=err))

done=[];seen=set()
for i in [12]+list(range(n)):
    if i in seen:continue
    orb=orbit(i);seen.update(orb)
    start=time.time();out=np.zeros(3);o1=np.zeros(n-1,np.int32);o2=o1.copy()
    s.LIB.optimal(mu,n,i,1,out,o1,o2)
    # Independently regroup the actual squared spectrum by returned orders.
    for rank,order,target in [(1,o1,out[1]),(2,o2,out[2])]:
        p,q=s.spectral_witness(mu,L,i,order,rank=rank)
        assert abs(float(s.phi(p,q).sum()/q.sum())-target)<1e-9
    row=dict(i=i,orbit=orb,influence=float(out[0]),best_nested=float(out[1]),best_two=float(out[2]),nested_order=o1.tolist(),two_order=o2.tolist(),seconds=time.time()-start,se=0)
    done.append(row)
    s.save('optimal_L5.json',dict(L=L,symmetry_checks=checks,rows=done,complete=len(seen)==n,seconds=time.time()-t))
    print('OPTIMAL5',i,orb,out.tolist(),row['seconds'],flush=True)
    if len(sys.argv)>1 and sys.argv[1]=='centre-only':break
