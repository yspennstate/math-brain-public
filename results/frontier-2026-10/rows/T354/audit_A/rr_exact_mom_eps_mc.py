# Validation of the reduction in rr_exact_mom_eps.py with momentum and eps (agent A, 20 Oct): direct RR stream at frozen x,
# m and v run by their recursions, D(x) = mean m/(sqrt v + eps) over 400 independent chains x 4,000 epochs after 200 burn-in epochs.
# Argv: beta1 beta2 eps x [seed].
import sys, numpy as np
b1, b2, eps, x = (float(a) for a in sys.argv[1:5]); n = 10; rng = np.random.default_rng(int(sys.argv[5]) if len(sys.argv) > 5 else 354)
C, Ep, burn = 400, 4000, 200
m = np.zeros(C); v = np.full(C, (x - 1) ** 2 + 8.0); acc = []
for e in range(Ep + burn):
    pos = rng.integers(0, n, C)
    s = np.zeros(C)
    for p in range(n):
        g = x + np.where(pos == p, 9.0, -1.0)
        m = b1 * m + (1 - b1) * g; v = b2 * v + (1 - b2) * g * g
        s += m / (np.sqrt(v) + eps)
    if e >= burn: acc.append(s / n)
A = np.array(acc); per_chain = A.mean(0)
print("MC beta1 %s beta2 %s eps %s x %s: D = %.6e +/- %.1e" % (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], per_chain.mean(), per_chain.std() / np.sqrt(C)))
