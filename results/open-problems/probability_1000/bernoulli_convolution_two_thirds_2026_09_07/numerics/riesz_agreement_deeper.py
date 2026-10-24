"""Does the discrete-to-continuum agreement keep improving, or is it a coincidence of scales?

A_K = 2^(K+1) * (1/L) * sum_(k in W) F_K(k)   against   I_K = int_1^2 prod_(m=0..K)(1+cos(2 pi x (3/2)^m/3)) dx

The integrand oscillates at frequency (3/2)^K and the window has length L = (3/2)^K, so the discrete sum
is a Riemann sum in exactly the regime where such a sum can fail. Measured agreement so far: 1.2e-2 at
K=4, 1.7e-5 at K=8, 1.2e-5 at K=16, 1.1e-6 at K=22. If that keeps shrinking the equivalence is solid
numerically; if it turns around, my headline claim is in trouble.

SIZING (the standing rule): the quadrature needs many points per oscillation. At K the integrand has
about (3/2)^K periods on [1,2], so ppp = N/(3/2)^K points per period; keep ppp >= 64 and chunk so no
array exceeds ~64 MB.
"""
import numpy as np, sys

def A_discrete(K):
    L = max(1, int(round(1.5 ** K))); k0 = L
    tot = 0.0; CH = 1 << 20; s = 0
    while s < L:
        e = min(s + CH, L)
        k = np.arange(k0 + s, k0 + e, dtype=np.float64)
        F = np.ones_like(k)
        for i in range(K + 1):
            F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
        tot += float(F.sum()); s = e
    return (2.0 ** (K + 1)) * tot / L

def I_continuum(K, ppp=96):
    per = 1.5 ** K
    N = int(max(1 << 22, ppp * per))
    CH = 1 << 22
    acc = 0.0; done = 0
    while done < N:
        n = min(CH, N - done)
        x = 1.0 + (np.arange(done, done + n) + 0.5) / N
        P = np.ones_like(x)
        for m in range(K + 1):
            P *= 1.0 + np.cos(2 * np.pi * x * (1.5 ** m) / 3.0)
        acc += float(P.sum()); done += n
    return acc / N, N

print(f"{'K':>4} {'A_K discrete':>15} {'I_K continuum':>16} {'|diff|':>11} {'grid N':>12} {'pts/period':>11}")
for K in (8, 12, 16, 20, 22, 24, 26):
    A = A_discrete(K)
    I, N = I_continuum(K)
    print(f"{K:>4} {A:>15.9f} {I:>16.9f} {abs(A-I):>11.2e} {N:>12} {N/(1.5**K):>11.0f}")
    sys.stdout.flush()
