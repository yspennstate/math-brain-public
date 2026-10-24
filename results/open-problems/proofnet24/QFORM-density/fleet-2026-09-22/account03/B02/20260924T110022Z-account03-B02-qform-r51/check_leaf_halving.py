#!/usr/bin/env python3
import math
import numpy as np

SEED = 2026092411
RNG = np.random.default_rng(SEED)
ALPHA = 1.0 / 228.0
TAU = math.sqrt(113.0 / 456.0)
RHO = 1.0
CUT = RHO / 38.0
HUB = RHO / 456.0

def svals(M):
    return np.linalg.svd(M, compute_uv=False)

def proj_diag_abs_ge(D, cut):
    w, U = np.linalg.eigh(D)
    mask = np.abs(w) >= cut
    if not np.any(mask):
        return np.zeros(D.shape[0])
    return np.sum(U[:, mask] ** 2, axis=1)

assert abs((ALPHA + math.sqrt(ALPHA*ALPHA + 4*TAU*TAU))/2 - 0.5) < 2e-15

trials = 0
spectral_violations = 0
hub_violations = 0
max_star_norm_over_half = 0.0
min_weyl_margin = float("inf")
min_hub_margin = float("inf")

for n in range(4, 11):
    for _ in range(600):
        c = RNG.uniform(-ALPHA, ALPHA)
        d = RNG.normal(size=n-1)
        d /= np.linalg.norm(d)
        d *= RNG.uniform(0.0, TAU)

        G = RNG.normal(size=(n-1, n-1))
        D = (G + G.T) / 2.0
        sd = svals(D)
        D *= 2.0 / max(sd[1], 1e-12)

        S = np.zeros((n, n))
        S[0, 0] = c
        S[0, 1:] = d
        S[1:, 0] = d
        S[1:, 1:] = D

        while svals(S)[1] < 1.0:
            D *= 1.25
            S[1:, 1:] = D

        trials += 1
        s2S = svals(S)[1]
        s2D = svals(D)[1]
        star_norm = (abs(c) + math.sqrt(c*c + 4*np.dot(d,d))) / 2.0
        max_star_norm_over_half = max(max_star_norm_over_half, star_norm / 0.5)

        margin = s2D - (s2S - star_norm)
        min_weyl_margin = min(min_weyl_margin, margin)
        if margin < -2e-10 or s2D < 0.5 - 2e-10:
            spectral_violations += 1

        Pdiag = proj_diag_abs_ge(D, CUT)
        k = int(np.argmax(Pdiag))
        if Pdiag[k] > 1.0/72.0:
            row = np.linalg.norm(np.delete(D[k, :], k))
            hub_margin = max(abs(D[k,k]), row) - HUB
            min_hub_margin = min(min_hub_margin, hub_margin)
            if hub_margin <= -2e-10:
                hub_violations += 1

print(f"seed={SEED}")
print(f"trials={trials}")
print(f"spectral_violations={spectral_violations}")
print(f"hub_violations={hub_violations}")
print(f"max_star_norm_over_(rho/2)={max_star_norm_over_half:.15f}")
print(f"min_weyl_margin={min_weyl_margin:.15e}")
print(f"min_high_leverage_hub_margin={min_hub_margin:.15e}")
print(f"tau={TAU:.15f}")
print(f"leaf_scale=0.5")
print(f"leaf_hub_threshold={HUB:.15f}")
