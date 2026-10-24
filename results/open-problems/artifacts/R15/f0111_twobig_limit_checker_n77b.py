from fractions import Fraction as F


def exp_bounds(x, N=18):
    """Exact rational lower/upper bounds for exp(x), x>=0.

    The upper tail uses that from term N+1 onward every successive
    term ratio is at most x/(N+2).
    """
    assert x >= 0
    s = F(1)
    term = F(1)
    for n in range(1, N + 1):
        term *= x / n
        s += term
    first = term * x / (N + 1)
    ratio = x / (N + 2)
    assert ratio < 1
    tail = first / (1 - ratio)
    return s, s + tail


tests = {}

# Elementary logarithm bounds used in the analytic proof.
e07_lo, e07_hi = exp_bounds(F(7, 10))
tests["ln2_lt_7_10"] = e07_lo > 2

e069_lo, e069_hi = exp_bounds(F(69, 100))
tests["ln2_gt_69_100"] = e069_hi < 2

e109_lo, e109_hi = exp_bounds(F(109, 100))
tests["ln3_gt_109_100"] = e109_hi < 3

# beta = (ln 3 - (4/3) ln 2)/(ln 2)^2 > 2/9 follows from
# 9 ln 3 - 12 ln 2 - 2 (ln 2)^2 > 0.  The rational bounds above
# leave the following strictly positive lower margin.
beta_margin_surrogate = (
    9 * F(109, 100) - 12 * F(7, 10) - 2 * F(7, 10) ** 2
)
tests["beta_gt_2_9_surrogate"] = beta_margin_surrogate > 0

# In the interior-minimizer branch the atanh lower bound reduces the
# envelope derivative to a positive multiple of
# P(x)=576x^5+637x^4+129x^3-459x^2+155x+42, x in [1/2,1].
# The proof lower-bounds P by the concave quadratic
# Q(x)=-(653/4)x^2+155x+42, so checking its endpoints is exact.
Q1 = -F(653, 4) + 155 + 42
Qhalf = -F(653, 4) * F(1, 4) + 155 * F(1, 2) + 42
tests["Q1_pos"] = Q1 > 0
tests["Qhalf_pos"] = Qhalf > 0

# Exact rational lower bounds at s=7/2 for the boundary-y=0 branch.
Lprime35_lb = F(71, 180) - F(4, 9) * F(7, 10)
L35_lb = F(69, 50) - F(203, 90) + F(637, 720)
tests["Lprime35_pos"] = Lprime35_lb > 0
tests["L35_pos"] = L35_lb > 0

# The r=1 branch uses that f'(y)=0 exactly when
# 8 t^2 - 17 t + 2=0, t=e^y; the roots are 1/8 and 2, hence the
# unique admissible critical point t>=1 is t=2.
tests["fprime_roots"] = (
    8 * F(2) ** 2 - 17 * F(2) + 2 == 0
    and 8 * F(1, 8) ** 2 - 17 * F(1, 8) + 2 == 0
)

for key, value in tests.items():
    print(key, value)

print("exp_0.7_lower_minus_2 =", e07_lo - 2)
print("2_minus_exp_0.69_upper =", 2 - e069_hi)
print("3_minus_exp_1.09_upper =", 3 - e109_hi)
print("beta_margin_surrogate =", beta_margin_surrogate)
print("Q(1) =", Q1)
print("Q(1/2) =", Qhalf)
print("L'(7/2,0) lower =", Lprime35_lb)
print("L(7/2,0) lower =", L35_lb)

assert all(tests.values())
print("ALL_EXACT_CHECKS_PASS")
