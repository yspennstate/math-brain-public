"""Float transcription of iv_scm.full_driver (reference path and frames only; never decides an inequality)."""
import numpy as np
from math import pi
MU = 2 / pi
SIGNS = np.array([-1., -1., 1., 1.])

def f(x, eta):
    Q = np.array([[x[0], x[1]], [x[1], x[2]]]); R = np.array([[x[3], x[4]], [x[5], x[6]]])
    G = np.zeros((4, 4)); G[:2, :2] = Q; G[:2, 2:] = R; G[2:, :2] = R.T; G[2:, 2:] = np.eye(2)
    A = np.array([[MU / np.sqrt((1 + Q[i, i]) * (1 + Q[j, j]) - Q[i, j] ** 2) for j in range(2)] for i in range(2)])
    T = np.array([[MU / np.sqrt(2 * (1 + Q[i, i]) - R[i, m] ** 2) for m in range(2)] for i in range(2)])
    beta = [(sum(Q[i, j] * A[i, j] for j in range(2)) - sum(R[i, m] * T[i, m] for m in range(2))) / (1 + Q[i, i]) for i in range(2)]
    C = {}
    for i, j in [(0, 0), (0, 1), (1, 1)]:
        if i == j:
            den = 1 + 2 * G[i, i]; Tl = G - 2 * np.outer(G[:, i], G[i, :]) / den
        else:
            den = (1 + G[i, i]) * (1 + G[j, j]) - G[i, j] ** 2
            Tl = G - ((1 + G[j, j]) * np.outer(G[:, i], G[i, :]) - G[i, j] * (np.outer(G[:, i], G[j, :]) + np.outer(G[:, j], G[i, :]))
                      + (1 + G[i, i]) * np.outer(G[:, j], G[j, :])) / den
        d = np.sqrt(1 + np.diag(Tl)); arg = Tl / np.outer(d, d)
        C[i, j] = A[i, j] * MU * float(SIGNS @ np.arcsin(arg) @ SIGNS)
    out = []
    for i, j in [(0, 0), (0, 1), (1, 1)]:
        det = (beta[i] + beta[j]) * Q[i, j] - sum(A[i, l] * Q[l, j] + A[j, l] * Q[l, i] for l in range(2)) \
              + sum(T[i, m] * R[j, m] + T[j, m] * R[i, m] for m in range(2))
        out.append(eta * det + eta ** 2 * C[i, j])
    out += [eta * (T[i, m] + beta[i] * R[i, m] - sum(A[i, j] * R[j, m] for j in range(2))) for i in range(2) for m in range(2)]
    return np.array(out)

def jac(x, eta, h=1e-7):
    J = np.zeros((7, 7))
    for k in range(7):
        d = np.zeros(7); d[k] = h; J[:, k] = (f(x + d, eta) - f(x - d, eta)) / (2 * h)
    return J
