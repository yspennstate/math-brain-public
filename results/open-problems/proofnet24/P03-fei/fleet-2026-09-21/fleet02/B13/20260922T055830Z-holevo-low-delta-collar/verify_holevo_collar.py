#!/usr/bin/env python3
"""
Self-check for fleet02/B13 20260922T055830Z.

The theorem is analytic.  This script only checks:
  * the signed-overlap / Bhattacharyya / Holevo inequalities on every
    ordered Boolean child pair through three residual variables at five
    pivot biases;
  * the vertical spectral entropy cap H(J|S) <= h2(V_t delta);
  * the exact two-channel spectral mass identity;
  * the rational positivity of the final collar constants.

No external packages are used.
"""
from fractions import Fraction
from math import log2, sqrt

T_VALUES = (0.5, 0.25, 0.125, 1.0 / 16.0, 1.0 / 256.0)
TOL = 5e-13

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)

def entropy(prob):
    out = 0.0
    for x in prob:
        if x > 0.0:
            out -= x * log2(x)
    return out

def fwht(values):
    a = [float(x) for x in values]
    h = 1
    n = len(a)
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    inv = 1.0 / n
    return [x * inv for x in a]

checks = 0
max_holevo_excess = -1e100
max_vertical_excess = -1e100
max_mass_identity_error = 0.0
max_overlap_deficit = -1e100
max_signed_overlap_error = 0.0
worst_holevo = None

for n in range(4):
    N = 1 << n
    funcs = []
    specs = []
    for mask in range(1 << N):
        vals = [1.0 if ((mask >> i) & 1) == 0 else -1.0 for i in range(N)]
        funcs.append(vals)
        specs.append(fwht(vals))

    for ia, a in enumerate(specs):
        P = [x * x for x in a]
        HP = entropy(P)
        for ib, b in enumerate(specs):
            Q = [x * x for x in b]
            HQ = entropy(Q)
            delta = sum(1 for x, y in zip(funcs[ia], funcs[ib]) if x != y) / N
            signed = sum(x * y for x, y in zip(a, b))
            max_signed_overlap_error = max(
                max_signed_overlap_error, abs(signed - (1.0 - 2.0 * delta))
            )
            BC = sum(abs(x * y) for x, y in zip(a, b))
            max_overlap_deficit = max(max_overlap_deficit, abs(signed) - BC)

            for t in T_VALUES:
                q = 1.0 - t
                V = 4.0 * t * q
                T = [q * p + t * r for p, r in zip(P, Q)]
                JS = entropy(T) - q * HP - t * HQ

                discr = max(0.0, 1.0 - 4.0 * V * delta * (1.0 - delta))
                lam = (1.0 - sqrt(discr)) / 2.0
                chi = h2(lam)
                holevo_excess = JS - chi
                if holevo_excess > max_holevo_excess:
                    max_holevo_excess = holevo_excess
                    worst_holevo = (n, ia, ib, t, delta, JS, chi, BC)

                alpha = [q * x + t * y for x, y in zip(a, b)]
                beta = [sqrt(t * q) * (y - x) for x, y in zip(a, b)]
                vertical = [x * x for x in beta]
                for u, v, m in zip(alpha, vertical, T):
                    max_mass_identity_error = max(
                        max_mass_identity_error, abs(u * u + v - m)
                    )

                HJ_given_S = 0.0
                for m, v in zip(T, vertical):
                    if m > 0.0:
                        HJ_given_S += m * h2(v / m)
                max_vertical_excess = max(
                    max_vertical_excess, HJ_given_S - h2(V * delta)
                )
                checks += 1

if max_holevo_excess > TOL:
    raise AssertionError(("Holevo excess", max_holevo_excess, worst_holevo))
if max_vertical_excess > TOL:
    raise AssertionError(("vertical entropy excess", max_vertical_excess))
if max_mass_identity_error > TOL:
    raise AssertionError(("mass identity", max_mass_identity_error))
if max_overlap_deficit > TOL:
    raise AssertionError(("Bhattacharyya deficit", max_overlap_deficit))
if max_signed_overlap_error > TOL:
    raise AssertionError(("signed overlap error", max_signed_overlap_error))

kappa = Fraction(512, 511)
A = Fraction(49096, 10000) - 4 * kappa
B = 4 + 4 * kappa
C = Fraction(222, 100) - 6 - 4 * kappa
coef_D = 9 * A - B
constant = 10 * A + C

assert A > 0
assert coef_D > 0
assert constant > 0

print("PASS")
print(f"ordered_child_pair_bias_checks={checks}")
print(f"max_holevo_excess={max_holevo_excess:.3e}")
print(f"max_vertical_entropy_excess={max_vertical_excess:.3e}")
print(f"max_parent_mass_identity_error={max_mass_identity_error:.3e}")
print(f"max_signed_overlap_error={max_signed_overlap_error:.3e}")
print(f"max_BC_deficit={max_overlap_deficit:.3e}")
print(f"kappa={kappa}={float(kappa):.15f}")
print(f"A={A}={float(A):.15f}")
print(f"9A-B={coef_D}={float(coef_D):.15f}")
print(f"10A+C={constant}={float(constant):.15f}")
print("analytic_collar=u<=2^-10*delta^9, 0<delta<=1/4")
