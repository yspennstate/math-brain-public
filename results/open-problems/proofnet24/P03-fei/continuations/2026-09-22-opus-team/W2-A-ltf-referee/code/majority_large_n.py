"""Lemma 3 and Lemma 4 ratios for Maj_n at large odd n, from the closed form
fhat(S) = (-1)^{(k-1)/2} C((n-1)/2,(k-1)/2)/C(n-1,k-1) * C(n-1,(n-1)/2) / 2^{n-1},  |S| = k odd,
checked against the Walsh transform at small n. Predicted limits: Lemma 3 -> 2 ln 2 / L1 = 0.3340,
Lemma 4 -> (2 ln 2 - 1/2) / L1 = 0.2135 (arcsine law of |S|/n under the size-biased spectral sample)."""
import math
import numpy as np
import ltf_ref as L

L.be_polite()


def lc(a, b):
    return math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(a - b + 1)


def level_weights_maj(n):
    W = np.zeros(n + 1)
    for k in range(1, n + 1, 2):
        lf = lc((n - 1) // 2, (k - 1) // 2) - lc(n - 1, k - 1) + lc(n - 1, (n - 1) // 2) - (n - 1) * math.log(2)
        W[k] = math.exp(lc(n, k) + 2 * lf)
    return W


for n in [5, 9, 13]:
    sp = L.Spec(L.ltf_table([1] * n, 0))
    W = sp.level_weights()
    assert np.max(np.abs(W - level_weights_maj(n))) < 1e-12, n
print("closed form matches the Walsh transform at n = 5, 9, 13")
print("predicted limits: L3 ->", 2 * math.log(2) / L.L1_CONST, " L4 ->", (2 * math.log(2) - 0.5) / L.L1_CONST)
for n in [21, 101, 1001, 4001, 20001]:
    W = level_weights_maj(n)
    ks = np.arange(n + 1)
    I = float((ks * W).sum())
    sb = ks * W / I                                   # size-biased law of |S| given i in S
    A = float((sb[1:] * np.log(n / ks[1:])).sum())    # E ln(N/(|T|+1)), N = n, |T|+1 = |S|
    # Sigma = sum_k W_k (k/n) sum_{s=1}^n ln+(s/k)
    s = np.arange(1, n + 1)
    cum = np.concatenate([[0.0], np.cumsum(np.log(s))])   # cum[m] = ln m!
    Sig = 0.0
    for k in range(1, n + 1, 2):
        if W[k] == 0:
            continue
        # sum_{s=k}^{n} ln(s/k) = ln(n!) - ln((k-1)!) - (n-k+1) ln k
        tot = cum[n] - cum[k - 1] - (n - k + 1) * math.log(k)
        Sig += W[k] * (k / n) * tot
    print(f"n={n:6d}  I={I:.4f}  Lemma3 ratio={A / L.L1_CONST:.5f}  Lemma4 ratio={Sig / (L.L1_CONST * I):.5f}  sum W={W.sum():.12f}")
