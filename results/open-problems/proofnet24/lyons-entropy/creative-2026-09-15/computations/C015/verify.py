#!/usr/bin/env python3
"""C015: exact arithmetic identities and separately labeled diagnostics.

The mathematical transport theorem is proved in agents/C015.md.  This file
does not use finite numerical tests to establish a universal inequality.
Only the Python standard library is required.
"""
from fractions import Fraction as F
from itertools import permutations, combinations, product
import cmath
import json
import math
from pathlib import Path


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, c):
    return [[c * x for x in row] for row in a]


def star(a):
    return [[a[j][i].conjugate() if hasattr(a[j][i], 'conjugate')
             else a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def diag(v):
    return [[v[i] if i == j else 0 for j in range(len(v))]
            for i in range(len(v))]


def det(a):
    n = len(a)
    ans = 0
    for p in permutations(range(n)):
        invs = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = (-1) ** invs
        for i in range(n):
            term *= a[i][p[i]]
        ans += term
    return ans


def inverse(a):
    n = len(a)
    b = [list(a[i]) + eye(n)[i] for i in range(n)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(b[i][k]))
        b[k], b[pivot] = b[pivot], b[k]
        v = b[k][k]
        assert v != 0
        b[k] = [x / v for x in b[k]]
        for i in range(n):
            if i != k:
                v = b[i][k]
                b[i] = [x - v * y for x, y in zip(b[i], b[k])]
    return [r[n:] for r in b]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def kernel(l):
    return mul(l, inverse(add(eye(len(l)), l)))


def atoms(k, direction=None):
    n = len(k)
    if direction is None:
        direction = [[0] * n for _ in range(n)]
    answer = []
    for mask in range(1 << n):
        m = [[k[i][j] if mask >> j & 1 else int(i == j) - k[i][j]
              for j in range(n)] for i in range(n)]
        d = [[direction[i][j] * (1 if mask >> j & 1 else -1)
              for j in range(n)] for i in range(n)]
        coefficients = []
        for order in range(3):
            total = 0
            for cols in combinations(range(n), order):
                c = set(cols)
                mat = [[d[i][j] if j in c else m[i][j]
                        for j in range(n)] for i in range(n)]
                total += det(mat)
            coefficients.append(total * math.factorial(order))
        answer.append(tuple(coefficients))
    return answer


def shape_ratios(l):
    pairs = [1 - l[j][k] * l[k][j] / (l[j][j] * l[k][k])
             for j, k in ((1, 2), (0, 2), (0, 1))]
    determinant = det(l) / math.prod(l[i][i] for i in range(3))
    return pairs, math.prod(pairs) / determinant


def check_exact():
    l = [[F(100) if i == j else -F(499, 10) for j in range(3)]
         for i in range(3)]
    k = kernel(l)
    d = diag([F(101, 100), F(100, 101), F(1)])
    a = mul(d, d)
    e = add(a, scale(eye(3), -1))
    lp = mul(mul(d, l), d)
    kp = kernel(lp)
    t = mul(d, inverse(add(eye(3), mul(k, e))))
    z = det(add(eye(3), mul(e, k)))
    assert kp == mul(mul(d, k), mul(inverse(add(eye(3), mul(e, k))), d))
    assert shape_ratios(l) == shape_ratios(lp)
    w = [math.prod(a[i][i] for i in range(3) if mask >> i & 1)
         for mask in range(8)]
    r = math.prod(min(F(1), a[i][i]) for i in range(3)) / z
    dirs = []
    for i in range(3):
        b = [[F(0)] * 3 for _ in range(3)]
        b[i][i] = F(1)
        dirs.append(b)
    for i, j in combinations(range(3), 2):
        b = [[F(0)] * 3 for _ in range(3)]
        b[i][j] = b[j][i] = F(1)
        dirs.append(b)
    dirs.append([[F(1, 3), F(-2, 5), F(3, 7)],
                 [F(-2, 5), F(1, 11), F(-1, 4)],
                 [F(3, 7), F(-1, 4), F(-4, 9)]])
    for b in dirs:
        bp = mul(mul(t, b), star(t))
        n = mul(e, inverse(add(eye(3), mul(k, e))))
        acceleration = scale(mul(mul(mul(mul(t, b), n), b), star(t)), -2)
        old, new, acc = atoms(k, b), atoms(kp, bp), atoms(kp, acceleration)
        z1 = sum(wi * v[1] for wi, v in zip(w, old))
        z2 = sum(wi * v[2] for wi, v in zip(w, old))
        for wi, p, q, aa in zip(w, old, new, acc):
            assert q[0] == wi * p[0] / z
            assert q[1] == wi / z * (p[1] - p[0] * z1 / z)
            assert q[2] + aa[1] == wi / z * (
                p[2] - 2 * p[1] * z1 / z - p[0] * z2 / z
                + 2 * p[0] * (z1 / z) ** 2)
        fi = sum(p[1] ** 2 / p[0] for p in old)
        fip = sum(p[1] ** 2 / p[0] for p in new)
        assert fip >= r * fi
    P = F(31, 30) ** 3
    remaining = F(23, 100) - 2 * (P - 1)
    assert remaining == F(157, 6750)
    target_margin = remaining / P ** 3
    assert target_margin > F(1, 60)
    # The coefficient bound behind the general-shape radius.
    coeff = [F(247, 32), F(1125, 256), F(125, 256)]
    assert all(x < y for x, y in zip(coeff, [F(9), F(6), F(1)]))
    assert F(59, 24) < F(5, 2)
    assert F(5, 3) < F(4, 3) ** 2
    assert F(9, 8) < F(9, 8) ** 2
    return {'status': 'PASS', 'rational_directions': len(dirs),
            'identities': ['kernel fractional transform', 'shape ratios',
                           'atom tilt', 'first derivatives',
                           'second derivatives with acceleration',
                           'Fisher lower comparison'],
            'box_product_bound': str(P), 'pullback_margin': str(remaining),
            'target_margin': str(target_margin),
            'target_margin_greater_than_1_over_60': True,
            'general_radius_coefficients': list(map(str, coeff))}


def re(x):
    x = complex(x)
    assert abs(x.imag) < 1e-8 * max(1, abs(x.real))
    return x.real


def eig_real(a):
    a = [list(map(float, row)) for row in a]
    n = len(a)
    tol = 1e-13 * max(1.0, max(abs(x) for row in a for x in row))
    for _ in range(20000):
        i, j = max(combinations(range(n), 2), key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[i][j]) <= tol:
            return sorted(a[k][k] for k in range(n))
        angle = 0.5 * math.atan2(2 * a[i][j], a[j][j] - a[i][i])
        c, s = math.cos(angle), math.sin(angle)
        x, y, z = a[i][i], a[i][j], a[j][j]
        for k in range(n):
            if k not in (i, j):
                xk, yk = a[k][i], a[k][j]
                a[k][i] = a[i][k] = c * xk - s * yk
                a[k][j] = a[j][k] = s * xk + c * yk
        a[i][i] = c * c * x - 2 * c * s * y + s * s * z
        a[j][j] = s * s * x + 2 * c * s * y + c * c * z
        a[i][j] = a[j][i] = 0.0
    raise AssertionError('Jacobi did not converge')


def eig_herm(a):
    n = len(a)
    real = [[complex(x).real for x in row] for row in a]
    imag = [[complex(x).imag for x in row] for row in a]
    doubled = [real[i] + [-x for x in imag[i]] for i in range(n)]
    doubled += [imag[i] + real[i] for i in range(n)]
    e = eig_real(doubled)
    return [(e[2*i] + e[2*i+1]) / 2 for i in range(n)]


def cholesky(a):
    n = len(a)
    c = [[0j] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            v = a[i][j] - sum(c[i][k] * c[j][k].conjugate() for k in range(j))
            c[i][j] = math.sqrt(re(v)) if i == j else v / c[j][j]
    return c


def basis():
    out = []
    for i in range(3):
        a = [[0j] * 3 for _ in range(3)]
        a[i][i] = 1
        out.append(a)
    for i, j in combinations(range(3), 2):
        for v in [1 / math.sqrt(2), 1j / math.sqrt(2)]:
            a = [[0j] * 3 for _ in range(3)]
            a[i][j], a[j][i] = v, v.conjugate() if isinstance(v, complex) else v
            out.append(a)
    return out


def hessian(k):
    bs = basis()
    vals = [atoms(k, b) for b in bs]
    p = [re(v[0]) for v in vals[0]]
    assert min(p) > 0
    h = [[0.0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(i, 9):
            if i == j:
                second = [re(v[2]) for v in vals[i]]
            else:
                both = atoms(k, add(bs[i], bs[j]))
                second = [re((v[2] - x[2] - y[2]) / 2)
                          for v, x, y in zip(both, vals[i], vals[j])]
            h[i][j] = h[j][i] = -sum(
                re(vals[i][s][1]) * re(vals[j][s][1]) / p[s]
                + second[s] * math.log(p[s]) for s in range(8))
    return h, min(p)


def coefficients(l, k):
    pair, triple = shape_ratios(l)
    d = [-math.log(re(x)) for x in pair]
    tau = math.log(re(triple))
    return d, tau, add(diag(d), scale(k, tau))


def metric(m):
    inv = inverse(m)
    inv = scale(add(inv, star(inv)), 0.5)
    bs = basis()
    # The expression is real algebraically.  Near-singular source metrics
    # contain large cancelling terms, so use the explicitly real part here.
    return [[complex(trace(mul(mul(mul(inv, a), inv), b))).real
             for b in bs] for a in bs]


def diagnostic(name, l, factors, epsilon, target_epsilon):
    k = kernel(l)
    d, tau, m = coefficients(l, k)
    ds = diag([math.sqrt(x) for x in factors])
    lp = mul(mul(ds, l), ds)
    kp = kernel(lp)
    dp, taup, mp = coefficients(lp, kp)
    e = diag([x - 1 for x in factors])
    t = mul(ds, inverse(add(eye(3), mul(k, e))))
    ti = inverse(t)
    z = re(det(add(eye(3), mul(e, k))))
    wmax = math.prod(max(1, x) for x in factors)
    s = wmax / z
    c = inverse(cholesky(m))
    mismatch = add(scale(mul(mul(c, mul(mul(ti, mp), star(ti))), star(c)), s),
                   scale(eye(3), -1))
    eig_e = eig_herm(mismatch)
    hh, pmin = hessian(kp)
    mm = metric(mp)
    delta = re(det(mp))
    deficit = [[-hh[i][j] - target_epsilon * delta * mm[i][j]
                for j in range(9)] for i in range(9)]
    ev = eig_real(deficit)
    assert ev[0] > -1e-7, (name, ev[0])
    return {'name': name, 'odds_factors': factors, 'source_epsilon': epsilon,
            'claimed_target_epsilon': target_epsilon,
            'target_min_atom': pmin, 'mismatch_eigenvalues': eig_e,
            'mismatch_norm': max(abs(x) for x in eig_e),
            'minimum_numerical_margin_eigenvalue': ev[0],
            'shape_log_difference': max([abs(tau - taup)] + [abs(x-y) for x,y in zip(d,dp)])}


def main():
    exact = check_exact()
    diagnostics = []
    lstar = [[100.0 if i == j else -49.9 for j in range(3)] for i in range(3)]
    for j, factors in enumerate(product([30 / 31, 31 / 30], repeat=3)):
        diagnostics.append(diagnostic('C010_hard_box_corner_' + str(j), lstar,
                                      list(factors), 23 / 100, 1 / 60))
    for tv in [1e-4, 1e-6]:
        u = -math.log(tv)
        h = 1 / (625 * u * u)
        shape = [[1, math.sqrt(1-tv), -0.5j * math.sqrt(tv)],
                 [math.sqrt(1-tv), 1, 0.49 * math.sqrt(tv)],
                 [0.5j * math.sqrt(tv), 0.49 * math.sqrt(tv), 1]]
        ell = diag([math.sqrt(0.9), math.sqrt(1.1), math.sqrt(1.1)])
        ll = mul(mul(ell, shape), ell)
        diagnostics.append(diagnostic('C001_expanded_' + str(tv), ll,
                                      [1/(1+h), 1+h, 1+h], 1/(25*u), 1/(200*u)))
    output = {'exact_checks': exact,
              'floating_point_diagnostics_only': diagnostics,
              'diagnostic_count': len(diagnostics)}
    dest = Path(__file__).with_name('verify_output.json')
    dest.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({'exact_checks': exact['status'],
                      'diagnostic_count': len(diagnostics),
                      'minimum_diagnostic_margin': min(x['minimum_numerical_margin_eigenvalue']
                                                       for x in diagnostics)}, indent=2))


if __name__ == '__main__':
    main()
