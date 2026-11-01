"""Independent check of T325 DOSSIER claims (agent A, 16 Oct): no code shared with gd_steps*.py / gap_rate.py.
MP_q (mean 1, variance q): density sqrt((b-s)(s-a))/(2 pi q s) on [a, b], a,b = (1 -+ sqrt q)^2. Quadrature: s = c - r cos(t),
Gauss-Legendre in t on [0, pi] with 4000 nodes. R(g) = int P^2 + lam (1 - P)^2 / s, lam = sigma^2 q, P = prod (1 - g_l s)."""
import json
import numpy as np
from scipy.optimize import minimize, minimize_scalar


def nodes(q, N=4000):
    a, b = (1 - q ** .5) ** 2, (1 + q ** .5) ** 2; c, r = (a + b) / 2, (b - a) / 2
    x, w = np.polynomial.legendre.leggauss(N); t = (x + 1) * np.pi / 2; w = w * np.pi / 2
    s = c - r * np.cos(t); dens = np.sqrt(np.maximum((b - s) * (s - a), 0)) / (2 * np.pi * q * s)
    return s, w * dens * r * np.sin(t)


def risk(g, s, w, lam):
    P = np.prod(1 - np.outer(g, s), axis=0)
    return float(np.sum(w * (P ** 2 + lam * (1 - P) ** 2 / s)))


out = []
for q in (0.25, 0.5):
    s, w = nodes(q); out.append({"q": q, "mass": float(w.sum()), "mean": float((w * s).sum()), "var": float((w * s * s).sum() - 1)})
    for L in (1, 2, 3, 4, 6):   # noiseless floor over all polynomials with P(0)=1: least squares in the monomial-free basis
        V = np.stack([s ** k for k in range(1, L + 1)], 1); A = (V * w[:, None]).T @ V; bb = (V * w[:, None]).T @ np.ones_like(s)
        cfs = np.linalg.solve(A, -bb); P = 1 + V @ cfs
        out.append({"q": q, "L": L, "noiseless_floor": float(np.sum(w * P * P)), "formula": 1 / sum(q ** -k for k in range(L + 1))})
    lam = 0.25 * q
    out.append({"q": q, "ridge_floor": float(np.sum(w * lam / (s + lam)))})
    # the q = 0.5 claim: (1 - 0.6004 s)^6 is the global real-step minimum, value 0.184571738; check value, gradient, Hessian
    if q == 0.5:
        r1 = minimize_scalar(lambda c: risk([c] * 6, s, w, lam), bounds=(0.3, 0.9), method="bounded")
        g0 = np.full(6, r1.x); h = 1e-5; H = np.zeros((6, 6)); f0 = risk(g0, s, w, lam)
        for i in range(6):
            for j in range(6):
                def fv(di, dj):
                    g = g0.copy(); g[i] += di; g[j] += dj; return risk(g, s, w, lam)
                H[i, j] = (fv(h, h) - fv(h, -h) - fv(-h, h) + fv(-h, -h)) / (4 * h * h)
        out.append({"q": q, "repeated_step": r1.x, "value": f0, "hess_min_eig": float(np.linalg.eigvalsh(H).min())})
        best = min((minimize(lambda g: risk(g, s, w, lam), np.random.default_rng(k).uniform(0, 6 / 2.914, 6), method="L-BFGS-B",
                             bounds=[(0, 3)] * 6).fun for k in range(40)))
        out.append({"q": q, "best_of_40_random_starts": best})
for o in out: print(json.dumps(o))
