import math

TAU = 0.1740316570325050
DEGREES = [1, 2, 3, 4, 5, 10, 15, 20, 50, 100]


def q_degree(d: int) -> float:
    r = 2.0 ** (-1.0 + 1.0 / d)
    return (r * r) / (1.0 + r * r)


print(f"tau={TAU:.16f}")
print("d q_d mass_floor down_energy_floor")
for d in DEGREES:
    qd = q_degree(d)
    mass = 4.0 ** (1 - d)
    delta = max(qd - TAU, 0.0)
    # The proved down-oriented branch gives
    # sum w(q-tau)^2 >= 2 * mass * delta^2.
    energy = 2.0 * mass * delta * delta
    print(f"{d:3d} {qd:.16g} {mass:.16g} {energy:.16g}")

# Structural threshold check: q_d > 1/5 for every sampled finite d,
# while analytically q_d decreases to 1/5 as d -> infinity.
for d in range(2, 10001):
    assert q_degree(d) > 0.2

print("finite_degree_threshold_check=PASS")
