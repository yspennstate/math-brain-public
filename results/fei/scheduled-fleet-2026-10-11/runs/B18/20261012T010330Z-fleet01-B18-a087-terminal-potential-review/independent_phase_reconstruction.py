#!/usr/bin/env python3
"""Independent exact-interval reconstruction of the B19 phase sign.

This implementation does not import the B19 checker.  All logarithms use
rational atanh partial sums with explicit positive tails.
"""

from fractions import Fraction as F


NTERMS = 96


def ln_interval(x):
    assert x > 0
    shift = 0
    y = x
    while y < 1:
        y *= 2
        shift -= 1
    while y >= 2:
        y /= 2
        shift += 1

    def atanh_log(zarg):
        z = (zarg - 1) / (zarg + 1)
        total = F(0)
        power = z
        for m in range(NTERMS):
            total += 2 * power / (2 * m + 1)
            power *= z * z
        tail = 2 * power / ((2 * NTERMS + 1) * (1 - z * z))
        return total, total + tail

    lo, hi = atanh_log(y)
    l2lo, l2hi = atanh_log(F(2))
    if shift >= 0:
        return lo + shift * l2lo, hi + shift * l2hi
    return lo + shift * l2hi, hi + shift * l2lo


LN2 = ln_interval(F(2))


def quotient(num, den):
    values = [a / b for a in num for b in den]
    return min(values), max(values)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def subtract(x, y):
    return x[0] - y[1], x[1] - y[0]


def multiply(c, x):
    if c >= 0:
        return c * x[0], c * x[1]
    return c * x[1], c * x[0]


def phi(x):
    if x == 0:
        return F(0), F(0)
    lo, hi = ln_interval(x)
    return quotient((-x * hi, -x * lo), LN2)


def phase(a, v):
    mass = a * a + v * v
    if mass == 0:
        return F(0), F(0)
    # 1/2+sqrt(t(1-t)) = 1/2+|av|/(a^2+v^2).
    z = F(1, 2) + abs(a * v) / mass
    entropy = add(phi(z), phi(1 - z))
    return multiply(mass, subtract((F(1), F(1)), entropy))


def label(a, v):
    mass = a * a + v * v
    return subtract(add(phi(a * a), phi(v * v)), phi(mass))


def complete(a, v):
    return add(label(a, v), phase(a, v))


def qn_packet(n, packet):
    d = F(1, 1 << n)
    return add(packet(-1 + d, d), multiply((1 << n) - 1, packet(d, d)))


def qn_credit(n, packet):
    return subtract(qn_packet(n, packet), multiply(F(1, 2), qn_packet(n - 1, packet)))


def product_packet(a, b, packet):
    A, B = F(1, 1 << a), F(1, 1 << b)
    d = A * B
    spectrum = (
        (1, (-1 + 2 * A) * (-1 + 2 * B)),
        ((1 << a) - 1, 2 * A * (-1 + 2 * B)),
        ((1 << b) - 1, (-1 + 2 * A) * 2 * B),
        (((1 << a) - 1) * ((1 << b) - 1), 4 * A * B),
    )
    answer = (F(0), F(0))
    for multiplicity, coefficient in spectrum:
        answer = add(answer, multiply(multiplicity, packet(coefficient - d, d)))
    return answer


def product_credit(a, b, first_factor, packet):
    child = product_packet(a - 1, b, packet) if first_factor else product_packet(a, b - 1, packet)
    return subtract(product_packet(a, b, packet), multiply(F(1, 2), child))


def as_float(x):
    return float(x[0]), float(x[1])


checks = 0
for n in range(3, 33):
    for packet in (phase, complete):
        interval = qn_credit(n, packet)
        assert interval[1] < 0
        checks += 1

for first_factor in (True, False):
    for packet in (phase, complete):
        interval = product_credit(4, 5, first_factor, packet)
        assert interval[1] < 0
        checks += 1
        print(
            "q4_tensor_q5",
            "factor=A" if first_factor else "factor=B",
            "packet=Q" if packet is phase else "packet=D",
            "interval=", as_float(interval),
        )

print("analytic_endpoint=x<=1/8; rational_factor>=9/10")
print("finite_qn_range=3..32")
print(f"rigorous_sign_checks={checks}")
print("random_seed=None")
print("status=PASS")
