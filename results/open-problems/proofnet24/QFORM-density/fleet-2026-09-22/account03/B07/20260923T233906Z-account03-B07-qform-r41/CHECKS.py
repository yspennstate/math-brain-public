"""Finite regression checks for account03/B07 r41.
These checks are not proof evidence; REPORT.md contains the proofs.
"""
import itertools
import math
import random
import numpy as np
import sympy as sp

random.seed(4107)
np.random.seed(4107)


def e2_np(M):
    vals = np.linalg.eigvalsh(M @ M.T)
    return sum(vals[i] * vals[j]
               for i in range(len(vals))
               for j in range(i + 1, len(vals)))


def e3_np(M):
    vals = np.linalg.eigvalsh(M @ M.T)
    return sum(vals[i] * vals[j] * vals[k]
               for i in range(len(vals))
               for j in range(i + 1, len(vals))
               for k in range(j + 1, len(vals)))


def e2_sym(M):
    G = M * M.T
    return sum(G.extract([i, j], [i, j]).det()
               for i, j in itertools.combinations(range(G.rows), 2))


def e3_sym(M):
    G = M * M.T
    return sum(G.extract(list(idx), list(idx)).det()
               for idx in itertools.combinations(range(G.rows), 3))


max_rel = 0.0
min_schur_gap = float("inf")
for _ in range(500):
    ni = random.randint(2, 6)
    nj = random.randint(3, 7)
    K = np.random.randn(ni, nj)
    m = np.random.randn(nj)
    mm = float(m @ m)
    P = np.outer(m, m) / mm
    C = K @ (np.eye(nj) - P)
    Z = e2_np(C)

    M = np.vstack([m, K])
    lhs = mm * Z
    rhs = 0.0
    for r, s in itertools.combinations(range(1, ni + 1), 2):
        rhs += e3_np(M[[0, r, s], :])
    rel = abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs))
    max_rel = max(max_rel, rel)

    a = random.choice([-1.0, 1.0]) * (0.1 + 2.0 * random.random())
    u = np.random.randn(ni)
    R = K - np.outer(u, m) / a
    gap = e2_np(R) - Z
    min_schur_gap = min(min_schur_gap, gap)
    assert gap > -1e-9

assert max_rel < 1e-10

exact_trials = 0
for _ in range(50):
    ni, nj = 3, 4
    K = sp.Matrix([[random.randint(-3, 3) for _ in range(nj)] for _ in range(ni)])
    m = sp.Matrix([[random.randint(-3, 3) for _ in range(nj)]])
    mm = (m * m.T)[0]
    if mm == 0:
        continue
    P = m.T * m / mm
    C = K * (sp.eye(nj) - P)
    Z = sp.factor(e2_sym(C))
    lhs = sp.factor(mm * Z)
    M = m.col_join(K)
    rhs = 0
    for r, s in itertools.combinations(range(1, ni + 1), 2):
        rows = sp.Matrix([list(M.row(0)), list(M.row(r)), list(M.row(s))])
        rhs += e3_sym(rows)
    assert sp.simplify(lhs - rhs) == 0

    a = random.choice([-3, -2, -1, 1, 2, 3])
    u = sp.Matrix([[random.randint(-3, 3)] for _ in range(ni)])
    R = K - u * m / a
    assert sp.factor(e2_sym(R) - Z) >= 0
    exact_trials += 1

C3 = 3 * 2 ** (4 / 3) * math.e ** (1 / 3)
C_Z2 = 8 * math.e ** 0.25
S = 2 / 3125
d = 1 / 64
z3_bound = C3 * 3125 ** (1 / 6)
eta = d * d * S / 8
square_bound = C_Z2 * eta ** (-1 / 8)
core_bound = (8 / 3) * math.sqrt(18 * math.pi) / d
low_z_sum = S / (4 * d * d)

assert abs(low_z_sum - 0.65536) < 1e-12
assert eta == 1.953125e-8

print(f"floating_trials=500")
print(f"max_star_identity_relative_error={max_rel:.3e}")
print(f"minimum_schur_e2_gap={min_schur_gap:.3e}")
print(f"exact_rational_trials={exact_trials}")
print(f"C3={C3:.15f}")
print(f"z3_density_bound={z3_bound:.15f}")
print(f"square_eta={eta:.15e}")
print(f"square_density_bound={square_bound:.15f}")
print(f"partner_core_density_bound={core_bound:.15f}")
print(f"low_diagonal_sumZ_lower={low_z_sum:.15f}")
print("STATUS=PASS")
