# Deterministic sanity checks for fleet03/B13 r27.
# These checks do not replace the proofs in REPORT.md.
import itertools
import numpy as np

rng=np.random.default_rng(20260923)
m,d=7,3
U,_=np.linalg.qr(rng.normal(size=(m,d)))
U=U[:,:d]
lam=np.array([2.0,-1.5,0.8])
R=U@np.diag(lam)@U.T
pdet=abs(np.prod(lam))
lev=np.sum(U*U,axis=1)
star=np.zeros(m)
total=0.0
for I in itertools.combinations(range(m),d):
    v=abs(np.linalg.det(R[np.ix_(I,I)]))
    total += v
    for j in I:
        star[j]+=v
assert abs(total-pdet)<1e-12
assert np.max(np.abs(star/pdet-lev))<1e-12
assert max(4*k/(k-2) for k in range(3,101))==12.0
assert 2*12*(1+2*0.5)==48.0
print('QFORM_B13_R27_RANGE_STAR_CHECK_PASS')
print('total_abs_principal_volume=',total)
print('pdet=',pdet)
print('max_star_identity_error=',np.max(np.abs(star/pdet-lev)))
print('max_range_constant_d_ge_3=',max(4*k/(k-2) for k in range(3,101)))
