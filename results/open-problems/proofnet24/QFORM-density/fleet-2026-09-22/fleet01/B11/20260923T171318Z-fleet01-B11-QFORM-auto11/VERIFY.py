import numpy as np
from math import exp


def e2_singular_sq(C):
    s = np.linalg.svd(C, compute_uv=False)
    lam = s * s
    return sum(lam[i] * lam[j]
               for i in range(len(lam)) for j in range(i + 1, len(lam)))


rng = np.random.default_rng(20260923)
max_identity_relerr = 0.0
max_marginal_err = 0.0

for _ in range(50):
    RI = rng.normal(size=(6, 3))
    RJ = rng.normal(size=(7, 3))
    B = rng.normal(size=(3, 3))
    M = B + B.T
    while abs(np.linalg.det(M)) < 0.2:
        B = rng.normal(size=(3, 3))
        M = B + B.T
    r = rng.normal(size=3)
    m = M @ r
    w = RJ @ m
    P = np.eye(len(w)) - np.outer(w, w) / (w @ w)
    C = RI @ M @ RJ.T @ P
    GI = RI.T @ RI
    GJ = RJ.T @ RJ

    Z2 = e2_singular_sq(C)
    lhs = (w @ w) * Z2
    rhs = ((np.linalg.det(M) ** 2) * np.linalg.det(GJ) *
           np.linalg.det(GI) * (r @ np.linalg.inv(GI) @ r))
    rel = abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs))
    max_identity_relerr = max(max_identity_relerr, rel)

    projector = C @ np.linalg.pinv(C)
    Ginv = np.linalg.inv(GI)
    denom = r @ Ginv @ r
    alpha_formula = np.array([
        ri @ Ginv @ ri - (ri @ Ginv @ r) ** 2 / denom
        for ri in RI
    ])
    max_marginal_err = max(
        max_marginal_err,
        float(np.max(np.abs(np.diag(projector) - alpha_formula)))
    )

# Explicit exact-null-pivot family in the fleet02/B11 two-plane chamber.
c = 0.5
r = np.sqrt(c) * np.array([1.0, 0.0, 0.0])
M = np.array([[0.0, 1.0, 1.0],
              [1.0, 0.0, 1.0],
              [1.0, 1.0, 0.0]])
GI = np.diag([(1.0 - c) / 2.0, 0.5, 0.5])
GJ = GI.copy()
RI = np.vstack([
    np.array([np.sqrt((1.0 - c) / 2.0), 0.0, 0.0]),
    np.array([0.0, 0.5, 0.0]),
    np.array([0.0, 0.5, 0.0]),
    np.array([0.0, 0.0, 0.5]),
    np.array([0.0, 0.0, 0.5]),
])
RJ = RI.copy()
m = M @ r
w = RJ @ m
P = np.eye(len(w)) - np.outer(w, w) / (w @ w)
C = RI @ M @ RJ.T @ P
Z2 = e2_singular_sq(C)
S2 = w @ w
Ginv = np.linalg.inv(GI)
denom = r @ Ginv @ r
alphas = [
    ri @ Ginv @ ri - (ri @ Ginv @ r) ** 2 / denom
    for ri in RI
]
Cstar = 3.0 * 2.0 ** (7.0 / 6.0) * exp(1.0 / 3.0)
bound = Cstar * (S2 * Z2) ** (-1.0 / 6.0)

assert max_identity_relerr < 1e-11
assert max_marginal_err < 1e-11
assert np.max(np.abs(np.linalg.eigvalsh(M) - np.array([-1.0, -1.0, 2.0]))) < 1e-12
assert abs(float(r @ M @ r)) < 1e-12
assert abs(S2 - 0.5) < 1e-12
assert abs(Z2 - 1.0 / 16.0) < 1e-12
assert abs(S2 * Z2 - 1.0 / 32.0) < 1e-12
assert max(alphas) <= 0.5 + 1e-12

print('max_identity_relerr', max_identity_relerr)
print('max_marginal_err', max_marginal_err)
print('family_eigenvalues', np.linalg.eigvalsh(M))
print('hub_physical_diagonal', float(r @ M @ r))
print('S2', S2)
print('Z2', Z2)
print('S2Z2', S2 * Z2)
print('row_marginals', alphas)
print('Cstar', Cstar)
print('density_bound', bound)
print('QFORM_B11_HUB_PROJECTED_CROSSING_CHECK_PASS')
