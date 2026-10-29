"""Second, independent check of the x d term in E2 (agent C, 20 Oct 2026); see uniform_check.py.

(a) Fit E2 = a x d + c d^2 to the three exact roots-free drift values of uniform_check.txt part 3 (x = 0.1, n d = 1).
(b) Compute E eta^2 exactly at x = 0.1 from the permutation formula E S^2 = sum (w - mean w)^2 P2/(n-1), epoch by epoch, averaged
    over the position p, and compare a with (3/8) E eta^2 / d, the size the expansion predicts for the x E eta^2 term.
(c) The exact coefficient in E[b (Z_k + W)^2] = c_n(beta2) E[b Z^2] (all three pieces are multiples of E[b Z^2]):
    c = avg_p [1 - (2 sum_j beta^j + sum_j beta^{2j})/(n-1) + 2 sum_{j != l} beta^{j+l}/((n-1)(n-2))], j, l in 1..p;
    against the brute-force ratios 0.710, 0.429, 0.315, 0.182 of part 2.
"""
import numpy as np

E2 = {0.01: 6.1143e-04, 0.005: 2.4386e-04, 0.0025: 1.0696e-04}
x = 0.1
M = np.array([[x * d, d * d] for d in E2])
a, c = np.linalg.lstsq(M, np.array(list(E2.values())), rcond=None)[0]
print("(a) E2 = %.4f x d + %.3f d^2  (residuals %s)" % (a, c, np.array2string(M @ [a, c] - np.array(list(E2.values())), precision=2)))

def eeta2(n, b2, x):
    m = n // 10
    g2 = np.array([(x + 9) ** 2] * m + [(x - 1) ** 2] * (n - m))
    V = g2.mean(); Z = g2 - V; P2 = np.sum(Z ** 2); d = 1 - b2
    tot = 0.0
    for p in range(n):
        w = b2 ** np.arange(p + 1)                         # current epoch, lags 0..p on p+1 of the n slots
        wc = np.concatenate([w, np.zeros(n - p - 1)])
        tot += np.sum((wc - wc.mean()) ** 2) * P2 / (n - 1)
        L = p + 1                                          # earlier epochs, lags L + e n .. L + e n + n - 1
        e = 0
        while b2 ** (L + e * n) > 1e-12:
            w = b2 ** (L + e * n + np.arange(n))
            tot += np.sum((w - w.mean()) ** 2) * P2 / (n - 1)
            e += 1
    return (d / V) ** 2 * tot / n

for n, b2 in ((100, 0.99), (200, 0.995), (400, 0.9975)):
    d = 1 - b2
    print("(b) n %d d %.4f: E eta^2/d %.4f, (3/8) E eta^2/d %.4f" % (n, d, eeta2(n, b2, x) / d, 0.375 * eeta2(n, b2, x) / d))

for n, b2 in ((6, 0.5), (7, 0.8), (8, 0.9), (8, 0.99)):
    cs = []
    for p in range(n):
        j = np.arange(1, p + 1); w = b2 ** j
        off = np.sum(w) ** 2 - np.sum(w ** 2)
        cs.append(1 - (2 * np.sum(w) + np.sum(w ** 2)) / (n - 1) + 2 * off / ((n - 1) * (n - 2)))
    print("(c) n %d beta2 %.2f: c_n %.3f" % (n, b2, np.mean(cs)))
