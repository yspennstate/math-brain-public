import math
import numpy as np

rng = np.random.default_rng(20260922)
M = rng.normal(size=(4,4))
Q,_ = np.linalg.qr(M)
# abs eigenvalues 1.5,1,0.625,0, so s2(S)=1 exactly up to floating arithmetic.
eigs = np.array([1.5,-1.0,0.625,0.0])
S = Q @ np.diag(eigs) @ Q.T
ell = rng.normal(size=4)
z = rng.normal(size=4)

print("QFORM_B19_R18_CHECK")
print("s2(S)=", sorted(np.linalg.svd(S, compute_uv=False), reverse=True)[1])
for eps in [0.2,0.05,0.01,0.001]:
    Se = S + eps*np.eye(4)
    h = 0.5*np.linalg.solve(Se, ell)
    lhs = z@Se@z + ell@z
    rhs = (z+h)@Se@(z+h) - h@Se@h
    s2 = sorted(np.linalg.svd(Se, compute_uv=False), reverse=True)[1]
    print(eps, "s2=", s2, "lower=", 1-eps, "completion_err=", abs(lhs-rhs))

same = 2*math.sqrt(2*math.pi*math.e)
general = 128*math.sqrt(math.e)
print("SAME_SIGN_CONST", same)
print("GENERAL_SIGN_CONST", general)
for m in [3,5,10,100]:
    bank = (m-1)/(2*m)
    maxdet = 1/m**2
    print("m",m,"S2bank",bank,"maxdet",maxdet)

assert same < 8.266
assert general < 211.037
assert all((m-1)/(2*m) >= 1/3 for m in [3,5,10,100])
print("QFORM_B19_R18_CHECK_PASS")
