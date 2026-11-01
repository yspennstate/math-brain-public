#!/usr/bin/env python3
"""Worker 058: exact finite certificates for the accompanying analytic proofs.

Standard library only. No numerical logarithms, optimization, or random search.
Run from the session root with: python computations/058_renyi_exact.py
"""

from fractions import Fraction as Q
from itertools import permutations
from math import isqrt
from pathlib import Path
import json


def product(values):
    result = Q(1)
    for value in values:
        result *= value
    return result


def determinant(matrix):
    n = len(matrix)
    result = Q(0)
    for order in permutations(range(n)):
        inversions = sum(order[i] > order[j]
                         for i in range(n) for j in range(i + 1, n))
        result += (-1) ** inversions * product(matrix[i][order[i]]
                                                for i in range(n))
    return result


def minor(matrix, mask):
    indices = [i for i in range(len(matrix)) if mask & (1 << i)]
    return [[matrix[i][j] for j in indices] for i in indices]


def dpp_atoms(matrix):
    n = len(matrix)
    minors = {mask: determinant(minor(matrix, mask))
              for mask in range(1 << n)}
    atoms = {}
    for mask in range(1 << n):
        atoms[mask] = sum(((-1) ** (sup.bit_count() - mask.bit_count())
                           * minors[sup]
                           for sup in range(1 << n)
                           if mask & sup == mask), Q(0))
    assert sum(atoms.values(), Q(0)) == 1
    assert all(p >= 0 for p in atoms.values())
    return atoms


def diagonal_product(diagonal):
    return {mask: product(diagonal[i] if mask & (1 << i)
                          else 1 - diagonal[i]
                          for i in range(len(diagonal)))
            for mask in range(1 << len(diagonal))}


def kernel(diagonal, off_diagonal, t=Q(1)):
    return [[diagonal[i] if i == j else t * off_diagonal[i][j]
             for j in range(len(diagonal))] for i in range(len(diagonal))]


def strict_contraction(matrix):
    n = len(matrix)
    complement = [[Q(i == j) - matrix[i][j] for j in range(n)]
                  for i in range(n)]
    # Sylvester's criterion: both real symmetric matrices are positive definite.
    for size in range(1, n + 1):
        assert determinant([row[:size] for row in matrix[:size]]) > 0
        assert determinant([row[:size] for row in complement[:size]]) > 0


def collision(atoms):
    return sum((p * p for p in atoms.values()), Q(0))


def chi_squared(atoms, reference):
    return sum(((atoms[x] - reference[x]) ** 2 / reference[x]
                for x in atoms), Q(0))


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(a))), Q(0))
             for j in range(len(a))] for i in range(len(a))]


def resample(atoms, diagonal, t):
    n = len(diagonal)
    return {y: sum((atoms[x] * product(
        t * Q(bool(x & (1 << i)) == bool(y & (1 << i)))
        + (1 - t) * (diagonal[i] if y & (1 << i) else 1 - diagonal[i])
        for i in range(n)) for x in range(1 << n)), Q(0))
        for y in range(1 << n)}


def rational_sqrt(value):
    num, den = isqrt(value.numerator), isqrt(value.denominator)
    assert num * num == value.numerator and den * den == value.denominator
    return Q(num, den)


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(v) for v in value]
    return value


