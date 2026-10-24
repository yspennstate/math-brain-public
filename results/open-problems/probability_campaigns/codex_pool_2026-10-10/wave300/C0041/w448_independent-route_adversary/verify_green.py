"""Exact finite-state audit; four environments, no simulation or model loading."""
from fractions import Fraction as F
from pathlib import Path
import json
import time


def main():
    started = time.perf_counter()
    checks = 0

    def check(condition, name):
        nonlocal checks
        if not condition:
            raise AssertionError(name)
        checks += 1

    rows = {
        "A": (F(7, 10), F(1, 10), F(1, 10), F(1, 10)),
        "B": (F(1, 10), F(7, 10), F(1, 10), F(1, 10)),
    }
    mass = {"A": F(11, 20), "B": F(9, 20)}
    for label, row in rows.items():
        check(sum(row) == 1, f"{label}: normalized")
        check(min(row) >= F(1, 10), f"{label}: UE")
    check(sum(mass.values()) == 1, "iid one-site probability law")
    raw_drift = sum(mass[t] * (rows[t][0] - rows[t][1]) for t in rows)
    check(raw_drift == F(3, 50), "positive raw drift")

    g = [F(0), F(0)]
    flow = [[F(0) for _ in range(4)] for _ in range(2)]
    cases = []
    for t0 in rows:
        for tm in rows:
            p0, pm = rows[t0], rows[tm]
            weight = mass[t0] * mass[tm]
            # Solve the two occupation-balance equations exactly.
            g0 = 1 / (1 - p0[1] * pm[0])
            gm = g0 * p0[1]
            check(g0 == 1 + gm * pm[0], "origin balance")
            check(gm == g0 * p0[1], "minus-site balance")
            # Independently compute total outgoing probability through the boundary.
            exits0 = g0 * (1 - p0[1])
            exitsm = gm * (1 - pm[0])
            check(exits0 + exitsm == 1, "exit probability conserved")
            # Boundary first coordinates are +1 at origin's +e1 exit,
            # -2 at minus-site's -e1 exit, -1 at its transverse exits.
            boundary_coordinate = g0 * p0[0] - gm * (
                2 * pm[1] + pm[2] + pm[3]
            )
            occupation_drift = g0 * (p0[0] - p0[1]) + gm * (pm[0] - pm[1])
            check(boundary_coordinate == occupation_drift, "telescoped drift equals exit flux")
            for site, green, row in [(0, g0, p0), (1, gm, pm)]:
                g[site] += weight * green
                for direction in range(4):
                    flow[site][direction] += weight * green * row[direction]
            cases.append({"origin": t0, "minus_site": tm, "probability": str(weight), "green_origin": str(g0)})

    auxiliary = [[value / g[site] for value in flow[site]] for site in range(2)]
    for site in range(2):
        check(sum(auxiliary[site]) == 1, "auxiliary normalized")
        check(min(auxiliary[site]) >= F(1, 10), "auxiliary UE")
    # Solve the auxiliary chain independently, then compare annealed Green entries.
    aux_g0 = 1 / (1 - auxiliary[0][1] * auxiliary[1][0])
    aux_gm = aux_g0 * auxiliary[0][1]
    check(aux_g0 == g[0], "annealed and auxiliary origin Green agree")
    check(aux_gm == g[1], "annealed and auxiliary minus-site Green agree")
    weighted_drift = flow[0][0] - flow[0][1]
    aux_drift = auxiliary[0][0] - auxiliary[0][1]
    check(g[0] == F(2021, 1581), "displayed mean Green")
    check(weighted_drift == -F(202, 2635), "displayed weighted numerator")
    check(aux_drift == -F(606, 10105), "displayed auxiliary drift")
    check(aux_drift < 0 < raw_drift, "sign reversal")
    wrong_factorization = g[0] * raw_drift
    check(weighted_drift - wrong_factorization == -F(4041, 26350), "exact covariance")

    # Universal single-site lower bound at A-mass 9/10: r is any
    # nonnegative, nonzero escape vector. Verify the linear inequality
    # coefficient by coefficient, which proves it for the whole cone.
    a, b, step_drift, lower = F(9, 10), F(1, 10), F(3, 5), F(3, 40)
    coefficients = []
    for e in range(4):
        wa, wb = rows["A"][e], rows["B"][e]
        numerator = step_drift * (a * wb - b * wa)
        denominator = a * wb + b * wa
        residual = numerator - lower * denominator
        check(residual >= 0, "universal escape-tilt bound coefficient")
        coefficients.append(str(residual))
    check(coefficients[0] == "0", "algebraic cone bound is sharp at +e1 vertex")

    out = {
        "status": "PASS",
        "exact_checks": checks,
        "environment_configurations": len(cases),
        "simulation": False,
        "raw_drift": str(raw_drift),
        "raw_drift_decimal": float(raw_drift),
        "mean_origin_green": str(g[0]),
        "incorrect_factorized_numerator": str(wrong_factorization),
        "incorrect_factorized_numerator_decimal": float(wrong_factorization),
        "correct_occupation_numerator": str(weighted_drift),
        "correct_occupation_numerator_decimal": float(weighted_drift),
        "auxiliary_origin_drift": str(aux_drift),
        "auxiliary_origin_drift_decimal": float(aux_drift),
        "covariance": str(weighted_drift - wrong_factorization),
        "special_case_mass_A": str(a),
        "universal_auxiliary_drift_lower_bound": str(lower),
        "escape_cone_residual_coefficients": coefficients,
        "cases": cases,
        "elapsed_seconds": time.perf_counter() - started,
        "scope": "Exact rational identities and a cone inequality. The infinite-volume proof and existing ballisticity theorem require mathematical review.",
    }
    Path("measurements.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
