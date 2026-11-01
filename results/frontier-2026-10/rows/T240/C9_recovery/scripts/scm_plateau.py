"""Saad-Solla ODE for a soft committee machine (erf g(z)=erf(z/sqrt2), output weights 1, noiseless), K=M=2, T=I.
Find the symmetric plateau fixed point and the eigenvalues of the full Jacobian there."""
import numpy as np
from scipy.optimize import fsolve
import sys

PI = np.pi


def I3(C, a, b, c):
    C11, C12, C13, C22, C23, C33 = C[a, a], C[a, b], C[a, c], C[b, b], C[b, c], C[c, c]
    L3 = (1 + C11) * (1 + C33) - C13 ** 2
    return 2 / PI / np.sqrt(L3) * (C23 * (1 + C11) - C12 * C13) / (1 + C11)


def I4(C, a, b, c, d):
    C11, C12, C13, C14 = C[a, a], C[a, b], C[a, c], C[a, d]
    C22, C23, C24, C33, C34, C44 = C[b, b], C[b, c], C[b, d], C[c, c], C[c, d], C[d, d]
    L4 = (1 + C11) * (1 + C22) - C12 ** 2
    L0 = L4 * C34 - C23 * C24 * (1 + C11) - C13 * C14 * (1 + C22) + C12 * C13 * C24 + C12 * C14 * C23
    L1 = L4 * (1 + C33) - C23 ** 2 * (1 + C11) - C13 ** 2 * (1 + C22) + 2 * C12 * C13 * C23
    L2 = L4 * (1 + C44) - C24 ** 2 * (1 + C11) - C14 ** 2 * (1 + C22) + 2 * C12 * C14 * C24
    return 4 / PI ** 2 / np.sqrt(L4) * np.arcsin(L0 / np.sqrt(L1 * L2))


K = M = 2


def unpack(z):
    Q = np.array([[z[0], z[1]], [z[1], z[2]]])
    R = np.array([[z[3], z[4]], [z[5], z[6]]])
    return Q, R


def rhs(z, eta):
    Q, R = unpack(z)
    C = np.zeros((4, 4))
    C[:2, :2] = Q
    C[:2, 2:] = R
    C[2:, :2] = R.T
    C[2:, 2:] = np.eye(2)
    S = range(K)
    Tt = range(K, K + M)
    dR = np.zeros((2, 2))
    for i in S:
        for n in Tt:
            dR[i, n - K] = eta * (sum(I3(C, i, n, m) for m in Tt) - sum(I3(C, i, n, j) for j in S))
    dQ = np.zeros((2, 2))
    for i in S:
        for k in S:
            lin = sum(I3(C, i, k, m) for m in Tt) - sum(I3(C, i, k, j) for j in S)
            lin += sum(I3(C, k, i, m) for m in Tt) - sum(I3(C, k, i, j) for j in S)
            quad = (sum(I4(C, i, k, n, m) for n in Tt for m in Tt) - 2 * sum(I4(C, i, k, j, n) for j in S for n in Tt)
                    + sum(I4(C, i, k, j, l) for j in S for l in S))
            dQ[i, k] = eta * lin + eta ** 2 * quad
    return np.array([dQ[0, 0], dQ[0, 1], dQ[1, 1], dR[0, 0], dR[0, 1], dR[1, 0], dR[1, 1]])


def eg(z):
    Q, R = unpack(z)
    t = sum(np.arcsin(Q[i, k] / np.sqrt((1 + Q[i, i]) * (1 + Q[k, k]))) for i in range(2) for k in range(2))
    t += sum(np.arcsin(0.0 / 2) for n in range(2) for m in range(2)) + 2 * np.arcsin(1 / 2.0)
    t -= 2 * sum(np.arcsin(R[i, n] / np.sqrt((1 + Q[i, i]) * 2)) for i in range(2) for n in range(2))
    return t / PI


def sym_rhs(s, eta):
    q, c, r = s
    z = np.array([q, c, q, r, r, r, r])
    d = rhs(z, eta)
    return [d[0], d[1], d[3]]


for eta in [float(x) for x in sys.argv[1:]] or [0.1, 0.5, 1.0]:
    # integrate the symmetric ODE from a small symmetric start to land on the plateau
    s = np.array([0.2, 0.0, 0.0001])
    dt = 0.05
    for _ in range(40000):
        s = s + dt * np.array(sym_rhs(s, eta))
    sp = fsolve(sym_rhs, s, args=(eta,), xtol=1e-13)
    z = np.array([sp[0], sp[1], sp[0], sp[2], sp[2], sp[2], sp[2]])
    J = np.zeros((7, 7))
    h = 1e-6
    for j in range(7):
        e = np.zeros(7); e[j] = h
        J[:, j] = (rhs(z + e, eta) - rhs(z - e, eta)) / (2 * h)
    ev = np.linalg.eigvals(J)
    ev = ev[np.argsort(-ev.real)]
    print("eta %.3f plateau Q=%.6f C=%.6f R=%.6f |rhs|=%.1e eg=%.6f" % (eta, sp[0], sp[1], sp[2], np.abs(sym_rhs(sp, eta)).max(), eg(z)))
    print("   eigenvalues:", " ".join("%.6g%+.2gi" % (x.real, x.imag) for x in ev))
    # escape time from a transverse seed of size N^-1/2 ~ (1/2 lambda) log N
    lam = ev[0].real
    if lam > 0:
        print("   top eigenvalue %.6g -> plateau length ~ log(N)/(2*%.4g) = %.3g * log N (time in units of N steps)" % (lam, lam, 1 / (2 * lam)))
