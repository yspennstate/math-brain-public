from math import sqrt, e

# Exact rational comparison proving 1/sqrt(5) < 715/1597.
assert 1597**2 < 5*715**2

kappa = 19/1000
Z = kappa**6
double_anchor = Z/3
nested_anchor = Z/12
Dprime = 9*sqrt(3*e)/kappa

assert 19**6 == 47045881
assert Dprime < 1353

print({
    "1597_sq": 1597**2,
    "5_times_715_sq": 5*715**2,
    "kappa_conservative": kappa,
    "Z_lower": Z,
    "double_anchor_lower": double_anchor,
    "nested_anchor_lower": nested_anchor,
    "Dprime_bound": Dprime,
    "Dprime_bound_lt_1353": Dprime < 1353,
})
