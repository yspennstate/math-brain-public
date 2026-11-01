"""Jensen step of BT-10: level-wise credits always dominate the global credit:
   sum_i I_i ln^+(4 pi_i/sigma_i^2)  <=  sum_k sum_i W_k pi_i^(k) ln^+(4 pi_i^(k)/sigma_i^2),  pi_i = I_i/V.
(x -> x ln^+(c x) is convex and pi_i = sum_k (W_k/V) pi_i^(k).)  Checked on random Boolean functions, exact P."""
import random
from fractions import Fraction as Fr
import mpmath
from bfcore import *
mpmath.mp.dps = 30
random.seed(10)
worst = mpmath.mpf(-1)
for trial in range(1500):
    n = random.randint(2, 6)
    T = [random.randint(0, 1) for _ in range(1 << n)]
    if 0 in (sum(T), len(T) - sum(T)):
        continue
    qs = [random.choice([Fr(random.randint(1, 999), 1000), Fr(1, 10**6), Fr(10**6 - 1, 10**6)]) for _ in range(n)]
    P = spectrum([2 * t - 1 for t in T], qs)
    V = sum(P[1:])
    g = mpmath.mpf(0)
    for i in range(n):
        Ii = sum(P[S] for S in range(1 << n) if (S >> i) & 1)
        a = 4 * (Ii / V) / sig2(qs[i])
        if Ii and a > 1:
            g += mpq(Ii) * mpmath.log(mpq(a))
    lw = mpmath.mpf(0)
    for k in range(1, n + 1):
        Wk = sum(P[S] for S in range(1 << n) if popcount(S) == k)
        if Wk == 0:
            continue
        for i in range(n):
            mass = sum(P[S] for S in range(1 << n) if popcount(S) == k and (S >> i) & 1)
            a = 4 * (mass / Wk) / sig2(qs[i])
            if mass and a > 1:
                lw += mpq(mass) * mpmath.log(mpq(a))
    worst = max(worst, g - lw)
print("max (global credit - level-wise credits) over 1500 random functions:", mpmath.nstr(worst, 6), "(must be <= 0)")
