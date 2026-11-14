"""In R^2: as the measure a -> 1, compare joint exceedances J = P(X notin A, Y notin A) of the strip |x1| <= t and the
ball |x| <= r of the same Gaussian measure a = 1 - eps in R^2. Stab(A) = 1 - 2 eps + J, so the larger J wins.
Laplace prediction: J_strip / J_ball ~ 2 (r^2/t^2) exp((r^2 - t^2)/(1+rho)) / (r sqrt(2 pi / rho)), which grows like
t^{(1-rho)/(1+rho)}."""
import math
import numpy as np
from scipy import integrate
from scipy.stats import ncx2, norm

def J_strip(t, rho):
    s = math.sqrt(1 - rho * rho)
    f = lambda x: norm.pdf(x) * (norm.sf((t - rho * x) / s) + norm.cdf((-t - rho * x) / s))
    v, _ = integrate.quad(f, t, t + 40, epsabs=0, epsrel=1e-12, limit=400)
    return 2 * v

def J_ball(r, rho):
    s2 = 1 - rho * rho
    f = lambda u: u * math.exp(-u * u / 2) * ncx2.sf(r * r / s2, 2, rho * rho * u * u / s2)
    v, _ = integrate.quad(f, r, r + 40, epsabs=0, epsrel=1e-12, limit=400)
    return v

print('rho  eps      t       r       J_strip      J_ball       ratio    predicted  ratio/pred')
for rho in [0.1, 0.5, 0.9]:
    for eps in [1e-2, 1e-4, 1e-8, 1e-16, 1e-32, 1e-64]:
        t = norm.isf(eps / 2); r = math.sqrt(-2 * math.log(eps))
        js, jb = J_strip(t, rho), J_ball(r, rho)
        pred = 2 * (r * r / (t * t)) * math.exp((r * r - t * t) / (1 + rho)) / (r * math.sqrt(2 * math.pi / rho))
        print(f'{rho:<4} {eps:<8.0e} {t:7.3f} {r:7.3f} {js:12.4e} {jb:12.4e} {js / jb:9.4f} {pred:9.4f} {js / jb / pred:9.4f}')
