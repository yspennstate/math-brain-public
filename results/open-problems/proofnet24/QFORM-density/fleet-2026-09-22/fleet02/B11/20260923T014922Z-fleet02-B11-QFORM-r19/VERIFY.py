import math
import numpy as np

m = 16
eps = 1.0e-6
n = 2 + 2*m
S = np.zeros((n, 3))
S[0,0] = math.sqrt(1-eps)
S[1,0] = math.sqrt(eps)
S[2:2+m,1] = 1/math.sqrt(m)
S[2+m:,2] = 1/math.sqrt(m)
A0 = np.array([[0.,-1.,-1.],[-1.,0.,-1.],[-1.,-1.,0.]])
A = S @ A0 @ S.T

assert np.max(np.abs(S.T @ S - np.eye(3))) < 1e-12
assert np.max(np.abs(np.diag(A))) < 1e-12
vals = np.linalg.eigvalsh(A)
nz = vals[np.abs(vals) > 1e-10]
assert np.max(np.abs(nz - np.array([-2.,1.,1.]))) < 1e-10
max_pair = np.max(np.abs(A - np.diag(np.diag(A))))
assert max_pair <= 1/math.sqrt(m) + 1e-12
lev = np.diag(S @ S.T)
assert abs(lev[0] - (1-eps)) < 1e-12
assert abs(lev[1] - eps) < 1e-12
D0 = 2*eps*(1-eps)*(1-1/m)**2
partner_C = 3*2**(4/3)
claude_C = 2*math.pi/math.sqrt(3)

print('orth_error', np.max(np.abs(S.T @ S - np.eye(3))))
print('diag_error', np.max(np.abs(np.diag(A))))
print('nonzero_eigs', nz.tolist())
print('max_pair', max_pair)
print('pair_cap', 1/math.sqrt(m))
print('heavy_leverage', lev[0])
print('D0_ordered_formula', D0)
print('partner_global_constant', partner_C)
print('claude_one_sheet_constant', claude_C)
print('QFORM_NEAR_COLOOP_CONDITIONING_LOSS_CHECK_PASS')
