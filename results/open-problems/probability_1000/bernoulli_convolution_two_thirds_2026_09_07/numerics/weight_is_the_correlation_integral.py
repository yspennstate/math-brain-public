"""The (4/3)^K growth of the absolute sum IS the correlation integral, with the same constant.

c(eps) = 2^(-#nonzero eps_i) on {-1,0,1}^(K+1) and nu(eps) = sum_i eps_i 2^i 3^(K-i).
Normalising, c(eps)/2^(K+1) is exactly the probability of the pattern eps under eta_i iid with
P(0) = 1/2, P(+-1) = 1/4 -- and eta = B - B' for fair bits.  So

    c(m) = 2^(K+1) P(V = m),    V = sum_i eta_i 2^i 3^(K-i) = 3^(K+1) (Y - Y') at depth K.

Hence the cumulative weight on the block is
    Cum(u) = sum_{0 < m <= u 2^K} c(m) = 2^K P( 0 < |3(Y-Y')| <= u (2/3)^K )
           ~ 2^K * (2/3)||f||^2 * u (2/3)^K = (2/3)||f||^2 * u * (4/3)^K.

So the (4/3)^K is not a window artifact to be removed by a smoother majorant: it is the linear growth
of the correlation integral, i.e. mu in L^2, with the constant (2/3)||f||^2 = 0.80421.
"""
import numpy as np

# 1. the identity c(m) = 2^(K+1) P(V = m), checked exactly at small K
for K in (3, 5, 7):
    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64); c = np.ones(1); pr = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c = np.concatenate([c * 0.5, c, c * 0.5])
        pr = np.concatenate([pr * 0.25, pr * 0.5, pr * 0.25])
    err = np.abs(c - (2.0 ** (K + 1)) * pr).max()
    print(f"K={K:>2}: max |c - 2^(K+1) P(V)| over all {3**(K+1)} patterns = {err:.3e}")

# 2. the profile constant, extrapolated
print()
print("Cum(u)/(u (4/3)^K) at u = 1, against the predicted (2/3)||f||^2 = 0.804207:")
def block(K):
    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64); c = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c = np.concatenate([c * 0.5, c, c * 0.5])
    B = 2 ** (K + 1) - 1
    s = (nu >= 1) & (nu <= B)
    m, cm = nu[s], c[s]
    o = np.argsort(m)
    return m[o].astype(float), np.cumsum(cm[o])

vals = []
for K in (6, 8, 10, 12, 14):
    m, cum = block(K)
    j = np.searchsorted(m, 1.0 * 2 ** K, side="right")
    v = cum[j - 1] / ((4.0 / 3.0) ** K)
    vals.append((K, v))
    print(f"  K={K:>3}: {v:.6f}")
# Richardson on the last three, assuming error ~ a * rho^K
(K1, v1), (K2, v2), (K3, v3) = vals[-3:]
rho = (v3 - v2) / (v2 - v1)
lim = v3 + (v3 - v2) * rho / (1 - rho)
print(f"  geometric extrapolation (ratio {rho:.4f}) -> {lim:.6f}")
print(f"  predicted (2/3)*1.206310                  =  0.804207")
