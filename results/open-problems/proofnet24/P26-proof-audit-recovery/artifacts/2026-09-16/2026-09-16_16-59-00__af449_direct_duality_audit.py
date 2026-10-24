from fractions import Fraction

# Independent exact-arithmetic audit for the algebraic finite core of
# C31's Aldous-Fill Open Problem 4.49(ii) Ramanujan-cone construction.

historical = Fraction(2326533, 1125826)
assert historical > 2
assert historical - 2 == Fraction(74881, 1125826)


def lower_ratio(s: int) -> Fraction:
    assert s >= 4
    d = s * s
    r = s
    # F lower bound / (D * tau_rel upper bound), with D=2 and
    # tau_rel < 1/(1-2s/(s^2+1)).
    F = Fraction(r * (d + 1) * (d + 3), (d + 2) * (d + r))
    gap_factor = Fraction((s - 1) ** 2, s * s + 1)
    return F * gap_factor / 2


def closed_form(s: int) -> Fraction:
    return Fraction((s - 1) ** 2 * (s * s + 3), 2 * (s + 1) * (s * s + 2))


def positive_remainder(s: int) -> Fraction:
    return Fraction(5 * s * s - 2 * s + 9, 2 * (s + 1) * (s * s + 2))


samples = [4, 7, 8, 16, 32, 64, 128]
print("P26 independent AF4.49(ii) exact audit")
print(f"historical_ratio={historical} ~= {float(historical):.12f}")
print(f"historical_excess_over_2={historical - 2}")
for s in samples:
    lhs = lower_ratio(s)
    cf = closed_form(s)
    assert lhs == cf
    rem = lhs - Fraction(s - 3, 2)
    assert rem == positive_remainder(s)
    assert rem > 0
    print(f"s={s} lower_ratio={lhs} ~= {float(lhs):.12f}; remainder={rem}")

assert lower_ratio(64) == Fraction(5422977, 177580)
print("s=64_exact_match=5422977/177580")
print("IDENTITY: L_s-(s-3)/2=(5s^2-2s+9)/(2(s+1)(s^2+2)) > 0")
print("ALL_EXACT_CHECKS_PASS")
