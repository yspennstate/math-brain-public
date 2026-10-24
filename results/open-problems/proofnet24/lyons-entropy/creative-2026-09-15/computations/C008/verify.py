#!/usr/bin/env python3
"""C008 exact algebra checks and supplementary numerical diagnostics.

The analytic proof is agents/C008.md. Finite numerical checks are not a proof.
Requires Python 3 and NumPy; exact checks use the standard-library Fraction.
"""

from fractions import Fraction as F
from itertools import permutations
from math import log, log1p, sqrt

import numpy as np


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    a = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        a[i] += x
    for i, x in enumerate(q):
        a[i] += x
    return trim(a)


def scale(p, x):
    return trim([F(x) * a for a in p])


def mul(p, q):
    a = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            a[i + j] += x * y
    return trim(a)


def eq(p, q):
    assert trim(p) == trim(q), (p, q)


def exact_polynomials():
    # Numerators in the count Fisher matrix.
    D = [3, -2, -1]
    alpha = [36, 0, -12, -8]
    beta = [0, 0, 0, -16]
    gamma = [0, 0, 48, -32]
    eq(alpha, add(mul(mul([3, -1], [3, -1]), [3, 1]),
                  scale(mul(mul([1, 1], [1, 1]), [1, -1]), 9)))
    eq(beta, add(scale(mul([0, 1], mul([3, -1], [3, 1])), -2),
                 scale(mul([0, 1], mul([1, 1], [1, -1])), 18)))
    eq(gamma, add(scale(mul([0, 0, 1], [3, 1]), 4),
                  scale(mul([0, 0, 1], [1, -1]), 36)))
    eq(add(mul(alpha, gamma), scale(mul(beta, beta), -1)),
       scale(mul([0, 0, 1], D), 576))
    eq(add(alpha, scale(gamma, -1)),
       scale(mul([1, -1], [3, 3, -2]), 12))
    assert 576 * F(3, 5) ** 2 - 192 == F(384, 25)
    assert 72 * F(3, 5) == F(216, 5)

    # Positive Bernstein representation proving the uniform 2/5 budget.
    bernstein = add(scale(mul(mul([1, -1], [1, -1]), [1, -1]), 8),
                    scale(mul([0, 1], mul([1, -1], [1, -1])), 12))
    bernstein = add(bernstein, [0, 0, 0, 1])
    eq(bernstein, [8, -12, 0, 5])
    # Substitution u = w-1 into (3-w)(w^2-1)/(4w).
    eq(mul([2, -1], [0, 2, 1]), [0, 4, 0, -1])
    print("PASS: exact polynomial identities and both allocation constants")


# Gaussian rational operations for an independent exact determinant expansion.
ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def ca(x, y):
    return x[0] + y[0], x[1] + y[1]


def cm(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def cpadd(p, q):
    out = [ZERO] * max(len(p), len(q))
    for i, x in enumerate(p):
        out[i] = ca(out[i], x)
    for i, x in enumerate(q):
        out[i] = ca(out[i], x)
    return out


def cpmul(p, q):
    out = [ZERO] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] = ca(out[i + j], cm(x, y))
    return out


PERMS = []
for p in permutations(range(3)):
    inv = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    PERMS.append((p, (-1) ** inv))


def exact_atom_poly(K, A, mask):
    Q = [[K[i][j] for j in range(3)] for i in range(3)]
    for i in range(3):
        if not (mask >> i & 1):
            Q[i][i] = ca(Q[i][i], (-F(1), F(0)))
    ans = [ZERO] * 4
    atom_sign = (-1) ** (3 - mask.bit_count())
    for perm, parity in PERMS:
        term = [(F(atom_sign * parity), F(0))]
        for i in range(3):
            j = perm[i]
            term = cpmul(term, [Q[i][j], A[i][j]])
        ans = cpadd(ans, term)
    assert all(im == 0 for re, im in ans)
    return [re for re, im in ans]


def exact_K(v):
    B = [[0, v[2], -v[1]], [-v[2], 0, v[0]], [v[1], -v[0], 0]]
    return [[(F(i == j, 2), F(B[i][j])) for j in range(3)] for i in range(3)]


