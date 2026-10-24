"""
PROB20-16 corroborative checker:
global nonexchangeable three-site weak-edge core with coherent satellites.

Analytic proof is in the accompanying report. This script checks one strict
complex example:
  * both endpoint squared-strength representatives satisfy the finite robust
    weak-edge domain, including every satellite atom and every subset vertex;
  * the exact Schur-complement physical constraints hold;
  * conditional entropy chain rule matches direct six-site entropy;
  * the actual affine kernel chord is strictly feasible and obeys Jensen;
  * random convex-combination/downward points retain the robust domain.

Floating point only; not a proof.
"""
import itertools
import numpy as np

TOL = 2e-10

def atom_probs(K):
    K = np.asarray(K, dtype=complex)
    n = K.shape[0]
    p = np.empty(1 << n, dtype=float)
    for mask in range(1 << n):
        M = K.copy()
        absent = [i for i in range(n) if not ((mask >> i) & 1)]
        for i in absent:
            M[i, i] -= 1
        val = ((-1) ** len(absent)) * np.linalg.det(M)
        assert abs(val.imag) < 2e-10
        p[mask] = val.real
    assert p.min() > -2e-10
    assert abs(p.sum() - 1) < 2e-10
    return p

def entropy(K):
    p = atom_probs(K)
    p = p[p > 1e-15]
    return float(-(p * np.log(p)).sum())

def weak_edge_margin(A):
    A = np.asarray(A, dtype=complex)
    d = np.real(np.diag(A))
    out = np.inf
    for i in range(3):
        for j in range(i + 1, 3):
            e = abs(A[i, j])
            for k in range(3):
                out = min(out, (2 / 7) * d[k] - e)
                out = min(out, (2 / 7) * (1 - d[k]) - e)
    return float(out)

def sat_data(C, v):
    C = np.asarray(C, dtype=complex)
    v = np.asarray(v, dtype=complex)
    n = len(v)
    out = []
    for mask in range(1 << n):
        Q = C.copy()
        absent = [i for i in range(n) if not ((mask >> i) & 1)]
        for i in absent:
            Q[i, i] -= 1
        q = (((-1) ** len(absent)) * np.linalg.det(Q)).real
        d = float(np.real(v.conj() @ np.linalg.inv(Q) @ v))
        out.append((mask, q, d))
    assert min(q for _, q, _ in out) > 0
    assert abs(sum(q for _, q, _ in out) - 1) < 2e-12
    return out

def full_kernel(A, z, Cs, bs, vs):
    sizes = [len(v) for v in vs]
    n = 3 + sum(sizes)
    K = np.zeros((n, n), dtype=complex)
    K[:3, :3] = A
    pos = 3
    for zj, Cj, bj, vj in zip(z, Cs, bs, vs):
        q = len(vj)
        K[pos:pos+q, pos:pos+q] = Cj
        X = zj * np.outer(bj, vj.conj())
        K[:3, pos:pos+q] = X
        K[pos:pos+q, :3] = X.conj().T
        pos += q
    return K

def physical_margin(A, s, Cs, bs, vs):
    P = A.copy()
    Q = np.eye(3, dtype=complex) - A
    for sj, Cj, bj, vj in zip(s, Cs, bs, vs):
        alpha = float(np.real(vj.conj() @ np.linalg.inv(Cj) @ vj))
        beta = float(np.real(vj.conj() @ np.linalg.inv(np.eye(len(vj)) - Cj) @ vj))
        P -= alpha * sj * np.outer(bj, bj.conj())
        Q -= beta * sj * np.outer(bj, bj.conj())
    return float(min(np.linalg.eigvalsh(P).min(), np.linalg.eigvalsh(Q).min()))

def robust_margin(A, s, datas, bs):
    ans = np.inf
    for atoms in itertools.product(*datas):
        ds = [a[2] for a in atoms]
        for Jmask in range(1 << len(bs)):
            M = A.copy()
            for j, bj in enumerate(bs):
                if (Jmask >> j) & 1:
                    M -= s[j] * ds[j] * np.outer(bj, bj.conj())
            ans = min(ans, weak_edge_margin(M))
    return float(ans)

