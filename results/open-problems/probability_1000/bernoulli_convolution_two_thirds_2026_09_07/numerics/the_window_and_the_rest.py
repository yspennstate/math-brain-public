"""Split int_0^1 e^(S_K phi) into the alignment window at 0 and everything else.

WINDOW  theta in [0, M (2/3)^K]: substitute theta = (2/3)^K u, so theta_m = u (2/3)^(K-m) and
        S_K phi = sum_(j=0..K) phi( (2/3)^j u mod 1 ). For large j the argument is near 0 and phi -> log 2,
        so the sum is K log 2 + a convergent correction: the window is EXACTLY (4/3)^K times
            c_M = int_0^M prod_(j>=0) [ (1 + cos(2 pi (2/3)^j u mod 1)) / 2 ] du,
        a K-free constant. Compute c_M and check it stabilises in M and in K.
REST    theta in [M (2/3)^K, 1]: if this is BOUNDED in K then all growth is the window, the leading
        eigenvalue 1.335 I measured by Ulam is a smeared atom, and the octave (which lives entirely in
        the rest) never had the (4/3)^K at all. Mesh resolves the fastest factor at ~150 points per
        oscillation, so the K=18 uptick can be told from quadrature failure.
"""
import numpy as np

def phi_sum(theta, K):
    out = np.zeros_like(theta)
    for m in range(K + 1):
        t = np.mod(theta * (1.5 ** m), 1.0)
        out += np.log(np.maximum(1.0 + np.cos(2 * np.pi * t), 1e-300))
    return out

M = 40.0
print(f"window constant c_M = int_0^M prod_j (1+cos 2 pi (2/3)^j u)/2 du,  M = {M:g}")
u = (np.arange(4_000_000) + 0.5) * (M / 4_000_000)
prod = np.ones_like(u)
for j in range(200):
    prod *= 0.5 * (1.0 + np.cos(2 * np.pi * np.mod((2.0/3.0) ** j * u, 1.0)))
    if j > 60 and prod.max() < 1e-300:
        break
c_M = prod.sum() * (M / 4_000_000)
print(f"  c_M = {c_M:.6f}   (K-free; the window is 2 c_M (4/3)^K after the +1 term)")
print()
print(f"{'K':>4} {'window':>14} {'window/(4/3)^K':>16} {'REST':>12} {'octave':>11} {'pts/osc':>9}")
for K in (8, 10, 12, 14, 16, 18, 20, 22, 24):
    d = M * (2.0/3.0) ** K
    # window by the substitution, K-free integrand
    uu = (np.arange(400_000) + 0.5) * (M / 400_000)
    pw = np.ones_like(uu)
    for j in range(K + 1):
        pw *= 0.5 * (1.0 + np.cos(2 * np.pi * np.mod((2.0/3.0) ** j * uu, 1.0)))
    window = (2.0 ** (K + 1)) * (2.0/3.0) ** K * pw.sum() * (M / 400_000)
    # rest, mesh at ~150 points per oscillation of the fastest factor
    freq = (1.5 ** K)
    npts = int(min(max(150.0 * freq, 200_000), 12_000_000))
    edges = np.linspace(d, 1.0, npts + 1)
    mid = 0.5 * (edges[:-1] + edges[1:])
    val = np.exp(phi_sum(mid, K)) * (1.0 - d) / npts
    rest = val.sum()
    oct_sel = (mid >= 1/3) & (mid < 2/3)
    print(f"{K:>4} {window:>14.6f} {window/(4/3)**K:>16.6f} {rest:>12.6f} {val[oct_sel].sum():>11.6f} {npts/freq:>9.0f}")
