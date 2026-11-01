# Audit of agent B's per-sample-Hessian vector term (T354 NOTE "Vector case, per-sample Hessians H_i", push d714532b).
# agent A, 20 Oct 2026. Own model, own exact code: n = 6, three coordinates, TWO special samples (s1, s2) and four others,
# so every coordinate's gradient is three-valued, H_s1, H_s2, H_o 3x3 and non-commuting. Exact scalar RR drift of one coordinate
# with values g1, g2, go (random reshuffling, momentum b1, eps), no Taylor step: only the slots (q1, q2) of the two specials in each
# epoch matter (uniform over ordered distinct pairs, independent across epochs). With A_i = (1 - b2)(g_i^2 - go^2):
#   v = go^2 + sum_e [A1 b2^lag1 + A2 b2^lag2] (past only),  m = go + (1 - b1) sum_e [(g1 - go) b1^lag1 + (g2 - go) b1^lag2],
#   1/(sqrt v + eps) = int k(u) e^(-uv) du, k(u) = (pi u)^(-1/2) [1 - eps sqrt(pi u) erfcx(eps sqrt u)],
# epochs factorize given u; far epochs by the cumulants of Y = A1 b2^(-q1) + A2 b2^(-q2) to order 4, summed in closed form.
# The 3-d root by Newton with a difference Jacobian. Argv: beta1 beta2 eps [h].
import sys, math, itertools, numpy as np
from scipy.special import erfcx
b1, b2, eps = (float(a) for a in sys.argv[1:4]); hstep_t = float(sys.argv[4]) if len(sys.argv) > 4 else 0.02
n = 6; d = 1 - b2
pairs = np.array([pq for pq in itertools.permutations(range(n), 2)], dtype=float); Q1, Q2 = pairs[:, 0], pairs[:, 1]
def drift(g1, g2, go):
    A1, A2 = d * (g1 * g1 - go * go), d * (g2 * g2 - go * go); c1, c2 = (1 - b1) * (g1 - go), (1 - b1) * (g2 - go)
    vmin = min(g1 * g1, g2 * g2, go * go)
    t = np.arange(-45.0, math.log(50.0 / vmin) + hstep_t / 2, hstep_t); u = np.exp(t)
    k = (np.pi * u) ** -0.5 * (1 - eps * np.sqrt(np.pi * u) * erfcx(eps * np.sqrt(u))); wt = hstep_t * u * k
    Y = A1 * b2 ** (-Q1) + A2 * b2 ** (-Q2); spread = np.abs(Y).max()
    mo = [np.mean(Y ** j) for j in range(1, 5)]
    kap = [mo[0], mo[1] - mo[0] ** 2, mo[2] - 3 * mo[1] * mo[0] + 2 * mo[0] ** 3,
           mo[3] - 4 * mo[2] * mo[0] - 3 * mo[1] ** 2 + 12 * mo[1] * mo[0] ** 2 - 6 * mo[0] ** 4]
    tot = 0.0
    for p in range(n):
        logF = np.zeros_like(u); GF = np.zeros_like(u); e = 0
        while True:
            if e > 0:
                base = b2 ** (p + e * n); mw = b1 ** (p + e * n - (n - 1)) if b1 > 0 else 0.0
                if mw < 1e-17 and u.max() * base * spread <= 1e-3: break
            l1, l2 = p + e * n - Q1, p + e * n - Q2
            p1, p2 = (l1 >= 0), (l2 >= 0)
            w = np.where(p1, A1 * b2 ** np.maximum(l1, 0), 0.0) + np.where(p2, A2 * b2 ** np.maximum(l2, 0), 0.0)
            mm = np.where(p1, c1 * b1 ** np.maximum(l1, 0), 0.0) + np.where(p2, c2 * b1 ** np.maximum(l2, 0), 0.0)
            E = np.exp(-np.outer(u, w)); Fm = E.mean(1)
            logF += np.log(Fm); GF += (E @ mm / len(w)) / Fm
            e += 1
        for j in range(1, 5):
            geo = b2 ** ((p + e * n) * j) / (1 - b2 ** (j * n))
            logF += (-1) ** j * kap[j - 1] * u ** j * geo / math.factorial(j)
        tot += wt @ (np.exp(-u * go * go + logF) * (go + GF))
    return tot / n
