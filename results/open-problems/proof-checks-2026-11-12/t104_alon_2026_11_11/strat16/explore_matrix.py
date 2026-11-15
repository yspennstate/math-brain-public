"""NUMERICAL discovery for a positive matrix extension on the rank-3 face."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import numpy as np
from scipy.linalg import null_space


def target(S, z):
    t=np.trace(S);v=np.trace(S@S);d=np.diag(S);M=(5-t)/2
    # On vectors orthogonal to 1 and S, this matrix gives T*.
    C=2*(t-v)+(M-1)*(2-2*z-4*z*z-4*M*z+(13/5)*(z+2*z*z))
    return C*np.eye(5)+(-2+4*z)*(S*S)+np.diag((-2-2*(M-1)*(z+2*z*z))*d-2*S@d+4*np.diag(S@S))-2*t/5*np.eye(5)


def main():
    rng=np.random.default_rng(160106);H=np.eye(5)-np.ones((5,5))/5
    K=null_space(np.ones((1,5)));mins={c:100 for c in (1,2,4,8,16)}
    topmin=100;feasible=0
    for it in range(20000):
        V=rng.normal(size=(5,2));V-=V.mean(axis=0)
        S=V@V.T
        p=max(-S[i,j]for i in range(5)for j in range(i+1,5))
        S/=5*p
        if np.linalg.eigvalsh(S)[-1]>1+1e-10:continue
        feasible+=1
        top=null_space(np.vstack((np.ones(5),V.T)))
        for z in (0,.1,.2):
            F=target(S,z)
            topmin=min(topmin,np.linalg.eigvalsh(top.T@F@top)[0])
            for c in mins:mins[c]=min(mins[c],np.linalg.eigvalsh(K.T@(F+c*S)@K)[0])
    print('NUMERICAL feasible samples',feasible,'selected minimum',topmin,'extension minima',mins)

if __name__=='__main__':main()
