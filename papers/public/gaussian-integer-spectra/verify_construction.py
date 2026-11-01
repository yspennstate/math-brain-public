#!/usr/bin/env python3
"""Exact, dependency-free checks for the block-shear sign-matrix construction.

Enumerates the constructed families for n=1,2,3,4, checks distinctness,
computes characteristic polynomials by the Leibniz determinant formula,
and compares them with the prescribed Gaussian-integer eigenvalues.
Gaussian integers are represented by pairs of Python integers. No floating
point arithmetic or numerical eigenvalue routine is used.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path

SIGNS = (-1, 1)
UNITS = ((1, 0), (-1, 0), (0, 1), (0, -1))
ZERO = (0, 0)
ONE = (1, 0)


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gneg(x):
    return (-x[0], -x[1])


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def terminal_ok(quad, tau):
    a, b, c, d = quad
    return gadd(gadd((c, 0), gmul(tau, (d - a, 0))),
                gneg(gmul((b, 0), gmul(tau, tau)))) == ZERO


QUADS = tuple(itertools.product(SIGNS, repeat=4))
TERMINAL_SETS = {tau: frozenset(q for q in QUADS if terminal_ok(q, tau))
                 for tau in UNITS}
TERMINAL = tuple(sorted(set().union(*TERMINAL_SETS.values())))


def real_diagonal(epsilon):
    return tuple(q for q in QUADS if q[2] + epsilon * (q[3] - q[0]) - q[1] == 0)


def core_options(m, epsilon, imaginary_terminal):
    choices = []
    for i in range(m):
        for j in range(m):
            if i > j:
                choices.append(tuple((-b * epsilon[j], b, -d * epsilon[j], d)
                                     for b, d in itertools.product(SIGNS, repeat=2)))
            elif i < j:
                choices.append(tuple((a, b, epsilon[i] * a, epsilon[i] * b)
                                     for a, b in itertools.product(SIGNS, repeat=2)))
            elif imaginary_terminal and i == m - 1:
                choices.append(TERMINAL)
            else:
                choices.append(real_diagonal(epsilon[i]))
    return choices


def fill_core(n, m, core):
    matrix = [[None] * n for _ in range(n)]
    for (i, j), (a, b, c, d) in zip(itertools.product(range(m), repeat=2), core):
        matrix[i][j] = a
        matrix[i][m + j] = b
        matrix[m + i][j] = c
        matrix[m + i][m + j] = d
    return matrix


def diagonal_roots(matrix, m, parameters, odd):
    roots = []
    for j, r in enumerate(parameters):
        a, b, d = matrix[j][j], matrix[j][m + j], matrix[m + j][m + j]
        br = gmul((b, 0), r)
        roots.extend((gadd((a, 0), br), gadd((d, 0), gneg(br))))
    if odd:
        roots.append((matrix[-1][-1], 0))
    return tuple(roots)


def family(n):
    if n == 1:
        for a in SIGNS:
            yield ((a,),), ((a, 0),)
        return
    m = n // 2
    odd = n % 2 == 1
    for epsilon in itertools.product(SIGNS, repeat=m if odd else m - 1):
        choices = core_options(m, epsilon, imaginary_terminal=not odd)
        for core in itertools.product(*choices):
            if not odd:
                matrix = fill_core(n, m, core)
                terminal = core[-1]
                tau = next(t for t in UNITS if terminal in TERMINAL_SETS[t])
                parameters = tuple((e, 0) for e in epsilon) + (tau,)
                yield tuple(map(tuple, matrix)), diagonal_roots(matrix, m, parameters, False)
            else:
                for extra in itertools.product(SIGNS, repeat=2 * m + 1):
                    matrix = fill_core(n, m, core)
                    for i in range(m):
                        b = extra[i]
                        matrix[i][-1] = b
                        matrix[m + i][-1] = epsilon[i] * b
                    for j in range(m):
                        d = extra[m + j]
                        matrix[-1][j] = -d * epsilon[j]
                        matrix[-1][m + j] = d
                    matrix[-1][-1] = extra[-1]
                    parameters = tuple((e, 0) for e in epsilon)
                    yield tuple(map(tuple, matrix)), diagonal_roots(matrix, m, parameters, True)


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def characteristic_polynomial(matrix):
    """Coefficients in ascending order, by the exact Leibniz formula."""
    n = len(matrix)
    answer = [0] * (n + 1)
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = [(-1) ** inversions]
        for i, j in enumerate(perm):
            factor = [-matrix[i][j], 1] if i == j else [-matrix[i][j]]
            term = pmul(term, factor)
        for k, coefficient in enumerate(term):
            answer[k] += coefficient
    return tuple(answer)


def polynomial_from_roots(roots):
    answer = [ONE]
    for root in roots:
        nxt = [ZERO] * (len(answer) + 1)
        for j, coefficient in enumerate(answer):
            nxt[j] = gadd(nxt[j], gneg(gmul(root, coefficient)))
            nxt[j + 1] = gadd(nxt[j + 1], coefficient)
        answer = nxt
    return tuple(answer)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional JSON results path')
    args = parser.parse_args()

    plus, minus = TERMINAL_SETS[(1, 0)], TERMINAL_SETS[(-1, 0)]
    ip, im = TERMINAL_SETS[(0, 1)], TERMINAL_SETS[(0, -1)]
    assert len(real_diagonal(1)) == len(real_diagonal(-1)) == 6
    assert (len(plus), len(minus), len(plus & minus), len(plus | minus)) == (6, 6, 4, 8)
    assert ip == im and len(ip) == 4 and not (ip & (plus | minus))
    assert len(TERMINAL) == 12

    dimensions = []
    for n in range(1, 5):
        seen = set()
        integer_count = 0
        for matrix, roots in family(n):
            assert all(x in SIGNS for row in matrix for x in row)
            assert matrix not in seen, ('Duplicate construction', n, matrix)
            seen.add(matrix)
            assert len(roots) == n
            direct = characteristic_polynomial(matrix)
            factored = polynomial_from_roots(roots)
            assert tuple((x, 0) for x in direct) == factored, (n, matrix, direct, factored)
            integer_count += all(root[1] == 0 for root in roots)
        predicted = (2 ** ((n * n + 1) // 2)) * (3 ** (n // 2))
        predicted_integer = predicted if n % 2 else (2 * predicted) // 3
        assert len(seen) == predicted
        assert integer_count == predicted_integer
        dimensions.append({
            'n': n,
            'constructed_distinct_matrices': len(seen),
            'predicted_count': predicted,
            'ordinary_integer_spectrum_matrices': integer_count,
            'predicted_ordinary_integer_count': predicted_integer,
            'exact_characteristic_polynomials_checked': len(seen),
            'all_passed': True,
        })
    report = {
        'method': 'Exhaustive enumeration of the constructed families for n=1..4; exact integer and Gaussian-integer-pair arithmetic; Leibniz characteristic polynomials.',
        'scope': 'Finite verification only. The all-dimension theorem is proved in the accompanying manuscript.',
        'local_counts': {'real_plus': 6, 'real_minus': 6, 'real_intersection': 4, 'real_union': 8,
                         'imaginary_plus': 4, 'imaginary_minus': 4, 'terminal_union': 12},
        'dimensions': dimensions,
        'total_characteristic_polynomials_checked': sum(d['exact_characteristic_polynomials_checked'] for d in dimensions),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'all_passed': True,
    }
    rendered = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end='')


if __name__ == '__main__':
    main()
