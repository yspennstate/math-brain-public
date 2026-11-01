"""Finite checks for C018; proofs are in agents/C018.md.

The calculations do not certify an unproved large-correlation region.
"""

from itertools import combinations
from pathlib import Path
import json
import math

import numpy as np
import sympy as sp


OUT = Path(__file__).resolve().parent


def subsets(n):
    return [[i for i in range(n) if mask & (1 << i)] for mask in range(1 << n)]


def minor(M, S):
    return float(np.linalg.det(M[np.ix_(S, S)]).real) if S else 1.0


def atoms(K):
    n = len(K)
    ans = []
    for S in subsets(n):
        absent = np.array([i not in S for i in range(n)], dtype=float)
        Q = K - np.diag(absent)
        p = (-1) ** int(absent.sum()) * float(np.linalg.det(Q).real)
        ans.append((S, p, np.linalg.inv(Q)))
    return ans


def wedge2(M):
    pairs = list(combinations(range(len(M)), 2))
    return np.array([[M[i, k] * M[j, l] - M[i, l] * M[j, k]
                      for k, l in pairs] for i, j in pairs])


def exterior(K, table):
    d = math.comb(len(K), 2)
    T = np.zeros((d, d), dtype=complex)
    for (S, p, Qinv), f in zip(atoms(K), table):
        T += p * f * wedge2(Qinv)
    return (T + T.conj().T) / 2


def hermitian_basis(n):
    basis = []
    for i in range(n):
        A = np.zeros((n, n), dtype=complex)
        A[i, i] = 1
        basis.append(A)
    for i, j in combinations(range(n), 2):
        for z in [1.0, 1.0j]:
            A = np.zeros((n, n), dtype=complex)
            A[i, j], A[j, i] = z / np.sqrt(2), z.conjugate() / np.sqrt(2)
            basis.append(A)
    return np.array(basis)


def entropy_hessian(K):
    basis = hermitian_basis(len(K))
    H = np.zeros((len(basis), len(basis)))
    for S, p, Qinv in atoms(K):
        assert p > 0
        R = np.einsum('ij,ajk->aik', Qinv, basis)
        tr = np.trace(R, axis1=1, axis2=2).real
        trprod = np.einsum('aij,bji->ab', R, R).real
        f = -np.log(p)
        H += p * ((f - 1) * np.outer(tr, tr) - f * trprod)
    return (H + H.T) / 2


def indefinite_odds_check():
    n = 6
    avec = sp.Matrix([1, sp.Rational(1, 5), sp.Rational(1, 4),
                      sp.Rational(1, 6), sp.Rational(1, 7), sp.Rational(1, 8)])
    D = sp.diag(sp.Rational(-1, 2), *([1] * (n - 1)))
    Lexact = D + avec * avec.T
    total_w = sum(avec[i] ** 2 for i in range(1, n))
    factorization = True
    for S in subsets(n):
        actual = Lexact.extract(S, S).det() if S else sp.Integer(1)
        W = sum(avec[i] ** 2 for i in S if i != 0)
        predicted = (sp.Rational(1, 2) * (1 - W)) if 0 in S else (1 + W)
        factorization &= actual == predicted
        assert actual > 0
    L = np.array(Lexact, dtype=float)
    rng = np.random.default_rng(1801820260915)
    Z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    U, _ = np.linalg.qr(Z)
    Kexternal = (U * np.array([.12, .25, .39, .61, .74, .88])) @ U.conj().T
    a = np.array(avec, dtype=float).ravel()
    f, absent_gate, occupied_gate = [], [], []
    for S in subsets(n):
        W = sum(a[i] ** 2 for i in S if i)
        f.append(-np.log(minor(L, S)))
        absent_gate.append(-np.log1p(W) if 0 not in S else 0.0)
        occupied_gate.append(-np.log1p(-W) if 0 in S else 0.0)
    T = exterior(Kexternal, f)
    T0 = exterior(Kexternal, absent_gate)
    T1 = exterior(Kexternal, occupied_gate)
    Klinked = L @ np.linalg.inv(np.eye(n) + L)
    hess_eigs = np.linalg.eigvalsh(entropy_hessian(Klinked))
    return {
        'all_64_principal_minor_identities_exact': bool(factorization),
        'sum_w_exact': str(total_w),
        'L_eigenvalues': np.linalg.eigvalsh(L).tolist(),
        'external_K_full_exterior_min_eigenvalue': float(np.linalg.eigvalsh(T)[0]),
        'absent_gate_exterior_min_eigenvalue': float(np.linalg.eigvalsh(T0)[0]),
        'occupied_gate_exterior_min_eigenvalue': float(np.linalg.eigvalsh(T1)[0]),
        'exterior_gate_decomposition_error': float(np.max(np.abs(T-T0-T1))),
        'linked_full_entropy_hessian_max_eigenvalue_numerical_only': float(hess_eigs[-1]),
        'external_K_real': Kexternal.real.tolist(),
        'external_K_imag': Kexternal.imag.tolist(),
    }


