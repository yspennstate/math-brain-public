#!/usr/bin/env python3
"""Finite checks of X046's determinant-design Fisher allocation.

No random search. Exact four-site atom jets are checked independently;
one 64-site occupation table is summed by its exact permutation orbits.
"""
import json
import math
from itertools import product
from pathlib import Path

import numpy as np
import sympy as s

Q = s.Rational
I = s.I
checks = 0


def check(ok, label):
    global checks
    if not ok:
        raise AssertionError(label)
    checks += 1


def eq(a, b=0):
    if isinstance(a, s.MatrixBase):
        diff = a-b if isinstance(b, s.MatrixBase) else a
        return all(s.simplify(x) == 0 for x in diff)
    return s.simplify(a - b) == 0


def pd(A):
    return all(s.simplify(A[:k, :k].det()) > 0
               for k in range(1, A.rows + 1))


def atom(K, z):
    eye = s.eye(K.rows)
    return s.expand(s.Matrix.hstack(*[
        K[:, j] if z[j] else (eye - K)[:, j]
        for j in range(K.rows)]).det())


def exact_four(label, M, bound_m, positive):
    V = s.Matrix([[1, 1], [1, -1], [1, I], [1, -I]]) / 2
    E = s.Matrix([[1, (1 + I)/3], [(1 - I)/3, 2]])
    n, t = 4, s.Symbol('t', real=True)
    K = s.eye(n)/2 + V*M*V.conjugate().T
    A = V*E*V.conjugate().T
    check(eq(V.conjugate().T*V, s.eye(2)), label+' Parseval')
    check(pd(bound_m*s.eye(2)-M), label+' upper active bound')
    check(pd(M if positive else bound_m*s.eye(2)+M), label+' lower active bound')
    check(pd(E), label+' definite direction')
    check(not eq(M*E, E*M), label+' noncommuting direction')
    states = list(product([0, 1], repeat=n))
    p, dp, ddp = {}, {}, {}
    detT = {}
    for z in states:
        T = V.conjugate().T*s.diag(*[2 if b else -2 for b in z])*V
        poly = s.Poly(atom(K+t*A, z), t)
        p[z], dp[z], ddp[z] = poly.nth(0), poly.nth(1), 2*poly.nth(2)
        detT[z] = T.det()
        check(poly.degree() <= 2, label+' atom degree')
        check(eq(poly.as_expr(), (s.eye(2)+(M+t*E)*T).det()/16), label+' full atom jet')
        check(eq(ddp[z], E.det()*T.det()/8), label+' second jet')
        check(p[z] > 0, label+' positive atom')
    check(eq(sum(p.values()), 1), label+' normalized atoms')
    check(eq(sum(dp.values())), label+' normalized first jet')
    check(eq(sum(ddp.values())), label+' normalized second jet')
    C = s.zeros(n)
    J = s.S.Zero
    max_face = 0.0
    for i in range(n):
        for j in range(i+1, n):
            c = s.simplify(abs(V[[i, j], :].det())**2)
            C[i, j] = C[j, i] = c
            rest = [k for k in range(n) if k not in (i, j)]
            for r in product([0, 1], repeat=n-2):
                zs = []
                for a, b in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                    z = dict(zip(rest, r)); z[i], z[j] = a, b
                    zs.append(tuple(z[k] for k in range(n)))
                z00, z10, z01, z11 = zs
                ratio = s.cancel(p[z10]*p[z01]/(p[z00]*p[z11]))
                check(ratio >= 1, label+' face logarithm sign')
                ell = s.log(ratio)
                J += c*ell/4
                max_face = max(max_face, float(ell))
    check(eq(C*s.ones(n, 1), s.ones(n, 1)/2), label+' volume marginal')
    Sigma = s.Matrix(n, n, lambda i, j:
                     K[i, i]*(1-K[i, i]) if i == j else -abs(K[i, j])**2)
    check(pd(Sigma), label+' positive occupation covariance')
    direct_cov = s.zeros(n)
    for z in states:
        dz = s.Matrix(z)-s.Matrix([K[i, i] for i in range(n)])
        direct_cov += p[z]*dz*dz.T
    check(eq(direct_cov, Sigma), label+' actual occupation covariance')
    check(eq(sum(dp[z]*sum(z) for z in states), s.trace(E)), label+' count score')
    FI = sum(dp[z]**2/p[z] for z in states)
    negH = FI + sum(ddp[z]*s.log(p[z]) for z in states)
    remainder = s.expand_log(negH-FI+2*E.det()*J, force=True)
    check(abs(float(remainder.evalf(50))) < 1e-45, label+' complete entropy identity')
    qlog = sum(detT[z]*s.log(p[z])/16 for z in states)
    check(abs(float((qlog+J).evalf(50))) < 1e-45, label+' Bernoulli face allocation')
    sf = np.array(Sigma, dtype=float)
    cf = np.array(C, dtype=float)
    ds, us = np.linalg.eigh(sf)
    sinv = (us/np.sqrt(ds))@us.T
    lam = np.linalg.eigvalsh(sinv@cf@sinv)[-1]
    check(float(FI) >= 2*float(E.det())*lam-1e-12, label+' optimal design lower bound')
    b = 2*bound_m/(Q(1, 2)-bound_m)
    denom = n*(n+4*b if positive else n-4*b)
    logbound = float(s.log((n+(2*b if positive else -2*b))**2/denom))
    check(max_face <= logbound+1e-12, label+' uniform Schur face bound')
    check(float(J) <= logbound+1e-12, label+' volume average bound')
    check(float(negH) >= float((Q(16, n)-2*s.log((n+(2*b if positive else -2*b))**2/denom))*E.det())-1e-12,
          label+' proved entropy surplus')
    return dict(FI=float(FI), J=float(J), negative_entropy_curvature=float(negH),
                design_eigenvalue=lam, uniform_log_bound=logbound,
                max_face_log=max_face)


