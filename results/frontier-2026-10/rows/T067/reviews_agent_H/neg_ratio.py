# Is the -1/10 shift on g24 a real negative arm? K_shift = K - phi24/10, so it is negative iff K/phi24 < 1/10 somewhere.
import random
import numpy as np
from scipy.optimize import minimize
from fractions import Fraction as Fr
import cert_b1e as C
rng = random.Random(7)
def pts(x, ca, cb):
    a, _, _ = C.point(list(np.abs(x[:4]) + 1e-12), ca); b, _, _ = C.point(list(np.abs(x[4:]) + 1e-12), cb)
    return a, b
def phi24(a, b, m):
    A = sum(t * t for t in a); B = sum(t * t for t in b)
    return A * B * (A + B) - m * (A * A + B * B)
best = (9e9,)
for m in (0.0, float(C.M_END)):
    for trial in range(60):
        ca, cb = rng.randint(0, 1), rng.randint(0, 1)
        def f(x):
            a, b = pts(x, ca, cb); p = phi24(a, b, m)
            return float(C.K_direct(a, b, m)) / p if p > 1e-9 else 9e9
        x0 = np.array([rng.random() for _ in range(8)])
        r = minimize(f, x0, method='Nelder-Mead', options=dict(maxiter=1500, xatol=1e-9, fatol=1e-12))
        if r.fun < best[0]:
            a, b = pts(r.x, ca, cb)
            best = (r.fun, m, a, b, float(C.K_direct(a, b, m, Fr(-1, 10))))
print('min K/phi24 = %.5g at m=%s ; shifted K there %.4g' % (best[0], best[1], best[4]))
print('a', [round(t, 4) for t in best[2]], 'b', [round(t, 4) for t in best[3]])
