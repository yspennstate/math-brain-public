#!/usr/bin/env python3
"""Exact rational certificates for C029's nonreversible DPP semigroups.

Run with Python + sympy. No numerical optimization or tolerance is used.
"""
from itertools import product
import json
from pathlib import Path

import sympy as sp

F = sp.Rational
I = sp.I
STATES = list(product((0, 1), repeat=4))


def atom(K, state):
    eye = sp.eye(4)
    M = sp.Matrix.hstack(*[K[:, j] if state[j] else eye[:, j] - K[:, j]
                          for j in range(4)])
    value = sp.simplify(M.det())
    assert value.is_Rational
    return value


def generic_certificate(A, D, B):
    def kernel(eta):
        return A.row_join(eta * B).col_join((eta * B.conjugate().T).row_join(D))

    # Every atom is even in eta and has degree at most four.
    probs = [[atom(kernel(t), state) for state in STATES] for t in (0, 1, 2)]
    mu = probs[0]
    g = [(probs[2][j] - 4 * probs[1][j] + 3 * mu[j]) / (12 * mu[j])
         for j in range(16)]
    h = [(probs[1][j] - mu[j]) / mu[j] - g[j] for j in range(16)]
    dot = lambda u, v: sum(mu[j] * u[j] * v[j] for j in range(16))
    H, G, C = dot(h, h), dot(g, g), dot(h, g)
    gram_det = H * G - C * C
    assert all(x > 0 for x in mu)
    assert sum(mu) == 1
    assert sum(mu[j] * h[j] for j in range(16)) == 0
    assert sum(mu[j] * g[j] for j in range(16)) == 0
    assert G > 0 and gram_det > 0 and C != 0
    ell = [(G * h[j] - C * g[j]) / gram_det for j in range(16)]
    assert dot(ell, h) == 1 and dot(ell, g) == 0
    assert sum(mu[j] * ell[j] for j in range(16)) == 0

    # Coefficients vanish under each fixed block marginal.
    for indices in ((0, 1), (2, 3)):
        for values in product((0, 1), repeat=2):
            js = [j for j, s in enumerate(STATES)
                  if tuple(s[k] for k in indices) == values]
            assert sum(mu[j] * h[j] for j in js) == 0
            assert sum(mu[j] * g[j] for j in js) == 0

    offdiag_products = [h[i] * ell[j] for i in range(16)
                        for j in range(16) if i != j]
    minimum = min(offdiag_products)
    assert minimum > -F(6, 5)
    # Coarse rational norm bounds provide a compact human-readable certificate.
    max_h, max_ell = max(abs(x) for x in h), max(abs(x) for x in ell)
    assert max_h < F(13, 200)
    assert max_ell < F(83, 5)
    assert F(13, 200) * F(83, 5) == F(1079, 1000) < F(6, 5)
    assert -F(2, 10**9) < C < -F(1, 10**9)
    print('dense example max |h|:', float(max_h))
    print('dense example max |ell|:', float(max_ell))
    print('dense example min off-diagonal h_i ell_j:', float(minimum))
    print('dense example <h,g>:', float(C))

    # Detailed balance would require h_i ell_j = h_j ell_i for every i,j.
    witness = next((i, j) for i in range(16) for j in range(i + 1, 16)
                   if h[i] * ell[j] != h[j] * ell[i])

    # Explicitly certify spectral relations and generator properties.
    # The rank-one formulas avoid unnecessary large 16-by-16 matrix products.
    one = [sp.S.One] * 16
    def apply_generator(f, reset, projection):
        mean, dual = dot(one, f), dot(ell, f)
        return [reset * (mean - f[i]) + projection * h[i] * dual
                for i in range(16)]

    assert apply_generator(one, 4, 2) == [0] * 16
    assert apply_generator(h, 4, 2) == [-2 * x for x in h]
    assert apply_generator(g, 4, 2) == [-4 * x for x in g]
    assert apply_generator(h, 12, 10) == [-2 * x for x in h]
    assert apply_generator(g, 12, 10) == [-12 * x for x in g]

    return {
        'states': STATES,
        'mu': list(map(str, mu)), 'h': list(map(str, h)), 'g': list(map(str, g)),
        'ell': list(map(str, ell)), 'H': str(H), 'G': str(G), 'C': str(C),
        'gram_determinant': str(gram_det),
        'min_offdiagonal_product': str(minimum),
        'max_abs_h': str(max_h), 'max_abs_ell': str(max_ell),
        'certified_abs_h_upper_bound': '13/200',
        'certified_abs_ell_upper_bound': '83/5',
        'certified_product_lower_bound': '-1079/1000',
        'certified_h_g_inner_product_interval': ['-2/1000000000', '-1/1000000000'],
        'nonreversibility_witness_state_indices': witness,
    }


