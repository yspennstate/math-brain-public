import math


def constants(q):
    assert 1.0 <= q < 2.0
    beta = 0.5 + 1.0 / q
    invp = 1.0 - 1.0 / q
    K0 = ((4 * math.pi) ** (-0.5) * 2 ** (-1.0 / q)
          * (2 * math.pi) ** invp * (16 * math.pi ** 2 / q) ** (1.0 / q))
    K0_simplified = 2 ** (2.0 / q) * math.pi ** beta * q ** (-1.0 / q)
    density_raw = beta / (math.pi * (beta - 1.0)) * K0 ** (1.0 / beta)
    density_raw_simplified = ((q + 2) / (2 - q)
                              * 2 ** (4 / (q + 2)) * q ** (-2 / (q + 2)))
    target = density_raw * 2 ** (1 / (q + 2))
    target_simplified = ((q + 2) / (2 - q)
                         * 2 ** (5 / (q + 2)) * q ** (-2 / (q + 2)))
    collision_multiplier = 4 + 2 / (2 * beta - 0.5)
    return (beta, K0, K0_simplified, density_raw, density_raw_simplified,
            target, target_simplified, collision_multiplier)


for q in (1.0, 1.2, 1.5, 1.8):
    vals = constants(q)
    assert abs(vals[1] - vals[2]) < 1e-11
    assert abs(vals[3] - vals[4]) < 1e-11
    assert abs(vals[5] - vals[6]) < 1e-11
    print("q", q, "beta", vals[0], "K0", vals[1],
          "Ctarget", vals[5], "collision_multiplier", vals[7])

q = 1.5
Ctarget = constants(q)[5]
Cpartner = 7 * 2 ** (16 / 7) * 3 ** (-4 / 7)
envelope = 128 * math.sqrt(15)
threshold = (Ctarget / envelope) ** (7 / 2)
partner_threshold = (Cpartner / envelope) ** (7 / 2)
u2_floor = 0.994673971719684
print("Ctarget_q_3_2", Ctarget)
print("Cpartner_q_3_2", Cpartner)
print("threshold_new", threshold)
print("threshold_partner", partner_threshold)
print("threshold_ratio", partner_threshold / threshold)
print("left_concentrated_delta_zeta_ceiling", threshold / u2_floor)

K0 = constants(q)[1]
beta = constants(q)[0]
collision_multiplier = constants(q)[7]
Ccollision = (collision_multiplier * K0 ** (1 / (2 * beta))
              * 2 ** (1 / (2 * (q + 2))))
print("Ccollision_q_3_2", Ccollision)

Cq1 = constants(1.0)[5]
tauq1 = (Cq1 / envelope) ** 3
print("Ctarget_q_1", Cq1)
print("threshold_q_1_for_u2_zeta", tauq1)

assert abs(partner_threshold / threshold - 2.0) < 1e-10
assert abs(Ctarget - 28 * 3 ** (-4 / 7)) < 1e-10
assert abs(Ccollision - 13.184993358485492) < 1e-10
print("QFORM_B03_TWO_PHYSICAL_ROW_PASS")
