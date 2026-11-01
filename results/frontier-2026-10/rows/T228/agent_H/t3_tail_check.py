"""T228 target 3, numerical control for claim (2) of T3_CLAIM.md.

Simulates the class-(A) single-index SGD chain in R^d with Gaussian data,
    x' = x - c sum_i sigma'(a_i.x)(sigma(a_i.x) - y_i) a_i,  y_i = sigma(a_i.x*) + eps_i,
with sigma(z) = z + 0.5 tanh(z) (r = 0.5), x* = e_1, s = 1, and compares
  - alpha from the root of h(p) = E[((1-cX)^2 + c^2 X Y)^(p/2)] = 1 (Monte Carlo, fixed seed),
  - the Hill estimate of the tail index of |x| under the simulated stationary law,
  - c0 from the formula E[|Psi(x)|^alpha - |Mx|^alpha]/(alpha E xi^alpha log xi)
    against the empirical t^alpha P(|x| > t).
Memory: about 100 MB per case. Usage: python t3_tail_check.py [seed]
"""
import sys
import numpy as np

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 1
CASES = [(2, 1, 0.60), (2, 1, 0.80), (3, 2, 0.90)]
N_CHAIN, N_STEP, BURN, THIN = 4000, 100_000, 5_000, 20


def sigma(z):
    return z + 0.5 * np.tanh(z)


def dsigma(z):
    return 1.0 + 0.5 / np.cosh(z) ** 2


def h_root(d, b, eta, rng, n=4_000_000):
    c = eta / b
    X = rng.chisquare(b, n)
    Y = rng.chisquare(d - 1, n) if d > 1 else np.zeros(n)
    lx = 0.5 * np.log((1 - c * X) ** 2 + c * c * X * Y)
    gamma = lx.mean()
    if gamma >= 0:
        return gamma, None, None
    h = lambda p: np.exp(p * lx).mean()
    lo, hi = 1e-3, 1.0
    while h(hi) < 1:
        hi *= 2
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if h(mid) < 1 else (lo, mid)
    alpha = 0.5 * (lo + hi)
    m_alpha = (np.exp(alpha * lx) * lx).mean()
    return gamma, alpha, m_alpha


def step(x, d, b, c, xs, rng):
    n = x.shape[0]
    a = rng.standard_normal((n, b, d))
    eps = rng.standard_normal((n, b))
    z = np.einsum("nbd,nd->nb", a, x)
    y = sigma(a @ xs) + eps
    u = dsigma(z) * (sigma(z) - y)
    psi = x - c * np.einsum("nb,nbd->nd", u, a)
    mx = x - c * np.einsum("nb,nbd->nd", z, a)
    return psi, mx


def hill(sample, k):
    top = np.sort(sample)[-(k + 1):]
    return 1.0 / np.mean(np.log(top[1:] / top[0]))


def run(d, b, eta, rng):
    c = eta / b
    xs = np.zeros(d)
    xs[0] = 1.0
    gamma, alpha, m_alpha = h_root(d, b, eta, rng)
    print(f"\n(d, b, eta) = ({d}, {b}, {eta}): gamma = {gamma:.4f}", flush=True)
    if alpha is None:
        print("  (S_d) fails; skipped")
        return
    print(f"  root of h: alpha = {alpha:.4f}, m_alpha = {m_alpha:.4f}  (eta0 = {2*b/(b+d+1):.4f})", flush=True)
    x = np.zeros((N_CHAIN, d))
    keep = []
    xs_keep = []
    for k in range(N_STEP):
        x, _ = step(x, d, b, c, xs, rng)
        if k >= BURN and (k - BURN) % THIN == 0:
            keep.append(np.linalg.norm(x, axis=1).astype(np.float32))
            if len(xs_keep) < 50:
                xs_keep.append(x.copy())
    r = np.concatenate(keep).astype(np.float64)
    n = r.size
    print(f"  samples {n:,} (thinned {THIN}); median |x| = {np.median(r):.3g}, max = {r.max():.3g}")
    for frac in (0.01, 0.003, 0.001, 0.0003):
        kk = int(frac * n)
        print(f"  Hill, top {frac*100:.2f}% (k = {kk:,}): alpha_hat = {hill(r, kk):.4f}")
    # c0 from the formula: one fresh step from stationary points
    pts = np.concatenate(xs_keep)
    acc = []
    for _ in range(25):
        psi, mx = step(pts, d, b, c, xs, rng)
        acc.append(np.linalg.norm(psi, axis=1) ** alpha - np.linalg.norm(mx, axis=1) ** alpha)
    acc = np.concatenate(acc)
    c0 = acc.mean() / (alpha * m_alpha)
    se = acc.std() / np.sqrt(acc.size) / (alpha * m_alpha)
    print(f"  c0 formula = {c0:.4g} (+- {se:.2g} naive se, {acc.size:,} draws)")
    rs = np.sort(r)
    for q in (0.99, 0.999, 0.9999):
        t = rs[int(q * n)]
        print(f"  t = {t:.4g} (q {q}): t^alpha P(|x| > t) = {t**alpha * (1 - q):.4g}")


if __name__ == "__main__":
    rng = np.random.default_rng(SEED)
    print(f"seed {SEED}; chains {N_CHAIN}, steps {N_STEP}, burn {BURN}, thin {THIN}; sigma = z + 0.5 tanh z, x* = e1, s = 1")
    for case in CASES:
        run(*case, rng)
