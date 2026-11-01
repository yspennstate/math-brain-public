"""Exact rational values of T(f) = int_R cos(2 pi f v) Q(v)^2 dv, predicted and tested.

Q(v)^2 = cos^2(pi v) Q(2v/3)^2 and cos^2(pi v) = 1/2 + (1/2)cos(2 pi v) give, with
W_g = int cos(2 pi g v) Q(2v/3)^2 dv = (3/2) T(3g/2),

    T(f) = (3/4) T(3f/2) + (3/8) T(3(f+1)/2) + (3/8) T(3(f-1)/2).

T(f) = 2 rho(2f) with rho = nu*nu supported on |x| <= 6, so T VANISHES for |f| > 3. That truncation
closes the recursion on the integers:
    f = 0:  T(0) = (3/4)T(0) + (3/4)T(3/2)              ->  T(3/2) = T(0)/3      (the half-shift)
    f = 1:  T(1) = (3/4)T(3/2) + (3/8)T(3) + (3/8)T(0)  ->  T(1)   = (5/8)T(0)
    f = 2:  T(2) = (3/4)T(3) + (3/8)T(9/2) + (3/8)T(3/2)->  T(2)   = (1/8)T(0)
    f = 3:  T(3) = (3/8)T(3)                            ->  T(3)   = 0
PREDICTIONS: T(1)/T(0) = 0.625, T(2)/T(0) = 0.125, T(3)/T(0) = 0, T(3/2)/T(0) = 1/3, and T(f)=0 for f>3.
Any of these failing kills the derivation.
"""
import numpy as np

M, PTS, CH = 100_000.0, 400, 2_000_000
n_tot = int(M * PTS); du = M / n_tot
FS = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
acc = np.zeros(len(FS))
for s in range(0, n_tot, CH):
    k = min(CH, n_tot - s)
    v = (s + np.arange(k) + 0.5) * du
    q = np.ones(k); j = 0
    while True:
        a = (2.0/3.0) ** j * v
        q *= np.cos(np.pi * a); j += 1
        if a.max() < 1e-9: break
    q2 = q * q
    for i, f in enumerate(FS):
        acc[i] += (np.cos(2 * np.pi * f * v) * q2).sum() * du

pred = {0.0: 1.0, 1.5: 1/3, 1.0: 5/8, 2.0: 1/8, 3.0: 0.0, 3.5: 0.0, 4.0: 0.0}
print(f"{'f':>5} {'T(f)/T(0)':>13} {'predicted':>12} {'diff':>12}")
for i, f in enumerate(FS):
    r = acc[i] / acc[0]
    p = pred.get(f)
    if p is None:
        print(f"{f:>5.1f} {r:>13.8f} {'(not closed)':>12} {'':>12}")
    else:
        print(f"{f:>5.1f} {r:>13.8f} {p:>12.8f} {r-p:>+12.2e}")
print("\nT(f) must vanish for f > 3 - that support truncation is what closes the recursion.")
