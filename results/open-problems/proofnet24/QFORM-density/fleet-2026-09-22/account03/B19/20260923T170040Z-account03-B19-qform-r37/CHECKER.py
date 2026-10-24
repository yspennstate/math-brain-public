import math
import numpy as np

rng=np.random.default_rng(20260923)
tau=2.0**-20
rho_star=63*(1-tau)**2/16384
x2_star=(64/259)*rho_star
Delta=(3/8)*rho_star
sigma2_star=(3/8)*x2_star
Z0=Delta**2*sigma2_star/64
density_bound=6*math.sqrt(math.e)*Z0**(-1/6)

assert rho_star > 0.0038452
assert x2_star > 0.00095016
assert Delta > 0.00144195
assert sigma2_star > 0.00035631
assert Z0 > 1.1575e-11
assert density_bound < 658

def e3(M):
    lam=np.linalg.eigvalsh(M@M.T)
    out=0.0
    for i in range(len(lam)):
        for j in range(i+1,len(lam)):
            for k in range(j+1,len(lam)):
                out += lam[i]*lam[j]*lam[k]
    return out

min_ext_ratio=float('inf')
min_common_ratio=float('inf')
max_det_rel=0.0
for _ in range(2000):
    N1=rng.normal(size=(4,5))
    N2=rng.normal(size=(3,5))
    _,s1,Vh1=np.linalg.svd(N1,full_matrices=False)
    _,s2,Vh2=np.linalg.svd(N2,full_matrices=False)
    Q1b=Vh1[:2].T
    Q2b=Vh2[:2].T
    Q1=Q1b@Q1b.T
    Q2=Q2b@Q2b.T
    delta=float(np.trace(Q2@(np.eye(5)-Q1)))
    Z=e3(np.hstack([N1.T,N2.T]))
    rhs=(s1[0]*s1[1])**2 * s2[1]**2 * delta
    if rhs>1e-12:
        min_ext_ratio=min(min_ext_ratio,Z/rhs)
    sv=np.linalg.svd(N2@Q1b,compute_uv=False)
    projected_product=sv[0]*sv[1]
    target=(1-delta)*s2[0]*s2[1]
    if target>1e-12:
        min_common_ratio=min(min_common_ratio,projected_product/target)

    C=rng.normal(size=(2,2))
    N=rng.normal(size=(2,2))
    P=rng.normal(size=(2,2))
    while abs(np.linalg.det(N))<0.05:
        N=rng.normal(size=(2,2))
    while abs(np.linalg.det(P))<0.05:
        P=rng.normal(size=(2,2))
    H=np.block([[np.zeros((2,2)),C,N],
                [C.T,np.zeros((2,2)),P],
                [N.T,P.T,np.zeros((2,2))]])
    R=np.linalg.inv(N)@C@np.linalg.inv(P).T
    rhsdet=(np.linalg.det(N)**2)*(np.linalg.det(P)**2)*np.linalg.det(R+R.T)
    rel=abs(np.linalg.det(H)-rhsdet)/(1+abs(rhsdet))
    max_det_rel=max(max_det_rel,rel)

assert min_ext_ratio >= 1-2e-10
assert min_common_ratio >= 1-2e-10
assert max_det_rel < 1e-10
print('rho_star',rho_star)
print('x2_star',x2_star)
print('Delta',Delta)
print('sigma2_star',sigma2_star)
print('Z0',Z0)
print('Dprime_bound',density_bound)
print('anchor_half_Z0',Z0/2)
print('common_plane_edge_product',(63/64)*Delta)
print('min_exterior_ratio',min_ext_ratio)
print('min_common_plane_ratio',min_common_ratio)
print('max_cycle_det_relative_residual',max_det_rel)
print('QFORM_B19_R38_COMMON_PLANE_CYCLE_CHECK_PASS')
