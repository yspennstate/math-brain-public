from fractions import Fraction
from functools import lru_cache


def cantor_cdf(x):
    x = Fraction(x)
    if x <= 0:
        return Fraction(0)
    if x >= 1:
        return Fraction(1)

    r = x
    value = Fraction(0)
    weight = Fraction(1, 2)
    seen = {}
    step = 0
    while True:
        if r in seen:
            old_step, old_value, old_weight = seen[r]
            ratio = weight / old_weight
            cycle_gain = value - old_value
            return old_value + cycle_gain / (1 - ratio)
        seen[r] = (step, value, weight)

        y = 3 * r
        digit = y.numerator // y.denominator
        r = y - digit
        if digit == 0:
            pass
        elif digit == 2:
            value += weight
        elif digit == 1:
            return value + weight
        else:
            raise AssertionError("unexpected ternary digit")

        if r == 0:
            return value
        weight /= 2
        step += 1


def cantor_ceiling(x):
    x = Fraction(x)
    if x <= 0:
        return Fraction(0)
    if x >= 1:
        return Fraction(1)

    r = x
    prefix = Fraction(0)
    seen = set()
    j = 1
    while True:
        if r in seen:
            return x
        seen.add(r)
        y = 3 * r
        digit = y.numerator // y.denominator
        r = y - digit
        if digit == 0:
            pass
        elif digit == 2:
            prefix += Fraction(2, 3**j)
        elif digit == 1:
            return prefix + Fraction(2, 3**j)
        else:
            raise AssertionError("unexpected ternary digit")
        if r == 0:
            return x
        j += 1


def dyadic_interval(n, k):
    return Fraction(k, 2**n), Fraction(k + 1, 2**n)


def cantor_mass(n, k):
    a, b = dyadic_interval(n, k)
    return cantor_cdf(b) - cantor_cdf(a)


def intersects_cantor(n, k):
    a, b = dyadic_interval(n, k)
    return cantor_ceiling(a) <= b


def branch_conductance(C):
    # C=None denotes the wired sink at the finite cutoff.
    return Fraction(1) if C is None else C / (1 + C)


@lru_cache(None)
def truncated_effective_conductance(n, k, radius):
    assert intersects_cantor(n, k)
    if radius == 0:
        return None
    total = Fraction(0)
    for child_k in (2 * k, 2 * k + 1):
        if intersects_cantor(n + 1, child_k):
            child_C = truncated_effective_conductance(n + 1, child_k, radius - 1)
            total += branch_conductance(child_C)
    return total


def conditional_cantor_flow_energy_prefix(n0, k0, radius):
    """Exact energy of the conditional Cantor flow through the first radius levels below (n0,k0)."""
    m0 = cantor_mass(n0, k0)
    assert m0 > 0
    current = [(k0, m0)]
    cumulative = Fraction(0)
    for r in range(1, radius + 1):
        n = n0 + r
        nxt = []
        level_energy = Fraction(0)
        for parent_k, _ in current:
            for child_k in (2 * parent_k, 2 * parent_k + 1):
                cm = cantor_mass(n, child_k)
                if cm > 0:
                    nxt.append((child_k, cm))
                    level_energy += (cm / m0) ** 2
        cumulative += level_energy
        current = nxt
    return cumulative


# The source-valid asymmetric dyadic split from the prior run.
assert cantor_mass(8, 8) == Fraction(1, 64)
assert cantor_mass(8, 9) == Fraction(1, 64)

# Exact conditional-Cantor-flow energy through eight descendant levels of I_8^8.
left_energy_prefix = conditional_cantor_flow_energy_prefix(8, 8, 8)
assert left_energy_prefix == Fraction(955961, 524288)

# Elementary rational checks used in the paper proof of q=2^{-d}<2/3,
# where d=log_3(2): 3^3<2^5 gives d>3/5, and 3^5<2^8 gives
# 2^{-3/5}<2/3.
assert 3**3 < 2**5
assert 3**5 < 2**8

# The proved Frostman estimate nu_3(J)<=2|J|^d implies, for descendant
# depth r>=9 below a level-8 cell of mass 1/64,
# S_r <= 128 q^{8+r} < 128(2/3)^{8+r}.
# Summing the geometric tail gives the following exact rational upper bound.
tail_upper = Fraction(384) * Fraction(2, 3) ** 17
assert tail_upper == Fraction(16777216, 43046721)

left_energy_upper = left_energy_prefix + tail_upper
assert left_energy_upper == Fraction(49947079476089, 22568879259648)

# Thomson: R_eff(I_8^8) <= left_energy_upper. After the parent edge,
# branch conductance is at least 1/(1+left_energy_upper).
left_branch_lower = Fraction(1, 1) / (1 + left_energy_upper)
assert left_branch_lower == Fraction(22568879259648, 72515958735737)

# Rayleigh/exhaustion: the infinite effective conductance below I_9^8 is at
# most every finite wired conductance. Radius 6 is already enough.
right_C_wired_radius6 = truncated_effective_conductance(8, 9, 6)
assert right_C_wired_radius6 == Fraction(13703, 31620)
right_branch_upper = right_C_wired_radius6 / (1 + right_C_wired_radius6)
assert right_branch_upper == Fraction(13703, 45323)

assert left_branch_lower > right_branch_upper

# Therefore the true infinite harmonic current split at parent I_4^7 is
# strictly larger than 1/2. The following is a rigorous lower bound obtained
# from the branch bounds above.
left_split_lower = left_branch_lower / (left_branch_lower + right_branch_upper)
assert left_split_lower > Fraction(1, 2)
assert left_split_lower == Fraction(1022889314685026304, 2016575497240830415)
assert left_split_lower - Fraction(1, 2) == Fraction(29203132129222193, 4033150994481660830)

print("EXACT_CHECK_PASS")
print("left_energy_prefix_r1_to_r8 =", left_energy_prefix)
print("frostman_tail_upper_r_ge_9 =", tail_upper)
print("left_energy_total_upper =", left_energy_upper)
print("left_branch_conductance_lower =", left_branch_lower)
print("right_C_wired_radius6 =", right_C_wired_radius6)
print("right_branch_conductance_upper =", right_branch_upper)
print("infinite_harmonic_left_split_lower =", left_split_lower)
print("split_excess_lower =", left_split_lower - Fraction(1, 2))
