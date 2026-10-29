"""Momentum audit, earlier-epoch lag (agent A, 20 Oct 2026): b at slot q of an epoch whose eta_e weights are arbitrary w in [0,1].
E[b_pi(q) (sum_r w_r Z_pi(r))^2] by enumeration, against the piece count bound (w_q^2 + 2 w_q + 3) |E b Z^2| <= 6 |E b Z^2| that the
beta1 = 0 count gives (weights <= 1, at most n - 1 other slots). The 1/d weight-sum bound alone would only give O(sum w^2) = O(1/d)."""
import itertools, numpy as np
rng = np.random.default_rng(5); worst = 0.0
for n in (5, 6, 7):
    P = np.array(list(itertools.permutations(range(n))))
    for t in range(60):
        b = rng.standard_normal(n); b -= b.mean(); x = 0.1 * rng.standard_normal()
        Z = (x + b) ** 2; Z -= Z.mean(); EbZ2 = np.mean(b * Z ** 2)
        w = rng.random(n) if t % 2 else np.ones(n)       # all-ones weights: the worst case for the count
        q = rng.integers(n)
        S = (w[None, :] * Z[P]).sum(1)
        val = np.mean(b[P[:, q]] * S ** 2)
        worst = max(worst, abs(val) / abs(EbZ2))
    print("n %d: 60 draws, max |E[b_sigma eta_e^2]| / |E b Z^2| so far %.3f (bound 6)" % (n, worst))
