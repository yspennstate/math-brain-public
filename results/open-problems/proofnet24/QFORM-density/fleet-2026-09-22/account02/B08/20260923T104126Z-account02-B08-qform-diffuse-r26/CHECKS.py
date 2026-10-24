from fractions import Fraction
import math
import numpy as np


def hadamard(m):
    H=np.array([[1.0]])
    while H.shape[0] < m:
        H=np.block([[H,H],[H,-H]])
    return H/math.sqrt(m)


def e2_singular(M):
    s=np.linalg.svd(M,compute_uv=False)
    x=s*s
    return sum(x[i]*x[j] for i in range(len(x)) for j in range(i+1,len(x)))


def delta_formula(k,d):
    if k==1:
        s=7/5-d
        return (768/625)*((1-d)**2+d*d/8)/(s*s)
    s=11/5-2*d
    return (48/25)*(2*(1-d)**2*d*d+d**4/16)/(s*s)

beta=3/16*math.sqrt(3/5)
eta=1/64
C1=5*math.sqrt(2*math.e)*beta**(-2/5)*eta**(-3/5)
C2=5*math.sqrt(2*math.e)*beta**(-1/5)*eta**(-4/5)
assert C1 < 306 and C2 < 478

# Exact endpoint constants from the symbolic derivative checks in REPORT.md.
delta1_min=Fraction(62304,105625)
ratio2_min=Fraction(7779,10000)
assert float(delta1_min) > 0.5898
assert float(ratio2_min) > 0.7778

partner_k1=36.45/math.sqrt(1.3)*float(delta1_min)**(-1/8)
partner_k2=36.45/math.sqrt(2.0)*float(ratio2_min)**(-1/8)
assert partner_k1 < 34.15
assert partner_k2 < 26.60

F1=6*((4/5)*(3/5)**2)**(-1/6)
F2=6*((4/5)**2*(3/5))**(-1/6)
assert F1 < 7.384 and F2 < 7.038

maxerr=0.0
for m in (8,16,32):
    U=hadamard(m)[:,:3]
    for k in (1,2):
        for d in (0.001,0.01,0.1):
            p=np.array([1-d]*k+[0.2]*(3-k))
            P=np.diag(p)
            Q=np.eye(3)-P
            D=U@P@U.T
            B=U@Q@U.T
            a=D[0,0]
            M=B[1:,:]-np.outer(D[1:,0],B[0,:])/a
            err=abs(e2_singular(M)-delta_formula(k,d))
            maxerr=max(maxerr,err)
            assert err < 2e-12
            svals=np.linalg.svd(M,compute_uv=False)
            assert svals[2] < 2e-12

print('QFORM_B08_R26_CHECK_PASS')
print('beta_gate=',repr(beta))
print('D5_k1_eta_1_64=',repr(C1))
print('D5_k2_eta_1_64=',repr(C2))
print('delta1_min=',float(delta1_min),'fraction=62304/105625')
print('partner_k1_sqrtm_coeff=',repr(partner_k1))
print('delta2_over_d2_min=',float(ratio2_min),'fraction=7779/10000')
print('partner_k2_sqrtm_dminusquarter_coeff=',repr(partner_k2))
print('F_k1=',repr(F1))
print('F_k2=',repr(F2))
print('finite_matrix_max_abs_error=',repr(maxerr))
