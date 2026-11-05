"""T390: the m^-4 coefficient of ratio(m) = ARE / (sqrt(2 pi) e^(-m^2/2)/m), and the remainder check.
ratio = A(eps)^2 / (2 pi B(eps)) * (1 + O(e^(-m^2/2))), eps = 1/m^2, expanded to eps^2 by exact series of the
integrands (dominated convergence: every y^k sech^3 is integrable, so term-by-term expansion is legitimate and the
remainder after eps^2 is O(eps^3))."""
import json
import mpmath as mp
mp.mp.dps = 40
inf = mp.inf
S = lambda f: mp.quad(f, [-inf, 0, inf])
sech, tanh = mp.sech, mp.tanh
K = lambda k, p: S(lambda y: y**k * sech(y)**p)
KT = lambda k: S(lambda y: y**k * tanh(y) * sech(y)**3)
KT2 = lambda k: S(lambda y: y**k * tanh(y)**2 * sech(y)**3)
# A = a0 + a1 e + a2 e^2 ; e^(-e y^2/2) = 1 - e y^2/2 + e^2 y^4/8
a0, a1, a2 = K(0, 3), -K(2, 3) / 2, K(4, 3) / 8
# B integrand: sech^3 (tanh^2 + 2 e y tanh + e^2 y^2)(1 - e y^2/2 + e^2 y^4/8)
b0 = KT2(0)
b1 = 2 * KT(1) - KT2(2) / 2
b2 = K(2, 3) - KT(3) + KT2(4) / 8
r0 = a0**2 / (2 * mp.pi * b0)
c1 = 2 * a1 / a0 - b1 / b0
c2 = (a1 / a0)**2 + 2 * a2 / a0 - 2 * (a1 / a0) * (b1 / b0) - b2 / b0 + (b1 / b0)**2
out = {"r0": str(r0), "first_order_coef": str(c1), "c_claimed": str(4 / mp.mpf(3) + mp.pi**2 / 8),
       "second_order_coef_d": str(c2),
       "identify_d": str(mp.identify(c2, ["pi**2", "pi**4"])),
       "identify_d_z3": str(mp.identify(c2, ["pi**2", "pi**4", "zeta(3)"]))}
from t390_check import ratio
rem = {}
for m in [10, 20, 40, 100, 200]:
    e = mp.mpf(1) / m**2
    r = ratio(m)
    rem[m] = str(mp.nstr((r - 1 - c1 * e - c2 * e**2) / e**3, 8))
out["m6_times_remainder_after_eps2"] = rem
print(json.dumps(out, indent=1))
json.dump(out, open("t390_second_order.json", "w"), indent=1)
