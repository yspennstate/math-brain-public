from fractions import Fraction

# Exact self-check for the explicit d=2 two-type i.i.d. RWRE example used in
# NM13-12's P0483 report. Transition order: +e1, -e1, +e2, -e2.

p_plus = [Fraction(2, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5)]
p_minus = [Fraction(1, 5), Fraction(3, 10), Fraction(1, 4), Fraction(1, 4)]
theta = Fraction(3, 5)
ell_dot = [1, -1, 0, 0]

assert sum(p_plus) == 1
assert sum(p_minus) == 1
kappa = min(p_plus + p_minus)
assert kappa == Fraction(1, 5)

d_plus = sum(p * a for p, a in zip(p_plus, ell_dot))
d_minus = sum(p * a for p, a in zip(p_minus, ell_dot))
assert d_plus == Fraction(1, 5)
assert d_minus == Fraction(-1, 10)

ratios = [a / b for a, b in zip(p_plus, p_minus)]
R = max(ratios)
assert ratios == [Fraction(2, 1), Fraction(2, 3), Fraction(4, 5), Fraction(4, 5)]
assert R == 2

# Robust lower bound furnished by the two-type Kalikow calculation:
# delta_two(theta) = [theta*d_plus + (1-theta)*d_minus*R]
#                    / [theta + (1-theta)*R].
delta_two = (theta * d_plus + (1 - theta) * d_minus * R) / (
    theta + (1 - theta) * R
)
assert delta_two == Fraction(1, 35)

mean_drift = theta * d_plus + (1 - theta) * d_minus
assert mean_drift == Fraction(2, 25)

# For a symbolic type probability t, the same expression simplifies to
#   delta_two(t) = (2*t - 1)/(5*(2 - t)),
# and the denominator is positive on 0 <= t <= 1.  Hence this certified
# family satisfies the sufficient Kalikow inequality exactly for t > 1/2.

print("p_plus =", p_plus)
print("p_minus =", p_minus)
print("kappa =", kappa)
print("d_plus =", d_plus)
print("d_minus =", d_minus)
print("ratios =", ratios)
print("R =", R)
print("theta =", theta)
print("delta_two =", delta_two)
print("mean_drift =", mean_drift)
print("symbolic_delta(theta) = (2*theta - 1)/(5*(2-theta))")
print("symbolic_positive_iff = theta > 1/2")
print("ALL_EXACT_CHECKS_PASS")
