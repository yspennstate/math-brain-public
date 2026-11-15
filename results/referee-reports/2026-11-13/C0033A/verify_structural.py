"""Check conditional-kernel lifting and the sharp fourth-order coefficient."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json
from pathlib import Path
import numpy as np
from scipy.linalg import block_diag
from dpp import probabilities,random_kernel,stats,basis

rng=np.random.default_rng(330016);root=Path(__file__).resolve().parent;out={}
errors=[];chain_errors=[]
for n in (3,4,6):
    for cx in (False,True):
        q=random_kernel(rng,n,cx,'uniform');p,_=probabilities(q)
        c=list(range(2,n));qc=q[np.ix_(c,c)];pc,_=probabilities(qc)
        hs=[]
        for t in range(1<<(n-2)):
            m=qc.copy()
            for i in range(n-2):m[i,i]-=0 if t>>i&1 else 1
            qb=q[:2,:2]-q[:2,2:]@np.linalg.solve(m,q[2:,:2]);qb=(qb+qb.conj().T)/2
            pp,_=probabilities(qb)
            actual=np.array([p[(t<<2)|s]/pc[t] for s in range(4)])
            errors.append(float(np.max(abs(pp-actual))))
            hs.append(stats(qb)[0])
        chain=stats(qc)[0]+np.dot(pc,hs)
        chain_errors.append(float(abs(chain-stats(q)[0])))
out['conditioning']={'cases':6,'max_atom_error':max(errors),'max_entropy_chain_error':max(chain_errors)}
assert max(errors)<1e-12 and max(chain_errors)<1e-12

rows=[]
for n,k in ((3,1),(4,2),(5,2),(6,3),(8,4)):
    for cx in (False,True):
        ratios=[];svals=[]
        for trial in range(40):
            q=block_diag(random_kernel(rng,k,cx,'uniform'),random_kernel(rng,n-k,cx,'uniform'))
            z=rng.normal(size=(k,n-k))
            if cx:z=z+1j*rng.normal(size=(k,n-k))
            z=z/(np.sqrt(2)*np.linalg.norm(z));a=np.zeros((n,n),complex);a[:k,k:]=z;a[k:,:k]=z.conj().T
            p,m=probabilities(q);inv=np.linalg.inv(m)
            c=np.einsum('sij,jk->sik',inv,a)
            tr=np.trace(c,axis1=1,axis2=2)
            r=p/2*(tr**2-np.einsum('sij,sji->s',c,c)).real
            ss=float(np.sum(r*r/p));bound=16*float(np.sum(abs(z)**4))
            ratios.append(ss/bound);svals.append(ss)
        # Equality: all entries of B have modulus 1/sqrt(2 k(n-k)).
        q=np.eye(n)/2;z=np.full((k,n-k),1/np.sqrt(2*k*(n-k)));a=np.zeros((n,n),complex)
        a[:k,k:]=z;a[k:,:k]=z.T;p,m=probabilities(q);inv=np.linalg.inv(m);c=np.einsum('sij,jk->sik',inv,a)
        r=-p/2*np.einsum('sij,sji->s',c,c).real
        coef=float(np.sum(r*r/p)/2)
        assert min(ratios)>1-1e-10 and abs(coef-2/(k*(n-k)))<1e-12
        rows.append({'n':n,'k':k,'field':'complex' if cx else 'real','trials':40,'minimum_sharp_bound_ratio':min(ratios),'equality_quartic_coefficient':coef,'sharp_coefficient':2/(k*(n-k))})
out['quartic']=rows
(root/'data/structural_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
