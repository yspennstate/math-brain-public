import numpy as np
from explore import curvatures

def reduced(K):
    Q,D=curvatures(K);T=np.zeros((9,9));T[:3,:3]=np.eye(3)
    for k,(i,j) in enumerate([(0,1),(0,2),(1,2)]):
        z=K[i,j]/abs(K[i,j]);a,b=z.real,z.imag
        T[3+2*k,3+k]=a;T[4+2*k,3+k]=b
        T[3+2*k,6+k]=-b;T[4+2*k,6+k]=a
    Q=T.T@Q@T;D=T.T@D@T
    X=np.vstack([np.eye(6),-np.linalg.solve(Q[6:,6:],Q[6:,:6])])
    return X.T@Q@X,X.T@D@X,D,T@X

if __name__=='__main__':
    rng=np.random.default_rng(73);worst=(0,None)
    for j in range(2000):
        Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));U=np.linalg.qr(Z)[0]
        K=U@np.diag(rng.uniform(.001,.999,3))@U.conj().T
        S,D,_,X=reduced(K);val=np.linalg.eigvalsh(D)[0]
        if val<worst[0]:worst=(val,K)
    print('reduced minimum forcing',worst)
    if worst[1] is not None:
        K=worst[1];S,D,_,X=reduced(K);v=np.linalg.eigh(D)[1][:,0]
        print('full physical coordinates',X@v,'curvature',v@S@v)
        print('least eig D+Q',np.linalg.eigvalsh(D+S)[0])
        np.savez('computations/X073/schur-witness.npz',K=K,Acoords=X@v)
