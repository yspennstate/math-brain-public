"""Black-box check of STRAT11's corner-ball claim: feasible S with 0<||S-S0||_max<=1/20800 has T6 >= ||S-S0||_max/120.
T6 uses the invariant formula in STRAT11 RESULT.md; first it is checked against my own slice T=-(a-1)(79a+9)/80."""
import numpy as np
rng = np.random.default_rng(20261113)
u0 = np.array([-4, 1, 1, 1, 1]) / np.sqrt(20); w0 = np.array([0, 1, -1, -1, 1]) / 2.0
S0 = np.outer(u0, u0) + np.outer(w0, w0)
iu = np.triu_indices(5, 1)

def T6(S):
    ev, V = np.linalg.eigh(S); B = V[:, -2:]; Q = B @ B.T
    tau = np.trace(S); q = np.diag(Q); M = q @ np.diag(S); S2 = S @ S
    br = 100 * tau * M - 320 * np.sum(np.diag(S) ** 2) - 1280 * q @ np.diag(S2) + 448 * np.trace(S2) - 33 * tau ** 2
    return 9 / 80 + (11 * M - 2 * tau) / 8 + br / 320 + np.sum(Q * S ** 2) + 2 * q @ S @ np.diag(S)

for a in (0.9, 0.97, 0.999):
    S = a * S0; print("slice a=%.3f  T6=%.12f  mine=%.12f" % (a, T6(S), -(a - 1) * (79 * a + 9) / 80))

# pressure family U=(-4,1+s,1+s,1-s,1-s), W0, r=1, a=(5+s^2)/(5+10s-s^2)
for s in (1e-3, 1e-4):
    U = np.array([-4, 1 + s, 1 + s, 1 - s, 1 - s]); W = np.array([0, 1, -1, -1, 1.0])
    a = (5 + s * s) / (5 + 10 * s - s * s); S = a * np.outer(U, U) / (U @ U) + a * np.outer(W, W) / (W @ W)
    lam = (2 + np.trace(S)) / 4; om = lam / 5 + S[iu]
    e = np.abs(S - S0).max(); print("pressure s=%g  min w=%.2e  T6=%.3e  eps=%.3e  T6/eps=%.4f" % (s, om.min(), T6(S), e, T6(S) / e))

def orth_zero_sum(P):
    # project to zero-sum, Gram-Schmidt two columns
    P = P - P.mean(axis=0); u = P[:, 0] / np.linalg.norm(P[:, 0]); w = P[:, 1] - (u @ P[:, 1]) * u
    return u, w / np.linalg.norm(w)

X = np.array([0, 1, 1, -1, -1]) / 2.0; Y = np.array([0, 1, -1, 1, -1]) / 2.0
n_feas = 0; worst = np.inf; worst_pt = None; n = 0
for scale in (1e-4, 3e-5, 1e-5, 3e-6):
    for _ in range(200000):
        n += 1
        c = rng.standard_normal(6) * scale
        U = u0 + c[0] * X + c[1] * Y + c[2] * w0; W = w0 + c[3] * X + c[4] * Y - c[2] * u0
        u, w = orth_zero_sum(np.stack([U, W], 1))
        al = abs(rng.standard_normal()) * scale * rng.choice([0.3, 1, 3]); be = rng.uniform(0, 2 * al)
        a = 1 - al; r = 1 - be
        S = a * np.outer(u, u) + a * r * np.outer(w, w)
        e = np.abs(S - S0).max()
        if e == 0 or e > 1 / 20800: continue
        lam = (2 + np.trace(S)) / 4
        if (lam / 5 + S[iu]).min() < 0 or not (a < lam): continue
        n_feas += 1; t = T6(S); ratio = t / e
        if ratio < worst: worst, worst_pt = ratio, (scale, al, be, c.copy())
print("samples %d feasible-in-ball %d  min T6/eps = %.5f  (claim >= 1/120 = %.5f)" % (n, n_feas, worst, 1 / 120))
print("worst point", worst_pt)
print("VERDICT", "PASS" if n_feas > 1000 and worst >= 1 / 120 else "CHECK")
