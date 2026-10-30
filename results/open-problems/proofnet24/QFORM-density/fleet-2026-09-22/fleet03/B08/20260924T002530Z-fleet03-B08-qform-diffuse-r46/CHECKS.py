import math
import numpy as np

rng=np.random.default_rng(20260924)
max_det_delete=0.0
max_det_schur=0.0
max_leverage_excess=-1e100
count=0

for _ in range(2000):
    m=int(rng.integers(3,15))
    M=rng.normal(size=(2,m))
    if np.linalg.matrix_rank(M)<2:
        continue
    G=M@M.T
    Gi=np.linalg.inv(G)
    lev=np.array([M[:,j]@Gi@M[:,j] for j in range(m)])
    js=np.where(lev<=1/3)[0]
    if len(js)==0:
        continue
    j=int(rng.choice(js))
    R=rng.normal(size=(2,2)); R=(R+R.T)/2
    if abs(np.linalg.det(R))<1e-4:
        continue
    dj=float(rng.choice([-1,1])*(0.1+rng.random()*3))
    mj=M[:,j]
    aj=float(dj+mj@R@mj)
    if abs(aj)<1e-5:
        continue
    K=[k for k in range(m) if k!=j]
    MK=M[:,K]
    GK=MK@MK.T
    Rj=R-np.outer(R@mj,R@mj)/aj
    max_det_delete=max(max_det_delete,abs(np.linalg.det(GK)-np.linalg.det(G)*(1-lev[j])))
    max_det_schur=max(max_det_schur,abs(np.linalg.det(Rj)-np.linalg.det(R)*dj/aj))
    GKinv=np.linalg.inv(GK)
    levK=np.array([MK[:,q]@GKinv@MK[:,q] for q in range(m-1)])
    mu=float(np.max(lev))
    max_leverage_excess=max(max_leverage_excess,float(np.max(levK)-mu/(1-lev[j])))
    count+=1

C=4*math.sqrt(2*math.e)
print('instances',count)
print('max_abs_det_delete_error',repr(max_det_delete))
print('max_abs_det_schur_error',repr(max_det_schur))
print('max_leverage_excess',repr(max_leverage_excess))
print('C_half_riesz',repr(C))
print('C_alpha_delta_half',repr(C*3**0.25))
print('C_lowrank_sigma_L_over_128',repr((96*math.sqrt(math.e)/7)*128))
assert max_det_delete < 1e-10
assert max_det_schur < 1e-9
assert max_leverage_excess <= 1e-10
print('QFORM_B08_R46_CHECK_PASS')
