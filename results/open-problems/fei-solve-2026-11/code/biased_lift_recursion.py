"""Iterate h <- Maj_3(h, h, h) on a biased psi with the FLOW 12(hh) item 2 identity, exactly.
State per original coordinate i (all copies are equal by symmetry): a_i = hhat({i})^2, E_i, Inf_i, plus mu.
Next level: mu' = F^mu(empty); a'_i = F^mu({j})^2 a_i / s2; Inf'_i = Inf^mu_j Inf_i / s2;
E'_i = Inf^mu_j (E_i - Phi(mu^2, a_i)) / s2 + sum_{T not j} Phi(F^mu(T)^2, F^mu(T+j)^2 a_i / s2).
G = sum_i mult * E_i / sum_i mult * Inf_i, the multiplicity cancels. Checked against biased_comp_check.py at depth 1."""
import sys
import numpy as np
sys.argv = sys.argv[:1]
from biased_comp_check import Phi, biased_coeffs, psi, n, wht, EI  # noqa: E402

m = 3
Ftab = np.array([-1.0 if bin(y).count("1") > m // 2 else 1.0 for y in range(1 << m)])
mu = psi.mean(); ph = wht(psi)
a = np.array([ph[1 << i] ** 2 for i in range(n)])
E, I = EI(psi, n)
print(f"depth 0: mu {mu:+.6f} G {E.sum() / I.sum():.6f}")
for d in range(1, 13):
    s2 = 1 - mu * mu
    co = biased_coeffs(Ftab, m, mu)
    j = 0
    infj = sum(co[T] ** 2 for T in co if (T >> j) & 1)
    En = np.array([infj * (E[i] - Phi(mu * mu, a[i])) / s2
                   + sum(Phi(co[T] ** 2, co[T | 1] ** 2 * a[i] / s2) for T in co if not T & 1) for i in range(n)])
    I = infj * I / s2
    a = co[1] ** 2 * a / s2
    mu = co[0]; E = En
    print(f"depth {d}: mu {mu:+.6f} G {E.sum() / I.sum():.6f}  min_i E/Inf {np.min(E / I):.6f}")
