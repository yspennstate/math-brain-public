try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Model where (SQ) holds exactly: R = lam V^2 + C, V = sum of 30 uniforms/sqrt30 on its own coordinates (independent of
# everything else), C = sigma_c t^2 + mu U (U another independent sum), t = L + beta.
# Theorem 3.3 bound:  1 + 9.05 K E|t^2 + a(s - C)|^{-1/4},  K = |lam|^{-1/2} * sup rho_V.
# Theorem 3.4 bound:  1 + K D |sigma_c|^{-1/2}(11.4 + 1.42 log_+|sigma_c| + 1.42 min{2 log_+ alpha_1(C'), log_+(8|sigma_c|/|D_H|)})
# (D = sup density of t given C' = sup rho_L, C' = mu U).  Compare with the true max density (exact estimator).
import numpy as np, time, sys
sys.path.insert(0, '.')
from hublib import *
rng = np.random.default_rng(61)
m = 30; wv = np.ones(m)/np.sqrt(m)
N = 250000
fh = uniform_law()
# sup of the density of a normalized sum of 30 uniforms (var 1/12): ~ N(0,1/12) peak 1.382; use 1.40 as a safe upper value
rho_max = 1.40
t0 = time.time()
def sums(r):
    return r.random((N, m)) @ wv - 0.5*np.sqrt(m)
for (a, sigma_c, lam, mu) in [(0.1, 0.0, -1.0, 0.0), (0.1, 3.0, -1.0, 0.0), (0.2, 4.95, -1.0, 0.0), (0.2, 4.95, -1.0, 0.3), (-0.3, 1.0, 1.0, 0.5)]:
    DH = 1 - a*sigma_c
    def samp(r):
        L = sums(r); V = sums(r); U = sums(r)
        return L, lam*V*V + sigma_c*L*L + mu*U
    sg = np.unique(np.concatenate([np.linspace(-0.6, 0.6, 31), np.linspace(-0.03, 0.03, 7)]))
    d = density_on_grid(a, 0.0, samp, fh, sg, 2, rng); j = int(np.argmax(d)); smax = sg[j]
    # Theorem 3.3 bound at the argmax s (and sup over the grid of the Monte Carlo quarter moment)
    Lp = sums(rng); Up = sums(rng)
    qm = max(np.mean(np.abs(Lp**2 + a*(s - (sigma_c*Lp**2 + mu*Up)))**-0.25) for s in sg)
    K = abs(lam)**-0.5*rho_max
    b33 = 1 + 9.05*K*qm
    # Theorem 3.4 bound
    if sigma_c != 0:
        a1C = np.inf if mu == 0 else 2*np.sqrt(2)*0 + (np.sqrt(2)*rho_max/abs(mu))**0.5*2  # alpha_1 of mu U <= 2 sqrt(D') with D' = rho_max/|mu| (density bound), crude
        term = min(2*np.log(max(a1C, 1.0)) if np.isfinite(a1C) else np.inf, np.log(max(8*abs(sigma_c)/abs(DH), 1.0)))
        b34 = 1 + K*rho_max*abs(sigma_c)**-0.5*(11.4 + 1.42*max(0.0, np.log(abs(sigma_c))) + 1.42*term)
    else:
        b34 = np.inf
    print("a %5.2f sigma_c %5.2f D_H %6.3f lam %4.1f mu %.1f : true max %.3f (s=%.3f) | Thm3.3 bound %.1f | Thm3.4 bound %s  t=%.0fs"
          % (a, sigma_c, DH, lam, mu, d[j], smax, b33, ("%.1f" % b34) if np.isfinite(b34) else "n/a", time.time()-t0), flush=True)
