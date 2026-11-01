import numpy as np
import math

rng=np.random.default_rng(20260922)
max_werr=max_serr=max_derr=0.0
count=0
for n in [4,5,8,12,20]:
    for rep in range(20):
        G=rng.normal(size=(n,3))
        U,_=np.linalg.qr(G)
        Lam=np.diag([1.3,2.1,-1.7])
        for i in range(n):
            u=U[i,:]
            ell=float(u@u)
            d=float(u@Lam@u)
            if ell < 1e-10 or abs(d)<1e-7:
                continue
            _,_,vh=np.linalg.svd(u.reshape(1,3))
            P=vh[1:,:].T
            mask=[k for k in range(n) if k!=i]
            W=U[mask,:]@P
            H=Lam-np.outer(Lam@u,Lam@u)/d
            M=P.T@H@P
            A=U@Lam@U.T
            S=A[np.ix_(mask,mask)]-np.outer(A[mask,i],A[i,mask])/d
            max_werr=max(max_werr,float(np.linalg.norm(W.T@W-np.eye(2),ord=2)))
            max_serr=max(max_serr,float(np.linalg.norm(S-W@M@W.T,ord=2)))
            lhs=abs(np.linalg.det(M))
            rhs=abs(np.linalg.det(Lam))*ell/abs(d)
            max_derr=max(max_derr,abs(lhs-rhs)/max(1,rhs))
            count+=1

print('cases',count)
print('max_parseval_operator_error',repr(max_werr))
print('max_schur_factorization_operator_error',repr(max_serr))
print('max_relative_det_identity_error',repr(max_derr))
print('C_bank',repr(16*math.sqrt(15)*6**0.25))
print('C_small_q',repr(16*math.sqrt(2)/(3**0.25)*(3**0.125)))
print('C_definite_heavy',repr(16*math.sqrt(15)*6**0.25*math.sqrt(32)))
