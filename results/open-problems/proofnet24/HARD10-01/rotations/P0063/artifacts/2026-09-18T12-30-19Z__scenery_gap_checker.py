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


def in_cantor_exact(x):
    x = Fraction(x)
    if x < 0 or x > 1:
        return False
    if x in (0, 1):
        return True
    r = x
    seen = set()
    while True:
        if r in seen:
            return True
        seen.add(r)
        y = 3*r
        digit = y.numerator // y.denominator
        r = y - digit
        if digit == 1:
            # A terminating 1 followed by zeros is a Cantor endpoint,
            # with the alternative ternary expansion ending in 2s.
            return r == 0
        if digit not in (0, 2):
            raise AssertionError("unexpected ternary digit")
        if r == 0:
            return True


def dyadic_interval(n, k):
    return Fraction(k, 2**n), Fraction(k+1, 2**n)


def cantor_mass(n, k):
    a,b = dyadic_interval(n,k)
    return cantor_cdf(b)-cantor_cdf(a)


def intersects_cantor(n,k):
    a,b=dyadic_interval(n,k)
    return cantor_ceiling(a) <= b


def branch_conductance(C):
    return Fraction(1) if C is None else C/(1+C)


@lru_cache(None)
def truncated_effective_conductance(n,k,radius):
    assert intersects_cantor(n,k)
    if radius == 0:
        return None
    total=Fraction(0)
    for ck in (2*k,2*k+1):
        if intersects_cantor(n+1,ck):
            total += branch_conductance(
                truncated_effective_conductance(n+1,ck,radius-1)
            )
    return total


def conditional_cantor_flow_energy_prefix(n0,k0,radius):
    m0=cantor_mass(n0,k0)
    assert m0>0
    current=[k0]
    cumulative=Fraction(0)
    for r in range(1,radius+1):
        n=n0+r
        nxt=[]
        level=Fraction(0)
        for pk in current:
            for ck in (2*pk,2*pk+1):
                cm=cantor_mass(n,ck)
                if cm>0:
                    nxt.append(ck)
                    level += (cm/m0)**2
        cumulative += level
        current=nxt
    return cumulative


# Base scenery: level-7 dyadic parent I_4^7 contains exactly
# the level-5 ternary cylinder [8/3^5, 9/3^5], whose ternary prefix is 00022.
u0 = Fraction(52,243)
r0 = Fraction(128,243)
assert r0 == Fraction(2**7,3**5)
assert Fraction(1,32) + u0*Fraction(1,128) == Fraction(8,243)
assert Fraction(1,32) + u0/Fraction(128,1) == Fraction(8,243)

left_margin_cyl_units = u0/r0
right_margin_cyl_units = (1-u0-r0)/r0
midpoint_in_cylinder = (Fraction(1,2)-u0)/r0
assert left_margin_cyl_units == Fraction(13,32) < 1
assert right_margin_cyl_units == Fraction(63,128) < 9
assert midpoint_in_cylinder == Fraction(139,256)
assert Fraction(1,3) < midpoint_in_cylinder < Fraction(2,3)

# Cantor-Lebesgue mass splits the two level-8 dyadic children equally.
assert cantor_mass(8,8) == Fraction(1,64)
assert cantor_mass(8,9) == Fraction(1,64)

# Recompute the strict effective-conductance certificate from the previous run.
left_energy_prefix = conditional_cantor_flow_energy_prefix(8,8,8)
assert left_energy_prefix == Fraction(955961,524288)
tail_upper = Fraction(384)*Fraction(2,3)**17
assert tail_upper == Fraction(16777216,43046721)
left_energy_upper = left_energy_prefix + tail_upper
left_branch_lower = Fraction(1,1)/(1+left_energy_upper)
assert left_branch_lower == Fraction(22568879259648,72515958735737)

right_C_wired_radius6 = truncated_effective_conductance(8,9,6)
assert right_C_wired_radius6 == Fraction(13703,31620)
right_branch_upper = right_C_wired_radius6/(1+right_C_wired_radius6)
assert right_branch_upper == Fraction(13703,45323)
assert left_branch_lower > right_branch_upper

# The finite right-wired topology through radius 6 below the right child
# only uses normalized dyadic boundaries through relative level 7.
# None of these boundaries lies on the base scaled Cantor copy u0+r0 E.
# Since E is compact and the boundary set is finite, this gives a positive
# topology-stability neighborhood around (u0,r0).
checked = 0
for ell in range(1,8):
    for j in range(1,2**ell):
        t = Fraction(j,2**ell)
        y = (t-u0)/r0
        if 0 <= y <= 1:
            checked += 1
            assert not in_cantor_exact(y), (ell,j,t,y)

split_lower = left_branch_lower/(left_branch_lower+right_branch_upper)
assert split_lower == Fraction(
    1022889314685026304,2016575497240830415
)
assert split_lower > Fraction(1,2)

print("EXACT_CHECK_PASS")
print("u0 =", u0)
print("r0 =", r0)
print("left_margin_cylinder_units =", left_margin_cyl_units)
print("right_margin_cylinder_units =", right_margin_cyl_units)
print("midpoint_relative_to_cylinder =", midpoint_in_cylinder)
print("finite_normalized_boundaries_checked =", checked)
print("left_branch_lower =", left_branch_lower)
print("right_branch_upper =", right_branch_upper)
print("split_lower =", split_lower)
