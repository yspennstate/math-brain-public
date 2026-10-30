import math
import numpy as np

C = 3*(math.pi/2)**(1/3)
print(f"density_constant={C:.15f}")
print("constant_lt_3.488=", C < 3.488)

rng=np.random.default_rng(12345)
errs=[]
for _ in range(5000):
    m=6
    Q,_=np.linalg.qr(rng.normal(size=(4,4)))
    U=Q[:,:2]; V=Q[:,2:]
    R,_=np.linalg.qr(rng.normal(size=(m,m)))
    W=R[:,:2]
    s=np.exp(rng.uniform(-2,2,size=2))
    K=U@np.diag(s)@W.T
    Z=rng.normal(size=(4,4)); B=(Z+Z.T)/2
    H=V.T@B@V
    C6=np.block([[B,K@W],[W.T@K.T,np.zeros((2,2))]])
    lhs=abs(np.linalg.det(C6))
    rhs=(s[0]*s[1])**2*abs(np.linalg.det(H))
    if rhs > 1e-12:
        errs.append(abs(lhs-rhs)/rhs)
print(f"det_identity_trials={len(errs)}")
print(f"det_identity_max_relative_error={max(errs):.16e}")

H4=np.array([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]],dtype=float)/2
U=H4[:,:2]; V=H4[:,2:]
B=V@V.T; K=U
A=np.block([[B,K],[K.T,np.zeros((2,2))]])
eigs=np.linalg.eigvalsh(A)
print("overlap_control_eigenvalues=", ",".join(f"{x:.12g}" for x in eigs))
print("STATUS=PASS" if C < 3.488 and max(errs)<1e-10 and np.max(np.abs(eigs-np.array([-1,-1,1,1,1,1])))<1e-10 else "STATUS=FAIL")
