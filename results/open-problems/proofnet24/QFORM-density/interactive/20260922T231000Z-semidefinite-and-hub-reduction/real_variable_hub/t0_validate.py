try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Validation of fibre_density.py against the hub-conditional estimator (condition on X', integrate X_h exactly).
import numpy as np, time, sys
sys.path.insert(0, r'~\AppData\Local\Temp\claude\<project>\9bfb8ed3-a0b8-4b06-94b3-3777f80a6d98\scratchpad\wave2\14_real_variable_hub_dense')
from fibre_density import Law, density
rng = np.random.default_rng(1)
n1 = 40; n = n1 + 1
Qm, _ = np.linalg.qr(rng.normal(size=(n1, 3))); w, v, u = Qm[:, 0], Qm[:, 1], Qm[:, 2]
# Q = 2 X_h (L + beta) + lam V^2 + mu B ,  B = <u, X'>
lam, beta, mu = 1.0, 0.1, 0.7
A = np.zeros((n, n)); A[0, 1:] = w; A[1:, 0] = w; A[1:, 1:] += lam * np.outer(v, v)
b = np.zeros(n); b[0] = 2 * beta; b[1:] = mu * u
laws = [Law('unif', rng) for _ in range(n)]
svals = np.linspace(-0.3, 0.9, 7)
t = time.time()
m, sd = density(A, b, laws, svals, 20000)
print('fibre     :', np.round(m, 3), ' sd', np.round(sd, 3), f'{time.time()-t:.1f}s', flush=True)
# hub-conditional estimator: p(s) = E[ f_h((s - F)/(2t)) / (2|t|) ], F = lam V^2 + mu B, t = L + beta
N = 400000
Xp = rng.uniform(-0.5, 0.5, (N, n1)); L = Xp @ w; V = Xp @ v; B = Xp @ u
tt = L + beta; F = lam * V ** 2 + mu * B
est = [np.mean(((np.abs((s - F) / (2 * tt)) < 0.5)) / (2 * np.abs(tt))) for s in svals]
print('hub-cond  :', np.round(est, 3), flush=True)
