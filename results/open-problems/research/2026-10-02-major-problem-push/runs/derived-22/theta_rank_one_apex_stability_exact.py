#!/usr/bin/env python3
"""Exact certificate for rank-one positive edge weights on K_{2,3}.

The backbone edges are (0,j),(1,j), j=2,3,4, with weights
    p*a_j, q*a_j.
The script constructs the apex-spoke forest polynomial and proves its three
Rayleigh templates by exact polynomial identities and binary-form minors.
"""

import itertools
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


def forest_polynomial(p, q, arms, z):
    edges = [(0,j) for j in (2,3,4)] + [(1,j) for j in (2,3,4)]
    weights = [p*t for t in arms] + [q*t for t in arms]
    answer = 0
    backbone_count = 0
    augmented_count = 0
    for mask in range(64):
        chosen = [edges[k] for k in range(6) if mask >> k & 1]
        if not is_forest(5, chosen):
            continue
        backbone_count += 1
        weight = sp.prod(weights[k] for k in range(6) if mask >> k & 1)
        parent = list(range(5))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for u, v in chosen:
            ru, rv = find(u), find(v)
            parent[ru] = rv
        components = {}
        for i in range(5):
            components.setdefault(find(i), []).append(i)
        factor = sp.prod(1 + sum(z[i] for i in C) for C in components.values())
        answer += weight * factor
        # A component admits either no apex edge or one edge from the apex.
        augmented_count += sp.prod(1 + len(C) for C in components.values())
    return sp.expand(answer), backbone_count, int(augmented_count)


def rayleigh(P, z, i, j):
    return sp.expand(sp.diff(P,z[i])*sp.diff(P,z[j])
                     - P*sp.diff(P,z[i],z[j]))


def quadratic_data(F, t):
    coeffs = sp.Poly(F,t).all_coeffs()
    coeffs = [sp.Integer(0)]*(3-len(coeffs)) + coeffs
    A,B,C = map(sp.expand,coeffs)
    return A,B,C,sp.expand(B*B-4*A*C)


def coefficient_positive(expr, parameters):
    coeffs = sp.Poly(sp.expand(expr),*parameters).coeffs()
    return bool(coeffs) and all(c.is_nonnegative for c in coeffs) and any(c>0 for c in coeffs)


def binary_certificate(expr, x, y, parameters):
    """Strip a common x^m y^n and certify a positive-definite binary form."""
    poly = sp.Poly(sp.expand(expr),x,y)
    monomials = [m for m,_ in poly.terms()]
    mx = min(m[0] for m in monomials)
    my = min(m[1] for m in monomials)
    core = sp.cancel(expr/(x**mx*y**my))
    cp = sp.Poly(sp.expand(core),x,y)
    assert cp.total_degree() == 2
    U = cp.coeff_monomial(x*x)
    twoV = cp.coeff_monomial(x*y)
    W = cp.coeff_monomial(y*y)
    determinant = sp.expand(U*W-twoV*twoV/4)
    assert coefficient_positive(U,parameters)
    assert coefficient_positive(W,parameters)
    assert coefficient_positive(determinant,parameters)
    return {
        "removed_monomial": [mx,my],
        "U_term_count": len(sp.Poly(sp.expand(U),*parameters).terms()),
        "W_term_count": len(sp.Poly(sp.expand(W),*parameters).terms()),
        "determinant_term_count": len(sp.Poly(determinant,*parameters).terms()),
        "determinant_factorization": str(sp.factor(determinant)),
    }


def binary_determinant(expr, x, y):
    cp = sp.Poly(sp.expand(expr),x,y)
    U = cp.coeff_monomial(x*x)
    twoV = cp.coeff_monomial(x*y)
    W = cp.coeff_monomial(y*y)
    return sp.expand(U*W-twoV*twoV/4)