def exact_atoms():
    vectors = [
        (F(0), F(0), F(0)),
        (F(2, 5), F(0), F(0)),
        (F(1, 3), -F(1, 4), F(0)),
        (F(1, 5), F(1, 7), -F(1, 9)),
        (F(4999, 10000), F(1, 10000), -F(1, 100000)),
    ]
    real_directions = [
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[F(1, 3), F(2, 7), -F(1, 5)],
         [F(2, 7), -F(3, 4), F(2, 9)],
         [-F(1, 5), F(2, 9), F(5, 6)]],
        [[0, 2, 3], [2, 0, -1], [3, -1, 0]],
    ]
    nchecks = 0
    for v in vectors:
        r = [x * x for x in v]
        T = sum(r)
        assert T < F(1, 4)
        q = [F(1, 8) - T / 2] + [F(1, 8) + T / 2 - x for x in r]
        assert sum(q) == F(1, 2)
        for i in range(3):
            j, k = [a for a in range(3) if a != i]
            assert q[j + 1] * q[k + 1] - q[0] * q[i + 1] == r[i] / 4 + r[j] * r[k]
            assert q[0] + q[i + 1] == F(1, 4) - r[i]
        for R in real_directions:
            A = [[(F(R[i][j]), F(0)) for j in range(3)] for i in range(3)]
            s = sum(F(R[i][i]) for i in range(3))
            z = sum(v[i] * F(R[i][j]) * v[j] for i in range(3) for j in range(3))
            d = s / 4 - z
            g = [F(R[i][i]) / 2 - s / 4 - z for i in range(3)]
            for mask in range(8):
                p = exact_atom_poly(exact_K(v), A, mask)
                card = mask.bit_count()
                if card == 0:
                    mass, deriv = q[0], -d
                elif card == 3:
                    mass, deriv = q[0], d
                elif card == 1:
                    i = next(i for i in range(3) if mask >> i & 1)
                    mass, deriv = q[i + 1], g[i]
                else:
                    i = next(i for i in range(3) if not (mask >> i & 1))
                    mass, deriv = q[i + 1], -g[i]
                assert p[0] == mass
                assert p[1] == deriv
                nchecks += 1
    print(f"PASS: {nchecks} exact Gaussian-rational determinant atom/derivative checks")


PAIRS = [(1, 2), (0, 2), (0, 1)]


def basis():
    out = []
    for i in range(3):
        A = np.zeros((3, 3), dtype=complex)
        A[i, i] = 1
        out.append(A)
    for imaginary in [False, True]:
        for i, j in PAIRS:
            A = np.zeros((3, 3), dtype=complex)
            A[i, j] = (1j if imaginary else 1) / sqrt(2)
            A[j, i] = A[i, j].conjugate()
            out.append(A)
    return out


BASIS = basis()


def atom_coeffs(K, A, mask):
    Q = K.copy()
    for i in range(3):
        if not (mask >> i & 1):
            Q[i, i] -= 1
    sign = (-1) ** (3 - mask.bit_count())
    p0 = sign * np.linalg.det(Q)
    p1 = 0j
    p2 = 0j
    for i in range(3):
        J = Q.copy()
        J[:, i] = A[:, i]
        p1 += sign * np.linalg.det(J)
    for i in range(3):
        for j in range(i + 1, 3):
            J = Q.copy()
            J[:, i] = A[:, i]
            J[:, j] = A[:, j]
            p2 += sign * np.linalg.det(J)
    assert max(abs(p0.imag), abs(p1.imag), abs(p2.imag)) < 1e-11
    return p0.real, p1.real, p2.real


def numeric_data(v):
    v = np.asarray(v, dtype=float)
    r = v * v
    T = sum(r)
    q = np.r_[.125 - T / 2, .125 + T / 2 - r]
    m = np.zeros(3)
    for i in range(3):
        j, k = [a for a in range(3) if a != i]
        m[i] = log1p((r[i] / 4 + r[j] * r[k]) / (q[0] * q[i + 1]))
    B = np.array([[0, v[2], -v[1]], [-v[2], 0, v[0]], [v[1], -v[0], 0]])
    return np.eye(3) / 2 + 1j * B, r, q, m


