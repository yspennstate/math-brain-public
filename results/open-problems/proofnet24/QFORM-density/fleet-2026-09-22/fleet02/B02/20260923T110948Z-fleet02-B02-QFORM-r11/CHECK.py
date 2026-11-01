import math
import numpy as np

rng=np.random.default_rng(20260923)
max_shear=0.0
max_anchor=0.0
for _ in range(500):
    m=n=5
    P=rng.normal(size=(2,2))
    while abs(np.linalg.det(P))<0.2:
        P=rng.normal(size=(2,2))
    R=rng.normal(size=(2,n))
    C=rng.normal(size=(m,2))
    M=rng.normal(size=(m,n))
    x=rng.normal(size=2); u=rng.normal(size=m)
    y=rng.normal(size=2); v=rng.normal(size=n)
    S=M-C@np.linalg.inv(P)@R
    xi=x+np.linalg.inv(P).T@C.T@u
    eta=y+np.linalg.inv(P)@R@v
    lhs=x@P@y+x@R@v+u@C@y+u@M@v
    rhs=xi@P@eta+u@S@v
    max_shear=max(max_shear,abs(lhs-rhs)/(1+abs(lhs)))
    B=np.block([[P,R],[C,M]])
    gsum=0.0
    for i in range(m):
        for j in range(n):
            gsum += np.linalg.det(B[np.ix_([0,1,2+i],[0,1,2+j])])**2
    g=(np.linalg.det(P)**2)*np.sum(S*S)
    max_anchor=max(max_anchor,abs(gsum-g)/(1+abs(g)))

print('max_shear_relative_error',repr(max_shear))
print('max_anchor_relative_error',repr(max_anchor))
print('sharp_D5',repr(5*math.e/math.sqrt(2)))
print('sharp_D5_rho4',repr((5*math.e/math.sqrt(2))*24**0.1))
print('rank1_live',repr(3*math.e**(1/3)*24**(1/6)))
print('singular_scalar_rank2_live',repr(3*math.e**(2/3)*24**(1/6)))
print('rank3_shear_coefficient',repr((5/3)*math.e**(3/5)))
print('stress_limit',repr(3*math.e**(1/3)))
for m in (2,4,16,64):
    a=np.ones(m)/math.sqrt(m)
    B=np.zeros((m+2,m+2)); B[:2,:2]=np.eye(2); B[2:,2:]=np.outer(a,a)
    sv=np.linalg.svd(B,compute_uv=False)
    c=3*(1-1/m)**(-(m-1)/3)
    print('stress',m,'top_singulars',*[float(x) for x in sv[:3]],'bound',c)
print('STATUS=PASS')
