"""Try to break the candidate answer C = 1 to Hasebe and Ueda's Problem 3.3.

Claim under test: if mu is supported in an interval of length 1 and u0 is a separating local minimum
of xi_R(u) = int dmu(x)/((x-u)^2+R^2), then xi_R(u0) >= 1.  Equivalently t*(mu) <= 1, so mu box+ S(0,t)
is unimodal for every t >= D^2 -- four times better than the published t >= 4D^2, and exactly tight at
the symmetric Bernoulli.  A single measure with xi_R(u0) < 1 refutes it.
"""
import numpy as np, sys
from free_unimod import xi, valleys

rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 5)
trials = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
worst, arg = np.inf, None
for k in range(trials):
    natoms = rng.integers(2, 7)
    # support of diameter exactly 1, endpoints always carrying mass
    inner = rng.uniform(-0.5, 0.5, size=max(0, natoms - 2))
    x = np.concatenate(([-0.5, 0.5], inner))
    w = rng.dirichlet(np.ones(len(x)) * rng.choice([0.3, 1.0, 3.0]))
    for R in np.linspace(1e-3, np.sqrt(3), 300):
        for m in valleys(x, w, R, n=1501):
            if m < worst:
                worst, arg = m, (x.copy(), w.copy(), R)
print(f"{trials} random measures, smallest separating-valley value of xi_R: {worst:.6f}")
print("  (the claim is that this cannot go below 1)")
x, w, R = arg
print("  attained at R =", round(R, 4))
print("  atoms  ", np.round(x, 4))
print("  weights", np.round(w, 4))
