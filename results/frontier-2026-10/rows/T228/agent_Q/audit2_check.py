"""T228 target 3 v2, second independent audit (agent Q, 22 Oct 2026). Written without reading the author's
t3_tail_check.py or the first reviewer's script. Three checks:
  (a) the root alpha of h(p) = E[((1 - cX)^2 + c^2 X Y)^(p/2)] = 1, X ~ chi2_b, Y ~ chi2_(d-1), by bisection on
      common random numbers;
  (b) Lemma R directly: |M u| for M = I - c sum a_i a_i^T against the chi2 form, for two different unit u;
  (c) the chain itself: Hill estimate on |x| and t^alpha P(|x| > t) against the c0 formula of claim (2).
    python audit2_check.py D B ETA [CHAINS STEPS SEED]"""
import sys

import numpy as np

d, b, eta = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
chains = int(sys.argv[4]) if len(sys.argv) > 4 else 2000
steps = int(sys.argv[5]) if len(sys.argv) > 5 else 40000
seed = int(sys.argv[6]) if len(sys.argv) > 6 else 7
rng = np.random.default_rng(seed)
c = eta / b
s = 1.0
xs = np.zeros(d)
xs[0] = 1.0

# (a) the index
X = rng.chisquare(b, 4_000_000)
Y = rng.chisquare(d - 1, 4_000_000) if d > 1 else np.zeros(4_000_000)
lxi = 0.5 * np.log((1 - c * X) ** 2 + c * c * X * Y)
gamma = lxi.mean()


def logh(p):
    m = (p * lxi).max()
    return m + np.log(np.mean(np.exp(p * lxi - m)))


lo, hi = 1e-3, 1.0
while logh(hi) < 0:
    hi *= 2
for _ in range(60):
    mid = 0.5 * (lo + hi)
    lo, hi = (mid, hi) if logh(mid) < 0 else (lo, mid)
alpha = 0.5 * (lo + hi)
w = np.exp(alpha * lxi)
den = alpha * np.mean(w * lxi)
print("d=%d b=%d eta=%.3f  gamma=E log xi=%.4f  alpha=%.4f  E xi^2 MC %.4f formula %.4f  eta0=%.4f"
      % (d, b, eta, gamma, alpha, np.mean(np.exp(2 * lxi)), 1 - 2 * eta + eta ** 2 * (b + d + 1) / b,
         2.0 * b / (b + d + 1)))
del X, Y, w

# (b) Lemma R
n = 400_000
for u in (np.eye(d)[0], np.ones(d) / np.sqrt(d)):
    a = rng.standard_normal((n, b, d))
    au = a @ u
    Mu = u[None, :] - c * np.einsum("nb,nbd->nd", au, a)
    r = np.linalg.norm(Mu, axis=1)
    Xs = rng.chisquare(b, n)
    Ys = rng.chisquare(d - 1, n) if d > 1 else np.zeros(n)
    xi = np.sqrt((1 - c * Xs) ** 2 + c * c * Xs * Ys)
    qs = [0.1, 0.5, 0.9, 0.99]
    print("Lemma R u=%s  |Mu| quantiles %s  xi quantiles %s" % (
        np.round(u, 3), np.round(np.quantile(r, qs), 4), np.round(np.quantile(xi, qs), 4)))
del a


# (c) the chain
def sig(z):
    return z + 0.5 * np.tanh(z)


def dsig(z):
    return 1 + 0.5 / np.cosh(z) ** 2


def step(x, a, eps):
    z = np.einsum("nbd,nd->nb", a, x)
    y = sig(a @ xs) + eps
    g = dsig(z) * (sig(z) - y)
    return x - c * np.einsum("nb,nbd->nd", g, a)


x = np.zeros((chains, d))
samp = []
burn, thin = 2000, 20
for k in range(steps):
    a = rng.standard_normal((chains, b, d))
    x = step(x, a, s * rng.standard_normal((chains, b)))
    if k >= burn and k % thin == 0:
        samp.append(x.copy())
S = np.concatenate(samp)
R = np.linalg.norm(S, axis=1)
Rs = np.sort(R)[::-1]
N = len(R)
hill = []
for kk in (1000, 3000, 10000, 30000, 100000):
    if kk < N:
        hill.append((kk, 1.0 / np.mean(np.log(Rs[:kk] / Rs[kk]))))
print("chain: %d samples; Hill %s" % (N, ", ".join("k=%d %.3f" % h for h in hill)))
emp = []
for q in (0.99, 0.999, 0.9999):
    t = np.quantile(R, q)
    emp.append("q%.4g t=%.2f %.3f" % (q, t, t ** alpha * (1 - q)))
# c0 formula: one fresh step from stationary samples (thin further to keep memory small)
P = S[:: max(1, N // 400_000)]
a = rng.standard_normal((len(P), b, d))
eps = s * rng.standard_normal((len(P), b))
psi = np.linalg.norm(step(P, a, eps), axis=1)
Mx = np.linalg.norm(P - c * np.einsum("nb,nbd->nd", np.einsum("nbd,nd->nb", a, P), a), axis=1)
num = psi ** alpha - Mx ** alpha
c0 = num.mean() / den
se = num.std() / np.sqrt(len(num)) / den
print("c0 formula %.3f +- %.3f   empirical t^alpha P(|x|>t): %s" % (c0, se, "; ".join(emp)))
