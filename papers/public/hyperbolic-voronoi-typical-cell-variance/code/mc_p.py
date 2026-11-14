"""Monte Carlo check of p(t) = P(o and x have the same nearest nucleus) for a Poisson process of intensity lam in H^2,
x at hyperbolic area-distance t (lam * 2 pi (cosh r - 1) = t). Nuclei are sampled in the disc of radius R around o
with lam * area(B(o, R)) large enough that both nearest nuclei lie inside it except with probability < 1e-12."""
import math, sys
import numpy as np
from var import p_of, gl_pieces
from var3 import geo

def mc(lam, t, reps, seed=0):
    rng = np.random.default_rng(seed)
    r = math.acosh(1 + t / (2 * math.pi * lam))
    Rn = math.acosh(1 + 28 / (2 * math.pi * lam))        # nearest nucleus of x lies within Rn of x w.p. 1 - e^-28
    R = r + Rn
    mu = lam * 2 * math.pi * (math.cosh(R) - 1)
    same = 0
    for _ in range(reps):
        n = rng.poisson(mu)
        u = rng.random(n)
        rho = np.arccosh(1 + u * (math.cosh(R) - 1))
        phi = rng.random(n) * 2 * math.pi
        do = rho
        cd = math.cosh(r) * np.cosh(rho) - math.sinh(r) * np.sinh(rho) * np.cos(phi)
        same += int(np.argmin(do) == np.argmin(cd))
    return same / reps, mu

if __name__ == '__main__':
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    for lam, t in [(1.0, 1.0), (0.01, 0.003), (0.01, 0.3), (0.01, 3.0), (0.01, 30.0), (0.001, 1.0)]:
        est, mu = mc(lam, t, reps)
        se = math.sqrt(max(est * (1 - est), 1e-12) / reps)
        S = gl_pieces(geo(min(1e-4, 1e-4 * lam), 80.0), 18)
        TH = gl_pieces(geo(1e-4 * min(1.0, math.sqrt(lam)), math.pi), 18)
        q = p_of(t, lam, S, TH)
        print(f'lam={lam} t={t}: MC {est:.4f} +- {se:.4f} (mean points {mu:.0f})  quadrature {q:.4f}  e^-t {math.exp(-t):.4f}', flush=True)
