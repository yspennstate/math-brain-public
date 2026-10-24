import numpy as np
from math import sqrt, e

rng=np.random.default_rng(20260924024521)
h=1/20
eps=1/64
delta=1/2-eps-sqrt(2*eps)
sigma=delta-h
ridge_lhs=sqrt(eps/delta)+sqrt(6)*h/sigma
resource=1/(160*sqrt(2))

trials=10000
vp=vr=0
heavy=0
min_margin=float('inf')
for _ in range(trials):
    n=int(rng.integers(6,50))
    U,_=np.linalg.qr(rng.normal(size=(n,n)))
    lam=rng.choice([-1,1],size=n)*(10**rng.uniform(-3,2,size=n))
    lam[:3]=rng.choice([-1,1],size=3)*rng.uniform(1,4,size=3)
    A=(U*lam)@U.T
    hi=np.abs(lam)>=h
    P=U[:,hi]@U[:,hi].T
    vp += np.linalg.eigvalsh(A@A-h*h*P)[0] < -1e-8
    rowsq=np.sum(A*A,axis=1)
    for i in np.where(np.diag(P)>eps)[0]:
        heavy += 1
        cross=np.sqrt(max(0.0,rowsq[i]-A[i,i]**2))
        min_margin=min(min_margin,max(abs(A[i,i]),cross)-resource)
        vr += (abs(A[i,i])<=resource and cross<=resource)

print({
 'trials':trials,
 'heavy_coordinate_tests':heavy,
 'violations_psd':int(vp),
 'violations_strong_resource':int(vr),
 'minimum_observed_resource_margin':min_margin,
 'h':h,
 'eps':eps,
 'delta':delta,
 'sigma':sigma,
 'ridge_leverage_lhs':ridge_lhs,
 'one_over_sqrt2':1/sqrt(2),
 'diffuse_density_bound':9*sqrt(3*e)/(2*sigma),
 'row_energy_threshold':1/160,
 'pivot_cross_threshold':resource,
 'improvement_factor_over_1_512':resource/(1/512),
})
