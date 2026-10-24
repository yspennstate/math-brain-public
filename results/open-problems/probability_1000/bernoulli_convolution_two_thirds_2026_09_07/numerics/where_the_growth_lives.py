"""Two audits of the fixed-point explanation.

(a) GRID DEPENDENCE of nu(octave): a real singular concentration shrinks as N grows; a discretisation
    artefact stays put. Also nu near 0 versus N.
(b) THE DIRECT DECOMPOSITION, no operator at all: if the global growth (4/3)^K is the neighbourhood of
    the fixed point theta = 0, then a point with theta ~ (2/3)^K keeps its first K iterates near 0,
    collects phi ~ log 2 each step, so e^(S_K phi) ~ 2^K on a set of measure ~(2/3)^K - product (4/3)^K.
    Test it: split int_0^1 e^(S_K phi) at delta = (2/3)^K and at a few fixed cuts, and see which piece
    carries the growth. Closed-form orbit (never iterate the map).
"""
import numpy as np

def S(theta, K):
    """sum_(m=0..K) log(1 + cos 2 pi theta_m), theta_m = theta (3/2)^m mod 1, closed form."""
    out = np.zeros_like(theta)
    for m in range(K + 1):
        t = np.mod(theta * (1.5 ** m), 1.0)
        out += np.log(np.maximum(1.0 + np.cos(2 * np.pi * t), 1e-300))
    return out

print("(a) grid dependence of the leading eigenMEASURE")
print(f"{'N':>8} {'nu(octave)':>14} {'nu[0,1/3]':>12} {'nu[2/3,1]':>12} {'nu[0,0.001]':>13}")
for p in (11, 12, 13, 14):
    N = 1 << p
    y = (np.arange(N) + 0.5) / N
    x0 = 2*y/3.0; x1 = 2*(y+1)/3.0
    w0 = 1.0 + np.cos(2*np.pi*x0)
    w1 = np.where(y < 0.5, 1.0 + np.cos(2*np.pi*x1), 0.0)
    i0 = np.minimum((x0*N).astype(int), N-1); i1 = np.minimum((x1*N).astype(int), N-1)
    v = np.ones(N)
    for _ in range(300):
        nv = np.zeros(N)
        np.add.at(nv, i0, (2.0/3.0)*w0*v)
        np.add.at(nv, i1, (2.0/3.0)*w1*v)
        v = nv / max(nv.sum(), 1e-300)
    m = lambda lo, hi: float(v[(y >= lo) & (y < hi)].sum())
    print(f"{N:>8} {m(1/3,2/3):>14.8f} {m(0,1/3):>12.6f} {m(2/3,1):>12.6f} {m(0,0.001):>13.6f}")

print()
print("(b) where the growth of int_0^1 e^(S_K phi) actually lives (adaptive quadrature near 0)")
print(f"{'K':>4} {'total':>12} {'(4/3)^K':>12} {'tot/(4/3)^K':>12} {'frac [0,(2/3)^K]':>17} {'frac [0,0.01]':>14} {'frac octave':>12}")
for K in (6, 8, 10, 12, 14, 16, 18):
    # graded mesh: dense near 0 where the integrand spikes, uniform elsewhere
    edges = np.concatenate([np.geomspace(1e-12, 1e-2, 4000), np.linspace(1e-2, 1.0, 200000)])
    mid = 0.5*(edges[:-1] + edges[1:]); wid = np.diff(edges)
    val = np.exp(S(mid, K)) * wid
    tot = val.sum()
    d = (2.0/3.0)**K
    f_d   = val[mid < d].sum() / tot
    f_1e2 = val[mid < 1e-2].sum() / tot
    f_oct = val[(mid >= 1/3) & (mid < 2/3)].sum() / tot
    print(f"{K:>4} {tot:>12.6f} {(4/3)**K:>12.4f} {tot/(4/3)**K:>12.6f} {f_d:>17.6f} {f_1e2:>14.6f} {f_oct:>12.3e}")
