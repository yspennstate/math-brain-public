# T354 vector case with per-sample Hessians H_i, random reshuffling, any beta1, eps >= 0 (agent B, 20 Oct 2026). Candidate.
# g_i(x) = H_i x + b_i in R^2, coordinatewise Adam, E b = 0. Coordinate j's moments m_j, v_j are built from g_{.j} alone, so at
# frozen x its drift is the SCALAR drift evaluated at the values g_{ij}(x). Model: n = 10, one special sample s (H_s, b_s) and nine
# others (H_o, b_o), so every coordinate is two-valued and audit_A/rr_exact_mom_eps.py gives the exact scalar drift
# D(g_s, g_o). The exact root solves D(g_s1(x), g_o1(x)) = D(g_s2(x), g_o2(x)) = 0 (chord Newton, Jacobian by differences).
# Prediction, per coordinate j (s_j = sqrt(B2_j), r_j = s_j/(s_j + eps), p2_j = s_j(eps + 3 s_j)/(4(eps + s_j)^2)):
#   (Hbar x)_j - (d K/2) [r_j m_j + (r_j (M x)_j + m_j (R x)_j)] + (p2_j/2) d^2 T_j Hb/B2_j^2 = 0,
#   m_j = B3_j/B2_j,
#   M_jk = (3 E[b_j^2 H_jk] - Hbar_jk B2_j)/B2_j - 2 B3_j E[b_j H_jk]/B2_j^2     (the matrix form of c1),
#   R_jk = eps E[b_j H_jk]/(s_j (s_j + eps)^2)                                     (the matrix form of r1),
# a linear system. Control "noM": M = R = 0 (only Hbar), i.e. the coupling through H_i dropped.
# Printed per coordinate: G_j = (x*_j - pred_j)/(x0_j d^2), x0 = (d K/2) Hbar^{-1} (r m). Flat in d <=> the O(d^2) part of x* is right.
import sys, numpy as np
sys.path.insert(0, ".")
from kfactor import K_rr
src = open("../audit_A/rr_exact_mom_eps.py", encoding="utf-8").read().split("import os")[0]
old = "def D(x):\n    gs, go = 9 + x, -1 + x; "
assert old in src
src = src.replace(old, "def D(gs, go):\n    ")
n = 10; P = np.arange(n)
h = 1 - 3 * P / (n - 1) + 2 * P * (P - 1) / ((n - 1) * (n - 2))
bs = np.array([9.0, -4.5]); bo = -bs / 9
w = np.array([0.1, 0.9])                                   # sample weights: special, others
def mom(f): return w[0] * f(bs, 0) + w[1] * f(bo, 1)
B2 = mom(lambda b, i: b * b); B3 = mom(lambda b, i: b ** 3)
T = mom(lambda b, i: b * (b * b - B2) ** 2)
MODELS = {"A": (np.array([[3.0, 1.0], [1.0, 2.0]]), np.array([[1.0, 0.3], [0.3, 1.5]])),
          "B": (np.array([[0.5, -0.8], [-0.8, 3.0]]), np.array([[1.5, 0.2], [0.2, 0.8]]))}
which, b1, b2, EPS = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
Hs, Ho = MODELS[which]; Hl = [Hs, Ho]; Hbar = w[0] * Hs + w[1] * Ho
d = 1 - b2; K = K_rr(n, b1, b2); Hb = np.mean((1 - b1 ** (P + 1)) * h)
sq = np.sqrt(B2); r = sq / (sq + EPS); p2 = sq * (EPS + 3 * sq) / (4 * (EPS + sq) ** 2); m = B3 / B2
Eb2H = sum(w[i] * (np.array([bs, bo][i]) ** 2)[:, None] * Hl[i] for i in range(2))
EbH = sum(w[i] * np.array([bs, bo][i])[:, None] * Hl[i] for i in range(2))
M = (3 * Eb2H - Hbar * B2[:, None]) / B2[:, None] - 2 * (B3 / B2 ** 2)[:, None] * EbH
R = EPS * EbH / (sq * (sq + EPS) ** 2)[:, None]
rhs = d * K / 2 * r * m - p2 / 2 * d * d * T * Hb / B2 ** 2
pred = np.linalg.solve(Hbar - d * K / 2 * (r[:, None] * M + m[:, None] * R), rhs)
pred0 = np.linalg.solve(Hbar, rhs)
x0 = np.linalg.solve(Hbar, d * K / 2 * r * m)
sys.argv = ["x", str(b1), str(b2), str(EPS)]; ns = {}
exec(compile(src, "rr_exact", "exec"), ns); Dsc = ns["D"]
def F(x):
    gs = Hs @ x + bs; go = Ho @ x + bo
    return np.array([Dsc(gs[j], go[j]) for j in range(2)])
x = pred.copy(); f = F(x); J = np.zeros((2, 2)); hstep = 1e-3 * np.abs(x0).max()
for k in range(2):
    e = np.zeros(2); e[k] = hstep; J[:, k] = (F(x + e) - f) / hstep
for it in range(8):
    dx = np.linalg.solve(J, -f); x = x + dx; f = F(x)
    if np.abs(dx).max() < 1e-13 * np.abs(x0).max(): break
G = (x - pred) / (x0 * d * d); G0 = (x - pred0) / (x0 * d * d)
print("model %s beta1 %s beta2 %s eps %g K %.6f | x0 %s exact x* %s | G = (x*-pred)/(x0 d^2) %s | noM %s | resid %.1e it %d"
      % (which, b1, b2, EPS, K, np.array2string(x0, precision=6), np.array2string(x, precision=10),
         np.array2string(G, precision=3), np.array2string(G0, precision=1), np.abs(f).max(), it + 1), flush=True)
