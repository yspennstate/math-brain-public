import math
import numpy as np

rng=np.random.default_rng(20260923)
max_rel=0.0
for _ in range(1000):
    m=int(rng.integers(3,10)); n=int(rng.integers(3,10))
    B=rng.normal(size=(m,n))
    i=int(rng.integers(m)); a=int(rng.integers(n))
    rows=[j for j in range(m) if j!=i]
    cols=[k for k in range(n) if k!=a]
    b=B[i,a]; r=B[i,cols]; c=B[rows,a]; D=B[np.ix_(rows,cols)]
    lhs=0.0
    for j in rows:
        for k in cols:
            det=B[i,a]*B[j,k]-B[i,k]*B[j,a]
            lhs += det*det
    rhs=float(np.linalg.norm(b*D-np.outer(c,r),'fro')**2)
    rel=abs(lhs-rhs)/max(1.0,abs(lhs),abs(rhs))
    max_rel=max(max_rel,rel)

eps=1/256
live_anchor=(1-2*eps)/4*(16/25)
live_cofactor=math.sqrt(live_anchor)
live_dichotomy=live_cofactor/2

N=37; M=53
u=np.zeros(N+1); u[1:]=1/math.sqrt(N)
v=np.zeros(M+1); v[1:]=1/math.sqrt(M)
eL=np.zeros(N+1); eL[0]=1
eR=np.zeros(M+1); eR[0]=1
B=np.outer(eL,v)+np.outer(u,eR)
s=np.linalg.svd(B,compute_uv=False)
z2=0.0; maxminor=0.0
for i in range(N+1):
    for j in range(i+1,N+1):
        for a in range(M+1):
            for b in range(a+1,M+1):
                det=B[i,a]*B[j,b]-B[i,b]*B[j,a]
                z2 += det*det
                maxminor=max(maxminor,abs(det))

base=math.e*math.sqrt(2*math.pi)
partner=2*math.sqrt(base)
print(f'max_relative_anchor_identity_error={max_rel:.3e}')
print(f'live_anchor_Z_fraction_of_G4={live_anchor:.12f}')
print(f'live_cofactor_norm_fraction_of_G2={live_cofactor:.12f}')
print(f'live_schur_or_star_fraction_of_G2={live_dichotomy:.12f}')
print(f'double_star_top_singular_values={s[0]:.12f},{s[1]:.12f}')
print(f'double_star_Z2={z2:.12f}')
print(f'double_star_max_local_minor={maxminor:.12f}')
print(f'fleet04_B18_applied_bound={partner:.12f}')
assert max_rel < 1e-12
assert abs(live_anchor-127/800) < 1e-15
assert abs(z2-1) < 1e-12
assert abs(s[0]-1) < 1e-12 and abs(s[1]-1) < 1e-12
print('QFORM_B06_R28_CHECK_PASS')
