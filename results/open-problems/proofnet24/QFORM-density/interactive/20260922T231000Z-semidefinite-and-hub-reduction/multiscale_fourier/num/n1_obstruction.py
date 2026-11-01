try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
# Obstruction N3: Q = 2 X_h L + sigma L^2 + lam V^2, (L,V) Gaussian limit N(0, s2 I) of spread uniform sums.
# For each t0, the adversarial hub density f_h (<= 1, mass <= 1) maximises |phi(t0)|.
# Claim: max |phi(t0)| ~ c sigma^{1/2} / t0 for t0 >> 1/sigma, so t0^{3/2} |phi(t0)| is unbounded.
import numpy as np
s2 = 1.0/12.0
def Psi(t, y, sigma, lam):
    z1 = 1 - 2j*t*sigma*s2
    z2 = 1 - 2j*t*lam*s2
    return z1**-0.5 * np.exp(-y**2*s2/(2*z1)) * z2**-0.5
def adversarial(t0, sigma, lam, xmax, N=400001):
    x = np.linspace(-xmax, xmax, N); dx = x[1]-x[0]
    P = Psi(t0, 2*t0*x, sigma, lam)
    best = 0.0; fbest = None
    for ph in np.linspace(0, 2*np.pi, 73)[:-1]:
        r = np.real(np.exp(-1j*ph)*P)
        f = (r > 0).astype(float)
        mass = f.sum()*dx
        if mass > 1:   # keep the part of the set with largest |P| until mass 1
            idx = np.argsort(-np.abs(P)*f); keep = idx[:int(1.0/dx)]
            f = np.zeros_like(f); f[keep] = 1.0
        val = abs((f*P).sum()*dx)
        if val > best: best, fbest = val, f
    return best, x, fbest
for sigma in [0.05, 0.1]:
    lam = 1.0
    print(f"sigma={sigma}  (1/sigma={1/sigma:.0f})", flush=True)
    for t0 in [10, 40, 160, 640, 2560]:
        xmax = 8*sigma*np.sqrt(1+ (2*t0*sigma*s2)**2)/max(1.0, 2*t0*sigma*s2) + 8/(t0*np.sqrt(s2))
        b, x, f = adversarial(t0, sigma, lam, xmax)
        # uniform hub law on [-1/2,1/2] for comparison
        xu = np.linspace(-0.5, 0.5, 400001); du = xu[1]-xu[0]
        u = abs(Psi(t0, 2*t0*xu, sigma, lam).sum()*du)
        print(f"  t0={t0:5d}  adv|phi|={b:.3e}  t0*adv={t0*b:.4f}  t0^1.5*adv={t0**1.5*b:.3f}   "
              f"uniform-hub |phi|={u:.3e} t0^1.5*unif={t0**1.5*u:.3f}  sqrt(sigma)*..={np.sqrt(sigma):.3f}", flush=True)
