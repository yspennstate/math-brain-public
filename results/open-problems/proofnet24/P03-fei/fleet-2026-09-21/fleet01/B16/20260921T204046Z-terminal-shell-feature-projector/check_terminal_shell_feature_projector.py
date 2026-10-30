#!/usr/bin/env python3
"""Exact finite checks for B16 terminal-shell feature projector.

This is a falsification/self-check only. The report contains analytic proofs.
It does not rerun the settled FEI read-once certificate.
"""
from fractions import Fraction
from math import comb

def parity(x):
    return x.bit_count() & 1

def dot_parity(a, b):
    return parity(a & b)

def chi(A, q):
    return -1 if dot_parity(A, q) else 1

def phys_xor(A, n):
    out = 0
    for x in range(1 << n):
        if (A >> x) & 1:
            out ^= x
    return out

def c0_words(n):
    N = 1 << n
    return [
        A for A in range(1 << N)
        if parity(A) == 0 and phys_xor(A, n) == 0
    ]

def perp(words, N):
    return [
        r for r in range(1 << N)
        if all(dot_parity(r, A) == 0 for A in words)
    ]

def magnetization(q, N):
    return Fraction(N - 2 * q.bit_count(), N)

def lambda_threshold(A, u, N):
    total = 0
    G = 1 << N
    for q in range(G):
        if magnetization(q, N) ** 2 >= u:
            total += chi(A, q)
    return Fraction(total, G)

def direct_D_threshold(n, fword, q, u):
    """E_{P0} delta - E_G delta for E={0}."""
    N = 1 << n
    G = 1 << N
    C0 = c0_words(n)
    P0 = perp(C0, N)
    ans = Fraction(0)
    for r in P0:
        V = magnetization(r ^ q ^ fword, N) ** 2
        U = magnetization(r ^ q, N) ** 2
        ans += Fraction((V >= u) - (U >= u), len(P0))
    for r in range(G):
        V = magnetization(r ^ q ^ fword, N) ** 2
        U = magnetization(r ^ q, N) ** 2
        ans -= Fraction((V >= u) - (U >= u), G)
    return ans

def formula_D_threshold(n, fword, q, u):
    N = 1 << n
    ans = Fraction(0)
    for A in c0_words(n):
        if A and chi(A, fword) == -1:
            ans -= 2 * lambda_threshold(A, u, N) * chi(A, q)
    return ans

def syndrome_square(n, fword, u, generators):
    N = 1 << n
    lhs = Fraction(0)
    m = len(generators)
    for S in range(1 << m):
        q = 0
        for j, g in enumerate(generators):
            if (S >> j) & 1:
                q ^= g
        d = direct_D_threshold(n, fword, q, u)
        lhs += d * d / (1 << m)

    grouped = {}
    for A in c0_words(n):
        if not A or chi(A, fword) != -1:
            continue
        R = 0
        for j, g in enumerate(generators):
            if chi(A, g) == -1:
                R |= 1 << j
        grouped[R] = grouped.get(R, Fraction(0)) + lambda_threshold(A, u, N)
    rhs = 4 * sum(x * x for x in grouped.values())
    return lhs, rhs

def threshold_mu_by_level(N):
    values = sorted({magnetization(q, N) ** 2 for q in range(1 << N)})
    mu = [Fraction(0) for _ in range(N + 1)]
    for a, b in zip(values[:-1], values[1:]):
        u = (a + b) / 2
        length = b - a
        for k in range(N + 1):
            A = (1 << k) - 1 if k else 0
            lam = lambda_threshold(A, u, N)
            mu[k] += length * lam * lam
    return mu

def expected_abs_rademacher(m):
    return sum(
        Fraction(comb(m, j), 1 << m) * abs(m - 2 * j)
        for j in range(m + 1)
    )

def main():
    shell_checks = 0
    feature_checks = 0
    syndrome_checks = 0

    for n in (2, 3):
        N = 1 << n
        G = 1 << N
        C0 = c0_words(n)
        P0 = perp(C0, N)
        assert len(P0) == 2 * N

        # E={0}, so P1=G and terminal multiplier must be 1_{C0\{0}}.
        for A in range(G):
            val = sum(Fraction(chi(A, r), len(P0)) for r in P0)
            val -= sum(Fraction(chi(A, r), G) for r in range(G))
            target = Fraction(int(A in C0 and A != 0))
            assert val == target
            shell_checks += 1

        values = sorted({magnetization(q, N) ** 2 for q in range(G)})
        probes = values + [(a + b) / 2 for a, b in zip(values[:-1], values[1:])]
        fwords = [x for x in (1, 3, 5, G - 2) if x < G]
        for fword in fwords:
            for q in range(min(G, 16)):
                for u in probes:
                    assert direct_D_threshold(n, fword, q, u) == formula_D_threshold(
                        n, fword, q, u
                    )
                    feature_checks += 1

        generators = [1, 2, 4][: min(3, N)]
        for fword in (1, 3, 5):
            if fword >= G:
                continue
            for u in values:
                lhs, rhs = syndrome_square(n, fword, u, generators)
                assert lhs == rhs
                syndrome_checks += 1

    energy_checks = 0
    obstruction_values = {}
    for N in (4, 8):
        mu = threshold_mu_by_level(N)
        total = sum(Fraction(comb(N, k)) * mu[k] for k in range(N + 1))
        degree = sum(
            Fraction(comb(N, k) * k) * mu[k] for k in range(N + 1)
        )
        expected_total = Fraction(1, N)
        expected_degree = expected_abs_rademacher(N - 1) / N
        assert total == expected_total
        assert degree == expected_degree
        energy_checks += 2

        one_point_diag = 4 * expected_abs_rademacher(N - 1)
        obstruction_values[str(N)] = str(one_point_diag)

    print("PASS")
    print("shell_multiplier_checks", shell_checks)
    print("feature_factorization_checks", feature_checks)
    print("syndrome_square_checks", syndrome_checks)
    print("threshold_energy_checks", energy_checks)
    print("one_point_forbidden_diagonal", obstruction_values)

if __name__ == "__main__":
    main()
