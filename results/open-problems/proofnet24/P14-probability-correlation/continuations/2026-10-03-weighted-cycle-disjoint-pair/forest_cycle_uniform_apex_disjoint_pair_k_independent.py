"""Independent exact audit of the uniform-cycle apex/disjoint-pair extension.

No implementation from the forest-backbone proof is imported.  The apex
partition is computed by a literal connectivity-partition DP retaining the
cycle vertices and apex.  Selected four-terminal cases retain all cycle and
terminal vertices.  All arithmetic and Sturm calculations are exact.
"""

from collections import defaultdict
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


OUT = Path(__file__).with_name(
    "forest_cycle_uniform_apex_disjoint_pair_k_independent_results.json"
)


def canonical(labels):
    names = {}
    return tuple(names.setdefault(label, len(names)) for label in labels)


def join(state, u, v):
    if state[u] == state[v]:
        return None
    left, right = state[u], state[v]
    return canonical(tuple(left if label == right else label for label in state))


def add_polynomial(target, source, multiplier=F(1), shift=0):
    for degree, coefficient in enumerate(source):
        if degree + shift < len(target):
            target[degree + shift] += multiplier * coefficient


def cycle_edges(n, weight):
    if n == 2:
        return [(0, 1, weight), (0, 1, weight)]
    return [(vertex, (vertex + 1) % n, weight) for vertex in range(n)]


def apex_polynomial_literal(n, lam):
    """Literal forest DP; the final vertex n is the apex."""
    zero = (F(0),) * (n + 1)
    unit = [F(0)] * (n + 1)
    unit[0] = F(1)
    frontier = {tuple(range(n + 1)): tuple(unit)}

    edges = [(u, v, weight, 0) for u, v, weight in cycle_edges(n, lam)]
    edges += [(n, vertex, F(1), 1) for vertex in range(n)]
    for u, v, multiplier, degree_shift in edges:
        following = {}
        for state, polynomial in frontier.items():
            if state not in following:
                following[state] = list(zero)
            add_polynomial(following[state], polynomial)
            target = join(state, u, v)
            if target is not None:
                if target not in following:
                    following[target] = list(zero)
                add_polynomial(
                    following[target],
                    polynomial,
                    multiplier=multiplier,
                    shift=degree_shift,
                )
        frontier = {state: tuple(poly) for state, poly in following.items()}

    answer = [F(0)] * (n + 1)
    for polynomial in frontier.values():
        add_polynomial(answer, polynomial)
    return answer


