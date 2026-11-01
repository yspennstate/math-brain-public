"""T325 check 3: at the distinct real-step end values with noise (L = 6), gradient norm and Hessian eigenvalues - strict local minima or stalls?"""
import numpy as np
from scipy.optimize import minimize
from gd_steps_landscape import mp_nodes, risk_and_grad
rng = np.random.default_rng(7)
for q in (0.25, 0.5):
    s, w = mp_nodes(q); b = (1 + np.sqrt(q))**2; sig2 = 0.25; L = 6
    seen = {}
    for k in range(200):
        r = minimize(risk_and_grad, rng.uniform(0, 6/b, L), args=(s, w, sig2, q), jac=True, method="L-BFGS-B",
                     options=dict(maxiter=5000, gtol=1e-12, ftol=1e-15))
        key = round(r.fun, 7)
        seen.setdefault(key, []).append(np.sort(r.x))
    for key in sorted(seen):
        g = seen[key][0]
        # polish with Newton-free BFGS from the end point, then finite-difference Hessian of the gradient
        r = minimize(risk_and_grad, g, args=(s, w, sig2, q), jac=True, method="BFGS", options=dict(gtol=1e-13, maxiter=20000))
        g = r.x; f0, gr = risk_and_grad(g, s, w, sig2, q)
        h = 1e-6; H = np.zeros((L, L))
        for i in range(L):
            e = np.zeros(L); e[i] = h
            H[:, i] = (risk_and_grad(g + e, s, w, sig2, q)[1] - risk_and_grad(g - e, s, w, sig2, q)[1])/(2*h)
        ev = np.linalg.eigvalsh((H + H.T)/2)
        print(f"q={q} L=6 end {key} x{len(seen[key])}: polished {f0:.9f} |grad| {np.linalg.norm(gr):.1e} steps {np.round(np.sort(g),4)} "
              f"Hessian eig min/max {ev.min():.2e}/{ev.max():.2e}", flush=True)
