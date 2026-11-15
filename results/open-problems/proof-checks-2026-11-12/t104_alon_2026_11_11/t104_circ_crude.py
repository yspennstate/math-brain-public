"""Crude bound for odd circulants: sum g Q <= 8 lam (lam - 2/n) and
sum g P >= (m lam - 1) K(lam), K = 8 lam/(n-2) - 32/(n(n-2)) + 4 (1 - lam)(n-4)/(n-2)^2,
using sum_{j != k} theta_j = 1 - lam, sum g theta >= 0, 1 - sum a C_k C_j <= 2, lam in [2/(n-1), 4/n].
Prints the smallest margin (m lam - 1) K - 8 lam (lam - 2/n) over the lam range, for each odd n."""
import numpy as np
for n in range(5, 61, 2):
    m = (n - 1) // 2
    lam = np.linspace(2.0 / (n - 1), 4.0 / n, 20001)
    K = 8 * lam / (n - 2) - 32 / (n * (n - 2)) + 4 * (1 - lam) * (n - 4) / (n - 2) ** 2
    marg = (m * lam - 1) * K - 8 * lam * (lam - 2.0 / n)
    print("n %2d  min margin %+.3e at lam %.4f" % (n, marg.min(), lam[marg.argmin()]))
