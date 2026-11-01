#!/usr/bin/env python3
"""Exact finite checks of X040's Boolean second-cumulant identity."""
import json
from itertools import product
from pathlib import Path
import sympy as s

Q = s.Rational
ii = s.I
n = 4
ident = s.eye(n)
t = s.Symbol("t", real=True)
D = s.diag(Q(1, 5), Q(1, 4), Q(3, 10), Q(1, 3))
B = s.Matrix([[1, 0], [0, 1], [1, 1], [1, ii]]) / 2
M0 = s.Matrix([[Q(1, 4), Q(1, 20)], [Q(1, 20), Q(1, 3)]])
E = s.Matrix([[Q(1, 10), (1-ii)/12], [(1+ii)/12, -Q(1, 10)]])
states = list(product([0, 1], repeat=n))
count = 0


def check(condition, label):
    global count
    if not condition:
        raise AssertionError(label)
    count += 1


def zero(expr):
    return s.cancel(s.expand(expr)) == 0


def positive_definite(mat):
    return all(s.simplify(mat[:k, :k].det()) > 0 for k in range(1, mat.rows+1))


def direct_atom(K, z):
    cols = [K[:, j] if z[j] else (ident-K)[:, j] for j in range(n)]
    return s.cancel(s.Matrix.hstack(*cols).det(method="domain-ge"))


def verify_case(label, M, direction):
    K = D+B*M*B.conjugate().T
    A = B*direction*B.conjugate().T
    delta = s.simplify(direction.det())
    check(positive_definite(K), label+" K>0")
    check(positive_definite(ident-K), label+" K<I")
    check(delta < 0, label+" indefinite direction")
    probs, first, second, q, g, face_coeff = {}, {}, {}, {}, {}, {}
    T = {}
    for z in states:
        q[z] = s.prod(D[j,j] if z[j] else 1-D[j,j] for j in range(n))
        eta = [1/D[j,j] if z[j] else -1/(1-D[j,j]) for j in range(n)]
        T[z] = B.conjugate().T*s.diag(*eta)*B
        direct = direct_atom(K+t*A, z)
        expected = q[z]*(s.eye(2)+(M+t*direction)*T[z]).det()
        check(zero(direct-expected), label+" atom polynomial "+str(z))
        poly = s.Poly(direct, t)
        check(poly.degree() <= 2, label+" rank-two degree "+str(z))
        probs[z] = poly.nth(0)
        first[z] = poly.nth(1)
        second[z] = 2*poly.nth(2)
        check(probs[z] > 0, label+" positive atom "+str(z))
        g[z] = s.cancel(q[z]*T[z].det())
        check(zero(second[z]-2*delta*g[z]), label+" second jet "+str(z))
        expected_first = q[z]*(s.trace(direction*T[z])
                              +s.trace(M.adjugate()*direction)*T[z].det())
        check(zero(first[z]-expected_first), label+" first jet "+str(z))
        face_coeff[z] = s.S.Zero
    check(sum(probs.values()) == 1, label+" normalization")
    check(sum(first.values()) == 0, label+" derivative normalization")
    check(sum(second.values()) == 0, label+" second normalization")
    interaction = s.S.Zero
    face_terms = []
    for i in range(n):
        for j in range(i+1, n):
            c = s.simplify(abs(B[[i,j], :].det())**2)
            check(c >= 0, label+" wedge positivity")
            rest = [k for k in range(n) if k not in (i, j)]
            for r in product([0,1], repeat=n-2):
                zr = dict(zip(rest, r))
                qr = s.prod(D[k,k] if zr[k] else 1-D[k,k] for k in rest)
                face = {}
                for a, b in product([0,1], repeat=2):
                    z = tuple(a if k == i else b if k == j else zr[k] for k in range(n))
                    face[(a,b)] = z
                    face_coeff[z] += c*qr*(1 if a == b else -1)
                odds = s.cancel(probs[face[(1,0)]]*probs[face[(0,1)]]
                                /(probs[face[(0,0)]]*probs[face[(1,1)]]))
                check(odds >= 1, label+" conditional face sign")
                face_terms.append((c*qr, odds))
                interaction += c*qr*s.log(odds)
    for z in states:
        check(zero(g[z]-face_coeff[z]), label+" full formal log coefficient "+str(z))
    fisher = s.cancel(sum(first[z]**2/probs[z] for z in states))
    diagonal_norm = s.simplify(sum(A[j,j]**2 for j in range(n)))
    check(fisher >= 2*diagonal_norm, label+" occupation Fisher bound")
    curvature = fisher-2*delta*interaction
    direct_curvature = fisher+sum(second[z]*s.log(probs[z]) for z in states)
    error = abs(s.N(curvature-direct_curvature, 60))
    check(error < s.Float("1e-50"), label+" displayed Hessian evaluation")
    return {
        "atoms": len(states),
        "faces": len(face_terms),
        "det_direction": str(delta),
        "active_determinant": str(s.simplify(M.det())),
        "full_fisher": str(s.N(fisher, 25)),
        "face_interaction": str(s.N(interaction, 25)),
        "minus_entropy_curvature": str(s.N(curvature, 25)),
        "diagonal_norm_squared": str(diagonal_norm),
        "hessian_evaluation_error": str(error),
    }


results = {"positive_active": verify_case("positive active", M0, E)}
Mindef = s.Matrix([[Q(1,10), Q(1,20)+ii/30], [Q(1,20)-ii/30, -Q(1,10)]])
check(Mindef.det() < 0, "second active base is indefinite")
results["indefinite_active"] = verify_case("indefinite active", Mindef, E/4)
A = s.simplify(B*E*B.conjugate().T)
check(E.det() == -Q(43,1800), "exact det E")
check(A.diagonal() == s.Matrix([[Q(1,40), -Q(1,40), Q(1,24), -Q(1,24)]]), "physical means")
check(s.trace(A) == 0, "fixed expected count")
check(M0*E-E*M0 != s.zeros(2), "noncommuting active matrices")
check(sum(A[j,j]**2 for j in range(n)) == Q(17,3600), "uniform Jensen gap constant")
for u in [-1,0,1]:
    Ku = D+B*(M0+u*E)*B.conjugate().T
    check(positive_definite(Ku), "interval endpoint K>0")
    check(positive_definite(ident-Ku), "interval endpoint K<I")
    check(positive_definite(M0+u*E), "interval active positive")
certificate = {"status": "PASS", "exact_and_display_assertions": count, "cases": results,
               "uniform_minus_second_derivative_bound": "17/1800",
               "whole_interval_midpoint_gap_bound": "17/3600",
               "note": "Finite checks supplement the analytic interval proof. Only the final displayed-log equality uses high precision; coefficient equality and every sign/constant are exact."}
Path(__file__).with_name("certificate.json").write_text(json.dumps(certificate, indent=2)+"\n")
print(json.dumps(certificate, indent=2))
