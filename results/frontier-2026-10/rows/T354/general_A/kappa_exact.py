"""T354 general case (agent A, 21 Oct 2026): audit of Proposition 1's covariance step. Under reshuffling, phase
averaged, Cov(m, v) = C [sum_s a_s w_s - (1/(n - 1)) sum over ordered pairs (s, s'), s != s', in one epoch, of a_s w_s'],
a_s = (1 - b1) b1^s, w_s = (1 - b2) b2^s. kappa = Cov/((1 - b2) C) is computed exactly from the weights and checked
against [K - 1, K], K = (1 - b1)/(1 - b1 b2), and against a direct Monte Carlo of the filters on a reshuffled stream."""
import numpy as np
from scipy.signal import lfilter


def kappa(b1, b2, n, tol=1e-15):
    L = 1
    while (1 - b1) * b1 ** L > tol or (1 - b2) * b2 ** L > tol:
        L += 1
    s = np.arange(L + n)
    a = (1 - b1) * b1 ** s
    w = (1 - b2) * b2 ** s
    diag = (a * w).sum()
    cross = 0.0
    for p in range(n):                      # the current slot sits at position p of its epoch
        # epoch blocks going back: [0, p], [p + 1, p + n], [p + n + 1, p + 2n], ...
        lo = 0; hi = p
        while lo < L:
            sa = a[lo:hi + 1].sum(); sw = w[lo:hi + 1].sum(); same = (a[lo:hi + 1] * w[lo:hi + 1]).sum()
            cross += sa * sw - same
            lo, hi = hi + 1, hi + n
    cross /= n
    cov = diag - cross / (n - 1)
    return cov / (1 - b2), (1 - b1) / (1 - b1 * b2)


def kappa_mc(b1, b2, n, T, seed):
    r = np.random.default_rng(seed)
    x = r.exponential(1.0, n); x -= x.mean()             # skewed values, so C != 0
    C = (x * (x * x - (x * x).mean())).mean()
    g = x[np.concatenate([r.permutation(n) for _ in range(T // n + 1)])[:T]]
    burn = int(30 / (1 - b2))
    m = lfilter([1 - b1], [1, -b1], g)[burn:]
    v = lfilter([1 - b2], [1, -b2], g * g)[burn:]
    return ((m - m.mean()) * (v - v.mean())).mean() / ((1 - b2) * C)


if __name__ == "__main__":
    print(__doc__)
    for b1, b2, n in [(0, .99, 16), (0, .99, 2000), (.9, .99, 16), (.9, .999, 16), (.9, .99, 200), (.5, .5, 4), (.99, .999, 50)]:
        k, K = kappa(b1, b2, n)
        mc = kappa_mc(b1, b2, n, 4_000_000, 7)
        print(f"b1 {b1} b2 {b2} n {n}: kappa exact {k:.5f}  Monte Carlo {mc:.5f}  K {K:.5f}  "
              f"in [K-1, K]: {K - 1 - 1e-12 <= k <= K + 1e-12}  |kappa| <= 1: {abs(k) <= 1 + 1e-12}", flush=True)
