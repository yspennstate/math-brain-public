"""The functional equation muhat(3k) = muhat(2k) is satisfied by SINGULAR measures too.

muhat_p(xi) = prod_{k>=0} [(1-p) + p e(-xi (2/3)^k / 3)].  Then
  muhat_p(3 xi) = prod_{k>=0} [(1-p) + p e(-xi (2/3)^k)]
  muhat_p(2 xi) = prod_{k>=0} [(1-p) + p e(-xi (2/3)^(k+1))] = prod_{k>=1} [...]
so the quotient is the k = 0 factor, (1-p) + p e(-xi), which is 1 at every INTEGER xi.
Hence muhat_p(3k) = muhat_p(2k) for every integer k and EVERY p in (0,1).

For p < p* with H(p*) = log(3/2), dim mu_p <= H(p)/log(3/2) < 1, so mu_p is singular.
p* solves -p log p - (1-p) log(1-p) = log(3/2): p* = 0.11531.
Therefore the functional equation alone carries NO information about absolute continuity.
"""
import numpy as np
from math import log
from scipy.optimize import brentq

def muhat_p(xi, p, terms=200):
    xi = np.asarray(xi, dtype=float)
    out = np.ones_like(xi, dtype=complex)
    r = 1.0
    for _ in range(terms):
        out *= (1 - p) + p * np.exp(-2j * np.pi * xi * r / 3.0)
        r *= 2.0 / 3.0
        if r < 1e-18:
            break
    return out

k = np.arange(1, 3001, dtype=float)
print(f"{'p':>8}  max |muhat_p(3k) - muhat_p(2k)| over k <= 3000")
for p in (0.5, 0.35, 0.2113, 0.15, 0.10, 0.05, 0.02):
    d = np.abs(muhat_p(3 * k, p) - muhat_p(2 * k, p)).max()
    print(f"{p:>8.4f}  {d:.3e}")

f = lambda p: -(p * log(p) + (1 - p) * log(1 - p)) - log(1.5)
pstar = brentq(f, 1e-6, 0.5 - 1e-9)
print()
print(f"H(p) = log(3/2) at p* = {pstar:.5f}; for p < p* the dimension bound H(p)/log(3/2) < 1")
for p in (0.10, 0.05, 0.02):
    H = -(p * log(p) + (1 - p) * log(1 - p))
    print(f"  p={p:.2f}: H(p)/log(3/2) = {H/log(1.5):.4f}  -> singular, and it satisfies the equation")
