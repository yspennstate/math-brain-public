"""
PROB20-16 corroborative checker:
quantitative strong concavity in squared amplitudes for a rank-one bridge.

Analytic theorem is in the accompanying report. This script verifies:
1) exact atom affinity p(x)=p0+D x;
2) the Fisher lower bound -Hess_x H >= lambda I;
3) the Pinsker/secant gradient bound -dH/dx_r >= 8 x_r gamma_r^2;
4) the resulting affine-complex-path curvature lower bound.

No numerical output is used as a proof premise.
"""
import numpy as np


def atom_probs(K):
    K = np.asarray(K, dtype=complex)
    n = K.shape[0]
    p = np.empty(1 << n, float)
    for mask in range(1 << n):
        M = K.copy()
        outside = [i for i in range(n) if not ((mask >> i) & 1)]
        for i in outside:
            M[i, i] -= 1
        p[mask] = (((-1) ** len(outside)) * np.linalg.det(M)).real
    p[np.abs(p) < 1e-14] = 0.0
    return p


rng = np.random.default_rng(2026091514)

# Active blocks V1={0,1}, V2={2}, V3={3,4}; exterior O={5,6,7}.
blocks = [[0, 1], [2], [3, 4]]
m = len(blocks)
n = 8

A = np.zeros((5, 5), complex)
A[:2, :2] = np.array([[.46, .07 + .02j], [.07 - .02j, .53]])
A[2, 2] = .41
A[3:5, 3:5] = np.array([[.57, -.05 + .03j], [-.05 - .03j, .48]])
C = np.array([
    [.52, .04 + .015j, -.02j],
    [.04 - .015j, .44, .03 + .01j],
    [.02j, .03 - .01j, .55],
], complex)
w = np.array([.18 + .04j, -.13 + .02j, .16 - .05j,
              .11 + .07j, -.15 + .03j], complex)
v = np.array([.17 - .02j, -.12 + .05j, .14 + .03j], complex)
B = np.outer(w, np.conj(v))

Kstar = np.block([[A, B], [B.conj().T, C]])
base_margin = min(np.linalg.eigvalsh(Kstar).min(),
                  np.linalg.eigvalsh(np.eye(n) - Kstar).min())
assert base_margin > 0.3


def K_from_x(x):
    scales = np.ones(5)
    for r, bl in enumerate(blocks):
        scales[bl] = np.sqrt(x[r])
    Z = np.diag(scales)
    Bx = Z @ B
    return np.block([[A, Bx], [Bx.conj().T, C]])


# Exact affine atom model from 0 and coordinate vertices.
p0 = atom_probs(K_from_x(np.zeros(m)))
cols = []
for r in range(m):
    e = np.zeros(m)
    e[r] = 1.0
    cols.append(atom_probs(K_from_x(e)) - p0)
D = np.column_stack(cols)

max_affine_residual = 0.0
for _ in range(250):
    x = rng.uniform(0, 1, m)
    p = atom_probs(K_from_x(x))
    pred = p0 + D @ x
    max_affine_residual = max(max_affine_residual,
                              float(np.max(np.abs(p - pred))))
assert max_affine_residual < 5e-12

# One common exterior coordinate and one nonzero coordinate per active block.
j = int(np.argmax(np.abs(v)))
gamma = []
for bl in blocks:
    i = max(bl, key=lambda k: abs(w[k]))
    gamma.append(abs(w[i]) ** 2 * abs(v[j]) ** 2)
gamma = np.asarray(gamma, float)
lam = float(np.min(gamma ** 2) / m)
assert lam > 0

min_hessian_surplus = np.inf
min_gradient_surplus = np.inf
for _ in range(500):
    x = rng.uniform(.01, .99, m)
    p = p0 + D @ x
    assert p.min() > 0

    # - Hess_x H = D^T diag(1/p) D.
    neg_hess = D.T @ ((1.0 / p)[:, None] * D)
    eigmin = float(np.linalg.eigvalsh(neg_hess).min())
    min_hessian_surplus = min(min_hessian_surplus, eigmin - lam)

    # grad H = -D^T log p because D^T 1 = 0.
    grad = -(D.T @ np.log(p))
    surplus = (-grad) - 8.0 * x * gamma ** 2
    min_gradient_surplus = min(min_gradient_surplus,
                               float(surplus.min()))

assert min_hessian_surplus > -1e-11
assert min_gradient_surplus > -1e-11

# Complex affine path with independent mixed radial motions.
z0 = np.array([0.72 + 0.12j, 0.55 - 0.18j, 0.34 + 0.22j])
z1 = np.array([0.25 - 0.20j, 0.78 + 0.08j, -0.10 + 0.32j])
beta = z1 - z0

min_neg_second = np.inf
min_path_surplus = np.inf
min_analytic_lower = np.inf

for t in np.linspace(0, 1, 201):
    z = z0 + t * beta
    x = np.abs(z) ** 2
    p = p0 + D @ x
    neg_hess = D.T @ ((1.0 / p)[:, None] * D)
    grad = -(D.T @ np.log(p))

    xp = 2 * np.real(np.conj(z) * beta)
    xpp = 2 * np.abs(beta) ** 2

    # H_tt = x'^T Hess_x H x' + grad H dot x''.
    Htt = -(xp @ neg_hess @ xp) + grad @ xpp
    neg_second = float(-Htt)

    lower = float(lam * np.dot(xp, xp)
                  + np.sum(16.0 * np.abs(beta) ** 2 * x * gamma ** 2))

    min_neg_second = min(min_neg_second, neg_second)
    min_analytic_lower = min(min_analytic_lower, lower)
    min_path_surplus = min(min_path_surplus, neg_second - lower)

assert min_neg_second > 0
assert min_analytic_lower > 0
assert min_path_surplus > -1e-11

print("PASS")
print("base spectral margin =", base_margin)
print("max atom-affinity residual =", max_affine_residual)
print("gamma =", gamma.tolist())
print("lambda strong-concavity bound =", lam)
print("min Hessian surplus over lambda =", min_hessian_surplus)
print("min Pinsker-gradient surplus =", min_gradient_surplus)
print("min -H'' along complex affine path =", min_neg_second)
print("min analytic path lower bound =", min_analytic_lower)
print("min path surplus =", min_path_surplus)
