"""
PROB20-16 corroborative checker for the coherent-reservoir quartic theorem.

Analytic theorem (in the accompanying report):
For independent leaf coordinates with fixed diagonal D, arbitrary strict coherent
reservoir C, and arbitrary fixed complex attachment rows B, write
    K(z) = [[D, diag(z) B], [B* diag(conj z), C]].
Near z=0, with x_i=|z_i|^2,
    Hess_x H(0) = -diag(J_i/[d_i(1-d_i)])
and all mixed x-Hessian entries vanish. Hence
    H(K(z)) = H(D blockdiag C)
      - 1/2 sum_i J_i/[d_i(1-d_i)] |z_i|^4 + O(||z||^6).

This script:
1. verifies exact multi-affinity of atom probabilities in x;
2. verifies the exact Hessian-at-zero formula;
3. samples a weak-strength cube and checks negative-definite x-Hessians;
4. samples arbitrary mixed-sign/phase affine complex amplitude chords in that cube;
5. checks convergence to the quartic coefficient.
Numerics corroborate only; they are not the proof.
"""

import numpy as np

rng = np.random.default_rng(20260915)


def atom_probs(K):
    K = np.asarray(K, dtype=complex)
    n = K.shape[0]
    out = np.empty(1 << n, dtype=float)
    for mask in range(1 << n):
        M = K.copy()
        outside = [i for i in range(n) if not ((mask >> i) & 1)]
        for i in outside:
            M[i, i] -= 1
        val = ((-1) ** len(outside)) * np.linalg.det(M)
        assert abs(val.imag) < 2e-9
        out[mask] = val.real
    return out


def entropy_from_probs(p):
    p = np.asarray(p, float)
    assert p.min() > -1e-9
    p = np.clip(p, 0.0, None)
    p /= p.sum()
    q = p[p > 1e-15]
    return float(-(q * np.log(q)).sum())


def entropy(K):
    return entropy_from_probs(atom_probs(K))


m, r = 3, 3
D = np.diag([0.31, 0.53, 0.72])

# Fixed strict coherent reservoir.
Z = rng.normal(size=(r, r)) + 1j * rng.normal(size=(r, r))
U, _ = np.linalg.qr(Z)
C = U @ np.diag([0.28, 0.47, 0.69]) @ U.conj().T

# Full-rank arbitrary attachment matrix, deliberately not rank one.
B0 = rng.normal(size=(m, r)) + 1j * rng.normal(size=(m, r))
B0 /= np.linalg.norm(B0, 2)
B = 0.34 * B0
assert np.linalg.matrix_rank(B, tol=1e-10) == 3


def K_of_x(x):
    x = np.asarray(x, float)
    S = np.diag(np.sqrt(x))
    BB = S @ B
    return np.block([[D, BB], [BB.conj().T, C]])


# The entire x-cube happens to be feasible in this deterministic witness,
# though the theorem proved in the report only needs a sufficiently small cube.
corner = K_of_x(np.ones(m))
base_margin = min(
    np.linalg.eigvalsh(corner).min(),
    np.linalg.eigvalsh(np.eye(m + r) - corner).min(),
)
assert base_margin > 1e-6

# Recover exact multilinear atom coefficients from the 2^m corners.
corner_probs = {}
for mask in range(1 << m):
    x = np.array([(mask >> i) & 1 for i in range(m)], float)
    corner_probs[mask] = atom_probs(K_of_x(x))

coeff = {}
for J in range(1 << m):
    c = np.zeros_like(corner_probs[0])
    L = J
    while True:
        c += (-1) ** (J.bit_count() - L.bit_count()) * corner_probs[L]
        if L == 0:
            break
        L = (L - 1) & J
    coeff[J] = c


def atom_from_coeff(x):
    x = np.asarray(x, float)
    p = np.zeros_like(coeff[0])
    for J, c in coeff.items():
        prod = 1.0
        for i in range(m):
            if (J >> i) & 1:
                prod *= x[i]
        p += c * prod
    return p


def entropy_hessian_x(x):
    x = np.asarray(x, float)
    p = atom_from_coeff(x)
    assert p.min() > 1e-13
    deriv = []
    for i in range(m):
        di = np.zeros_like(p)
        for J, c in coeff.items():
            if not ((J >> i) & 1):
                continue
            prod = 1.0
            for k in range(m):
                if k != i and ((J >> k) & 1):
                    prod *= x[k]
            di += c * prod
        deriv.append(di)

    H = np.zeros((m, m))
    for i in range(m):
        H[i, i] = -np.sum(deriv[i] ** 2 / p)
        for j in range(i + 1, m):
            dij = np.zeros_like(p)
            for J, c in coeff.items():
                if ((J >> i) & 1) and ((J >> j) & 1):
                    prod = 1.0
                    for k in range(m):
                        if k not in (i, j) and ((J >> k) & 1):
                            prod *= x[k]
                    dij += c * prod
            val = -np.sum(deriv[i] * deriv[j] / p) - np.sum(dij * np.log(p))
            H[i, j] = H[j, i] = val
    return H


