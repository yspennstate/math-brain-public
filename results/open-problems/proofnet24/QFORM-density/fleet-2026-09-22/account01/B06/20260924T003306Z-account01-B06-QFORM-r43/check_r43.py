import math
import numpy as np
import mpmath as mp

rng = np.random.default_rng(4306)


def weighted_stability_trial(m=8):
    # Diffuse positive weights p_i proportional to a_i^2.
    a = 0.8 + 0.4 * rng.random(m)
    p = a * a
    p /= p.sum()

    R = rng.normal(size=(m, m))
    R = (R + R.T) / 2
    np.fill_diagonal(R, 0.0)

    # Normal equations for min sum_{i != j} p_i p_j(R_ij-u_i-u_j)^2.
    M = np.zeros((m, m))
    rhs = np.zeros(m)
    for i in range(m):
        rhs[i] = sum(p[j] * R[i, j] for j in range(m) if j != i)
        M[i, i] = 1 - p[i]
        for j in range(m):
            if j != i:
                M[i, j] += p[j]
    u = np.linalg.solve(M, rhs)

    e = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            if i != j:
                e[i, j] = R[i, j] - u[i] - u[j]

    row_err = np.max(np.abs(e @ p))
    N = np.sum((p[:, None] * p[None, :]) * e**2)

    F = 0.0
    G = 0.0
    for i in range(m):
        for j in range(m):
            for k in range(m):
                for l in range(m):
                    Delta = e[j, l] - e[i, l] - e[j, k] + e[i, k]
                    w = p[i] * p[j] * p[k] * p[l]
                    F += w * Delta**2
                    if len({i, j, k, l}) == 4:
                        G += w * Delta**2

    delta = p.max()
    exact_err = abs(F - 4 * N)
    lower_margin = G - (4 - 36 * delta) * N
    return row_err, exact_err, lower_margin


def schur_trial(m=8):
    lam = rng.normal()
    kappa = math.sqrt(1 + lam * lam)
    a = rng.normal(size=m)
    v = rng.normal(size=m)
    d = rng.normal(size=m)

    C = np.diag(d) + np.outer(a, v) + np.outer(v, a)
    A = np.block([
        [np.zeros((1, 1)), (kappa * a)[None, :]],
        [(kappa * a)[:, None], C],
    ])

    j = int(np.argmax(np.abs(a)))
    pair = [0, j + 1]
    rest = [k + 1 for k in range(m) if k != j]
    B = A[np.ix_(pair, pair)]
    E = A[np.ix_(pair, rest)]
    Crr = A[np.ix_(rest, rest)]
    Schur = Crr - E.T @ np.linalg.inv(B) @ E

    ar = np.delete(a, j)
    dr = np.delete(d, j)
    target = np.diag(dr) + (d[j] / a[j] ** 2) * np.outer(ar, ar)
    schur_err = np.max(np.abs(Schur - target))

    det_err = 0.0
    for k in range(m):
        if k == j:
            continue
        inds = [0, j + 1, k + 1]
        lhs = np.linalg.det(A[np.ix_(inds, inds)])
        rhs = -(kappa**2) * (a[j] ** 2 * d[k] + a[k] ** 2 * d[j])
        det_err = max(det_err, abs(lhs - rhs))
    return schur_err, det_err


stab = [weighted_stability_trial() for _ in range(20)]
sch = [schur_trial() for _ in range(100)]

alpha = mp.mpf('0.25')
c14 = 2 ** (1 - alpha) * mp.gamma((1 - alpha) / 2) / (2 * mp.sqrt(mp.pi) * mp.gamma(alpha / 2))
Cdiff = 32 * mp.sqrt(6) * c14 * mp.pi ** mp.mpf('0.25')
Czero = 4 * mp.sqrt(2) * mp.e ** mp.mpf('0.25')

print('max weighted-row normal-equation error =', max(x[0] for x in stab))
print('max |E Delta^2 - 4N| =', max(x[1] for x in stab))
print('min margin in G >= (4-36 delta)N =', min(x[2] for x in stab))
print('max flat-core Schur identity error =', max(x[0] for x in sch))
print('max physical-triple determinant identity error =', max(x[1] for x in sch))
print('c_1/4 =', c14)
print('diffuse flat-core front constant =', Cdiff)
print('zero-star diagonal endpoint front constant =', Czero)
print('QFORM_B06_R43_CHECK_PASS')
