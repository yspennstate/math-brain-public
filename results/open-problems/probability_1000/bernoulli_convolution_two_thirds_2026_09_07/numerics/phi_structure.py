"""The increments sample one function at four points. Which of them can matter?

Write Phi(u) = int_1^2 cos(2 pi u t) P_(K-1)(t) dt. Then
    C_K     = Phi(f_K)
    C_(K+1) = Phi(1.5 f_K) + (1/2) Phi(0.5 f_K) + (1/2) Phi(2.5 f_K).
P_(K-1) has frequencies sum_(m<=K-1) eps_m (3/2)^m/3 with eps in {0,+-1}, so its LARGEST is
    sum_(m<=K-1) (3/2)^m/3 = 2 f_K - 2/3,
just under 2 f_K. So 0.5 f_K, f_K and 1.5 f_K lie INSIDE the spectrum while 2.5 f_K lies OUTSIDE it -
the third term should be pure tail and negligible. Check that, then look at how Phi behaves across the
band, since consecutive increments sample it at f and at its two neighbours 0.5 f and 1.5 f.
"""
import numpy as np

N = 1 << 21
x = 1 + (np.arange(N) + 0.5) / N
f = lambda K: (1.5 ** K) / 3.0

def P(K):
    out = np.ones(N)
    for m in range(K + 1):
        out *= 1.0 + np.cos(2 * np.pi * x * f(m))
    return out

def Phi(Pm1, u):
    return float((np.cos(2 * np.pi * u * x) * Pm1).mean())

print(f"{'K':>4} {'max freq / f_K':>15} {'C_K':>12} {'T1 (1.5f)':>12} {'T2 (0.5f)':>12} {'T3 (2.5f)':>12} {'|T3|/|C_(K+1)|':>15}")
for K in (8, 10, 12, 14, 16):
    Pm1 = P(K - 1)
    fk = f(K)
    maxfreq = sum(f(m) for m in range(K))
    C_K = Phi(Pm1, fk)
    T1 = Phi(Pm1, 1.5 * fk)
    T2 = 0.5 * Phi(Pm1, 0.5 * fk)
    T3 = 0.5 * Phi(Pm1, 2.5 * fk)
    tot = T1 + T2 + T3
    print(f"{K:>4} {maxfreq/fk:>15.4f} {C_K:>12.6f} {T1:>12.6f} {T2:>12.6f} {T3:>12.3e} {abs(T3)/max(abs(tot),1e-18):>15.2e}")
