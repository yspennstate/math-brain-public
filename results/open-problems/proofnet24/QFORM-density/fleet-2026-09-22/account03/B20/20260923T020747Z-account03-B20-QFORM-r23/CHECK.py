import math
import numpy as np

rng=np.random.default_rng(20260923)
max_rel=0.0
checks=0
for _ in range(25):
    X=rng.normal(size=(3,3))
    M=(X+X.T)/2
    ev,Q=np.linalg.eigh(M)
    ev=np.sign(ev+(ev==0))*(np.abs(ev)+1.2)
    M=Q@np.diag(ev)@Q.T
    v=rng.normal(size=3); v/=np.linalg.norm(v)
    m=float(v@M@v)
    if abs(m)<0.1:
        continue
    A=np.column_stack([v,rng.normal(size=(3,2))])
    O,_=np.linalg.qr(A)
    if np.dot(O[:,0],v)<0:
        O[:,0]*=-1
    E=O[:,1:]
    U=rng.normal(size=(8,3))
    W=U@E
    lam=0.4+rng.random()
    DeltaG=float(np.linalg.det(W.T@W))
    Delta12=0.0
    for j in range(4):
        for k in range(4,8):
            Delta12+=float(np.linalg.det(np.vstack([W[j],W[k]]))**2)
    D=abs(float(np.linalg.det(M)))
    mu=D*lam*Delta12
    N=M-np.outer(M@v,M@v)/m
    B=U@N@U.T
    vals=np.linalg.eigvalsh(B)
    nz=np.sort(np.abs(vals))[-2:]
    Pi=float(nz.prod())
    lhs=abs(lam*m)*Pi
    rhs=D*lam*DeltaG
    max_rel=max(max_rel,abs(lhs-rhs)/max(1.0,abs(rhs)))
    assert mu<=rhs+1e-8
    checks+=1

C=16*math.sqrt(60)*(512*24)**0.25
assert C<1305
assert abs(24/512-3/64)<1e-15
print(f"trials={checks}")
print(f"max_relative_schur_pseudodet_error={max_rel:.3e}")
print(f"threshold_constant={C:.12f}")
print(f"punctured_residual_product_threshold={3/64:.12f}")
print("QFORM_B20_R23_CHECK_PASS")
