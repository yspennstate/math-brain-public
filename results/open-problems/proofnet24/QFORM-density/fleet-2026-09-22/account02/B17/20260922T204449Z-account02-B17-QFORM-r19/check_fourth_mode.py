from math import atan, erfc, exp, pi, sqrt


def neg_factor(delta: float) -> float:
    return 1.0 / sqrt(1.0 + delta)


def pos_zero_factor(delta: float) -> float:
    if abs(delta - 1.0) < 1e-15:
        return sqrt(2.0) / pi
    if not (0.0 < delta < 1.0):
        raise ValueError("formula checked here only for 0<delta<=1")
    return 2.0 / (pi * sqrt(1.0 - delta)) * atan(sqrt((1.0 - delta) / (2.0 * delta)))


eta = erfc(1.0 / sqrt(2.0))
baseline = 3.0 * sqrt(2.0)

# The Bessel density h_delta has log derivative
# -alpha + beta I1/I0; since I1/I0<1 it is enough that alpha-beta>0.
for delta in (0.01, 0.1, 0.5, 1.0, 2.0, 10.0):
    alpha = (1.0 + 1.0 / delta) / 4.0
    beta = abs(1.0 - 1.0 / delta) / 4.0
    assert alpha - beta > 0.0

for delta in (0.01, 0.1, 0.5, 1.0):
    nf = neg_factor(delta)
    pf = pos_zero_factor(delta)
    partner_factor = 1.0 - eta * (1.0 - exp(-delta / 4.0))
    assert 0.0 < nf < 1.0
    assert 0.0 < pf < 1.0
    assert nf < partner_factor
    print(
        f"delta={delta:g} neg_factor={nf:.15f} "
        f"plus_zero_factor={pf:.15f} partner_factor={partner_factor:.15f}"
    )

# delta=1 exact physical constants.
neg_phys_1 = baseline * neg_factor(1.0)
pos_zero_phys_1 = baseline * pos_zero_factor(1.0)
partner_phys_1 = baseline * (1.0 - eta * (1.0 - exp(-0.25)))
assert abs(neg_phys_1 - 3.0) < 1e-14
assert abs(pos_zero_phys_1 - 6.0 / pi) < 1e-14
assert neg_phys_1 < partner_phys_1 < baseline

print(f"baseline_3sqrt2={baseline:.15f}")
print(f"delta1_exact_negative_physical={neg_phys_1:.15f}")
print(f"delta1_plus_zero_physical={pos_zero_phys_1:.15f}")
print(f"delta1_partner_signfree_bound={partner_phys_1:.15f}")

# Small-delta expansions used in the report.
for delta in (1e-8, 1e-6, 1e-4):
    neg_series = 1.0 - delta / 2.0 + 3.0 * delta * delta / 8.0
    pos_series = (
        1.0
        - (2.0 * sqrt(2.0) / pi) * sqrt(delta)
        + delta / 2.0
        - (2.0 * sqrt(2.0) / (3.0 * pi)) * delta ** 1.5
        + 3.0 * delta * delta / 8.0
    )
    assert abs(neg_factor(delta) - neg_series) < 1e-9
    assert abs(pos_zero_factor(delta) - pos_series) < 1e-8

print("PASS")
