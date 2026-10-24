from fractions import Fraction
from math import ceil, pi, sqrt

FULL_E = Fraction(4, 9)
CENTRAL_E = Fraction(11, 288)
RATIO = CENTRAL_E / FULL_E
assert RATIO == Fraction(11, 128)

FULL_LB = Fraction(7, 3145728)
CENTRAL_LB = FULL_LB * RATIO
assert CENTRAL_LB == Fraction(77, 402653184)

CENTRAL_ASYM = Fraction(11, 864)
AVERAGED_ASYM = CENTRAL_ASYM / 8
assert AVERAGED_ASYM == Fraction(11, 6912)


def sink_ratio_lower(D):
    n = D - 1
    # P_cen >= CENTRAL_LB / n^3 and K <= 16n/2^D.
    return Fraction(
        CENTRAL_LB.numerator * (1 << D),
        CENTRAL_LB.denominator * 16 * n**4,
    )


def terminal_energy_ratio_upper(D):
    n = D - 1
    d = ceil(D / 2)
    m = (1 << (d - 1)) - 1
    T = 1 / sqrt(2 * n)
    E1 = 4 * pi * T**3 / sqrt(m)
    E0_asym = float(Fraction(2, 3)) * T**6
    return E1 / E0_asym


Ds = [128, 160, 192, 256]
ratios = [sink_ratio_lower(D) for D in Ds]
for a, b in zip(ratios, ratios[1:]):
    assert b > a

print("PASS")
print("central/full multiplier ratio =", RATIO)
print("central rigorous lower-bound coefficient =", CENTRAL_LB)
print("central asymptotic coefficient =", CENTRAL_ASYM)
print("outer-average asymptotic coefficient =", AVERAGED_ASYM)
for D, r in zip(Ds, ratios):
    print(f"D={D}: source/sink rigorous lower ratio >= {float(r):.12e}")
for D in Ds:
    print(
        f"D={D}: terminal E1/E0_asym upper proxy <= "
        f"{terminal_energy_ratio_upper(D):.12e}"
    )
