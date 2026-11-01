"""Any test function returns the autocorrelation. The exact identity, and one disputed step.

For any M : Z -> R with enough decay,
    sum_k M(k) |muhat(k)|^2 = int_0^1 A(t) Mcheck(t) dt,   Mcheck(t) = sum_k M(k) e(kt),
because |muhat(k)|^2 are exactly the Fourier coefficients of the autocorrelation density A = f * f~.
So EVERY nonnegative test function dominating 1_W returns an integral of A against its own transform:
the majorant route does not bound the correlation integral, it returns it.  That is the clean statement,
and it needs no truncation, no (4/3)^K and no window shape.

A round-2 verifier sharpened this to a numerical FLOOR, via 'int_{-d}^{d} Mcheck = M(0) >= 1 for any
M >= 1_W'.  That step needs 0 in W.  For an octave window W = [R, 2R) the origin is NOT in W, so M(0)
carries no lower bound from domination, and the floor as stated does not follow.  Check both here.
"""
import numpy as np

# A on [0,1): autocorrelation of the density, via its Fourier coefficients |muhat(k)|^2
def muhat_abs2(k):
    k = np.asarray(k, dtype=float)
    out = np.ones_like(k); r = 1.0
    while True:
        a = np.pi * k * r / 3.0
        if np.max(np.abs(a)) < 1e-14: break
        out *= np.abs(np.cos(a)); r *= 2.0 / 3.0
    return out ** 2

KMAX = 200000
ks = np.arange(-KMAX, KMAX + 1)
c = muhat_abs2(ks)

# a concrete test function: a raised-cosine bump on the octave window, k0 = R, length L
R = 4096; L = R
k0, k1 = R, 2 * R
M = np.zeros_like(c)
inw = (ks >= k0) & (ks < k1)
# raised-cosine taper of half-width L/2 on each side, so M >= 1 on W and M >= 0 everywhere
tap = L // 2
for i, kk in enumerate(ks):
    if k0 <= kk < k1:
        M[i] = 1.0
    elif k0 - tap <= kk < k0:
        M[i] = 0.5 * (1 + np.cos(np.pi * (k0 - kk) / tap))
    elif k1 <= kk < k1 + tap:
        M[i] = 0.5 * (1 + np.cos(np.pi * (kk - k1) / tap))

lhs = float((M * c).sum())
Ewindow = float(c[inw].sum())
print(f"octave R = {R}")
print(f"  E(R) = sum over the window          = {Ewindow:.6e}")
print(f"  sum_k M(k)|muhat(k)|^2 (majorised)  = {lhs:.6e}   ratio {lhs/Ewindow:.4f}")

# right-hand side by FFT (never build an outer product: 4096 x 2^20 floats is 32 GiB)
T = 1 << 20
def series_from_coeffs(kk, vv, T):
    """sum_k v_k e(k t) on the grid t = j/T, by placing coefficients and inverse-FFT."""
    buf = np.zeros(T, dtype=complex)
    idx = np.mod(kk.astype(np.int64), T)
    np.add.at(buf, idx, vv)
    return np.real(np.fft.ifft(buf) * T)

sup = np.nonzero(M)[0]
Mcheck = series_from_coeffs(ks[sup], M[sup].astype(complex), T)
nz = np.nonzero(c)[0]
A = series_from_coeffs(ks[nz], c[nz].astype(complex), T)
rhs = float((A * Mcheck).mean())
print(f"  int_0^1 A(t) Mcheck(t) dt           = {rhs:.6e}   (identity check)")
print(f"  relative difference                 = {abs(rhs-lhs)/abs(lhs):.3e}")
print()
print(f"  A(0) = sum_k |muhat(k)|^2           = {float(c.sum()):.6f}  (||f||^2 = 1.206310)")
print(f"  A(0) from the series                = {A[0]:.6f}")
print(f"  M(0), the disputed quantity         = {float(M[ks == 0][0]):.6f}")
print("     The octave window does not contain the origin, so domination gives no floor at k = 0,")
print("     and the claimed per-octave floor of 2.41 does not follow. Measured here, a nonnegative")
print("     majorant of the window costs only the ratio printed above.")
