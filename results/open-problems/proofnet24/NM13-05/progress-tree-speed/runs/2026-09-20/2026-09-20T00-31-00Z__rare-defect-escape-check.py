from fractions import Fraction as F


def fmt(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


L = F(19, 10)
Q = (2 - L) * (2 - L / 2)
V = 3 - L / 3
a = 1 / Q - 1 / V
Rplus = (3 - L) * (4 - L) / ((9 - L) * (2 - L))
Rminus = 3 * (2 - L) / (3 - L) ** 2

small_prod = L * a * Rplus
small_ratio_threshold = 2 / small_prod
small_p_threshold = small_ratio_threshold / (1 + small_ratio_threshold)

large_prod = L * a / Rminus
large_q_threshold = 2 / large_prod
large_p_threshold = 1 / (1 + large_q_threshold)

p_small = F(1, 30)
small_mix_ratio = p_small / (1 - p_small)
small_num = 4 - 2 * small_prod * small_mix_ratio
den = (3 + L) ** 2
small_margin = small_num / den

p_large = F(35, 36)
large_mix_ratio = (1 - p_large) / p_large
large_num = 4 - 2 * large_prod * large_mix_ratio
large_margin = large_num / den

# Monotonicity certificates on [1,19/10].
# a'(lambda)=4(3-lambda)/((2-lambda)^2(4-lambda)^2)-3/(9-lambda)^2.
# The first term is >=22/45 and the second <=300/5041.
aprime_lower = F(22, 45) - F(300, 5041)


def rplus_quad(lam):
    # Rplus'(lambda) = -2*q(lambda)/((lambda-9)^2(lambda-2)^2).
    return 2 * lam * lam - 6 * lam - 3


checks = {
    "Q(19/10)": Q,
    "V(19/10)": V,
    "a(19/10)": a,
    "Rplus(19/10)": Rplus,
    "Rminus(19/10)": Rminus,
    "L*a*Rplus": small_prod,
    "small ratio threshold p/(1-p)": small_ratio_threshold,
    "small p sharp threshold": small_p_threshold,
    "L*a/Rminus": large_prod,
    "large ratio threshold (1-p)/p": large_q_threshold,
    "large p sharp threshold": large_p_threshold,
    "p=1/30 numerator": small_num,
    "p=1/30 derivative margin": small_margin,
    "p=35/36 numerator": large_num,
    "p=35/36 derivative margin": large_margin,
    "a' crude lower bound": aprime_lower,
    "Rplus derivative quadratic at 1": rplus_quad(F(1)),
    "Rplus derivative quadratic at 19/10": rplus_quad(L),
}

assert Q == F(21, 200)
assert V == F(71, 30)
assert a == F(13570, 1491)
assert Rplus == F(231, 71)
assert Rminus == F(30, 121)
assert small_prod == F(283613, 5041)
assert small_ratio_threshold == F(10082, 283613)
assert small_p_threshold == F(10082, 293695)
assert large_prod == F(3119743, 44730)
assert large_q_threshold == F(89460, 3119743)
assert large_p_threshold == F(3119743, 3209203)
assert small_num == F(17530, 146189)
assert small_margin == F(1753000, 350999789)
assert large_num == F(11357, 782775)
assert large_margin == F(45428, 75177711)
assert aprime_lower > 0
assert rplus_quad(F(1)) < 0 and rplus_quad(L) < 0
assert p_small < small_p_threshold
assert p_large > large_p_threshold

for key, value in checks.items():
    print(f"{key} = {fmt(value)} = {float(value):.15g}")
print("ALL_EXACT_CHECKS_PASS")
