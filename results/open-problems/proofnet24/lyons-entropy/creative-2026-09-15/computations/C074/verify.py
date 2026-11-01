#!/usr/bin/env python3
"""C074 exact atom identities and supplementary full-Hermitian checks.

The all-parameter proof is in agents/C074.md. Numerical eigenvalues here are
corroboration, never the sign certificate. Python 3 + NumPy are required.
"""
from fractions import Fraction as F
from math import comb, pi
from pathlib import Path
import json
import numpy as np

Z = (F(0), F(0))
O = (F(1), F(0))


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def mul(x, y):
    return x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0]


def div(x, y):
    d = y[0]**2 + y[1]**2
    return (x[0]*y[0] + x[1]*y[1])/d, (x[1]*y[0] - x[0]*y[1])/d


def power(x, k):
    out = O
    for _ in range(k):
        out = mul(out, x)
    return out


def det_exact(matrix):
    a = [row[:] for row in matrix]
    value = O
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k] != Z), None)
        if pivot is None:
            return Z
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            value = neg(value)
        value = mul(value, a[k][k])
        for i in range(k+1, len(a)):
            factor = div(a[i][k], a[k][k])
            for j in range(k+1, len(a)):
                a[i][j] = add(a[i][j], neg(mul(factor, a[k][j])))
            a[i][k] = Z
    return value


def exact_checks():
    checks = []
    cases = [(n, F(2, 5), F(1, 4*n)) for n in range(2, 7)]
    cases += [(4, F(1, 2), F(1, 5))]
    for n, a, b in cases:
        k_matrix = [[(a, F(0)) if i == j else (F(0), b*(1 if j > i else -1))
                     for j in range(n)] for i in range(n)]
        atoms = {}
        for mask in range(1 << n):
            indices = [i for i in range(n) if mask >> i & 1]
            m = len(indices)
            minor = [[k_matrix[i][j] for j in indices] for i in indices]
            delta = det_exact(minor)
            expected_minor = (power((a, b), m)[0], F(0))
            assert delta == expected_minor
            # Exact mixed-column determinant. Absent columns use I-K.
            mixed = [[k_matrix[i][j] if mask >> j & 1 else
                      add((F(i == j), F(0)), neg(k_matrix[i][j]))
                      for j in range(n)] for i in range(n)]
            atom = det_exact(mixed)
            formula = mul(power((a, b), m), power((1-a, -b), n-m))[0]
            assert atom == (formula, F(0)) and formula > 0
            atoms[mask] = formula
        assert sum(atoms.values()) == 1
        by_count = [str(atoms[(1 << m)-1]) for m in range(n+1)]
        for m in range(n+1):
            assert sum(v for mask, v in atoms.items() if mask.bit_count() == m) == \
                   comb(n, m)*atoms[(1 << m)-1]
        checks.append(dict(n=n, a=str(a), b=str(b), single_atom_by_count=by_count,
                           all_principal_minors_and_atoms_exact=True))
    # Strong four-site endpoint: sqrt(2)<3/2 proves (1+sqrt(2))/5<1/2.
    assert F(2) < F(3, 2)**2
    return checks


def hermitian_basis(n):
    basis = []
    for i in range(n):
        a = np.zeros((n, n), dtype=complex)
        a[i, i] = 1
        basis.append(a)
    for i in range(n):
        for j in range(i+1, n):
            a = np.zeros((n, n), dtype=complex)
            a[i, j] = a[j, i] = 1/np.sqrt(2)
            basis.append(a)
            a = np.zeros((n, n), dtype=complex)
            a[i, j] = 1j/np.sqrt(2)
            a[j, i] = -1j/np.sqrt(2)
            basis.append(a)
    return np.array(basis)


def count_law(p, exclude=()):
    f = np.array([1.])
    for i, x in enumerate(p):
        if i not in exclude:
            f = np.convolve(f, [1-x, x])
    return f


def scalar_count_hessian(p):
    n = len(p)
    f = count_law(p)
    q = f/np.array([comb(n, k) for k in range(n+1)])
    df = np.array([np.convolve(count_law(p, (i,)), [-1., 1.]) for i in range(n)])
    G = -(df/f) @ df.T
    R = np.zeros((n, n))
    ell = np.log(q[1:-1]**2/(q[:-2]*q[2:]))
    for i in range(n):
        for j in range(i+1, n):
            r = count_law(p, (i, j))
            ddf = np.convolve(r, [1., -2., 1.])
            G[i, j] -= ddf @ np.log(q)
            G[j, i] = G[i, j]
            R[i, j] = R[j, i] = r @ ell
    return f, q, G, R


