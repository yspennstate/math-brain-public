"""T325 Target 1, second half: risk gap of the best degree-L residual polynomial (P(0)=1, complex roots allowed) to ridge, against the
Bernstein-ellipse prediction rho^(-2L), rho the ellipse parameter of the ridge pole s = -sigma^2 q relative to the MP_q support [a, b].
Basis: P(s) = 1 + s Q(s), Q in Chebyshev polynomials of the mapped variable (well conditioned up to L ~ 20)."""
import numpy as np
from gd_steps_landscape import mp_nodes, ridge_floor
for q in (0.25, 0.5):
    s, w = mp_nodes(q); a, b = (1 - np.sqrt(q))**2, (1 + np.sqrt(q))**2
    x = (2*s - a - b)/(b - a)
    for sig2 in (0.0, 0.25, 1.0):
        lam = sig2*q
        x0 = (-2*lam - a - b)/(b - a); rho = abs(x0) + np.sqrt(x0**2 - 1)
        R_ridge = np.sum(w*lam/(s + lam)) if sig2 > 0 else 0.0   # pointwise ridge risk lam/(s+lam), same nodes
        gaps = []
        for L in range(1, 17):
            B = np.stack([s*np.cos(k*np.arccos(np.clip(x, -1, 1))) for k in range(L)], 1)   # s T_k(x)
            # R = sum w [P^2 + lam (1-P)^2/s],  P = 1 + B c,  1-P = -B c
            A = (B*w[:, None]).T @ B + lam*(B*(w/s)[:, None]).T @ B
            c = np.linalg.solve(A, -(B*w[:, None]).T @ np.ones_like(s))
            P = 1 + B @ c
            R = np.sum(w*(P**2 + lam*(1 - P)**2/s))
            if L == 1 and sig2 > 0: print(f'  (check: ridge on these nodes {R_ridge:.8f}, ridge_floor() {ridge_floor(s, w, sig2, q):.8f})')
            gaps.append(R - R_ridge)
        g = np.array(gaps); ratio = g[1:]/g[:-1]
        print(f"q={q} sig2={sig2}: rho^-2={rho**-2:.5f} | gap L=1..16 {np.array2string(g[[0,3,7,11,15]], precision=3)} (L=1,4,8,12,16)"
              f" | successive ratios L=12..16 {np.array2string(ratio[-5:], precision=5)}", flush=True)
