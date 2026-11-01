"""Exact certificates for C050: marked replicas and a full entropy Hessian.

Run from any directory with Python 3 and SymPy. All assertions use rational
arithmetic; no numerical eigenvalue or logarithm is used in a certificate.
The exploratory NumPy script in this directory is not needed.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import sympy as sp

OUT = Path(__file__).resolve().parent


def frac(x):
    x = sp.cancel(x)
    assert x.is_Rational, x
    return F(int(x.p), int(x.q))


def atom_jets(K, basis):
    """Exact determinant values, gradients, and Hessians in real coordinates."""
    n = K.rows
    atoms = []
    for bits in product((0, 1), repeat=n):
        M = sp.Matrix.hstack(*[(K if bit else sp.eye(n) - K)[:, j]
                              for j, bit in enumerate(bits)])
        p = M.det()
        assert p > 0
        inv = M.inv()
        R = [inv * sp.Matrix.hstack(*[(E if bit else -E)[:, j]
                                      for j, bit in enumerate(bits)])
             for E in basis]
        v = [frac(p * X.trace()) for X in R]
        B = [[frac(p * (X.trace() * Y.trace() - (X * Y).trace()))
              for Y in R] for X in R]
        atoms.append({'bits': bits, 'p': frac(p), 'v': v, 'B': B})
    return atoms


def matrix_add_entry(M, i, j, value):
    M[i][j] += value


def verify_replica_formula():
    """Finite Rademacher integrals, with zero, one-double, and two-single marks."""
    K = sp.Matrix([[sp.Rational(2, 5), (1 + sp.I) / 10],
                   [(1 - sp.I) / 10, sp.Rational(3, 5)]])
    A = sp.Matrix([[sp.Rational(1, 3), (2 - sp.I) / 7],
                   [(2 + sp.I) / 7, -sp.Rational(1, 5)]])
    t = sp.Symbol('t', real=True)
    atoms = atom_jets(K, [A])
    d = [F(1, 3), F(2, 5)]
    mu0 = (1 - d[0]) * (1 - d[1])
    odds = [di / (1 - di) for di in d]
    for atom in atoms:
        atom['mu'] = mu0
        for i, bit in enumerate(atom['bits']):
            if bit:
                atom['mu'] *= odds[i]

    cache = {}

    def determinant_jet(z):
        z = tuple(z)
        if z not in cache:
            Z = sp.diag(*[sp.Rational(x.numerator, x.denominator) for x in z])
            f = (sp.eye(2) - K - t * A + (K + t * A) * Z).det().expand()
            cache[z] = tuple(frac(sp.diff(f, t, order).subs(t, 0))
                             for order in (0, 1, 2))
        return cache[z]

    def integral(m, weighted):
        if weighted:
            eta = [o ** (1 - m) for o in odds]
            prefactor = mu0 ** (1 - m)
        else:
            eta = [F(1), F(1)]
            prefactor = F(1)
        sums = [F(0), F(0), F(0)]
        for flat in product((-1, 1), repeat=2 * (m - 1)):
            zs = [tuple(F(flat[2 * r + i]) for i in range(2))
                  for r in range(m - 1)]
            last = [eta[i] * sp.prod(z[i] for z in zs) for i in range(2)]
            jets = [determinant_jet(z) for z in zs]
            jets.append(determinant_jet(tuple(F(z) for z in last)))
            sums[0] += sp.prod(jet[0] for jet in jets)
            sums[1] += jets[0][2] * sp.prod(jet[0] for jet in jets[1:])
            sums[2] += jets[0][1] * jets[1][1] * sp.prod(jet[0] for jet in jets[2:])
        return [frac(value * prefactor / 2 ** (2 * (m - 1))) for value in sums]

    results = []
    for m, weighted in [(2, False), (2, True), (3, True), (4, True)]:
        direct = [F(0), F(0), F(0)]
        for atom in atoms:
            p, g, h = atom['p'], atom['v'][0], atom['B'][0][0]
            weight = atom['mu'] ** (1 - m) if weighted else F(1)
            direct[0] += weight * p ** m
            direct[1] += weight * h * p ** (m - 1)
            direct[2] += weight * g * g * p ** (m - 2)
        value = integral(m, weighted)
        assert value == direct
        results.append({'order': m, 'relative': weighted,
                        'moment': str(value[0]), 'one_double_mark': str(value[1]),
                        'two_single_marks': str(value[2])})
    return results


def main():
    replica_checks = verify_replica_formula()
    n = 3
    K = sp.Matrix([[sp.Rational(13, 20) if i == j else -sp.Rational(3, 10)
                    for j in range(n)] for i in range(n)])
    assert K.eigenvals() == {sp.Rational(1, 20): 1, sp.Rational(19, 20): 2}
    basis, labels = [], []
    for i in range(n):
        E = sp.zeros(n); E[i, i] = 1
        basis.append(E); labels.append(f'd{i}')
    for i, j in [(1, 2), (0, 2), (0, 1)]:
        E = sp.zeros(n); E[i, j] = E[j, i] = 1
        basis.append(E); labels.append(f're{i}{j}')
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        E = sp.zeros(n); E[i, j] = sp.I; E[j, i] = -sp.I
        basis.append(E); labels.append(f'im{i}{j}')
    atoms = atom_jets(K, basis)
    for atom in atoms:
        atom['mu'] = F(1)
        for bit in atom['bits']:
            atom['mu'] *= F(13, 20) if bit else F(7, 20)
    dim = len(basis)
    assert sum(atom['p'] for atom in atoms) == 1
    for i in range(dim):
        assert sum(atom['v'][i] for atom in atoms) == 0
        for j in range(dim):
            assert sum(atom['B'][i][j] for atom in atoms) == 0
            for site in range(n):
                assert sum(atom['B'][i][j] for atom in atoms if atom['bits'][site]) == 0

    # Independently recover all jets in C046's displayed direction.
    a = [F(1, 2)] * 3 + [F(0)] * 3 + [F(1), F(-1), F(1)]
    p_by_size = [F(w, 8000) for w in (19, 241, 2299, 361)]
    g_by_size = [F(w, 800) for w in (-39, -241, 121, 399)]
    h_by_size = [F(w, 40) for w in (-207, 147, -87, 27)]
    for atom in atoms:
        atom['g'] = sum(atom['v'][i] * a[i] for i in range(dim))
        atom['h'] = sum(atom['B'][i][j] * a[i] * a[j]
                        for i in range(dim) for j in range(dim))
        size = sum(atom['bits'])
        assert (atom['p'], atom['g'], atom['h']) == (
            p_by_size[size], g_by_size[size], h_by_size[size])
    c = F(2)
    assert all(0 < atom['p'] / (c * atom['mu']) < 1 for atom in atoms)

    # Direction-level seven-replica certificate, including its geometric tail.
    N = 6
    partial, tail, gamma0 = F(0), F(0), F(0)
    for atom in atoms:
        p, mu, g, h = (atom[key] for key in ('p', 'mu', 'g', 'h'))
        x, u = p / (c * mu), 1 - p / (c * mu)
        S = sum((u ** k / F(k) for k in range(1, N + 1)), F(0))
        partial += g * g / p * (1 - u ** N) - h * S
        tail += max(h, F(0)) * u ** (N + 1) / ((N + 1) * x)
        gamma0 += g * g / (c * mu) - h * u
    lower = partial - tail
    assert gamma0 == -F(1447050, 753571)
    assert lower == F(278133778323876598539324261940892499174531,
                      1456636674552442178434959990165335591489920)
    assert lower > F(19, 100)

    # Full matrix certificate with replica orders no greater than 49.
    N = 48
    L = [[F(0) for _ in range(dim)] for _ in range(dim)]
    for atom in atoms:
        p, mu, v, B = (atom[key] for key in ('p', 'mu', 'v', 'B'))
        x, u = p / (c * mu), 1 - p / (c * mu)
        S = sum((u ** k / F(k) for k in range(1, N + 1)), F(0))
        e = u ** (N + 1) / ((N + 1) * x)
        for i in range(dim):
            for j in range(dim):
                L[i][j] += v[i] * v[j] / p * (1 - u ** N) - B[i][j] * S
            L[i][i] -= e * sum(abs(z) for z in B[i])

    Q = [[F(0) for _ in range(dim)] for _ in range(dim)]
    for i in range(3):
        for j in range(3):
            Q[i][j] = F(8012 * (i == j) + 2292, 1000)
            Q[i + 3][j + 3] = F(15809 * (i == j) + 9634, 1000)
            Q[i][j + 3] = Q[j + 3][i] = F(3248 * (i == j) - 1833, 1000)
    w = [1, -1, 1]
    for i in range(3):
        for j in range(3):
            Q[i + 6][j + 6] = F(7450 * (i == j) - 2365 * w[i] * w[j], 1000)
    max_entry_error = max(abs(L[i][j] - Q[i][j])
                          for i in range(dim) for j in range(dim))
    assert max_entry_error < F(1, 2000)
    # The two real representation blocks are positive by diagonal dominance.
    trivial = [[F(14888, 1000), -F(2251, 1000)],
               [-F(2251, 1000), F(44711, 1000)]]
    standard = [[F(8012, 1000), F(3248, 1000)],
                [F(3248, 1000), F(15809, 1000)]]
    for block in (trivial, standard):
        assert min(block[0][0] - abs(block[0][1]),
                   block[1][1] - abs(block[1][0])) > F(71, 200)
    assert F(7450 - 2365 * sum(z * z for z in w), 1000) == F(71, 200)
    coordinate_gap = F(71, 200) - F(dim, 2000)
    frobenius_gap = coordinate_gap / 2
    assert coordinate_gap == F(701, 2000)
    assert frobenius_gap == F(701, 4000) > F(7, 40)

    serial_atoms = []
    for atom in atoms:
        serial_atoms.append({'bits': atom['bits'], 'p': str(atom['p']),
                             'mu': str(atom['mu']),
                             'v': [str(z) for z in atom['v']],
                             'B': [[str(z) for z in row] for row in atom['B']]})
    (OUT / 'certificate_jets.json').write_text(json.dumps(
        {'coordinate_order': labels, 'atoms': serial_atoms}, indent=2) + '\n')
    (OUT / 'matrix_lower_48.json').write_text(json.dumps(
        {'coordinate_order': labels,
         'L48': [[str(z) for z in row] for row in L],
         'Q': [[str(z) for z in row] for row in Q]}, indent=2) + '\n')
    results = {'all_assertions_passed': True,
               'replicated_determinant_checks': replica_checks,
               'first_corrected_replica_term': str(gamma0),
               'seven_replica_partial': str(partial),
               'seven_replica_tail_bound': str(tail),
               'seven_replica_lower_bound': str(lower),
               'seven_replica_simple_lower_bound': '19/100',
               'full_matrix_replicas_through_order': 49,
               'entrywise_enclosure': '1/2000',
               'Q_least_eigenvalue_proved': '71/200',
               'full_matrix_coordinate_gap': str(coordinate_gap),
               'full_matrix_frobenius_gap': str(frobenius_gap)}
    (OUT / 'exact_results.json').write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
