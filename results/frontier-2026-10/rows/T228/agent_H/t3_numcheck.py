"""T228 target 3 checks (agent H, 22 Oct). M = I - (eta/b) sum a a^T, a ~ N(0,I_d).
(1) |M u| has the same law for every unit u, and that law is sqrt((1-cX)^2 + c^2 X Y), X~chi2_b, Y~chi2_{d-1}.
(2) h(2) = 1 - 2eta + eta^2 (b+d+1)/b, so alpha<2 iff eta > 2b/(b+d+1).
(3) gamma = E log|M e1| < 0 on a range; alpha root of h(alpha)=1."""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(7)
def norms(d, b, eta, u, n):
    a = rng.standard_normal((n, b, d)); c = eta / b
    Mu = u[None, :] - c * np.einsum('nbi,nb->ni', a, a @ u)
    return np.linalg.norm(Mu, axis=1)
def formula(d, b, eta, n):
    c = eta / b; X = rng.chisquare(b, n); Y = rng.chisquare(d - 1, n) if d > 1 else 0.0
    return np.sqrt((1 - c * X) ** 2 + c ** 2 * X * Y)
for d, b, eta in [(3, 2, 0.5), (5, 4, 1.0), (10, 8, 0.9)]:
    us = [np.eye(d)[0], np.ones(d) / np.sqrt(d), rng.standard_normal(d)]
    us[2] /= np.linalg.norm(us[2])
    qs = [np.quantile(norms(d, b, eta, u, 200000), [.1, .5, .9]) for u in us]
    f = np.quantile(formula(d, b, eta, 400000), [.1, .5, .9])
    m2 = np.mean(formula(d, b, eta, 400000) ** 2)
    print(f"d={d} b={b} eta={eta}: quantiles by direction {np.round(qs,4).tolist()} formula {np.round(f,4).tolist()} "
          f"E|Me1|^2 MC {m2:.4f} exact {1-2*eta+eta**2*(b+d+1)/b:.4f}")
# exact index by quadrature-free MC with common random numbers
def index(d, b, eta, n=2_000_000):
    c = eta / b; X = rng.chisquare(b, n); Y = rng.chisquare(d - 1, n) if d > 1 else np.zeros(n)
    L = 0.5 * np.log((1 - c * X) ** 2 + c ** 2 * X * Y)
    g = L.mean()
    if g >= 0: return g, None
    hm1 = lambda s: np.mean(np.exp(s * L)) - 1
    hi = 0.5
    while hm1(hi) < 0 and hi < 60: hi *= 2
    return g, (brentq(hm1, 1e-3, hi) if hm1(hi) > 0 else None)
for d in (1, 2, 5, 10):
    for b in (1, 4):
        row = []
        for eta in (0.3, 0.6, 1.0, 1.5):
            g, al = index(d, b, eta)
            row.append(f"eta={eta}: gamma={g:+.3f} alpha={'none' if al is None else f'{al:.3f}'}")
        print(f"d={d} b={b} thr2={2*b/(b+d+1):.3f} | " + " | ".join(row))
