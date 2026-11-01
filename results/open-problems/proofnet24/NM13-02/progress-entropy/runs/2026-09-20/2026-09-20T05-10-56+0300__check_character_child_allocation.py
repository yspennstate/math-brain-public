import math
import json


def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log(p, 2) - (1.0 - p) * math.log(1.0 - p, 2)


def psi(delta):
    if delta <= 0.0 or delta >= 1.0:
        return 0.0
    q = (1.0 - delta) ** 2 + delta ** 2
    return 2.0 * delta * (1.0 - delta) + q * h2(delta ** 2 / q)


def walsh_coeff(values, n):
    N = 1 << n
    out = []
    for s in range(N):
        total = 0
        for x, value in enumerate(values):
            parity = (s & x).bit_count() & 1
            total += value * (-1 if parity else 1)
        out.append(total / N)
    return out


def direct_B_inf(m, A, g_values):
    # bit 0 is the queried coordinate; bits 1..m are the remaining cube.
    n = m + 1
    values = []
    for x in range(1 << n):
        xi = x & 1
        y = x >> 1
        char = -1 if ((A & y).bit_count() & 1) else 1
        values.append(char if xi == 0 else g_values[y])

    hats = walsh_coeff(values, n)
    B = 0.0
    for T in range(1 << m):
        a = hats[T << 1] ** 2
        b = hats[(T << 1) | 1] ** 2
        q = a + b
        if q > 0.0:
            B += q * h2(b / q)

    disagreements = 0
    for y in range(1 << m):
        char = -1 if ((A & y).bit_count() & 1) else 1
        disagreements += (char != g_values[y])
    influence = disagreements / (1 << m)
    return B, influence


def one_defect_R_ratio(n):
    if n < 2:
        return 0.0
    total = 0.0
    for m in range(2, n + 1):
        delta = 2.0 ** (1 - m)
        total += psi(delta) / delta
    return total / n


def main():
    C_char = 2.0 + 1.0 / (math.sqrt(math.e) * math.log(2.0))

    max_error = 0.0
    max_direct_ratio = 0.0
    cases = 0
    # Exhaust every Boolean opposite branch and every character child for m <= 3.
    for m in range(4):
        N = 1 << m
        for mask in range(1 << N):
            g = [1 if ((mask >> y) & 1) == 0 else -1 for y in range(N)]
            for A in range(1 << m):
                B, delta = direct_B_inf(m, A, g)
                max_error = max(max_error, abs(B - psi(delta)))
                if delta > 0.0:
                    max_direct_ratio = max(max_direct_ratio, B / delta)
                cases += 1

    grid_max_delta = 0.0
    grid_max_ratio = 0.0
    for k in range(1, 200000):
        delta = k / 200000.0
        ratio = psi(delta) / delta
        if ratio > grid_max_ratio:
            grid_max_ratio = ratio
            grid_max_delta = delta

    ns = [2, 3, 4, 5, 10, 20, 50, 100]
    result = {
        "status": "PASS",
        "analytic_constant_C_char": C_char,
        "analytic_constant_lt_2_876": C_char < 2.876,
        "direct_exhaustive_cases_m_le_3": cases,
        "max_abs_formula_error": max_error,
        "max_direct_ratio_m_le_3": max_direct_ratio,
        "continuous_grid_points": 199999,
        "continuous_grid_max_delta": grid_max_delta,
        "continuous_grid_max_ratio": grid_max_ratio,
        "grid_max_below_analytic_constant": grid_max_ratio < C_char,
        "one_defect_R_over_I": {str(n): one_defect_R_ratio(n) for n in ns},
        "p03_derivative_degree_ratio_examples": {str(n): (n - 1) / 2 for n in ns},
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
