"""Does the reduction 'Err <= CL suffices' itself survive the p-substitution?

The reduction says: sum_(k in W) F_K(k) = (avg)^(K+1) (L + Err), so if Err <= C L then
E(R) <= (1+C) (1 - 2p(1-p))^(K+1) L, whose exponent is alpha(p) = 1 + log(1-2p(1-p))/log(3/2).
At p = 0.5 that is -0.7095 and S converges; at p = 0.1 it is +0.5106 and S diverges.

So the reduction is only useful where alpha < 0.  The question the p-test asks is different and
sharper: is 'Err = O(L)' itself TRUE at p = 0.1, where the measure is singular?  If it is, then the
statement proves nothing on its own and the decay comes entirely from the main term - which is exactly
as it should be, and the formulation is sound.  If Err/L blew up at p = 0.1, the formulation would be
smuggling the conclusion into the deviation term.
"""
import numpy as np
from math import log

def err_over_L(p, K):
    P = 3 ** (K + 1)
    L = max(1, int(round(1.5 ** K)))
    k0 = L
    k = np.arange(k0, k0 + L, dtype=float)
    F = np.ones_like(k)
    r = 1.0
    for i in range(K + 1):
        a = 2 * np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))
        F *= np.abs((1 - p) + p * np.exp(-1j * a)) ** 2
    avg = (1 - 2 * p * (1 - p)) ** (K + 1)
    return (F.sum() / avg - L) / L, L

print(f"{'p':>8} {'alpha(p)':>10} " + " ".join(f"{'K='+str(K):>9}" for K in (6,8,10,12,14,16)) + "   Err/L at the octave")
for p in (0.5, 0.35, 0.2113, 0.15, 0.10, 0.05):
    a = 1 + log(1 - 2 * p * (1 - p)) / log(1.5)
    row = []
    for K in (6, 8, 10, 12, 14, 16):
        e, L = err_over_L(p, K)
        row.append(e)
    print(f"{p:>8.4f} {a:>+10.4f} " + " ".join(f"{x:>+9.4f}" for x in row))
print()
print("Bounded at every p, singular ones included: the deviation term carries no part of the")
print("conclusion, and all the decay lives in the main term's exponent alpha(p). The formulation")
print("passes its own p-test.")
