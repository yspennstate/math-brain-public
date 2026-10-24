"""An exact recursion for the increments, showing where their dependence comes from.

P_K = P_(K-1) (1 + cos(2 pi f_K t)),  f_K = (3/2)^K / 3,  I_K = I_(K-1) + C_K,
C_K = int_1^2 cos(2 pi f_K t) P_(K-1)(t) dt.

Then, using cos A cos B = (cos(A-B) + cos(A+B))/2 and f_(K+1) = (3/2) f_K:

  C_(K+1) = int cos(2 pi f_(K+1) t) P_(K-1) dt
          + (1/2) int cos(2 pi (f_K/2) t) P_(K-1) dt          <- f_(K+1) - f_K = f_K/2
          + (1/2) int cos(2 pi (5 f_K/2) t) P_(K-1) dt        <- f_(K+1) + f_K = 5 f_K/2

all three against the SAME P_(K-1). None of the three frequencies belongs to P_(K-1) (each would need
3^K/2 or similar to be an integer), so all three are interval-leakage terms, and leakage falls like
1/frequency - so the HALF-frequency term f_K/2 is the large one. That term is the entire source of
dependence between C_K and C_(K+1), and it is what a negative-dependence proof has to control.

Verify the identity numerically.
"""
import numpy as np

N = 1 << 22
x = 1 + (np.arange(N) + 0.5) / N
f = lambda K: (1.5 ** K) / 3.0

def P(K):
    out = np.ones(N)
    for m in range(K + 1):
        out *= 1.0 + np.cos(2 * np.pi * x * f(m))
    return out

print(f"{'K':>4} {'C_(K+1) direct':>17} {'three-term sum':>17} {'rel err':>10} {'half-freq share':>16}")
for K in (6, 8, 10, 12, 14):
    Pm1 = P(K - 1)
    direct = float((np.cos(2 * np.pi * f(K + 1) * x) * Pm1 * (1.0 + np.cos(2 * np.pi * f(K) * x))).mean())
    t1 = float((np.cos(2 * np.pi * f(K + 1) * x) * Pm1).mean())
    t2 = 0.5 * float((np.cos(2 * np.pi * (f(K) / 2) * x) * Pm1).mean())
    t3 = 0.5 * float((np.cos(2 * np.pi * (2.5 * f(K)) * x) * Pm1).mean())
    tot = t1 + t2 + t3
    rel = abs(direct - tot) / max(abs(direct), 1e-18)
    share = abs(t2) / (abs(t1) + abs(t2) + abs(t3))
    print(f"{K:>4} {direct:>17.9f} {tot:>17.9f} {rel:>10.2e} {share:>15.1%}")
