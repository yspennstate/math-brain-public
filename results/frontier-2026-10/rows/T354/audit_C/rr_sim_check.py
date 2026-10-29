"""Direct RR simulation of the frozen-x drift E[m/(sqrt v + eps)] (agent C, T354 audit): validates rr_exact_mom_eps.D.
usage: python rr_sim_check.py BETA1 BETA2 EPS X"""
import sys
import numpy as np
from rr_exact_mom_eps import D

b1, b2, eps, x = map(float, sys.argv[1:5])
rng = np.random.default_rng(7)
b = np.array([9.0] + [-1.0] * 9)
C, E = 4000, 600  # chains, epochs
m = np.zeros(C)
v = np.full(C, np.mean((x + b) ** 2))
acc, cnt, means = 0.0, 0, []
for e in range(E):
    perm = np.argsort(rng.random((C, 10)), axis=1)
    run = np.zeros(C)
    for j in range(10):
        g = x + b[perm[:, j]]
        m = b1 * m + (1 - b1) * g
        v = b2 * v + (1 - b2) * g * g
        run += m / (np.sqrt(v) + eps)
    if e >= 100:
        means.append(run / 10)
means = np.array(means).mean(axis=0)  # per chain
print("RR beta1 %g beta2 %g eps %g x %g: exact %.6f  sim %.6f +/- %.6f" % (b1, b2, eps, x, D(x, b1, b2, eps), means.mean(),
                                                                            means.std() / np.sqrt(len(means))))
