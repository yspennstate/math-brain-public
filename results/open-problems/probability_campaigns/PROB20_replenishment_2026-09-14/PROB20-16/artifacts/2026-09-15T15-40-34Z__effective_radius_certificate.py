import sympy as sp
import numpy as np

# Exact four-site rank-two example from PROB20-16 run 2026-09-15T15-40-34Z.
# Leaves: 0,1. Reservoir: 2,3.
D = sp.diag(sp.Rational(2, 5), sp.Rational(3, 5))
C = sp.Matrix([
    [sp.Rational(1, 2), sp.Rational(1, 10)],
    [sp.Rational(1, 10), sp.Rational(1, 2)],
])
B = sp.Matrix([
    [sp.Rational(1, 5), sp.Rational(1, 8)],
    [sp.Rational(1, 7), -sp.Rational(1, 6)],
])
assert B.det() == -sp.Rational(43, 840)


def kernel_corner(x, y):
    # At Boolean squared-strength corners, sqrt(x)=x and sqrt(y)=y.
    Z = sp.diag(sp.Integer(x), sp.Integer(y))
    return D.row_join(Z * B).col_join((B.T * Z).row_join(C))


def atom_probs(K):
    n = K.rows
    out = []
    for mask in range(1 << n):
        M = sp.Matrix(K)
        outside = [i for i in range(n) if not ((mask >> i) & 1)]
        for i in outside:
            M[i, i] -= 1
        out.append(sp.factor(((-1) ** len(outside)) * M.det()))
    return out


# Multi-affine coefficients p(x,y)=c0+cx*x+cy*y+cxy*x*y.
p00 = atom_probs(kernel_corner(0, 0))
p10 = atom_probs(kernel_corner(1, 0))
p01 = atom_probs(kernel_corner(0, 1))
p11 = atom_probs(kernel_corner(1, 1))

coeffs = []
for k in range(16):
    c0 = p00[k]
    cx = sp.factor(p10[k] - p00[k])
    cy = sp.factor(p01[k] - p00[k])
    cxy = sp.factor(p11[k] - p10[k] - p01[k] + p00[k])
    coeffs.append((c0, cx, cy, cxy))

assert all(sum(t) == p11[k] for k, t in enumerate(coeffs))
assert sum(c[0] for c in coeffs) == 1
assert sum(c[1] for c in coeffs) == 0
assert sum(c[2] for c in coeffs) == 0
assert sum(c[3] for c in coeffs) == 0

p_star = min(p00)
assert p_star == sp.Rational(24, 625)

# Exact decoupled squared-strength curvatures.
lambda_1 = sp.factor(sum(cx**2 / c0 for c0, cx, cy, cxy in coeffs))
lambda_2 = sp.factor(sum(cy**2 / c0 for c0, cx, cy, cxy in coeffs))
assert lambda_1 == sp.Rational(127625, 3833856)
assert lambda_2 == sp.Rational(64380625, 2912547456)
lambda_star = min(lambda_1, lambda_2)

# Physical feasibility certificate using ||B||op <= ||B||F.
sigma = sp.Rational(2, 5)
B_frob_sq = sp.factor(sum(v*v for v in B))
assert B_frob_sq == sp.Rational(73249, 705600)
r_phys_lower = sp.factor(sigma**2 / (4 * B_frob_sq))
assert r_phys_lower == sp.Rational(28224, 73249)

r0 = sp.Rational(1, 4)
assert r0 < r_phys_lower


def coefficient_bounds(r):
    dev = max(
        sp.Abs(cx)*r + sp.Abs(cy)*r + sp.Abs(cxy)*r*r
        for c0, cx, cy, cxy in coeffs
    )
    M1 = max(
        max(sp.Abs(cx) + r*sp.Abs(cxy),
            sp.Abs(cy) + r*sp.Abs(cxy))
        for c0, cx, cy, cxy in coeffs
    )
    M2 = max(sp.Abs(cxy) for c0, cx, cy, cxy in coeffs)
    return sp.factor(dev), sp.factor(M1), sp.factor(M2)


Delta0, M1, M2 = coefficient_bounds(r0)
mu = p_star / 2
assert Delta0 < mu
M3 = sp.Integer(0)
N = sp.Integer(16)

# Uniform third-entropy-derivative certificate.
T = sp.factor(N * (3*M2*M1/mu + M1**3/mu**2))
assert T == sp.Rational(6457539287652415, 12950250637492224)

m = sp.Integer(2)
r_cert = sp.factor(lambda_star / (2 * m**2 * T))
assert r_cert == sp.Rational(93034432512000, 16789602147896279)
assert r_cert < r0

margin = sp.factor(lambda_star / 2)

# Corroborative dense numerical grid on the certified square.
cf = np.array([[float(v) for v in tup] for tup in coeffs], dtype=float)


def probs_xy(x, y):
    return cf[:, 0] + cf[:, 1]*x + cf[:, 2]*y + cf[:, 3]*x*y


def entropy_hessian(x, y):
    p = probs_xy(x, y)
    assert np.min(p) > 0.0
    px = cf[:, 1] + cf[:, 3]*y
    py = cf[:, 2] + cf[:, 3]*x
    pxy = cf[:, 3]
    Hxx = -np.sum(px*px/p)
    Hyy = -np.sum(py*py/p)
    Hxy = -np.sum(px*py/p) - np.sum(pxy*np.log(p))
    return np.array([[Hxx, Hxy], [Hxy, Hyy]])


rc = float(r_cert)
largest = -np.inf
for x in np.linspace(0.0, rc, 101):
    for y in np.linspace(0.0, rc, 101):
        largest = max(largest, np.linalg.eigvalsh(entropy_hessian(x, y))[-1])

assert largest < 0.0
assert largest <= -float(margin) + 1e-12

print("rank(B) =", B.rank())
print("p_star =", p_star, float(p_star))
print("lambda_1 =", lambda_1, float(lambda_1))
print("lambda_2 =", lambda_2, float(lambda_2))
print("r_phys_lower =", r_phys_lower, float(r_phys_lower))
print("Delta0(r0) =", Delta0, float(Delta0))
print("mu =", mu, float(mu))
print("M1 =", M1, float(M1))
print("M2 =", M2, float(M2))
print("T =", T, float(T))
print("r_cert =", r_cert, float(r_cert))
print("certified Hessian upper margin =", -float(margin))
print("largest grid Hessian eigenvalue =", largest)
print("EFFECTIVE RADIUS CERTIFICATE CHECK PASSED")
