"""NUMERICAL discovery only: Hessian eigenvalues for the variation space."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
from scipy.linalg import null_space


def q(E, u, invk):
    p = u*u
    m = np.trace(E)/2
    return (-2*np.trace(E@E)+(-2+4*invk)*np.sum(np.outer(u,u)*E**2)
            +4*p@np.diag(E@E)-2*p@E@np.diag(E)
            +m*(-4*invk*m+(2*invk+4*invk**2)*p@np.diag(E)))


def matrix(u, invk):
    K = null_space(np.array([np.ones(5),u]))
    basis = []
    for i in range(3):
        for j in range(i,3):
            v = np.zeros((3,3));v[i,j]=v[j,i]=1
            basis.append(K@v@K.T)
    C = np.empty((6,6))
    for i in range(6):
        C[i,i] = q(basis[i],u,invk)
        for j in range(i):
            C[i,j]=C[j,i]=(q(basis[i]+basis[j],u,invk)-C[i,i]-C[j,j])/2
    return C, basis


def main():
    rng=np.random.default_rng(160104); best=(-100,None)
    for it in range(4000):
        u=rng.normal(size=5);u-=u.mean();u/=np.linalg.norm(u)
        for invk in (0,.1,.2):
            C,basis=matrix(u,invk);ev,vec=np.linalg.eigh(C)
            if ev[-1]>best[0]:best=(ev[-1],(u,invk))
    print('NUMERICAL max Hessian eigenvalue:',best,flush=True)

if __name__=='__main__':main()
