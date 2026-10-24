try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Prop 5.4' check: Q = a X_h^2 + 2(L+beta) X_h + mu L^2 + lam V^2, X_h uniform[-1/2,1/2], (L,V) projections of 60 uniform leaves.
# Conditional density given (L,V): k = sum_{roots x} f(x)/(2 Delta), Delta = sqrt(t^2 + a z), z = s - F, t = L+beta.
import numpy as np
rng = np.random.default_rng(3)
n1 = 60; N = 1_000_000
Qm, _ = np.linalg.qr(rng.normal(size=(n1, 2))); w, v = Qm[:, 0], Qm[:, 1]
Xp = rng.uniform(-0.5, 0.5, (n1, N)); L = w @ Xp; V = v @ Xp
f = lambda x: ((x >= -0.5) & (x < 0.5)).astype(float)
def dens(s, a, beta, mu, lam):
    t = L + beta; z = s - (mu*L**2 + lam*V**2)
    if a == 0:
        return np.mean(f(z/(2*t))/(2*np.abs(t)))
    disc = t**2 + a*z; ok = disc > 0; D = np.sqrt(np.where(ok, disc, 0.0))
    xp = (-t + D)/a; xm = (-t - D)/a
    k = np.where(ok, (f(xp) + f(xm))/(2*np.maximum(D, 1e-300)), 0.0)
    return np.mean(k)
for a in (0.0, 0.01, 0.1, 0.5, -0.3):
    for mu in (0.0, 0.5):
        for beta in (0.0, 0.2):
            vals = [dens(s, a, beta, mu, 1.0) for s in np.linspace(-1.5, 1.5, 61)]
            print(f"a={a:+.2f} mu={mu:.1f} beta={beta:.1f} lam=1: max_s p_Q ~ {max(vals):.3f}   D_H=|1-mu*a|={abs(1-mu*a):.2f}", flush=True)
