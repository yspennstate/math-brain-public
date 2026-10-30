"""T228 target 2 numerics (supporting evidence only, not proof). Scalar leaky-ReLU SGD:
A+ = 1 - c*S, S = sum_i w(a_i)^2 a_i^2, w(a) = 1{a>0} + beta 1{a<0}, a ~ N(0,1), c = eta/b.
Index kappa solves E|A+|^kappa = 1 (Perron root of ABB's symmetric 2x2 Cramer matrix)."""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(1)

def draws(beta, b, n=4_000_000):
    a = rng.standard_normal((n, b))
    w = np.where(a > 0, 1.0, beta)
    return (w * w * a * a).sum(1)

def index(beta, b, c, S):
    A = np.abs(1 - c * S)
    Elog = np.log(A).mean()
    if Elog >= 0:
        return Elog, None, (A ** 2).mean()
    f = lambda k: np.log((A ** k).mean())
    hi = 0.5
    while f(hi) < 0 and hi < 40:
        hi *= 1.5
    return Elog, brentq(f, 1e-3, hi), (A ** 2).mean()

def sim(beta, b, c, xs=1.0, s=1.0, chains=20000, steps=3000):
    x = np.zeros(chains)
    for _ in range(steps):
        a = rng.standard_normal((chains, b))
        y = np.maximum(a * xs, beta * a * xs) + s * rng.standard_normal((chains, b))
        z = a * x[:, None]
        sp = np.where(z > 0, 1.0, beta)
        x = x - c * (sp * (np.maximum(z, beta * z) - y) * a).sum(1)
    return x

def hill(v, k):
    v = np.sort(np.abs(v))[::-1]
    return 1.0 / np.mean(np.log(v[:k] / v[k]))

print("beta b c  Elog|A|  kappa  E A^2")
for beta in (0.0, 0.1, 0.5):
    for b in (1, 4):
        S = draws(beta, b)
        for eta in (0.5, 1.0, 1.5, 2.5):
            c = eta / b
            e, k, m2 = index(beta, b, c, S)
            print(f"{beta:4} {b} {c:5.3f} {e:8.4f} {('none' if k is None else f'{k:6.3f}')} {m2:7.3f}")
for beta, b, eta in ((0.1, 1, 1.0), (0.5, 4, 2.5)):
    c = eta / b
    S = draws(beta, b)
    k = index(beta, b, c, S)[1]
    x = sim(beta, b, c)
    pos, neg = (x > 0).sum(), (x < 0).sum()
    print(f"sim beta {beta} b {b} c {c}: kappa {k:.3f}, Hill(k=200) {hill(x, 200):.3f}, Hill(k=500) {hill(x, 500):.3f}; "
          f"top-1% sign split +{(np.sort(np.abs(x))[-200:] == np.abs(x[x > 0])[:, None]).any(0).sum()}/200")