def inspect_hessian(K, label):
    n = len(K)
    basis = hermitian_basis(n)
    m = len(basis)
    fisher = np.zeros((m, m))
    frozen = np.zeros((m, m))
    f = np.zeros(n+1)
    df = np.zeros((n+1, m))
    ddf = np.zeros((n+1, m, m))
    atoms = []
    for mask in range(1 << n):
        occupied = np.array([bool(mask >> i & 1) for i in range(n)])
        k = int(occupied.sum())
        Q = K - np.diag(~occupied)
        atom = ((-1)**(n-k)*np.linalg.det(Q)).real
        assert atom > 0
        inv = np.linalg.inv(Q)
        r = np.einsum('ij,ajk->aik', inv, basis)
        t = np.trace(r, axis1=1, axis2=2).real
        first = atom*t
        second = atom*(np.outer(t, t)-np.einsum('aij,bji->ab', r, r).real)
        fisher += np.outer(first, first)/atom
        frozen -= second*np.log(atom)
        f[k] += atom
        df[k] += first
        ddf[k] += second
        atoms.append((k, atom))
    H = -fisher + frozen
    count_fisher = (df.T/f) @ df
    direct_F = -count_fisher - np.einsum('k,kab->ab',
        np.log(f/np.array([comb(n,k) for k in range(n+1)])), ddf)
    eig, U = np.linalg.eigh(K)
    fs, qs, G, R = scalar_count_hessian(eig)
    B = np.einsum('ij,ajk,kl->ail', U.conj().T, basis, U)
    V = np.diagonal(B, axis1=1, axis2=2).real
    spectral = V @ G @ V.T
    for i in range(n):
        for j in range(i+1, n):
            w = B[:, i, j]
            spectral -= 2*R[i, j]*np.outer(w.conj(), w).real
    defect = fisher-count_fisher
    error = max(np.max(np.abs(H-(spectral-defect))),
                np.max(np.abs(spectral-direct_F)))
    atom_error = max(abs(atom-qs[k]) for k, atom in atoms)
    assert error < 2e-9 and atom_error < 1e-12
    return dict(label=label, n=n, kernel_eigenvalues=eig.tolist(),
                max_full_entropy_hessian_eigenvalue=float(np.linalg.eigvalsh(H)[-1]),
                max_spectral_envelope_hessian_eigenvalue=float(np.linalg.eigvalsh(spectral)[-1]),
                max_scalar_count_hessian_eigenvalue=float(np.linalg.eigvalsh(G)[-1]),
                min_fisher_defect_eigenvalue=float(np.linalg.eigvalsh(defect)[0]),
                minimum_offdiagonal_penalty=float(min(R[i,j] for i in range(n) for j in range(i+1,n))),
                hessian_decomposition_max_abs_error=float(error),
                conditional_uniformity_max_abs_error=float(atom_error))


def numerical_checks():
    outputs = []
    for n, a, fraction in [(3, .37, .9), (4, .5, .965685424949238),
                           (5, .41, .94), (6, .5, .97)]:
        c = 1/np.tan(pi/(2*n))
        b = fraction*min(a, 1-a)/c
        S = np.sign(np.arange(n)[None,:]-np.arange(n)[:,None])
        K = a*np.eye(n)+1j*b*S
        d = np.exp(1j*pi*np.arange(n)/n)
        C = d.conj()[:,None]*K*d[None,:]
        expected = np.array([a-b/np.tan((2*k+1)*pi/(2*n)) for k in range(n)])
        assert np.max(np.abs(np.linalg.eigvalsh(K)-np.sort(expected))) < 1e-12
        for i in range(n):
            assert np.max(np.abs(C[i]-np.roll(C[0], i))) < 1e-12
        out = inspect_hessian(C, 'circulant family, fraction %.8f of spectral limit' % fraction)
        out['a'], out['b'] = a, b
        assert out['max_full_entropy_hessian_eigenvalue'] < 0
        assert out['max_spectral_envelope_hessian_eigenvalue'] < 0
        outputs.append(out)
    # A general 3-site circulant, with nonzero real triangle product and a!=1/2.
    a, z = .45, .10+.16j
    K = np.array([[a,z,z.conjugate()],[z.conjugate(),a,z],[z,z.conjugate(),a]])
    outputs.append(inspect_hessian(K, 'general three-site complex circulant'))
    return outputs


if __name__ == '__main__':
    result = {'exact_checks': exact_checks(),
              'numerical_checks_are_supplementary_only': numerical_checks()}
    destination = Path(__file__).with_name('results.json')
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
