#!/usr/bin/env python3
"""Finite consistency checks for the PROB20-14 balanced-prefix reduction.

This is NOT proof evidence for the infinite-variance theorem.  It checks:
  1. the deterministic fixed-depth collapse lemma on exhaustive small sequences;
  2. the elementary Chernoff half-drop inequality on a critical finite-support law;
  3. the excess-total-progeny forest recoding against the exact Dwass formula
     for the critical binary offspring law P(xi=0)=P(xi=2)=1/2.

Only Python's standard library is used.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, exp, gcd


def check_collapse_lemma(max_k=5, zmax=7):
    checked = 0
    triggered = 0
    for k in range(1, max_k + 1):
        C = k * (2 ** k)
        for tail in product(range(zmax + 1), repeat=k):
            z = (1,) + tail
            N = sum(z[:-1])
            L = z[-1]
            checked += 1
            if N > C * L:
                triggered += 1
                ok = any(
                    z[j] * C >= N and 2 * z[j + 1] <= z[j]
                    for j in range(k)
                )
                assert ok, (k, C, z, N, L)
    return checked, triggered


def convolve_once(dist, offspring):
    out = defaultdict(float)
    for s, ps in dist.items():
        for x, px in offspring.items():
            out[s + x] += ps * px
    return dict(out)


def check_half_drop_chernoff(max_m=40):
    # Critical law: 0*.19 + 1*.80 + 20*.01 = 1.
    offspring = {0: 0.19, 1: 0.80, 20: 0.01}
    assert abs(sum(x * p for x, p in offspring.items()) - 1.0) < 1e-14

    # Search a harmless t with rho=e^(t/2) E e^(-t xi) < 1.
    candidates = [j / 1000 for j in range(1, 1001)]
    t = min(candidates, key=lambda s: exp(s / 2) * sum(p * exp(-s * x) for x, p in offspring.items()))
    rho = exp(t / 2) * sum(p * exp(-t * x) for x, p in offspring.items())
    assert rho < 1.0

    dist = {0: 1.0}
    worst_ratio = 0.0
    for m in range(1, max_m + 1):
        dist = convolve_once(dist, offspring)
        p_lower = sum(p for s, p in dist.items() if 2 * s <= m)
        bound = rho ** m
        assert p_lower <= bound * (1 + 1e-10), (m, p_lower, bound)
        worst_ratio = max(worst_ratio, p_lower / bound if bound else 0.0)
    return t, rho, worst_ratio


def catalan(m):
    return comb(2 * m, m) // (m + 1)


def u_binary(m):
    # Critical full-binary GW tree: X=1+2m with probability Catalan_m / 2^(2m+1).
    return Fraction(catalan(m), 2 ** (2 * m + 1))


def convolution_mass_u(b, M):
    dist = [Fraction(0) for _ in range(M + 1)]
    dist[0] = Fraction(1)
    base = [u_binary(j) for j in range(M + 1)]
    for _ in range(b):
        nxt = [Fraction(0) for _ in range(M + 1)]
        for a in range(M + 1):
            if not dist[a]:
                continue
            for j in range(M - a + 1):
                nxt[a + j] += dist[a] * base[j]
        dist = nxt
    return dist[M]


def check_binary_forest_dwass(max_b=6, max_M=18):
    # Here h=2 and U=(X-1)/2.
    offspring_support = [0, 2]
    h = 0
    for d in offspring_support:
        if d > 0:
            h = gcd(h, d)
    assert h == 2

    cases = 0
    for b in range(1, max_b + 1):
        for M in range(max_M + 1):
            lhs = convolution_mass_u(b, M)
            N = b + 2 * M
            # Forest Dwass: P(total size N from b roots)=b/N P(S_N=N-b).
            # S_N=2 Bin(N,1/2), and N-b=2M.
            rhs = Fraction(b * comb(N, M), N * (2 ** N))
            assert lhs == rhs, (b, M, lhs, rhs)
            cases += 1
    return cases


def main():
    checked, triggered = check_collapse_lemma()
    t, rho, worst = check_half_drop_chernoff()
    forest_cases = check_binary_forest_dwass()
    print(f"collapse sequences checked: {checked}")
    print(f"collapse antecedent triggered: {triggered}")
    print(f"Chernoff t={t:.6f}, rho={rho:.12f}, worst exact/bound={worst:.12f}")
    print(f"exact binary forest/Dwass cases checked: {forest_cases}")
    print("ALL ASSERTIONS PASSED")


if __name__ == "__main__":
    main()
