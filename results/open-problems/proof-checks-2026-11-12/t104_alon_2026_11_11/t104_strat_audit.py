"""Independent audit of the Codex STRAT circulant certificates (n = 5, 6, 7).
For each sector: enumerate the sector polytope's vertices from its inequalities, evaluate the target
T = Ptotal - Qtotal at the vertices and midpoints from the original pair definitions (real Fourier
eigenvectors, P_l and Q_l summed over the top pairs), and print q_ij = 2T(mid) - (T_i + T_j)/2.
Also checks the trace form against the pair form, and the n = 7 rational interval bounds exactly.
usage: python t104_strat_audit.py
"""
import itertools
from fractions import Fraction as Fr
import numpy as np


def circ_L(n, x):
    m = n // 2
    W = np.zeros((n, n))
    for r in range(1, m + 1):
        wr = x[r - 1] / n if 2 * r != n else 2 * x[r - 1] / n
        for i in range(n):
            j = (i + r) % n
            W[i, j] = W[j, i] = wr
    return np.diag(W.sum(1)) - W, W


def fourier(n, k):
    i = np.arange(n)
    if 2 * k == n:
        return [np.cos(np.pi * i) / np.sqrt(n)]
    return [np.cos(2 * np.pi * k * i / n) * np.sqrt(2 / n), np.sin(2 * np.pi * k * i / n) * np.sqrt(2 / n)]


def eig_a(n, x, k):
    m = n // 2
    return (2 / n) * sum(x[r - 1] * (1 - np.cos(2 * np.pi * k * r / n)) for r in range(1, m + 1))


