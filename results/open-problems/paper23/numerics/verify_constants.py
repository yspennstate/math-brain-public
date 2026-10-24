"""Verify the deterministic constants asserted in the paper."""
import numpy as np
from scipy import optimize, stats, integrate

phi = stats.norm.pdf
Phi = stats.norm.cdf
Phinv = stats.norm.ppf


def kappa(a):
    # E[Z^2 1{|Z|>=t}], P(|Z|>=t)=a  => t = Phi^{-1}(1 - a/2)
    t = Phinv(1 - a / 2)
    return a + 2 * t * phi(t)


def kcheck(a):
    # E[Z^2 1{|Z|<=s}], P(|Z|<=s)=a => s = Phi^{-1}((1+a)/2)
    s = Phinv((1 + a) / 2)
    return a - 2 * s * phi(s)


# quarter-circle top-alpha quantile s*: int_{s*}^2 (1/pi) sqrt(4-x^2) dx = a
def sstar(a):
    def cdf_upper(s):
        val, _ = integrate.quad(lambda x: np.sqrt(4 - x**2) / np.pi, s, 2)
        return val
    return optimize.brentq(lambda s: cdf_upper(s) - a, 0, 2)


H = lambda a: -a*np.log(a) - (1-a)*np.log(1-a)

print(f"kappa(1/2)      = {kappa(0.5):.6f}   (paper: 0.928674)")
print(f"sqrt kappa(1/2) = {np.sqrt(kappa(0.5)):.6f}   (paper: 0.963677)")
print(f"kcheck(1/2)     = {kcheck(0.5):.6f}   (paper: 0.071326)")
print(f"sqrt kcheck(1/2)= {np.sqrt(kcheck(0.5)):.6f}   (paper: 0.267070)")
print(f"kappa+kcheck(1/2) check kappa(1/2)+kcheck(1/2) = {kappa(0.5)+kcheck(0.5):.6f} (=1? complement is kappa(a)+kcheck(1-a)=1)")
print(f"kappa(1/2)+kcheck(1/2) = {kappa(0.5)+kcheck(0.5):.6f}")
# complement identity kappa(a) + kcheck(1-a) = 1
for a in (0.3, 0.5, 0.7):
    print(f"  kappa({a})+kcheck({1-a:.1f}) = {kappa(a)+kcheck(1-a):.6f}  (should be 1)")
astar = optimize.brentq(lambda a: kappa(a) - 0.25, 1e-6, 0.5)
print(f"alpha* (kappa=1/4) = {astar:.6f}   (paper: 0.042672)")
print(f"s*(1/2)         = {sstar(0.5):.6f}   (paper: 0.807946)")
print(f"2H(1/2)={2*H(0.5):.6f}  3H(1/2)={3*H(0.5):.6f}")
# complex kappa_C(a)=a(1-log a), kcheck_C(a)=a+(1-a)log(1-a)
kC = lambda a: a*(1-np.log(a))
kcC = lambda a: a + (1-a)*np.log(1-a)
print(f"kappa_C(1/2)={kC(0.5):.6f}  kcheck_C(1/2)={kcC(0.5):.6f}  sum-complement kC(a)+kcC(1-a):")
for a in (0.3,0.5,0.7):
    print(f"  kC({a})+kcC({1-a:.1f})={kC(a)+kcC(1-a):.6f} (should be 1)")
# fixed-mask contraction threshold (k^k/(k+1)^{k+1})^{1/k}
for k in range(1,6):
    print(f"  fixed-mask alpha*_k, k={k}: {(k**k/(k+1)**(k+1))**(1/k):.5f}")
