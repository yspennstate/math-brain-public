#!/usr/bin/env python3
"""Audit the optimal root signed-KL payment and its A099 remainder."""

from decimal import Decimal, getcontext
from functools import lru_cache
from math import log, log2

getcontext().prec = 90


def fwht(values):
    a = list(values)
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2 * h):
            for j in range(start, start + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def upper(values, n):
    z = list(values)
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not s & bit:
                z[s] += z[s | bit]
    return z


def h2(x):
    return sum(-z * log2(z) for z in (x, 1 - x) if z > 0)


def d2(p, q):
    ans = 0.0
    for x, y in ((p, q), (1 - p, 1 - q)):
        if x:
            ans += x * log2(x / y)
    return ans


def children(values, i):
    ans = [[], []]
    for x, v in enumerate(values):
        ans[(x >> i) & 1].append(v)
    return tuple(map(tuple, ans))


@lru_cache(None)
def metrics(values):
    n = len(values).bit_length() - 1
    raw = fwht(values)
    p = [(x / len(values)) ** 2 for x in raw]
    pi = upper(p, n)
    U = sum(x * log2(y / x) for x, y in zip(p, pi) if x)
    I = sum(s.bit_count() * x for s, x in enumerate(p))
    if n == 0:
        return U, I, 0.0
    G = 0.0
    for i in range(n):
        G += U - sum(metrics(c)[0] for c in children(values, i)) / 2
    return U, I, G


def remove_bit(s, i):
    lo = s & ((1 << i) - 1)
    hi = s >> (i + 1)
    return lo | (hi << i)


def insert_bit(a, i, one):
    lo = a & ((1 << i) - 1)
    hi = a >> i
    return lo | (one << i) | (hi << (i + 1))


def signed_rows(values):
    n = len(values).bit_length() - 1
    c = [x / len(values) for x in fwht(values)]
    root = 0.0
    root_bound_mass = 0.0
    nonempty_debt = 0.0
    identity_error = 0.0
    for i in range(n):
        size = 1 << (n - 1)
        aa = [c[insert_bit(a, i, 0)] for a in range(size)]
        bb = [c[insert_bit(a, i, 1)] for a in range(size)]
        m = [x*x + y*y for x, y in zip(aa, bb)]
        mb = [y*y for y in bb]
        cross = [x*y for x, y in zip(aa, bb)]
        M = upper(m, n - 1)
        N = upper(mb, n - 1)
        C = upper(cross, n - 1)
        B = Gamma = K = 0.0
        for A in range(size):
            if m[A]:
                B += m[A] * h2(mb[A] / m[A])
                alpha = 2 * aa[A] * bb[A] / m[A]
                beta = 2 * C[A] / M[A]
                K += m[A] * d2((1 + alpha) / 2, (1 + beta) / 2)
            if mb[A]:
                Gamma += mb[A] * log2(M[A] / N[A])
        a0, b0 = aa[0], bb[0]
        m0 = a0*a0 + b0*b0
        k0 = 0.0 if not m0 else m0 * (1 - h2((1 + 2*a0*b0/m0) / 2))
        bound = (2 / log(2)) * min(a0*a0, b0*b0)
        assert k0 <= bound + 3e-12
        root += k0
        root_bound_mass += min(a0*a0, b0*b0)
        nonempty_debt += B - Gamma + K - k0
        du = metrics(values)[0] - sum(metrics(ch)[0] for ch in children(values, i)) / 2
        identity_error = max(identity_error, abs(du - (B - Gamma + K)))
    return root, root_bound_mass, nonempty_debt, identity_error


def point_defect_ratio(n):
    one = Decimal(1)
    t = Decimal(2) ** (1 - n)
    a, b = one - t, t
    m = a*a + b*b
    x = 2*a*b/m
    p = (one + x) / 2
    q = one - p
    h = -(p*p.ln() + q*q.ln()) / Decimal(2).ln()
    k = m * (one - h)
    return k / min(a*a, b*b)


def main():
    cases = assertions = candidate_failures = 0
    max_scalar_ratio = max_identity_error = max_candidate_excess = 0.0
    worst = None
    c0 = 2 / log(2)
    for n in range(1, 5):
        N = 1 << n
        for mask in range(1 << (N - 1)):
            values = tuple([1] + [1 if (mask >> (x - 1)) & 1 else -1
                                  for x in range(1, N)])
            U, I, G = metrics(values)
            root, mass, debt, err = signed_rows(values)
            max_identity_error = max(max_identity_error, err)
            assert abs(G - root - debt) < 2e-11
            if mass:
                max_scalar_ratio = max(max_scalar_ratio, root / mass)
            # Sufficient nonempty-row endpoint for (a,b)=(4,3/4).
            excess = debt + c0 * mass - 4 * I - 0.75 * U
            if excess > max_candidate_excess:
                max_candidate_excess, worst = excess, (n, mask, U, I, G, root, mass, debt)
            if excess > 2e-11:
                candidate_failures += 1
            cases += 1
            assertions += n + 2

    defect = point_defect_ratio(40)
    print('STATUS PASS')
    print('boolean_signs_mod_output', cases)
    print('assertions_at_least', assertions)
    print('maximum_local_identity_error', format(max_identity_error, '.3e'))
    print('optimal_constant_2_over_ln2', format(c0, '.15g'))
    print('maximum_finite_root_over_min_mass', format(max_scalar_ratio, '.15g'))
    print('point_defect_n40_ratio', format(defect, '.15g'))
    print('candidate_nonempty_endpoint_failures_n_le_4', candidate_failures)
    print('maximum_candidate_excess', format(max_candidate_excess, '.15g'))
    print('worst_case', worst)
    print('universal_GU', 'OPEN')


if __name__ == '__main__':
    main()
