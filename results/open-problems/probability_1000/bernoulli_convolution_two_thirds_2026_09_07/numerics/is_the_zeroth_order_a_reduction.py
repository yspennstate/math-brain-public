"""Is the exact-zero mechanism a REDUCTION, or an elegant restatement? Check the algebra.

sum_eps c_eps e(k nu_eps / P) = prod_i (1 + cos(2 pi k n_i / P)) = 2^(K+1) prod_i cos^2(pi k n_i / P)
                              = 2^(K+1) F_K(k),
since 1 + cos(2 pi t) = 2 cos^2(pi t).  So the character sum at ANY k is just 2^(K+1) F_K(k).

Consequences:
 (a) the zeroth-order term, sum_eps c_eps e(theta_eps) * L = L * 2^(K+1) F_K(k0), is exactly 0 because
     F_K(R) = 0 - that is the mechanism, and it is exact;
 (b) but L + Err = sum_eps c_eps e(theta_eps) G(nu_eps) = 2^(K+1) sum_{k in W} F_K(k) identically,
     so A_K = (L + Err)/L IS the normalised window sum itself.
So the identity explains the SIZE of the cancellation (the main term L is annihilated because the window
begins at a zero) without reducing the quantity that must be bounded: A_K is the original object.
Verify (b) numerically, since it is the load-bearing half.
"""
import numpy as np

print(f"{'K':>4} {'A_K via window sum':>20} {'A_K via characters':>20} {'2^(K+1) F_K(k0)':>18}")
for K in (6, 8, 10, 12):
    P = 3 ** (K + 1)
    L = max(1, int(round(1.5 ** K))); k0 = L
    k = np.arange(k0, k0 + L, dtype=float)
    F = np.ones_like(k)
    for i in range(K + 1):
        F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
    A_window = (2.0 ** (K + 1)) * F.sum() / L

    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64); c = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c = np.concatenate([c * 0.5, c, c * 0.5])
    v = nu.astype(float)
    z = np.exp(2j * np.pi * v / P)
    den = 1.0 - z
    G = np.where(np.abs(den) < 1e-12, complex(L), (1.0 - np.exp(2j * np.pi * L * v / P)) / den)
    A_char = float(np.real((c * np.exp(2j * np.pi * k0 * v / P) * G).sum())) / L

    # the zeroth-order piece
    F0 = 1.0
    for i in range(K + 1):
        F0 *= np.cos(np.pi * k0 * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
    print(f"{K:>4} {A_window:>20.8f} {A_char:>20.8f} {(2.0**(K+1))*F0:>18.3e}")
print()
print("Identical columns confirm (b): the character route and the window sum are the same object,")
print("so the mechanism explains the cancellation without shrinking what has to be bounded.")