def stable_phi(q):
    # (1+q)log(1+q)-q, via its convergent series for small q.
    if abs(q) < .1:
        return sum((-1) ** m * q ** m / (m * (m - 1)) for m in range(2, 30))
    return (1 + q) * np.log1p(q) - q


def product_expansion_check():
    n = 6
    c = np.linspace(.35, .65, n)
    v = c * (1 - c)
    rng = np.random.default_rng(18018)
    phase = np.exp(1j * np.linspace(0, .6, n))
    B = -np.outer(phase, phase.conj())
    np.fill_diagonal(B, 0)
    B /= np.linalg.norm(B)
    Z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    E = (Z + Z.conj().T) / 2
    np.fill_diagonal(E, 0)
    E -= np.vdot(B, E).real * B
    E *= .01 / np.linalg.norm(E)
    B += E
    B /= np.linalg.norm(B)
    trials = []
    for scale in [.05, .025, .0125]:
        C = scale * B
        K = np.diag(c) + C
        p_direct = {tuple(S): p for S, p, _ in atoms(K)}
        divergence, err, degree_five = 0.0, 0.0, 0.0
        for X in subsets(n):
            x = np.array([i in X for i in range(n)], dtype=float)
            mu = np.prod(np.where(x, c, 1-c))
            w = (x-c)/v
            q, q2, q3 = 0.0, 0.0, 0.0
            for S in subsets(n):
                if len(S) < 2:
                    continue
                term = minor(C, S) * np.prod(w[S])
                q += term
                if len(S) == 2:
                    q2 += term
                if len(S) == 3:
                    q3 += term
            err = max(err, abs(mu*(1+q)-p_direct[tuple(X)]))
            divergence += mu * stable_phi(q)
            degree_five += mu * q2 * q3
        quartic = sum(abs(C[i,j])**4/(2*v[i]*v[j]) for i,j in combinations(range(n),2))
        eigs = np.linalg.eigvalsh(entropy_hessian(K))
        trials.append({
            'scale': scale,
            'moment_expansion_atom_error': err,
            'degree_five_cross_expectation': degree_five,
            'divergence': divergence,
            'quartic': quartic,
            'remainder_divided_by_scale_6': (divergence-quartic)/scale**6,
            'full_Hessian_max_eigenvalue_numerical_only': float(eigs[-1]),
            'max_eigenvalue_divided_by_scale_2': float(eigs[-1]/scale**2),
        })
    return trials


def exact_tetrad():
    s, t = sp.symbols('s t', real=True)
    u = sp.ones(4, 1)
    v = sp.Matrix([1, 1+s, 1+2*s, 1+3*s])
    M = -t*(u*u.T + v*v.T)/2
    obstruction = sp.factor(M[0,1]*M[2,3] - M[0,3]*M[2,1])
    assert obstruction == s*s*t*t
    return str(obstruction)


if __name__ == '__main__':
    result = {
        'indefinite_odds': indefinite_odds_check(),
        'weak_product_diagnostics': product_expansion_check(),
        'rank_one_midpoint_tetrad_exact': exact_tetrad(),
        'scope': 'Finite corroboration only. The full-Hessian theorem applies within its explicit small radius; no sampled larger radius is certified by these checks.',
    }
    (OUT/'results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
