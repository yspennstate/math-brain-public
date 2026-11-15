"""Independent finite-n beta=2 CDF check using quadrature projection kernels.

This is not an evaluation of the limiting Painleve hierarchy distribution.
The quadrature approximation is checked by doubling the number of nodes.
"""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
import csv,json,resource
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
from scipy.linalg import cholesky
from models import quartic_U

@np.errstate(over='ignore',divide='ignore',invalid='ignore',under='ignore')
def projection(n,nodes):
    z,w=roots_legendre(nodes)
    x=-3.5+(z+1)*4.75;w=w*4.75
    exponent=-n*quartic_U(x);exponent-=np.max(exponent)
    # Take the square root BEFORE exponentiation; exp(exponent) underflows
    # near the critical edge at n=256 even when its square root is representable.
    root_weight=np.sqrt(w)*np.exp(exponent/2)
    Q=np.empty((nodes,n));Q[:,0]=root_weight/np.linalg.norm(root_weight)
    for j in range(n-1):
        v=x*Q[:,j]
        # Full reorthogonalization makes the finite projection unambiguous.
        for _ in range(2):
            v-=Q[:,:j+1]@(Q[:,:j+1].T@v)
        if not np.isfinite(v).all():raise FloatingPointError('Nonfinite projection vector')
        Q[:,j+1]=v/np.linalg.norm(v)
    orth_error=float(np.max(abs(Q.T@Q-np.eye(n))))
    if not np.isfinite(Q).all() or not orth_error<1e-10:
        raise FloatingPointError('Projection lost orthogonality')
    return x,Q,orth_error

@np.errstate(over='ignore',divide='ignore',invalid='ignore',under='ignore')
def cdf(x,Q,threshold):
    right=Q[x>threshold]
    G=np.eye(Q.shape[1])-right.T@right
    if not np.isfinite(G).all():raise FloatingPointError('Nonfinite restricted Gram matrix')
    try:
        L=cholesky(G,lower=True,check_finite=True)
    except np.linalg.LinAlgError:
        # Only the far left numerical tail may lose positive definiteness.
        if np.linalg.eigvalsh(G).min() < -1e-10:raise
        return 0.
    return float(np.clip(np.exp(2*np.log(np.diag(L)).sum()),0,1))

if __name__=='__main__':
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    n=256;c=6**(2/7)
    grid=np.linspace(-9,2,45)
    vals=[];ortho=[]
    for nodes in [4096,8192]:
        x,Q,err=projection(n,nodes);ortho.append(err)
        vals.append([cdf(x,Q,2+s/(c*n**(2/7))) for s in grid])
        print('projection',nodes,'orthogonality',err,flush=True)
    rows=list(csv.DictReader(Path('data/quartic_banded_eigenvalues.csv').open()))
    sample=np.array([float(r['cv_scaled_top0']) for r in rows if r['n']==str(n) and r['beta']=='2'])
    empirical=np.array([np.mean(sample<=s) for s in grid])
    out=dict(n=n,nodes=[4096,8192],interval=[-3.5,6.0],orthogonality=ortho,
             cdf_max_grid_difference=float(np.max(abs(np.array(vals[0])-vals[1]))),
             empirical_max_grid_difference=float(np.max(abs(empirical-vals[1]))),
             samples=len(sample),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with Path('data/finite_unitary_cdf.csv').open('w',newline='') as f:
        wr=csv.writer(f);wr.writerow(['cv_scaled_s','cdf_4096','cdf_8192','hmc_empirical'])
        wr.writerows(zip(grid,*vals,empirical))
    Path('data/finite_unitary_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
