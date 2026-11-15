"""Independent numerical checks of the reductions and boundary coefficients."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,resource
from pathlib import Path
import numpy as np
from reduced import *
from dpp import random_kernel,probabilities,stats,hessian

def main():
    rng=np.random.default_rng(33406);start=time.monotonic();errs=[]
    for _ in range(2000):
        q=random_kernel(rng,3,True,'uniform');p,C=atoms_grad(q);pp,m=probabilities(q)
        g=pp[:,None]*np.einsum('sij,bji->sb',np.linalg.inv(m),B).real
        gg=np.einsum('sij,bji->sb',C,B).real
        d=criterion(q,True);A=d['A'];v=np.r_[A.diagonal().real,[t for i,j in PAIRS for t in (A[i,j].real,A[i,j].imag)]]
        H=hessian(q,B)
        errs.append([np.max(abs(p-pp)),np.max(abs(g-gg)),abs(d['theta']-probability_criterion(q)),
                     abs(d['theta']-seven_criterion(q)),abs(d['theta']-criterion(gauge(q))),
                     abs(d['theta']-criterion(np.eye(3)-q)),abs(v@H@v-stats(q,A)[1])])
    D=np.diag([.3,.45,.65]);W=np.array([[0,.7,.8],[.7,0,.5+.4j],[.8,.5-.4j,0]])
    vv=np.diag(D)*(1-np.diag(D));cc=0
    for i,j,k in ((0,1,2),(1,0,2),(2,0,1)):cc+=abs(W[i,j])**2*abs(W[i,k])**2/(vv[i]*abs(W[j,k])**2)
    diagonal=[]
    for t in (.01,.003,.001,.0003):
        th=criterion(D+t*W);diagonal.append(dict(t=t,theta=th,theta_over_t2=th/t**2,predicted=cc))
    K=np.array([[.7,.14,.13],[.14,.8,.1+.12j],[.13,.1-.12j,.9]])
    ell=np.array([np.log(K[j,j].real*K[k,k].real/(K[j,j].real*K[k,k].real-abs(K[j,k])**2)) for i,j,k in ((0,1,2),(1,0,2),(2,0,1))])
    coeff=np.prod(ell)*sum(K[i,i].real/ell[i]**2 for i in range(3));zero=[]
    for t in (.01,.003,.001,.0003):
        th=criterion(t*K);zero.append(dict(t=t,theta=th,theta_over_t=th/t,predicted=coeff))
    out=dict(seed=33406,cases=2000,error_columns=['atoms','gradients','theta_8','theta_7','gauge','complement','curvature_cpp'],
             max_errors=np.max(errs,axis=0).tolist(),diagonal_asymptotic=diagonal,zero_asymptotic=zero,
             seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
    Path('data/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
