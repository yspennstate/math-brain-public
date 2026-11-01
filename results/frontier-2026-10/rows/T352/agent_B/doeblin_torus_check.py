# T352 (agent B, 19 Oct 2026). Numerical check of the Doeblin plateau on the circle R/DZ.
# Noisy GD x <- x - eta grad F_S(x) + N(0, s^2) mod D, last iterate released, x0 = 0. F_S = (1/n) sum_i l_i with
# l_i(x) = A cos(2 pi x / D) (a double well on the circle), the neighbour flips record 1: l_1 -> -l_1. Per-example
# gradient bound K = 2 pi A / D, so |grad F_S - grad F_S'| <= 2K/n. Densities on an N-point grid (Nystrom: periodic
# trapezoid rule is spectrally accurate). Prints D_2 = log(1 + chi2) of the two last-iterate laws, the bound of the
# theorem in NOTE.md (chi2 <= w u / m with u <= beta min(T, 1/gamma), w <= (M-m)/2 u + beta_inf), and n^2 D_2.
import sys, json, numpy as np
D, s, eta, A = (float(x) for x in sys.argv[1:5]); N = int(sys.argv[5]); T = int(sys.argv[6])
x = np.arange(N) * D / N; h = D / N
def wrapped(z):
    z = np.mod(z + D / 2, D) - D / 2
    return sum(np.exp(-(z + j * D) ** 2 / (2 * s * s)) for j in range(-6, 7)) / (s * np.sqrt(2 * np.pi))
kk = wrapped(np.linspace(-D / 2, D / 2, 20001)); m, M = kk.min(), kk.max(); gamma = m * D
zz = np.linspace(-D / 2, D / 2, 200001); dk = np.abs(np.gradient(wrapped(zz), zz)).max()
K = 2 * np.pi * A / D
CK = [t for t in (10, 100, 1000, 3000, 10000, 30000) if t < T] + [T]
def grad(xx, n, flip):
    g1 = -A * 2 * np.pi / D * np.sin(2 * np.pi * xx / D)
    return g1 if not flip else g1 * (n - 2) / n          # n-1 copies of l plus one -l, averaged
out = {}
for n in [int(v) for v in sys.argv[7].split(",")]:
    laws = []
    for flip in (False, True):
        phi = x - eta * grad(x, n, flip)
        P = wrapped(x[None, :] - phi[:, None]) * h        # P[i, j] = mass from grid point i to j
        f = wrapped(x - (0 - eta * grad(np.array([0.0]), n, flip)[0]))   # law after step 1 (density)
        hist = []
        for t in range(2, T + 1):
            f = (f * 1.0) @ P / h * h if False else f @ P
            if t in CK: hist.append(f.copy())
        laws.append(hist)
    rows = []
    for (f, g), t in zip(zip(*laws), CK):
        chi2 = np.sum((f - g) ** 2 / g) * h; u = np.sum(np.abs(f - g)) * h; w = np.abs(f - g).max()
        sens = 2 * eta * K / n; beta = sens * np.sqrt(2 / np.pi) / s; binf = sens * dk
        ub = beta * min(t, 1 / gamma); wb = (M - m) / 2 * ub + binf
        rows.append(dict(t=t, D2=float(np.log1p(chi2)), u=float(u), w=float(w), chi2_bound=float(wb * ub / m),
                         n2D2=float(n * n * np.log1p(chi2))))
        print("n %7d t %5d  D2 %.4e  n^2 D2 %.5f  |  u %.3e (<= %.3e)  w %.3e (<= %.3e)  chi2 bound %.3e" %
              (n, t, np.log1p(chi2), n * n * np.log1p(chi2), u, ub, w, wb, wb * ub / m), flush=True)
    out[n] = rows
print("m %.4g M %.4g gamma %.4g ||k'||_inf %.4g K %.4g" % (m, M, gamma, dk, K))
json.dump(dict(args=sys.argv[1:], m=m, M=M, gamma=gamma, rows=out), open(sys.argv[8] if len(sys.argv) > 8 else "doeblin_torus_check.json", "w"), indent=1)