def main():
    p,q,a,b,c = sp.symbols("p q a b c", positive=True)
    z = sp.symbols("z0:5", real=True)
    x,y = sp.symbols("x y", real=True)
    parameters = (p,q,a,b,c)
    P, backbone_count, augmented_count = forest_polynomial(p,q,(a,b,c),z)

    s = p+q
    ha,hb,hc = 1+a*s,1+b*s,1+c*s
    h0,h1 = 1+p*(a+b+c),1+q*(a+b+c)
    checks = []
    R = lambda u,v: (1+s*(u+v)+p*q*(u*u+v*v)+s*s*u*v
                     +p*q*s*u*v*(u+v))
    arms = (a,b,c)
    ordered_cubic = sum(u*u*v for u in arms for v in arms if u != v)
    S = (1+s*sum(arms)+p*q*sum(u*u for u in arms)
         +s*s*(a*b+a*c+b*c)+p*q*s*ordered_cubic
         +p*q*s*s*a*b*c*sum(arms)+s**3*a*b*c)

    # Template E-E: endpoint pair (0,1), quadratic in arm-spoke z2.
    F01 = sp.expand(rayleigh(P,z,0,1).subs({z[3]:x-hb,z[4]:y-hc}))
    A01,B01,C01,D01 = quadratic_data(F01,z[2])
    expected_A01 = p*q*(c*c*(c*p+1)*(c*q+1)*x*x
                         +2*b*b*c*c*p*q*x*y
                         +b*b*(b*p+1)*(b*q+1)*y*y)
    checks.append(sp.expand(A01-expected_A01)==0)
    checks.append(sp.expand(binary_determinant(A01,x,y)
                            -b*b*c*c*p*p*q*q*R(b,c))==0)
    checks.append(sp.expand(F01.subs(x,0)
        -b*b*p*q*y*y*(b*p+1)*(b*q+1)*(z[2]+ha)**2)==0)
    checks.append(sp.expand(F01.subs(y,0)
        -c*c*p*q*x*x*(c*p+1)*(c*q+1)*(z[2]+ha)**2)==0)
    ee_lead = binary_certificate(A01,x,y,parameters)
    assert sp.rem(sp.Poly(-D01,x),sp.Poly(x*x,x)) == 0
    phi = sp.cancel(-D01/(4*a*a*p*p*q*q*x*x*y*y))
    ee_disc = binary_certificate(phi,x,y,parameters)
    checks.append(sp.expand(binary_determinant(phi,x,y)
        -b*b*c*c*(a*p+1)*(a*q+1)*S)==0)

    # Template E-I: endpoint 0 and arm vertex 2, quadratic in z1.
    F02 = sp.expand(rayleigh(P,z,0,2).subs({z[3]:x-hb,z[4]:y-hc}))
    A02,B02,C02,D02 = quadratic_data(F02,z[1])
    checks.append(sp.expand(A02-a*p*(a*p+1)*x*x*y*y)==0)
    checks.append(sp.expand(D02-D01)==0)
    checks.append(sp.expand(F02.subs(x,0)
        -a*b*b*p*q*q*y*y*(b*q+1)*(a*s+b*s+2))==0)
    checks.append(sp.expand(F02.subs(y,0)
        -a*c*c*p*q*q*x*x*(c*q+1)*(a*s+c*s+2))==0)

    # Template I-I: arm vertices 2,3, quadratic in the unused arm-spoke z4.
    F23 = sp.expand(rayleigh(P,z,2,3).subs({z[0]:x-h0,z[1]:y-h1}))
    A23,B23,C23,D23 = quadratic_data(F23,z[4])
    expected_A23 = a*b*(q*q*(a*q+1)*(b*q+1)*x*x
                         +2*a*b*p*p*q*q*x*y
                         +p*p*(a*p+1)*(b*p+1)*y*y)
    checks.append(sp.expand(A23-expected_A23)==0)
    checks.append(sp.expand(binary_determinant(A23,x,y)
                            -a*a*b*b*p*p*q*q*R(a,b))==0)
    center23 = a*b*c*c*p*p*q*q*(a*s+c*s+2)*(b*s+c*s+2)
    checks.append(sp.expand(F23.subs({x:0,y:0})-center23)==0)
    ii_lead = binary_certificate(A23,x,y,parameters)
    omega = sp.cancel(-D23/(4*a*a*b*b*c*c*p*p*q*q))
    ii_disc = binary_certificate(omega,x,y,parameters)
    checks.append(sp.expand(binary_determinant(omega,x,y)
        -p*p*q*q*(2+s*(a+b))*(2+s*(a+c))*(2+s*(b+c))*S)==0)

    assert all(checks), checks
    # The three templates cover all ten pairs by S_3 arm permutations and
    # endpoint interchange p<->q.
    pair_reductions = {
        "endpoint_endpoint": [[0,1]],
        "endpoint_internal": [[e,j] for e in (0,1) for j in (2,3,4)],
        "internal_internal": [list(pair) for pair in itertools.combinations((2,3,4),2)],
    }
    report = {
        "status":"PASS",
        "sympy_version":sp.__version__,
        "scope":"K_{2,3}: w_(0,j)=p*a_j and w_(1,j)=q*a_j, all five parameters positive",
        "backbone_forests":backbone_count,
        "augmented_forests_at_unit_weights":augmented_count,
        "spoke_polynomial_terms":len(sp.Poly(P,*z).terms()),
        "template_identity_checks":len(checks),
        "pair_reductions":pair_reductions,
        "certificates":{
            "endpoint_pair_leading_form":ee_lead,
            "shared_endpoint_discriminant_form":ee_disc,
            "internal_pair_leading_form":ii_lead,
            "internal_pair_discriminant_form":ii_disc,
        },
        "conclusion":"all ten Rayleigh differences are nonnegative on R^5; the multiaffine polynomial is real stable",
    }
    out=Path(__file__).with_name("theta_rank_one_apex_stability_exact_results.json")
    out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__ == "__main__":
    main()
