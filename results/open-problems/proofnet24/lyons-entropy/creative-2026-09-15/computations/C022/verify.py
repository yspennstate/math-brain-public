"""Exact example and independent numerical checks for C022's block theorem."""
from pathlib import Path
import json
import itertools
import numpy as np
import sympy as sp

OUT = Path(__file__).resolve().parent


def atoms_exact(K):
    n = K.rows
    return [sp.expand((-1) ** (n - x.bit_count()) *
                      (K - sp.diag(*[0 if x >> j & 1 else 1
                                     for j in range(n)])).det())
            for x in range(1 << n)]


def atoms(K):
    n = len(K)
    return np.array([((-1) ** (n - x.bit_count()) * np.linalg.det(
        K - np.diag([0 if x >> j & 1 else 1 for j in range(n)]))).real
        for x in range(1 << n)])


def block_maps(D, blocks):
    n = len(D)
    out = []
    for B in blocks:
        mu = atoms(D[np.ix_(B, B)])
        mask = sum(1 << j for j in B)
        local = np.array([sum(((x >> j) & 1) << k for k, j in enumerate(B))
                          for x in range(1 << n)])
        outside = np.array([x & ~mask for x in range(1 << n)])

        def replacement(p, mu=mu, local=local, outside=outside):
            marg = np.bincount(outside, weights=p, minlength=len(p))
            return mu[local] * marg[outside]

        out.append(replacement)
    return out


def hessian(K, A):
    n = len(K)
    value = 0.0
    for x in range(1 << n):
        N = K - np.diag([0 if x >> j & 1 else 1 for j in range(n)])
        p = (((-1) ** (n - x.bit_count())) * np.linalg.det(N)).real
        R = np.linalg.solve(N, A)
        t = np.trace(R)
        p1 = (p * t).real
        p2 = (p * (t * t - np.trace(R @ R))).real
        value -= p1 * p1 / p + p2 * np.log(p)
    return value


def jeffreys_curvature(p, maps):
    chi = 0.0
    cross = 0.0
    individual = []
    for i, Ri in enumerate(maps):
        q = Ri(p)
        chi += np.sum((p - q) ** 2 / p)
        r = np.log(p / q)
        for j, Rj in enumerate(maps):
            if i == j:
                continue
            u, v = Rj(p) - p, Rj(q) - q
            e = -np.sum(u * (r + 1 - q / p) +
                        v * (-r + 1 - p / q))
            cross += e
            individual.append(float(e))
    return float(chi), float(cross), individual


def exact_example():
    q = sp.Rational
    D = sp.diag(sp.Matrix([[q(2, 5), q(1, 10)], [q(1, 10), q(1, 2)]]),
                sp.Matrix([[q(3, 5), -q(1, 12)], [-q(1, 12), q(2, 5)]]))
    U = sp.Matrix([[q(1, 2), 0], [q(1, 2), 0],
                   [0, q(1, 3)], [0, -q(2, 3)]])
    M = sp.Matrix([[q(1, 5), q(1, 4)], [q(1, 4), -q(1, 6)]])
    A, K = U * M * U.T, D + U * M * U.T
    leading = lambda Q: [sp.factor(Q[:j, :j].det()) for j in range(1, 5)]
    certificates = {name: leading(Q) for name, Q in
                    [('D', D), ('I-D', sp.eye(4) - D),
                     ('K', K), ('I-K', sp.eye(4) - K)]}
    assert all(x > 0 for values in certificates.values() for x in values)
    assert M.det() < 0
    assert D * K != K * D
    p = atoms_exact(K)
    mu0 = atoms_exact(D[:2, :2])
    mu1 = atoms_exact(D[2:, 2:])

    def R0(p):
        return [mu0[x & 3] * sum(p[(x & 12) | y] for y in range(4))
                for x in range(16)]

    def R1(p):
        return [mu1[x >> 2] * sum(p[(x & 3) | (y << 2)] for y in range(4))
                for x in range(16)]

    eta = sp.Symbol('eta', real=True)
    actual = atoms_exact(D + eta * A)
    channel = [eta * a + (1 - eta) * b for a, b in zip(p, R0(p))]
    channel = [eta * a + (1 - eta) * b
               for a, b in zip(channel, R1(channel))]
    assert all(sp.expand(a - b) == 0 for a, b in zip(actual, channel))
    H = lambda p: float(-sum(float(x) * np.log(float(x)) for x in p))
    midpoint_gap = H(atoms_exact(D + A / 2)) - (H(atoms_exact(D)) + H(p)) / 2
    return dict(D=str(D), U=str(U), M=str(M), K=str(K),
                exact_positive_leading_minors={k: list(map(str, v))
                                              for k, v in certificates.items()},
                reduced_determinant=str(M.det()),
                exact_all_eta_atom_identity=True,
                noncommuting=True, midpoint_gap=midpoint_gap,
                eigenvalues_D=np.linalg.eigvalsh(np.array(D, dtype=float)).tolist(),
                eigenvalues_K=np.linalg.eigvalsh(np.array(K, dtype=float)).tolist())


def random_checks():
    rng = np.random.default_rng(220220260915)
    worst_atom, worst_curvature, min_cross = 0.0, 0.0, float('inf')
    min_total = float('inf')
    count = 0
    for sizes in [(2, 2), (2, 1, 2), (3, 2, 1)]:
        n, m = sum(sizes), len(sizes)
        blocks, start = [], 0
        for size in sizes:
            blocks.append(list(range(start, start + size)))
            start += size
        for _ in range(6):
            D = np.zeros((n, n), complex)
            U = np.zeros((n, m), complex)
            for j, B in enumerate(blocks):
                Z = rng.normal(size=(len(B), len(B))) + 1j * rng.normal(size=(len(B), len(B)))
                Q, _ = np.linalg.qr(Z)
                D[np.ix_(B, B)] = Q @ np.diag(rng.uniform(.3, .7, len(B))) @ Q.conj().T
                v = rng.normal(size=len(B)) + 1j * rng.normal(size=len(B))
                U[B, j] = v / np.linalg.norm(v)
            Z = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
            M = (Z + Z.conj().T) / 2
            M *= .15 / np.linalg.norm(M, 2)
            A = U @ M @ U.conj().T
            K = D + A
            maps = block_maps(D, blocks)
            p1 = atoms(K)
            for eta in [.2, .6, 1.0]:
                p = atoms(D + eta * A)
                modeled = p1.copy()
                for R in maps:
                    modeled = eta * modeled + (1 - eta) * R(modeled)
                worst_atom = max(worst_atom, float(np.max(np.abs(p - modeled))))
                chi, cross, terms = jeffreys_curvature(p, maps)
                lhs = -eta * eta * hessian(D + eta * A, A)
                worst_curvature = max(worst_curvature, abs(lhs - chi - cross))
                min_cross = min(min_cross, min(terms))
                min_total = min(min_total, lhs)
                count += 1
    assert worst_atom < 2e-14
    assert worst_curvature < 2e-12
    assert min_cross > -1e-12
    return dict(cases=count, maximum_atom_identity_error=worst_atom,
                maximum_hessian_identity_error=worst_curvature,
                minimum_cross_term=min_cross, minimum_total_curvature=min_total)


if __name__ == '__main__':
    results = dict(exact_example=exact_example(), numerical_checks=random_checks())
    (OUT / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))
