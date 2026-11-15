"""Odd circulants, refined: sum g Q <= (8 lam / n)((n-1) lam - 2)  (Cauchy-Schwarz on sum a_s^2 (1 - C_k(s)))
and sum g P >= ((n-1) lam - 2)/2 * K(lam). Both vanish at lam = 2/(n-1); ratio <= 1 follows from
E(lam) = K(lam)/2 - 8 lam / n >= 0 on [2/(n-1), 4/n]. E is linear in lam: check both ends exactly (fractions)."""
from fractions import Fraction as F
def E(n, lam):
    K = 8 * lam / (n - 2) - F(32, n * (n - 2)) + 4 * (1 - lam) * (n - 4) / F((n - 2) ** 2)
    return K / 2 - 8 * lam / n
bad = []
for n in range(5, 202, 2):
    e1, e2 = E(n, F(2, n - 1)), E(n, F(4, n))
    if n <= 15 or min(e1, e2) <= 0:
        print("n %3d  E(2/(n-1)) %+.5f  E(4/n) %+.5f" % (n, float(e1), float(e2)))
    if min(e1, e2) <= 0:
        bad.append(n)
print("odd n in 5..201 where an end is <= 0:", bad)
