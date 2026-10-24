#!/usr/bin/env python3
"""Exact finite audit for quadratic tensor transfer and bounded-seed bounds."""

from fractions import Fraction
from functools import lru_cache
import math


def fwht(values):
    a = list(values)
    h = 1
    while h < len(a):
        for b in range(0, len(a), 2 * h):
            for j in range(h):
                x, y = a[b + j], a[b + j + h]
                a[b + j], a[b + j + h] = x + y, x - y
        h *= 2
    return a


def factor_exponents(n):
    ans = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            ans[p] = ans.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def add_log_ratio(out, coefficient, num, den):
    for p, e in factor_exponents(num).items():
        out[p] = out.get(p, Fraction()) + coefficient * e
    for p, e in factor_exponents(den).items():
        out[p] = out.get(p, Fraction()) - coefficient * e
    return {p: c for p, c in out.items() if c}


def vec_add(a, b, scale=Fraction(1)):
    out = dict(a)
    for p, c in b.items():
        out[p] = out.get(p, Fraction()) + scale * c
        if not out[p]:
            del out[p]
    return out


def vec_float(a):
    return sum(float(c) * math.log2(p) for p, c in a.items())


@lru_cache(None)
def spectral_data(f):
    n = len(f).bit_length() - 1
    w = fwht(f)
    sq = [z * z for z in w]
    den = 1 << (2 * n)
    masses = [Fraction(z, den) for z in sq]
    caps = [sum((masses[t] for t in range(len(f)) if (t & s) == s), Fraction())
            for s in range(len(f))]
    return masses, caps


@lru_cache(None)
def upper_u(f):
    masses, caps = spectral_data(f)
    out = {}
    for p, cap in zip(masses, caps):
        if p:
            r = cap / p
            out = add_log_ratio(out, p, r.numerator, r.denominator)
    return out


@lru_cache(None)
def entropy_h(f):
    masses, _ = spectral_data(f)
    out = {}
    for p in masses:
        if p:
            r = 1 / p
            out = add_log_ratio(out, p, r.numerator, r.denominator)
    return out


def restrict_table(f, i, bit):
    return tuple(f[x] for x in range(len(f)) if ((x >> i) & 1) == bit)


def influence_i(f, i):
    return Fraction(sum(f[x] != f[x ^ (1 << i)] for x in range(len(f))), len(f))


def total_influence(f):
    n = len(f).bit_length() - 1
    return sum((influence_i(f, i) for i in range(n)), Fraction())


@lru_cache(None)
def G_vec(f):
    n = len(f).bit_length() - 1
    out = {}
    u = upper_u(f)
    for i in range(n):
        out = vec_add(out, u)
        out = vec_add(out, upper_u(restrict_table(f, i, 0)), Fraction(-1, 2))
        out = vec_add(out, upper_u(restrict_table(f, i, 1)), Fraction(-1, 2))
    return out


def tensor_truth(f, g):
    return tuple(f[x] * g[y] for y in range(len(g)) for x in range(len(f)))


def quadratic_truth(n, edge_mask, linear_mask):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    ans = []
    for x in range(1 << n):
        bit = (linear_mask & x).bit_count() & 1
        for k, (i, j) in enumerate(edges):
            bit ^= ((edge_mask >> k) & 1) & ((x >> i) & 1) & ((x >> j) & 1)
        ans.append(1 if bit == 0 else -1)
    return tuple(ans)


def all_signs(n):
    # Quotient the irrelevant global output sign by fixing f(0)=1.
    for mask in range(1 << ((1 << n) - 1)):
        yield tuple([1] + [1 if ((mask >> (x - 1)) & 1) == 0 else -1
                           for x in range(1, 1 << n)])


def main():
    bounded_seed_functions = bounded_seed_inequalities = 0
    tensor_pairs = tensor_identities = 0
    maximum_seed_g_over_i = 0.0
    maximum_seed_h_over_i = 0.0

    # Every Boolean seed through four variables.
    for n in range(1, 5):
        edge_floor = Fraction(n, 1 << (n - 1))
        for f in all_signs(n):
            I = total_influence(f)
            U = vec_float(upper_u(f))
            H = vec_float(entropy_h(f))
            G = vec_float(G_vec(f))
            assert U >= -1e-12 and U <= H + 1e-12
            assert H <= n + 1e-12
            assert G <= n * U + 1e-11
            if I:
                assert I >= edge_floor
                assert H <= (2 ** (n - 1)) * float(I) + 1e-11
                assert G <= n * (2 ** (n - 1)) * float(I) + 1e-10
                maximum_seed_g_over_i = max(maximum_seed_g_over_i, G / float(I))
                maximum_seed_h_over_i = max(maximum_seed_h_over_i, H / float(I))
            else:
                assert not upper_u(f) and not entropy_h(f) and not G_vec(f)
            bounded_seed_functions += 1
            bounded_seed_inequalities += 6

    # Exact tensor identities for all seeds through two variables and all
    # quadratic phases through three variables, plus eight hard three-bit seeds.
    seeds = []
    for n in range(1, 3):
        seeds.extend(all_signs(n))
    hard_masks = [1, 3, 7, 13, 37, 59, 85, 107]
    seeds.extend(tuple([1] + [1 if ((m >> (x - 1)) & 1) == 0 else -1
                             for x in range(1, 8)]) for m in hard_masks)
    quadratics = []
    for n in range(1, 4):
        ec = n * (n - 1) // 2
        for e in range(1 << ec):
            for lin in range(1 << n):
                quadratics.append(quadratic_truth(n, e, lin))

    for f in seeds:
        for q in quadratics:
            F = tensor_truth(q, f)
            assert upper_u(F) == vec_add(upper_u(q), upper_u(f))
            assert entropy_h(F) == vec_add(entropy_h(q), entropy_h(f))
            assert total_influence(F) == total_influence(q) + total_influence(f)
            assert G_vec(F) == vec_add(G_vec(q), G_vec(f))
            tensor_pairs += 1
            tensor_identities += 4

    print(f"bounded_seed_functions={bounded_seed_functions}")
    print(f"bounded_seed_inequalities={bounded_seed_inequalities}")
    print(f"exact_tensor_pairs={tensor_pairs}")
    print(f"exact_tensor_identities={tensor_identities}")
    print(f"maximum_seed_G_over_I={maximum_seed_g_over_i:.15f}")
    print(f"maximum_seed_H_over_I={maximum_seed_h_over_i:.15f}")
    print("arithmetic=integer_Walsh_Fraction_and_exact_prime_log_vectors")
    print("randomness=none")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