def polynomial_trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def polynomial_add(left, right, right_multiplier=F(1)):
    out = [F(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += right_multiplier * value
    return polynomial_trim(out)


def polynomial_multiply(left, right):
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return polynomial_trim(out)


def recurrence_polynomial(n, p):
    """(r_+^n+r_-^n-2p^n)/(1-p^n), without adjoining sqrt(p)."""
    trace = [F(1) + p, F(1) - p]
    previous, current = [F(2)], trace
    if n == 0:
        power_sum = previous
    elif n == 1:
        power_sum = current
    else:
        for _ in range(2, n + 1):
            following = polynomial_add(
                polynomial_multiply(trace, current),
                previous,
                right_multiplier=-p,
            )
            previous, current = current, following
        power_sum = current
    power_sum[0] -= 2 * p**n
    denominator = 1 - p**n
    return [value / denominator for value in power_sum]


def composition_coefficient(n, k, p):
    """Claimed normalized coefficient of s^k."""
    if k == 0:
        return F(1)
    target = n - k
    coefficient = F(0)
    for right_degree in range(target + 1):
        left_degree = target - right_degree
        coefficient += (
            comb(k + left_degree - 1, left_degree)
            * comb(k + right_degree - 1, right_degree)
            * p**right_degree
        )
    return F(n, k) * (1 - p) ** k * coefficient / (1 - p**n)


def derivative(poly):
    return [F(i) * poly[i] for i in range(1, len(poly))] or [F(0)]


def remainder(dividend, divisor):
    dividend = list(dividend)
    divisor = polynomial_trim(divisor)
    while len(polynomial_trim(dividend)) >= len(divisor) and any(dividend):
        dividend = polynomial_trim(dividend)
        degree = len(dividend) - len(divisor)
        factor = dividend[-1] / divisor[-1]
        for i, value in enumerate(divisor):
            dividend[degree + i] -= factor * value
    return polynomial_trim(dividend)


def variations(signs):
    signs = [sign for sign in signs if sign]
    return sum(left != right for left, right in zip(signs, signs[1:]))


def sturm_negative_distinct_roots(poly):
    sequence = [polynomial_trim(poly), polynomial_trim(derivative(poly))]
    while len(sequence[-1]) > 1:
        following = [-value for value in remainder(sequence[-2], sequence[-1])]
        following = polynomial_trim(following)
        if not any(following):
            break
        sequence.append(following)

    at_negative_infinity = []
    at_zero = []
    for row in sequence:
        leading_sign = 1 if row[-1] > 0 else -1
        degree = len(row) - 1
        at_negative_infinity.append(
            leading_sign * (-1 if degree % 2 else 1)
        )
        at_zero.append(1 if row[0] > 0 else -1 if row[0] < 0 else 0)
    root_count = variations(at_negative_infinity) - variations(at_zero)
    square_free = len(sequence[-1]) == 1
    return root_count, square_free


def evaluate_derivative(poly, point, order=0):
    value = F(0)
    for degree in range(order, len(poly)):
        falling = 1
        for factor in range(order):
            falling *= degree - factor
        value += poly[degree] * falling * point ** (degree - order)
    return value


def direct_marked_coefficients(n, lam, columns):
    """Literal DP on all n+4 vertices, with marked activities omitted."""
    total_vertices = n + 4
    frontier = {tuple(range(total_vertices)): F(1)}
    unmarked = cycle_edges(n, lam) + [
        (n + row, vertex, columns[row])
        for row in range(4)
        for vertex in range(n)
        if columns[row]
    ]
    for u, v, weight in unmarked:
        following = defaultdict(F)
        for state, mass in frontier.items():
            following[state] += mass
            target = join(state, u, v)
            if target is not None:
                following[target] += mass * weight
        frontier = dict(following)

    coefficients = [F(0)] * 4
    for state, mass in frontier.items():
        for marked in range(4):
            target = state
            if marked & 1:
                target = join(target, n, n + 1)
            if target is not None and marked & 2:
                target = join(target, n + 2, n + 3)
            if target is not None:
                coefficients[marked] += mass
    return coefficients


def scalar_marked_coefficients(apex, columns):
    a, b, c, d = columns
    s = sum(columns, F(0))
    assert s > 0
    D = evaluate_derivative(apex, s, 0)
    D1 = evaluate_derivative(apex, s, 1)
    D2 = evaluate_derivative(apex, s, 2)
    D3 = evaluate_derivative(apex, s, 3)
    log1 = D1 / D
    log2 = D2 / D - log1**2
    log3 = D3 / D - 3 * D1 * D2 / D**2 + 2 * log1**3
    n = len(apex) - 1
    U = (F(n) - log1) / s
    T = -log2
    Gamma = (U - T) / s
    Omega = Gamma / s - log3 / (2 * s)

    p, q, u, v = a + b, c + d, a * b, c * d
    H3 = Gamma + s * U**2
    H4 = 2 * Omega - U**2 + 3 * s * U * Gamma + s**2 * U**3
    coefficients = [
        D * (1 + (p * q + u + v) * U + (u * q + v * p) * H3 + u * v * H4),
        D * (1 + (p * q + v) * U + v * p * H3),
        D * (1 + (p * q + u) * U + u * q * H3),
        D * (1 + p * q * U),
    ]
    first = U * T - Omega
    second = Gamma**2 + U**2 * T - 2 * U * Omega
    rayleigh = D**2 * a * b * c * d * (
        2 * first + p * q * second
    )
    return coefficients, rayleigh, (D, U, Gamma, Omega, T, first, second)


def normalized_apex_case(n, p):
    lam = p / (1 - p) if p else F(0)
    literal = apex_polynomial_literal(n, lam)
    ZH = (1 + lam) ** n * (1 - p**n)
    normalized = [value / ZH for value in literal]
    recurrence = recurrence_polynomial(n, p)
    composition = [composition_coefficient(n, k, p) for k in range(n + 1)]
    assert normalized == recurrence == composition
    assert normalized[0] == 1
    assert normalized[1] == n
    if p:
        negative, square_free = sturm_negative_distinct_roots(normalized)
        assert negative == n and square_free
    else:
        assert normalized == [
            F(comb(n, k)) for k in range(n + 1)
        ]
        negative, square_free = 1, False
    return {
        "n": n,
        "p": str(p),
        "lambda": str(lam),
        "Z_H": str(ZH),
        "normalized_coefficients_ascending": list(map(str, normalized)),
        "negative_distinct_roots": negative,
        "square_free": square_free,
    }


def marked_case(n, p, columns):
    lam = p / (1 - p) if p else F(0)
    apex = apex_polynomial_literal(n, lam)
    direct = direct_marked_coefficients(n, lam, columns)
    scalar, predicted_rayleigh, parameters = scalar_marked_coefficients(
        apex, columns
    )
    assert direct == scalar
    observed_rayleigh = direct[1] * direct[2] - direct[0] * direct[3]
    assert observed_rayleigh == predicted_rayleigh
    expected_strict = bool(all(columns) and n >= 2)
    assert (observed_rayleigh > 0) == expected_strict
    assert parameters[-2] >= 0 and parameters[-1] >= 0
    return {
        "n": n,
        "p": str(p),
        "lambda": str(lam),
        "columns": list(map(str, columns)),
        "direct_A_E_F_C": list(map(str, direct)),
        "Rayleigh": str(observed_rayleigh),
        "strict": expected_strict,
        "D_U_Gamma_Omega_T_first_second": list(map(str, parameters)),
    }


def main():
    apex_cases = [
        normalized_apex_case(n, p)
        for n in range(2, 10)
        for p in (F(0), F(1, 5), F(1, 2), F(4, 5))
    ]
    marked_inputs = [
        (2, F(0), [F(1), F(2), F(3), F(4)]),
        (2, F(1, 3), [F(1, 2), F(2, 3), F(3, 4), F(4, 5)]),
        (3, F(0), [F(2), F(3), F(5), F(7)]),
        (3, F(2, 5), [F(1), F(2), F(3), F(4)]),
        (4, F(1, 5), [F(1, 3), F(2, 5), F(3, 7), F(4, 9)]),
        (5, F(1, 2), [F(1), F(1), F(2), F(3)]),
        (6, F(3, 4), [F(2, 3), F(3, 5), F(5, 7), F(7, 11)]),
        (3, F(1, 2), [F(0), F(2), F(3), F(5)]),
        (4, F(2, 3), [F(2), F(0), F(5), F(7)]),
    ]
    marked_cases = [marked_case(n, p, columns) for n, p, columns in marked_inputs]
    report = {
        "status": "PASS; exact finite audit, analytic root proof is separate",
        "arithmetic": "fractions.Fraction and exact Sturm sequences",
        "implementation": (
            "literal all-vertex connectivity partitions; no imports from "
            "the forest-backbone theorem implementation"
        ),
        "apex_cases": apex_cases,
        "marked_cases": marked_cases,
        "summary": {
            "apex_cases": len(apex_cases),
            "apex_max_n": max(case["n"] for case in apex_cases),
            "all_positive_p_cases_have_n_distinct_negative_roots": True,
            "p_zero_cases_equal_(1+s)^n": True,
            "marked_cases": len(marked_cases),
            "marked_strict_cases": sum(case["strict"] for case in marked_cases),
            "marked_equality_cases": sum(not case["strict"] for case in marked_cases),
            "counterexamples": 0,
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["summary"], indent=2), flush=True)


if __name__ == "__main__":
    main()
