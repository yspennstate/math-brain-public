#!/usr/bin/env python3
"""Reproduce C023's coherent-block affine DPP example and channel identity.

Numerical checks support the proved determinant identities in agents/C023.md.
Gershgorin contraction bounds and the 3 by 3 coupling determinant are rational.
Only Python's standard library and NumPy are required.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math
import numpy as np


def atoms(kernel, direction=None):
    n = len(kernel)
    eye = np.eye(n)
    out = np.empty(1 << n)
    first = np.empty_like(out) if direction is not None else None
    second = np.empty_like(out) if direction is not None else None
    for mask in range(1 << n):
        included = np.array([(mask >> j) & 1 for j in range(n)])
        matrix = np.where(included[None, :], kernel, eye - kernel)
        out[mask] = np.linalg.det(matrix).real
        if direction is not None:
            signed_direction = direction * (2 * included - 1)[None, :]
            response = np.linalg.solve(matrix, signed_direction)
            tr = np.trace(response)
            first[mask] = (out[mask] * tr).real
            second[mask] = (out[mask] * (tr * tr - np.trace(response @ response))).real
    if direction is None:
        return out
    return out, first, second


def entropy(p):
    return float(-np.dot(p[p > 0], np.log(p[p > 0])))


def pack(mask, sites):
    return sum(((mask >> j) & 1) << k for k, j in enumerate(sites))


def marginal(p, sites):
    result = np.zeros(1 << len(sites))
    for mask, mass in enumerate(p):
        result[pack(mask, sites)] += mass
    return result


def replace(p, sites, reference):
    n = (len(p) - 1).bit_length()
    other = [j for j in range(n) if j not in sites]
    outside = marginal(p, other)
    return np.array([reference[pack(mask, sites)] * outside[pack(mask, other)]
                     for mask in range(len(p))])


def rational_matrix_example():
    n = 9
    k = [[F(0) for _ in range(n)] for _ in range(n)]
    diagonal_blocks = [
        [[F(2, 5), F(1, 20)], [F(1, 20), F(1, 2)]],
        [[F(1, 2), F(1, 25)], [F(1, 25), F(3, 5)]],
        [[F(9, 20), F(-3, 100)], [F(-3, 100), F(11, 20)]],
    ]
    c = [[F(1, 2), F(1, 50), F(-1, 100)],
         [F(1, 50), F(12, 25), F(3, 100)],
         [F(-1, 100), F(3, 100), F(13, 25)]]
    u = [[1, 2], [2, 1], [1, -1]]
    w = [[1, 2, -1], [2, -1, 1], [1, 1, 2]]
    for block, d in enumerate(diagonal_blocks):
        for a in range(2):
            for b in range(2):
                k[2 * block + a][2 * block + b] = d[a][b]
            for b in range(3):
                value = F(u[block][a] * w[block][b], 100)
                k[2 * block + a][6 + b] = value
                k[6 + b][2 * block + a] = value
    for a in range(3):
        for b in range(3):
            k[6 + a][6 + b] = c[a][b]
    radii = [sum(abs(k[i][j]) for j in range(n) if j != i) for i in range(n)]
    lower = min(k[i][i] - radii[i] for i in range(n))
    upper = max(k[i][i] + radii[i] for i in range(n))
    assert lower > 0 and upper < 1
    detw = (w[0][0] * (w[1][1] * w[2][2] - w[1][2] * w[2][1])
            - w[0][1] * (w[1][0] * w[2][2] - w[1][2] * w[2][0])
            + w[0][2] * (w[1][0] * w[2][1] - w[1][1] * w[2][0]))
    assert detw != 0
    return k, lower, upper, detw


def main():
    rational, lower, upper, detw = rational_matrix_example()
    rational_start = [row.copy() for row in rational]
    for i, amplitude in enumerate([F(1, 5), F(2, 5), F(3, 5)]):
        for a in [2 * i, 2 * i + 1]:
            for b in [6, 7, 8]:
                rational_start[a][b] *= amplitude
                rational_start[b][a] *= amplitude
    commutator_1_7 = sum(rational_start[0][j] * rational[j][6]
                         - rational[0][j] * rational_start[j][6] for j in range(9))
    assert commutator_1_7 == F(-1, 2500)
    kstar = np.array([[float(x) for x in row] for row in rational])
    groups = [[0, 1], [2, 3], [4, 5]]
    references = [atoms(kstar[np.ix_(g, g)]) for g in groups]
    pstar = atoms(kstar)
    mu = pstar.copy()
    for group, ref in zip(groups, references):
        mu = replace(mu, group, ref)

    start = np.array([1 / 5, 2 / 5, 3 / 5])
    slopes = 1 - start
    direction = np.zeros_like(kstar)
    for i, group in enumerate(groups):
        direction[np.ix_(group, [6, 7, 8])] = slopes[i] * kstar[np.ix_(group, [6, 7, 8])]
        direction[np.ix_([6, 7, 8], group)] = direction[np.ix_(group, [6, 7, 8])].T

    identity_error = 0.0
    curvature_error = 0.0
    cross_entropies = []
    curvatures = []
    entropies = []
    for t in np.linspace(0, 1, 11):
        amplitudes = start + t * slopes
        k = kstar.copy()
        projected = pstar.copy()
        for i, (group, ref) in enumerate(zip(groups, references)):
            k[np.ix_(group, [6, 7, 8])] *= amplitudes[i]
            k[np.ix_([6, 7, 8], group)] *= amplitudes[i]
            retention = amplitudes[i] ** 2
            projected = retention * projected + (1 - retention) * replace(projected, group, ref)
        p, dp, ddp = atoms(k, direction)
        identity_error = max(identity_error, float(np.max(np.abs(p - projected))))
        cross_entropies.append(float(-np.dot(p, np.log(mu))))
        direct = float(-np.sum(dp * dp / p) - np.dot(ddp, np.log(p)))

        rhs = 0.0
        for i, (group, ref) in enumerate(zip(groups, references)):
            q = replace(p, group, ref)
            delta = p - q
            log_ratio = np.log(p / q)
            jeffreys = float(np.dot(delta, log_ratio))
            chi = float(np.sum(delta * delta / p))
            rate = slopes[i] / amplitudes[i]
            rhs += (4 * chi + 2 * jeffreys) * rate * rate
            for j in range(i + 1, len(groups)):
                up = replace(p, groups[j], references[j]) - p
                uq = replace(q, groups[j], references[j]) - q
                dissipation = -float(np.dot(up, log_ratio + 1 - q / p)
                                     + np.dot(uq, -log_ratio + 1 - p / q))
                assert dissipation >= -1e-13
                rhs += 8 * dissipation * rate * slopes[j] / amplitudes[j]
        curvature_error = max(curvature_error, abs(-direct - rhs))
        curvatures.append(direct)
        entropies.append(entropy(p))

    eig_direction = np.linalg.eigvalsh(direction)
    inertia = [int(np.sum(eig_direction > 1e-10)), int(np.sum(eig_direction < -1e-10)),
               int(np.sum(np.abs(eig_direction) <= 1e-10))]
    assert inertia == [3, 3, 3]
    assert identity_error < 2e-14
    assert curvature_error < 2e-12
    assert np.ptp(cross_entropies) < 1e-12
    assert max(curvatures) < 0
    gaps = [entropies[i] - ((1 - i / 10) * entropies[0] + (i / 10) * entropies[-1])
            for i in range(11)]
    assert min(gaps) > -1e-13

    counterexample_mu = np.array([3, 5, 5, 3]) / 16
    counterexample_input = np.ones(4) / 4
    counterexample_h2 = -2 * float(np.dot(counterexample_input - counterexample_mu,
                                         np.log(counterexample_mu)))
    assert abs(counterexample_h2 - math.log(5 / 3) / 4) < 1e-15
    result = {
        "dimension": 9,
        "kernel_star_rational": [[str(x) for x in row] for row in rational],
        "gershgorin_interval_exact": [str(lower), str(upper)],
        "integer_coupling_determinant": detw,
        "endpoint_commutator_entry_1_7_exact": str(commutator_1_7),
        "affine_direction_inertia_positive_negative_zero": inertia,
        "maximum_atom_intertwining_error": identity_error,
        "maximum_hessian_decomposition_error": curvature_error,
        "cross_entropy_range": [min(cross_entropies), max(cross_entropies)],
        "entropy_curvatures": curvatures,
        "entropy_chord_gaps": gaps,
        "nonproduct_reset_counterexample_H_second_at_zero": counterexample_h2,
    }
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key != "kernel_star_rational"}, indent=2))


if __name__ == "__main__":
    main()
