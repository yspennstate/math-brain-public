from fractions import Fraction

# Stable centre under the current LIMIT-PRIME-GATE-LIFT-v1 candidate.
C = Fraction(65218512, 10_000_000)

# Peer-certified upward entropy bounds from fleet01/B17's complete balanced
# five-bit certificate. B>=30 is treated by H<=5 at the smallest such I.
ENTROPY_UPPER = {
    22: Fraction(1701237775599294, 10**15),
    24: Fraction(3, 1),
    26: Fraction(3716917186688700, 10**15),
    28: Fraction(3912687890016525, 10**15),
    30: Fraction(5, 1),
}


def ln_atanh_bounds(y: Fraction, terms: int = 120):
    """Rigorous rational enclosure for ln(y), 1 <= y <= 2.

    ln y = 2 sum_{n>=0} z^(2n+1)/(2n+1), z=(y-1)/(y+1).
    Every term is nonnegative.  The tail is bounded by replacing each
    denominator by the first omitted denominator and summing the geometric
    series.
    """
    y = Fraction(y)
    assert Fraction(1) <= y <= Fraction(2)
    z = (y - 1) / (y + 1)
    zz = z * z
    s = Fraction(0)
    zpow = z
    for n in range(terms):
        s += zpow / (2 * n + 1)
        zpow *= zz
    lo = 2 * s
    if z == 0:
        return lo, lo
    rem = 2 * zpow / Fraction(2 * terms + 1) / (1 - zz)
    return lo, lo + rem


def ln_bounds(x: Fraction, terms: int = 120):
    """Rigorous rational enclosure for ln(x), x>0, by powers-of-two reduction."""
    x = Fraction(x)
    assert x > 0
    e = 0
    y = x
    while y >= 2:
        y /= 2
        e += 1
    while y < 1:
        y *= 2
        e -= 1
    l2lo, l2hi = ln_atanh_bounds(Fraction(2), terms)
    ylo, yhi = ln_atanh_bounds(y, terms)
    if e >= 0:
        return ylo + e * l2lo, yhi + e * l2hi
    return ylo + e * l2hi, yhi + e * l2lo


LN2_LO, LN2_HI = ln_bounds(Fraction(2))


def h2_upper(p: Fraction):
    """Rigorous rational upper bound for binary entropy h_2(p)."""
    p = Fraction(p)
    if p == 0 or p == 1:
        return Fraction(0)
    _, a_hi = ln_bounds(1 / p)
    _, b_hi = ln_bounds(1 / (1 - p))
    numerator_hi = p * a_hi + (1 - p) * b_hi
    return numerator_hi / LN2_LO


# Step 1: the exact child-slack gap supplied by the peer envelope.
slacks = {}
for B, Hup in ENTROPY_UPPER.items():
    I_minus_1 = Fraction(B - 16, 16)
    slacks[B] = C * I_minus_1 - Hup

s0 = min(slacks.values())
assert s0 == Fraction(326157, 1_250_000)  # 0.2609256, attained at B=24

# Step 2: every possible disagreement probability for two functions on Q_5.
# JS <= 2 delta / ln 2 and H(J|S) <= h_2(delta), so the debit is bounded by
# h_2(delta) + (2/ln2-C) delta.  Use an upper bound throughout.
penalties = []
for k in range(1, 33):
    delta = Fraction(k, 32)
    debit_hi = h2_upper(delta) + 2 * delta / LN2_LO - C * delta
    penalties.append((debit_hi, k))

penalty_max, worst_k = max(penalties)
eta = s0 / 2 - penalty_max
literal_distinct_margin = C / 2 - 2

print("C_star=", float(C))
print("ln2_interval_width=", float(LN2_HI - LN2_LO))
print("child_slack_lower_bounds=", {B: float(v) for B, v in slacks.items()})
print("s0=", float(s0))
print("worst_delta_k=", worst_k)
print("worst_delta=", worst_k / 32)
print("information_debit_upper=", float(penalty_max))
print("two_generation_margin_lower=", float(eta))
print("distinct_literal_margin=", float(literal_distinct_margin))

assert worst_k == 2
assert penalty_max < Fraction(110012, 1_000_000)
assert eta > Fraction(2045, 100_000)  # > 0.02045
assert literal_distinct_margin > 1
print("PASS=True")
