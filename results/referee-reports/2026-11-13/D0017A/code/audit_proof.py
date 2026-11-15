#!/usr/bin/env python3
"""Independent numerical sanity checks of the proof's algebra, not a proof."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
if os.getpriority(os.PRIO_PROCESS,0)<10: os.setpriority(os.PRIO_PROCESS,0,10)
import json, pathlib
import numpy as np
rng=np.random.default_rng(17017)
checks=[]
for p in range(1,9):
    for rep in range(120):
        u=rng.integers(0,17,p+1)/16
        v=2+rng.integers(0,17,p+1)/16
        s=float(rng.uniform(.5,2))
        cov=s*np.maximum(0,np.minimum(v[:,None],v[None,:])-np.maximum(u[:,None],u[None,:]))
        prev=cov[:-1,:-1]
        actual=float(cov[-1,-1]-cov[-1,:-1]@np.linalg.pinv(prev,rcond=1e-12)@cov[:-1,-1])
        anchors_u=np.r_[0.,1.,u[:-1]]; anchors_v=np.r_[2.,3.,v[:-1]]
        rho_u=float(np.min(np.abs(anchors_u-u[-1])))
        rho_v=float(np.min(np.abs(anchors_v-v[-1])))
        bound=s*(rho_u+rho_v)/2
        def bridge(x,anchors):
            if np.min(np.abs(anchors-x))<1e-12: return 0.
            left=max(a for a in anchors if a<x); right=min(a for a in anchors if a>x)
            return (x-left)*(right-x)/(right-left)
        bridge_var=s*(bridge(u[-1],anchors_u)+bridge(v[-1],anchors_v))
        assert actual+1e-9>=bridge_var>=bound-1e-12
        checks.append(actual-bound)
kernels=[]
for n in (4,6,8,10):
    delta=2.**(-n)
    for alpha in (.3,.4,.49):
        eps=delta**alpha
        grid=np.arange(2**n+1)*delta
        for k in (0,1,3,7):
            au=np.r_[0.,1.,rng.choice(grid,k)]; av=np.r_[2.,3.,2+rng.choice(grid,k)]
            du=np.min(abs(grid[:,None]-au),axis=1)
            dv=np.min(abs((2+grid)[:,None]-av),axis=1)
            total=float(np.sum(eps**4/(eps**2+du[:,None]+dv[None,:])**2))
            norm=(k+2)**2*eps**4*delta**(-2)*(1+n)
            kernels.append({'n':n,'alpha':alpha,'previous_pairs':k,'normalized_kernel_sum':total/norm})
out={'seed':17017,'covariance_cases':len(checks),'smallest_actual_minus_lower_bound':min(checks),'max_normalized_kernel_sum':max(x['normalized_kernel_sum'] for x in kernels),'kernel_checks':kernels,'nice':os.getpriority(os.PRIO_PROCESS,0),'meaning':'Sanity checks only; the analytic arguments are in REPORT.md.'}
pathlib.Path('data/proof_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='kernel_checks'},indent=2))
