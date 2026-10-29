# Local search from the peer's m=M point: is min K/phi24 below 0.1036 (= the real g24 change of the -1/10 arm)?
import numpy as np
from scipy.optimize import minimize
from fractions import Fraction as Fr
import cert_b1e as C
m = float(C.M_END)
def phi24(a, b):
    A = sum(t * t for t in a); B = sum(t * t for t in b); return A * B * (A + B) - m * (A * A + B * B)
a0 = [-0.3107, -0.4837, -0.2757, 1.0701]; b0 = [-0.2517, -0.4117, 0.8964, -0.2331]
print('peer point: K/phi24 = %.5f' % (float(C.K_direct(a0, b0, m)) / phi24(a0, b0)), 'sum a', sum(a0), 'sum b', sum(b0))
print('VERT', C.VERT)
# parametrize directly: a, b in R^4 with sum 0 projected; domain membership checked via barycentric coords on VERT
V = np.array(C.VERT, dtype=float)
def bary(x):
    # solve x = sum lam_k V_k, sum lam = 1  (V is 4x4; use lstsq on augmented system)
    Mx = np.vstack([V.T, np.ones(4)]); lam, *_ = np.linalg.lstsq(Mx, np.append(x, 1), rcond=None); return lam
print('bary a0', np.round(bary(np.array(a0)), 4), 'bary b0', np.round(bary(np.array(b0)), 4))
def f(y):
    la, lb = np.abs(y[:4]), np.abs(y[4:]); la = la / la.sum(); lb = lb / lb.sum()
    a = la @ V; b = lb @ V; p = phi24(a, b)
    return float(C.K_direct(list(a), list(b), m)) / p if p > 1e-9 else 9e9
best = 9e9
rng = np.random.default_rng(3)
y0 = np.concatenate([np.abs(bary(np.array(a0))), np.abs(bary(np.array(b0)))])
for t in range(40):
    y = y0 * np.exp(0.3 * rng.standard_normal(8)) if t else y0
    r = minimize(f, y, method='Nelder-Mead', options=dict(maxiter=4000, xatol=1e-10, fatol=1e-13))
    if r.fun < best:
        best = r.fun; yb = r.x
la, lb = np.abs(yb[:4]) / np.abs(yb[:4]).sum(), np.abs(yb[4:]) / np.abs(yb[4:]).sum()
print('min K/phi24 near peer point = %.5f' % best, 'lam a', np.round(la, 4), 'lam b', np.round(lb, 4))
a = la @ V; b = lb @ V
print('K true %.4g, K at shift -1/10 %.4g' % (float(C.K_direct(list(a), list(b), m)), float(C.K_direct(list(a), list(b), m, Fr(-1, 10)))))
