"""T250: the constant in a quantitative Netsor CLT cannot be polynomial in depth without a stability normalization.
Deep linear program h1 = W1 x, h_l = W_l h_{l-1} (W_l iid N(0, sigma^2/n)), one input with |x|^2/d = 1. Given h_{l-1},
h_l ~ N(0, sigma^2 |h_{l-1}|^2/n I), so |h_L|^2/n = K_L prod_{l=1..L} chi2_n/n and the GP limit has |hbar_L|^2/n = K_L chi2_n/n,
K_L = sigma^(2L). Both laws are rotation invariant, so W1(h_L/sqrt n, hbar_L/sqrt n) = W1 of the radii (same-direction
coupling is optimal: |r u - s v| >= |r - s|). Computed by sorting samples; prediction for n >> L:
sqrt(K_L) (sqrt L - 1) / sqrt(pi n).
usage: python -X utf8 deeplin_w1.py"""
import numpy as np

rng = np.random.default_rng(3)
S = 400000
n = 1000
print("n %d, %d samples per law" % (n, S))
for sigma in (1.0, 1.2):
    for L in (1, 2, 4, 8, 16, 32):
        lg = np.zeros(S)
        for _ in range(L):
            lg += np.log(rng.chisquare(n, S) / n)
        r = sigma ** L * np.exp(0.5 * lg)
        rb = sigma ** L * np.sqrt(rng.chisquare(n, S) / n)
        w1 = np.mean(np.abs(np.sort(r) - np.sort(rb)))
        pred = sigma ** L * (np.sqrt(L) - 1) / np.sqrt(np.pi * n)
        print("sigma %.1f L %2d: W1 %.5f  prediction %.5f  W1 * sqrt(n) / sigma^L %.4f" % (sigma, L, w1, pred, w1 * np.sqrt(n) / sigma ** L), flush=True)
