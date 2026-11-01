"""Same model as check_t2.py, on a vectorised (g1, g2) grid (trapezoid; spacing h from argv). Prints D(P_S||Q_S), D(Q_S||P_S), the
ANTI total, the pointwise-best total over psi_2 in a 9x9 grid of [-1,1]^2 (and over the two named policies), and where SAME wins."""
import numpy as np, sys
s, eps = 1.0, 0.5; E = np.exp(eps); h = float(sys.argv[1]) if len(sys.argv) > 1 else 0.01
g = np.arange(-10, 12 + h / 2, h); w = np.full(len(g), h); w[[0, -1]] /= 2
phi = lambda x, m: np.exp(-0.5 * ((x - m) / s) ** 2) / (s * np.sqrt(2 * np.pi))
G1, G2 = g[:, None], g[None, :]
P = 0.5 * (phi(G1, 2) * phi(G2, 0) + phi(G1, 0) * phi(G2, 2)); Q = 0.5 * (phi(G1, 1) * phi(G2, 0) + phi(G1, 0) * phi(G2, 1))
D = lambda A, B: float(w @ np.maximum(A - E * B, 0) @ w)
print(f"h={h}  D(P_S||Q_S)={D(P, Q):.6f}  D(Q_S||P_S)={D(Q, P):.6f}", flush=True)
m, mp = -2.0, -1.0
A1 = 0.5 * phi(g, m)[:, None] * phi(g, 0)[None, :]; B1 = 0.5 * phi(g, mp)[:, None] * phi(g, 0)[None, :]; A0 = 0.5 * phi(g, 0)[:, None]
def I(a, c):  # inner integral over g2, as a function of g1
    return np.maximum(A1 + A0 * phi(G2, a) - E * (B1 + A0 * phi(G2, c)), 0) @ w
ia, isame = I(2, 1), I(0, -1)
best = np.maximum(ia, isame)
for pu in np.linspace(-1, 1, 9):
    for pw in np.linspace(-1, 1, 9):
        best = np.maximum(best, I(pu - pw, -pw))
win = g[isame > ia]
print(f"ANTI total={w @ ia:.6f}  max(ANTI,SAME) total={w @ np.maximum(ia, isame):.6f}  best-over-grid total={w @ best:.6f}", flush=True)
print(f"SAME beats ANTI on g1 in [{win.min():.3f}, {win.max():.3f}]  (" + ", ".join(f"g1={x}: {isame[np.argmin(abs(g-x))]-ia[np.argmin(abs(g-x))]:+.3e}" for x in (-3.0, -2.5, -2.0)) + ")")
# reverse order of the same adaptive method, for completeness
