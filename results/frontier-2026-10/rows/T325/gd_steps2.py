"""T325 check 2: noisy case, L = 4, 6 - are the floor roots complex, and how many distinct real-step end values does GD reach?"""
import numpy as np
from scipy.optimize import minimize
from gd_steps_landscape import mp_nodes, risk_and_grad, ridge_floor
rng = np.random.default_rng(7)
for q in (0.25, 0.5):
    s, w = mp_nodes(q); b = (1 + np.sqrt(q))**2
    # noiseless closed form check: 1/sum_{k<=L} q^-k
    for L in (4, 6):
        sig2 = 0.25
        V = np.stack([s**k for k in range(1, L+1)], 1)
        A = (V*w[:, None]).T @ V + sig2*q*(V*(w/s)[:, None]).T @ V
        c = np.linalg.solve(A, -(V*w[:, None]).T @ np.ones_like(s))
        roots = np.roots(np.r_[c[::-1], 1])
        ends = []
        for k in range(200):
            r = minimize(risk_and_grad, rng.uniform(0, 6/b, L), args=(s, w, sig2, q), jac=True, method="L-BFGS-B",
                         options=dict(maxiter=5000, gtol=1e-12, ftol=1e-15))
            ends.append(r.fun)
        ends = np.array(ends); best = ends.min()
        vals = np.unique(np.round(ends, 7))
        print(f"q={q} sig2={sig2} L={L}: floor roots {np.round(roots,3)} | real-step ends: best {best:.6e}, distinct (7 dp) {len(vals)}, "
              f"share within 1e-7 of best {np.mean(ends-best<1e-7):.2f}, values {vals[:6]} | ridge {ridge_floor(s,w,sig2,q):.6e}", flush=True)
