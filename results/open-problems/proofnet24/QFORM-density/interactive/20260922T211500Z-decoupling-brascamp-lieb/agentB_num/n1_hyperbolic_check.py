try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Check the exact hyperbolic change of variables and the log-profile bound
# p(delta) <= D^{-1/2} (5.2 + log_+(32/(Lambda |delta|)))  for W with independent coords, densities <= 1.
import numpy as np
rng = np.random.default_rng(1)

def rot(th):
    c, s = np.cos(th), np.sin(th); return np.array([[c, -s], [s, c]])

def density_via_t(B, w0, f1, f2, delta, T=40.0, N=400001):
    ev, O = np.linalg.eigh(B)          # ev[0] < 0 < ev[1]
    mneg, mpos = ev[0], ev[1]
    eneg, epos = O[:, 0], O[:, 1]
    D = -mneg * mpos
    t = np.linspace(-T, T, N); dt = t[1] - t[0]
    tot = 0.0
    for eps in (1.0, -1.0):
        if delta > 0:
            w = w0[:, None] + eps*np.sqrt(delta/mpos)*np.cosh(t)*epos[:, None] + np.sqrt(delta/(-mneg))*np.sinh(t)*eneg[:, None]
        else:
            w = w0[:, None] + np.sqrt(-delta/mpos)*np.sinh(t)*epos[:, None] + eps*np.sqrt(-delta/(-mneg))*np.cosh(t)*eneg[:, None]
        tot += np.sum(f1(w[0]) * f2(w[1])) * dt
    return tot/(2*np.sqrt(D))

def bound(B, delta):
    ev = np.linalg.eigvalsh(B); D = -ev[0]*ev[1]; Lam = 1/abs(ev[0]) + 1/abs(ev[1])
    return (5.2 + max(0.0, np.log(32/(Lam*abs(delta)))))/np.sqrt(D)

def union_indicator(starts, lens):
    starts = np.asarray(starts); lens = np.asarray(lens)
    def f(x):
        x = np.asarray(x); out = np.zeros_like(x, dtype=float)
        for a, l in zip(starts, lens):
            out[(x >= a) & (x < a + l)] = 1.0
        return out
    return f

# 1) Monte Carlo cross-check of the change-of-variables formula
B = rot(0.7) @ np.diag([2.0, -0.5]) @ rot(0.7).T
f1 = union_indicator([-0.5], [1.0]); f2 = union_indicator([-3.0, 1.7], [0.5, 0.5])
M = 4_000_000
X1 = rng.uniform(-0.5, 0.5, M); X2 = np.where(rng.random(M) < 0.5, rng.uniform(-3, -2.5, M), rng.uniform(1.7, 2.2, M))
w0 = np.array([0.1, -0.2])
Wc = np.stack([X1 - w0[0], X2 - w0[1]])
P = np.einsum('in,ij,jn->n', Wc, B, Wc)
for d in (0.3, -0.8, 2.5):
    h = 0.01
    mc = np.mean(np.abs(P - d) < h)/(2*h)
    ex = density_via_t(B, w0, f1, f2, d)
    print(f"MC check delta={d:5.2f}: MC {mc:.4f}  formula {ex:.4f}  bound {bound(B,d):.3f}")
