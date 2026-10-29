"""Checks of the momentum and eps>0 RR enclosure algebra (agent C, 20 Oct 2026, T354).
(1) Momentum pairing: over ALL pairs of permutations (current + one earlier epoch, n = 4), E[g_{k-i}(sum_j c_j Z_{k-j})^2] equals the
    exact in-epoch moment formula for lag i's epoch plus f' * E[(other epoch part)^2]; cross-epoch terms vanish.
(2) eps>0: psi = (s+eps)/(s sqrt y + eps); psi'(1), psi''(1) and the closed |psi'''| against finite differences, and |psi'''|
    decreasing in y on [0.2, 1.8] (so the sup on [1-e, 1+e] sits at 1-e)."""
import itertools, numpy as np
rng = np.random.default_rng(3)
n = 4; g = rng.normal(size=n) + 0.4
V = np.mean(g * g); Z = g * g - V; fp = g.mean()
M00 = np.mean(g * Z * Z)
M0l = np.mean([g[a] * Z[a] * Z[c] for a, c in itertools.permutations(range(n), 2)])
Mjj = np.mean([g[a] * Z[c] * Z[c] for a, c in itertools.permutations(range(n), 2)])
Mjl = np.mean([g[a] * Z[c] * Z[e] for a, c, e in itertools.permutations(range(n), 3)])
perms = list(itertools.permutations(range(n)))
worst = 0.0
for p in range(n):
    L = p + 1 + n
    lag = np.arange(L); c = 0.7 ** lag + 0.1 * lag     # arbitrary positive weights
    ep = np.where(lag <= p, 0, 1)
    for i in range(L):
        brute = 0.0
        for P0 in perms:
            for P1 in perms:
                idx = [P0[p - j] if j <= p else P1[n - 1 - (j - p - 1)] for j in lag]
                brute += g[idx[i]] * np.dot(c, Z[idx]) ** 2
        brute /= len(perms) ** 2
        same = ep == ep[i]
        ci = c[i]; s1 = c[same].sum(); s2 = (c[same] ** 2).sum()
        inep = ci * ci * M00 + 2 * ci * (s1 - ci) * M0l + (s2 - ci * ci) * Mjj + ((s1 - ci) ** 2 - (s2 - ci * ci)) * Mjl
        other = 0.0                                          # E[(other-epoch part)^2] by brute force
        oth = ~same
        for P0 in perms:
            for P1 in perms:
                idx = [P0[p - j] if j <= p else P1[n - 1 - (j - p - 1)] for j in lag]
                other += np.dot(c[oth], Z[idx][oth]) ** 2
        other /= len(perms) ** 2
        worst = max(worst, abs(brute - inep - fp * other))
print("(1) momentum pairing, n=4, all p and lags: max |brute - (in-epoch formula + f' E[other^2])| = %.2e" % worst)
for s, eps in [(3.0, 0.0), (3.0, 1.0), (3.0, 10.0), (0.7, 2.0)]:
    psi = lambda y: (s + eps) / (s * np.sqrt(y) + eps)
    def m3(y):
        q = s * np.sqrt(y) + eps; q1, q2, q3 = s / (2 * np.sqrt(y)), s / (4 * y ** 1.5), 3 * s / (8 * y ** 2.5)
        return (s + eps) * (q3 / q ** 2 + 6 * q1 * q2 / q ** 3 + 6 * q1 ** 3 / q ** 4)
    h = 1e-3; r = s / (s + eps)
    d1 = (psi(1 + h) - psi(1 - h)) / (2 * h); d2 = (psi(1 + h) - 2 * psi(1) + psi(1 - h)) / h ** 2
    ys = np.linspace(0.2, 1.8, 41)
    fd3 = [abs((psi(y + 2 * h) - 2 * psi(y + h) + 2 * psi(y - h) - psi(y - 2 * h)) / (2 * h ** 3)) for y in ys]
    rel = max(abs(a - m3(y)) / m3(y) for a, y in zip(fd3, ys))
    mono = all(np.diff([m3(y) for y in ys]) < 0)
    print("(2) s %.1f eps %4.1f: psi'(1) %.6f vs -r/2 %.6f | psi''(1) %.6f vs r/4+r^2/2 %.6f | |psi'''| closed vs FD max rel %.1e | decreasing in y: %s"
          % (s, eps, d1, -r / 2, d2, r / 4 + r * r / 2, rel, mono))
