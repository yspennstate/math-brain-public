from fractions import Fraction as F
from math import factorial


def kappa(d):
    return F(4, 1) / ((d + 3) * (1 - d * d))


def nu(d):
    return (d + 1) ** 2 / (2 * (1 - d) * (d + 3))


def ck(d):
    return F(29, 48) * (1 - d) * (1 + d) ** 3


def eta(d, N):
    return F(29, 8) * (1 + d) ** 3 - N


def V(d, N, C):
    x1 = (d * d + 4 * d + 7) / (2 * (d + 1) * (d + 3))
    return F(29, 4) * (d + 3) * (1 - d * d) * (x1 + C) - (28 - N)


def mu(d, N):
    return (N * (1 - d * d) + d * d + 4 * d + 7) / (4 * (d + 1) * (d + 3))


def require(name, condition, value=None):
    if not condition:
        raise AssertionError((name, value))
    print(name, "PASS", "" if value is None else value)


# e^(7/100) > 1 + 7/100 = 107/100.
require("exp_007_gt_107_100", F(107, 100) == 1 + F(7, 100))
# e^6 > the Taylor partial sum through degree 8 > 315, hence log 315 < 6.
taylor6 = sum(F(6 ** n, factorial(n)) for n in range(9))
require("exp6_taylor_gt_315", taylor6 > 315, taylor6)

# The derivative formulas written in the run report show kappa, nu and eta increasing,
# V and mu decreasing on both intervals; ck increases up to 1/2 and decreases after 1/2.
lo12, hi12 = F(49, 100), F(1, 2)
require("N12_kappa_lt_153_100", kappa(hi12) < F(153, 100), kappa(hi12))
require("N12_nu_lt_65_100", nu(hi12) < F(65, 100), nu(hi12))
require("N12_V_lt_290", V(lo12, 12, 15) < 290, V(lo12, 12, 15))
require("N12_mu_lt_89_100", mu(lo12, 12) < F(89, 100), mu(lo12, 12))
require("N12_ck_lt_102_100", ck(hi12) < F(102, 100), ck(hi12))
require("N12_eta_lt_24_100", eta(hi12, 12) < F(24, 100), eta(hi12, 12))

face12 = F(153, 100) * 289 / (29 * F(107, 100))
ebar12 = F(65, 100) * F(11, 2) * F(2, 100) ** 2
ksec12 = F(153, 100) / 29 * F(24, 100) * F(102, 100)
ej12 = F(7, 100) * F(89, 100) * 6
total12 = face12 + ebar12 + ksec12 + ej12
require("N12_face_lt_57_4", face12 < F(57, 4), face12)
require("N12_Ebar_lt_2e_3", ebar12 < F(2, 1000), ebar12)
require("N12_Ksec_lt_13e_3", ksec12 < F(13, 1000), ksec12)
require("N12_EJ_lt_374e_3", ej12 < F(374, 1000), ej12)
require("N12_total_lt_15", total12 < 15, total12)

lo13, hi13 = F(53, 100), F(27, 50)
require("N13_kappa_lt_8_5", kappa(hi13) < F(8, 5), kappa(hi13))
require("N13_nu_lt_73_100", nu(hi13) < F(73, 100), nu(hi13))
require("N13_V_lt_315", V(lo13, 13, 17) < 315, V(lo13, 13, 17))
require("N13_mu_lt_88_100", mu(lo13, 13) < F(88, 100), mu(lo13, 13))
require("N13_ck_lt_509_500", ck(lo13) < F(509, 500), ck(lo13))
require("N13_eta_lt_24_100", eta(hi13, 13) < F(24, 100), eta(hi13, 13))

face13 = F(8, 5) * 314 / (29 * F(107, 100))
ebar13 = F(73, 100) * 6 * F(18, 1000) ** 2
ksec13 = F(8, 5) / 29 * F(24, 100) * F(509, 500)
ej13 = F(7, 100) * F(88, 100) * 6
total13 = face13 + ebar13 + ksec13 + ej13
require("N13_face_lt_162_10", face13 < F(162, 10), face13)
require("N13_Ebar_lt_2e_3", ebar13 < F(2, 1000), ebar13)
require("N13_Ksec_lt_14e_3", ksec13 < F(14, 1000), ksec13)
require("N13_EJ_lt_370e_3", ej13 < F(370, 1000), ej13)
require("N13_total_lt_17", total13 < 17, total13)

print("ALL_EXACT_CHECKS_PASS")
