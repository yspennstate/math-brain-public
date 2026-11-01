#!/usr/bin/env python3
"""Independent exact audit of rank-one weighted K_{2,3} apex stability.

Weights are p*a_j and q*a_j on the two edges of arm j.  The polynomial is
constructed from backbone-component factors; no author probe is imported.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from random import Random
import json

import sympy as sp


OUT = Path(__file__).with_name("theta_rank_one_apex_stability_k_independent.json")
SEED = 1003202605


def component_polynomial(p, q, arms, z):
    edges = []
    for offset, arm in enumerate(arms):
        vertex = offset + 2
        edges += [(0, vertex, p*arm), (1, vertex, q*arm)]
    answer, accepted = 0, 0
    for mask in range(64):
        parent = list(range(5))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        weight, cyclic = 1, False
        for index, (u, v, activity) in enumerate(edges):
            if not (mask >> index) & 1:
                continue
            u, v = find(u), find(v)
            if u == v:
                cyclic = True
                break
            parent[u] = v
            weight *= activity
        if cyclic:
            continue
        accepted += 1
        components = defaultdict(list)
        for vertex in range(5):
            components[find(vertex)].append(vertex)
        term = weight
        for component in components.values():
            term *= 1 + sum(z[vertex] for vertex in component)
        answer += term
    return sp.expand(answer), accepted


def rayleigh(polynomial, z, i, j):
    return sp.expand(
        sp.diff(polynomial, z[i])*sp.diff(polynomial, z[j])
        - polynomial*sp.diff(polynomial, z[i], z[j])
    )


def quadratic_data(polynomial, variable):
    coefficients = sp.Poly(polynomial, variable).all_coeffs()
    assert len(coefficients) == 3
    leading, linear, constant = coefficients
    return tuple(map(sp.expand, (
        leading, linear, constant, linear*linear - 4*leading*constant,
    )))


def positive_coefficients(polynomial, variables):
    return all(coefficient > 0 for coefficient in sp.Poly(polynomial, *variables).coeffs())


def simultaneous_swaps(polynomial, pairs):
    temporaries = [sp.Dummy() for _ in pairs]
    first = {}
    second = {}
    for temporary, (left, right) in zip(temporaries, pairs):
        first[left], first[right] = temporary, left
        second[temporary] = right
    return polynomial.xreplace(first).xreplace(second)


def pair_form(u, v, p, q):
    s = p + q
    return ((1+s*u)*(1+s*v)
            + p*q*(u*u + v*v + s*u*v*(u+v)))


def triple_form(a, b, c, p, q):
    s = p + q
    symmetric_degree_two = (a*a*b + a*a*c + a*b*b + a*c*c + b*b*c + b*c*c)
    return ((1+s*a)*(1+s*b)*(1+s*c)
            + p*q*(a*a+b*b+c*c + s*s*a*b*c*(a+b+c)
                   + s*symmetric_degree_two))


def canonical(labels):
    names = {}
    return tuple(names.setdefault(value, len(names)) for value in labels)


def join(partition, u, v):
    if partition[u] == partition[v]:
        return None
    left, right = partition[u], partition[v]
    return canonical(left if value == right else value for value in partition)


def direct_marked(p, q, arms, beta, rows):
    n = 5
    edges = []
    for offset, arm in enumerate(arms):
        vertex = offset + 2
        edges += [(0, vertex, Fraction(p*arm)), (1, vertex, Fraction(q*arm))]
    edges += [
        (n + row, vertex, Fraction(rows[row])*Fraction(beta[vertex]))
        for row in range(4)
        for vertex in range(n)
        if rows[row]*beta[vertex]
    ]
    states = {tuple(range(n+4)): Fraction(1)}
    for u, v, weight in edges:
        following = defaultdict(Fraction)
        for partition, mass in states.items():
            following[partition] += mass
            target = join(partition, u, v)
            if target is not None:
                following[target] += weight*mass
        states = dict(following)
    coefficients = [Fraction(0)]*4
    for partition, mass in states.items():
        for mask in range(4):
            target = partition
            if mask & 1:
                target = join(target, n, n+1)
            if target is not None and mask & 2:
                target = join(target, n+2, n+3)
            if target is not None:
                coefficients[mask] += mass
    return coefficients


def root_cases(polynomial, parameters, z):
    p, q, a, b, c = parameters
    rng = Random(SEED)
    s = sp.symbols("s", real=True)
    records = []
    for trial in range(24):
        values = [sp.Rational(rng.randrange(1, 8), rng.randrange(1, 6)) for _ in range(5)]
        beta = [sp.Rational(rng.randrange(0, 7), rng.randrange(1, 6)) for _ in range(5)]
        if not any(beta):
            beta[trial % 5] = 1
        substitutions = dict(zip(parameters, values))
        substitutions.update({z[i]: s*beta[i] for i in range(5)})
        value = sp.Poly(polynomial.subs(substitutions), s, domain=sp.QQ)
        degree = sum(1 for entry in beta if entry > 0)
        negative = 0
        _, factors = sp.sqf_list(value)
        for factor, multiplicity in factors:
            negative += multiplicity*factor.count_roots(-sp.oo, 0)
        assert value.degree() == degree == negative
        assert all(coefficient > 0 for coefficient in value.all_coeffs())
        records.append({
            "trial": trial,
            "p_q_a2_a3_a4": list(map(str, values)),
            "profile": list(map(str, beta)),
            "degree": degree,
            "negative_roots_counting_multiplicity": int(negative),
        })
    return records


def rational_rayleigh_stress(polynomial, parameters, z, trials=120):
    rng = Random(SEED + 1)
    coefficient_rows = []
    for exponents, coefficient in sp.Poly(polynomial, *z).terms():
        mask = sum((1 << i) for i, exponent in enumerate(exponents) if exponent)
        coefficient_rows.append((mask, coefficient))

    def evaluate(rows, point, i, j):
        total = di = dj = dij = sp.Rational(0)
        for mask, coefficient in rows:
            product_all = coefficient
            for vertex in range(5):
                if mask >> vertex & 1:
                    product_all *= point[vertex]
            total += product_all
            if mask >> i & 1:
                term = coefficient
                for vertex in range(5):
                    if vertex != i and mask >> vertex & 1:
                        term *= point[vertex]
                di += term
            if mask >> j & 1:
                term = coefficient
                for vertex in range(5):
                    if vertex != j and mask >> vertex & 1:
                        term *= point[vertex]
                dj += term
            if (mask >> i & 1) and (mask >> j & 1):
                term = coefficient
                for vertex in range(5):
                    if vertex not in (i, j) and mask >> vertex & 1:
                        term *= point[vertex]
                dij += term
        return sp.factor(di*dj-total*dij)

    minimum = None
    zeros = 0
    for _ in range(trials):
        values = [sp.Rational(rng.randrange(1, 9), rng.randrange(1, 7)) for _ in range(5)]
        rows = [(mask, sp.Rational(coefficient.subs(dict(zip(parameters, values)))))
                for mask, coefficient in coefficient_rows]
        point = [sp.Rational(rng.randrange(-12, 13), rng.randrange(1, 7)) for _ in range(5)]
        for i, j in combinations(range(5), 2):
            value = evaluate(rows, point, i, j)
            assert value >= 0, (values, point, i, j, value)
            zeros += value == 0
            minimum = value if minimum is None or value < minimum else minimum
    return {
        "parameter_and_real_spoke_specializations": trials,
        "rayleigh_pair_evaluations": trials*10,
        "exact_zeros": zeros,
        "minimum_exact_value": str(minimum),
    }


def main():
    p, q, a, b, c = sp.symbols("p q a2 a3 a4", positive=True)
    parameters = (p, q, a, b, c)
    z = sp.symbols("z0:5", real=True)
    x, y = sp.symbols("x y", real=True)
    polynomial, backbone_forests = component_polynomial(p, q, (a, b, c), z)
    assert backbone_forests == 54
    assert len(sp.Poly(polynomial, *z).terms()) == 32
    assert polynomial.subs({p:1,q:1,a:1,b:1,c:1,**{entry:1 for entry in z}}) == 712
    for coefficient in sp.Poly(polynomial, *z).coeffs():
        assert positive_coefficients(coefficient, parameters)
    # Simultaneously permuting arm weights and their spoke variables leaves P
    # invariant. These two transpositions generate all arm permutations.
    assert sp.expand(simultaneous_swaps(polynomial, [(a,b),(z[2],z[3])])-polynomial) == 0
    assert sp.expand(simultaneous_swaps(polynomial, [(b,c),(z[3],z[4])])-polynomial) == 0

    parameter_sum = p + q
    xb, xc = z[3] + parameter_sum*b + 1, z[4] + parameter_sum*c + 1
    form_r_bc = pair_form(b, c, p, q)
    form_q_abc = triple_form(a, b, c, p, q)

    # Template 1: endpoint--endpoint, collected in the arm-a spoke z2.
    d01 = rayleigh(polynomial, z, 0, 1)
    lead01, _, _, disc01 = quadratic_data(d01, z[2])
    phi_endpoint = (
        c*c*(c*p+1)*(c*q+1)*x*x
        + 2*p*q*b*b*c*c*x*y
        + b*b*(b*p+1)*(b*q+1)*y*y
    )
    psi_endpoint = (
        c*c*pair_form(a, c, p, q)*x*x
        + 2*p*q*b*b*c*c*(1+parameter_sum*a)*x*y
        + b*b*pair_form(a, b, p, q)*y*y
    )
    checks = [
        sp.expand(lead01 - p*q*phi_endpoint.subs({x:xb,y:xc})) == 0,
        sp.expand(disc01 + 4*a*a*p*p*q*q*xb*xb*xc*xc
                  * psi_endpoint.subs({x:xb,y:xc})) == 0,
        sp.expand(d01.subs({z[3]:-parameter_sum*b-1,z[4]:-parameter_sum*c-1})) == 0,
        sp.expand(
            (c*c*(c*p+1)*(c*q+1))*(b*b*(b*p+1)*(b*q+1))
            - (p*q*b*b*c*c)**2 - b*b*c*c*form_r_bc
        ) == 0,
        sp.expand(
            (c*c*pair_form(a,c,p,q))*(b*b*pair_form(a,b,p,q))
            - (p*q*b*b*c*c*(1+parameter_sum*a))**2
            - b*b*c*c*(a*p+1)*(a*q+1)*form_q_abc
        ) == 0,
    ]

    # Template 2: endpoint--internal.  Both separate axes are essential.
    d02 = rayleigh(polynomial, z, 0, 2)
    lead02, _, _, disc02 = quadratic_data(d02, z[1])
    boundary_b = a*b*b*p*q*q*(b*q+1)*(2+parameter_sum*(a+b))*xc*xc
    boundary_c = a*c*c*p*q*q*(c*q+1)*(2+parameter_sum*(a+c))*xb*xb
    checks += [
        sp.expand(lead02 - a*p*(a*p+1)*xb*xb*xc*xc) == 0,
        sp.expand(disc02-disc01) == 0,
        sp.expand(d02.subs(z[3],-parameter_sum*b-1)-boundary_b) == 0,
        sp.expand(d02.subs(z[4],-parameter_sum*c-1)-boundary_c) == 0,
    ]
    d12 = rayleigh(polynomial, z, 1, 2)
    lead12, _, _, disc12 = quadratic_data(d12, z[0])
    boundary_b_1 = a*b*b*q*p*p*(b*p+1)*(2+parameter_sum*(a+b))*xc*xc
    boundary_c_1 = a*c*c*q*p*p*(c*p+1)*(2+parameter_sum*(a+c))*xb*xb
    checks += [
        sp.expand(lead12 - a*q*(a*q+1)*xb*xb*xc*xc) == 0,
        sp.expand(disc12-disc01) == 0,
        sp.expand(d12.subs(z[3],-parameter_sum*b-1)-boundary_b_1) == 0,
        sp.expand(d12.subs(z[4],-parameter_sum*c-1)-boundary_c_1) == 0,
    ]

    # Template 3: internal--internal, pair arms a,b and collect in unused c.
    h0, h1 = p*(a+b+c)+1, q*(a+b+c)+1
    u0, u1 = z[0]+h0, z[1]+h1
    d23 = rayleigh(polynomial, z, 2, 3)
    lead23, _, _, disc23 = quadratic_data(d23, z[4])
    theta_internal = (
        q*q*(a*q+1)*(b*q+1)*x*x
        + 2*a*b*p*p*q*q*x*y
        + p*p*(a*p+1)*(b*p+1)*y*y
    )
    omega = sp.cancel(-disc23/(4*a*a*b*b*c*c*p*p*q*q))
    omega_shifted = sp.expand(omega.subs({z[0]:x-h0,z[1]:y-h1}))
    omega_poly = sp.Poly(omega_shifted, x, y)
    omega_x = omega_poly.coeff_monomial(x*x)
    omega_xy = omega_poly.coeff_monomial(x*y)
    omega_y = omega_poly.coeff_monomial(y*y)
    assert len(omega_poly.terms()) == 3
    assert positive_coefficients(sp.cancel(omega_x/(q*q)), parameters)
    assert positive_coefficients(sp.cancel(omega_y/(p*p)), parameters)
    checks += [
        sp.expand(lead23 - a*b*theta_internal.subs({x:u0,y:u1})) == 0,
        sp.expand(disc23 + 4*a*a*b*b*c*c*p*p*q*q
                  * omega_shifted.subs({x:u0,y:u1})) == 0,
        sp.expand(d23.subs({z[0]:-h0,z[1]:-h1})
                  - a*b*c*c*p*p*q*q*(2+parameter_sum*(a+c))
                    *(2+parameter_sum*(b+c))) == 0,
        sp.expand(
            (q*q*(a*q+1)*(b*q+1))*(p*p*(a*p+1)*(b*p+1))
            - (a*b*p*p*q*q)**2 - p*p*q*q*pair_form(a,b,p,q)
        ) == 0,
        sp.expand(
            omega_x*omega_y-(omega_xy/2)**2
            - p*p*q*q*(2+parameter_sum*(a+b))*(2+parameter_sum*(a+c))
              *(2+parameter_sum*(b+c))*form_q_abc
        ) == 0,
    ]
    assert all(checks), checks

    stress = rational_rayleigh_stress(polynomial, parameters, z)
    profiles = root_cases(polynomial, parameters, z)
    rows = [Fraction(1,2),Fraction(2,3),Fraction(3,4),Fraction(4,5)]
    marked_input = [
        (Fraction(1),Fraction(2),(Fraction(1),Fraction(3),Fraction(2)),[1,2,0,0,0]),
        (Fraction(2,3),Fraction(5,2),(Fraction(4,3),Fraction(1,2),Fraction(3)),[0,1,3,0,0]),
        (Fraction(7,4),Fraction(1,5),(Fraction(2),Fraction(5,3),Fraction(1,4)),[0,0,1,2,0]),
        (Fraction(3),Fraction(4),(Fraction(5,3),Fraction(2,5),Fraction(7,2)),[1,0,0,0,5]),
        (Fraction(1),Fraction(3),(Fraction(7,2),Fraction(2),Fraction(4,5)),[2,0,0,0,0]),
        (Fraction(5,4),Fraction(2),(Fraction(1,7),Fraction(3),Fraction(5,2)),[0,0,0,0,0]),
    ]
    marked = []
    for pv,qv,arms,beta in marked_input:
        coefficients = direct_marked(pv,qv,arms,beta,rows)
        difference = coefficients[1]*coefficients[2]-coefficients[0]*coefficients[3]
        strict = sum(value > 0 for value in beta) >= 2
        assert difference >= 0 and (difference > 0) == strict
        marked.append({
            "p_q_arms": [str(pv),str(qv),*map(str,arms)],
            "profile": list(map(str,beta)), "EF_minus_AC": str(difference),
            "strict": strict,
        })

    report = {
        "status":"PASS; exact independent rank-one theta audit",
        "implementation":"64 backbone subsets/component factors; no author probe",
        "sympy_version":sp.__version__, "backbone_forests":backbone_forests,
        "apex_polynomial_terms":len(sp.Poly(polynomial,*z).terms()),
        "unit_activity_augmented_forests":712,
        "generic_symbolic_template_checks":len(checks),
        "omega_x_coefficient_terms":len(sp.Poly(omega_x/(q*q),*parameters).terms()),
        "omega_y_coefficient_terms":len(sp.Poly(omega_y/(p*p),*parameters).terms()),
        "endpoint_internal_boundaries":{
            "endpoint_0_X_b_zero":str(sp.factor(boundary_b/xc**2)),
            "endpoint_0_X_c_zero":str(sp.factor(boundary_c/xb**2)),
            "endpoint_1_X_b_zero":str(sp.factor(boundary_b_1/xc**2)),
            "endpoint_1_X_c_zero":str(sp.factor(boundary_c_1/xb**2)),
        },
        "rational_rayleigh_stress":stress,
        "univariate_profile_cases":profiles,
        "direct_marked_cases":marked,
        "summary":{
            "generic_symbolic_template_checks":len(checks),
            "exact_rayleigh_pair_evaluations":stress["rayleigh_pair_evaluations"],
            "exact_univariate_root_cases":len(profiles),
            "direct_marked_cases":len(marked),
            "strict_marked_cases":sum(row["strict"] for row in marked),
            "equality_marked_cases":sum(not row["strict"] for row in marked),
            "counterexamples":0,
        },
    }
    OUT.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report["summary"],indent=2))


if __name__ == "__main__":
    main()
