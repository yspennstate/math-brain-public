"""Independent generator for the T255 attention SDE, from the formulas in M2_EXACT.md section 1 only
(agent H, 17 Oct 2026). Nothing from rows/T255/*.py was read.

  dV = b(V) dt + L dGamma L^T,  dGamma = sqrt(c) dH + k (dN K + K dN^T),  K = L^T P L,  V = L L^T
  c = g2 (2 - g2), k = g2/(m tau0); H GOE BM (diag var 2, offdiag var 1), N iid m x m BM, independent.
  b(V) = (g2/tau0^2) [ V |W|_F^2/m^2 + (1/2m)(v (V D)^T + (V D) v^T) ],  W = P V P, v = diag V, D = diag W - (tr W/m) 1.

Generator of a scalar F: drift = DF[b] + 1/2 sum_alpha D^2F[E_alpha, E_alpha], E_alpha the noise directions.
Everything in mpmath; second directional derivatives by a 4th-order central difference with step 1e-30 |V|/|E| at 100 digits.
"""
import itertools
import mpmath as mp

mp.mp.dps = 100
H_REL = mp.mpf("1e-30")


def mat(rows):
    return mp.matrix(rows)


def P_of(m):
    return mp.matrix([[(1 if i == j else 0) - mp.mpf(1) / m for j in range(m)] for i in range(m)])


def drift_b(V, g2, tau0):
    m = V.rows
    P = P_of(m)
    W = P * V * P
    W2 = sum(W[i, j] ** 2 for i in range(m) for j in range(m))
    v = mp.matrix([V[i, i] for i in range(m)])
    trW = sum(W[i, i] for i in range(m))
    D = mp.matrix([W[i, i] - trW / m for i in range(m)])
    VD = V * D
    out = V * (W2 / m ** 2) + (v * VD.T + VD * v.T) * (mp.mpf(1) / (2 * m))
    return out * (g2 / tau0 ** 2)


def noise_dirs(V, g2, tau0, with_c=True, with_att=True):
    m = V.rows
    L = mp.cholesky(V)
    P = P_of(m)
    K = L.T * P * L
    c = g2 * (2 - g2)
    k = g2 / (m * tau0)
    dirs = []
    if with_c:
        for i in range(m):
            G = mp.zeros(m, m); G[i, i] = mp.sqrt(2)
            dirs.append(L * (G * mp.sqrt(c)) * L.T)
        for i, j in itertools.combinations(range(m), 2):
            G = mp.zeros(m, m); G[i, j] = 1; G[j, i] = 1
            dirs.append(L * (G * mp.sqrt(c)) * L.T)
    if with_att:
        for i in range(m):
            for j in range(m):
                F = mp.zeros(m, m); F[i, j] = 1
                dirs.append(L * ((F * K + K * F.T) * k) * L.T)
    return dirs


def _nrm(A):
    return mp.sqrt(sum(A[i, j] ** 2 for i in range(A.rows) for j in range(A.cols)))


def _step(V, E):
    return H_REL * _nrm(V) / _nrm(E)


def d1(F, V, E, h=None):
    h = _step(V, E) if h is None else h
    return (-F(V + 2 * h * E) + 8 * F(V + h * E) - 8 * F(V - h * E) + F(V - 2 * h * E)) / (12 * h)


def d2(F, V, E, h=None):
    h = _step(V, E) if h is None else h
    return (-F(V + 2 * h * E) + 16 * F(V + h * E) - 30 * F(V) + 16 * F(V - h * E) - F(V - 2 * h * E)) / (12 * h * h)


def generator(F, V, g2, tau0, with_c=True, with_att=True):
    """(drift per unit t, quadratic variation rate per unit t) of F(V)."""
    b = drift_b(V, g2, tau0)
    dirs = noise_dirs(V, g2, tau0, with_c, with_att)
    drift = d1(F, V, b) + sum(d2(F, V, E) for E in dirs) / 2
    qv = sum(d1(F, V, E) ** 2 for E in dirs)
    return drift, qv


def W2_of(V):
    m = V.rows
    P = P_of(m)
    W = P * V * P
    return sum(W[i, j] ** 2 for i in range(m) for j in range(m))
