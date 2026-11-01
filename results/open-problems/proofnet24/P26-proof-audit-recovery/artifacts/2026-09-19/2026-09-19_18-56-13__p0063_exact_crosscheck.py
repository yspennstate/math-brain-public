from fractions import Fraction
from functools import lru_cache


def cantor_F(x):
    """Exact Cantor-Lebesgue CDF via affine functional equations."""
    x = Fraction(x)
    if x <= 0:
        return Fraction(0)
    if x >= 1:
        return Fraction(1)
    state = x
    A, B = Fraction(0), Fraction(1)
    seen = {}
    while True:
        if state in seen:
            A0, B0 = seen[state]
            f_state = (A - A0) / (B0 - B)
            return A + B * f_state
        seen[state] = (A, B)
        if state < Fraction(1, 3):
            state *= 3
            B /= 2
        elif state > Fraction(2, 3):
            A += B / 2
            B /= 2
            state = 3 * state - 2
        else:
            return A + B / 2


def dyadic_mass(n, k):
    return cantor_F(Fraction(k + 1, 2**n)) - cantor_F(Fraction(k, 2**n))


@lru_cache(None)
def wired_positive_mass_subtree(n, k, radius):
    """Wired finite conductance after deleting zero-conductance singleton rays."""
    assert dyadic_mass(n, k) > 0
    if radius == 0:
        return None
    total = Fraction(0)
    for ck in (2 * k, 2 * k + 1):
        if dyadic_mass(n + 1, ck) > 0:
            C = wired_positive_mass_subtree(n + 1, ck, radius - 1)
            total += Fraction(1) if C is None else C / (1 + C)
    return total


def conditional_flow_energy(n0, k0, radius):
    m0 = dyadic_mass(n0, k0)
    current = {k0}
    total = Fraction(0)
    for rr in range(1, radius + 1):
        n = n0 + rr
        nxt = set()
        level = Fraction(0)
        for pk in current:
            for ck in (2 * pk, 2 * pk + 1):
                m = dyadic_mass(n, ck)
                if m > 0:
                    nxt.add(ck)
                    level += (m / m0) ** 2
        total += level
        current = nxt
    return total


def in_cantor(x):
    """Exact rational membership test, allowing the endpoint alternative expansion."""
    x = Fraction(x)
    if x < 0 or x > 1:
        return False
    if x in (0, 1):
        return True
    seen = set()
    r = x
    while True:
        if r in seen:
            return True
        seen.add(r)
        y = 3 * r
        digit = y.numerator // y.denominator
        r = y - digit
        if digit == 1:
            return r == 0
        if digit not in (0, 2):
            return False
        if r == 0:
            return True


u0 = Fraction(52, 243)
r0 = Fraction(128, 243)
assert dyadic_mass(8, 8) == dyadic_mass(8, 9) == Fraction(1, 64)
assert u0 / r0 == Fraction(13, 32)
assert (1 - u0 - r0) / r0 == Fraction(63, 128)
assert (Fraction(1, 2) - u0) / r0 == Fraction(139, 256)

left_energy_prefix = conditional_flow_energy(8, 8, 8)
assert left_energy_prefix == Fraction(955961, 524288)
tail_upper = Fraction(384) * Fraction(2, 3) ** 17
assert tail_upper == Fraction(16777216, 43046721)
left_branch_lower = Fraction(1) / (1 + left_energy_prefix + tail_upper)
assert left_branch_lower == Fraction(22568879259648, 72515958735737)

right_wired_descendant = wired_positive_mass_subtree(8, 9, 6)
assert right_wired_descendant == Fraction(13703, 31620)
right_branch_upper = right_wired_descendant / (1 + right_wired_descendant)
assert right_branch_upper == Fraction(13703, 45323)

split_lower = left_branch_lower / (left_branch_lower + right_branch_upper)
assert split_lower == Fraction(1022889314685026304, 2016575497240830415)
assert split_lower > Fraction(1, 2)

checked = 0
for ell in range(1, 8):
    for j in range(1, 2**ell):
        y = (Fraction(j, 2**ell) - u0) / r0
        if 0 <= y <= 1:
            checked += 1
            assert not in_cantor(y)
assert checked == 133

# Independent finite sanity-check of the suffix-22 isolation formulas.
for m in range(2, 13):
    for address in range(2**m):
        if address & 3 != 3:
            continue
        bits = [(address >> (m - 1 - i)) & 1 for i in range(m)]
        num = sum(2 * bits[i] * 3 ** (m - 1 - i) for i in range(m))
        if address > 0:
            prev = [((address - 1) >> (m - 1 - i)) & 1 for i in range(m)]
            prev_num = sum(2 * prev[i] * 3 ** (m - 1 - i) for i in range(m))
            assert num - prev_num - 1 == 1
        if address < 2**m - 1:
            nxt = [((address + 1) >> (m - 1 - i)) & 1 for i in range(m)]
            nxt_num = sum(2 * nxt[i] * 3 ** (m - 1 - i) for i in range(m))
            assert nxt_num - num - 1 >= 9

print("P26_P0063_EXACT_CROSSCHECK_PASS")
print("left_mass =", dyadic_mass(8, 8), "right_mass =", dyadic_mass(8, 9))
print("left_energy_prefix =", left_energy_prefix)
print("tail_upper =", tail_upper)
print("left_branch_lower =", left_branch_lower)
print("right_wired_descendant =", right_wired_descendant)
print("right_branch_upper =", right_branch_upper)
print("split_lower =", split_lower)
print("split_excess =", split_lower - Fraction(1, 2))
print("finite_boundaries_checked =", checked)
print("suffix22_gap_exhaustive_through_m = 12")
