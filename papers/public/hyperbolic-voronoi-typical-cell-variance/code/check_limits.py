"""Check of the two limits used in the proof that lam V_2(lam) -> infinity (d = 2).

Upper half-plane, o = i, the nearest nucleus xi = i e^r on the ray towards infinity, with lam |B(o, r)| = s. For w in
the upper half-plane, B_w = B(w, d(w, xi)) and B_o = B(o, r). The claims are
    lam |B_w|        -> s / v,
    lam |B_w n B_o|  -> s I(w) / M,   M = pi/2,  I(w) = m(A_w n A_o) (closed form as in the paper).
The second is computed here directly: a point of B_o in polar coordinates (theta, rho) about o, with lam |B(o, rho)| =
u uniform on (0, s), theta uniform; lam |B_w n B_o| = s P(d(w, y) < d(w, xi))."""
import math
import numpy as np

def dist(z1, z2):
    return np.arccosh(1 + np.abs(z1 - z2) ** 2 / (2 * z1.imag * z2.imag))

def rot(z, th):                       # rotation by angle th about i
    c, s_ = math.cos(th / 2), math.sin(th / 2)
    return (z * c + s_) / (-z * s_ + c)

def I_closed(u, v):
    u = abs(u) if abs(u) > 1e-12 else 1e-12
    xs = (u * u + v * v - 1) / (2 * u)
    return 0.5 * ((math.atan((xs - u) / v) + math.pi / 2) / v + (math.pi / 2 - math.atan(xs)))

rng = np.random.default_rng(7)
lam, n = 1e-6, 200_000
for (u, v, s) in [(0.0, 0.5, 1.0), (1.0, 1.0, 0.7), (3.0, 0.4, 2.0), (-10.0, 2.0, 1.0), (40.0, 1.0, 1.5)]:
    w = complex(u, v)
    r = math.acosh(1 + s / (2 * math.pi * lam))
    xi = complex(0, math.exp(r))
    dwx = dist(np.array([w]), np.array([xi]))[0]
    ballw = lam * 2 * math.pi * (math.cosh(dwx) - 1)
    U = rng.uniform(0, s, n); TH = rng.uniform(0, 2 * math.pi, n)
    rho = np.arccosh(1 + U / (2 * math.pi * lam))
    y = np.array([rot(complex(0, math.exp(p)), t) for p, t in zip(rho, TH)])
    frac = (dist(np.full(y.shape, w), y) < dwx).mean()
    se = math.sqrt(frac * (1 - frac) / len(y))
    print(f'w=({u},{v}) s={s}: lam|B_w| {ballw:.5f} vs s/v {s / v:.5f};  lam|B_w n B_o| {s * frac:.4f} +- {s * se:.4f} '
          f'vs s I/M {s * I_closed(u, v) / (math.pi / 2):.4f}')
