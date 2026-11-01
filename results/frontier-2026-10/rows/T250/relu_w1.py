"""T250 (agent A, 18 Oct 2026): an explicit depth-uniform rate for the critical ReLU MLP, one input.
h_1 = W_1 x, h_l = W_l relu(h_(l-1)), W_l iid N(0, 2/n), |x|^2/d = K0 = 1. Given layer l-1, h_l ~ N(0, K_(l-1) I_n) with
K_l = K_(l-1) M_l, M_l = (2/n) chi2_(B_l), B_l ~ Bin(n, 1/2), iid. GP limit: hbar_L ~ N(0, K0 I_n).
BOUND (synchronous coupling h_L = sqrt(K_(L-1)) g, hbar_L = sqrt(K0) g):
  W1(h_L/sqrt n, hbar_L/sqrt n) <= E|sqrt K_(L-1) - 1| E|g|/sqrt n <= sqrt(E(sqrt K_(L-1) - 1)^2) = sqrt(2 (1 - a_n^(L-1))),
  a_n = E sqrt(M) = sum_k Bin(n,1/2)(k) sqrt(2/n) sqrt(2) Gamma((k+1)/2)/Gamma(k/2)  (k = 0 term 0),
  and 1 - a^(L-1) <= (L-1)(1 - a): the rate is sqrt(2 (L-1)(1 - a_n)) ~ sqrt(5 (L-1)/(4 n)), and never above sqrt 2.
EXACT W1: both laws are rotation invariant, so W1 = W1 of the radii (sorting).
usage: python relu_w1.py"""
import numpy as np
from scipy.special import gammaln
from scipy.stats import binom
rng = np.random.default_rng(5); S = 200000
for n in (250, 1000):
    k = np.arange(1, n + 1)
    a = float(np.sum(binom.pmf(k, n, 0.5) * np.sqrt(2 / n) * np.sqrt(2) * np.exp(gammaln((k + 1) / 2) - gammaln(k / 2))))
    print(f"n {n}: a_n = {a:.8f}, n (1 - a_n) = {n * (1 - a):.4f} (5/8 = 0.625)", flush=True)
    for L in (2, 4, 8, 16, 32, 64, 128, 256):
        lg = np.zeros(S)
        for _ in range(L - 1):
            B = rng.binomial(n, 0.5, S); lg += np.log(np.maximum(2 / n * rng.chisquare(np.maximum(B, 1), S), 1e-300))
        r = np.exp(0.5 * lg) * np.sqrt(rng.chisquare(n, S) / n); rb = np.sqrt(rng.chisquare(n, S) / n)
        w1 = np.mean(np.abs(np.sort(r) - np.sort(rb)))
        bound = np.sqrt(2 * (1 - a ** (L - 1)))
        print(f"  L {L:4d} (L/n {L / n:6.3f}): exact W1 {w1:.5f}   bound {bound:.5f}   ratio {w1 / bound:.3f}   "
              f"W1 sqrt(n/(L-1)) {w1 * np.sqrt(n / (L - 1)):.4f}", flush=True)
