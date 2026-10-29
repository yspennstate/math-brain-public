"""Independent check of cert_t3_arb.py (agent B), T353 at T = 3, s = 1, eps = 1/2, by agent A.
Built from the mechanism, not from their code: n = 3b records, record i holds u (x) or bottom (x'), the rest hold w;
query answers psi_t(u), psi_t(w) in {-1, 1}; batch t's noisy sum minus b psi_t(w) is N(mu_t, 1) with
mu_t = psi_t(u) - psi_t(w) under x and -psi_t(w) under x' when i is in batch t, and 0 otherwise; i is in each batch w.p. 1/3.
Step 1 (-1, 1); step 2 ANTI (1, -1); step 3 ANTI (1, -1) or SAME (1, 1) as a function of (g1, g2).
Checks: (1) D with all-ANTI equals D(P_S || Q_S) by a brute 3-D grid; (2) the inner difference I3_SAME - I3_ANTI at the
crosscheck points, by direct quadrature in g3 (no root formula); (3) the gain int_B (I3_SAME - I3_ANTI) over
B = [-0.1, 0.3] x [2.2, 2.3] by Gauss-Legendre in (g1, g2), against their rigorous lower bound 2.25346e-5;
(4) min over a fine grid of B of the inner difference, against their min lower end 9.91e-8."""
import numpy as np
E = np.exp(0.5)
phi = lambda x: np.exp(-x * x / 2) / np.sqrt(2 * np.pi)
z = np.linspace(-14, 14, 280001); hz = z[1] - z[0]
wz = np.full(z.size, hz); wz[0] = wz[-1] = hz / 2


def means(step3):
    """(mu under x, mu under x') for the three batches, given step-3 answers."""
    ans = [(-1, 1), (1, -1), step3]
    return [(pu - pw, -pw) for pu, pw in ans]


def I3(g1, g2, step3):
    mu = means(step3)
    # batch holding i is t: coordinate t ~ N(mu_t), the others N(0)
    p = sum(phi(g1 - (mu[0][0] if t == 0 else 0)) * phi(g2 - (mu[1][0] if t == 1 else 0)) * phi(z - (mu[2][0] if t == 2 else 0)) for t in range(3)) / 3
    q = sum(phi(g1 - (mu[0][1] if t == 0 else 0)) * phi(g2 - (mu[1][1] if t == 1 else 0)) * phi(z - (mu[2][1] if t == 2 else 0)) for t in range(3)) / 3
    return (np.maximum(p - E * q, 0) * wz).sum()


ANTI, SAME = (1, -1), (1, 1)
d = lambda a, b: I3(a, b, SAME) - I3(a, b, ANTI)
print("(2) inner difference by direct quadrature (theirs in cert_t3_crosscheck.txt):")
for a, b, th in ((0.1, 2.2, 0.001775603045), (-0.5, 2.4, 0.0004490015957), (0.0, 1.8, -0.002139201887), (0.1, 2.25, 0.001535260930)):
    v = d(a, b); print(f"   ({a}, {b}): {v:+.10f}   theirs {th:+.10f}   diff {v - th:+.1e}")
# (1) D(P_S || Q_S) at T = 3 by integrating I3_ANTI over (g1, g2) on a Gauss-Hermite-free plain grid
g = np.linspace(-9, 11, 401); hg = g[1] - g[0]; wg = np.full(g.size, hg); wg[0] = wg[-1] = hg / 2
# separable speed-up: for fixed g1, I3 needs the g3 integral; do a coarse 2-D trapezoid (401^2 x 280k too big) -> use 161^2 on [-7, 9]
g = np.linspace(-7, 9, 161); hg = g[1] - g[0]; wg = np.full(g.size, hg); wg[0] = wg[-1] = hg / 2
z = np.linspace(-9, 11, 20001); hz = z[1] - z[0]; wz = np.full(z.size, hz); wz[0] = wz[-1] = hz / 2
Dg = sum(wg[i] * wg[j] * I3(g[i], g[j], ANTI) for i in range(g.size) for j in range(g.size))
print(f"(1) D(all ANTI) on a 161^2 x 20001 grid: {Dg:.6f}   (their t3_dp N=121: 0.207611, MC 0.207652 +- 0.000143)")
z = np.linspace(-14, 14, 280001); hz = z[1] - z[0]; wz = np.full(z.size, hz); wz[0] = wz[-1] = hz / 2
# (3) gain over B by 12 x 6 Gauss-Legendre
x1, w1 = np.polynomial.legendre.leggauss(12); x2, w2 = np.polynomial.legendre.leggauss(6)
a1, b1, a2, b2 = -0.1, 0.3, 2.2, 2.3
G = sum(w1[i] * w2[j] * d((a1 + b1) / 2 + (b1 - a1) / 2 * x1[i], (a2 + b2) / 2 + (b2 - a2) / 2 * x2[j]) for i in range(12) for j in range(6)) * (b1 - a1) / 2 * (b2 - a2) / 2
print(f"(3) int_B (I3_SAME - I3_ANTI) = {G:.6e}   (their rigorous lower bound 2.25346e-5)")
# (4) min over a 41 x 11 grid of B (corners included)
vals = np.array([[d(u, v) for v in np.linspace(a2, b2, 11)] for u in np.linspace(a1, b1, 41)])
k = np.unravel_index(vals.argmin(), vals.shape)
print(f"(4) min of the inner difference on a 41 x 11 grid of B: {vals.min():.4e} at g1 = {np.linspace(a1, b1, 41)[k[0]]:.3f}, g2 = {np.linspace(a2, b2, 11)[k[1]]:.3f}; max {vals.max():.4e}")
