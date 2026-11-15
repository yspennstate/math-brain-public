# Second, independent check of C0033F Theorem 1 (general mixed collar), written from REPORT.md's statements only.
# True margin m(Q_x) at tiny x from the C0033E-check Hessian code (det(-D^2 H)/det J, 9 ambient directions),
# compared with formula (4) m0 = (1 + K/det W * eta^T N_C^{-1} eta)^{-1}; then bound (5) m0 >= 1/(2K+3) on many blocks.
import sys, itertools, random
from mpmath import mp, mpf, mpc, matrix, det, log, sqrt, inverse, exp, cos, sin, pi
import c0033e_core as core

mp.dps = 250
core.STEP = mpf(10) ** -90
I = mpc(0, 1)
B4 = []
for (i, j, val) in ((0, 0, 1), (1, 1, 1)):
    M = matrix(2, 2); M[i, j] = val; B4.append(M)
M = matrix(2, 2); M[0, 1] = 1; M[1, 0] = 1; B4.append(M)
M = matrix(2, 2); M[0, 1] = I; M[1, 0] = -I; B4.append(M)   # i(E23 - E32)
TS = [frozenset(), frozenset([0]), frozenset([1]), frozenset([0, 1])]

def Dmat(T):
    D = matrix(2, 2)
    for k in range(2):
        if k not in T: D[k, k] = 1
    return D

def pi2(C):
    return {T: (det(C - Dmat(T)) * (-1) ** (2 - len(T))).real for T in TS}

def tr(A): return A[0, 0] + A[1, 1]

def two_point(C):
    h = mpf(10) ** (-(mp.dps // 3)); p = pi2(C); n = 4
    g = [{T: (pi2(C + h * B4[i])[T] - pi2(C - h * B4[i])[T]) / (2 * h) for T in TS} for i in range(n)]
    F = matrix(n, n); N = matrix(n, n)
    for i in range(n):
        for j in range(n):
            a = pi2(C + h*B4[i] + h*B4[j]); b = pi2(C + h*B4[i] - h*B4[j]); c = pi2(C - h*B4[i] + h*B4[j]); d = pi2(C - h*B4[i] - h*B4[j])
            f = sum(g[i][T] * g[j][T] / p[T] for T in TS)
            F[i, j] = f
            N[i, j] = f + sum((1 + log(p[T])) * (a[T] - b[T] - c[T] + d[T]) / (4 * h * h) for T in TS)
    return p, F, N

def m0_formula(C, v):
    p, F, N = two_point(C)
    K = log(p[TS[1]] * p[TS[2]] / (p[TS[0]] * p[TS[3]]))
    W = matrix(2, 2)
    for T in TS:
        Mi = inverse(C - Dmat(T))
        k = (v.H * Mi * v)[0, 0]
        W += p[T] * k * Mi
    eta = matrix([tr(W * B).real for B in B4])
    q = (eta.T * inverse(N) * eta)[0, 0]
    dW = det(W).real
    # also the second expression for W in (15)
    W2 = matrix(2, 2)
    for T in TS:
        Mi = inverse(C - Dmat(T)); W2 += p[T] * Mi * v * v.H * Mi
    werr = max(abs(W[i, j] - W2[i, j]) for i in range(2) for j in range(2))
    return 1 / (1 + K / dW * q), K, werr, min(p.values())

def Qx(a, C, v, x):
    Q = matrix(3, 3); Q[0, 0] = a; s = sqrt(x)
    for k in range(2):
        Q[0, k + 1] = s * v[k].conjugate(); Q[k + 1, 0] = s * v[k]
        for l in range(2): Q[k + 1, l + 1] = C[k, l]
    return Q

def block(b, c, r, phase=0):
    C = matrix(2, 2); C[0, 0] = b; C[1, 1] = c; C[0, 1] = -r * exp(I * phase); C[1, 0] = -r * exp(-I * phase)
    return C

def unit(t1, t2, ph):
    return matrix([cos(t1), sin(t1) * exp(I * ph)])

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "all"
    if part in ("all", "thm1"):
        print("Theorem 1: true m(Q_x) at x = 1e-60 vs formula (4); independence of a; gauge invariance")
        cases = [  # (a, b, c, r, phase of C23, v angle, v phase)
            (mpf("0.3"), mpf("0.4"), mpf("0.6"), mpf("0.2"), 0, mpf("0.7"), mpf("1.1")),
            (mpf("0.8"), mpf("0.4"), mpf("0.6"), mpf("0.2"), 0, mpf("0.7"), mpf("1.1")),
            (mpf("0.5"), mpf("0.1"), mpf("0.85"), mpf("0.25"), 0, mpf("0.2"), mpf("2.5")),
            (mpf("0.5"), mpf("0.1"), mpf("0.85"), mpf("0.25"), mpf("0.9"), mpf("0.2"), mpf("2.5")),
            (mpf("0.05"), mpf("0.02"), mpf("0.03"), mpf("0.015"), 0, mpf("1.3"), mpf("0.4")),
            (mpf("0.6"), mpf("0.97"), mpf("0.5"), mpf("0.1"), 0, mpf("0"), 0),   # v = e2: one connection zero
        ]
        for (a, b, c, r, ph, t, vph) in cases:
            C = block(b, c, r, ph); v = unit(t, 0, vph)
            m0, K, werr, pmin = m0_formula(C, v)
            m, err, Lam = core.margin(Qx(a, C, v, mpf(10) ** -60))
            print(f"  a={float(a)} b={float(b)} c={float(c)} r={float(r)} ph={float(ph):.2f}: m={float(m.real):.15f} "
                  f"(4)={float(m0):.15f} diff={float(abs(m-m0)):.1e} K={float(K):.4f} 1/(2K+3)={float(1/(2*K+3)):.4f} "
                  f"W-eq err={float(werr):.1e} id err={float(err):.1e}", flush=True)
    if part in ("all", "bound5"):
        mp.dps = 90
        random.seed(20261114)
        worst = (mpf(10), None); n = 0; viol = 0
        for it in range(int(sys.argv[2]) if len(sys.argv) > 2 else 400):
            # random strict 2x2 contraction with eigenvalues l1, l2 (some near 0/1), random complex v
            mode = it % 4
            def ev():
                u = random.random()
                if mode == 0: return mpf(u)
                if mode == 1: return mpf(10) ** (-random.uniform(1, 8))
                if mode == 2: return 1 - mpf(10) ** (-random.uniform(1, 8))
                return mpf(10) ** (-random.uniform(1, 8)) if random.random() < 0.5 else 1 - mpf(10) ** (-random.uniform(1, 8))
            l1, l2 = ev(), ev()
            th = mpf(random.uniform(0.05, 1.52)); U = matrix([[cos(th), -sin(th)], [sin(th), cos(th)]])
            C = U * matrix([[l1, 0], [0, l2]]) * U.T
            if C[0, 1] > 0:  # gauge to negative off-diagonal
                C[0, 1] = -C[0, 1]; C[1, 0] = -C[1, 0]
            v = unit(mpf(random.uniform(0, 1.5708)), 0, mpf(random.uniform(0, 6.28)))
            m0, K, werr, pmin = m0_formula(C, v)
            ratio = m0 * (2 * K + 3); n += 1
            if ratio < 1: viol += 1
            if ratio < worst[0]: worst = (ratio, (float(l1), float(l2), float(th), float(K)))
        print(f"Bound (5): {n} blocks, violations of m0 >= 1/(2K+3): {viol}; smallest m0*(2K+3) = {float(worst[0]):.4f} at (l1,l2,th,K)={worst[1]}")