def conditional_entropy(A, z, Cs, bs, vs, datas):
    s = np.abs(z) ** 2
    ans = sum(entropy(C) for C in Cs)
    for atoms in itertools.product(*datas):
        q = np.prod([a[1] for a in atoms])
        M = A.copy()
        for j, bj in enumerate(bs):
            M -= s[j] * atoms[j][2] * np.outer(bj, bj.conj())
        ans += q * entropy(M)
    return float(ans)

A0 = np.array([
    [0.43,  0.025+0.012j, -0.018+0.009j],
    [0.025-0.012j, 0.56,  0.021-0.008j],
    [-0.018-0.009j, 0.021+0.008j, 0.49],
], dtype=complex)

A1 = np.array([
    [0.57, -0.019+0.016j,  0.023+0.006j],
    [-0.019-0.016j, 0.46, -0.017+0.011j],
    [0.023-0.006j, -0.017-0.011j, 0.53],
], dtype=complex)

C1 = np.array([
    [0.48, 0.055+0.018j],
    [0.055-0.018j, 0.57],
], dtype=complex)
C2 = np.array([[0.54]], dtype=complex)

v1 = np.array([0.075+0.025j, -0.060+0.018j])
v2 = np.array([0.080-0.030j])
b1 = np.array([0.70, 0.20+0.10j, -0.30j])
b2 = np.array([-0.10+0.20j, 0.65, 0.25-0.10j])

Cs = [C1, C2]
vs = [v1, v2]
bs = [b1, b2]
datas = [sat_data(C1, v1), sat_data(C2, v2)]

z0 = np.array([0.70+0.10j, 0.55-0.15j])
z1 = np.array([-0.55+0.20j, 0.25+0.45j])
s0 = np.abs(z0) ** 2
s1 = np.abs(z1) ** 2

assert weak_edge_margin(A0) > 0
assert weak_edge_margin(A1) > 0
phys0 = physical_margin(A0, s0, Cs, bs, vs)
phys1 = physical_margin(A1, s1, Cs, bs, vs)
rob0 = robust_margin(A0, s0, datas, bs)
rob1 = robust_margin(A1, s1, datas, bs)
assert min(phys0, phys1, rob0, rob1) > 0

H0 = entropy(full_kernel(A0, z0, Cs, bs, vs))
H1 = entropy(full_kernel(A1, z1, Cs, bs, vs))

max_chain_resid = 0.0
min_spectral = np.inf
min_gap = np.inf
min_robust_actual = np.inf
for t in np.linspace(0, 1, 101):
    A = (1-t)*A0 + t*A1
    z = (1-t)*z0 + t*z1
    s = np.abs(z) ** 2
    K = full_kernel(A, z, Cs, bs, vs)
    min_spectral = min(
        min_spectral,
        np.linalg.eigvalsh(K).min(),
        np.linalg.eigvalsh(np.eye(K.shape[0]) - K).min(),
    )
    direct = entropy(K)
    cond = conditional_entropy(A, z, Cs, bs, vs, datas)
    max_chain_resid = max(max_chain_resid, abs(direct-cond))
    gap = direct - ((1-t)*H0 + t*H1)
    if 0 < t < 1:
        min_gap = min(min_gap, gap)
    min_robust_actual = min(min_robust_actual, robust_margin(A, s, datas, bs))

assert min_spectral > 0
assert max_chain_resid < 5e-10
assert min_gap > -5e-10
assert min_robust_actual > 0

rng = np.random.default_rng(20260915)
min_random_robust = np.inf
min_random_physical = np.inf
for _ in range(500):
    t = rng.random()
    A = (1-t)*A0 + t*A1
    sbar = (1-t)*s0 + t*s1
    theta = rng.random(2)
    s = theta*sbar
    min_random_robust = min(min_random_robust, robust_margin(A, s, datas, bs))
    min_random_physical = min(min_random_physical, physical_margin(A, s, Cs, bs, vs))

assert min_random_robust > 0
assert min_random_physical > 0

print("PROB20-16 NONEXCHANGEABLE CORE LIFTING CHECK PASSED")
print("endpoint physical margins =", phys0, phys1)
print("endpoint robust weak-edge margins =", rob0, rob1)
print("minimum full-chord spectral margin =", min_spectral)
print("maximum conditional entropy identity residual =", max_chain_resid)
print("minimum interior Jensen gap =", min_gap)
print("minimum actual-chord robust margin =", min_robust_actual)
print("minimum random downward robust margin =", min_random_robust)
print("minimum random downward physical margin =", min_random_physical)
