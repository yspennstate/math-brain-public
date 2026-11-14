"""Checks the geometry of var.py against the hyperbolic law of cosines in 60-digit arithmetic. For random triangles o x y
with |x| = r, |y| = a and angle th at o (radii up to 24, angles down to 1e-9), it compares cosh b - 1 and the union area
A(a) + A(b) - lens, with A(u) = 2 pi (cosh u - 1), and prints the largest relative error. Usage: python geometry_check.py"""
import math
import numpy as np
import mpmath as mp
from var import geometry

mp.mp.dps = 60


def exact(a, r, th):
    a, r, th = mp.mpf(a), mp.mpf(r), mp.mpf(th)
    cb = mp.cosh(a) * mp.cosh(r) - mp.sinh(a) * mp.sinh(r) * mp.cos(th)
    b = mp.acosh(cb)
    al = th
    be = mp.acos((mp.cosh(r) * cb - mp.cosh(a)) / (mp.sinh(r) * mp.sinh(b)))
    ga = mp.acos((mp.cosh(a) * cb - mp.cosh(r)) / (mp.sinh(a) * mp.sinh(b)))
    lens = 2 * al * mp.cosh(a) + 2 * be * cb + 2 * ga - 2 * mp.pi
    union = 2 * mp.pi * (mp.cosh(a) - 1) + 2 * mp.pi * (cb - 1) - lens
    return cb - 1, union


rng = np.random.default_rng(20261114)
worst_b = worst_u = 0.0
for k in range(400):
    r = float(rng.uniform(0.001, 24)); a = float(rng.uniform(0.001, 24))
    if k % 4 == 1:
        a = r * (1 + float(rng.uniform(-1e-6, 1e-6)))       # nearly equal radii
    th = float(10 ** rng.uniform(-9, math.log10(math.pi)))
    cbm1, lens = geometry(np.float64(a), np.float64(r), np.float64(th))
    union = 2 * math.pi * (math.cosh(a) - 1) + 2 * math.pi * cbm1 - lens
    e_b, e_u = exact(a, r, th)
    worst_b = max(worst_b, float(abs((cbm1 - e_b) / e_b)))
    worst_u = max(worst_u, float(abs(union - e_u) / max(1.0, abs(e_u))))
print(f'400 triangles: max relative error of cosh b - 1 = {worst_b:.2e}, of the union area = {worst_u:.2e}')
