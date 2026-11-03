r"""Numerical value of the many-prize limit of the instance family (Section 5 of the paper).

u = remaining time in [0, 1].  W solves dW/du = 1 + sum_j p_j (b_j - W)^+, W(0) = 0 (sure item already seen);
V solves dV/du = 1 + sum_j p_j (b_j - V)^+ + (max(a, W) - V)/u, V(0) = a (sure item still to come).
Limit ratio = V(1) / (1 + E max(a, cloud values)), clouds Poisson(p_j) with values b_j.
These are numerical solutions, not certified bounds.

usage: python continuum.py
"""
import math
from scipy.integrate import solve_ivp


def ratio(a, clouds):
    def rhs(u, y):
        W, V = y
        dW = 1 + sum(p * max(b - W, 0.0) for b, p in clouds)
        dV = 1 + sum(p * max(b - V, 0.0) for b, p in clouds) + (max(a, W) - V) / u
        return [dW, dV]
    u0 = 1e-12
    # near u = 0: W = u (1 + sum p b), V = a + c u with c solving c = 1 + sum p (b - a)^+ - c
    c = (1 + sum(p * max(b - a, 0.0) for b, p in clouds)) / 2
    y0 = [u0 * (1 + sum(p * b for b, p in clouds)), a + c * u0]
    sol = solve_ivp(rhs, (u0, 1.0), y0, method="DOP853", rtol=1e-12, atol=1e-14)
    V1 = sol.y[1, -1]
    vals = sorted(clouds, key=lambda t: -t[0])
    em, surv = 0.0, 1.0
    for b, p in vals:
        if b <= a:
            break
        em += surv * (1 - math.exp(-p)) * b
        surv *= math.exp(-p)
    em += surv * a
    return V1 / (1 + em)


cases = [
    ("no medium items (a = sqrt 3 - 1)", math.sqrt(3) - 1, []),
    ("one value, GMS parameters", 0.789, [(1.24, 0.421)]),
    ("one value, optimised", 0.8204, [(1.3304, 0.3717)]),
    ("two values, parameters of I(k, m)", 0.823, [(1.28233, 0.2065), (1.38487, 0.17698)]),
    ("two values, optimised", 0.82160, [(1.27865, 0.20840), (1.38431, 0.18833)]),
    ("three values, optimised", 0.82178, [(1.26006, 0.14352), (1.33157, 0.13374), (1.40321, 0.12514)]),
]
for name, a, cl in cases:
    print(f"{name:40s} {ratio(a, cl):.8f}")
print(f"{'sqrt 3 - 1':40s} {math.sqrt(3) - 1:.8f}")
