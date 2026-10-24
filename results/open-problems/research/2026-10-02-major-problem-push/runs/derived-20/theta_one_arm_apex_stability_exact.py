#!/usr/bin/env python3
"""Exact certificate for the one-distinguished-arm K_{2,3} theorem."""

import json
from pathlib import Path

import sympy as sp


def is_forest(n, edges):
    parent = list(range(n))

    def find(x):
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


def enumerate_polynomial(t, r, z):
    backbone = [(0, j) for j in (2, 3, 4)] + [(1, j) for j in (2, 3, 4)]
    weights = [t * r, t, t, t * r, t, t]
    spokes = [(5, i) for i in range(5)]
    polynomial = 0
    forest_count = 0
    for bmask in range(64):
        bedges = [backbone[k] for k in range(6) if bmask >> k & 1]
        weight = sp.prod(weights[k] for k in range(6) if bmask >> k & 1)
        for smask in range(32):
            sedges = [spokes[k] for k in range(5) if smask >> k & 1]
            if is_forest(6, bedges + sedges):
                forest_count += 1
                polynomial += weight * sp.prod(
                    z[k] for k in range(5) if smask >> k & 1
                )
    return sp.expand(polynomial), forest_count


def rayleigh(polynomial, z, i, j):
    return sp.expand(
        sp.diff(polynomial, z[i]) * sp.diff(polynomial, z[j])
        - polynomial * sp.diff(polynomial, z[i], z[j])
    )


def quadratic_data(polynomial, variable):
    a, b, c = sp.Poly(polynomial, variable).all_coeffs()
    return tuple(map(sp.expand, (a, b, c, b * b - 4 * a * c)))


