import itertools
import math
import mpmath as mp
import numpy as np


def P(r):
    return 4 * (2-r)**((r-3)/2) * r**(-r/2)


def C(q,k,r):
    K = (1/k) * mp.beta(mp.mpf(1)/(2*k), mp.mpf(r)/(4*q)-mp.mpf(1)/(2*k))
    return P(r) * math.sqrt(math.e) * 2**(-3/4) * q**(-1/4) * math.sqrt(float(K))


def flat_frame(m):
    u1 = np.ones(m)/math.sqrt(m)
    u2 = np.r_[np.ones(m//2), -np.ones(m//2)]/math.sqrt(m)
    return np.column_stack([u1,u2])

print('C_q1_k2_r3/2=', repr(C(1,2,1.5)))
print('C_q2_k3_r3/2=', repr(C(2,3,1.5)))
for m in (4,8,16,32):
    U=flat_frame(m)
    B=U@U.T
    sv=np.linalg.svd(B, compute_uv=False)
    leverage=float(np.max(np.sum(U*U,axis=1)))
    E2=0.0
    mx=0.0
    for R in itertools.combinations(range(m),2):
        for T in itertools.combinations(range(m),2):
            d=float(np.linalg.det(B[np.ix_(R,T)]))
            E2 += d*d
            mx=max(mx,abs(d))
    print('m=',m,'s1=',sv[0],'s2=',sv[1],'leverage=',leverage,'E2=',E2,
          'max_minor=',mx,'m2_times_max_minor=',m*m*mx)
    assert abs(sv[0]-1)<1e-10 and abs(sv[1]-1)<1e-10
    assert abs(leverage-2/m)<1e-10
    assert abs(E2-1)<1e-9
    assert abs(m*m*mx-4)<1e-8
print('QFORM_SQUARE_PIVOT_EK_CHECK_PASS')
