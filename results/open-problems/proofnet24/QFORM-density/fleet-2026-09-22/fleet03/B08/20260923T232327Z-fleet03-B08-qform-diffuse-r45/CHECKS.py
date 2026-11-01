import math
import numpy as np

L = 1.0
C_ridge = 288*math.sqrt(3*math.e)/13
row = 1/(64*math.sqrt(32))
diag = 1/(512*math.sqrt(2))
off = math.sqrt(3/2)/512
sstar = 1/(64*math.sqrt(896))
Cstar = 2**(13/6)*math.sqrt(3)
eta619 = (Cstar/619)**3/sstar
heavy = (3*math.sqrt(6)/32)*eta619

assert C_ridge < 64
assert abs(row - 2*diag) < 1e-15
assert abs(off - math.sqrt(3)/2*row) < 1e-15
assert abs(eta619 - 0.0037987340155334467) < 1e-15
assert abs(heavy - 0.000872340000619756) < 1e-15

rng = np.random.default_rng(20260923)
max_factor_error = 0.0
violations = 0
for _ in range(1000):
    m = int(rng.integers(3, 20))
    B = rng.normal(size=(2,2)); B=(B+B.T)/2
    R = rng.normal(size=(2,2)); R=(R+R.T)/2
    M = rng.normal(size=(2,m))
    d = rng.uniform(-1/128,1/128,size=m)
    A0 = np.block([[B,M],[M.T,M.T@R@M]])
    A = A0 + np.diag(np.r_[np.zeros(2),d])
    T = np.block([[np.eye(2),np.zeros((2,m))],[np.zeros((2,2)),M]])
    K = np.block([[B,np.eye(2)],[np.eye(2),R]])
    max_factor_error=max(max_factor_error,float(np.linalg.norm(A0-T.T@K@T)))
    ss=np.linalg.svd(A,compute_uv=False)
    if len(ss)>=5 and ss[4] > np.max(np.abs(d))+1e-10:
        violations += 1
assert violations == 0
print('QFORM_B08_R45_CHECK_PASS')
print('C_ridge', C_ridge)
print('row', row, 'diag', diag, 'off', off)
print('sstar', sstar, 'Cstar', Cstar, 'eta619', eta619, 'heavy', heavy)
print('max_factor_error', max_factor_error, 'violations', violations)
