"""E0046 (Bandeira Open Problem 1.2, complex case): sigma_C(n) = E[(1/n) sum sigma_i(G/sqrt n)] for n x n complex Ginibre.
Squared singular values ~ LUE (square case): one-point density rho_n(x) = e^{-x} sum_{k<n} L_k(x)^2.
So E tr sqrt(GG*) = sum_{k<n} a_k,  a_k = int_0^inf sqrt(x) e^{-x} L_k(x)^2 dx,  and sigma_C(n) = S_n / n^{3/2}."""
import numpy as np
from mpmath import mp, mpf, quad, laguerre, sqrt, exp, gamma, binomial, pi
mp.dps = 30
def a(k):
    return quad(lambda x: sqrt(x)*exp(-x)*laguerre(k, 0, x)**2, [0, 5, 20, 60, 200, mp.inf])
A = [a(k) for k in range(0, 41)]
S = np.cumsum([float(v) for v in A])
print("a_k for k=0..8:", [mp.nstr(v, 12) for v in A[:9]])
print("a_k / sqrt(k) for k=10,20,40:", [mp.nstr(A[k]/sqrt(k), 8) for k in (10,20,40)], "  (2/pi =", mp.nstr(2/pi,8), ")")
# candidate closed form: Gamma(3/2) * sum_{j<=k} binom(1/2, j)^2  ?
cand = [gamma(mpf(3)/2)*sum(binomial(mpf(1)/2, j)**2 for j in range(k+1)) for k in range(6)]
print("candidate Gamma(3/2) sum binom(1/2,j)^2:", [mp.nstr(v,10) for v in cand])
print("\n n   sigma_C(n)=S_n/n^1.5      diff to next    ratio a_n/S_n vs (1+1/n)^1.5-1")
for n in range(1, 41):
    s = S[n-1]/n**1.5; s2 = S[n]/(n+1)**1.5 if n < 41 else float('nan')
    print(f"{n:2d}  {s:.12f}   {s2-s:+.3e}   {float(A[n])/S[n-1]:.6f} vs {(1+1/n)**1.5-1:.6f}")
print("limit 8/(3 pi) =", 8/(3*np.pi))
