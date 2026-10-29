# Audit of agent B's RR next-order term with momentum (T354, push 12aff637): an independent check of H.
# agent A, 20 Oct 2026. At x = 0 and beta2 = 1 the quadratic term is E[m (sum_j Z_(k-j))^2] with m = (1-b1) sum_i b1^i b_(k-i),
# the sum over all past lags. Brute force: every permutation of the current epoch AND every permutation of one full earlier epoch
# (independent), n = 6, random b with mean 0, momentum truncated at the two epochs (the weight beyond is b1^(p+1+n), kept exactly
# by restricting the formula to the same truncation). Claim: E = T H with H = (1/n) sum_p (1 - b1^(p+1)) h(p), and the earlier epoch
# contributes nothing.
import itertools, numpy as np
rng = np.random.default_rng(12); n = 6
b = rng.standard_normal(n); b -= b.mean(); B2 = (b ** 2).mean(); Z = b ** 2 - B2; T = (b * Z * Z).mean()
P = np.array(list(itertools.permutations(range(n))))          # 720 x 6
for b1 in [0.0, 0.5, 0.7, 0.9]:
    tot_cur = 0.0; tot_two = 0.0
    for p in range(n):
        lag_cur = np.arange(p + 1)                             # lags 0..p: slots p, p-1, ..., 0 of the current epoch
        w_cur = (1 - b1) * b1 ** lag_cur
        mc = (b[P[:, p - lag_cur]] * w_cur).sum(1)             # momentum from the current epoch, per permutation
        zc = Z[P[:, :p + 1]].sum(1)                            # sum of Z over the current epoch's past slots
        tot_cur += np.mean(mc * zc * zc)
        lag_prev = p + 1 + np.arange(n)                        # previous epoch slots n-1 .. 0
        w_prev = (1 - b1) * b1 ** lag_prev
        mp = (b[P[:, n - 1 - np.arange(n)]] * w_prev).sum(1)   # momentum from the previous epoch
        zp = Z[P].sum(1)                                       # its Z sum (identically 0)
        M = mc[:, None] + mp[None, :]; S = zc[:, None] + zp[None, :]
        tot_two += np.mean(M * S * S)
    h = lambda p: 1 - 3 * p / (n - 1) + 2 * p * (p - 1) / ((n - 1) * (n - 2))
    H = np.mean([(1 - b1 ** (p + 1)) * h(p) for p in range(n)])
    print(f"n {n} b1 {b1}: current epoch only E/T {tot_cur / n / T:.12f} | with a full earlier epoch {tot_two / n / T:.12f} | H {H:.12f}")
# the peer's limit coefficients on the test model (b = (9, -1 x 9), n = 10): K0 - (3/4) T H/(K0 B2 B3)
n = 10; B2, B3, T = 9.0, 72.0, 4608.0
h = lambda p: 1 - 3 * p / (n - 1) + 2 * p * (p - 1) / ((n - 1) * (n - 2))
for b1 in [0.0, 0.3, 0.5, 0.9]:
    H = np.mean([(1 - b1 ** (p + 1)) * h(p) for p in range(n)]); K0 = np.mean([(1 - b1 ** (p + 1)) * (1 - p / (n - 1)) for p in range(n)])
    print(f"test model b1 {b1}: H {H:.6f} K0 {K0:.6f} limit coefficient {K0 - 0.75 * T * H / (K0 * B2 * B3):.6f}")
