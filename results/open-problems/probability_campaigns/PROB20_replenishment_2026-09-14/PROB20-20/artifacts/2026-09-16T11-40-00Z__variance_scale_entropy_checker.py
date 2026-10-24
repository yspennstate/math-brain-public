import math


def run_case(name, R, L, U, h, s, c0):
    q = {}
    for k in range(1, R):
        # Deterministic strict pre-record rates above h.
        rate = h + 0.22 / math.sqrt(k) + 0.015
        q[k] = math.exp(-rate * k) / c0
    q[R] = math.exp(-h * R) / c0

    point_rate = {k: -math.log(c0 * q[k]) / k for k in range(1, R + 1)}
    r = {}
    cur = float("inf")
    for k in range(1, R + 1):
        cur = min(cur, point_rate[k])
        r[k] = cur

    assert abs(r[R] - h) < 1e-12

    D = sum(q[k] * math.exp(s * k) for k in range(L + 1, U + 1))
    mu = {k: q[k] * math.exp(s * k) / D for k in range(L + 1, U + 1)}
    M = sum(k * p for k, p in mu.items())
    V = min(U, max(L + 1, math.ceil(2 * M)))

    Dv = sum(q[k] * math.exp(s * k) for k in range(L + 1, V + 1))
    muv = {k: q[k] * math.exp(s * k) / Dv for k in range(L + 1, V + 1)}
    Mv = sum(k * p for k, p in muv.items())
    H = -sum(p * math.log(p) for p in muv.values())

    Gamma = min(x * (r[x] - h) for x in range(L, V + 1))

    # Pointwise record-barrier / entropy inequality:
    # -log(mu_k) >= Gamma + (h-s) k + log(c0 Dv)
    point_slacks = [
        -math.log(muv[k]) - (Gamma + (h - s) * k + math.log(c0 * Dv))
        for k in muv
    ]

    averaged_lower = Gamma + (h - s) * Mv + math.log(c0 * Dv)
    avg_slack = H - averaged_lower

    # Elementary geometric maximum-entropy upper bound.
    maxent = math.log(math.e * (Mv + 1.0))
    maxent_slack = maxent - H

    gamma_rhs = H + max(s - h, 0.0) * Mv - math.log(c0 * Dv)
    gamma_slack = gamma_rhs - Gamma

    half_mass = Dv / D

    assert half_mass >= 0.5
    assert min(point_slacks) >= -1e-11
    assert avg_slack >= -1e-11
    assert maxent_slack >= -1e-11
    assert gamma_slack >= -1e-11

    return {
        "name": name,
        "R": R,
        "L": L,
        "U": U,
        "V": V,
        "half_mass_ratio": half_mass,
        "M": M,
        "Mv": Mv,
        "H": H,
        "Gamma": Gamma,
        "min_pointwise_slack": min(point_slacks),
        "avg_entropy_slack": avg_slack,
        "max_entropy_slack": maxent_slack,
        "gamma_upper_slack": gamma_slack,
    }


cases = [
    ("tilt_above_record", 200, 20, 100, 0.025, 0.045, 0.50),
    ("mild_tilt_above_record", 300, 30, 140, 0.018, 0.027, 0.40),
    ("tilt_below_record", 180, 15, 90, 0.030, 0.020, 0.60),
]

for result in [run_case(*case) for case in cases]:
    print(result["name"])
    for key in [
        "R", "L", "U", "V", "half_mass_ratio", "M", "Mv", "H", "Gamma",
        "min_pointwise_slack", "avg_entropy_slack", "max_entropy_slack",
        "gamma_upper_slack",
    ]:
        value = result[key]
        if isinstance(value, float):
            print(f"  {key}={value:.12g}")
        else:
            print(f"  {key}={value}")
    print()

print("PASS")
