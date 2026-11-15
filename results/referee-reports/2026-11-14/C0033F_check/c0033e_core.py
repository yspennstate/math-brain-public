# Second, independent check of C0033E (three-point determinantal entropy margin m = 1 - theta).
# Written from REPORT.md's statements only. m is computed two ways at each point:
#   (a) m = det(-D^2 H) / det(J), with -D^2 H from finite differences of H in mpmath (no atom formula),
#   (b) J from (9): J = F + d tr(R^{-1} E_i R^{-1} E_j), R = diag(l23, l13, l12) - gamma Q,
# and the identity -D^2 H = J - d z z^T is checked entrywise. Then (1), (2), (4)-(6) and the trend in (8).
import itertools
from mpmath import mp, mpf, mpc, matrix, det, log, sqrt, inverse

mp.dps = 300
STEP = mpf(10) ** -80

def basis():
    E = []
    for i in range(3):
        M = matrix(3, 3); M[i, i] = 1; E.append(M)
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        M = matrix(3, 3); M[i, j] = 1; M[j, i] = 1; E.append(M)
        M = matrix(3, 3); M[i, j] = mpc(0, 1); M[j, i] = mpc(0, -1); E.append(M)
    return E
E = basis()
SUBSETS = [frozenset(s) for k in range(4) for s in itertools.combinations(range(3), k)]

def atoms(Q):
    p = {}
    for S in SUBSETS:
        D = matrix(3, 3)
        for i in range(3):
            if i not in S:
                D[i, i] = 1
        v = det(Q - D) * (-1) ** (3 - len(S))
        p[S] = v.real
    return p

def H(Q):
    return -sum(v * log(v) for v in atoms(Q).values())

def neg_hess(Q):
    # -D^2 H = sum_S [ Dp Dp^T / p + (1 + log p) D^2 p ]; p_S is a cubic polynomial, so central differences of p
    # are exact for D^2 p and accurate to STEP^2 for Dp. This avoids differencing H itself.
    n = len(E); h = STEP; p = atoms(Q)
    plus = [atoms(Q + h * E[i]) for i in range(n)]; minus = [atoms(Q - h * E[i]) for i in range(n)]
    g = [{S: (plus[i][S] - minus[i][S]) / (2 * h) for S in SUBSETS} for i in range(n)]
    Hm = matrix(n, n)
    for i in range(n):
        for j in range(i, n):
            a = atoms(Q + h * E[i] + h * E[j]); b = atoms(Q + h * E[i] - h * E[j])
            c = atoms(Q - h * E[i] + h * E[j]); d = atoms(Q - h * E[i] - h * E[j])
            v = mpf(0)
            for S in SUBSETS:
                d2 = (a[S] - b[S] - c[S] + d[S]) / (4 * h * h)
                v += g[i][S] * g[j][S] / p[S] + (1 + log(p[S])) * d2
            Hm[i, j] = Hm[j, i] = v
    return Hm

def J_and_z(Q):
    p = atoms(Q); n = len(E); h = STEP
    grads = {S: [(atoms(Q + h * E[i])[S] - atoms(Q - h * E[i])[S]) / (2 * h) for i in range(n)] for S in SUBSETS}
    F = matrix(n, n)
    for S in SUBSETS:
        for i in range(n):
            for j in range(n):
                F[i, j] += grads[S][i] * grads[S][j] / p[S]
    P = lambda *ix: p[frozenset(ix)]
    l = {}
    for (i, j) in ((1, 2), (0, 2), (0, 1)):
        l[(i, j)] = log(P(i) * P(j) / (P() * P(i, j)))
    gamma = log(P(0, 1, 2) * P(0) * P(1) * P(2) / (P() * P(0, 1) * P(0, 2) * P(1, 2)))
    R = matrix(3, 3)
    R[0, 0] = l[(1, 2)]; R[1, 1] = l[(0, 2)]; R[2, 2] = l[(0, 1)]
    R = R - gamma * Q
    d = det(R).real; Ri = inverse(R)
    z = [ (Ri * E[i]).apply(lambda x: x) for i in range(n)]
    z = [sum((Ri * E[i])[k, k] for k in range(3)).real for i in range(n)]
    J = matrix(n, n)
    for i in range(n):
        for j in range(n):
            tr = sum((Ri * E[i] * Ri * E[j])[k, k] for k in range(3)).real
            J[i, j] = F[i, j] + d * tr
    return J, z, d, min(p.values())

