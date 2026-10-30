import numpy as np
from math import sqrt, e

rng=np.random.default_rng(20260924024520)
gamma=1/64
eta=1/32
hub=gamma*sqrt(eta)
split=hub/sqrt(2)

def rand_orth(n):
    q,r=np.linalg.qr(rng.normal(size=(n,n)))
    d=np.sign(np.diag(r)); d[d==0]=1
    return q*d

trials=10000
vp=vh=vs=va=0
heavy=0
min_psd=float('inf')
max_add=0.0
for _ in range(trials):
    n=int(rng.integers(6,40))
    V=rand_orth(n)
    lam=rng.uniform(-100,100,size=n)
    lam[:3]=rng.choice([-1,1],size=3)*rng.uniform(1,5,size=3)
    mags=10**rng.uniform(-3,2,size=n-3)
    lam[3:]=rng.choice([-1,1],size=n-3)*mags
    A=(V*lam)@V.T
    hi=np.abs(lam)>=gamma
    P=V[:,hi]@V[:,hi].T
    D=A@A-gamma**2*P
    me=np.linalg.eigvalsh(D)[0]
    min_psd=min(min_psd,me)
    vp += me < -1e-8
    rowsq=np.sum(A*A,axis=1)
    for i in np.where(np.diag(P)>eta)[0]:
        heavy += 1
        vh += rowsq[i]+1e-12 < gamma**2*P[i,i]
        cross=np.sqrt(max(0.0,rowsq[i]-A[i,i]**2))
        vs += (abs(A[i,i])<=split and cross<=split)
    P0=V[:,:3]@V[:,:3].T
    rest=np.abs(lam[3:])>=gamma
    PR=V[:,3:][:,rest]@V[:,3:][:,rest].T if np.any(rest) else np.zeros((n,n))
    err=np.linalg.norm(P-(P0+PR),2)
    max_add=max(max_add,err)
    va += err>1e-9

print({
 'trials':trials,
 'heavy_coordinate_tests':heavy,
 'violations_psd':int(vp),
 'violations_heavy_row':int(vh),
 'violations_pivot_cross_split':int(vs),
 'violations_projector_additivity':int(va),
 'minimum_numeric_psd_eigenvalue':min_psd,
 'maximum_projector_additivity_operator_error':max_add,
 'gamma':gamma,
 'eta':eta,
 'hub_threshold':hub,
 'pivot_cross_threshold':split,
 'ridge_density_constant':288*sqrt(3*e)/13,
})
