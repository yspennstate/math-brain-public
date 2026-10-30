#!/usr/bin/env python3
"""Exhaustive checks for B13 derivative sign-stability identity.

Enumerates Boolean f modulo global output negation through n=4. For each
coordinate derivative g with density 0<j<=1/2 it verifies:
  4 d_g = I(A)+I(B)+2 J(A,B)
and numerically (only logarithms enter here)
  4 j Delta = iso(A)+iso(B)+2J+2j h_2(theta),
plus the Fourier Palm TV bound against the unsigned-support row.
"""
from fractions import Fraction
from math import log2, sqrt


def walsh(a):
    a = list(a)
    h = 1
    N = len(a)
    while h < N:
        for base in range(0, N, 2 * h):
            for k in range(base, base + h):
                u, v = a[k], a[k + h]
                a[k], a[k + h] = u + v, u - v
        h *= 2
    return a


def derivative(vals, n, i):
    rem = [r for r in range(n) if r != i]
    out = []
    for y in range(1 << (n - 1)):
        x0 = 0
        for k, r in enumerate(rem):
            if (y >> k) & 1:
                x0 |= 1 << r
        x1 = x0 | (1 << i)
        out.append((vals[x0] - vals[x1]) // 2)
    return out


def influence(ind, m):
    N = 1 << m
    return sum(
        Fraction(sum(ind[x] != ind[x ^ (1 << r)] for x in range(N)), N)
        for r in range(m)
    )


def cross_rate(A, B, m):
    N = 1 << m
    return sum(
        Fraction(
            sum(
                (A[x] and B[x ^ (1 << r)])
                or (B[x] and A[x ^ (1 << r)])
                for x in range(N)
            ),
            N,
        )
        for r in range(m)
    )


def dirichlet(g, m):
    N = 1 << m
    return sum(
        Fraction(
            sum((g[x] - g[x ^ (1 << r)]) ** 2 for x in range(N)),
            4 * N,
        )
        for r in range(m)
    )


def spectrum_prob(v):
    N = len(v)
    norm = Fraction(sum(x * x for x in v), N)
    W = walsh(v)
    return norm, [Fraction(w * w, N * N) / norm for w in W]


def xlog(x):
    return 0.0 if x == 0 else float(x) * log2(1.0 / float(x))


def h2(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -t * log2(t) - (1 - t) * log2(1 - t)


rows = 0
exact_edge = 0
slack_checks = 0
tv_checks = 0
max_slack_error = 0.0
max_tv_excess = -1.0

for n in range(1, 5):
    N = 1 << n
    for mask in range(1 << (N - 1)):  # f(0)=+1 quotients global sign
        vals = [1] + [1 if (mask >> (x - 1)) & 1 else -1 for x in range(1, N)]
        for i in range(n):
            g = derivative(vals, n, i)
            m = n - 1
            j = Fraction(sum(x * x for x in g), 1 << m)
            if j == 0 or j > Fraction(1, 2):
                continue
            rows += 1
            A = [x == 1 for x in g]
            B = [x == -1 for x in g]
            a = Fraction(sum(A), 1 << m)
            b = Fraction(sum(B), 1 << m)
            IA = influence(A, m)
            IB = influence(B, m)
            J = cross_rate(A, B, m)
            d = dirichlet(g, m)

            assert 4 * d == IA + IB + 2 * J
            exact_edge += 1

            Delta = float(d / j) - 0.5 * log2(1.0 / float(j))
            theta = min(float(a / j), float(b / j))
            isoA = float(IA) - 2 * xlog(a)
            isoB = float(IB) - 2 * xlog(b)
            lhs = 4 * float(j) * Delta
            rhs = isoA + isoB + 2 * float(J) + 2 * float(j) * h2(theta)
            err = abs(lhs - rhs)
            max_slack_error = max(max_slack_error, err)
            assert err < 1e-10
            assert isoA > -1e-10 and isoB > -1e-10
            assert h2(theta) <= 2 * Delta + 1e-10
            assert theta <= Delta + 1e-10
            slack_checks += 1

            _, Pg = spectrum_prob(g)
            E = [1 if x else 0 for x in g]
            _, PE = spectrum_prob(E)
            tv = 0.5 * sum(abs(float(x - y)) for x, y in zip(Pg, PE))
            tv_bound = 2 * sqrt(theta * (1 - theta))
            max_tv_excess = max(max_tv_excess, tv - tv_bound)
            assert tv <= tv_bound + 1e-10
            tv_checks += 1

print("PASS")
print(f"derivative_rows={rows}")
print(f"exact_edge_identities={exact_edge}")
print(f"slack_identity_checks={slack_checks}")
print(f"palm_tv_checks={tv_checks}")
print(f"total_checks={exact_edge + slack_checks + tv_checks}")
print(f"max_slack_abs_error={max_slack_error:.3e}")
print(f"max_tv_excess={max_tv_excess:.3e}")
