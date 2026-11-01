#!/usr/bin/env python3
"""Exact certificates for C057. Uses SymPy for rational matrix arithmetic.

No numerical Hessian eigensolver or sampled sign test is used as a proof.
The full conditional identity is checked as a quadratic form at two rational
kernels, with every logarithm expanded into formal logarithms of primes.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path

import sympy as sp

R = sp.Rational
OUT = Path(__file__).resolve().parent


def clean(x):
    x = sp.simplify(sp.expand_complex(x))
    assert x.is_Rational, x
    return R(x)


def add(f, g, scale=R(1)):
    h = dict(f)
    for p, c in g.items():
        h[p] = clean(h.get(p, R(0)) + scale * c)
        if not h[p]:
            del h[p]
    return h


def log_form(x, coefficient=R(1)):
    """Prime 0 is reserved for a nonlogarithmic constant."""
    x = clean(x)
    assert x > 0
    ans = {}
    for sign, integer in [(1, sp.numer(x)), (-1, sp.denom(x))]:
        for p, power in sp.factorint(integer).items():
            ans[int(p)] = ans.get(int(p), R(0)) + coefficient * sign * power
    return {p: clean(c) for p, c in ans.items() if c}


def atom_data(K):
    n = K.rows
    ans = []
    for mask in range(1 << n):
        absent = [i for i in range(n) if not (mask >> i) & 1]
        Q = K - sp.diag(*[int(i in absent) for i in range(n)])
        p = clean((-1) ** len(absent) * Q.det())
        assert p > 0
        ans.append((mask, p, Q.inv()))
    assert sum(p for _, p, _ in ans) == 1
    return ans


def grad_form(data, A):
    ans = {}
    for _, p, Qinv in data:
        p1 = clean(p * sp.trace(Qinv * A))
        ans = add(ans, log_form(p), -p1)
    return ans


def hess_form(data, A):
    ans = {}
    for _, p, Qinv in data:
        T = Qinv * A
        p1 = clean(p * sp.trace(T))
        p2 = clean(p * (sp.trace(T) ** 2 - sp.trace(T * T)))
        ans = add(ans, {0: -p1 * p1 / p})
        ans = add(ans, log_form(p), -p2)
    return ans


def basis(n):
    ans = []
    for i in range(n):
        A = sp.zeros(n)
        A[i, i] = 1
        ans.append(A)
    for i, j in combinations(range(n), 2):
        A = sp.zeros(n)
        A[i, j] = A[j, i] = 1
        ans.append(A)
        A = sp.zeros(n)
        A[i, j], A[j, i] = sp.I, -sp.I
        ans.append(A)
    return ans


def condition(K):
    a = K[0, 0]
    b = 1 - a
    z = K[1:, 0]
    B = K[1:, 1:]
    F1 = B - z * z.H / a
    F0 = B + z * z.H / b
    return a, b, z, B, F1, F0


def verify_full_identity(K):
    a, b, z, B, F1, F0 = condition(K)
    q = a * b
    all_data, data1, data0 = atom_data(K), atom_data(F1), atom_data(F0)
    bs = basis(K.rows)
    directions = bs + [bs[i] + bs[j] for i, j in combinations(range(len(bs)), 2)]
    for A in directions:
        alpha, w, C = A[0, 0], A[1:, 0], A[1:, 1:]
        E1 = C - (w * z.H + z * w.H) / a + alpha * z * z.H / a**2
        E0 = C + (w * z.H + z * w.H) / b + alpha * z * z.H / b**2
        r1, r0 = w - alpha * z / a, w + alpha * z / b
        Q = alpha * C - w * w.H
        assert sp.simplify(alpha * E1 - r1 * r1.H - Q) == sp.zeros(K.rows - 1)
        assert sp.simplify(-alpha * E0 + r0 * r0.H + Q) == sp.zeros(K.rows - 1)
        Ddot = (w * z.H + z * w.H) / q + alpha * (a - b) * z * z.H / q**2
        M = C + alpha * z * z.H / q
        assert sp.simplify(E1 - (M - b * Ddot)) == sp.zeros(K.rows - 1)
        assert sp.simplify(E0 - (M + a * Ddot)) == sp.zeros(K.rows - 1)
        rhs = {0: -alpha**2 / q}
        rhs = add(rhs, hess_form(data1, E1), a)
        rhs = add(rhs, hess_form(data0, E0), b)
        rhs = add(rhs, grad_form(data1, Q), 2)
        rhs = add(rhs, grad_form(data0, Q), -2)
        assert add(hess_form(all_data, A), rhs, -1) == {}, (K, A)
    return {
        "hermitian_basis_dimension": len(bs),
        "exact_quadratic_identity_directions": len(directions),
        "conditional_acceleration_cancellation": True,
        "weighted_velocity_square_identity": True,
        "all_logarithm_coefficients_match": True,
    }


def frac(x):
    x = clean(x)
    return Fraction(int(sp.numer(x)), int(sp.denom(x)))


def scale_interval(interval, c):
    lo, hi = interval
    return (c * lo, c * hi) if c >= 0 else (c * hi, c * lo)


def log_unit_interval(x, terms=100):
    assert 1 <= x <= 2
    z = (x - 1) / (x + 1)
    s = sum((2 * z ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), Fraction(0))
    remainder = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return s, s + remainder


def log_interval(x):
    x = Fraction(x)
    power = 0
    while x >= 2:
        x /= 2
        power += 1
    while x < 1:
        x *= 2
        power -= 1
    lo, hi = log_unit_interval(x)
    a, b = scale_interval(log_unit_interval(Fraction(2)), power)
    return lo + a, hi + b


def evaluate_interval(form, digits=40):
    lo = hi = Fraction(0)
    for prime, coefficient in form.items():
        c = frac(coefficient)
        if prime == 0:
            lo += c
            hi += c
        else:
            a, b = scale_interval(log_interval(prime), c)
            lo += a
            hi += b
    denominator = 10**digits
    low_integer = (lo * denominator).__floor__()
    high_integer = (hi * denominator).__ceil__()
    return Fraction(low_integer, denominator), Fraction(high_integer, denominator)


def interval_json(interval):
    lo, hi = interval
    return {"lower": str(lo), "upper": str(hi), "decimal_display": float((lo + hi) / 2)}


def matrix_json(K):
    return [[str(x) for x in row] for row in K.tolist()]


def main():
    K = sp.Matrix([[R(1, 2), R(1, 10), R(1, 10)],
                   [R(1, 10), R(1, 2), R(1, 5)],
                   [R(1, 10), R(1, 5), R(1, 2)]])
    bad = sp.Matrix([[R(1, 2), R(1, 10), 0],
                     [R(1, 10), R(11, 50), R(1, 10)],
                     [0, R(1, 10), R(4, 5)]])
    a, b, z, B, F1, F0 = condition(K)
    q, rho, delta, gamma = R(1, 4), R(1, 50), R(2, 25), R(81, 625)
    Pplus = sp.ones(2) / 2
    Pminus = sp.eye(2) - Pplus
    assert F1 == R(33, 50) * Pplus + R(3, 10) * Pminus
    assert F0 == R(37, 50) * Pplus + R(3, 10) * Pminus
    margin = 9 * gamma * q - 208 * rho**2
    assert margin == R(521, 2500) > 0
    eta_lower = 1 / q + 4 * delta**2 - R(208, 9) * delta**2 / gamma
    E_upper = delta + 5 * delta / gamma
    assert eta_lower == R(1314164, 455625) > R(14, 5)
    assert E_upper == R(6412, 2025) < 4
    assert gamma >= R(1, 25)
    assert eta_lower >= R(33, 50)
    assert 8 * delta / 15 >= R(1, 25)
    data1, data0 = atom_data(F1), atom_data(F0)
    gplus = add(grad_form(data1, Pplus), grad_form(data0, Pplus), -1)
    gminus = add(grad_form(data1, Pminus), grad_form(data0, Pminus), -1)
    gp_interval, gm_interval = evaluate_interval(gplus), evaluate_interval(gminus)
    assert gp_interval[0] > 0 and gm_interval[0] > 0
    assert min(p for _, p, _ in atom_data(K)) == R(91, 1000)
    radius = R(1, 10**7)
    assert (R(91, 1000) * (1 - 5 * radius)**3) > R(1, 20)
    assert R(1, 5) - radius > R(1, 10)
    assert R(1, 50) - 74000 * radius > R(1, 100)

    # The universal-sign obstruction is proved by one integer comparison.
    N = 3**34 * 7**6 * 103**19
    D = 13**14 * 29**6 * 71**19
    assert D - N == 5498050420673646735604190142408463302595378867725283418312 > 0
    _, _, _, _, bad1, bad0 = condition(bad)
    Q = sp.diag(0, 1)
    g22 = add(grad_form(atom_data(bad1), Q), grad_form(atom_data(bad0), Q), -1)
    assert add(g22, log_form(R(N, D), R(1, 25)), -1) == {}
    remainder = add({}, g22, -2)
    remainder_interval = evaluate_interval(remainder)
    assert remainder_interval[0] > 0
    lead = lambda J: [str(J[:k, :k].det()) for k in range(1, 4)]
    assert lead(bad) == ["1/2", "1/10", "3/40"]
    assert lead(sp.eye(3) - bad) == ["1/2", "19/50", "71/1000"]

    L = K * (sp.eye(3) - K).inv()
    output = {
        "status": "verified with exact rational arithmetic and rigorous logarithm intervals",
        "positive_example": {
            "K": matrix_json(K), "F1": matrix_json(F1), "F0": matrix_json(F0),
            "q": str(q), "rho": str(rho), "delta": str(delta), "gamma": str(gamma),
            "condition_margin": str(margin), "eta_lower": str(eta_lower),
            "E_norm_upper": str(E_upper),
            "gradient_secant_eigenvalues": [interval_json(gp_interval), interval_json(gm_interval)],
            "point_hessian_gap": "1/50", "ball_radius": str(radius), "ball_hessian_gap": "1/100",
            "atom_probabilities_mask_order": [str(p) for _, p, _ in atom_data(K)],
            "odds_normalized_edge_squares": [str(sp.factor(L[i,j]**2/(L[i,i]*L[j,j]))) for i,j in [(0,1),(0,2),(1,2)]],
            "identity_checks": verify_full_identity(K),
        },
        "universal_remainder_sign_obstruction": {
            "K": matrix_json(bad), "F1": matrix_json(bad1), "F0": matrix_json(bad0),
            "direction": matrix_json(sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])),
            "K_leading_minors": lead(bad), "I_minus_K_leading_minors": lead(sp.eye(3)-bad),
            "N": str(N), "D": str(D), "D_minus_N": str(D-N),
            "G22": "log(N/D)/25", "positive_remainder": "2*log(D/N)/25",
            "remainder_interval": interval_json(remainder_interval),
            "identity_checks": verify_full_identity(bad),
        },
    }
    (OUT / "exact_certificate.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({
        "identity_checks": 90,
        "point_gap": output["positive_example"]["point_hessian_gap"],
        "ball_radius": str(radius),
        "ball_gap": output["positive_example"]["ball_hessian_gap"],
        "gradient_secant_eigenvalues": [float(sum(gp_interval)/2), float(sum(gm_interval)/2)],
        "positive_obstruction_remainder": float(sum(remainder_interval)/2),
        "all_checks_passed": True,
    }, indent=2))


if __name__ == "__main__":
    main()
