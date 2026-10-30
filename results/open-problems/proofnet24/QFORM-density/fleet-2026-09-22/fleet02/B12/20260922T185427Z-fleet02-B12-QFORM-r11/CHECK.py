import math
import numpy as np

rng=np.random.default_rng(20260922185427)
worst_gap=1e9
tests=0
for n in range(4,10):
    for r in range(1,min(4,n)):
        for _ in range(80):
            M=rng.normal(size=(n,n))
            A=(M+M.T)/2
            B=A[:r,:r].copy()
            B += np.eye(r)*(1.0+np.linalg.norm(B,2))
            A[:r,:r]=B
            E=A[:r,r:]
            C=A[r:,r:]
            S=C-E.T@np.linalg.inv(B)@E
            sA=np.linalg.svd(A,compute_uv=False)
            sS=np.linalg.svd(S,compute_uv=False)
            gaps=sS-sA[r:r+len(sS)]
            if gaps.min() < -1e-9:
                raise AssertionError((n,r,gaps.min()))
            worst_gap=min(worst_gap,float(gaps.min()))
            tests += len(gaps)

rho=1/(156*math.sqrt(2))
alpha0=4/(math.sqrt(7)+math.sqrt(3))**2
old=8/(alpha0*rho)
new=8/rho
ratio=old/new

delta=rho/2
F=4/delta
max_err=0.0
for B0 in [1,17,100,10000]:
    x=B0
    for k in range(1,9):
        x=2*math.sqrt(x/delta)
        formula=F**(1-2**(-k))*B0**(2**(-k))
        max_err=max(max_err,abs(x-formula)/max(1,abs(formula)))
assert max_err < 1e-12

print('PASS')
print('singular_value_comparisons',tests)
print('minimum_gap_sjS_minus_sjrA',worst_gap)
print('rho',rho)
print('alpha0',alpha0)
print('partner_fixed_point',old)
print('lossless_fixed_point_theta_half',new)
print('improvement_factor',ratio)
print('recurrence_max_relative_error',max_err)
