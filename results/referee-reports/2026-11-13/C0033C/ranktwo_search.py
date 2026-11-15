"""Rank-two tests, coordinate-range theorem checks, and local optimization."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,resource
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from dpp import *
rng=np.random.default_rng(33362)
def adj(a):return a@a-np.trace(a)*a+(np.trace(a)**2-np.trace(a@a))*np.eye(3)/2

def coordinate_formula(q,alpha,b):
    c=q[1:,1:];v=q[1:,0];pi,m=probabilities(c);inv=np.linalg.inv(m)
    r=q[0,0].real-np.einsum('i,sij,j->s',v.conj(),inv,v,optimize=False).real
    k=np.einsum('i,sij,j->s',b[1:].conj(),inv,b[1:],optimize=False).real
    rho=abs(b[0]-np.einsum('i,sij,j->s',b[1:].conj(),inv,v,optimize=False).conj())**2
    hp=np.log((1-r)/r)
    f=np.sum(pi*(k*k+(alpha+rho)**2/(r*(1-r))))
    g=np.sum(pi*k*hp)
    return -f+2*alpha*g,g

def main():
    t=time.monotonic();rows=[];errors=[];ming=1e10
    for n in (3,4,6,8):
        for sign in (1,-1):
            vals=[];gaps=[];witness=None;mx=-1e100
            for it in range(800 if n<=4 else 300):
                q=random_kernel(rng,n,True,('uniform','extreme','projection')[it%3])
                u=random_unitary(rng,n,True)[:,:2]
                lam=np.array([1,sign*10**rng.uniform(-2,0)])
                a=np.einsum('ik,jk,k->ij',u,u.conj(),lam,optimize=False)
                a=(a+a.conj().T)/2;a/=np.linalg.norm(a)
                val=float(stats(q,a)[1]);vals.append(val)
                margin=min(np.linalg.eigvalsh(q)[0],1-np.linalg.eigvalsh(q)[-1]);step=margin/2
                gap=float(stats(q)[0]-(stats(q+step*a)[0]+stats(q-step*a)[0])/2);gaps.append(gap)
                if val>mx:mx=val;witness=(q.copy(),a.copy(),u.copy(),lam.copy())
            name=f'ranktwo_n{n}_sign{sign}'
            np.savez('data/'+name+'.npz',Q=witness[0],A=witness[1],factor=witness[2],weights=witness[3])
            row=dict(n=n,sign=sign,trials=len(vals),largest_curvature=max(vals),smallest_midpoint_gap=min(gaps),witness=name+'.npz')
            rows.append(row);print(row,flush=True)
        for it in range(100):
            q=random_kernel(rng,n,True,'uniform');b=rng.normal(size=n)+1j*rng.normal(size=n);b/=np.linalg.norm(b)
            alpha=(-1 if it%2 else 1)*rng.uniform(.1,1)
            a=np.outer(b,b.conj());a[0,0]+=alpha
            value,g=coordinate_formula(q,alpha,b)
            errors.append(abs(value-stats(q,a)[1]));ming=min(ming,g)
    # Optimize the genuine positive rank-two submanifold at n=3 jointly with Q.
    B=basis(3,True)
    def decode(v):
        x=np.einsum('b,bij->ij',v[:9],B,optimize=False);lam,u=np.linalg.eigh(x)
        q=spectral(u,1e-4+(1-2e-4)/(1+np.exp(-np.clip(lam,-25,25))))
        z=v[9:15].reshape(3,2)+1j*v[15:21].reshape(3,2)
        a=np.einsum('ik,jk->ij',z,z.conj(),optimize=False);a=(a+a.conj().T)/2;a/=np.linalg.norm(a)
        return q,a
    def fun(v):
        try:q,a=decode(v);return -float(stats(q,a)[1])
        except (ArithmeticError,np.linalg.LinAlgError):return 1e10
    opt=[]
    for it in range(8):
        res=minimize(fun,rng.normal(size=21),method='Nelder-Mead',options=dict(maxfev=2500,xatol=1e-8,fatol=1e-9))
        q,a=decode(res.x)
        factor=res.x[9:15].reshape(3,2)+1j*res.x[15:21].reshape(3,2)
        np.savez(f'data/psd_optimized_{it}.npz',Q=q,A=a,factor=factor,weights=np.ones(2))
        row=dict(start=it,curvature=-res.fun,evaluations=res.nfev,converged=bool(res.success),direction_eigenvalues=np.linalg.eigvalsh(a).tolist())
        opt.append(row);print(row,flush=True)
    out=dict(seed=33362,rows=rows,coordinate_theorem=dict(trials=len(errors),max_identity_error=max(errors),smallest_G_value=ming),psd_optimizations=opt,seconds=time.monotonic()-t,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
    Path('data/ranktwo_search.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
