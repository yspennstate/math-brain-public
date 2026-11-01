from fractions import Fraction

# Exact finite-core certification for the alpha0 = 43/5 WARM whisker bound.
alpha0 = Fraction(43, 5)
d0 = Fraction(46, 125)

# delta(alpha0)=(1-sqrt(3/43))/2 < d0 iff sqrt(3/43)>33/125.
delta_dom_lhs = 3 * 125**2
delta_dom_rhs = 43 * 33**2
assert delta_dom_lhs > delta_dom_rhs
assert delta_dom_lhs - delta_dom_rhs == 48

# Critical point s*=(120-9 sqrt(87))/215 lies in (1/6,21/125).
lower_gap = 505**2 - 54**2 * 87
upper_gap = 1125**2 * 87 - 10485**2
assert lower_gap > 0
assert upper_gap > 0
assert lower_gap == 1333
assert upper_gap == 174150

# The rational envelope at the critical point is bounded by
# (21/104)*(901/750)^(43/5). Raise to the fifth power.
lhs = 21**5 * 901**43
rhs = 104**5 * 750**43
assert lhs < rhs

# Endpoint s=d0 gives an even smaller value:
# R(d0) = d0/(1-d0) because 1+d0-d0=1.
endpoint = d0 / (1-d0)
assert endpoint == Fraction(46, 79)
assert endpoint < 1

print("PASS")
print("alpha0 = 43/5")
print("d0 = 46/125")
print("delta0<d0 square-gap =", delta_dom_lhs - delta_dom_rhs)
print("s*>1/6 square-gap =", lower_gap)
print("s*<21/125 square-gap =", upper_gap)
print("critical-envelope fifth-power integer comparison =", lhs < rhs)
print("critical-envelope integer gap =", rhs-lhs)
print("endpoint R(d0) =", endpoint)
