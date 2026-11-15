"""FLOW 12(hh) item 2: biased composition identity for h = F(psi(x^1), ..., psi(x^m)), psi with mean mu.
Inf_(j,i)(h) = Inf^mu_j(F) Inf_i(psi) / s2;  E_(j,i)(h) = Inf^mu_j(F) E'_i(psi) / s2 + sum_{T not j} Phi(F^mu(T)^2, F^mu(T+j)^2 psihat(i)^2 / s2)
with s2 = 1 - mu^2, E'_i = E_i - Phi(mu^2, psihat(i)^2), F^mu the mu-biased Fourier coefficients."""
import itertools
import numpy as np
from balance_mux_check import wht, EI, from_hex


def Phi(a, c):
    s = a + c
    if s <= 0 or a <= 0 or c <= 0:
        return 0.0
    t = c / s
    return s * -(t * np.log2(t) + (1 - t) * np.log2(1 - t))


def biased_coeffs(Ftab, m, mu):
    s = np.sqrt(1 - mu * mu); p1 = (1 + mu) / 2
    co = {}
    for T in range(1 << m):
        tot = 0.0
        for y in range(1 << m):
            ys = [1.0 if (y >> j) & 1 == 0 else -1.0 for j in range(m)]  # bit 0 -> +1
            w = np.prod([p1 if v > 0 else 1 - p1 for v in ys])
            tot += w * Ftab[y] * np.prod([(ys[j] - mu) / s for j in range(m) if (T >> j) & 1])
        co[T] = tot
    return co


n = 6
psi = from_hex("ffffffee", "fefefeee")
mu = psi.mean(); s2 = 1 - mu * mu
ph = wht(psi)
Ep, Ip = EI(psi, n)
Eprime = np.array([Ep[i] - Phi(mu * mu, ph[1 << i] ** 2) for i in range(n)])
for m in (3,):
    Ftab = np.array([-1.0 if bin(y).count("1") > m // 2 else 1.0 for y in range(1 << m)])  # Maj, bit1 = -1
    co = biased_coeffs(Ftab, m, mu)
    N = 1 << n
    h = np.empty(1 << (n * m))
    for idx in range(1 << (n * m)):
        y = 0
        for j in range(m):
            if psi[(idx >> (n * j)) & (N - 1)] < 0:
                y |= 1 << j
        h[idx] = Ftab[y]
    Eh, Ih = EI(h, n * m)
    worst = 0.0
    for j in range(m):
        infj = sum(co[T] ** 2 for T in co if (T >> j) & 1)
        for i in range(n):
            I_pred = infj * Ip[i] / s2
            extra = sum(Phi(co[T] ** 2, co[T | (1 << j)] ** 2 * ph[1 << i] ** 2 / s2) for T in co if not (T >> j) & 1)
            E_pred = infj * Eprime[i] / s2 + extra
            k = j * n + i
            worst = max(worst, abs(I_pred - Ih[k]), abs(E_pred - Eh[k]))
    print(f"m={m} mu={mu:+.5f}: max |pred - direct| over (j,i) = {worst:.2e}; G(h) = {Eh.sum() / Ih.sum():.6f}, "
          f"G(psi) = {Ep.sum() / Ip.sum():.6f}, E'/I(psi) = {Eprime.sum() / Ip.sum():.6f}")
