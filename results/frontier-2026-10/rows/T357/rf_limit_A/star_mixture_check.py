"""T357 sign lemma, the scale-mixture proof of the star condition: checks its two inputs.
(1) The logistic is a normal scale mixture, L = 2K Z with K Kolmogorov (Stefanski 1991): compare E Phi(x/(2K)) with sigma(x).
(2) The conclusion: for c in (0, 1.2), F_W(x) - F_L(c x) on x in (0, 40] has at most one sign change, from - to +, where
W = L + tau Z = sqrt(4K^2 + tau^2) Z. F_W by the mixture and, independently, by quadrature of sigma(x - tau z) against phi."""
import numpy as np
from scipy.special import ndtr
k = np.linspace(1e-4, 4, 40001)
j = np.arange(1, 200)[:, None]
cdf = 1 - 2 * ((-1.0) ** (j - 1) * np.exp(-2 * j ** 2 * k[None, :] ** 2)).sum(0)
cdf[k < 0.2] = 0.0                                   # the alternating series is useless near 0, where the cdf is < 1e-25
w = np.diff(cdf, prepend=0.0); w = np.clip(w, 0, None); w /= w.sum(); V = 2 * k
x = np.linspace(-10, 10, 201)
FL_mix = (ndtr(x[:, None] / V[None, :]) * w).sum(1); sig = 1 / (1 + np.exp(-x))
print(f"(1) max |E Phi(x/2K) - sigma(x)| on [-10, 10]: {np.abs(FL_mix - sig).max():.1e}   E (2K)^2 {(w * V ** 2).sum():.5f} (pi^2/3 {np.pi ** 2 / 3:.5f})")
z = np.linspace(-12, 12, 4801); pz = np.exp(-z ** 2 / 2); pz /= pz.sum()
xs = np.linspace(0.01, 40, 2000)
for tau in [0.1, 0.5, 1, 2, 4, 8]:
    U = np.sqrt(V ** 2 + tau ** 2)
    FW_mix = (ndtr(xs[:, None] / U[None, :]) * w).sum(1)
    FW_q = (np.exp(-np.logaddexp(0, -(xs[:, None] - tau * z[None, :]))) * pz).sum(1)
    worst = 0
    for c in np.linspace(0.05, 1.2, 116):
        dlt = FW_q - 1 / (1 + np.exp(-c * xs))
        sgn = np.sign(dlt[np.abs(dlt) > 1e-12]); ch = int((np.diff(sgn) != 0).sum())
        bad = ch > 1 or (ch == 1 and sgn[0] > 0)
        worst = max(worst, ch + 10 * bad)
    print(f"(2) tau {tau:4}: |F_W mix - quad| {np.abs(FW_mix - FW_q).max():.1e}   max sign changes over c {worst} (10+ = wrong order)", flush=True)
