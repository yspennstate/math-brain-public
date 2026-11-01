"""Two things a verifier caught that I did not.

(1) Err >= -L IS FREE. F_K = |truncated muhat|^2 >= 0, so sum_(k in W) F_K >= 0, and since
    sum_W F_K = 2^-(K+1) (L + Err), that gives L + Err >= 0, i.e. Err >= -L. One line, no Fourier, no
    equidistribution, every p, every window position. The exact-zero mechanism's "zeroth order gives
    Err/L = -1 exactly" lands precisely ON that free floor: it predicts A_K = 1 + Err/L = 0 while the
    truth is A_K ~ 0.05, so it captures none of the quantity at issue and bounds it in no direction.

(2) THE CONTINUUM FORM, which is the real prize. Integrality drops out:
        A_K  ->  int_1^2 prod_(m=0..K) (1 + cos(2 pi x (3/2)^m / 3)) dx
    so Err = O(L) is equivalent to the boundedness in K of a Riesz product with the non-Pisot ratio 3/2 -
    Erdos 1939 / Kahane-Salem territory, in standard form.
Check both.
"""
import numpy as np

print("(1) the free floor: min F_K on the octave window, and L + Err >= 0")
print(f"{'K':>4} {'min F_K on W':>15} {'L + Err = 2^(K+1) sum':>24} {'A_K':>10}")
for K in (8, 12, 16, 20):
    L = max(1, int(round(1.5 ** K))); k0 = L
    k = np.arange(k0, k0 + L, dtype=float)
    F = np.ones_like(k)
    for i in range(K + 1):
        F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
    A = (2.0 ** (K + 1)) * F.sum() / L
    print(f"{K:>4} {F.min():>15.3e} {(2.0**(K+1))*F.sum():>24.6f} {A:>10.6f}")
print("  min F_K is positive at every K, so the floor needs nothing but F_K >= 0.")

print()
print("(2) the discrete A_K against the continuum Riesz-product integral")
print(f"{'K':>4} {'A_K (discrete)':>16} {'integral (continuum)':>22} {'difference':>13}")
for K in (4, 8, 12, 16, 20, 22):
    L = max(1, int(round(1.5 ** K))); k0 = L
    k = np.arange(k0, k0 + L, dtype=float)
    F = np.ones_like(k)
    for i in range(K + 1):
        F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
    A = (2.0 ** (K + 1)) * F.sum() / L
    N = 1 << 22
    x = 1.0 + (np.arange(N) + 0.5) / N
    P = np.ones_like(x)
    for m in range(K + 1):
        P *= 1.0 + np.cos(2 * np.pi * x * (1.5 ** m) / 3.0)
    I = float(P.mean())
    print(f"{K:>4} {A:>16.8f} {I:>22.8f} {A - I:>13.2e}")
