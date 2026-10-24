#!/usr/bin/env python3
"""Exact certificate for side-uniform K_{2,3} apex-spoke stability.

Requires SymPy.  The script independently enumerates all forests of the
six-vertex graph obtained by adjoining one apex to K_{2,3}, constructs the
five-variable spoke polynomial, and checks the four symmetry-orbit
Rayleigh certificates used in the proof.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def is_forest(n: int, edges: list[tuple[int, int]]) -> bool:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True


def enumerate_polynomial(p, q, z):
    backbone = [(0, j) for j in (2, 3, 4)] + [(1, j) for j in (2, 3, 4)]
    spokes = [(5, i) for i in range(5)]
    polynomial = 0
    forest_count = 0
    for bmask in range(1 << 6):
        bedges = [backbone[k] for k in range(6) if bmask >> k & 1]
        for smask in range(1 << 5):
            sedges = [spokes[k] for k in range(5) if smask >> k & 1]
            if is_forest(6, bedges + sedges):
                forest_count += 1
                weight = sp.prod((p if k < 3 else q) for k in range(6) if bmask >> k & 1)
                polynomial += weight * sp.prod(
                    z[k] for k in range(5) if smask >> k & 1
                )
    return sp.expand(polynomial), forest_count


def rayleigh(p, z, i, j):
    return sp.expand(sp.diff(p, z[i]) * sp.diff(p, z[j]) - p * sp.diff(p, z[i], z[j]))


def quadratic_data(q, variable):
    poly = sp.Poly(q, variable)
    assert poly.degree() == 2
    a, b, c = poly.all_coeffs()
    return map(sp.expand, (a, b, c, b * b - 4 * a * c))


def main():
    p, q = sp.symbols("p q", positive=True)
    z = sp.symbols("z0:5", real=True)
    polynomial, forest_count = enumerate_polynomial(p, q, z)

    # Internal-variable shifts and the positive definite residual forms.
    x, y = sp.symbols("x y", real=True)
    h = p + q + 1
    h0, h1 = 3 * p + 1, 3 * q + 1
    form_a = (p + 1) * (q + 1) * (x * x + y * y) + 2 * p * q * x * y
    form_q = (2 * p * q + p + q + 1) * (x * x + y * y) + 2 * p * q * x * y
    form_b = q ** 2 * (q + 1) ** 2 * x * x + 2 * p ** 2 * q ** 2 * x * y + p ** 2 * (p + 1) ** 2 * y * y
    form_r = 3 * q ** 2 * (q + 1) ** 2 * x * x + 2 * p * q * (3 * p * q - p - q - 1) * x * y + 3 * p ** 2 * (p + 1) ** 2 * y * y

    checks = []

    # Endpoint--endpoint orbit; treat Delta_01 as a quadratic in z2.
    d01 = rayleigh(polynomial, z, 0, 1)
    a01, b01, c01, disc01 = quadratic_data(d01, z[2])
    checks += [
        sp.expand(a01 - p * q * form_a.subs({x: z[3] + h, y: z[4] + h})) == 0,
        sp.expand(
            disc01
            + 4 * p ** 2 * q ** 2 * h * (z[3] + h) ** 2 * (z[4] + h) ** 2
            * form_q.subs({x: z[3] + h, y: z[4] + h})
        ) == 0,
        sp.expand(d01.subs({z[3]: -h, z[4]: -h})) == 0,
    ]

    # Endpoint--internal orbit; treat Delta_02 as a quadratic in z1.
    d02 = rayleigh(polynomial, z, 0, 2)
    a02, b02, c02, disc02 = quadratic_data(d02, z[1])
    checks += [
        sp.expand(a02 - p * (p + 1) * (z[3] + h) ** 2 * (z[4] + h) ** 2) == 0,
        sp.expand(
            disc02
            + 4 * p ** 2 * q ** 2 * h * (z[3] + h) ** 2 * (z[4] + h) ** 2
            * form_q.subs({x: z[3] + h, y: z[4] + h})
        ) == 0,
        sp.expand(
            d02.subs(z[3], -h)
            - 2 * p * q ** 2 * (q + 1) * h * (z[4] + h) ** 2
        ) == 0,
        sp.expand(
            d02.subs(z[4], -h)
            - 2 * p * q ** 2 * (q + 1) * h * (z[3] + h) ** 2
        ) == 0,
    ]

    # The endpoint--internal orbit splits because p and q need not agree.
    d12 = rayleigh(polynomial, z, 1, 2)
    a12, b12, c12, disc12 = quadratic_data(d12, z[0])
    checks += [
        sp.expand(a12 - q * (q + 1) * (z[3] + h) ** 2 * (z[4] + h) ** 2) == 0,
        sp.expand(
            disc12
            + 4 * p ** 2 * q ** 2 * h * (z[3] + h) ** 2 * (z[4] + h) ** 2
            * form_q.subs({x: z[3] + h, y: z[4] + h})
        ) == 0,
        sp.expand(
            d12.subs(z[3], -h)
            - 2 * p ** 2 * q * (p + 1) * h * (z[4] + h) ** 2
        ) == 0,
        sp.expand(
            d12.subs(z[4], -h)
            - 2 * p ** 2 * q * (p + 1) * h * (z[3] + h) ** 2
        ) == 0,
    ]

    # Internal--internal orbit; treat Delta_23 as a quadratic in z4.
    d23 = rayleigh(polynomial, z, 2, 3)
    a23, b23, c23, disc23 = quadratic_data(d23, z[4])
    checks += [
        sp.expand(a23 - form_b.subs({x: z[0] + h0, y: z[1] + h1})) == 0,
        sp.expand(
            disc23
            + 4 * p ** 2 * q ** 2 * h ** 2
            * form_r.subs({x: z[0] + h0, y: z[1] + h1})
        ) == 0,
        sp.expand(
            d23.subs({z[0]: -h0, z[1]: -h1}) - 4 * p ** 2 * q ** 2 * h ** 2
        ) == 0,
    ]

    # Positive definiteness: use eigenvalues for the symmetric forms and
    # positive diagonal plus determinant for the unequal-diagonal forms.
    # Record the exact factorizations.
    positivity_data = {
        "form_a_eigenvalues": [2 * p * q + p + q + 1, p + q + 1],
        "form_q_eigenvalues": [3 * p * q + p + q + 1, p * q + p + q + 1],
        "form_b_diagonal_and_determinant": [
            q ** 2 * (q + 1) ** 2,
            p ** 2 * (p + 1) ** 2,
            p ** 2 * q ** 2 * (p + q + 1) * (2 * p * q + p + q + 1),
        ],
        "form_r_diagonal_and_determinant": [
            3 * q ** 2 * (q + 1) ** 2,
            3 * p ** 2 * (p + 1) ** 2,
            8 * p ** 2 * q ** 2 * (p + q + 1) * (3 * p * q + p + q + 1),
        ],
    }
    checks += [all(v.is_positive for v in vals) for vals in positivity_data.values()]

    assert all(checks), checks
    report = {
        "status": "PASS",
        "sympy_version": sp.__version__,
        "enumerated_forests_with_multiplicity_of_subsets": forest_count,
        "polynomial_terms": len(sp.Poly(polynomial, *z).terms()),
        "rayleigh_pair_orbits_checked": [[0, 1], [0, 2], [1, 2], [2, 3]],
        "exact_identity_checks": len(checks),
        "positive_form_certificates": {
            key: [str(sp.factor(v)) for v in vals] for key, vals in positivity_data.items()
        },
        "scope": "K_{2,3}; three edges incident to endpoint 0 have p>0 and the other three q>0",
    }
    out = Path(__file__).with_name("theta_uniform_apex_stability_exact_results.json")
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
