"""T348 Target 1 check, spherical ensemble (Lucibello-Mezard arXiv:2304.14964, energy eq. 1 with lambda).
phi_{alpha,1}(lambda) (uncondensed branch, re-derived 19 Oct: sup_t [lambda t + (1/2) log(1 - t^2)] / lambda + alpha / lambda),
alpha_1(lambda) = lambda - (1/2)(s - 1 - log((1 + s)/2)), s = sqrt(1 + 4 lambda^2).
Monte Carlo at finite N: M = round(e^{alpha N}) patterns uniform on the sphere of radius sqrt N; for every pattern nu the
quantity phi_hat_nu = log(sum_{mu != nu} e^{lambda xi_nu . xi_mu}) / (lambda N) (retrieval at x = xi_nu iff < 1); reports the median
and the max over nu (the all-pattern quantity), the max pairwise overlap against sqrt(1 - e^{-4 alpha}), and the count of failing
patterns. argv: lambda alpha N-list seed
"""
import sys, math
import numpy as np
from scipy.special import logsumexp
lam = float(sys.argv[1]); alpha = float(sys.argv[2]); Ns = [int(v) for v in sys.argv[3].split(",")]; seed = int(sys.argv[4])
s = math.sqrt(1 + 4 * lam ** 2)
a1 = lam - 0.5 * (s - 1 - math.log((1 + s) / 2))
lstar = math.exp(2 * alpha) * math.sqrt(1 - math.exp(-2 * alpha))
phi = alpha / lam + (s - 1 - math.log((1 + s) / 2)) / (2 * lam) if lam < lstar else math.sqrt(1 - math.exp(-2 * alpha))
print(f"lambda={lam} alpha={alpha}: alpha_1={a1:.4f} lambda_*={lstar:.3f} phi_(alpha,1)={phi:.4f} max-overlap bound sqrt(1-e^-4a)={math.sqrt(1-math.exp(-4*alpha)):.4f}")
rng = np.random.default_rng(seed)
for N in Ns:
    M = int(round(math.exp(alpha * N)))
    if M * N * 8 > 2.5e8:                      # memory cap, sized before allocating: patterns <= 250 MB
        print(f"  N={N} M={M}: refused, patterns would take {M*N*8/1e9:.1f} GB"); continue
    X = rng.standard_normal((M, N)); X *= math.sqrt(N) / np.linalg.norm(X, axis=1, keepdims=True)
    allp = M <= 30000                          # all-pattern max only when M^2 N is affordable
    rows = np.arange(M) if allp else np.sort(rng.choice(M, 2000, replace=False))
    B = max(1, int(1.5e7 // M))                # block of B x M overlaps <= 120 MB
    ph = np.empty(len(rows)); mo = 0.0
    for i0 in range(0, len(rows), B):
        idx = rows[i0:i0 + B]
        G = X[idx] @ X.T / N
        G[np.arange(len(idx)), idx] = -np.inf
        mo = max(mo, G.max())
        ph[i0:i0 + B] = logsumexp(lam * N * G, axis=1) / (lam * N)
    tag = "all patterns" if allp else "2000 sampled patterns"
    print(f"  N={N:4d} M={M:7d} ({tag}): phi_hat median {np.median(ph):.4f}  max {ph.max():.4f}  failing (phi_hat>=1) {int((ph >= 1).sum())}  max overlap {mo:.4f}", flush=True)