if __name__ == "__main__" and len(sys.argv) > 5 and sys.argv[5] == "selftest":
    # one special: g2 = go reduces to the single-special case; compare with rr_exact_mom_eps.py (n 10) is not possible at n 6,
    # so check instead D at a two-valued point against the iid-free single-special formula computed by setting A2 = 0 both ways.
    print(drift(9.5, -0.5, -0.5), drift(-0.5, 9.5, -0.5)); sys.exit()
# ---------------- the model and the candidate's prediction ----------------
sys.path.insert(0, "../agent_B"); from kfactor import K_rr
B = np.array([[5.0, 1.0, -1.5], [-6.0, 2.0, 1.0], [6.0, -2.0, -1.0]])      # rows: coordinate j; columns: s1, s2, other
wts = np.array([1, 1, 4]) / n
assert np.allclose(B @ wts, 0)
H1 = np.array([[2.0, 0.5, 0.3], [0.5, 1.0, -0.4], [0.3, -0.4, 1.5]])
H2 = np.array([[0.7, -0.6, 0.0], [-0.6, 2.5, 0.5], [0.0, 0.5, 0.8]])
Ho = np.array([[1.2, 0.2, -0.3], [0.2, 1.0, 0.1], [-0.3, 0.1, 1.3]])
Hs = [H1, H2, Ho]; Hbar = sum(wts[i] * Hs[i] for i in range(3))
B2 = (B ** 2) @ wts; B3 = (B ** 3) @ wts; T = (B * (B ** 2 - B2[:, None]) ** 2) @ wts; mj = B3 / B2
P = np.arange(n); hP = 1 - 3 * P / (n - 1) + 2 * P * (P - 1) / ((n - 1) * (n - 2)); Hb = np.mean((1 - b1 ** (P + 1)) * hP)
K = K_rr(n, b1, b2); s = np.sqrt(B2); r = s / (s + eps); p2 = s * (eps + 3 * s) / (4 * (eps + s) ** 2)
EbH = sum(wts[i] * B[:, i][:, None] * Hs[i] for i in range(3)); Eb2H = sum(wts[i] * (B[:, i] ** 2)[:, None] * Hs[i] for i in range(3))
M = (3 * Eb2H - Hbar * B2[:, None]) / B2[:, None] - 2 * (B3 / B2 ** 2)[:, None] * EbH
R = eps * EbH / (s * (s + eps) ** 2)[:, None]
rhs = d * K / 2 * r * mj - p2 / 2 * d * d * T * Hb / B2 ** 2
pred = np.linalg.solve(Hbar - d * K / 2 * (r[:, None] * M + mj[:, None] * R), rhs)
predR0 = np.linalg.solve(Hbar - d * K / 2 * (r[:, None] * M), rhs)                 # control: r1 dropped
x0 = np.linalg.solve(Hbar, d * K / 2 * r * mj)
def F(x):
    g = [Hs[i] @ x + B[:, i] for i in range(3)]
    return np.array([drift(g[0][j], g[1][j], g[2][j]) for j in range(3)])
x = pred.copy(); f = F(x); J = np.zeros((3, 3)); hs = 1e-3 * np.abs(x0).max()
for kk in range(3):
    ev = np.zeros(3); ev[kk] = hs; J[:, kk] = (F(x + ev) - f) / hs
for it in range(10):
    dx = np.linalg.solve(J, -f); x = x + dx; f = F(x)
    if np.abs(dx).max() < 1e-13 * np.abs(x0).max(): break
G = (x - pred) / (x0 * d * d); GR = (x - predR0) / (x0 * d * d)
print("beta1 %s beta2 %s eps %g K %.6f | x0 %s | x* %s | G %s | no-r1 %s | resid %.1e it %d"
      % (b1, b2, eps, K, np.array2string(x0, precision=6), np.array2string(x, precision=11),
         np.array2string(G, precision=3), np.array2string(GR, precision=2), np.abs(f).max(), it + 1), flush=True)
