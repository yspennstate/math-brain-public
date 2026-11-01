"""Audit of NOTE 'The remainder, uniform in n' (agent A, 20 Oct 2026). Brute force over all permutations at small n.
(1) E S^4 formula of item 3 against enumeration, and the constant 14 in E S^4 <= 14 (s2^2 A2^2 + m4 A4) over n >= 4.
(2) E[b_k (Z_k + W)^2] split into its three pieces (lag 0, cross, W^2) against the closed forms -E[bZ^2]/(n-1) etc.,
    and the total against 8 |E b Z^2| (the NOTE) and 6 |E b Z^2| (this audit's count: 1 + 2 + 3).
(3) E[b_k (Z_k + W)^3] against C/d: printed as d * |E| for several beta2 at fixed n."""
import itertools, math
import numpy as np
rng = np.random.default_rng(3)

def es4_formula(a, z):
    n = len(a); A2, A4 = np.sum(a**2), np.sum(a**4); P2, P4 = np.sum(z**2), np.sum(z**4)
    return (A2**2*(3*P2**2*(n*n-3*n+3) - 3*P4*n*(n-1)) + A4*(P4*n*n*(n+1) - 3*P2**2*n*(n-1))) / (n*(n-1)*(n-2)*(n-3))

worst = 0.0
for n in (4, 5, 6, 7):
    perms = np.array(list(itertools.permutations(range(n))))
    for t in range(40):
        a = rng.standard_normal(n); a -= a.mean(); z = rng.standard_normal(n)**3; z -= z.mean()
        if t % 3 == 0: z = np.zeros(n); z[0] = n - 1; z[1:] = -1.0   # spiky values
        S = (a[None, :] * z[perms]).sum(1)
        bf, fo = np.mean(S**4), es4_formula(a, z)
        assert abs(bf - fo) <= 1e-9 * max(1, abs(bf)), (n, bf, fo)
        s2, m4 = np.mean(z**2), np.mean(z**4)
        worst = max(worst, bf / (s2**2*np.sum(a**2)**2 + m4*np.sum(a**4)))
    print("E S^4: n %d formula matches enumeration (40 draws)" % n)
print("max E S^4 / (s2^2 A2^2 + m4 A4) over the draws: %.3f (NOTE's constant 14)" % worst)

for n in (5, 6, 7):
    perms = np.array(list(itertools.permutations(range(n))))
    for beta2 in (0.3, 0.7, 0.95):
        for t in range(5):
            b = rng.standard_normal(n); b -= b.mean(); x = 0.1 * rng.standard_normal()
            g2 = (x + b)**2; Z = g2 - g2.mean(); EbZ2 = np.mean(b * Z**2)
            pieces = np.zeros(3); tot3 = 0.0
            for p in range(n):
                k = perms[:, p]; w = beta2 ** np.arange(1, p + 1)          # lags 1..p
                W = sum(w[j-1] * Z[perms[:, p - j]] for j in range(1, p + 1)) if p else 0 * Z[k]
                pieces += [np.mean(b[k] * Z[k]**2), np.mean(2*b[k]*Z[k]*W), np.mean(b[k]*W**2)]
                tot3 += np.mean(b[k] * (Z[k] + W)**3)
            pieces /= n; tot3 /= n
            r = np.abs(pieces) / abs(EbZ2)
            assert r[0] <= 1 + 1e-12 and r[1] <= 2 + 1e-12 and r[2] <= 3 + 1e-12, (n, beta2, r)
            assert abs(pieces.sum()) <= 6 * abs(EbZ2) + 1e-12
        print("E[b eta_c^2]: n %d beta2 %.2f pieces/|EbZ2| last draw %s, all draws <= (1, 2, 3)" % (n, beta2, np.array2string(r, precision=3)))
