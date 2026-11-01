# -*- coding: utf-8 -*-
"""The one quantity the Poisson limit for P0016 needs.

Exact reduction.  Let S, S' be two M-subsets of the 2M-1 rows with C = S cap S', |C| = k.
The rows S\\C and S'\\C are disjoint and independent of each other and of A_C, so
CONDITIONALLY ON A_C the two events {sigma_min(A_S) <= eps} and {sigma_min(A_S') <= eps} are
INDEPENDENT.  Writing

    phi_eps(B) = P( sigma_min([B ; G]) <= eps ),   B a k x M matrix, G an (M-k) x M Gaussian,

we get exactly  P(both) = E[phi_eps(A_C)^2]  and  P(one) = E[phi_eps(A_C)] = p.  Hence

    P(both)/p^2 = 1 + rho_k,     rho_k := Var(phi_eps(A_C)) / E[phi_eps(A_C)]^2 .

With Y = #{S : sigma_min(A_S) <= eps},  E[Y(Y-1)] = p^2 ( N(N-1) + sum_k N_k rho_k ), so the
Poisson limit 4^M omega => Exp holds as soon as sum_k (N_k/N^2) rho_k -> 0, where N_k/N^2 is the
hypergeometric law of the overlap, concentrated at k ~ M/2.

phi_eps(B) depends on B only through its singular values (left and right orthogonal invariance),
and for k ~ M/2 those obey a Marchenko-Pastur law, so rho_k should vanish.  THIS SCRIPT MEASURES
rho_k, which is the whole content.
"""
import numpy as np, sys, time
rng = np.random.default_rng(5150)

def rho_k(M, k, nB=300, nG=20000, eps=None):
    """relative variance of phi_eps(B) over B ~ k x M Gaussian."""
    if eps is None:
        eps = 0.02 / np.sqrt(M)       # small enough that phi ~ kappa_M eps
    phis = np.empty(nB)
    for b in range(nB):
        B = rng.standard_normal((k, M))
        G = rng.standard_normal((nG, M-k, M))
        full = np.concatenate([np.broadcast_to(B, (nG, k, M)), G], axis=1)
        s = np.linalg.svd(full, compute_uv=False)[:, -1]
        phis[b] = np.mean(s <= eps)
    m = phis.mean()
    # subtract the binomial sampling noise from the measured variance
    v_raw = phis.var(ddof=1)
    v_noise = m*(1-m)/nG
    v = max(v_raw - v_noise, 0.0)
    return m, v/m**2 if m > 0 else np.nan, v_raw/m**2 if m > 0 else np.nan, eps

print("rho_k = Var(phi_eps(A_C))/E[phi_eps(A_C)]^2 ; the Poisson limit needs rho_k -> 0 at k ~ M/2")
print(" M   k   E[phi]      rho_k (noise-corrected)   rho_k (raw)   eps")
for M in [6, 8, 10, 12]:
    for k in sorted(set([1, 2, max(1, M//4), M//2, (3*M)//4, M-2, M-1])):
        if k < 1 or k > M-1: continue
        t0 = time.time()
        nG = 20000 if M <= 8 else 12000
        m, r, rraw, eps = rho_k(M, k, nB=250, nG=nG)
        print(f"{M:3d} {k:3d}  {m:.5f}     {r:8.4f}                 {rraw:8.4f}     {eps:.4f}   ({time.time()-t0:.0f}s)")
        sys.stdout.flush()