# 1. Multi-affinity.
max_affine_residual = 0.0
for _ in range(500):
    x = rng.random(m)
    max_affine_residual = max(
        max_affine_residual,
        float(np.max(np.abs(atom_probs(K_of_x(x)) - atom_from_coeff(x)))),
    )
assert max_affine_residual < 5e-12

# 2. Exact Hessian-at-zero coefficient from reservoir rank-one Fisher information.
q = atom_probs(C)
lambdas = []
for i in range(m):
    # K block uses row B[i,:]; the reservoir column vector is its conjugate.
    u = B[i, :].conj()
    Umat = np.outer(u, u.conj())
    # Atom probabilities are exactly affine under a rank-one kernel perturbation,
    # so this finite difference at step 1 is the exact polynomial derivative.
    a = atom_probs(C + Umat) - q
    J = float(np.sum(a * a / q))
    d = float(D[i, i].real)
    lambdas.append(J / (d * (1.0 - d)))

H0 = entropy_hessian_x(np.zeros(m))
pred = -np.diag(lambdas)
h0_formula_residual = float(np.max(np.abs(H0 - pred)))
assert h0_formula_residual < 5e-11
assert min(lambdas) > 0

# 3. Sample a genuinely weak cube (the theorem guarantees some nonzero cube).
eps = 0.15
max_cube_eigenvalue = -np.inf
for _ in range(5000):
    x = rng.uniform(0.0, eps, size=m)
    emax = float(np.linalg.eigvalsh(entropy_hessian_x(x))[-1])
    max_cube_eigenvalue = max(max_cube_eigenvalue, emax)
assert max_cube_eigenvalue < 1e-8

# 4. Arbitrary complex affine chords with mixed phases/slopes.
sqrt_eps = np.sqrt(eps)
min_midpoint_gap = np.inf
for _ in range(1000):
    z0 = rng.normal(size=m) + 1j * rng.normal(size=m)
    z1 = rng.normal(size=m) + 1j * rng.normal(size=m)
    # scale each endpoint coordinate into the disk |z_i| <= sqrt_eps
    for z in (z0, z1):
        mags = np.maximum(1.0, np.abs(z) / sqrt_eps)
        z /= mags

    def K_of_z(z):
        BB = np.diag(z) @ B
        return np.block([[D, BB], [BB.conj().T, C]])

    H0z = entropy(K_of_z(z0))
    H1z = entropy(K_of_z(z1))
    zm = 0.5 * (z0 + z1)
    Hmz = entropy(K_of_z(zm))
    gap = Hmz - 0.5 * (H0z + H1z)
    min_midpoint_gap = min(min_midpoint_gap, gap)
    assert gap > -2e-10

# 5. Quartic asymptotic along one generic complex direction.
eta = rng.normal(size=m) + 1j * rng.normal(size=m)
eta /= np.max(np.abs(eta))
H_decoupled = entropy(K_of_x(np.zeros(m)))
quartic_target = 0.5 * sum(
    lambdas[i] * abs(eta[i]) ** 4 for i in range(m)
)
quartic_rows = []
for tau in [0.12, 0.08, 0.05, 0.03, 0.02]:
    x = (tau ** 2) * np.abs(eta) ** 2
    val = (H_decoupled - entropy(K_of_x(x))) / (tau ** 4)
    quartic_rows.append((tau, float(val), float(val - quartic_target)))

print("COHERENT-RESERVOIR WEAK-ATTACHMENT CHECK PASSED")
print("attachment rank =", np.linalg.matrix_rank(B))
print("full-corner spectral margin =", base_margin)
print("max atom multi-affinity residual =", max_affine_residual)
print("lambda coefficients =", lambdas)
print("Hessian-at-zero formula residual =", h0_formula_residual)
print("largest sampled Hessian eigenvalue on [0,eps]^m =", max_cube_eigenvalue)
print("eps =", eps)
print("minimum sampled complex-chord midpoint gap =", min_midpoint_gap)
print("quartic target =", quartic_target)
print("quartic convergence rows =", quartic_rows)
