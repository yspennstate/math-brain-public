"""Audit of the T354 vector case with per-sample Hessians (agent B NOTE, 20 Oct 06:1x), agent C.
g_i(x) = H_i x + b_i in R^3, coordinatewise Adam, random reshuffling, n = 10: two special samples (H_1, b_1), (H_2, b_2)
and eight others (H_o, b_o). Every coordinate is three-valued, the b vectors are not collinear across coordinates and the
three Hessians do not commute. Coordinate j's exact frozen-x drift is the scalar drift of rr_exact_two_special_a.py at the
values (g_1j, g_2j, g_oj); the exact root solves all three by Newton with a difference Jacobian.
Prediction, built WITHOUT the note's closed-form M and R: per coordinate the drift is
    (Hbar x)_j - (d K/2) phi_j(x) + (p2_j/2) d^2 T_j Hb/B2_j^2 = 0,  phi_j(x) = r_j(x) C_j(x)/V_j(x),
with V_j, C_j the exact frozen moments of the three-valued g_.j and r_j(x) = sqrt(V_j)/(sqrt(V_j) + eps); phi_j is linearised by
central differences at x = 0 (step 1e-6), so the O(x) coefficient comes from the definitions, not from the algebra under test.
The note's M, R are computed too and compared with the difference gradient (columns 'MR vs grad').
usage: python vec3_audit.py HSET BETA1 BETA2 EPS [NODES]"""
import math, sys
import numpy as np
from rr_exact_two_special_a import D, K_rr

n = 10
w = np.array([0.1, 0.1, 0.8])
b1v = np.array([6.0, -3.0, 2.0]); b2v = np.array([2.0, 5.0, -6.0]); bov = -(b1v + b2v) / 8
B = [b1v, b2v, bov]
HSETS = {
    "P": [np.array([[4.0, 1.0, 0.0], [1.0, 2.0, 0.5], [0.0, 0.5, 1.0]]),
          np.array([[0.5, -0.3, 0.2], [-0.3, 3.0, 0.0], [0.2, 0.0, 2.0]]),
          np.array([[1.0, 0.2, -0.1], [0.2, 0.8, 0.3], [-0.1, 0.3, 1.5]])],
    "Q": [np.array([[0.6, -0.9, 0.4], [-0.9, 3.5, -0.7], [0.4, -0.7, 1.2]]),
          np.array([[2.5, 0.6, -0.8], [0.6, 0.4, 0.3], [-0.8, 0.3, 3.0]]),
          np.array([[1.2, -0.25, 0.15], [-0.25, 1.0, -0.35], [0.15, -0.35, 0.9]])],
}
hs, b1, b2, eps = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
Nt = int(sys.argv[5]) if len(sys.argv) > 5 else 160
Hl = HSETS[hs]; Hbar = sum(w[i] * Hl[i] for i in range(3))
d = 1 - b2; K = K_rr(b1, b2)
P = np.arange(n); h = 1 - 3 * P / (n - 1) + 2 * P * (P - 1) / ((n - 1) * (n - 2)); Hb = np.mean((1 - b1 ** (P + 1)) * h)
def mom(f): return sum(w[i] * f(B[i]) for i in range(3))
B2 = mom(lambda b: b * b); B3 = mom(lambda b: b ** 3); T = mom(lambda b: b * (b * b - B2) ** 2)
assert np.abs(mom(lambda b: b)).max() < 1e-12
s = np.sqrt(B2); p2 = s * (eps + 3 * s) / (4 * (eps + s) ** 2)

def phi(x):
    G = [Hl[i] @ x + B[i] for i in range(3)]
    mu = mom(lambda _: 0) + sum(w[i] * G[i] for i in range(3))
    V = sum(w[i] * G[i] ** 2 for i in range(3)); E3 = sum(w[i] * G[i] ** 3 for i in range(3))
    C = E3 - mu * V
    rr = np.sqrt(V) / (np.sqrt(V) + eps)
    return rr * C / V
phi0 = phi(np.zeros(3)); J = np.zeros((3, 3)); st = 1e-6
for k in range(3):
    e = np.zeros(3); e[k] = st; J[:, k] = (phi(e) - phi(-e)) / (2 * st)
# the note's closed form
r = s / (s + eps); m = B3 / B2
Eb2H = sum(w[i] * (B[i] ** 2)[:, None] * Hl[i] for i in range(3)); EbH = sum(w[i] * B[i][:, None] * Hl[i] for i in range(3))
M = (3 * Eb2H - Hbar * B2[:, None]) / B2[:, None] - 2 * (B3 / B2 ** 2)[:, None] * EbH
R = eps * EbH / (s * (s + eps) ** 2)[:, None]
Jnote = r[:, None] * M + m[:, None] * R
qterm = p2 / 2 * d * d * T * Hb / B2 ** 2
pred = np.linalg.solve(Hbar - d * K / 2 * J, d * K / 2 * phi0 - qterm)
noM = np.linalg.solve(Hbar, d * K / 2 * phi0 - qterm)
x0 = np.linalg.solve(Hbar, d * K / 2 * phi0)

def F(x):
    out = np.zeros(3)
    for j in range(3):
        out[j] = D(0.0, b1, b2, [Hl[0][j] @ x + b1v[j], Hl[1][j] @ x + b2v[j], Hl[2][j] @ x + bov[j]], eps, Nt)
    return out
x = pred.copy(); f = F(x); Jx = np.zeros((3, 3)); hstep = 1e-3 * np.abs(x0).max()
for k in range(3):
    e = np.zeros(3); e[k] = hstep; Jx[:, k] = (F(x + e) - f) / hstep
for it in range(10):
    dx = np.linalg.solve(Jx, -f); x = x + dx; f = F(x)
    if np.abs(dx).max() < 1e-14 * np.abs(x0).max(): break
G = (x - pred) / (x0 * d * d); G0 = (x - noM) / (x0 * d * d)
print("VEC3 H %s beta1 %g beta2 %g eps %g nodes %d K %.9f | x0 %s | x* %s | G %s | noM %s | MR vs grad %.1e | resid %.1e it %d"
      % (hs, b1, b2, eps, Nt, K, np.array2string(x0, precision=6), np.array2string(x, precision=12),
         np.array2string(G, precision=4), np.array2string(G0, precision=1), np.abs(J - Jnote).max(), np.abs(f).max(), it + 1),
      flush=True)
