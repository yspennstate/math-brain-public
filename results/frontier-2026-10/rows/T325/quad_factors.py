"""T325 repair (ii): parametrize P(s) = prod_{i=1}^{L/2} (1 - a_i s + b_i s^2) (each factor = two layers whose steps may be a complex pair,
or a 2x2 block). Does gradient descent from random starts reach the polynomial floor where real steps had several strict minima?"""
import numpy as np
from scipy.optimize import minimize
from gd_steps_landscape import mp_nodes
rng = np.random.default_rng(11)

def risk_grad(p, s, w, lam):
    a, b = p[0::2], p[1::2]; F = 1 - np.outer(s, a) + np.outer(s**2, b)      # nodes x factors
    P = F.prod(1)
    dR_dP = 2*w*(P - lam*(1 - P)/s)
    g = np.empty_like(p)
    for i in range(len(a)):
        others = np.delete(F, i, 1).prod(1)
        g[2*i] = np.sum(dR_dP*(-s)*others); g[2*i + 1] = np.sum(dR_dP*(s**2)*others)
    return np.sum(w*(P**2 + lam*(1 - P)**2/s)), g

if __name__ == "__main__":
      for q in (0.25, 0.5):
        s, w = mp_nodes(q); bb = (1 + np.sqrt(q))**2; sig2 = 0.25; lam = sig2*q
        for L in (4, 6):
            V = np.stack([s**k for k in range(1, L + 1)], 1)
            A = (V*w[:, None]).T @ V + lam*(V*(w/s)[:, None]).T @ V
            c = np.linalg.solve(A, -(V*w[:, None]).T @ np.ones_like(s)); P = 1 + V @ c
            floor = np.sum(w*(P**2 + lam*(1 - P)**2/s))
            ends = []
            for k in range(200):
                g1, g2 = rng.uniform(0, 6/bb, L//2), rng.uniform(0, 6/bb, L//2)        # start = a real-step pair (g1, g2)
                p0 = np.ravel(np.column_stack([g1 + g2, g1*g2]))
                r = minimize(risk_grad, p0, args=(s, w, lam), jac=True, method="L-BFGS-B", options=dict(maxiter=20000, gtol=1e-13, ftol=1e-16))
                ends.append(r.fun)
            ends = np.array(ends)
            print(f"q={q} sig2={sig2} L={L}: floor {floor:.9f} | quadratic factors: {np.sum(ends - floor < 1e-8)}/200 within 1e-8, "
                  f"worst {ends.max():.9f}, distinct (8 dp) {len(np.unique(np.round(ends, 8)))}", flush=True)
