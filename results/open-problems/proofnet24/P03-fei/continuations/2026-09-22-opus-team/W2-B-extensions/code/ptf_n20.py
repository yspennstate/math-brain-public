"""Phi = min_r Sigma_r / I and H/I for a few degree-2 families at n = 20 (exact Walsh transform),
to extend the n <= 18 table: the transitive families (cycle, equal weights), dense Gaussian quadratics,
a random sparse quadratic, and the read-once 2-CNF on 20 variables."""
import time
import numpy as np
from fei_lib import *
setup_process()
n = 20
rng = np.random.default_rng(20)
X = coords(n)
rows = []
A = np.zeros((n, n))
for j in range(n):
    a, b = j, (j + 1) % n
    A[min(a, b), max(a, b)] = 1.0
rows.append(("cycle-equal", sgn(((X @ A) * X).sum(1) - 0.5)))
for rep in range(2):
    A = np.triu(rng.standard_normal((n, n)), 1)
    th = rng.normal(0, 1.0) * np.sqrt((A ** 2).sum())
    rows.append(("dense b=0", sgn(((X @ A) * X).sum(1) - th)))
A = np.zeros((n, n))
for _ in range(3 * n // 2):
    a, b = rng.choice(n, 2, replace=False)
    A[min(a, b), max(a, b)] = rng.standard_normal()
rows.append(("sparse3", sgn(((X @ A) * X).sum(1) - rng.normal(0, 0.5) * np.sqrt((A ** 2).sum()))))
cl = np.ones(X.shape[0], dtype=bool)
for j in range(n // 2):
    cl &= (X[:, 2 * j] < 0) | (X[:, 2 * j + 1] < 0)
rows.append(("2-CNF m=10", np.where(cl, -1.0, 1.0)))
with open("../logs/ptf_n20.log", "w") as lg:
    for name, f in rows:
        t0 = time.time()
        c = wht(f)
        H, I = HI(c, n)
        v, _ = phi_min(c, n)
        infl = influences(c, n)
        s_inf = sigma_of_order(c, n, list(np.argsort(-infl, kind="stable")))
        print("n=20 %-12s H/I=%.4f Phi=%.4f Sigma(infl)/I=%.4f (%.1fs)" % (name, H / I, v / I, s_inf / I, time.time() - t0), file=lg, flush=True)
