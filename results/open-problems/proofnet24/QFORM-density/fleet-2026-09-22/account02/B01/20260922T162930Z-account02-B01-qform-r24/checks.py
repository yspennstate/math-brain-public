from fractions import Fraction
from math import pi, e, sqrt

EPS = Fraction(1, 4)

for m in (4, 10, 100, 1000):
    assert m % 2 == 0
    w_heavy_cloud = (1 - EPS) / m
    w_opp_cloud = 4 * EPS / (m * m)
    total = m * w_heavy_cloud + (m // 2) ** 2 * w_opp_cloud
    assert total == 1

    c_heavy = 1 - EPS
    c_cloud = (1 + EPS) / m
    assert c_heavy + m * c_cloud == 2

    Wbar_heavy_cloud = 1 - c_heavy - c_cloud + w_heavy_cloud
    assert Wbar_heavy_cloud == EPS * (1 - Fraction(2, m))

    Wbar_opp_cloud = 1 - 2 * c_cloud + w_opp_cloud
    assert Wbar_opp_cloud > 0

    tail_leverage = Fraction(2, m)
    assert tail_leverage <= Fraction(1, 2)

    s_hc_sq = w_heavy_cloud * Wbar_heavy_cloud
    s_opp_sq = w_opp_cloud * Wbar_opp_cloud
    print(
        f"m={m} total_w={float(total):.12f} "
        f"c_heavy={float(c_heavy):.12f} "
        f"tail_leverage={float(tail_leverage):.12f} "
        f"s_hc={sqrt(float(s_hc_sq)):.12f} "
        f" s_opp={sqrt(float(s_opp_sq)):.12f}"
    )

C0 = 2 * (3 ** 0.25) * sqrt(pi * e)
Ceps = C0 * float(EPS) ** (-0.25)
print(f"C0={C0:.12f}")
print(f"epsilon=1/4 bound={Ceps:.12f}")
print("STATUS=PASS")