def T_pair(n, x, K):
    L, W = circ_L(n, x)
    lam = eig_a(n, x, K[0])
    top = [v for k in K for v in fourier(n, k)]
    rest = [v for k in range(1, n // 2 + 1) if k not in K for v in fourier(n, k)]
    c = 2 * n / (n - 2)
    edges = [(i, j, W[i, j]) for i in range(n) for j in range(i + 1, n) if W[i, j] != 0]
    P = Q = 0.0
    for v in rest:
        mu = v @ L @ v
        g = lam - mu
        for u in top:
            p = u * v
            P += g * (mu + c * (lam * p @ p - p @ L @ p) + (1 - lam) * (1 - c * p @ p) / (n - 2))
            Q += g * 2 * sum(w * (u[i] - u[j]) ** 2 * (v[i] - v[j]) ** 2 for i, j, w in edges)
    return P - Q, P, Q, lam


def T_trace(n, x, K):
    L, W = circ_L(n, x)
    lam = eig_a(n, x, K[0])
    top = [v for k in K for v in fourier(n, k)]
    D = len(top)
    Pi = sum(np.outer(u, u) for u in top)
    G = lam * (np.eye(n) - np.ones((n, n)) / n) - L
    d = np.diag(L)
    S1 = D * (2 * lam - np.trace(L @ L))
    S2 = np.diag(Pi) @ np.diag(G)
    S3 = np.trace(L @ (Pi * G))
    S4 = D * np.trace(G)
    S5 = sum(W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (2 * lam - d[i] - d[j] - 2 * W[i, j])
             for i in range(n) for j in range(i + 1, n) if W[i, j] != 0)
    c = 2 * n / (n - 2)
    return S1 + c * (lam * S2 - S3) + (1 - lam) / (n - 2) * (S4 - c * S2) - 2 * S5


def sector_vertices(n, K):
    m = n // 2
    rows = [np.eye(m)[r] for r in range(m)]  # x_r >= 0
    k0 = K[0]
    for j in range(1, m + 1):
        if j in K:
            continue
        rows.append(np.array([(2 / n) * ((1 - np.cos(2 * np.pi * k0 * r / n)) - (1 - np.cos(2 * np.pi * j * r / n)))
                              for r in range(1, m + 1)]))
    eqs = [np.array([(2 / n) * ((1 - np.cos(2 * np.pi * k0 * r / n)) - (1 - np.cos(2 * np.pi * k * r / n)))
                     for r in range(1, m + 1)]) for k in K[1:]]
    R = np.array(rows)
    verts = []
    free = m - 1 - len(eqs)
    for S in itertools.combinations(range(len(rows)), free):
        A = np.vstack([np.ones(m)] + eqs + [R[s] for s in S])
        b = np.zeros(A.shape[0]); b[0] = 1
        if abs(np.linalg.det(A)) < 1e-12:
            continue
        xv = np.linalg.solve(A, b)
        if (R @ xv >= -1e-12).all() and not any(np.abs(xv - v).max() < 1e-9 for v in verts):
            verts.append(xv)
    return verts


def qmat(n, K, V):
    Tv = [T_pair(n, v, K)[0] for v in V]
    s = len(V)
    q = np.zeros((s, s))
    for a in range(s):
        for b in range(s):
            q[a, b] = Tv[a] if a == b else 2 * T_pair(n, (V[a] + V[b]) / 2, K)[0] - (Tv[a] + Tv[b]) / 2
    return q


s5 = np.sqrt(5)
t = 2 * np.cos(2 * np.pi / 7); bb = t * t - t; aa = 1 - bb
cases = [
    (5, [1], [np.array([0, 1.0]), np.array([.5, .5])],
     np.array([[28 * s5 - 40, 14 * s5], [14 * s5, 0]]) / 225),
    (6, [1], [np.array([0, 0, 1.0]), np.array([0, 1.0, 0]), np.array([.4, .4, .2])],
     np.array([[1 / 9, 47 / 144, 5 / 18], [47 / 144, 1 / 16, 5 / 48], [5 / 18, 5 / 48, 0]])),
    (6, [2], [np.array([0, 1.0, 0]), np.array([.75, .25, 0]), np.array([.4, .4, .2])],
     np.array([[1 / 16, 3 / 16, 5 / 48], [3 / 16, 1 / 8, 5 / 48], [5 / 48, 5 / 48, 0]])),
    (6, [1, 3], [np.array([0, 0, 1.0]), np.array([.4, .4, .2])], np.array([[1 / 6, 5 / 12], [5 / 12, 0]])),
    (6, [2, 3], [np.array([.75, .25, 0]), np.array([.4, .4, .2])], np.array([[19 / 96, 5 / 32], [5 / 32, 0]])),
]
M7 = {(0, 0): (552, 456, -1104), (0, 1): (402, 300, -612), (0, 2): (942, -240, -852), (0, 3): (234, 234, -312),
      (1, 1): (-3384, 2988, 1680), (1, 2): (1116, -612, -720), (1, 3): (468, -234, -312), (2, 2): (-2484, 2268, 1200),
      (2, 3): (468, -234, -312), (3, 3): (0, 0, 0)}
q7 = np.zeros((4, 4))
for (i, j), (A, B, C) in M7.items():
    q7[i, j] = q7[j, i] = (A * t * t + B * t + C) / 1225
cases.append((7, [1], [np.array([0, 0, 1.0]), np.array([0, aa, bb]), np.array([bb, 0, aa]), np.ones(3) / 3], q7))

worst = 0.0
for n, K, V, qc in cases:
    mine = sector_vertices(n, K)
    same = len(mine) == len(V) and all(any(np.abs(u - v).max() < 1e-9 for u in mine) for v in V)
    q = qmat(n, K, V)
    dtr = max(abs(T_pair(n, v, K)[0] - T_trace(n, v, K)) for v in V)
    err = np.abs(q - qc).max(); worst = max(worst, err)
    print("n %d K %s  sector vertices match: %s (%d found)  max|q - certificate| %.2e  min q %.4f  pair-vs-trace %.1e"
          % (n, K, same, len(mine), err, q.min(), dtr))
    rng = np.random.default_rng(n * 10 + K[0])
    for _ in range(200):  # random interior points: T >= 0 and quadratic identity
        al = rng.dirichlet(np.ones(len(V)))
        x = sum(a * v for a, v in zip(al, V))
        Tx = T_pair(n, x, K)[0]
        assert abs(Tx - al @ q @ al) < 1e-12 and Tx > -1e-13, (n, K, Tx)
    print("   200 random sector points: T = alpha' q alpha to 1e-12 and T >= 0")

# n = 7: exact interval check
f = lambda s: s ** 3 + s ** 2 - 2 * s - 1
lo, hi = Fr(1246, 1000), Fr(1247, 1000)
print("n 7 root bracket: f(lo) = %s < 0, f(hi) = %s > 0" % (f(lo), f(hi)), f(lo) < 0 < f(hi))
lbs = []
for (i, j), (A, B, C) in M7.items():
    if (A, B, C) == (0, 0, 0):
        continue
    # exact minimum of A s^2 + B s + C on [lo, hi]
    pts = [lo, hi]
    if A != 0 and lo < Fr(-B, 2 * A) < hi:
        pts.append(Fr(-B, 2 * A))
    lbs.append(min(A * s * s + B * s + C for s in pts) / 1225)
print("n 7 exact min over the bracket of the nine nonzero entries: %s = %.6f (claimed lower bound 3836859/38281250 = %.6f)"
      % (min(lbs), float(min(lbs)), 3836859 / 38281250))
print("largest certificate discrepancy %.2e" % worst)
