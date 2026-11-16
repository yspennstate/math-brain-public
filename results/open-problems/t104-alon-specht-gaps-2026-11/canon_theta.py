"""Three-valued vectors x = (alpha, beta, gamma, ..., gamma) in Reduction R (HOOKS_AND_TWO_ROWS.md section 5).

The unit sum-zero vectors of this shape form a circle x(phi) = cos(phi) s + sin(phi) u, with
s = (n-1, -1, ..., -1)/sqrt(n(n-1)) the star vector and u = (0, n-2, -1, ..., -1)/sqrt((n-1)(n-2)).
{1, x}^perp is spanned by v = x(phi + pi/2) and the block B of sum-zero vectors on the last n-2 coordinates.
By symmetry in the last n-2 coordinates and concavity of the smallest slack, the best covariance is
    C(theta) = theta v v^t + (1 - theta) Pi_B/(n-3),   0 <= theta <= 1,
and (*) is affine in theta for each of the four pair types.  The script prints, along the circle, the interval of
theta for which all four are >= 0, and the theta that maximises the smallest one.
usage: canon_theta.py n steps
"""
import sys
import numpy as np


def star_matrix(x, C):
    n = len(x)
    dg = np.diag(C)
    kappa = float((x * x * dg).sum())
    d2 = (x[:, None] - x[None, :]) ** 2
    cij = dg[:, None] + dg[None, :] - 2 * C
    gij = (x * x * dg)[:, None] + (x * x * dg)[None, :] - 2 * np.outer(x, x) * C
    return (2 - d2) + (2 * n * kappa / (n - 2.0)) * ((n - 1) * d2 - 2) - 2 * n * gij - (n - 2) * (2 * d2 - 1) * cij


def main():
    n, steps = int(sys.argv[1]), int(sys.argv[2])
    m = n - 2
    s = np.array([n - 1.0] + [-1.0] * (n - 1)) / np.sqrt(n * (n - 1.0))
    u = np.array([0.0, m] + [-1.0] * m) / np.sqrt((m + 1.0) * m)
    PB = np.zeros((n, n))
    PB[2:, 2:] = np.eye(m) - 1.0 / m
    CB = PB / (m - 1.0)
    types = [(0, 1), (0, 2), (1, 2), (2, 3)]
    names = ["ab", "ag", "bg", "gg"]
    worst = (float("inf"), None)
    empty = 0
    print("n=%d   phi/pi   alpha    beta   gamma | theta interval      | best theta, smallest (*) there, tight types" % n)
    for k in range(steps + 1):
        phi = np.pi * k / steps
        x = np.cos(phi) * s + np.sin(phi) * u
        v = -np.sin(phi) * s + np.cos(phi) * u
        S0 = star_matrix(x, CB)
        S1 = star_matrix(x, np.outer(v, v))
        a = np.array([S0[t] for t in types])
        b = np.array([S1[t] - S0[t] for t in types])
        lo, hi = 0.0, 1.0
        for ai, bi in zip(a, b):
            if abs(bi) < 1e-13:
                if ai < -1e-12:
                    lo, hi = 1.0, 0.0
            elif bi > 0:
                lo = max(lo, -ai / bi)
            else:
                hi = min(hi, -ai / bi)
        th = np.linspace(0, 1, 20001)
        vals = (a[:, None] + b[:, None] * th[None, :]).min(axis=0)
        j = int(vals.argmax())
        tight = [names[i] for i in range(4) if a[i] + b[i] * th[j] - vals[j] < 1e-6]
        if hi < lo - 1e-9:
            empty += 1
        if vals[j] < worst[0]:
            worst = (float(vals[j]), phi / np.pi)
        if k % max(1, steps // 48) == 0:
            print("       %.4f  %7.4f %7.4f %7.4f | [%.5f, %.5f] %s | %.5f  %9.6f  %s"
                  % (phi / np.pi, x[0], x[1], x[2], lo, hi, "EMPTY" if hi < lo - 1e-9 else "     ",
                     th[j], vals[j], ",".join(tight)))
    print("n=%d: %d of %d points with no feasible theta; smallest best value %.3e at phi/pi = %.4f"
          % (n, empty, steps + 1, worst[0], worst[1]))


if __name__ == "__main__":
    main()
