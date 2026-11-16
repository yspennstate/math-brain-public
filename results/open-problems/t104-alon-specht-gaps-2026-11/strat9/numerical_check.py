"""NUMERICAL: random-frame comparison to the read-only STRAT7 reference."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import sys,json
sys.dont_write_bytecode=True
sys.path.insert(0,'../STRAT7')
from terms import terms
import numpy as np
import sympy as S
from frame import A,B,C,d,e,f,h,a,r,formula

def main():
    rng=np.random.default_rng(9131311)
    funcs={N:S.lambdify((a,r,A,B,C,d,e,f,h),formula(N),'numpy')for N in (6,7,10)}
    error=0.;count=0;minimum=1e100
    for k in range(1200):
        M=rng.normal(size=(5,2));M-=M.mean(0);U=np.linalg.qr(M)[0];u,w=U.T
        rr=rng.uniform(.001,1)
        Dmax=max(3-rr,max(-1-rr-20*(u[i]*u[j]+rr*w[i]*w[j]) for i in range(5)for j in range(i+1,5)))
        aa=2/Dmax*rng.uniform(.01,.999)
        lm=(2+aa*(1+rr))/4
        ww=lm/5+aa*np.outer(u,u)+aa*rr*np.outer(w,w);np.fill_diagonal(ww,0)
        assert ww.min()>-1e-13
        ms=(sum(u**4),sum(w**4),sum(u*u*w*w),sum(u**3),sum(u*u*w),sum(u*w*w),sum(w**3))
        for N in funcs:
            padded=np.zeros((N,N));padded[:5,:5]=ww
            D,x1,x2,x3,y=terms(padded)
            assert D==2
            val=x1+x2+x3-y;pred=funcs[N](aa,rr,*ms)
            error=max(error,abs(val-pred));minimum=min(minimum,val);count+=1
    assert error<1e-10
    out=dict(label='NUMERICAL',seed=9131311,frames=1200,comparisons=count,N=[6,7,10],maximum_absolute_error=error,minimum_sampled_T=minimum)
    with open('numerical_check.json','w')as output:json.dump(out,output,indent=2)
    print('NUMERICAL:',out)
if __name__=='__main__':main()
