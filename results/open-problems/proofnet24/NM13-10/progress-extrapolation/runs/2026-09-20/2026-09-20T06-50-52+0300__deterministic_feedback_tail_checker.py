#!/usr/bin/env python3
import math
import sympy as sp
from scipy.integrate import quad

l, t, sigma = sp.symbols("l t sigma", positive=True)
V = sigma**2 * t
D = t + V/2
m = 3*V - D
Q = V - t

completion = sp.simplify(
    (l + D)**2/(2*V) - 3*l
    - ((l - m)**2/(2*V) - 3*Q)
)
assert completion == 0

gamma = sp.symbols("gamma", nonnegative=True)
sig = 1 + gamma
q = sp.expand(sig**2 - 1)
assert sp.simplify(q - (2*gamma + gamma**2)) == 0
assert sp.simplify(3*gamma - q - gamma*(1-gamma)) == 0

third_exp = sp.simplify(-3*(1 + sig**2/2) + sp.Rational(9,2)*sig**2)
assert sp.simplify(third_exp - 3*q) == 0

def I_k(ell, g, k):
    s = 1.0 + g
    vv = s*s
    c = 2.5*vv - 1.0
    def integrand(tt):
        if tt == 0.0:
            return 1.0 if (ell == 0.0 and k == 0) else 0.0
        return tt**k / math.sqrt(1.0 + tt) * math.exp(
            -((ell - c*tt)**2)/(2.0*vv*tt)
        )
    return quad(integrand, 0.0, math.inf, epsabs=1e-10, epsrel=1e-9, limit=300)

grid_g = [0.0, 0.25, 0.5, 1.0]
grid_l = [0.0, 0.25, 1.0, 5.0, 20.0, 100.0]
max_i0 = (0.0, None)
max_i2r = (0.0, None)
for g in grid_g:
    for ell in grid_l:
        i0, _ = I_k(ell, g, 0)
        i2, _ = I_k(ell, g, 2)
        ratio = i2/(1.0 + ell)**2
        print(f"g={g:4.2f} ell={ell:6.2f} I0={i0:.12g} "
              f"I2/(1+ell)^2={ratio:.12g}")
        if i0 > max_i0[0]:
            max_i0 = (i0, (g, ell))
        if ratio > max_i2r[0]:
            max_i2r = (ratio, (g, ell))

print("completion_identity =", completion)
print("q =", q)
print("third_moment_exponent =", sp.expand(third_exp))
print("max_grid_I0 =", max_i0)
print("max_grid_I2_ratio =", max_i2r)
print("CHECK_PASS")