def main():
    diagonal = [Q(1, 4), Q(1, 3)]
    off = [[Q(0), Q(1, 6)], [Q(1, 6), Q(0)]]
    middle, plus, minus = (kernel(diagonal, off, t) for t in [Q(0), Q(1), Q(-1)])
    for matrix in [middle, plus, minus]:
        strict_contraction(matrix)
    p0, pp, pm = (dpp_atoms(matrix) for matrix in [middle, plus, minus])
    assert pp == pm
    assert p0 == {0: Q(1, 2), 1: Q(1, 6), 2: Q(1, 4), 3: Q(1, 12)}
    assert pp == {0: Q(17, 36), 1: Q(7, 36), 2: Q(5, 18), 3: Q(1, 18)}
    for atoms in [p0, pp, pm]:
        assert atoms[1] + atoms[3] == diagonal[0]
        assert atoms[2] + atoms[3] == diagonal[1]
    z0, zp = collision(p0), collision(pp)
    assert z0 == Q(225, 648) and zp == Q(221, 648) and zp < z0
    assert z0 / zp == Q(225, 221)
    ab, ba = matmul(plus, minus), matmul(minus, plus)
    commutator = [[ab[i][j] - ba[i][j] for j in range(2)] for i in range(2)]
    assert commutator == [[Q(0), Q(1, 36)], [Q(-1, 36), Q(0)]]

    # Polynomial identity for K(t) with off-diagonal entry t, not t/6.
    pprime2 = [Q(-2), Q(2), Q(2), Q(-2)]
    coefficients = [z0, Q(0), Q(-1, 3), Q(0), Q(4)]
    assert coefficients[2] == sum((p0[i] * pprime2[i] for i in range(4)), Q(0))
    assert coefficients[4] == sum(((pprime2[i] / 2) ** 2 for i in range(4)), Q(0))
    h2_second = -2 * coefficients[2] / z0
    assert h2_second == Q(48, 25)
    assert determinant(plus) == Q(1, 18)
    complement_plus = [[Q(i == j) - plus[i][j] for j in range(2)] for i in range(2)]
    assert determinant(complement_plus) == Q(17, 36)

    # An order-1/2 local obstruction with square-root-free rational certificate.
    half_diagonal = [Q(1, 5), Q(4, 5)]
    half_atoms = diagonal_product(half_diagonal)
    zhalf = sum((rational_sqrt(p) for p in half_atoms.values()), Q(0))
    zhalf_second = sum((pprime2[i] / (2 * rational_sqrt(half_atoms[i]))
                       for i in range(4)), Q(0))
    hhalf_second = 2 * zhalf_second / zhalf
    assert zhalf == Q(9, 5) and hhalf_second == Q(25, 18)

    # At the same alpha=2 chord witness, product-reference weighting reverses
    # the mistaken unweighted comparison. The sharp t^4 factor is attained.
    mu = diagonal_product(diagonal)
    assert chi_squared(pp, mu) == Q(1, 54)
    pair_checks = {}
    for t in [Q(0), Q(1, 3), Q(2, 3), Q(1)]:
        atoms = dpp_atoms(kernel(diagonal, off, t))
        expected = t ** 4 / 54
        assert chi_squared(atoms, mu) == expected
        pair_checks[str(t)] = expected

    # A three-site triangle checks the density expansion, all atom noise
    # identities, degree-six contribution, and strict quartic contraction.
    diag3 = [Q(1, 3), Q(1, 2), Q(2, 3)]
    off3 = [[Q(0), Q(1, 12), Q(1, 10)],
            [Q(1, 12), Q(0), Q(1, 15)],
            [Q(1, 10), Q(1, 15), Q(0)]]
    k3 = kernel(diag3, off3)
    strict_contraction(k3)
    mu3, p3 = diagonal_product(diag3), dpp_atoms(k3)
    variances = [p * (1 - p) for p in diag3]
    minor_coefficients = {mask: determinant(minor(off3, mask))
                          for mask in range(1, 8)}
    chi_coefficients = {mask: minor_coefficients[mask] ** 2 /
                        product(variances[i] for i in range(3) if mask & (1 << i))
                        for mask in range(1, 8)}
    assert minor_coefficients[7] != 0
    checks3 = {}
    for t in [Q(0), Q(1, 3), Q(2, 3), Q(1)]:
        atoms = dpp_atoms(kernel(diag3, off3, t))
        assert atoms == resample(p3, diag3, t)
        for x in range(8):
            predicted_density = Q(1)
            for mask in range(1, 8):
                contrast = product((Q(bool(x & (1 << i))) - diag3[i]) / variances[i]
                                   for i in range(3) if mask & (1 << i))
                predicted_density += t ** mask.bit_count() * minor_coefficients[mask] * contrast
            assert atoms[x] / mu3[x] == predicted_density
        chi = chi_squared(atoms, mu3)
        expected = sum((t ** (2 * mask.bit_count()) * chi_coefficients[mask]
                        for mask in range(1, 8)), Q(0))
        assert chi == expected
        assert chi <= t ** 4 * chi_squared(p3, mu3)
        if Q(0) < t < Q(1):
            assert chi < t ** 4 * chi_squared(p3, mu3)
        checks3[str(t)] = chi
    assert resample(dpp_atoms(kernel(diag3, off3, Q(2, 3))), diag3, Q(1, 2)) == dpp_atoms(kernel(diag3, off3, Q(1, 3)))

    output = {
        "status": "all exact assertions passed",
        "arithmetic": "fractions.Fraction; no numerical logarithms or random sampling",
        "alpha_two_chord": {
            "midpoint_kernel": middle, "plus_kernel": plus, "minus_kernel": minus,
            "det_K_plus": determinant(plus), "det_I_minus_K_plus": determinant(complement_plus),
            "midpoint_atoms_bitmask_order": p0, "endpoint_atoms_bitmask_order": pp,
            "midpoint_collision": z0, "endpoint_collision": zp,
            "strict_chord_deficit": "log(225/221)", "ratio_certifying_positive_deficit": z0 / zp,
            "commutator_plus_minus": commutator,
            "collision_polynomial_offdiagonal_t": coefficients,
            "H2_second_derivative_offdiagonal_t_at_zero": h2_second,
        },
        "alpha_one_half_local": {
            "diagonal": half_diagonal, "atoms": half_atoms,
            "power_sum": zhalf, "power_sum_second_derivative": zhalf_second,
            "entropy_second_derivative": hhalf_second,
        },
        "weighted_pair": {"chi_squared_full": Q(1, 54), "chi_squared_by_scale": pair_checks},
        "weighted_triangle": {
            "diagonal": diag3, "off_diagonal": off3, "kernel": k3,
            "chi_squared_coefficients_by_subset_bitmask": chi_coefficients,
            "chi_squared_by_scale": checks3,
            "checks": ["all atom density identities", "all atom resampling identities",
                       "resampling semigroup", "quartic contraction strict away from endpoints"],
        },
        "scope": "Finite certificates check identities on stated examples; universal proofs are in agents/058.md."
    }
    target = Path(__file__).with_name("058_renyi_exact_output.json")
    target.write_text(json.dumps(serial(output), indent=2) + "\n")
    print(json.dumps({"status": output["status"], "output": str(target)}, indent=2))


if __name__ == "__main__":
    main()
