"""Audit of the closed-form K_rr in agent_B/NOTE.md ("Every n", push 17c04a29), two independent ways (agent C).

1. Lag sum from first principles: E[g_{k-i} Z_{k-j}] = C if i = j, -C/(n-1) if i != j and both steps fall in one epoch, else 0.
   With the step's epoch position uniform, two lags i < j = i + delta (delta < n) share an epoch for exactly n - delta of the
   n positions, whatever i is. So
       K = (1-b1) [ sum_i (b1 b2)^i - (1/(n-1)) sum_{i != j, |i-j| < n} b1^i b2^j (n - |i-j|)/n ].
2. Monte Carlo at x = 0: reshuffled epochs of b = 9 (n/10 of them) / -1, m_k = (1-b1) sum b1^i b_{k-i},
   eta_k = (1-b2) sum b2^j Z_{k-j} / V, K_mc = E[m eta] / ((1-b2) C / V), C = E b^3.
usage: python kcheck_indep.py
"""
import numpy as np


def K_closed(n, b1, b2):
    g = b1 * b2
    G = lambda z: z * (1 - z ** n) / (1 - z)
    d = 1 - b2
    return (n / (n - 1) * (1 - b1) / (1 - g)
            - (n - G(b1) - G(b2) + G(g) + g * (1 - b1 ** n) * (1 - b2 ** n) / (1 - g)) / (n * (n - 1) * d))


def K_lag(n, b1, b2, L=None):
    d = 1 - b2
    L = L or int(60 / min(d, 1 - b1 if b1 > 0 else 1)) + 2 * n
    i = np.arange(L)
    diag = np.sum((b1 * b2) ** i)
    off = 0.0
    for delta in range(1, n):
        w = (n - delta) / n
        # pairs (i, i+delta) and (i+delta, i)
        off += w * np.sum(b1 ** i[:L - delta] * b2 ** (i[:L - delta] + delta))
        off += w * np.sum(b1 ** (i[:L - delta] + delta) * b2 ** i[:L - delta])
    return (1 - b1) * (diag - off / (n - 1))


def K_mc(n, b1, b2, epochs, seed):
    rng = np.random.default_rng(seed)
    m = n // 10
    base = np.array([9.0] * m + [-1.0] * (n - m))
    b = np.concatenate([rng.permutation(base) for _ in range(epochs)])
    B2, B3 = np.mean(base ** 2), np.mean(base ** 3)
    Z = b ** 2 - B2
    from scipy.signal import lfilter
    mom = lfilter([1 - b1], [1, -b1], b)
    eta = lfilter([1 - b2], [1, -b2], Z) / B2
    burn = int(50 / (1 - b2)) + n
    prod = mom[burn:] * eta[burn:]
    est = prod.mean() / ((1 - b2) * B3 / B2)
    # batch-means standard error over 50 blocks
    blocks = np.array_split(prod, 50)
    se = np.std([bl.mean() for bl in blocks], ddof=1) / np.sqrt(50) / ((1 - b2) * B3 / B2)
    return est, se


if __name__ == "__main__":
    worst = 0.0
    for n in (2, 3, 10, 37, 100, 400):
        for b1 in (0.0, 0.5, 0.9):
            for b2 in (0.9, 0.99, 0.999):
                kc, kl = K_closed(n, b1, b2), K_lag(n, b1, b2)
                worst = max(worst, abs(kc - kl))
    print("closed form vs first-principles lag sum, n 2..400, b1 0/.5/.9, b2 .9/.99/.999: max |diff| %.2e" % worst)
    for (n, b1, b2) in ((50, 0.0, 0.99), (500, 0.0, 0.99), (50, 0.9, 0.99), (200, 0.5, 0.995)):
        est, se = K_mc(n, b1, b2, epochs=200000 // n * 20, seed=n)
        print("MC n %d b1 %g b2 %g: K_mc %.4f +- %.4f   closed %.4f   iid %.4f"
              % (n, b1, b2, est, se, K_closed(n, b1, b2), (1 - b1) / (1 - b1 * b2)))
