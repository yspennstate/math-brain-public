"""Brute-force check of the erasure composition law for BIASED inner functions.

f = G(g_1..g_k), g_j on disjoint blocks with means mu_j (+-1 convention), V_j = 1-mu_j^2, Ghat_mu the
coefficients of G in the orthonormal basis of the product measure with means mu (fresh inputs: mu=0).
Claim, for w in block j, c_w = ghat_j({w}), It_j = sum_{U ni j} Ghat_mu(U)^2:
  B_w(f)   = (It_j/V_j) [ B_w(g_j) - E(mu_j^2, c_w^2) ] + sum_{U not ni j} E( Ghat_mu(U)^2, (c_w^2/V_j) Ghat_mu(U+j)^2 )
  Inf_w(f) = (It_j/V_j) Inf_w(g_j)."""
import sys, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *
from check_composition import compose, E  # reuses the composer (runs its own balanced check once)

def biased_coeffs(Gtt, k, mu):
    """Ghat_mu(U) = E_{y~mu}[G(y) prod_{j in U} (y_j - mu_j)/sqrt(V_j)], y_j in {+1,-1} with E y_j = mu_j."""
    out = np.zeros(1 << k)
    for yidx in range(1 << k):
        y = np.array([1 - 2 * ((yidx >> j) & 1) for j in range(k)], dtype=float)  # bit 1 -> -1
        w = np.prod([(1 + y[j] * mu[j]) / 2 for j in range(k)])
        for U in range(1 << k):
            prod = 1.0
            for j in range(k):
                if (U >> j) & 1:
                    prod *= (y[j] - mu[j]) / np.sqrt(1 - mu[j] ** 2)
            out[U] += w * Gtt[yidx] * prod
    return out

rng = np.random.default_rng(7)
maxerr = 0.0; cases = 0
for trial in range(60):
    k = int(rng.integers(2, 4))
    Gtt = (1 - 2 * rng.integers(0, 2, 1 << k)).astype(np.int8)
    blocks = []
    for j in range(k):
        if rng.random() < 0.25:
            blocks.append(None); continue
        nj = int(rng.integers(2, 4))
        gt = (1 - 2 * rng.integers(0, 2, 1 << nj)).astype(np.int8)
        if abs(gt.mean()) > 0.99:  # avoid constants
            gt[0] = -gt[0]
        blocks.append((gt, nj))
    tt, n, offs, sizes = compose(Gtt, k, blocks)
    if n > 13: continue
    fh = wht(tt[None, :].astype(float)); cq = coord_quantities(fh, n)
    mu = np.array([0.0 if b is None else float(b[0].mean()) for b in blocks])
    Gmu = biased_coeffs(Gtt, k, mu)
    for j, b in enumerate(blocks):
        if b is None: continue
        gt, nj = b
        gh = wht(gt[None, :].astype(float))[0]; cg = coord_quantities(gh[None, :], nj)
        V = 1 - mu[j] ** 2
        U = np.arange(1 << k); lowU = U[((U >> j) & 1) == 0]
        It = (Gmu[U[((U >> j) & 1) == 1]] ** 2).sum()
        for wl in range(nj):
            w = offs[j] + wl
            c2 = gh[1 << wl] ** 2
            pred_B = (It / V) * (cg["B"][0, wl] - E(mu[j] ** 2, c2)) + E(Gmu[lowU] ** 2, (c2 / V) * Gmu[lowU | (1 << j)] ** 2).sum()
            pred_I = (It / V) * cg["Inf"][0, wl]
            maxerr = max(maxerr, abs(cq["B"][0, w] - pred_B), abs(cq["Inf"][0, w] - pred_I))
            cases += 1
print("biased composition law: cases", cases, "max abs error", maxerr)
