from fractions import Fraction as F

k = F(989, 20000)
old = F(80, 59049)
checks = {
    "sqrt101_certificate_margin": 1990**2 - 198**2*101,
    "kappa_gt_4_81": k - F(4,81),
    "W0": (1-9*k)*k*k,
    "W0_improves_old": (1-9*k)*k*k-old,
}
for name, value in checks.items():
    print(name, value)
assert checks["sqrt101_certificate_margin"] == 496
assert checks["kappa_gt_4_81"] > 0
assert checks["W0"] == F(10856164979,8000000000000)
assert checks["W0_improves_old"] > 0
