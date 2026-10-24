"""Does the triangle inequality on Err already suffice?  No, and by an exponential margin.

Err = sum_{eps != 0} c_eps D(nu_eps),  c_eps = 2^-|supp eps|,  nu_eps = sum_i eps_i 2^i 3^(K-i),
D(nu) = sum_{k in W} e(k nu / P),  P = 3^(K+1),  W = [k0, k0+L) the octave with L = R = (3/2)^K.
Then |D(nu)| = |sin(pi L nu / P) / sin(pi nu / P)|.

The window sum is 2^-(K+1) (L + Err), and E(R) <= that.  So E(R) << R^-0.71 -- which is MORE than
enough for S < infinity -- as soon as |Err| = o(L).  The paper quotes absolute values 6.0 .. 129.5
for K = 4..12 against L = 5.06 .. 129.7, which LOOKS like the triangle inequality is about to win.
It is not: those are the CONSECUTIVE BLOCK only, which carries 1.23 pct of the weight at K = 12.
Summed over all 3^(K+1) patterns the absolute sum is exponentially larger than L.
"""
import numpy as np

for K in (4, 6, 8, 10):
    P = 3 ** (K + 1)
    R = (1.5) ** K
    L = max(1, int(round(R)))
    k0 = max(1, int(round(R)))
    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64); c = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c = np.concatenate([c * 0.5, c, c * 0.5])
    nz = nu != 0
    v, cc = nu[nz].astype(float), c[nz]
    s2 = np.sin(np.pi * v / P)
    D = np.where(np.abs(s2) < 1e-14, float(L), np.sin(np.pi * L * v / P) / s2)
    absS = float((cc * np.abs(D)).sum())
    # signed Err: sum c_eps D(nu_eps), real since the pattern set is symmetric
    signed = float((cc * D).sum())
    blk = np.abs(v) <= 2 ** (K + 1) - 1
    absblk = float((cc[blk] * np.abs(D[blk])).sum())
    print(f"K={K:>3}  L={L:>6}  P={P:>9}")
    print(f"      signed Err                       = {signed:>14.4f}   (bounded, this is the real one)")
    print(f"      triangle bound over ALL patterns = {absS:>14.4f}   = {absS/L:>10.1f} x L")
    print(f"      triangle bound over the block    = {absblk:>14.4f}   = {absblk/L:>10.4f} x L")
    print(f"      total weight 2^(K+1)             = {2**(K+1):>14}")
    print()

print("=" * 78)
print("Now with the PHASE kept, and checked against a direct sum of F_K over the window.")
print("D(nu) = e(k0 nu/P) (1 - e(L nu/P))/(1 - e(nu/P)); dropping the phase destroys the")
print("cancellation, which is where the whole difficulty lives.")
print()
for K in (4, 6, 8, 10):
    P = 3 ** (K + 1)
    R = 1.5 ** K
    L = max(1, int(round(R)))
    k0 = max(1, int(round(R)))
    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64); c = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c = np.concatenate([c * 0.5, c, c * 0.5])
    nz = nu != 0
    v, cc = nu[nz].astype(float), c[nz]
    z = np.exp(2j * np.pi * v / P)
    zL = np.exp(2j * np.pi * L * v / P)
    z0 = np.exp(2j * np.pi * k0 * v / P)
    den = 1.0 - z
    D = np.where(np.abs(den) < 1e-12, complex(L), z0 * (1.0 - zL) / den)
    Err = float(np.real((cc * D).sum()))

    k = np.arange(k0, k0 + L, dtype=float)
    F = np.ones_like(k)
    for i in range(K + 1):
        F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
    direct = float(F.sum())
    print(f"K={K:>3} L={L:>5}: direct sum_(k in W) F_K(k) = {direct:.8f}")
    print(f"          2^-(K+1) (L + Err) with Err = {Err:>12.5f}  gives {(L+Err)/2**(K+1):.8f}")
    print(f"          Err / L = {Err/L:+.4f}")
