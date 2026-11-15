"""NUMERICAL relaxed-rank tests; these are not graph certificates."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import numpy as np


def value(L,u,vk):
    P=np.outer(u,u);A=np.eye(5)-L;m=(np.trace(L)+1)/2
    h=np.diag(P)@np.diag(L)+.5
    B=np.sum(P*A*A)
    Y=-2*sum(L[i,j]*(u[i]-u[j])**2*(2-L[i,i]-L[j,j]+2*L[i,j])for i in range(5)for j in range(i+1,5))
    return 2*(np.trace(L)-np.trace(L@L))+2*(1+2*vk)*B+(m-1)*(2-2*vk-4*vk*vk-4*m*vk+2*vk*(1+2*vk)*h)-Y


def main():
    rng=np.random.default_rng(160105);H=np.eye(5)-np.ones((5,5))/5
    for rank in (0,1,2,3):
        best=(100,None)
        for j in range(10000):
            M=rng.normal(size=(5,4));M-=M.mean(axis=0);Q,_=np.linalg.qr(M)
            u=Q[:,0];S=Q[:,1:rank+1]@Q[:,1:rank+1].T;L=H-S
            for vk in (0,.1,.2):
                val=value(L,u,vk)
                if val<best[0]:best=(val,(u,S,vk))
        print('gap rank',rank,'relaxed min',best[0],flush=True)
        if best[0]<0:print(best[1],flush=True)

if __name__=='__main__':main()
