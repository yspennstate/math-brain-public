"""Adversarial numerical audit of STRAT6 RESULT.md (n=5, D=2), with my own term code.
1. equal gap: min of T(g,g) over frames at g = G (claimed >= 0) and at g = G + 0.01, G + 0.03 (no claim);
2. uniform ceiling: min of T at a = 58/125 for r on a grid of [3/25, 1] (claimed >= 0);
3. moment inequalities (M1) and K >= 4/5: worst slack over frames by local search;
4. (W2) first line: N_a >= F^2/s - lam(2-K)/5 + S^2/2 on random frames;
5. (R1) as an identity along a ray: T(a) vs a(1-a/a_end)L + (a/a_end)^2 T(a_end).
usage: python t104_audit_strat6_result.py starts seed"""
import sys
import numpy as np
from scipy.optimize import minimize

ST, rng = int(sys.argv[1]), np.random.default_rng(int(sys.argv[2]))
B0 = np.linalg.qr(np.column_stack([np.ones(5), np.random.default_rng(1).standard_normal((5, 4))]))[0][:, 1:]
G_EQ = 0.551713118178820


def frame(x):
    Q = np.linalg.qr(x.reshape(4, 2))[0]
    return B0 @ Q[:, 0], B0 @ Q[:, 1]


def T_of(W, tol=1e-9):
    N = W.shape[0]; L = np.diag(W.sum(1)) - W
    ev, U = np.linalg.eigh(L); lm = ev[-1]; top = np.where(ev > lm - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T; G = lm * (np.eye(N) - np.ones((N, N)) / N) - L
    cc = 2 * N / (N - 2); beta = (1 - lm) / (N - 2)
    X1 = D * (lm * np.trace(G) - np.trace(G @ G)); X2 = cc * np.trace(G @ (Pi * G))
    X3 = beta * (D * np.trace(G) - cc * float(np.diag(Pi) @ np.diag(G)))
    S5 = sum(W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (G[i, i] + G[j, j] - 2 * G[i, j])
             for i in range(N) for j in range(i + 1, N))
    return D, X1 + X2 + X3 - 2 * S5, ev


def weights(u, w, a, b):
    lam = (2 + a + b) / 4
    W = lam / 5 + a * np.outer(u, u) + b * np.outer(w, w); np.fill_diagonal(W, 0)
    return W


def objective(x, a, b):
    u, w = frame(x); W = weights(u, w, a, b)
    neg = -min(W.min(), 0.0)
    D, T, ev = T_of(W)
    if neg > 0:
        return 10 + 100 * neg
    if D != 2 or ev[1] < 1e-7:  # wrong top multiplicity or disconnected: outside the stratum
        return 10.0
    return T


def search(a, b, starts):
    best = np.inf; bx = None
    for _ in range(starts):
        r = minimize(objective, rng.standard_normal(8), args=(a, b), method="Nelder-Mead",
                     options=dict(maxiter=3000, xatol=1e-10, fatol=1e-13))
        if r.fun < best:
            best, bx = r.fun, r.x
    return best, bx


print("1. equal gap (claimed T >= 0 for g <= G = %.6f)" % G_EQ)
for g in (G_EQ * (1 - 1e-9), G_EQ + 0.01, G_EQ + 0.03):
    m, _ = search(g, g, ST)
    print("   g %.5f  min T %.4e%s" % (g, m, "  (infeasible everywhere)" if m >= 10 else ""))

print("2. uniform ceiling a = 58/125 (claimed T >= 0 for every r)")
worst = np.inf
for r in np.linspace(0.12, 1.0, 12):
    m, _ = search(58 / 125, r * 58 / 125, max(ST // 3, 4))
    worst = min(worst, m)
    print("   r %.3f  min T %.4e" % (r, m))
print("   worst %.4e" % worst)

print("3. moment inequalities (worst slack; negative would refute)")
ineqs = [("(3/2)A+C<=27/25", lambda A, B, C: 27 / 25 - 1.5 * A - C), ("2A+C<=7/5", lambda A, B, C: 7 / 5 - 2 * A - C),
         ("2A+C<=11/8", lambda A, B, C: 11 / 8 - 2 * A - C), ("3A+C<=81/40", lambda A, B, C: 81 / 40 - 3 * A - C),
         ("4A+C<=107/40", lambda A, B, C: 107 / 40 - 4 * A - C), ("A-C<=5/8", lambda A, B, C: 5 / 8 - A + C),
         ("2A-C<=51/40", lambda A, B, C: 51 / 40 - 2 * A + C), ("3A-C<=77/40", lambda A, B, C: 77 / 40 - 3 * A + C),
         ("K>=4/5", lambda A, B, C: A + B + 2 * C - 0.8)]


def mom(x):
    u, w = frame(x)
    return (u ** 4).sum(), (w ** 4).sum(), (u * u * w * w).sum()


for name, f in ineqs:
    best = np.inf
    for _ in range(ST):
        r = minimize(lambda x: f(*mom(x)), rng.standard_normal(8), method="Nelder-Mead",
                     options=dict(maxiter=4000, xatol=1e-12, fatol=1e-14))
        best = min(best, r.fun)
    print("   %-18s worst slack %.3e" % (name, best))

print("4. (W2) N_a lower bound and 5. (R1) ray identity, random frames")
w2 = np.inf; r1 = 0.0
for _ in range(20000):
    u, w = frame(rng.standard_normal(8))
    r = rng.uniform(0.05, 1); a = rng.uniform(0.05, 0.9); b = r * a
    W = weights(u, w, a, b)
    if W.min() < 0:
        continue
    lam = (2 + a + b) / 4; s = a + b
    A, B, C = (u ** 4).sum(), (w ** 4).sum(), (u * u * w * w).sum()
    d, e, f, h = (u ** 3).sum(), (u * u * w).sum(), (u * w * w).sum(), (w ** 3).sum()
    F = a * (A + C) + b * (B + C); K = A + B + 2 * C; S = s - F - 2 * lam / 5
    Na = a * (d * d + 2 * e * e + f * f) + b * (e * e + 2 * f * f + h * h)
    w2 = min(w2, Na - (F * F / s - lam * (2 - K) / 5 + S * S / 2))
    # ray: a_end from D_ij
    Dij = [-1 - r - 20 * (u[i] * u[j] + r * w[i] * w[j]) for i in range(5) for j in range(i + 1, 5)]
    a_end = 2 / max(3 - r, max(Dij))
    if a > a_end:
        continue
    D1, Ta, _ = T_of(W); D2, Te, _ = T_of(weights(u, w, a_end * (1 - 1e-12), r * a_end * (1 - 1e-12)))
    D0, Ts, _ = T_of(weights(u, w, 1e-6, r * 1e-6))
    if D1 != 2 or D2 != 2 or D0 != 2:
        continue
    Lr = Ts / 1e-6
    r1 = max(r1, abs(Ta - (a * (1 - a / a_end) * Lr + (a / a_end) ** 2 * Te)))
print("   W2 worst slack %.3e   R1 worst |difference| %.3e" % (w2, r1))
