import numpy as np
from cover_exact import *
rng = np.random.default_rng(1)
def randW(n, loops=True, spread=2.0):
    A = np.exp(rng.normal(0, spread, (n, n))); W = (A + A.T) / 2
    if not loops: np.fill_diagonal(W, 0)
    return W
f = lambda W: E_pi_cover(rw_on_graph(W))
for n in [3, 4, 5, 6]:
    viol_q = 0; viol_c = 0; tot = 0; worst = 0
    for trial in range(300 if n < 6 else 80):
        W1 = randW(n, loops=rng.random() < 0.3); W2 = randW(n, loops=rng.random() < 0.3)
        # normalize scale so the segment is meaningful
        W1 /= W1.sum(); W2 /= W2.sum()
        f1, f2 = f(W1), f(W2)
        for lam in [0.25, 0.5, 0.75]:
            fm = f(lam * W1 + (1 - lam) * W2)
            tot += 1
            if fm > max(f1, f2) + 1e-9:
                viol_q += 1; worst = max(worst, fm / max(f1, f2))
            if fm > lam * f1 + (1 - lam) * f2 + 1e-9: viol_c += 1
    print("n=%d segments=%d quasi-convexity violations=%d (worst ratio %.4f) convexity violations=%d" % (n, tot, viol_q, worst, viol_c))
# symmetrization test: f(orbit average) <= f(W)?  orbit average of W is a(J-I)+bI: K_n with loops b/a. Check K_n with loops is monotone in loop weight.
for n in [4, 6]:
    for b in [0, 0.1, 0.5, 1, 2]:
        W = np.ones((n, n)) - np.eye(n) + b * np.eye(n)
        print("n=%d loop weight %.1f: E_pi C = %.5f" % (n, b, f(W)))
