import math


def J(m: int) -> float:
    return math.exp(
        -(math.log(m) / 3.0)
        + math.lgamma(m + 1)
        + math.lgamma(4.0 / 3.0)
        - math.lgamma(m + 1.0 / 3.0)
    )


print("m J_m J_m^2 ratio_to_m^(2/3)")
for m in [2, 4, 8, 16, 32, 64, 128, 256]:
    jm = J(m)
    moment = jm * jm
    print(m, jm, moment, moment / (m ** (2.0 / 3.0)))

limit = math.gamma(4.0 / 3.0) ** 2
C_ind = 8 * 3 ** (3 / 4) * 5 ** (1 / 4) / math.sqrt(math.e)
partner_bound = 2 ** (3 / 4) * C_ind
print("Gamma(4/3)^2 =", limit)
print("2^(3/4) C_ind =", partner_bound)

assert J(256) ** 2 > J(128) ** 2 > J(64) ** 2
assert abs((J(256) ** 2) / (256 ** (2.0 / 3.0)) - limit) < 0.01
assert partner_bound < 27.817
print("PASS")
