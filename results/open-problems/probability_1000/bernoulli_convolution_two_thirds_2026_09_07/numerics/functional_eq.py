# The exact functional equation.  3Y = B + 2Y' with Y' an independent copy, so frac(3Y) ~ frac(2Y),
# i.e. T_3 mu = T_2 mu, i.e.   hat_mu(3k) = hat_mu(2k)  for EVERY integer k.
# Consequence: for k = 2^a 3^b m with gcd(m,6)=1, hat_mu(k) = hat_mu(2^{a+b} m) -- the value depends only on
# the TOTAL number of 2s and 3s.  So the multiplicity of the value hat_mu(2^s m) among k <= X is (s+1)-ish, and
#   sum_{k != 0} |hat_mu(k)|^2 = sum_{gcd(m,6)=1} sum_{s>=0} (s+1) |hat_mu(2^s m)|^2 .
import numpy as np, math
def hat_mu(xi, terms=4000):
    xi = np.asarray(xi, dtype=np.float64); out = np.ones(xi.shape, dtype=np.complex128); a = xi/3.0
    for _ in range(terms):
        out *= (1 + np.exp(-2j*np.pi*a))/2; a *= 2.0/3.0
        if np.max(np.abs(a)) < 1e-16: break
    return out
ks = np.arange(1, 4001, dtype=np.float64)
h2 = hat_mu(2*ks); h3 = hat_mu(3*ks)
print(f"functional equation hat_mu(3k) = hat_mu(2k), k = 1..4000:  max|difference| = {np.abs(h2-h3).max():.3e}")
# the (a,b) -> a+b collapse
print("\ncheck the collapse hat_mu(2^a 3^b m) = hat_mu(2^{a+b} m) on random (a,b,m):")
bad = 0.0
for m in [1,5,7,11,13,25,49,101]:
    for a in range(0,6):
        for b in range(0,6):
            k = (2**a)*(3**b)*m; kk = (2**(a+b))*m
            if k > 10**12 or kk > 10**12: continue
            d = abs(complex(hat_mu(np.array([float(k)]))[0]) - complex(hat_mu(np.array([float(kk)]))[0]))
            bad = max(bad, d)
print(f"   max|difference| over 8 x 6 x 6 triples = {bad:.3e}")
# the resulting weighted series, truncated
print("\nthe weighted series  sum_{gcd(m,6)=1} sum_s (s+1)|hat_mu(2^s m)|^2  against the direct sum over k:")
X = 2**22
direct = 0.0
step = 1 << 16
for lo in range(1, X, step):
    kk = np.arange(lo, min(lo+step, X), dtype=np.float64)
    direct += float(np.sum(np.abs(hat_mu(kk))**2))
print(f"   direct sum over 1 <= k < {X}: {direct:.6f}   (int f^2 - 1 = 0.206310 is the infinite value)")
