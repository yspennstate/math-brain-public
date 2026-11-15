#!/usr/bin/env python3
"""Independent numerical audits of normalizations and load-bearing inequalities."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[key]='1'
import json, pathlib
import numpy as np
from scipy.linalg import eigh_tridiagonal, eigh
from scipy.integrate import quad
from scipy.special import ai_zeros, airy
from simulate import gue

rng=np.random.default_rng(46009)
records={}
# Check dense generation via ensemble entries, independent of eigenvalue scaling.
h=np.stack([gue(rng,5) for _ in range(20000)])
records['gue_diag_variance']=float(h[:,0,0].real.var())
records['gue_off_abs2_mean']=float(np.mean(abs(h[:,0,1])**2))
assert abs(records['gue_diag_variance']-1)<.04
assert abs(records['gue_off_abs2_mean']-1)<.04
# Check the exact radial transition moments against the analytic conditional law.
n=40;d=22;q0=19.;dt=.12;rho=np.exp(-dt);sig=-np.expm1(-2*dt)
q=sig*rng.noncentral_chisquare(d,rho*rho*q0/sig,size=200000)
mean=rho*rho*q0+sig*d
variance=2*sig*sig*d+4*sig*rho*rho*q0
records['radial_conditional_mean']={'empirical':float(q.mean()),'exact':float(mean)}
records['radial_conditional_variance']={'empirical':float(q.var()),'exact':float(variance)}
assert abs(q.mean()-mean)<.05
assert abs(q.var()-variance)/variance<.015
# Finite differences in the original Gaussian coordinates, not the b-coordinate formula.
n=10;a=rng.normal(size=n);z=[rng.normal(size=2*(n-i)) for i in range(1,n)]
b=np.array([np.linalg.norm(x)/np.sqrt(2) for x in z])
lam,v=eigh_tridiagonal(a,b,select='i',select_range=(n-1,n-1));v=v[:,0];p=v*v
predicted=float(np.sum(p*p)+2*np.sum(p[:-1]*p[1:]))
eps=2e-5; numerical=0.
for i in range(n):
    ap=a.copy();am=a.copy();ap[i]+=eps;am[i]-=eps
    lp=eigh_tridiagonal(ap,b,eigvals_only=True)[-1]
    lm=eigh_tridiagonal(am,b,eigvals_only=True)[-1]
    numerical+=((lp-lm)/(2*eps))**2
for i,zi in enumerate(z):
    for j in range(len(zi)):
        zp=zi.copy();zm=zi.copy();zp[j]+=eps;zm[j]-=eps
        bp=b.copy();bm=b.copy();bp[i]=np.linalg.norm(zp)/np.sqrt(2);bm[i]=np.linalg.norm(zm)/np.sqrt(2)
        lp=eigh_tridiagonal(a,bp,eigvals_only=True)[-1]
        lm=eigh_tridiagonal(a,bm,eigvals_only=True)[-1]
        numerical+=((lp-lm)/(2*eps))**2
records['gamma_finite_difference']={'predicted':predicted,'coordinate_difference_sum':float(numerical)}
assert abs(predicted-numerical)<1e-7
# Static concentration/min-max/Sobolev steps checked against directly computed vectors.
max_ratios=[]
for n in [64,256,1024]:
    for _ in range(20):
        a=rng.normal(size=n);b=np.sqrt(rng.chisquare(2*np.arange(n-1,0,-1))/2)
        ev,vec=eigh_tridiagonal(a,b,select='i',select_range=(n-2,n-1))
        r=np.sqrt(12*np.log(n));m=int(n**.25)
        assert abs(a).max()<=r and abs(b-np.sqrt(np.arange(n-1,0,-1))).max()<=r
        for j in [1,2]:
            w=abs(vec[:,-j]);D=np.sum(np.diff(np.r_[0,w,0])**2)
            lower=2*np.sqrt(n)-3*r-np.pi**2*j*j-2
            assert ev[-j]>=lower-1e-10
            assert D<=(6*r+np.pi**2*j*j+2)/(np.sqrt(n)+r)+1e-10
            assert max(w*w)<=2*np.sqrt(D)+1e-10
            max_ratios.append(float(max(w*w)/(2*np.sqrt(D))))
records['max_discrete_sobolev_ratio']=max(max_ratios)
# Re-derive both large-time Airy Laplace powers numerically, with y=t*x substitution.
a1=ai_zeros(1)[0][0];der=airy(a1)[1]
psi=lambda x:airy(a1+x)[0]/der
asympt=[]
for t in [10.,30.,100.,300.]:
    c4=quad(lambda y:(t*psi(y/t))**4*np.exp(-y),0,60,epsabs=1e-9)[0]
    c2=quad(lambda y:(t*psi(y/t))**2/y*np.exp(-y) if y else 0,0,60,epsabs=1e-9)[0]
    asympt.append({'t':t,'t5_integral_psi4':c4,'t2_integral_psi2_over_x':c2})
records['airy_laplace_asymptotics']=asympt
assert abs(asympt[-1]['t5_integral_psi4']-24)<.1
assert abs(asympt[-1]['t2_integral_psi2_over_x']-1)<.01
records['all_passed']=True
root=pathlib.Path(__file__).resolve().parents[1]
(root/'data'/'math_audit.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
