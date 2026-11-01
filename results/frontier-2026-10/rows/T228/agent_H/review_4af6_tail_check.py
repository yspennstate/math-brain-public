# Reviewer control for T228 target 3 (agent AF): simulate the class-(A) chain in R^d and compare the Hill tail
# index of |x| under (approximately) pi with alpha from E xi^alpha = 1 computed independently.
import numpy as np, sys
d, b, eta = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
c = eta / b; s = 0.5; rng = np.random.default_rng(20261022)
phi = lambda z: 0.5 * np.tanh(z); dphi = lambda z: 0.5 / np.cosh(z) ** 2
sig = lambda z: z + phi(z); dsig = lambda z: 1 + dphi(z)
# alpha: bisection on a fixed 4M-draw sample of xi
X = rng.chisquare(b, 4_000_000); Y = rng.chisquare(d - 1, 4_000_000) if d > 1 else 0.0
xi = np.sqrt((1 - c * X) ** 2 + c * c * X * Y); lx = np.log(xi)
h = lambda p: np.mean(np.exp(p * lx))
print("gamma %.4f" % lx.mean())
lo, hi = 1e-3, 20.0
for _ in range(60):
    mid = (lo + hi) / 2
    (lo, hi) = (mid, hi) if h(mid) < 1 else (lo, mid)
alpha = lo; print("alpha %.4f" % alpha)
N, T = 200_000, 2000
xs = np.zeros(d); xs[0] = 1.0
x = rng.standard_normal((N, d))
for k in range(1, T + 1):
    g = np.zeros_like(x)
    for i in range(b):
        a = rng.standard_normal((N, d)); e = rng.normal(0, s, N)
        z = a @ x.T if False else np.einsum("nd,nd->n", a, x)
        y = sig(a @ xs) + e
        g += (dsig(z) * (sig(z) - y))[:, None] * a
    x = x - c * g
    if k in (1000, 1500, 2000):
        r = np.sort(np.linalg.norm(x, axis=1))[::-1]
        out = []
        for kk in (200, 500, 1000, 2000):
            hill = 1.0 / np.mean(np.log(r[:kk] / r[kk]))
            out.append("k=%d %.3f" % (kk, hill))
        print("step %d  Hill: %s" % (k, "  ".join(out)))
