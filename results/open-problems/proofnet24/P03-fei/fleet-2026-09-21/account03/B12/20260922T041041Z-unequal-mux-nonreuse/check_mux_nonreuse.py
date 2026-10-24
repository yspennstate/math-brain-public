#!/usr/bin/env python3
"""Reproduce the scalar numbers in account03/B12's unequal-data MUX report.

This is a diagnostic/reproduction script, not an interval proof of the stored h96
candidate.  The proof in REPORT.md uses exact algebra plus the conservative source
premises already proved/recorded by account01/B18.
"""
import math

C0 = 6.4548
C = 6.521851214
a = 4.0 * (C - C0)
alpha = 2.0 * (C0 - 4.0)
B = C / 2.0 + 2.0


def V(p):
    return 4.0 * p * (1.0 - p)


def h(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def phi(w):
    return 0.0 if w <= 0.0 else w * math.log2(1.0 / w)


def mux_weights(t, q0, q1):
    r = (1.0 - t) * q0 + t * q1
    return (
        (1.0 - 2.0 * r) ** 2,
        V(t) * (q1 - q0) ** 2,
        (1.0 - t) ** 2 * V(q0),
        t * t * V(q1),
        t * (1.0 - t) * V(q0),
        t * (1.0 - t) * V(q1),
    )


def direct_entropy(t, q0, q1):
    return sum(phi(w) for w in mux_weights(t, q0, q1))


def influence_and_currency(t, q0, q1):
    delta = q0 + q1 - 2.0 * q0 * q1
    I = V(t) * delta + (1.0 - t) * V(q0) + t * V(q1)
    r = (1.0 - t) * q0 + t * q1
    W_direct = I / 4.0 - r * (1.0 - r)
    W_closed = V(t) * (V(q0) + V(q1)) / 16.0
    return I, W_direct, W_closed


# Source-output dyadic wobble values from cert_vi_h96k40.out.
wobble = {
    1: 8.000000,
    2: 8.000000,
    3: 6.264663,
    4: 4.780196,
    6: 3.122832,
    8: 2.515479,
    10: 2.316432,
    14: 2.236624,
    20: 2.229381,
    30: 2.229220,
    40: 2.229220,
}


def gamma_dagger_dyadic(x):
    q = 2.0 ** (-x)
    G = alpha * x + wobble[x]
    return q * G + a * q * (1.0 - q)


print("C0", format(C0, ".12f"))
print("Cdagger", format(C, ".12f"))
print("adagger", format(a, ".12f"))
print("alpha", format(alpha, ".12f"))
print("B=C/2+2", format(B, ".12f"))

# The interior stress point t=1/2, q0=1/4, q1=3/4.
q = 0.25
Gq = gamma_dagger_dyadic(2)
D_quarter = Gq - V(q) * B
S_half = C / 2.0 - 2.0
R_asym = D_quarter - V(q) * S_half
print("quarter_Gamma", format(Gq, ".15f"))
print("quarter_D", format(D_quarter, ".15f"))
print("half_equal_data_star_reserve_S", format(S_half, ".15f"))
print("quarter_residual", format(R_asym, ".15f"))
print("quarter_residual_exact_from_C0", format(C0 / 4.0 - 2.0, ".15f"))

# Conservative tail lower bound used in the proof.
x0 = 3.38
q0 = 2.0 ** (-x0)
K = 4.0 * B - a
L = alpha * x0 + 2.22 - K * (1.0 - q0)
dL = alpha - K * math.log(2.0) * q0
print("tail_x", format(x0, ".6f"))
print("tail_q", format(q0, ".15f"))
print("tail_lower_D_over_q", format(L, ".15f"))
print("tail_lower_derivative", format(dL, ".15f"))

print("dyadic_complementary_line")
for x in sorted(wobble):
    q = 2.0 ** (-x)
    gam = gamma_dagger_dyadic(x)
    D = gam - V(q) * B
    print(x, format(q, ".15g"), format(gam, ".15g"), format(D, ".15g"))

# Algebra smoke tests: weights sum to 1 and the two W formulas agree.
tests = [
    (0.3, 0.2, 0.7),
    (0.5, 0.25, 0.75),
    (0.11, 0.37, 0.82),
    (0.89, 0.03, 0.44),
]
max_parseval = 0.0
max_currency = 0.0
for t, x, y in tests:
    max_parseval = max(max_parseval, abs(sum(mux_weights(t, x, y)) - 1.0))
    _, wd, wc = influence_and_currency(t, x, y)
    max_currency = max(max_currency, abs(wd - wc))
print("max_parseval_error", format(max_parseval, ".3e"))
print("max_currency_identity_error", format(max_currency, ".3e"))
