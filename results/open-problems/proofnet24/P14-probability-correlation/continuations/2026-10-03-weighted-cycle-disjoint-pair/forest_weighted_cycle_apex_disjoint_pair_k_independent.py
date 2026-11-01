"""Independent exact audit for arbitrary weighted-cycle apex polynomials.

The checker retains all original vertices in literal connectivity-partition
DPs.  It independently reconstructs the two-state transfer and cyclic-gap
formula.  It imports no implementation from the proposed theorem or the
forest-backbone checkers.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from random import Random
import json


OUT = Path(__file__).with_name(
    "forest_weighted_cycle_apex_disjoint_pair_k_independent_results.json"
)
SEED = 731042


def canonical(labels):
    names = {}
    return tuple(names.setdefault(label, len(names)) for label in labels)


def join(state, u, v):
    if state[u] == state[v]:
        return None
    left, right = state[u], state[v]
    return canonical(tuple(left if label == right else label for label in state))


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left, right, right_multiplier=F(1)):
    out = [F(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += right_multiplier * value
    return trim(out)


def multiply(left, right):
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return trim(out)


def scale_and_shift(poly, multiplier, shift, size):
    out = [F(0)] * size
    for i, value in enumerate(poly):
        if i + shift < size:
            out[i + shift] += multiplier * value
    return out


def matrix_multiply(left, right):
    return [
        [
            add(
                multiply(left[i][0], right[0][j]),
                multiply(left[i][1], right[1][j]),
            )
            for j in range(2)
        ]
        for i in range(2)
    ]


def cycle_edges(lambdas):
    n = len(lambdas)
    # Edge i joins vertex i-1 to vertex i.  For n=2 these are the two
    # labeled parallel edges.
    return [((i - 1) % n, i, lambdas[i]) for i in range(n)]


def apex_literal(lambdas, betas):
    n = len(lambdas)
    size = n + 1
    unit = [F(0)] * size
    unit[0] = F(1)
    frontier = {tuple(range(n + 1)): unit}
    edges = [(u, v, weight, 0) for u, v, weight in cycle_edges(lambdas)]
    edges += [
        (n, vertex, betas[vertex], 1)
        for vertex in range(n)
        if betas[vertex]
    ]
    for u, v, weight, degree_shift in edges:
        following = {}
        for state, polynomial in frontier.items():
            following.setdefault(state, [F(0)] * size)
            following[state] = add(following[state], polynomial)
            following[state] += [F(0)] * (size - len(following[state]))
            target = join(state, u, v)
            if target is not None:
                following.setdefault(target, [F(0)] * size)
                contribution = scale_and_shift(
                    polynomial, weight, degree_shift, size
                )
                following[target] = add(following[target], contribution)
                following[target] += [F(0)] * (
                    size - len(following[target])
                )
        frontier = following
    answer = [F(0)] * size
    for polynomial in frontier.values():
        for i, value in enumerate(polynomial):
            answer[i] += value
    return trim(answer)


def transfer_polynomial(lambdas, betas):
    matrix = [[[F(1)], [F(0)]], [[F(0)], [F(1)]]]
    determinant = F(1)
    Lambda = F(1)
    for lam, beta in zip(lambdas, betas):
        transfer = [
            [[1 + lam, beta], [0, beta * lam]],
            [[1], [lam]],
        ]
        matrix = matrix_multiply(transfer, matrix)
        determinant *= lam * (1 + lam)
        Lambda *= lam
    polynomial = add(matrix[0][0], matrix[1][1])
    polynomial[0] -= 2 * Lambda
    observed_determinant = add(
        multiply(matrix[0][0], matrix[1][1]),
        multiply(matrix[0][1], matrix[1][0]),
        right_multiplier=-1,
    )
    assert observed_determinant == [determinant]
    return trim(polynomial), matrix, Lambda, determinant


def cyclic_gap_polynomial(lambdas, betas):
    n = len(lambdas)
    Lambda = F(1)
    all_plus = F(1)
    for lam in lambdas:
        Lambda *= lam
        all_plus *= 1 + lam
    coefficients = [F(0)] * (n + 1)
    coefficients[0] = all_plus - Lambda
    for mask in range(1, 1 << n):
        selected = [i for i in range(n) if mask >> i & 1]
        value = F(1)
        for i in selected:
            value *= betas[i]
        for position, start in enumerate(selected):
            finish = selected[(position + 1) % len(selected)]
            plus_product = rim_product = F(1)
            edge = (start + 1) % n
            while True:
                plus_product *= 1 + lambdas[edge]
                rim_product *= lambdas[edge]
                if edge == finish:
                    break
                edge = (edge + 1) % n
            value *= plus_product - rim_product
        coefficients[len(selected)] += value
    return trim(coefficients)


def derivative(poly):
    return [F(i) * poly[i] for i in range(1, len(poly))] or [F(0)]


def remainder(dividend, divisor):
    dividend = trim(dividend)
    divisor = trim(divisor)
    while any(dividend) and len(dividend) >= len(divisor):
        degree = len(dividend) - len(divisor)
        factor = dividend[-1] / divisor[-1]
        for i, value in enumerate(divisor):
            dividend[degree + i] -= factor * value
        dividend = trim(dividend)
    return dividend


def polynomial_gcd(left, right):
    left, right = trim(left), trim(right)
    while any(right):
        left, right = right, remainder(left, right)
    if not any(left):
        return [F(0)]
    return [value / left[-1] for value in left]


def variations(signs):
    signs = [sign for sign in signs if sign]
    return sum(left != right for left, right in zip(signs, signs[1:]))


def distinct_negative_roots(poly):
    sequence = [trim(poly), trim(derivative(poly))]
    while len(sequence[-1]) > 1:
        following = trim(
            [-value for value in remainder(sequence[-2], sequence[-1])]
        )
        if not any(following):
            break
        sequence.append(following)
    negative_infinity = []
    zero = []
    for row in sequence:
        sign = 1 if row[-1] > 0 else -1
        negative_infinity.append(
            sign * (-1 if (len(row) - 1) % 2 else 1)
        )
        zero.append(1 if row[0] > 0 else -1 if row[0] < 0 else 0)
    return variations(negative_infinity) - variations(zero)


def negative_roots_with_multiplicity(poly):
    current = trim(poly)
    total = 0
    while len(current) > 1:
        total += distinct_negative_roots(current)
        following = polynomial_gcd(current, derivative(current))
        if len(following) == 1:
            break
        current = following
    return total


def evaluate_derivative(poly, point, order=0):
    value = F(0)
    for degree in range(order, len(poly)):
        falling = 1
        for factor in range(order):
            falling *= degree - factor
        value += poly[degree] * falling * point ** (degree - order)
    return value


def direct_marked(lambdas, betas, columns, status=None):
    n = len(lambdas)
    if status is None:
        status = [-1] * n
    state = tuple(range(n + 4))
    fixed_mass = F(1)
    optional = []
    for index, ((u, v, weight), value) in enumerate(
        zip(cycle_edges(lambdas), status)
    ):
        if value == 0:
            continue
        if value == 1:
            if weight == 0:
                return None
            target = join(state, u, v)
            if target is None:
                return None
            state = target
            fixed_mass *= weight
        else:
            optional.append((u, v, weight))
    unmarked = optional + [
        (n + row, vertex, columns[row] * betas[vertex])
        for row in range(4)
        for vertex in range(n)
        if columns[row] * betas[vertex]
    ]
    frontier = {state: fixed_mass}
    for u, v, weight in unmarked:
        following = defaultdict(F)
        for partition, mass in frontier.items():
            following[partition] += mass
            target = join(partition, u, v)
            if target is not None:
                following[target] += mass * weight
        frontier = dict(following)
    coefficients = [F(0)] * 4
    for partition, mass in frontier.items():
        for marked in range(4):
            target = partition
            if marked & 1:
                target = join(target, n, n + 1)
            if target is not None and marked & 2:
                target = join(target, n + 2, n + 3)
            if target is not None:
                coefficients[marked] += mass
    return coefficients


def scalar_marked(apex, betas, columns):
    a, b, c, d = columns
    s = sum(columns, F(0))
    assert s > 0
    D = evaluate_derivative(apex, s)
    D1 = evaluate_derivative(apex, s, 1)
    D2 = evaluate_derivative(apex, s, 2)
    D3 = evaluate_derivative(apex, s, 3)
    log1 = D1 / D
    log2 = D2 / D - log1**2
    log3 = D3 / D - 3 * D1 * D2 / D**2 + 2 * log1**3
    total_profile = sum(betas, F(0))
    U = (total_profile - log1) / s
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


def conditioned_profile_rank(lambdas, betas, status):
    n = len(lambdas)
    state = tuple(range(n))
    for (u, v, weight), value in zip(cycle_edges(lambdas), status):
        if value == 1:
            if weight == 0:
                return None
            state = join(state, u, v)
            if state is None:
                return None
    sums = defaultdict(F)
    for vertex, beta in enumerate(betas):
        sums[state[vertex]] += beta
    return sum(value > 0 for value in sums.values())


def apex_case(lambdas, betas, label):
    literal = apex_literal(lambdas, betas)
    transfer, _, Lambda, delta = transfer_polynomial(lambdas, betas)
    gaps = cyclic_gap_polynomial(lambdas, betas)
    assert literal == transfer == gaps
    degree = sum(beta > 0 for beta in betas)
    assert len(literal) - 1 == degree
    negative = negative_roots_with_multiplicity(literal)
    assert negative == degree
    if all(lambdas):
        assert delta > Lambda**2
    return {
        "label": label,
        "n": len(lambdas),
        "lambdas": list(map(str, lambdas)),
        "betas": list(map(str, betas)),
        "coefficients_ascending": list(map(str, literal)),
        "degree": degree,
        "negative_roots_counting_multiplicity": negative,
        "Lambda": str(Lambda),
        "delta": str(delta),
    }


def marked_case(lambdas, betas, columns, label):
    apex = apex_literal(lambdas, betas)
    direct = direct_marked(lambdas, betas, columns)
    scalar, predicted, parameters = scalar_marked(apex, betas, columns)
    assert direct == scalar
    rayleigh = direct[1] * direct[2] - direct[0] * direct[3]
    assert rayleigh == predicted
    strict = bool(all(columns) and sum(beta > 0 for beta in betas) >= 2)
    assert (rayleigh > 0) == strict
    assert parameters[-2] >= 0 and parameters[-1] >= 0
    return {
        "label": label,
        "n": len(lambdas),
        "lambdas": list(map(str, lambdas)),
        "betas": list(map(str, betas)),
        "columns": list(map(str, columns)),
        "A_E_F_C": list(map(str, direct)),
        "Rayleigh": str(rayleigh),
        "strict": strict,
    }


def random_apex_cases(trials=120):
    rng = Random(SEED)
    counts = defaultdict(int)
    for _ in range(trials):
        n = rng.randrange(2, 9)
        lambdas = [
            F(rng.randrange(7), rng.randrange(1, 7)) for _ in range(n)
        ]
        betas = [
            F(rng.randrange(7), rng.randrange(1, 7)) for _ in range(n)
        ]
        apex_case(lambdas, betas, "seeded_random")
        counts[str(n)] += 1
    return {
        "seed": SEED,
        "cases": trials,
        "cases_by_n": dict(sorted(counts.items())),
        "counterexamples": 0,
    }


def conditioning_audit(lambdas, betas, columns):
    checked = strict = equality = 0
    for status in product((-1, 0, 1), repeat=len(lambdas)):
        rank = conditioned_profile_rank(lambdas, betas, status)
        if rank is None:
            continue
        coefficients = direct_marked(
            lambdas, betas, columns, status=list(status)
        )
        if coefficients is None:
            continue
        A, E, G, C = coefficients
        rayleigh = E * G - A * C
        expected = bool(all(columns) and rank >= 2)
        assert rayleigh >= 0 and (rayleigh > 0) == expected
        checked += 1
        strict += expected
        equality += not expected
    return {
        "n": len(lambdas),
        "lambdas": list(map(str, lambdas)),
        "betas": list(map(str, betas)),
        "coordinate_conditionings": checked,
        "strict": strict,
        "equality": equality,
    }


def main():
    prescribed = []
    for n in range(2, 9):
        positive_lambdas = [
            F((2 * i + n) % 7 + 1, (i + 2) % 5 + 1) for i in range(n)
        ]
        positive_betas = [
            F((3 * i + n) % 8 + 1, (2 * i + 1) % 5 + 1)
            for i in range(n)
        ]
        prescribed.append(
            apex_case(
                positive_lambdas,
                positive_betas,
                "all_positive_nonuniform",
            )
        )
        zero_lambda = positive_lambdas[:]
        zero_lambda[n // 2] = F(0)
        prescribed.append(
            apex_case(zero_lambda, positive_betas, "one_zero_lambda")
        )
        zero_beta = positive_betas[:]
        zero_beta[n // 2] = F(0)
        prescribed.append(
            apex_case(positive_lambdas, zero_beta, "one_zero_beta")
        )
        prescribed.append(
            apex_case(
                [F(0)] * n,
                [F(1)] * n,
                "edgeless_repeated_root_boundary",
            )
        )

    marked_inputs = [
        ([F(1), F(2)], [F(1), F(3)], [F(1), F(2), F(3), F(4)], "parallel_C2"),
        ([F(1, 2), F(2, 3), F(3, 4)], [F(1), F(2), F(4)], [F(2), F(3), F(5), F(7)], "weighted_C3"),
        ([F(1), F(2), F(3), F(4)], [F(1, 2), F(2, 3), F(3, 4), F(4, 5)], [F(1, 3), F(2, 5), F(3, 7), F(4, 9)], "weighted_C4"),
        ([F(1, 3), F(2, 5), F(3, 7), F(4, 9), F(5, 11)], [F(1), F(3), F(2), F(5), F(4)], [F(1), F(1), F(2), F(3)], "weighted_C5"),
        ([F(1), F(0), F(2), F(3)], [F(1), F(2), F(3), F(4)], [F(2), F(3), F(5), F(7)], "broken_cycle"),
        ([F(1), F(2), F(3), F(4)], [F(1), F(0), F(3), F(0)], [F(2), F(3), F(5), F(7)], "zero_profiles_rank2"),
        ([F(1), F(2), F(3)], [F(1), F(0), F(0)], [F(2), F(3), F(5), F(7)], "one_profile_equality"),
        ([F(1), F(2), F(3)], [F(1), F(2), F(3)], [F(0), F(3), F(5), F(7)], "zero_row_equality"),
    ]
    marked = [
        marked_case(lambdas, betas, columns, label)
        for lambdas, betas, columns, label in marked_inputs
    ]
    conditionings = [
        conditioning_audit(
            [F(1, 2), F(2, 3), F(3, 4)],
            [F(1), F(0), F(3)],
            [F(1), F(2), F(3), F(4)],
        ),
        conditioning_audit(
            [F(1), F(2), F(3), F(4)],
            [F(1), F(2), F(3), F(4)],
            [F(1, 2), F(2, 3), F(3, 4), F(4, 5)],
        ),
    ]
    report = {
        "status": "PASS; finite exact audit, analytic Hermitian proof separate",
        "arithmetic": "fractions.Fraction and exact Sturm/gcd",
        "implementation": (
            "literal all-vertex forest DPs, independent transfer matrices, "
            "and independent cyclic-gap enumeration"
        ),
        "prescribed_apex_cases": prescribed,
        "seeded_random_apex": random_apex_cases(),
        "marked_cases": marked,
        "conditioning_cases": conditionings,
        "summary": {
            "prescribed_apex_cases": len(prescribed),
            "seeded_random_apex_cases": 120,
            "maximum_n": 8,
            "marked_cases": len(marked),
            "strict_marked_cases": sum(case["strict"] for case in marked),
            "equality_marked_cases": sum(not case["strict"] for case in marked),
            "coordinate_conditionings": sum(
                case["coordinate_conditionings"] for case in conditionings
            ),
            "conditioning_strict": sum(case["strict"] for case in conditionings),
            "conditioning_equality": sum(case["equality"] for case in conditionings),
            "counterexamples": 0,
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["summary"], indent=2), flush=True)


if __name__ == "__main__":
    main()
