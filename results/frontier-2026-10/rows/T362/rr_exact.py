"""T362 Target 1 (agent A, 18 Oct 2026): exact last-iterate error of random reshuffling (fresh permutation each epoch,
constant step g) on two decoupled quadratic coordinates, F(x) = (mu/2) x1^2 + (L/2) x2^2, components f_i = F + b_i . x with
sum_i b_i = 0, noise sigma_1^2 = mean b_i1^2 on the flat coordinate and sigma_2^2 on the stiff one.
Per coordinate (curvature h, a = 1 - g h): one epoch maps X -> a^n X - g Z, Z = sum_k a^(n-1-k) b_pi(k), and sampling without
replacement gives Var Z = sigma^2 n/(n-1) sum_k (c_k - cbar)^2, c_k = a^(n-1-k). Epochs are independent, so
    E (h/2) X_K^2 = (h/2) [ a^(2nK) X0^2 + g^2 Var Z (1 - a^(2nK)) / (1 - a^(2n)) ].
Part 1 checks this against a Monte Carlo of actual RR. Part 2 minimises over g in (0, 2/L) and prints the optimal error and step
against K, n, kappa = L/mu. argv: mode (mc|sweep)"""
import sys, numpy as np
def err(g, h, n, K, sig2, X0):
    a = 1 - g * h; c = a ** np.arange(n - 1, -1, -1.0); vz = sig2 * n / (n - 1) * np.sum((c - c.mean()) ** 2)
    a2n = a ** (2 * n); geo = K if abs(1 - a2n) < 1e-15 else (1 - a2n ** K) / (1 - a2n)
    return 0.5 * h * (a2n ** K * X0 ** 2 + g * g * vz * geo)
def total(g, mu, L, n, K, s1, s2): return err(g, mu, n, K, s1, 1.0) + err(g, L, n, K, s2, 1.0)
def best(mu, L, n, K, s1, s2):
    gs = np.exp(np.linspace(np.log(1e-9), np.log(1.999 / L), 4000)); e = np.array([total(g, mu, L, n, K, s1, s2) for g in gs])
    i = int(np.argmin(e)); lo, hi = gs[max(i - 1, 0)], gs[min(i + 1, len(gs) - 1)]
    for _ in range(80):
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if total(m1, mu, L, n, K, s1, s2) < total(m2, mu, L, n, K, s1, s2): hi = m2
        else: lo = m1
    g = (lo + hi) / 2; return g, total(g, mu, L, n, K, s1, s2)
if sys.argv[1] == 'mc':
    rng = np.random.default_rng(362)
    for (mu, L, n, K, g) in ((1.0, 10.0, 8, 5, 0.02), (1.0, 10.0, 8, 20, 0.15), (0.5, 50.0, 16, 10, 0.01)):
        b = rng.standard_normal((n, 2)); b -= b.mean(0); s = (b ** 2).mean(0); h = np.array([mu, L]); R = 200000
        X = np.ones((R, 2))
        for k in range(K):
            P = np.argsort(rng.random((R, n)), axis=1)
            for j in range(n): X = X - g * (h * X + b[P[:, j]])
        mc = (0.5 * h * X ** 2).sum(1); ex = total(g, mu, L, n, K, s[0], s[1])
        print(f'mu {mu} L {L} n {n} K {K} g {g}: exact {ex:.6e}  MC {mc.mean():.6e} +- {mc.std() / np.sqrt(R):.1e}', flush=True)
else:
    mu = 1.0
    for s1, s2, lab in ((0.0, 1.0, 'noise on the STIFF coordinate'), (1.0, 0.0, 'noise on the FLAT coordinate')):
        print('==', lab)
        for n in (10, 100):
            for kap in (10, 100, 1000):
                row = []
                for K in (1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000):
                    g, e = best(mu, kap * mu, n, K, s1, s2); row.append((K, e, g))
                sl = [np.log(row[i + 1][1] / row[i][1]) / np.log(row[i + 1][0] / row[i][0]) for i in range(len(row) - 1)]
                print(f'n {n:4d} kappa {kap:5d}: ' + ' '.join(f'K{K}:{e:.2e}(g*L {g * kap:.2g})' for K, e, g in row), flush=True)
                print(f'      local slopes d log err / d log K: ' + ' '.join(f'{s:+.2f}' for s in sl), flush=True)
