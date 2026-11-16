"""The last step of the 2026 proof of Sendov's conjecture, evaluated directly.

A counterexample of degree n >= 6 with distinguished zero a in (0, 1) gives (Tao's exposition, Propositions 10
and 11, as quoted in arXiv 2609.04246, Section 2) numbers alpha = (n-1)(1-a^2)/2 in (0, 17] and eta with
    0 < eta < min(alpha/(alpha+3), 1 - log(alpha)/alpha)                                   (polar inequality)
    1 <= F(eta, alpha, n)                                                                 (origin inequality)
    F = eta/(2 alpha (1-eta)) + eta/(4 alpha) + 1/(2(n-1)) + eta/(4 alpha (n-1))
        + (1 - 2 alpha/(n-1))^2 n(n-1)(n-2) eta/(4 alpha) * int_0^1 t^3 beta(t)^((n-4)/2) dt,
    beta(t) = 1 - 2 (1 - alpha/(n-1) - eta/2) t + (1 - 2 alpha/(n-1)) t^2.
The proof ends by showing F < 1 on the whole admissible set.  This script does not use the slab certificate
of 2609.04246: it evaluates F on a grid.

Part 1  sup of F over alpha in (0, 17], eta in (0, eta_max(alpha)], n = 6..N1 (all n), with eta on a grid;
        where the sup sits, and whether F increases with eta everywhere on the grid.
Part 2  F at eta = eta_max for larger n (sparse), to see the decay in n.
Part 3  a finer grid around the maximiser found in Part 1.
"""
import math
import sys

import numpy as np

T, W = np.polynomial.legendre.leggauss(160)
T = 0.5 * (T + 1.0)
W = 0.5 * W


def eta_max(alpha):
    return np.minimum(alpha / (alpha + 3.0), 1.0 - np.log(alpha) / alpha)


def F(eta, alpha, n):
    """eta, alpha arrays of the same shape; n integer."""
    m = n - 1.0
    A = 1.0 - 2.0 * alpha / m
    c = 1.0 - alpha / m - eta / 2.0
    beta = 1.0 - 2.0 * c[..., None] * T + A[..., None] * T * T
    assert (beta > 0).all()
    integ = (W * T ** 3 * beta ** ((n - 4) / 2.0)).sum(axis=-1)
    return (eta / (2 * alpha * (1 - eta)) + eta / (4 * alpha) + 1 / (2 * m) + eta / (4 * alpha * m)
            + A * A * n * m * (n - 2) * eta / (4 * alpha) * integ)


def main():
    N1 = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    da = 0.01
    alphas_all = np.arange(da, 17.0 + da / 2, da)
    fr = np.linspace(0.02, 1.0, 50)
    best = (-1.0, None)
    nonmono = 0
    cells = 0
    per_n = {}
    for n in range(6, N1 + 1):
        al = alphas_all[alphas_all < (n - 1) / 2.0]          # a^2 = 1 - 2 alpha/(n-1) > 0
        em = eta_max(al)
        ok = em > 0
        al, em = al[ok], em[ok]
        eta = em[:, None] * fr[None, :]
        a2 = np.broadcast_to(al[:, None], eta.shape)
        v = F(eta, a2, n)
        cells += v.size
        nonmono += int((np.diff(v, axis=1) < -1e-12).sum())
        i, j = np.unravel_index(np.argmax(v), v.shape)
        per_n[n] = (float(v[i, j]), float(al[i]), float(fr[j]))
        if v[i, j] > best[0]:
            best = (float(v[i, j]), (n, float(al[i]), float(eta[i, j]), float(fr[j])))
    print("Part 1: n = 6..%d, alpha step %.2f, 50 values of eta per alpha: %d grid points" % (N1, da, cells), flush=True)
    print("  sup F = %.6f at n = %d, alpha = %.2f, eta = %.5f (%.2f of the polar bound)" % (best[0], best[1][0], best[1][1], best[1][2], best[1][3]), flush=True)
    print("  grid steps in eta where F decreases: %d" % nonmono, flush=True)
    for n in (6, 7, 8, 10, 12, 16, 20, 30, 36, 40, 50, 80, 120, 200, 400):
        if n in per_n:
            print("  n = %3d: max F = %.6f at alpha = %.2f, eta fraction %.2f" % ((n,) + per_n[n]), flush=True)
    assert best[0] < 1.0
    assert nonmono == 0

    print("Part 2: eta at the polar bound, larger n", flush=True)
    worst2 = 0.0
    for n in (500, 700, 1000, 2000, 5000, 10000, 100000, 1000000):
        al = alphas_all
        em = eta_max(al)
        v = F(em, al, n)
        i = int(np.argmax(v))
        worst2 = max(worst2, float(v[i]))
        print("  n = %7d: max F = %.6f at alpha = %.2f" % (n, v[i], al[i]), flush=True)
    assert worst2 < 1.0

    n0, a0 = best[1][0], best[1][1]
    print("Part 3: fine grid near the maximiser (alpha step 0.0005), n = %d..%d" % (max(6, n0 - 3), n0 + 3), flush=True)
    fine = (-1.0, None)
    for n in range(max(6, n0 - 3), n0 + 4):
        al = np.arange(max(0.0005, a0 - 0.5), min(17.0, a0 + 0.5) + 1e-9, 0.0005)
        al = al[al < (n - 1) / 2.0]
        v = F(eta_max(al), al, n)
        i = int(np.argmax(v))
        print("  n = %3d: max F = %.7f at alpha = %.4f" % (n, v[i], al[i]), flush=True)
        if v[i] > fine[0]:
            fine = (float(v[i]), n, float(al[i]))
    print("  sup F on the fine grid = %.7f (n = %d, alpha = %.4f); the bound proved in arXiv 2609.04246 is 0.966537" % fine, flush=True)
    assert fine[0] < 0.966537
    print("all assertions passed")


if __name__ == "__main__":
    main()
