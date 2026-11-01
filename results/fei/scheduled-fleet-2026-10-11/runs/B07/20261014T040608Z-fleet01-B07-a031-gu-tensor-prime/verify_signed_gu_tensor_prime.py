#!/usr/bin/env python3
"""Audit signed U-local identities and GU tensor/character transport."""

from math import log2


def walsh(values):
    return [sum(v * (-1 if (s & x).bit_count() & 1 else 1)
                for x, v in enumerate(values)) / len(values)
            for s in range(len(values))]


def upper_masses(p):
    n = (len(p) - 1).bit_length()
    out = p[:]
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not s & bit:
                out[s] += out[s | bit]
    return out


def U_from_p(p):
    pi = upper_masses(p)
    return sum(x * log2(pi[s] / x) for s, x in enumerate(p) if x > 0.0)


def invariants(values):
    c = walsh(values)
    p = [x * x for x in c]
    U = U_from_p(p)
    I = sum(s.bit_count() * p[s] for s in range(len(p)))
    return c, p, U, I


def restrict(values, i, bit_value):
    n = (len(values) - 1).bit_length()
    out = []
    for y in range(1 << (n - 1)):
        lo = y & ((1 << i) - 1)
        hi = y >> i
        x = lo | (bit_value << i) | (hi << (i + 1))
        out.append(values[x])
    return out


def G_value(values):
    n = (len(values) - 1).bit_length()
    _, _, U, _ = invariants(values)
    total = 0.0
    for i in range(n):
        up = invariants(restrict(values, i, 1))[2]
        um = invariants(restrict(values, i, 0))[2]
        total += U - 0.5 * (up + um)
    return total


def binary_kl(p, q):
    ans = 0.0
    for x, y in ((p, q), (1.0 - p, 1.0 - q)):
        if x == 0.0:
            continue
        assert y > 0.0
        ans += x * log2(x / y)
    return ans


def h2(p):
    return sum(-x * log2(x) for x in (p, 1 - p) if x > 0.0)


def compress(mask, i):
    lo = mask & ((1 << i) - 1)
    hi = mask >> (i + 1)
    return lo | (hi << i)


def local_audit(values, i):
    c, p, Uf, _ = invariants(values)
    n = (len(values) - 1).bit_length()
    size = 1 << (n - 1)
    aa = [0.0] * size
    bb = [0.0] * size
    bit = 1 << i
    for s in range(1 << n):
        if not s & bit:
            a = compress(s, i)
            aa[a] = c[s]
            bb[a] = c[s | bit]
    m = [a * a + b * b for a, b in zip(aa, bb)]
    d = [a * b for a, b in zip(aa, bb)]
    vb = [b * b for b in bb]
    M = upper_masses(m)
    C = upper_masses(d)
    N = upper_masses(vb)
    assert abs(C[0]) < 2e-12
    Um = U_from_p(m)
    up = invariants(restrict(values, i, 1))[2]
    um = invariants(restrict(values, i, 0))[2]
    K_direct = Um - 0.5 * (up + um)
    K_formula = B = Gamma = 0.0
    for A in range(size):
        if m[A] > 0.0:
            alpha = 2 * d[A] / m[A]
            beta = 2 * C[A] / M[A]
            K_formula += m[A] * binary_kl((1 + alpha) / 2,
                                           (1 + beta) / 2)
            B += m[A] * h2(vb[A] / m[A])
        if vb[A] > 0.0:
            Gamma += vb[A] * log2(M[A] / N[A])
    delta = Uf - 0.5 * (up + um)
    assert abs(K_direct - K_formula) < 2e-10
    assert K_formula > -2e-10
    assert abs(delta - (B - Gamma + K_formula)) < 2e-10
    return 4


def tensor(g, h):
    ng = (len(g) - 1).bit_length()
    return [g[x & ((1 << ng) - 1)] * h[x >> ng]
            for x in range(len(g) * len(h))]


def character_lift(g, r):
    ng = (len(g) - 1).bit_length()
    return [g[x & ((1 << ng) - 1)] *
            (-1 if ((x >> ng) & ((1 << r) - 1)).bit_count() & 1 else 1)
            for x in range(len(g) * (1 << r))]


def main():
    boolean_cases = 0
    local_assertions = 0
    for n in range(1, 5):
        N = 1 << n
        for table in range(1 << N):
            values = [1 if table >> x & 1 else -1 for x in range(N)]
            for i in range(n):
                local_assertions += local_audit(values, i)
            boolean_cases += 1

    tensor_cases = 0
    funcs2 = [[1 if table >> x & 1 else -1 for x in range(4)]
              for table in range(16)]
    for g in funcs2:
        for h in funcs2:
            F = tensor(g, h)
            _, _, UF, IF = invariants(F)
            _, _, Ug, Ig = invariants(g)
            _, _, Uh, Ih = invariants(h)
            GF, Gg, Gh = G_value(F), G_value(g), G_value(h)
            assert abs(UF - Ug - Uh) < 2e-10
            assert abs(IF - Ig - Ih) < 2e-10
            assert abs(GF - Gg - Gh) < 2e-10
            tensor_cases += 1

    lift_cases = 0
    for n in range(1, 5):
        N = 1 << n
        selected = range(1 << N) if n <= 3 else range(0, 1 << N, 257)
        for table in selected:
            g = [1 if table >> x & 1 else -1 for x in range(N)]
            _, _, Ug, Ig = invariants(g)
            Gg = G_value(g)
            for r in range(1, 5):
                F = character_lift(g, r)
                _, _, UF, IF = invariants(F)
                GF = G_value(F)
                assert abs(UF - Ug) < 2e-10
                assert abs(IF - Ig - r) < 2e-10
                assert abs(GF - Gg) < 2e-10
                lift_cases += 1

    print("SIGNED_GU_TENSOR_PRIME_PASS")
    print("boolean_truth_tables", boolean_cases)
    print("local_identity_assertions", local_assertions)
    print("tensor_cases", tensor_cases)
    print("character_lift_cases", lift_cases)
    print("status PASS")


if __name__ == "__main__":
    main()

