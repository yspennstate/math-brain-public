#!/usr/bin/env python3
import math
import numpy as np

rng=np.random.default_rng(20260923)
max_identity=0.0
max_decomp=0.0
max_router_violation=0.0
for _ in range(5000):
    a=rng.uniform(-3,3)
    if abs(a)<0.2:
        a=0.2 if a>=0 else -0.2
    u,v,b,h,c=rng.normal(size=5)
    T=np.array([[a,u,v],[u,b,h],[v,h,c]],float)
    d1=a*b-u*u
    d2=a*c-v*v
    k=a*h-u*v
    max_identity=max(max_identity,abs(a*np.linalg.det(T)-(d1*d2-k*k)))
    w=np.array([a,u,v])
    R=T-np.outer(w,w)/a
    R0=np.array([[0,0,0],[0,d1/a,k/a],[0,k/a,d2/a]],float)
    max_decomp=max(max_decomp,float(np.max(np.abs(R-R0))))

    m=4
    C=rng.normal(size=(3,m))
    D=rng.normal(size=(m,m)); D=(D+D.T)/2
    A=np.block([[T,C],[C.T,D]])
    s3=np.linalg.svd(A,compute_uv=False)[2]
    Delta=math.sqrt(d1*d1+d2*d2+2*k*k)/abs(a)
    s1C=np.linalg.svd(C,compute_uv=False)[0]
    Dnorm=np.linalg.norm(D,2)
    max_router_violation=max(max_router_violation,s3-(s1C+Dnorm+Delta))

L=2.5
spectra=[]
for R in [1,3,10,100]:
    cvec=np.array([math.sqrt(L),math.sqrt(L/R),math.sqrt(L/R)])
    T=np.outer(cvec,cvec)
    B=np.array([[0,L*R],[L*R,0.0]])
    A=np.block([[T,np.zeros((3,2))],[np.zeros((2,3)),B]])
    spectra.append((R,np.linalg.eigvalsh(A).tolist()))

print('QFORM_B08_R40_CHECK')
print('max_triangle_identity_error=',repr(max_identity))
print('max_rank1_decomposition_error=',repr(max_decomp))
print('max_router_violation=',repr(max_router_violation))
print('affine_stable_rank1_plus_pair_constant=',repr(128*math.sqrt(3/2)))
print('clean_rank1_plus_pair_constant=',repr(128.0))
print('volume_tail_prefactor=',repr(9*math.sqrt(3)*math.e/2))
for R,ev in spectra:
    print('target_family_R=',R,'eigenvalues=',ev)
    assert sum(abs(x)>=L-1e-10 for x in ev)>=3
assert max_identity<1e-10
assert max_decomp<1e-10
assert max_router_violation<1e-10
print('QFORM_B08_R40_CHECK_PASS')
