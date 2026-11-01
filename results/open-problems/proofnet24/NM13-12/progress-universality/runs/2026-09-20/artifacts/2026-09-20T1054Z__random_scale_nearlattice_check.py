import math
from fractions import Fraction

mu2 = Fraction(7, 3)   # E S^2, S ~ Unif[1,2]
mu4 = Fraction(31, 5)  # E S^4


def fourth(sig):
    a = float(mu2)
    b = float(mu4)
    return (1 + 6 * a * sig**2 + 3 * b * sig**4) / (1 + a * sig**2) ** 2


def rho(m, sigma):
    return sigma / math.sqrt(1 + float(mu2) * sigma * sigma)


print("mu2", mu2)
print("mu4", mu4)
print("noise_kappa4", 3 * (float(mu4) - float(mu2) ** 2))
print("xi_fourth_sigma1", fourth(1.0))
assert abs(float(mu2) - 7 / 3) < 1e-15
assert abs(float(mu4) - 31 / 5) < 1e-15
assert 3 * (float(mu4) - float(mu2) ** 2) > 0
assert fourth(1.0) < 3.0240000001

for q in (1, 2, 5, 10):
    # q-fold density lower bound at the all-R=+1 component center,
    # with b=2 and D>=1: ||f^{*q}||_inf >= c_q / sigma.
    c_q = (2.0 ** (-q)) / (2.0 * math.sqrt(2 * math.pi * q))
    print("conv_lower_const_q", q, c_q)
    assert c_q > 0

for m in (10**6, 10**9, 10**12):
    sigma = m ** (-1 / 3)
    rr = rho(m, sigma)
    vn1 = m * rr * rr / math.log(math.e / rr)
    k = m ** 0.4
    vn2 = k * (math.log(m) + math.log(math.e / rr)) / m

    sigma_crit = math.log(math.log(m)) * math.sqrt(math.log(m) / m)
    rrcrit = rho(m, sigma_crit)
    crit = m * rrcrit * rrcrit / math.log(math.e / rrcrit)

    print(
        "m",
        m,
        "sigma",
        sigma,
        "rho",
        rr,
        "VN1_ratio",
        vn1,
        "VN2_test",
        vn2,
        "nearcrit_sigma",
        sigma_crit,
        "nearcrit_ratio",
        crit,
    )
    assert vn1 > 1
    assert vn2 < 0.01
    assert crit > 1

# For S~Unif[1,2], the fourth moment is increasing in sigma^2 because
# E S^4 > (E S^2)^2. The grid is only a sanity check of the closed formula.
grid = [fourth(j / 10000) for j in range(10001)]
print("grid_fourth_max", max(grid))
assert max(grid) <= fourth(1.0) + 1e-12

# Uniform fixed-scale anti-concentration from the symmetrization/Paley-Zygmund lemma.
B = fourth(1.0)
Qbound = math.sqrt(1 - 1 / (2 * B + 6))
print("Q_half_bound", Qbound)
assert Qbound < 1

print("ALL_RANDOM_SCALE_NEARLATTICE_CHECKS_PASS")