def independent_hessian(v):
    K, r, q, m = numeric_data(v)
    H = np.zeros((9, 9))
    J = np.zeros((8, 9))
    p2 = np.zeros((8, 9))
    p = np.zeros(8)
    for mask in range(8):
        for i, A in enumerate(BASIS):
            p[mask], J[mask, i], p2[mask, i] = atom_coeffs(K, A, mask)
    assert np.all(p > 0)
    fisher = (J.T / p) @ J
    for i, A in enumerate(BASIS):
        for j in range(i, 9):
            if i == j:
                p_second = 2 * p2[:, i]
            else:
                p_second = np.array([atom_coeffs(K, A + BASIS[j], mask)[2]
                                     for mask in range(8)]) - p2[:, i] - p2[:, j]
            H[i, j] = H[j, i] = -fisher[i, j] - np.dot(p_second, np.log(p))
    frozen = np.zeros((9, 9))
    for i, (j, k) in enumerate(PAIRS):
        frozen[j, k] = frozen[k, j] = m[i]
        frozen[3 + i, 3 + i] = frozen[6 + i, 6 + i] = -m[i]
    error = np.max(np.abs(H - (-fisher + frozen)))
    assert error < 1e-8 * (1 + np.linalg.norm(H))
    eigenvalues = np.linalg.eigvalsh(H)
    assert eigenvalues[-1] < 1e-9 * (1 + np.linalg.norm(H))
    return eigenvalues, error


def four_feature_value(r, q, m):
    delta = np.prod(m)
    if delta == 0:
        return None
    V = np.array([[1, -4*r[2], -4*r[1], -4*r[0]],
                  [-4*r[2], 1, -4*r[0], -4*r[1]],
                  [-4*r[1], -4*r[0], 1, -4*r[2]],
                  [-4*r[0], -4*r[1], -4*r[2], 1]])
    Rm = np.dot(m, r)
    u = np.r_[2*m, -8*Rm]
    D = np.zeros((4, 4))
    D[:3, :3] = np.diag(4*m*m)
    D[:3, 3] = D[3, :3] = -16*m*m*r
    D[3, 3] = 64*Rm*Rm
    return u @ np.linalg.solve(D + delta * V, u)


def numerical_checks():
    print("Supplementary floating-point diagnostics; these are not universal proofs.")
    catalog = [
        ("diagonal", [0, 0, 0]),
        ("single_edge", [.4, 0, 0]),
        ("unequal_path", [1/3, -1/4, 0]),
        ("unequal_triangle", [1/5, 1/7, -1/9]),
        ("equal_triangle", [2/7, 2/7, 2/7]),
        ("near_boundary_unequal", [.4999, .0001, -.00001]),
        ("near_boundary_path", [.39999, .3, 0]),
        ("near_boundary_balanced", np.sqrt(.249999 * np.array([.50, .31, .19]))),
    ]
    for label, v in catalog:
        eig, err = independent_hessian(v)
        _, r, q, m = numeric_data(v)
        feature = four_feature_value(r, q, m)
        ftext = "singular M" if feature is None else f"four-feature={feature:.12g}"
        print(f"  {label:25s} max(H eig)={eig[-1]: .9g} min(H eig)={eig[0]: .9g} "
              f"identity-error={err:.3g} {ftext}")

    rng = np.random.default_rng(20260915)
    max_budget = (-1., None)
    min_feature = (np.inf, None)
    for _ in range(20000):
        r = rng.dirichlet([.4, .4, .4]) * rng.uniform(.0001, .9999) / 4
        _, r, q, m = numeric_data(np.sqrt(r))
        qs = np.sort(q)
        budget = 2 * sum((qs[0] + qs[i]) * log(qs[3] / qs[i]) for i in [1, 2])
        assert budget < .4
        if budget > max_budget[0]:
            max_budget = (budget, qs)
        val = four_feature_value(r, q, m)
        assert val > 2 - 1e-8
        if val < min_feature[0]:
            min_feature = (val, r)
    print(f"  20,000 fixed-seed inputs: largest unequal budget = {max_budget[0]:.12g}")
    print(f"    ordered masses = {max_budget[1]}")
    print(f"  20,000 fixed-seed inputs: smallest four-feature value = {min_feature[0]:.12g}")
    print(f"    r = {min_feature[1]}")
    print("PASS: numerical diagnostics; analytic proof remains Sections 2–6 of the report")


if __name__ == "__main__":
    exact_polynomials()
    exact_atoms()
    numerical_checks()
