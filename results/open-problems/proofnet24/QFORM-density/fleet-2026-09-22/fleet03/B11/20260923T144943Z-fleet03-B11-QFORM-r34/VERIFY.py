import itertools
import math
import numpy as np

R=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)/2
M=np.diag([1.0,1.0,-1.0])
A=R@M@R.T
assert np.allclose(R.T@R,np.eye(3))
assert np.allclose(np.sum(R*R,axis=1),0.75)
i,j=0,3
g=np.linalg.norm(np.cross(R[i],R[j]))**2
assert abs(g-0.5)<1e-12
for k in [1,2]:
    idx=[i,j,k]
    d=abs(np.linalg.det(A[np.ix_(idx,idx)]))
    assert abs(d-0.25)<1e-12
W2=0.5**2-2*0.25**2
assert abs(W2-0.125)<1e-12

rng=np.random.default_rng(1234)
maxerr=0.0
for n in [6,8,12]:
    for trial in range(20):
        X=rng.normal(size=(n,3))
        Rr,_=np.linalg.qr(X)
        U,_=np.linalg.qr(rng.normal(size=(3,3)))
        Mr=U@np.diag([1.2,2.1,-1.4])@U.T
        mask=rng.random(n)<0.5
        if mask.sum()<3 or (~mask).sum()<3:
            continue
        S=np.where(mask)[0]
        T=np.where(~mask)[0]
        B=Rr[S]@Mr@Rr[T].T
        sv=np.linalg.svd(B,compute_uv=False)
        Delta=np.prod(sv[:3])
        GS=Rr[S].T@Rr[S]
        GT=Rr[T].T@Rr[T]
        rhs=abs(np.linalg.det(Mr))*math.sqrt(max(np.linalg.det(GS)*np.linalg.det(GT),0.0))
        maxerr=max(maxerr,abs(Delta-rhs))
assert maxerr<1e-11

C=6*math.e*2**(1/3)
print('tetra_parseval: PASS')
print('tetra_leverage = 3/4: PASS')
print('pair_area_g = 1/2: PASS')
print('partner_extensions = 1/4,1/4: PASS')
print('partner_W2 = 1/8: PASS')
print('cross_volume_factorization_random_max_error =',maxerr)
print('q<=1/4 constant 6*e*2^(1/3) =',C)
print('QFORM_B11_R34_DPP_CROSSCUT_CHECK_PASS')
