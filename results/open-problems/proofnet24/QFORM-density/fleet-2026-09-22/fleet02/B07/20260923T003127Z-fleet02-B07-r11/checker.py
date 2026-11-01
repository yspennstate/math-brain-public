from fractions import Fraction
from math import comb, e, sqrt
import random


def overlap_energy(m, q):
    return Fraction(comb(3, q) * (m - 1) ** (3 - q), m ** 3)


# Exact stress-family overlap ledger.
for m in (4, 6, 10, 100):
    E = [overlap_energy(m, q) for q in range(4)]
    assert sum(E) == 1
    print("m", m, "E", *(str(x) for x in E))

# Balanced q=0 cross packet: (m/2)^6 minors, each of squared size m^-6.
for m in (4, 6, 10, 100):
    assert m % 2 == 0
    packet = Fraction((m // 2) ** 6, m ** 6)
    assert packet == Fraction(1, 64)
    leverage = Fraction(2, m)
    assert leverage <= Fraction(1, 2)
    print("balanced", m, "Z3", str(packet), "row_marginal", str(leverage))

# Partner q=0 packet and bi-anchor threshold.
P0 = Fraction(1, 5184)
assert P0 / 3 == Fraction(1, 15552)
print("partner_P0", str(P0), "bianchor_floor", str(P0 / 3))

# Constants used in the report.
q0_diffuse = 9 * sqrt(3 * e) * (5184 ** (1 / 6))
stress_D = 12 * sqrt(e)
print("q0_diffuse_bound", format(q0_diffuse, ".15f"))
print("stress_D_bound", format(stress_D, ".15f"))

# Seeded regression of V3 <= C(m,3) ||B||^4 s3(B)^2 at singular-value level.
rng = random.Random(20260923)
for m in range(3, 11):
    C = comb(m, 3)
    for _ in range(1000):
        s = sorted((10 ** rng.uniform(-3, 2) for _ in range(m)), reverse=True)
        L = s[0]
        V3 = 0.0
        for i in range(m):
            for j in range(i + 1, m):
                for k in range(j + 1, m):
                    V3 += (s[i] * s[j] * s[k]) ** 2
        rhs = C * (L ** 4) * (s[2] ** 2)
        assert V3 <= rhs * (1 + 1e-12)
print("core_compound_inequality_seeded_regression", "PASS")
print("QFORM_BOUNDED_CORE_Q0_PACKET_CHECK_PASS")
