import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import time, json
from pathlib import Path
import numpy as np

rng = np.random.default_rng(19102)
start = time.time()
rows = []
max_errors = {'vectorization': 0., 'similarity_bound': 0., 'diagonalizer_bound': 0., 'disk_inclusion': 0.}
for n in [1, 2, 4, 8]:
    for sample in range(12):
        x = (rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2*n)
        y = (rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2*n)
        eig, v = np.linalg.eig(x)
        v = v / np.linalg.norm(v,axis=0)
        inv = np.linalg.inv(v)
        overlaps = np.linalg.norm(inv,axis=1)
        w = n * float(np.sum(overlaps**2))
        cond = float(np.linalg.cond(v))
        max_errors['diagonalizer_bound'] = max(max_errors['diagonalizer_bound'],cond**2-w)
        assert cond**2 <= w+1e-9
        for k in [1,2,3,4]:
            xk = np.linalg.matrix_power(x,k)
            tmap = np.kron(np.eye(n),xk)+np.kron(xk.T,np.eye(n))
            sm = float(np.linalg.svd(tmap,compute_uv=False)[-1])
            delta = float(np.min(np.abs(eig[:,None]**k+eig[None,:]**k)))
            bound = delta/w
            err = float(np.linalg.norm(tmap@y.reshape(-1,order='F')-(xk@y+y@xk).reshape(-1,order='F')))
            max_errors['vectorization'] = max(max_errors['vectorization'],err)
            max_errors['similarity_bound'] = max(max_errors['similarity_bound'],bound-sm)
            assert err<1e-10 and sm>=bound-1e-9
            rows.append({'n':n,'k':k,'sample':sample,'delta':delta,'W':w,'map_smin':sm,'proved_lower_bound':bound})
        # Test the explicit resolvent disks used before Fatou.
        radii=[]
        for i in range(n):
            gaps=np.abs(eig-eig[i])
            rho=.5 if n==1 else min(.5,float(np.min(np.delete(gaps,i)))/4)
            bi=sum(float(overlaps[j])/(float(gaps[j])-rho) for j in range(n) if j!=i)
            radii.append((rho,bi))
        eps=min(1e-4,min(rho/(2*float(overlaps[i])) for i,(rho,bi) in enumerate(radii)))
        for i,(rho,bi) in enumerate(radii):
            r=eps*float(overlaps[i])/(1+eps*bi)
            assert r<=rho
            for angle in [0.,1.,2.]:
                z=eig[i]+.9*r*np.exp(1j*angle)
                sm=float(np.linalg.svd(x-z*np.eye(n),compute_uv=False)[-1])
                max_errors['disk_inclusion']=max(max_errors['disk_inclusion'],sm-eps)
                assert sm<=eps+1e-10
        if time.time()-start>90:
            raise RuntimeError('Research job time cap reached; no further samples.')

out={'seed':19102,'seconds':time.time()-start,'matrix_space_checks':len(rows),'resolvent_disk_checks':sum(12*n*3 for n in [1,2,4,8]),'max_positive_violations':max_errors,'results':rows,'scope':'Deterministic bookkeeping diagnostics, not a Monte Carlo proof of the tail.'}
Path('retry_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps({k:val for k,val in out.items() if k!='results'},indent=2))
