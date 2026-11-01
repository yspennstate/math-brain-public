"""Does the corrected recursion C(u) = 2C(2u/3) - M(u)/2 reproduce the half-shift identity?

D = Y - Y' = (1/3) sum_{k<=K} eta_k (2/3)^k  (+ tail), eta_k in {-1,0,1} w.p. (1/4,1/2,1/4).
Clearing denominators, 3^(K+1) D = V = sum_k eta_k 2^k 3^(K-k) is an INTEGER, so the law at
depth K lives exactly on the lattice 1/3^(K+1) and can be built by integer shift-adds.

If g is the autocorrelation density (g = f * f~) then near the origin
    C(u) = P(|D| <= u) ~ 2 g(0) u,     M(u) = P(| |D| - 1/2 | <= u) ~ 4 g(1/2) u.
Substituting into the recursion:
    2g(0) = (4/3) 2g(0) - (1/2) 4 g(1/2)   =>   g(0) = 3 g(1/2),
which is exactly the half-shift identity ||f||^2 = 3 int f(x) f(x+1/2) dx.  The uncorrected
recursion (M, not M/2) would give C/M -> 3 and g(0) = 6 g(1/2), which that identity contradicts
by a factor of two.
"""
import numpy as np

K = 13
N = 3 ** (K + 1)                      # D = V / N, V integer
half = 3 ** (K + 1) - 2 ** (K + 1)    # max |V|
size = 2 * half + 1
p = np.zeros(size)
p[half] = 1.0                          # V = 0
for k in range(K + 1):
    s = (2 ** k) * (3 ** (K - k))
    q = 0.5 * p
    q[s:] += 0.25 * p[:size - s]
    q[:size - s] += 0.25 * p[s:]
    p = q
print(f"depth K={K}: lattice 1/{N}, {size} sites, mass {p.sum():.12f}, "
      f"truncation scale (2/3)^{K+1}/3 = {(2/3)**(K+1)/3:.2e}")

V = np.arange(-half, half + 1)
absV = np.abs(V)
# C(u) = P(|D| <= u) = sum over |V| <= u*N
order = np.argsort(absV, kind="stable")
aS, pS = absV[order], p[order]
cum = np.cumsum(pS)

def C(u):
    j = np.searchsorted(aS, u * N, side="right")
    return cum[j - 1] if j > 0 else 0.0

def M(u):
    lo = np.searchsorted(aS, (0.5 - u) * N, side="left")
    hi = np.searchsorted(aS, (0.5 + u) * N, side="right")
    return pS[lo:hi].sum()

print(f"{'u':>9} {'C(u)/u':>12} {'M(u)/u':>12} {'C/M':>10} {'recursion resid':>16}")
for u in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002]:
    c, m = C(u), M(u)
    resid = c - (2 * C(2 * u / 3) - m / 2)
    print(f"{u:>9.4f} {c/u:>12.6f} {m/u:>12.6f} {c/m:>10.6f} {resid:>16.2e}")

g0 = 1.2063100
print()
print(f"predicted C(u)/u -> 2 g(0)   = {2*g0:.6f}")
print(f"predicted M(u)/u -> 4 g(1/2) = {4*g0/3:.6f}   (half-shift identity g(1/2) = g(0)/3)")
print(f"predicted C/M    -> 3/2      = 1.500000")
print(f"WRONG-FACTOR (M, not M/2) would need C/M -> 3 and g(0) = 6 g(1/2); measured C/M rules it out")
