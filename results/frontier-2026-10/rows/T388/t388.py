"""T388 target 2: an explicit degree-4 spectral statistic for the spiked cumulant model, offline and streaming (Oja).

Model (2312.14922): x = S (z + beta g u), z ~ N(0, I_d), g Rademacher, S = I - (1 - 1/sqrt(1+beta^2)) u u^T, so Cov x = I and the
only signal is the fourth cumulant along u, kappa = kappa4(g) beta^4/(1+beta^2)^2 = -2 beta^4/(1+beta^2)^2.
Identity: E[(|x|^2 - d - 2) x x^T] = sum_k kappa4_{ijkk} = kappa u u^T. So M_n = (1/n) sum (|x|^2 - d - 2) x x^T is a rank-one
spike kappa u u^T plus noise of operator norm about 2 sqrt(2d) sqrt(d/n) = 2 sqrt 2 d/sqrt n, giving a threshold n ~ d^2.
(a) offline: overlap of the bottom eigenvector of M_n with u, at n = c d^2.
(b) streaming: Oja's rule w <- normalize(w - eta a_i (w.x_i) x_i), one pass, eta = 2 log(n)/(|kappa| n), random start.
"""
import math
import numpy as np

np.seterr(all="ignore")
rng = np.random.default_rng(7)
beta = 1.0
kappa = -2 * beta ** 4 / (1 + beta ** 2) ** 2


def sample(n, d, u):
    z = rng.standard_normal((n, d)); g = rng.choice([-1.0, 1.0], size=n)
    y = z + beta * g[:, None] * u[None, :]
    proj = y @ u
    return y - (1 - 1 / math.sqrt(1 + beta ** 2)) * proj[:, None] * u[None, :]


print(f"beta {beta}, kappa {kappa}; overlap |<w,u>| (mean over 3 seeds); n = c d^2")
print("d    c      offline    Oja-1pass   noise-norm prediction 2 sqrt2 d/sqrt n vs |kappa|")
for d in [16, 32, 64]:
    for c in [0.5, 2.0, 8.0, 32.0]:
        n = int(c * d * d)
        if n * d > 6e7:
            continue
        offs, ojas = [], []
        for seed in range(3):
            u = rng.standard_normal(d); u /= np.linalg.norm(u)
            M = np.zeros((d, d)); w = rng.standard_normal(d); w /= np.linalg.norm(w)
            eta = 2 * math.log(n) / (abs(kappa) * n)
            done = 0
            while done < n:
                b = min(20000, n - done)
                X = sample(b, d, u)
                a = (X * X).sum(1) - d - 2
                M += (X * a[:, None]).T @ X
                for i in range(b):
                    xi = X[i]
                    w -= eta * a[i] * (w @ xi) * xi
                    w /= np.linalg.norm(w)
                done += b
            M /= n
            ev, V = np.linalg.eigh(M)
            offs.append(abs(V[:, 0] @ u)); ojas.append(abs(w @ u))
        print(f"{d:3d}  {c:5.1f}   {np.mean(offs):.3f}      {np.mean(ojas):.3f}       {2 * math.sqrt(2) * d / math.sqrt(n):.3f} vs {abs(kappa):.2f}", flush=True)
