from fractions import Fraction as F
from math import factorial

# Exact arithmetic certificate for the endpoint used in REPORT.md.
# No floating-point sign decision is used.

def ln_lower_gt1(r, n):
    assert r > 1
    z = (r - 1) / (r + 1)
    z2 = z * z
    term = z
    s = F(0)
    for k in range(n):
        s += term / F(2 * k + 1)
        term *= z2
    return 2 * s


def ln_upper_gt1(r, n):
    assert r > 1
    z = (r - 1) / (r + 1)
    lo = ln_lower_gt1(r, n)
    # Positive-tail bound for 2*sum z^(2k+1)/(2k+1), k>=n.
    rem = 2 * z ** (2 * n + 1) / F(2 * n + 1) / (1 - z * z)
    return lo + rem


# ln 2 = 2*sum_{k>=0} 1/((2k+1)3^(2k+1)).
ln2_lb = sum(F(2, (2 * k + 1) * 3 ** (2 * k + 1)) for k in range(3))
assert ln2_lb > F(693, 1000)

# Prove 2^(-6.52) < 109/10000 without transcendental floating point.
y = F(52, 100) * F(693, 1000)
exp_lb = sum(y ** k / F(factorial(k)) for k in range(5))
assert F(64) * exp_lb > F(10000, 109)

x = F(109, 10000)
Z = 15 * x + 20 * x * x + 15 * x ** 3 + 6 * x ** 4 + x ** 5
assert Z < 1

w = F(83, 256)
q = 1 - w
r1 = F(6) / w
r2 = q / Z

# Natural-log numerator of
# w log_2(6/w) + q log_2(Z/q).
# First log is upper-bounded; the negative second log uses a lower bound.
N = 100
nat_upper = w * ln_upper_gt1(r1, N) - q * ln_lower_gt1(r2, N)
assert nat_upper < -F(3, 1000)

print('PASS=True')
print('ln2_lower=', float(ln2_lb))
print('64_exp_poly_lower=', float(F(64) * exp_lb))
print('required_exp_threshold=', float(F(10000, 109)))
print('x_upper=', float(x))
print('Z_upper=', float(Z))
print('endpoint_natural_log_upper=', float(nat_upper))
print('endpoint_bound_lt_minus_0.003=', nat_upper < -F(3, 1000))
print('conclusion_W1_strictly_gt=', '83/256')
print('quantized_conclusion_W1_ge=', '84/256 = 21/64')
