# |hat mu(2^n)| = prod_{k>=0} |cos(pi 2^{n+k} / 3^{k+1})|  -- an arithmetic product over powers of two mod powers of three.
# Verify against the direct product formula, then see which factors make it small.
from fractions import Fraction
import math, numpy as np
def hat_abs_direct(xi, terms=4000):
    out = 1.0; a = xi/3.0
    for _ in range(terms):
        out *= abs(math.cos(math.pi*a)); a *= 2.0/3.0
        if abs(a) < 1e-17: break
    return out
def hat_abs_arith(n, KMAX=200):
    # exact rational argument 2^{n+k}/3^{k+1} reduced mod 2 before the cosine (cos has period 2)
    out = 1.0; small = []
    for k in range(KMAX):
        num = 2**(n+k); den = 3**(k+1)
        r = Fraction(num, den) % 2            # exact reduction mod 2
        c = abs(math.cos(math.pi*float(r)))
        out *= c
        if c < 0.5: small.append((k, float(r), c))
        if (2**(n+k))/(3**(k+1)) < 1e-17 and k > n: break
    return out, small
print(" n | product formula | arithmetic form | factors < 0.5 (k, 2^(n+k)/3^(k+1) mod 2, |cos|)")
for n in range(0, 17):
    d = hat_abs_direct(2.0**n); a, sm = hat_abs_arith(n)
    print(f"{n:2d}  {d:.6e}   {a:.6e}   " + ", ".join(f"(k={k}, {r:.4f}, {c:.3f})" for k, r, c in sm[:4]))
