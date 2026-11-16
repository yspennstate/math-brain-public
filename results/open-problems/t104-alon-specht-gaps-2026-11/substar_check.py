"""Psi of GAP_STATE_FORM.md at the vector of K_{1,k} padded with zeros, against the closed form in u = k/(k+1)."""
import numpy as np
from two_eig_family import psi

worst, low = 0.0, (9e9, None)
for n in range(5, 31):
    for k in range(2, n):
        x = np.zeros(n); x[0] = k; x[1:k + 1] = -1; x /= np.linalg.norm(x)
        ps, q, p3, m = psi(x)
        u = k / (k + 1.0)
        cf = (n - 4) * (2 * u - 1) * (3 * u - 2) / u - 2 * (n - 3) * (2 * u - 1) ** 2 / u \
            + (n - 1) * (n * n - 6 * n + 6 + 2 * n * q) * (1 - u) ** 2 / u
        worst = max(worst, abs(cf - ps))
        if k < n - 1 and ps < low[0]:
            low = (ps, (n, k))
        if k == n - 1 and abs(ps) > 1e-9:
            print("star not zero", n, ps)
print("closed form against Psi: largest deviation %.1e; smallest Psi over k < n-1, n = 5..30: %.4f at (n, k) = %s" % (worst, low[0], low[1]))
