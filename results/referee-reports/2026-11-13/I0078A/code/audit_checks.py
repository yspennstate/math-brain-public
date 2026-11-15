#!/usr/bin/env python3
"""Independent arithmetic checks used in REPORT.md; no proof by simulation."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
import sys, json
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.special import gamma
from periodic_check import kernel

root=Path(__file__).resolve().parents[1]
assert os.getpriority(os.PRIO_PROCESS,0)>=10
mp.mp.dps=40
kernel_rows=[]
for n in [32,64,128]:
    for t in [.00001,.001,.05,.25,.5]:
        t_mp=mp.mpf(str(t)); a_mp=mp.mpf('.5')
        exact=-mp.mpf(n)**a_mp*(mp.zeta(-a_mp,t_mp)+mp.zeta(-a_mp,1-t_mp)-2*mp.zeta(-a_mp))
        got=float(kernel(np.array([n*t]),n)[0])
        kernel_rows.append({'N':n,'t':t,'absolute_error':float(abs(exact-got))})
assert max(r['absolute_error'] for r in kernel_rows)<1e-10

resistance_rows=[]
for n in [16,32,64]:
    for a in [.25,.5,.75]:
        idx=np.arange(n)
        d=np.abs(idx[:,None]-idx[None,:]); d=np.minimum(d,n-d)
        w=np.zeros((n,n)); w[d>0]=d[d>0].astype(float)**(a-2)
        lap=np.diag(w.sum(axis=1))-w
        inverse=np.linalg.inv(lap[1:,1:])
        eigen=np.array([sum(w[0,r]*(1-np.cos(2*np.pi*m*r/n)) for r in range(1,n)) for m in range(1,n)])
        spectral=np.array([sum(abs(1-np.exp(2j*np.pi*np.arange(1,n)*i/n))**2/eigen)/n for i in range(1,n)])
        error=float(np.max(abs(np.diag(inverse)-spectral)))
        assert error<1e-10
        eta=min(3**(2-a)/24,1-np.sqrt(3)/2)
        printed_bound=2**(3-a)/(a*eta)
        assert spectral.max()<printed_bound
        resistance_rows.append({'N':n,'a':a,'max_resistance':float(spectral.max()),'spectral_vs_inverse_error':error,'printed_upper_bound':printed_bound})

# Independent finite-difference verification of the interval-background Hessian.
n=6; a=.5; x=np.arange(n)-(n-1)/2+np.array([.1,-.05,.07,-.08,.02,-.03])
def energy(y):
    i,j=np.triu_indices(n,1)
    return -np.abs(y[j]-y[i])**a @ np.ones(len(i)) + np.sum(((y+n/2)**(a+1)+(n/2-y)**(a+1))/(a+1))
hessian=np.zeros((n,n))
for i in range(n):
    for j in range(i+1,n):
        c=a*(1-a)*abs(x[j]-x[i])**(a-2)
        hessian[i,i]+=c;hessian[j,j]+=c;hessian[i,j]-=c;hessian[j,i]-=c
hessian+=np.diag(a*((x+n/2)**(a-1)+(n/2-x)**(a-1)))
step=1e-4; numeric=np.zeros_like(hessian)
for i in range(n):
    ei=np.eye(n)[i]*step
    numeric[i,i]=(energy(x+ei)-2*energy(x)+energy(x-ei))/step**2
    for j in range(i+1,n):
        ej=np.eye(n)[j]*step
        numeric[i,j]=numeric[j,i]=(energy(x+ei+ej)-energy(x+ei-ej)-energy(x-ei+ej)+energy(x-ei-ej))/(4*step**2)
hessian_error=float(np.max(abs(numeric-hessian)))
assert hessian_error<1e-5
result={'kernel':kernel_rows,'resistance':resistance_rows,'interval_hessian_error':hessian_error,'nice':os.getpriority(os.PRIO_PROCESS,0),'threads':1}

# Direct, piecewise-exact check of the deterministic convolution/energy bound.
def discrepancy_integral(y, n, length):
    lo, hi=-n/2,n/2
    events=np.unique(np.r_[lo-length,lo,hi-length,hi,y,y-length])
    left,right=events[:-1],events[1:]
    width=right-left; mid=(left+right)/2
    counts=((y[:,None]>mid)&(y[:,None]<=mid+length)).sum(axis=0)
    def overlap(t): return np.maximum(0,np.minimum(t+length,hi)-np.maximum(t,lo))
    residual=counts-overlap(mid)
    slope=(overlap(mid+width/4)-overlap(mid-width/4))/(width/2)
    return float(np.sum(width*residual**2+width**3*slope**2/12))

rng=np.random.default_rng(780078)
bound_rows=[]
for n in [8,32]:
    for a in [.25,.5,.75]:
        cs=2*gamma(1+a)*np.sin(np.pi*a/2)
        gamma_form=gamma((1+a)/2)/(-gamma(-a/2))*np.sqrt(np.pi)*2**(1+a)
        assert abs(cs-gamma_form)<1e-12
        b_s=2**(2+a)/cs
        for initial in ['lattice','uniform']:
            y=np.arange(n)-(n-1)/2 if initial=='lattice' else rng.uniform(-n/2,n/2,n)
            i,j=np.triu_indices(n,1)
            energy_n=-np.sum(abs(y[i]-y[j])**a)+np.sum(((y+n/2)**(a+1)+(n/2-y)**(a+1))/(a+1))-n**(a+2)/((a+1)*(a+2))
            assert energy_n>0
            for length in [1.,2.,4.]:
                integral=discrepancy_integral(y,n,length)
                upper=b_s*length**(1-a)*energy_n
                assert integral<=upper+1e-8
                bound_rows.append({'N':n,'a':a,'initial':initial,'L':length,'discrepancy_integral':integral,'upper_bound':upper})
result['deterministic_variance_bound']=bound_rows
(root/'data'/'independent_audit_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'kernel_max_error':max(r['absolute_error'] for r in kernel_rows),'resistance_max_error':max(r['spectral_vs_inverse_error'] for r in resistance_rows),'interval_hessian_max_error':hessian_error,'deterministic_variance_bound_cases':len(bound_rows)}))