def main():
    t, r = sp.symbols("t r", positive=True)
    z = sp.symbols("z0:5", real=True)
    x, y = sp.symbols("x y", real=True)
    polynomial, forest_count = enumerate_polynomial(t, r, z)

    h, hs, he = 2 * t + 1, 2 * r * t + 1, t * (r + 2) + 1
    s = (
        2 * r**2 * t**3 + r**2 * t**2 + 4 * r * t**3 + 4 * r * t**2
        + 2 * r * t + 2 * t**2 + 2 * t + 1
    )
    phi_a = (t + 1) ** 2 * (x*x + y*y) + 2 * t**2 * x*y
    alpha_01 = (r*t + t + 1) * (2*r*t**2 + r*t + t + 1)
    phi_01 = alpha_01 * (x*x + y*y) + 2*t**2*(2*r*t + 1)*x*y
    phi_03 = (
        (2*t + 1)*(2*t**2 + 2*t + 1)*x*x
        + 2*r**2*t**2*(2*t + 1)*x*y
        + r**2*(r*t + t + 1)*(2*r*t**2 + r*t + t + 1)*y*y
    )
    phi_23 = (t + 1)*(r*t + 1)*(x*x + y*y) + 2*r*t**2*x*y
    alpha_e = (r*t + 1)*(2*r*t**2 + 3*r*t + 4*t**2 + 6*t + 3)
    beta_e = (r*t + 2*t + 1)*(2*r*t**2 - r*t - 1)
    phi_e = alpha_e*(x*x + y*y) + 2*beta_e*x*y

    checks = []
    d01 = rayleigh(polynomial, z, 0, 1)
    a01, _, _, disc01 = quadratic_data(d01, z[2])
    checks += [
        sp.expand(a01 - t**2*phi_a.subs({x:z[3]+h,y:z[4]+h})) == 0,
        sp.expand(disc01 + 4*r**2*t**4*(z[3]+h)**2*(z[4]+h)**2
                  * phi_01.subs({x:z[3]+h,y:z[4]+h})) == 0,
        sp.expand(d01.subs({z[3]:-h,z[4]:-h})) == 0,
    ]

    d02 = rayleigh(polynomial, z, 0, 2)
    a02, _, _, disc02 = quadratic_data(d02, z[1])
    checks += [
        sp.expand(a02 - r*t*(r*t+1)*(z[3]+h)**2*(z[4]+h)**2) == 0,
        sp.expand(disc02-disc01) == 0,
        sp.expand(d02.subs(z[3],-h)-2*r*t**3*(t+1)*(r*t+t+1)*(z[4]+h)**2) == 0,
        sp.expand(d02.subs(z[4],-h)-2*r*t**3*(t+1)*(r*t+t+1)*(z[3]+h)**2) == 0,
    ]

    d03 = rayleigh(polynomial, z, 0, 3)
    a03, _, _, disc03 = quadratic_data(d03, z[1])
    checks += [
        sp.expand(a03 - t*(t+1)*(z[2]+hs)**2*(z[4]+h)**2) == 0,
        sp.expand(disc03 + 4*t**4*(z[2]+hs)**2*(z[4]+h)**2
                  * phi_03.subs({x:z[2]+hs,y:z[4]+h})) == 0,
        sp.expand(d03.subs(z[2],-hs)-2*r**2*t**3*(r*t+1)*(r*t+t+1)*(z[4]+h)**2) == 0,
        sp.expand(d03.subs(z[4],-h)-2*t**3*(t+1)*(2*t+1)*(z[2]+hs)**2) == 0,
    ]

    d23 = rayleigh(polynomial, z, 2, 3)
    a23, _, _, disc23 = quadratic_data(d23, z[4])
    checks += [
        sp.expand(a23-r*t**2*phi_23.subs({x:z[0]+he,y:z[1]+he})) == 0,
        sp.expand(disc23 + 4*r**2*t**6*(2*t+1)
                  * phi_e.subs({x:z[0]+he,y:z[1]+he})) == 0,
        sp.expand(d23.subs({z[0]:-he,z[1]:-he})
                  -4*r*t**4*(2*t+1)*(r*t+t+1)) == 0,
    ]

    d34 = rayleigh(polynomial, z, 3, 4)
    a34, _, _, disc34 = quadratic_data(d34, z[2])
    checks += [
        sp.expand(a34-t**2*phi_a.subs({x:z[0]+he,y:z[1]+he})) == 0,
        sp.expand(disc34-disc23) == 0,
        sp.expand(d34.subs({z[0]:-he,z[1]:-he})
                  -4*r**2*t**4*(r*t+t+1)**2) == 0,
    ]

    positivity = {
        "phi_a": [(t+1)**2, sp.factor((2*t+1)*(2*t**2+2*t+1))],
        "phi_01": [alpha_01, sp.factor((2*t+1)*(r*t+1)**2*s)],
        "phi_03": [(2*t+1)*(2*t**2+2*t+1), sp.factor(r**2*(t+1)**2*(2*t+1)*s)],
        "phi_23": [(t+1)*(r*t+1), sp.factor((r*t+t+1)*(2*r*t**2+r*t+t+1))],
        "phi_e": [alpha_e, sp.factor(8*(r*t+t+1)**2*s)],
    }
    checks += [all(v.is_positive for v in values) for values in positivity.values()]
    assert all(checks), checks

    report = {
        "status": "PASS",
        "sympy_version": sp.__version__,
        "enumerated_augmented_forests_at_unit_weights": forest_count,
        "polynomial_terms": len(sp.Poly(polynomial, *z).terms()),
        "rayleigh_pair_orbits_checked": [[0,1],[0,2],[0,3],[2,3],[3,4]],
        "exact_identity_checks": len(checks),
        "positive_form_certificates": {
            key: [str(sp.factor(value)) for value in values]
            for key, values in positivity.items()
        },
        "scope": "K_{2,3}; one arm has activities rt,rt and the other four edges t, with r,t>0",
    }
    output = Path(__file__).with_name("theta_one_arm_apex_stability_exact_results.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
