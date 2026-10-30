"""T325: classify the quadratic-factor end points (L = 4, 6, sigma^2 = 0.25): gradient norm, Hessian eigenvalues, factor discriminants."""
import numpy as np
from scipy.optimize import minimize
from gd_steps_landscape import mp_nodes
from quad_factors import risk_grad
rng = np.random.default_rng(11)
for q in (0.25, 0.5):
    s, w = mp_nodes(q); bb = (1 + np.sqrt(q))**2; lam = 0.25*q
    for L in (4, 6):
        seen = {}
        for k in range(200):
            g1, g2 = rng.uniform(0, 6/bb, L//2), rng.uniform(0, 6/bb, L//2)
            p0 = np.ravel(np.column_stack([g1 + g2, g1*g2]))
            r = minimize(risk_grad, p0, args=(s, w, lam), jac=True, method="L-BFGS-B", options=dict(maxiter=20000, gtol=1e-13, ftol=1e-16))
            seen.setdefault(round(r.fun, 8), []).append(r.x)
        for key in sorted(seen):
            p = seen[key][0]; f0, gr = risk_grad(p, s, w, lam); n = len(p); h = 1e-6; H = np.zeros((n, n))
            for i in range(n):
                e = np.zeros(n); e[i] = h
                H[:, i] = (risk_grad(p + e, s, w, lam)[1] - risk_grad(p - e, s, w, lam)[1])/(2*h)
            ev = np.linalg.eigvalsh((H + H.T)/2)
            a, b = p[0::2], p[1::2]; disc = a**2 - 4*b
            print(f"q={q} L={L} end {key} x{len(seen[key])}: |grad| {np.linalg.norm(gr):.1e} Hessian eig min {ev.min():+.2e} max {ev.max():.2e} | "
                  f"factors (a,b) {np.round(np.column_stack([a,b]),4).tolist()} disc {np.round(disc,4).tolist()}", flush=True)