def orbit64():
    """Four row types, each repeated 16 times; all 2^64 atoms are included."""
    size, n = 16, 64
    M = np.array([[1/3, (1+1j)/20], [(1-1j)/20, -1/4]], complex)
    E = np.array([[1, (1+1j)/3], [(1-1j)/3, 2]], complex)
    detm, dete = np.linalg.det(M).real, np.linalg.det(E).real
    adjm = np.trace(M)*np.eye(2)-M
    mixed = np.trace(adjm@E).real
    phases = [1, -1, 1j, -1j]
    effects = [np.array([[1, p], [np.conj(p), 1]], complex)/n for p in phases]
    weighted_mass, first_mass, second_mass, fi, interaction = [], [], [], [], []
    min_g = math.inf
    for ks in product(range(size+1), repeat=4):
        weight = math.prod(math.comb(size, k) for k in ks)/2**n
        T = sum((4*k-2*size)*effect for k, effect in zip(ks, effects))
        dett = np.linalg.det(T).real
        g = 1+np.trace(M@T).real+detm*dett
        h = np.trace(E@T).real+mixed*dett
        check(g > 0, '64-site positive atom orbit')
        min_g = min(min_g, g)
        weighted_mass.append(weight*g)
        first_mass.append(weight*h)
        second_mass.append(weight*2*dete*dett)
        fi.append(weight*h*h/g)
        interaction.append(-weight*dett*math.log(g))
    F, J = math.fsum(fi), math.fsum(interaction)
    check(abs(math.fsum(weighted_mass)-1) < 1e-13, '64-site normalized atoms')
    check(abs(math.fsum(first_mass)) < 1e-13, '64-site normalized first jet')
    check(abs(math.fsum(second_mass)) < 1e-13, '64-site normalized second jet')
    check(np.linalg.eigvalsh(M).min() > -0.4 and np.linalg.eigvalsh(M).max() < 0.4,
          '64-site signed active domain')
    check(J <= math.log(9/8), '64-site signed volume bound')
    check(F-2*dete*J >= dete*(0.25-2*math.log(9/8))-1e-12,
          '64-site complete curvature bound')
    return dict(occupation_atoms=str(2**n), orbit_records=(size+1)**4,
                FI=F, J=J, negative_entropy_curvature=F-2*dete*J,
                proved_lower_bound=dete*(0.25-2*math.log(9/8)),
                minimum_atom_factor=min_g)


def design_limit():
    eps = s.Symbol('epsilon', positive=True)
    K = s.eye(3)/2+(eps-Q(1, 2))*s.ones(3)/3
    masses = [(1-eps)/4, (2-eps)/12, (1+eps)/12, eps/4]
    for z in product([0, 1], repeat=3):
        check(eq(atom(K, z), masses[sum(z)]), 'exact three-site design obstruction atom')
    ratio = s.cancel((masses[1]**2/(masses[0]*masses[2]))
                     *(masses[2]**2/(masses[1]*masses[3])))
    check(eq(ratio, (2-eps)*(1+eps)/(9*eps*(1-eps))), 'exact design obstruction J')
    var_count = Q(1, 2)+eps-eps**2
    sigma_row = K[0, 0]*(1-K[0, 0])-2*K[0, 1]**2
    check(eq(3*sigma_row, var_count), 'exact design obstruction covariance')
    e0 = Q(1, 10**6)
    check(ratio.subs(eps, e0) > 3**8, 'J>4 using the elementary e<3 bound')
    check((2/var_count).subs(eps, e0) < 4, 'Lambda<4 in design obstruction')
    return dict(epsilon=str(e0), J=float(s.log(ratio.subs(eps, e0))/2),
                design_eigenvalue=float((2/var_count).subs(eps, e0)),
                conclusion='The universal stronger condition J<=Lambda is false.')


def main():
    results = {}
    results['positive_four_site'] = exact_four(
        'positive4', s.Matrix([[Q(3, 8), I/40], [-I/40, Q(1, 3)]]), Q(2, 5), True)
    results['signed_four_site'] = exact_four(
        'signed4', s.Matrix([[Q(1, 20), I/40], [-I/40, -Q(1, 15)]]), Q(1, 10), False)
    results['signed_64_site'] = orbit64()
    results['design_obstruction'] = design_limit()
    check(Q(64, 5)-6 > 2, 'exact failure of determinant-correlation sufficient threshold')
    results['checks'] = checks
    results['status'] = 'PASS'
    results['verification_provenance'] = {
        'four_site_algebra': 'Exact rational SymPy atom, covariance, and determinant identities.',
        'four_site_log_identities': 'Residuals evaluated at 50 decimal digits; signs proved in report.',
        'design_eigenvalues': 'Double-precision numerical verification of the proved inequality.',
        '64_site_orbits': 'Exact integer binomial multiplicities; double-precision weighted sums.',
        'universal_signs': 'Elementary inequalities in agents/X046.md, not numerical sampling.'}
    path = Path(__file__).with_name('certificate.json')
    path.write_text(json.dumps(results, indent=2)+'\n')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
