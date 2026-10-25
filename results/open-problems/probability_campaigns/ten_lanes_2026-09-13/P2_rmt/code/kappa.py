"""kappa_M = density at 0 of sigma_min(G_M), G_M an M x M real standard Gaussian.
   Exact claim to test: P(sigma_min <= eps) = kappa_M eps + O(eps^2), kappa_M ~ sqrt(M) * c.
   Then the Poisson heuristic predicts  median omega = ln2 / (C(2M-1,M) kappa_M).
   Compare with the measured medians."""
import numpy as np, math
from math import comb, sqrt, pi, log
rng = np.random.default_rng(7)
meas = {2:1.790431e-01,3:4.528037e-02,4:1.138211e-02,5:2.514050e-03,6:6.609764e-04,
        7:1.611111e-04,8:3.606954e-05,9:8.804994e-06,10:2.493531e-06}
print(" M    kappa_M(MC)   kappa/sqrt(M)   C(2M-1,M)   predicted median   measured median   ratio")
for M in range(2,11):
    n = 400000
    G = rng.standard_normal((n,M,M))
    s = np.linalg.svd(G, compute_uv=False)[:,-1]
    # density at 0: use P(s<=h)/h for a small h, Richardson-extrapolated
    def F(h): return np.mean(s<=h)
    h = 0.02/ sqrt(M)
    k1 = F(h)/h; k2 = F(h/2)/(h/2)
    kappa = 2*k2 - k1                       # linear extrapolation to h->0
    C = comb(2*M-1, M)
    pred = log(2)/(C*kappa)
    print(f"{M:2d}   {kappa:9.5f}   {kappa/sqrt(M):9.5f}   {C:9d}   {pred:.6e}     {meas[M]:.6e}   {meas[M]/pred:.4f}")
print("\nlimit prediction: kappa_M -> sqrt(2M/pi)*? ; check kappa/sqrt(M) column")
print("Poisson limit for omega*4^M median:  ln2 * 2*sqrt(pi) =", log(2)*2*sqrt(pi))
