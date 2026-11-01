"""Audit of agent_B/NOTE.md, "The remainder, uniform in n" (push 82ce66d6), agent C, 20 Oct 2026.

1. Brute force over all permutations (n 5..7, random a, z with sum 0) of E S^2, E S^3, E S^4 against the note's formulas,
   and the n >= 4 constant 14 in E S^4 <= 14 (s2^2 A2^2 + m4 A4) (its two coefficients, maximised over n).
2. Brute force of E[b (Z_k + W)^2] and E[b (Z_k + W)^3] over all permutations, W = sum_{j=1..p} beta2^j Z_{pi(p-j)}, averaged over p,
   against the note's bound 8 |E b Z^2| and the claim E[b (Z_k+W)^3] = O(1/d).
3. E2(x) = sqrt(V) D(x) - [x - (d K/2)(2 x B2 + B3)/V] from the exact solver rrm_indep.py at x = 0.1, n d = 1, d = 0.01/0.005/0.0025:
   the note says |E2| <= C d^2 for every |x| <= rho; the term (3/8) x E eta^2 is of order x d.
usage: python uniform_check.py
"""
import itertools
import math

import numpy as np

from rrm_indep import Solver, K_rr_b1zero


def perm_moments(a, z):
    n = len(a)
    S = np.array([np.dot(a, z[list(p)]) for p in itertools.permutations(range(n))])
    return [np.mean(S ** k) for k in (2, 3, 4)]


def formulas(a, z):
    n = len(a)
    A2, A3, A4 = (np.sum(a ** k) for k in (2, 3, 4))
    P2, P3, P4 = (np.sum(z ** k) for k in (2, 3, 4))
    e2 = A2 * P2 / (n - 1)
    e3 = n * A3 * P3 / ((n - 1) * (n - 2))
    e4 = (A2 ** 2 * (3 * P2 ** 2 * (n * n - 3 * n + 3) - 3 * P4 * n * (n - 1))
          + A4 * (P4 * n * n * (n + 1) - 3 * P2 ** 2 * n * (n - 1))) / (n * (n - 1) * (n - 2) * (n - 3))
    return [e2, e3, e4]


def part1():
    rng = np.random.default_rng(1)
    worst = 0.0
    for n in (5, 6, 7):
        for _ in range(3):
            a = rng.normal(size=n); a -= a.mean()
            z = rng.standard_t(3, size=n); z -= z.mean()
            bf, fo = perm_moments(a, z), formulas(a, z)
            worst = max(worst, max(abs(x - y) / (abs(x) + 1e-12) for x, y in zip(bf, fo)))
    print("1. E S^2, E S^3, E S^4: brute force vs formula, n 5..7, max rel diff %.2e" % worst)
    c1 = max(3 * n * (n * n - 3 * n + 3) / ((n - 1) * (n - 2) * (n - 3)) for n in range(4, 2000))
    c2 = max(n * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3)) for n in range(4, 2000))
    print("   coefficient of s2^2 A2^2: max over n>=4 %.4f (at n 4); of m4 A4: %.4f; the note's 14 covers both" % (c1, c2))


def part2():
    rng = np.random.default_rng(2)
    print("2. E[b (Z_k+W)^2] / |E b Z^2| (note: <= 8) and d E[b (Z_k+W)^3] (note: O(1)), exact over all permutations")
    for n, b2 in ((6, 0.5), (7, 0.8), (8, 0.9), (8, 0.99)):
        for _ in range(2):
            b = rng.normal(size=n); b -= b.mean()
            x = 0.2
            g2 = (x + b) ** 2
            Z = g2 - g2.mean()
            r2, r3 = [], []
            for perm in itertools.permutations(range(n)):
                perm = list(perm)
                for p in range(n):
                    W = sum(b2 ** j * Z[perm[p - j]] for j in range(1, p + 1))
                    r2.append(b[perm[p]] * (Z[perm[p]] + W) ** 2)
                    r3.append(b[perm[p]] * (Z[perm[p]] + W) ** 3)
            ebz2 = np.mean(b * Z ** 2)
            print("   n %d beta2 %.2f: ratio %.3f   d E[b(Z+W)^3] %.4f" % (n, b2, np.mean(r2) / abs(ebz2), (1 - b2) * np.mean(r3)))


def part3():
    print("3. E2(x)/d^2 at x = 0.1, n d = 1 (note: bounded); E2/(x d) alongside")
    for n, b2 in ((100, 0.99), (200, 0.995), (400, 0.9975)):
        S = Solver(n, b2)
        d = 1 - b2
        K = K_rr_b1zero(n, b2)
        x = 0.1
        V = x * x + 9.0
        first = x - (d * K / 2) * (2 * x * 9.0 + 72.0) / V
        E2 = math.sqrt(V) * S.drift(x) - first
        print("   n %d d %.4f: E2 %.4e   E2/d^2 %.3f   E2/(x d) %.4f" % (n, d, E2, E2 / d ** 2, E2 / (x * d)), flush=True)


if __name__ == "__main__":
    part1()
    part2()
    part3()