def cycle_certificate():
    c, d, a, b = F(1, 30), F(1, 24), F(1, 8), F(1, 80)
    alpha, beta, gamma, delta = 4*c*c, 4*d*d, 4*a*a, 4*b*b
    zeta_abs = 32*c*d*a*b
    N = (gamma**2 + delta**2 + 2*alpha*beta*gamma*delta) / (
        (1-alpha**2)*(1-beta**2))
    M = ((1+alpha)*(1+beta)/((1-alpha)*(1-beta))
         * (gamma+delta)*(gamma+delta+zeta_abs)
         / (gamma**2+delta**2+2*alpha*beta*gamma*delta))
    assert M == F(74469825, 71287172)
    assert M < F(21, 20) < F(6, 5)
    zeta = -F(3, 5)*zeta_abs
    A = sp.Matrix([[F(1, 2), c], [c, F(1, 2)]])
    D = sp.Matrix([[F(1, 2), d], [d, F(1, 2)]])
    B = sp.diag(a, b*(F(3, 5)+F(4, 5)*I))
    for eta in (F(0), F(1, 3), F(1), F(2)):
        K = A.row_join(eta*B).col_join((eta*B.conjugate().T).row_join(D))
        for state in STATES:
            y = [1-2*x for x in state]
            z, w, s = y[0]*y[1], y[2]*y[3], y[0]*y[2]
            Delta = (1-alpha*z)*(1-beta*w)
            h0 = -s*(gamma+delta*z*w)/Delta
            v = z*w/Delta
            expected = Delta/F(16)*(1+eta**2*(h0+zeta*v)
                                     +eta**4*gamma*delta*v)
            assert atom(K, state) == expected
    inner = zeta*gamma*delta/((1-alpha**2)*(1-beta**2))
    assert inner == -F(2187, 1343601459200)
    print('all-phase cycle positivity M =', M, '< 21/20')
    print('phase 3/5+4i/5 nonorthogonality <h,g> =', inner)
    return {'all_phase_M': str(M), 'N': str(N), 'h_g_inner_product': str(inner)}


def main():
    cycle = cycle_certificate()
    A = sp.Matrix([[F(99, 200), F(1, 30)+I*F(1, 1000)],
                   [F(1, 30)-I*F(1, 1000), F(101, 200)]])
    D = sp.Matrix([[F(199, 400), F(1, 24)-I*F(1, 1200)],
                   [F(1, 24)+I*F(1, 1200), F(201, 400)]])
    B = sp.Matrix([[F(1, 8), (1+2*I)/1000],
                   [(-2+I)/1200, (3+4*I)/400]])
    K = A.row_join(B).col_join(B.conjugate().T.row_join(D))
    centered = K - F(1, 2)*sp.eye(4)
    row_bounds = [sum(abs(sp.re(centered[i,j])) + abs(sp.im(centered[i,j]))
                      for j in range(4)) for i in range(4)]
    assert max(row_bounds) == F(69, 400) < F(1, 2)
    dense = generic_certificate(A, D, B)
    dense['row_sum_eigenvalue_bound'] = str(max(row_bounds))
    result = {'cycle': cycle, 'dense': dense}
    path = Path(__file__).with_name('exact_certificate.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print('All exact assertions passed; certificate saved to', path.name)


if __name__ == '__main__':
    main()
