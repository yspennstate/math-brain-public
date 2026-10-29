"""Independent check of the transposition identity in agent_B/NOTE.md 'Uniform in beta1' (agent C, 20 Oct 2026).
One epoch of n slots, all n! orders enumerated, other epochs as an independent two-point offset c. For arbitrary weights w, a:
    sum_q w_q E[b_pi(q) F(eta)] = (1/4n) sum_{q,r} (w_q - w_r)(a_q - a_r) E[Db DZ int_0^1 F'(eta - t (a_q - a_r) DZ) dt],
eta = c + sum_q a_q Z_pi(q), F(e) = psi(1 + e) - 1 - psi'(1) e. Then step 3: max_{q,r} |E[Db DZ int F']| / d over d."""
import itertools
import math

import numpy as np


def psi_fns(eps, sq):
    psi = lambda y: (sq + eps) / (sq * np.sqrt(y) + eps)
    dpsi = lambda y: -(sq + eps) * sq / (2 * np.sqrt(y) * (sq * np.sqrt(y) + eps) ** 2)
    return psi, dpsi


def run(bvals, x, n, b1, b2, eps, cs=0.0, wmode="mom"):
    g = x + bvals
    V = np.mean(g ** 2)
    Z = g ** 2 - V
    b = bvals - bvals.mean()
    d = 1 - b2
    lag = np.arange(n)[::-1]  # slot q = n-1 is the newest
    w = (1 - b1) * b1 ** lag if wmode == "mom" else np.random.default_rng(1).random(n)
    a = (d / V) * b2 ** lag if wmode == "mom" else np.random.default_rng(2).random(n) * d / V
    psi, dpsi = psi_fns(eps, math.sqrt(V))
    p1 = float(dpsi(1.0))
    F = lambda e: psi(1 + e) - 1 - p1 * e
    Fp = lambda e: dpsi(1 + e) - p1
    tg, tw = np.polynomial.legendre.leggauss(20)
    tg, tw = 0.5 * (tg + 1), 0.5 * tw
    perms = np.array(list(itertools.permutations(range(n))))
    eta0 = (a[None, :] * Z[perms]).sum(1)
    lhs = 0.0
    rhs = 0.0
    E = np.zeros((n, n))
    for c, pc in ((cs, 0.5), (-cs, 0.5)):
        eta = eta0 + c
        lhs += pc * np.mean((w[None, :] * b[perms]).sum(1) * F(eta))
        for q in range(n):
            for r in range(n):
                if q == r:
                    continue
                Db = b[perms[:, q]] - b[perms[:, r]]
                DZ = Z[perms[:, q]] - Z[perms[:, r]]
                da = a[q] - a[r]
                integ = sum(wt * Fp(eta - t * da * DZ) for t, wt in zip(tg, tw))
                E[q, r] += pc * np.mean(Db * DZ * integ)
    for q in range(n):
        for r in range(n):
            rhs += (w[q] - w[r]) * (a[q] - a[r]) * E[q, r] / (4 * n)
    S = sum((w[q] - w[r]) * (a[q] - a[r]) for q in range(n) for r in range(n)) / n
    return lhs, rhs, S, np.abs(E).max() / d, d


bv = {5: np.array([6.0, 2.0, -1, -1, -1]), 6: np.array([6.0, 2.0, -1, -1, -1, -1]), 7: np.array([6.0, 2.0, -1, -1, -1, -1, -1])}
print("identity, arbitrary (non-comonotone) weights, eps 0 and 1:")
for n in (5, 6, 7):
    for eps in (0.0, 1.0):
        L, R, S, M, d = run(bv[n], 0.01, n, 0, 0.9, eps, cs=0.05, wmode="rand")
        print("  n %d eps %g: lhs %+.15e rhs %+.15e rel diff %.1e" % (n, eps, L, R, abs(L - R) / abs(L)))
print("step 3: max_{q,r} |E[Db DZ int F']| / d, momentum weights, n 6, eps 0:")
for b1 in (0.0, 0.9, 0.999):
    row = []
    for b2 in (0.9, 0.99, 0.999, 0.9999):
        L, R, S, M, d = run(bv[6], 0.0, 6, b1, b2, 0.0, cs=0.0)
        row.append("d %g: %.4f (T/(dS) %+.4f)" % (d, M, L / (d * S)))
    print("  beta1 %g  " % b1 + "  ".join(row))