def margin(Q, check_identity=True):
    N = neg_hess(Q); J, z, d, pmin = J_and_z(Q)
    err = mpf(0)
    if check_identity:
        for i in range(9):
            for j in range(9):
                err = max(err, abs(N[i, j] - (J[i, j] - d * z[i] * z[j])) / (1 + abs(N[i, j])))
    return det(N) / det(J), err, -log(pmin)

def cyclic(r):
    i = mpc(0, 1)
    return matrix([[mpf(1) / 2, i * r, -i * r], [-i * r, mpf(1) / 2, i * r], [i * r, -i * r, mpf(1) / 2]])

def formula1(r):
    u = r * r; k = (1 + 4 * u) / (1 - 12 * u); L = log(k)
    A = 9*k**3 - 15*k**2 + 3*k + 3 + (6*k**2 + 6*k - 4)*L - (3*k**2 + k)*L**2
    B = 36*k**3 - 60*k**2 + 12*k + 12 + (9*k**3 + 33*k**2 - 21*k + 11)*L + (6*k**2 + 2*k)*L**2
    return 4 * A / B, L

def collar(a, h, e):
    return matrix([[a, e, e], [e, mpf(1) / 2, h - mpf(1) / 2], [e, h - mpf(1) / 2, mpf(1) / 2]])

def m0(h):
    b0 = h * (1 - h); b1 = mpf(1) / 2 - b0; k = b1 / b0; K = 2 * log(k)
    f = 1 / b0 - 1 / (2 * b1); g = 1 / (2 * b1); v = 1 / b0 - 3
    return (f**2 - (g - K)**2) / (f**2 - g**2 + f * K * (v + 1 / v) + K**2), K, k

if __name__ == "__main__":
    print("Theorem 1, cyclic family: m from Hessian vs formula (1)")
    for r in [mpf("0.05"), mpf("0.15"), mpf("0.25")]:
        m, err, Lam = margin(cyclic(r)); f1, L = formula1(r)
        print(f"  r={float(r):.3f} m={float(m):.12f} (1)={float(f1):.12f} diff={float(abs(m-f1)):.1e} identity err={float(err):.1e}", flush=True)
    for k in [mpf(60), mpf(500), mpf(10)**4]:
        u = (k - 1) / (4 * (3 * k + 1)); r = sqrt(u)
        m, err, Lam = margin(cyclic(r)); f1, L = formula1(r)
        rem = abs(m - 4 / (L + 4)); bound = mpf(10) / 3 * L * mp.e ** (-L)
        print(f"  k={float(k):g} L={float(L):.3f} m={float(m):.10f} (1)={float(f1):.10f} m>=2/(L+2): {m >= 2/(L+2)} "
              f"|m-4/(L+4)|={float(rem):.2e} <= {float(bound):.2e}: {rem <= bound}", flush=True)
    print("Theorem 2, collar: m at tiny x vs m0(h), and (6)")
    for (a, h) in [(mpf("0.3"), mpf("0.2")), (mpf("0.9"), mpf("0.05")), (mpf("0.01"), mpf("0.25"))]:
        e = mpf(10) ** -25
        m, err, Lam = margin(collar(a, h, e)); mm, K, k = m0(h)
        ok6 = mm >= 1 / (K + 1) and (k < 2 or mm - 1 / (K + 1) <= 3 / (k * (K + 1)))
        print(f"  a={float(a)} h={float(h)} m={float(m):.12f} m0={float(mm):.12f} diff={float(abs(m-mm)):.1e} (6) ok: {ok6} "
              f"(7): m >= 1/(4 Lambda+2)={float(1/(4*Lam+2)):.4f}: {m >= 1/(4*Lam+2)} identity err={float(err):.1e}", flush=True)
    print("Corollary 3: Lambda * m along Q(1/2, h, h^6)")
    for hexp in [3, 6, 12]:
        mp.dps = 300 + 12 * hexp
        globals()["STEP"] = mpf(10) ** -(80 + 7 * hexp)
        h = mpf(10) ** -hexp
        m, err, Lam = margin(collar(mpf(1) / 2, h, h ** 6), check_identity=False)
        mm, K, k = m0(h)
        print(f"  h=1e-{hexp} m={float(m):.6e} m0={float(mm):.6e} Lambda={float(Lam):.4f} Lambda*m={float(Lam*m):.5f}", flush=True)
