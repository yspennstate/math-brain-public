"""Audit exact trace identities, gradient and sparse spectral calculations."""
import os
for key in ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[key]="1"
import json
from pathlib import Path
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from models import quartic_action_grad,quartic_U,profile,bottom,quartic_mode,hmc_chain,quartic_hessian_banded

assert os.getpriority(os.PRIO_PROCESS,0)>=10
rng=np.random.default_rng(4313)
n=11;a=rng.normal(size=n);q=rng.normal(size=n-1)*.2
T=np.diag(a)+np.diag(np.exp(q),1)+np.diag(np.exp(q),-1)
val,ga,gq=quartic_action_grad(a,q)
exact=np.sum(quartic_U(np.linalg.eigvalsh(T)))/2-np.dot((n-np.arange(1,n))/n,q)
errors=[]
z=np.r_[a,q];grad=np.r_[ga,gq]
for j in range(len(z)):
    step=1e-5
    left=z.copy();right=z.copy();left[j]-=step;right[j]+=step
    finite=(quartic_action_grad(right[:n],right[n:])[0]-quartic_action_grad(left[:n],left[n:])[0])/(2*step)
    errors.append(abs(finite-grad[j]))
d,e,h=profile(10000,2,rng)
ev=bottom(d,e)
sp=diags([e,d,e],[-1,0,1],format='csc')
ev2=np.sort(eigsh(sp,k=3,sigma=-20,which='LM',return_eigenvectors=False,tol=1e-10))
assert abs(val-exact)<1e-9
assert max(errors)<1e-7
assert np.max(abs(ev-ev2))<1e-7
interleaved=np.empty(2*n-1);interleaved[::2]=a;interleaved[1::2]=q
band=quartic_hessian_banded(a,q)
H=np.diag(band[0])+np.diag(band[1,:-1],1)+np.diag(band[1,:-1],-1)+np.diag(band[2,:-2],2)+np.diag(band[2,:-2],-2)
def inter_grad(z):
    _,ga,gq=quartic_action_grad(z[::2],z[1::2])
    ret=np.empty_like(z);ret[::2]=ga;ret[1::2]=gq;return ret
hessian_error=0.
for j in range(len(interleaved)):
    evec=np.zeros_like(interleaved);evec[j]=1e-5
    hessian_error=max(hessian_error,float(np.max(abs((inter_grad(interleaved+evec)-inter_grad(interleaved-evec))/2e-5-H[:,j]))))
assert hessian_error<1e-7
am,qm,info=quartic_mode(64)
samples,hm=hmc_chain(64,2,(am,qm),rng,burn=150,draws=80)
out=dict(trace_error=abs(val-exact),gradient_max_error=max(errors),
          hessian_max_error=hessian_error,
          eigensolver_error=float(np.max(abs(ev-ev2))),mode64=info,
          hmc64_acceptance=hm['acceptance_post'],hmc64_mean_top=float(samples[:,0].mean()))
Path('data').mkdir(exist_ok=True)
Path('data/model_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
