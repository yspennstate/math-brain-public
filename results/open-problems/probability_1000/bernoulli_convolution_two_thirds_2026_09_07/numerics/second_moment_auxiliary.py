"""What the exact second moment reduces to.

Var_{k0}(Err) = sum_{eps != 0} c_eps^2 |G(nu_eps)|^2   (verified exactly against the direct variance).
c_eps^2 = 4^-|supp eps| and sum_eps c_eps^2 = (3/2)^(K+1) EXACTLY, so the normalised weight makes each
coordinate independent with P(0) = 2/3 and P(+-1) = 1/6.  Solving p(1-p) = 1/6 gives
p = (1 + 1/sqrt 3)/2 = 0.7886751, and then 1 - 2p(1-p) = 2/3: the auxiliary digit law is exactly
eta = B - B' for B Bernoulli(p).  So the second moment is governed by the correlation integral of the
BIASED Bernoulli convolution at ratio 2/3 with p = 0.78868.

That is the honest accounting: the route transfers the difficulty, and it transfers it UPWARD.
Dimension ratio h(p)/log(3/2): the unbiased p = 1/2 gives log2/log(3/2) = 1.7095; the auxiliary p gives
H(p)/log(3/2) = 1.27.  Less room, not more -- the auxiliary instance is harder than the original.
"""
import numpy as np
from math import log, sqrt

p = (1 + 1 / sqrt(3)) / 2
print(f"p = (1 + 1/sqrt3)/2 = {p:.7f}")
print(f"  p(1-p)          = {p*(1-p):.7f}   (target 1/6 = {1/6:.7f})")
print(f"  1 - 2p(1-p)     = {1-2*p*(1-p):.7f}   (target 2/3 = {2/3:.7f})")
H = -(p * log(p) + (1 - p) * log(1 - p))
chi = log(1.5)
print(f"  H(p)            = {H:.6f} nats,  H(p)/log(3/2) = {H/chi:.4f}")
print(f"  unbiased        : log2/log(3/2)               = {log(2)/chi:.4f}")
print()

# check the weight law directly: normalised c^2 must reproduce the (2/3, 1/6, 1/6) product law
for K in (4, 6, 8):
    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64); c2 = np.ones(1); pr = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c2 = np.concatenate([c2 * 0.25, c2, c2 * 0.25])
        pr = np.concatenate([pr * (1 / 6), pr * (2 / 3), pr * (1 / 6)])
    tot = c2.sum()
    err = np.abs(c2 / tot - pr).max()
    print(f"K={K:>2}: sum c^2 = {tot:.6f}  vs (3/2)^(K+1) = {1.5**(K+1):.6f};  "
          f"max |c^2/sum - product law| = {err:.3e}")
