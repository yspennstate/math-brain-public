#!/usr/bin/env python3
from fractions import Fraction
import json
import math


def s_exact(N, x):
    q = Fraction(1, 1) - x
    return sum(
        k * math.comb(N, k) * (x ** k) * (q ** (N - k))
        for k in range(4, N + 1)
    )


def s_tail_exact(N, x):
    q = Fraction(1, 1) - x
    p_le_2 = (
        q ** (N - 1)
        + (N - 1) * x * q ** (N - 2)
        + math.comb(N - 1, 2) * x * x * q ** (N - 3)
    )
    return N * x * (1 - p_le_2)


def universal_S_float(N, s):
    if s == 0.0:
        return 0.0
    x = math.sin(s / N) ** 2
    q = 1.0 - x
    p_le_2 = (
        q ** (N - 1)
        + (N - 1) * x * q ** (N - 2)
        + math.comb(N - 1, 2) * x * x * q ** (N - 3)
    )
    return N * x * max(0.0, 1.0 - p_le_2)


def simpson_integral(N, umax=30.0, steps=120000):
    # With u=s/N,
    # 4 int S_N(s) ds/s^3 = (4/N^2) int S_N(Nu) du/u^3.
    if steps % 2:
        steps += 1
    h = umax / steps

    def f(u):
        if u == 0.0:
            return 0.0
        return (4.0 / (N * N)) * universal_S_float(N, N * u) / (u ** 3)

    total = f(0.0) + f(umax)
    for j in range(1, steps):
        total += (4 if j % 2 else 2) * f(j * h)
    return total * h / 3.0


def plaquette_mean_and_p(table, n, i, w):
    N = 1 << n
    ei = 1 << i
    negative = 0
    support_mismatch = 0
    for y in range(N):
        h = table[y] * table[y ^ ei] * table[y ^ w] * table[y ^ w ^ ei]
        if h == -1:
            negative += 1
        eta_0 = int(table[y] != table[y ^ ei])
        eta_1 = int(table[y ^ w] != table[y ^ w ^ ei])
        if eta_0 != eta_1:
            support_mismatch += 1
    return negative, support_mismatch


exact_envelope_checks = 0
for N in [4, 8, 16, 32]:
    for den in [8, 16, 32]:
        for j in range(den + 1):
            x = Fraction(j, den)
            lhs = s_exact(N, x)
            rhs = s_tail_exact(N, x)
            assert lhs == rhs
            assert lhs <= N * x
            quartic = Fraction(N * (N - 1) * (N - 2) * (N - 3), 6) * (x ** 4)
            assert lhs <= quartic
            exact_envelope_checks += 3

plaquette_checks = 0
for n in [2, 3]:
    N = 1 << n
    for bits in range(1 << N):
        table = [-1 if (bits >> x) & 1 else 1 for x in range(N)]
        for i in range(n):
            for w in range(1, N):
                if (w >> i) & 1:
                    continue
                a, b = plaquette_mean_and_p(table, n, i, w)
                assert a == b
                plaquette_checks += 1

quadratic_obstruction = []
for n in range(2, 7):
    N = 1 << n
    # f(x)=(-1)^(x_1 x_2), with arbitrary dummy coordinates.
    table = [-1 if ((x & 1) and (x & 2)) else 1 for x in range(N)]
    a, b = plaquette_mean_and_p(table, n, 0, 2)
    influences = []
    for i in range(n):
        ei = 1 << i
        cnt = sum(1 for x in range(N) if table[x] != table[x ^ ei])
        influences.append(Fraction(cnt, N))
    J = sum(min(z, 1 - z) for z in influences)
    assert a == N and b == N and J == 1
    quadratic_obstruction.append(
        {"n": n, "N": N, "plaquette_negative_fraction": "1", "J": "1"}
    )

constant_term = 8.0 / 3.0 - (2.0 / 3.0) * math.log(6.0)
analytic_constants = {}
for N in [4, 8, 16, 32, 64, 128, 256, 1024]:
    analytic_constants[str(N)] = (2.0 * math.log(N) + constant_term) / N

integral_diagnostics = {}
for N in [4, 8, 16, 32, 64]:
    value = simpson_integral(N)
    tail_upper = 2.0 / (N * 30.0 * 30.0)
    bound = analytic_constants[str(N)]
    assert value <= bound
    integral_diagnostics[str(N)] = {
        "simpson_0_to_30N": value,
        "tail_upper_bound": tail_upper,
        "analytic_bound": bound,
    }

result = {
    "status": "PASS",
    "exact_binomial_envelope_checks": exact_envelope_checks,
    "plaquette_mean_identity_checks": plaquette_checks,
    "quadratic_mean_obstruction": quadratic_obstruction,
    "analytic_C_N": analytic_constants,
    "universal_shell_integral_diagnostics": integral_diagnostics,
    "theorem_bound": (
        "4 int_0^infty Var(V_s) ds/s^3 <= "
        "((2 ln N + 8/3 - (2/3) ln 6)/N) J"
    ),
    "notes": "Numerical integrals are diagnostics only; the theorem is analytic.",
}
print(json.dumps(result, indent=2, sort_keys=True))
