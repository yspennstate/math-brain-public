"""T325 move (agent A, 16 Oct 2026): scalar-preconditioner reduction of an L-layer linear transformer, isotropic case.

If every layer's preconditioner is a multiple g_l of the identity, L layers compute L steps of GD from w0 = 0 with step sizes
g_1..g_L, and on noiseless data with w ~ N(0, I_d) the population in-context risk (per coordinate, d, N -> inf, q = d/N fixed) is
    R(g) = int prod_l (1 - g_l s)^2 dMP_q(s),
MP_q the Marchenko-Pastur law of S = X'X/N. The best degree-L residual polynomial with P(0) = 1 (no real-root constraint) is a
convex quadratic problem; it gives the floor R*_L. Question measured: from many starts, does gradient descent on g reach R*_L,
or does it stop at other local minima (e.g. coincident steps)? Also with label noise sigma^2:
    R_sig(g) = int [ P(s)^2 + sigma^2 q (1 - P(s))^2 / s ] dMP_q(s)        (variance of the GD iterate; per coordinate, x d/N)
and the Bayes (ridge, lambda = sigma^2 q... ) floor is computed from the same nodes for comparison.
"""
import numpy as np
from scipy.optimize import minimize


def mp_nodes(q, m=6000):
    a, b = (1 - np.sqrt(q)) ** 2, (1 + np.sqrt(q)) ** 2
    t = (np.arange(m) + 0.5) / m
    s = a + (b - a) * (1 - np.cos(np.pi * t)) / 2           # Chebyshev-spaced nodes, denser at the edges
    ds = (b - a) * np.pi * np.sin(np.pi * t) / (2 * m)
    dens = np.sqrt(np.maximum((b - s) * (s - a), 0)) / (2 * np.pi * q * s)
    w = dens * ds
    return s, w / w.sum()


def risk_and_grad(g, s, w, sig2, q):
    F = 1 - np.outer(g, s)                                  # (L, m)
    P = F.prod(axis=0)
    integrand = P ** 2 + sig2 * q * (1 - P) ** 2 / s
    R = integrand @ w
    grad = np.empty_like(g)
    for l in range(len(g)):
        dP = -s * np.prod(np.delete(F, l, axis=0), axis=0)
        grad[l] = ((2 * P - 2 * sig2 * q * (1 - P) / s) * dP) @ w
    return R, grad


def floor_poly(L, s, w, sig2, q):
    # P(s) = 1 + sum_k c_k s^k, k = 1..L ; minimise the same integrand (quadratic in c)
    V = np.stack([s ** k for k in range(1, L + 1)], 1)       # (m, L)
    A = (V * w[:, None]).T @ V * (1 + sig2 * q * 0) + sig2 * q * (V * (w / s)[:, None]).T @ V
    bvec = -(V * w[:, None]).T @ np.ones_like(s)            # from P^2 = (1 + Vc)^2 ; noise term (Vc)^2/s has no linear part
    c = np.linalg.solve(A, bvec)
    P = 1 + V @ c
    return float((P ** 2 + sig2 * q * (1 - P) ** 2 / s) @ w), np.sort(np.roots(np.r_[c[::-1], 1]).real)


def ridge_floor(s, w, sig2, q):
    # posterior-mean / ridge residual in the same units: per-eigen risk of the optimal linear shrink h(s) = s/(s+lam)
    best = None
    for lam in np.geomspace(1e-6, 10, 400):
        P = lam / (s + lam)
        R = float((P ** 2 + sig2 * q * (1 - P) ** 2 / s) @ w)
        best = R if best is None or R < best else best
    return best


if __name__ == "__main__":
    rng = np.random.default_rng(325)
    for q in (0.25, 0.5):
        s, w = mp_nodes(q)
        b = (1 + np.sqrt(q)) ** 2
        for sig2 in (0.0, 0.25):
            for L in (1, 2, 3, 4, 6):
                fl, roots = floor_poly(L, s, w, sig2, q)
                ends = []
                for k in range(200):
                    g0 = rng.uniform(0, 3.0 / b * 2, L)
                    r = minimize(risk_and_grad, g0, args=(s, w, sig2, q), jac=True, method="L-BFGS-B",
                                 options=dict(maxiter=5000, gtol=1e-12, ftol=1e-15))
                    ends.append((r.fun, np.sort(r.x)))
                vals = np.array([e[0] for e in ends])
                gap = vals - fl
                hit = int((gap < 1e-7 * max(1.0, fl)).sum())
                worst = ends[int(vals.argmax())]
                rf = ridge_floor(s, w, sig2, q)
                print(f"q={q} sig2={sig2} L={L}: floor R*_L={fl:.4e} (roots->steps {np.round(1/np.array(roots[::-1]),3) if L<=4 else '...'}) "
                      f"| GD on steps: {hit}/200 reach floor, worst end {worst[0]:.4e} at g={np.round(worst[1],3)} "
                      f"| ridge floor {rf:.4e}", flush=True)
