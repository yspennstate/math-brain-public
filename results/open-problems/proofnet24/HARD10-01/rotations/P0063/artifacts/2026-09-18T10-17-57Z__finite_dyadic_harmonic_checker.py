from fractions import Fraction
from functools import lru_cache


def cantor_cdf(x):
    """Exact Cantor-Lebesgue CDF at rational x in [0,1]."""
    x = Fraction(x)
    if x <= 0:
        return Fraction(0)
    if x >= 1:
        return Fraction(1)

    r = x
    value = Fraction(0)
    weight = Fraction(1, 2)
    # state is remainder before taking next ternary digit.
    seen = {}
    step = 0
    while True:
        if r in seen:
            old_step, old_value, old_weight = seen[r]
            # The ternary remainder has repeated with only digits 0/2 seen.
            # Hence the binary digit block repeats. Sum the geometric tail.
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
            # Cantor function is constant across the removed middle-third gap.
            return value + weight
        else:
            raise AssertionError("unexpected ternary digit")

        if r == 0:
            return value
        weight /= 2
        step += 1


def cantor_ceiling(x):
    """Smallest point of middle-thirds Cantor set E that is >= rational x."""
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
            # Ternary expansion is eventually periodic using only 0 and 2.
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


def intersects_cantor(n, k):
    a, b = dyadic_interval(n, k)
    return cantor_ceiling(a) <= b


def cantor_mass(n, k):
    a, b = dyadic_interval(n, k)
    return cantor_cdf(b) - cantor_cdf(a)


def branch_conductance(C):
    # C=None represents an infinite conductance sink at the wired cutoff.
    return Fraction(1) if C is None else C / (1 + C)


@lru_cache(None)
def truncated_effective_conductance(n, k, radius):
    """
    Effective conductance from dyadic vertex (n,k) to a wired boundary
    radius levels below it in the exact coding tree T_[2](E), unit edge
    conductances. radius=0 is the wired sink.
    """
    assert intersects_cantor(n, k)
    if radius == 0:
        return None
    total = Fraction(0)
    for child_k in (2 * k, 2 * k + 1):
        if intersects_cantor(n + 1, child_k):
            child_C = truncated_effective_conductance(n + 1, child_k, radius - 1)
            total += branch_conductance(child_C)
    return total


def truncated_child_split(parent_n, parent_k, radius):
    """
    Current split at parent between its two children when descendants are
    truncated/wired radius levels below the children.
    """
    children = []
    for child_k in (2 * parent_k, 2 * parent_k + 1):
        assert intersects_cantor(parent_n + 1, child_k)
        C = truncated_effective_conductance(parent_n + 1, child_k, radius)
        children.append(branch_conductance(C))
    return children[0] / (children[0] + children[1])


# Basic exact tree counts, matching the maximal coding-tree definition.
expected_counts = {1: 2, 2: 4, 3: 6, 4: 10, 5: 16, 6: 28, 7: 42, 8: 70, 9: 102}
for n, expected in expected_counts.items():
    got = sum(intersects_cantor(n, k) for k in range(2**n))
    assert got == expected, (n, got, expected)

# The parent I_4^7 has two children I_8^8 and I_9^8.
assert cantor_mass(7, 4) == Fraction(1, 32)
assert cantor_mass(8, 8) == Fraction(1, 64)
assert cantor_mass(8, 9) == Fraction(1, 64)
q = cantor_mass(8, 8) / cantor_mass(7, 4)
assert q == Fraction(1, 2)

rows = []
for radius in range(1, 9):
    CA = truncated_effective_conductance(8, 8, radius)
    CB = truncated_effective_conductance(8, 9, radius)
    assert CA > CB
    p = truncated_child_split(7, 4, radius)
    assert p > Fraction(1, 2)
    rows.append((radius, CA, CB, p, p - Fraction(1, 2)))

print("EXACT_CHECK_PASS")
print("coding_tree_counts_n1_to_n9 =", [expected_counts[n] for n in range(1, 10)])
print("nu3_parent_mass =", cantor_mass(7, 4))
print("nu3_child_masses =", cantor_mass(8, 8), cantor_mass(8, 9))
print("nu3_conditional_split =", q)
for radius, CA, CB, p, diff in rows[:6]:
    print(f"r={radius}: C_A={CA}, C_B={CB}, p_trunc={p}, p_trunc-1/2={diff}")
print("verified_strict_truncated_asymmetry_for_radii_1_through_8 = True")
print("IMPORTANT: finite wired truncation only; no claim that the infinite-tree split differs from 1/2.")
