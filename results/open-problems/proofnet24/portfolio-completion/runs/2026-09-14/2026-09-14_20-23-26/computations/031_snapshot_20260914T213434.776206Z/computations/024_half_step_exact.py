"""Exact certificates for the independently audited half-step QSO rate.

Run with Python 3. No external dependencies or floating-point arithmetic.
The polynomial checks certify identities; inequalities for all real inputs
are established analytically in agents/024.md, not by sampling.
"""

from fractions import Fraction as F


def add(*terms):
    result = {}
    for term in terms:
        for monomial, coefficient in term.items():
            result[monomial] = result.get(monomial, F(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in result.items()
            if coefficient}


def scale(term, factor):
    return {monomial: factor * coefficient
            for monomial, coefficient in term.items() if factor * coefficient}


def multiply(left, right):
    result = {}
    for (a, b), coefficient_left in left.items():
        for (c, d), coefficient_right in right.items():
            monomial = (a + c, b + d)
            result[monomial] = (result.get(monomial, F(0))
                                + coefficient_left * coefficient_right)
    return {monomial: coefficient for monomial, coefficient in result.items()
            if coefficient}


one = {(0, 0): F(1)}
s = {(1, 0): F(1)}
v = {(0, 1): F(1)}
one_minus_s = add(one, scale(s, F(-1)))
v_endpoint = multiply(one_minus_s, one_minus_s)
y = scale(add(s, v), F(1, 2))
one_minus_y = add(one, scale(y, F(-1)))
cap_bound = add(scale(y, F(1, 2)),
                scale(multiply(one_minus_y, one_minus_y), F(1, 2)),
                scale(add(v_endpoint, scale(v, F(-1))), F(-1, 8)))
cap_target = scale(add(scale(one, F(3)),
                       multiply(add(scale(s, F(2)), scale(one, F(-1))), v),
                       multiply(v, v)), F(1, 8))
assert cap_bound == cap_target

endpoint_actual = scale(add(
    scale(one, F(3)),
    multiply(add(scale(s, F(2)), scale(one, F(-1))), v_endpoint),
    multiply(v_endpoint, v_endpoint)), F(1, 8))
endpoint_target = scale(add(scale(one, F(3)),
                            multiply(multiply(s, s), v_endpoint)), F(1, 8))
assert endpoint_actual == endpoint_target

q = F(49, 128)
d = 1 - 2 * q
epsilon = d * d / 2
rate = 1 - epsilon
theta_endpoint = epsilon / (d - 2 * epsilon) ** 2
overlap_endpoint = (d - epsilon) * (1 - theta_endpoint)
overlap_margin = overlap_endpoint - epsilon
cut_bound = F(1, 2) + q

assert d == F(15, 64)
assert epsilon == F(225, 8192)
assert F(0) < epsilon < d / 2
assert d - 2 * epsilon == F(735, 4096)
assert d - epsilon == F(1695, 8192)
assert theta_endpoint == F(2048, 2401) < 1
assert 1 - theta_endpoint == F(353, 2401)
assert overlap_endpoint == F(598335, 19668992)
assert overlap_margin == F(29055, 9834496) > 0
assert cut_bound == F(113, 128)
assert rate == F(7967, 8192)
assert max(cut_bound, 1 - epsilon) == rate < 1
assert rate - cut_bound == F(735, 8192) > 0
assert (F(3) + F(1, 16)) / 8 == q

print("All exact polynomial identities and constant comparisons passed.")
for name in ("q", "d", "epsilon", "theta_endpoint", "overlap_endpoint",
             "overlap_margin", "cut_bound", "rate"):
    print(f"{name} = {globals()[name]}")
