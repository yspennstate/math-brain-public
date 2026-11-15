"""Small exact checks of the linear-workload certificate; Python standard library."""
import itertools
import json
import os
from fractions import Fraction as F
from pathlib import Path

os.environ["OMP_NUM_THREADS"] = "1"


def solve(rows, rhs):
    n = len(rhs)
    aug = [[F(x) for x in row] + [F(y)] for row, y in zip(rows, rhs)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if aug[i][k]), None)
        if pivot is None:
            return None
        aug[k], aug[pivot] = aug[pivot], aug[k]
        scale = aug[k][k]
        aug[k] = [x / scale for x in aug[k]]
        for i in range(n):
            if i != k:
                scale = aug[i][k]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[k])]
    return tuple(row[-1] for row in aug)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def audit_vertices(A, C, weights):
    """Enumerate vertices for every active support, retaining Pareto vertices."""
    I = len(weights)
    b = [min(C[j] for j in range(len(C)) if A[j][i]) for i in range(I)]
    values = []
    count = 0
    for mask in range(1, 1 << I):
        active = [i for i in range(I) if mask & (1 << i)]
        k = len(active)
        rows = [[A[j][i] for i in active] for j in range(len(C))]
        bounds = list(C)
        rows += [[-int(i == j) for i in range(k)] for j in range(k)]
        bounds += [0] * k
        vertices = set()
        for chosen in itertools.combinations(range(len(rows)), k):
            x = solve([rows[j] for j in chosen], [bounds[j] for j in chosen])
            if x is None or any(dot(row, x) > c for row, c in zip(rows, bounds)):
                continue
            saturated = [j for j in range(len(C)) if dot(rows[j], x) == C[j]]
            if all(any(A[j][i] for j in saturated) for i in active):
                vertices.add(x)
        assert vertices
        count += len(vertices)
        values.extend(dot([weights[i] for i in active], x) for x in vertices)
    predicted = min(w * bi for w, bi in zip(weights, b))
    observed = min(values)
    assert observed == predicted
    return {
        "active_supports": (1 << I) - 1,
        "pareto_vertices_counted_by_support": count,
        "b": list(map(str, b)),
        "minimum_weighted_service": str(observed),
        "predicted_minimum": str(predicted),
    }


def main():
    A = [[1, 1, 0], [1, 0, 1]]
    rho = [F(1, 5), F(1, 2), F(1, 2)]
    loads_matrix = [dot(row, rho) for row in A]
    loads_routes = [rho[0] + rho[1], rho[0] + rho[2]]
    assert loads_matrix == loads_routes == [F(7, 10), F(7, 10)]
    beta = sum(rho)
    nu = sum(rho)  # For this check, mean file sizes are all one.
    mean_jump = sum(rate / nu for rate in rho)
    assert beta == nu * mean_jump == F(6, 5)
    witnesses = 0
    for weights in itertools.product(range(1, 9), repeat=3):
        q = min(weights)
        a = dot(weights, rho)
        assert a - q >= q * F(1, 5)
        witnesses += 1
    result = {
        "two_link_obstruction": {
            "loads_by_matrix_and_route_sums": list(map(str, loads_matrix)),
            "beta_by_load_sum_and_arrival_marks": str(beta),
            "positive_integer_weight_vectors_checked": witnesses,
            "positive_drift_lower_bound": "min(weights)/5",
        },
        "equal_capacity_vertices": audit_vertices(A, [F(1), F(1)], [F(2), F(3), F(5)]),
        "unequal_capacity_vertices": audit_vertices(
            [[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1]],
            [F(2), F(3), F(5)],
            [F(3, 2), F(2, 3), F(5, 4), F(7, 3)],
        ),
        "status": "all exact checks passed",
    }
    output = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("certificate_checks.json").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
