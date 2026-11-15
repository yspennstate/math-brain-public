"""One positive coordinate, general negatives: x = (a, -b, -t, -y_1..-y_r), b >= t >= y_i >= 0, a = b + t + sum y.
For fixed (b, t, sum y, r) compare G = T^3 Psi at a random y with G at the two extreme arrangements of y in the
majorisation order: all equal, and (t, .., t, tau, 0, .., 0).  Also certify the 'equal' family symbolically.
an agent, 11 Nov 2026."""
import random
import sympy as sp

def G_num(n, a, negs):
    T = a * a + sum(v * v for v in negs)
    P = a**3 - sum(v**3 for v in negs)
    Q = a**4 + sum(v**4 for v in negs)
    s = sorted(negs, reverse=True)
    m = s[0] * s[1]
    return (n - 4) * (2 * Q - T * T) * T - 2 * (n - 3) * P * P + (n - 1) * ((n * n - 6 * n + 6) * T * T + 2 * n * Q) * m, T

rnd = random.Random(5)
worse_than_both = 0
below_equal = below_spread = 0
neg = 0
tot = 0
worst = None
for trial in range(200000):
    n = rnd.randint(5, 40)
    r = n - 3
    t = rnd.random() ** rnd.choice([1, 3])
    b = t + rnd.random() ** rnd.choice([1, 3]) * rnd.choice([0.1, 1, 10])
    mode = rnd.randint(0, 3)
    if mode == 0:
        y = [t * rnd.random() for _ in range(r)]
    elif mode == 1:
        y = [t * rnd.random() ** 4 for _ in range(r)]
    elif mode == 2:
        y = [t * (1 - rnd.random() ** 4) for _ in range(r)]
    else:
        vals = [t * rnd.random() for _ in range(rnd.randint(1, 3))]
        y = [rnd.choice(vals + [0.0, t]) for _ in range(r)]
    s = sum(y)
    a = b + t + s
    g, T = G_num(n, a, [b, t] + y)
    ge, _ = G_num(n, a, [b, t] + [s / r] * r)
    kk = int(s // t) if t > 0 else 0
    kk = min(kk, r)
    sp_y = [t] * kk + ([s - kk * t] if kk < r else []) + [0.0] * max(0, r - kk - 1)
    gs, _ = G_num(n, a, [b, t] + sp_y)
    tot += 1
    sc = T**3
    if g < -1e-9 * sc:
        neg += 1
    if g < ge - 1e-9 * sc:
        below_equal += 1
    if g < gs - 1e-9 * sc:
        below_spread += 1
    if g < min(ge, gs) - 1e-9 * sc:
        worse_than_both += 1
        d = (min(ge, gs) - g) / sc
        if worst is None or d > worst[0]:
            worst = (d, n, b, t, [round(v, 4) for v in sorted(y, reverse=True)[:8]], g / sc, ge / sc, gs / sc)
print(f"samples {tot}: Psi<0 {neg}; G below the equal arrangement {below_equal}; below the spread arrangement {below_spread}; below both {worse_than_both}")
print("worst case below both:", worst)

z1, z2, z3, k, kap = sp.symbols("z1 z2 z3 k kap")
u, t_, b_ = z1, z1 + z2, z1 + z2 + z3
a_ = b_ + t_ + k * u
n_ = k + 3
T = a_**2 + b_**2 + t_**2 + k * u**2
P = a_**3 - b_**3 - t_**3 - k * u**3
Q = a_**4 + b_**4 + t_**4 + k * u**4
G = sp.Poly(sp.expand((n_ - 4) * (2 * Q - T**2) * T - 2 * (n_ - 3) * P**2 + (n_ - 1) * ((n_**2 - 6 * n_ + 6) * T**2 + 2 * n_ * Q) * b_ * t_), z1, z2, z3)
bad = []
for mon, c in G.terms():
    cc = sp.Poly(sp.expand(c.subs(k, 2 + kap)), kap)
    if any(v < 0 for v in cc.coeffs()):
        bad.append((mon, sp.factor(c)))
print("equal family x=(a,-b,-t,-u x k), k>=2: monomials", len(G.terms()), "with a negative coefficient:", len(bad))
for m_, f in bad[:8]:
    print("  ", m_, f)
