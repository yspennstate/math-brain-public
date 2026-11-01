# T354 iid, eps = 0: next-order term of the vanishing-step limit point (agent B, 20 Oct 2026).
# Expanding phi(y) = y^(-1/2) to third order and keeping every O(d^2) term of sqrt(V) D(x) (d = 1 - beta2, x* ~ d):
#   0 = x - (d K/2)(2 x B2 + B3)/V - (3/8) E[m (y-1)^2] + (5/16) E[m (y-1)^3] + O(d^3), with
#   E[m (y-1)^2] = d x S/(2 B2^2) + d^2 K2 E[b Z^2]/B2^2,  E[m (y-1)^3] = (3/2) d^2 K B3 S/B2^3,
# B_k = E b^k, Z = b^2 - B2, S = Var(b^2), K = (1-b1)/(1-b1 b2), K2 = (1-b1)/(1-b1 b2^2). Hence
#   x*/x0 = 1 + d [K + (3/4)(S/B2^2 - (K2/K) E[b Z^2]/(B2 B3))] + O(d^2),   x0 = d K B3/(2 B2).
# For a two-valued b, Z = (b_1 + b_2) b, so both ratios equal (b_1+b_2)^2/B2 and the bracket is K + (3/4)(b_1+b_2)^2/B2 (1 - K2/K).
# Argv: beta2 beta1 ...  (pairs). Model b = (9, -1 x 9).
import sys, numpy as np
import os; B = np.array([float(t) for t in os.environ["BVEC"].split(",")]); B2 = np.mean(B**2); B3 = np.mean(B**3); Z = B**2 - B2
S = np.mean(Z**2); EbZ2 = np.mean(B * Z**2)
a = [float(t) for t in sys.argv[1:]]
for b2, b1 in zip(a[0::2], a[1::2]):
    d = 1 - b2; K = (1 - b1) / (1 - b1 * b2); K2 = (1 - b1) / (1 - b1 * b2 * b2)
    br = K + 0.75 * (S / B2**2 - K2 / K * EbZ2 / (B2 * B3))
    print("beta2 %s beta1 %s  d/(1-b1) %.4g  bracket %.6f  predicted x*/x0 %.6f" % (b2, b1, d / (1 - b1) if b1 < 1 else float('inf'), br, 1 + d * br))
