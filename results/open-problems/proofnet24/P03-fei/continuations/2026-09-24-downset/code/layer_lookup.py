"""The layer-lookup function: majority whose ties are resolved by fresh bits.

f(y, z) = Maj_n(y) OR OR_{y* in L} (z_{y*} AND [y = y*]), n odd, L = the points of weight (n-1)/2, one fresh
z_{y*} per point (monotone). With A = (1 - 2 Maj_n) - 1_L (values 1, 0, -1),
    F = 1 - 2f = A + sum_{y* in L} delta_{y*}(y) chi_{z_{y*}},
so Fhat(T) = Ahat(T) for T in the y-coordinates, Fhat(T + z_{y*}) = 2^-n chi_T(y*), and every other coefficient is 0.
A is symmetric: 2^n Ahat(T) = N_t - K_{(n-1)/2}(t; n), N_t the majority sums, K the Krawtchouk polynomial.

Printed: H/I; the averaged half-moment sum_v sum_{T not v} |Fhat(T) Fhat(T+v)| / I restricted to the z coordinates
(its z-part alone already exceeds any constant times I); and the z-part of sum_v B_v / I. Exact integers, mpmath logs.
"""
import math
import sys
import functools
import mpmath as mp

sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from log_sharp import threshold_coeffs  # noqa: E402

print = functools.partial(print, flush=True)


def kraw(w, t, n):
    """sum over |y| = w of chi_T(y) for |T| = t."""
    return sum((-1) ** i * math.comb(t, i) * math.comb(n - t, w - i) for i in range(0, min(t, w) + 1) if w - i <= n - t)


def phi(p):
    return mp.mpf(0) if p == 0 else -p * mp.log(p, 2)


def run(n):
    mp.mp.prec = 3 * n + 128
    k = (n + 1) // 2
    N = threshold_coeffs(n, k)                 # 2^n * (1 - 2 Maj)^(T), |T| = t
    w = (n - 1) // 2
    nL = math.comb(n, w)
    two_n = mp.mpf(2) ** n
    Ahat = [mp.mpf(N[t] - kraw(w, t, n)) / two_n for t in range(n + 1)]
    # y-only part
    H_A = sum(math.comb(n, t) * phi(Ahat[t] ** 2) for t in range(n + 1))
    I_A = sum(math.comb(n, t) * t * Ahat[t] ** 2 for t in range(n + 1))
    # z part: 2^n sets T_y for each z, weight 4^-n each
    Pz = 1 / two_n ** 2
    H_z = nL * two_n * phi(Pz)
    I_z = nL * sum(math.comb(n, t) * (t + 1) for t in range(n + 1)) * Pz
    H = H_A + H_z
    I = I_A + I_z
    # half-moment at z: sum_{T_y} |Ahat(T_y)| 2^-n  (sets with other z's pair with two-z sets, weight 0)
    L1 = sum(math.comb(n, t) * abs(Ahat[t]) for t in range(n + 1))
    half_z = nL * L1 / two_n
    # erasure at z: pairs (T_y, T_y + z) with weights (Ahat^2, 4^-n); pairs (T_y + z', T_y + z' + z) have (4^-n, 0)
    Bz = mp.mpf(0)
    for t in range(n + 1):
        X = Ahat[t] ** 2
        Bz += math.comb(n, t) * (phi(X) + phi(Pz) - phi(X + Pz))
    Bz_tot = nL * Bz
    print(f"n={n:3d}: H/I = {float(H / I):.4f} (H_A/I_A = {float(H_A / I_A):.4f}, z-share of I = {float(I_z / I):.3f}); "
          f"z half-moment / I = {float(half_z / I):.4e}; z erasure / I = {float(Bz_tot / I):.4f}")


def brute(n):
    """Brute-force H, I and the summed erasure over the z coordinates (small n)."""
    import itertools
    import numpy as np
    from c1_refute import spectrum, ent
    w = (n - 1) // 2
    L = [y for y in itertools.product((0, 1), repeat=n) if sum(y) == w]
    nv = n + len(L)
    idx = np.arange(1 << nv)
    ybits = np.stack([(idx >> j) & 1 for j in range(n)], axis=1)
    maj = ybits.sum(axis=1) > n // 2
    f = maj.copy()
    for j, ys in enumerate(L):
        zj = (idx >> (n + j)) & 1
        f |= (zj == 1) & np.all(ybits == np.array(ys), axis=1)
    F = 1.0 - 2.0 * f
    P = spectrum(F)
    H = ent(P)
    pc = np.array([bin(t).count('1') for t in range(1 << nv)])
    I = float((P * pc).sum())
    B = 0.0
    for j in range(len(L)):
        v = n + j
        low = idx[((idx >> v) & 1) == 0]
        X = P[low]; Y = P[low | (1 << v)]
        def ph(p):
            q = np.where(p > 1e-300, p, 1.0)
            return np.where(p > 1e-300, -p * np.log2(q), 0.0)
        B += float((ph(X) + ph(Y) - ph(X + Y)).sum())
    print(f"brute n={n}: vars {nv}, H/I = {H / I:.4f}, z erasure / I = {B / I:.4f}")

if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]] or [7, 11, 15, 21, 31, 41, 61, 81, 101]:
        run(n)
