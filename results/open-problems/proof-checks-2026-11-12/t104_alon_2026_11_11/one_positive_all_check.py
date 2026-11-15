"""Check of one_positive_all.py's construction: build G_r(z; c, j) the same way, evaluate at random integer
points, and compare exactly with T^3 Psi computed from the definition (m = max over all pairs). Also a direct
exact test of Psi >= 0 on random one-positive integer vectors with many levels (n up to 60)."""
import random
from fractions import Fraction
from sympy import ZZ
from sympy.polys.rings import ring


def psiT3(x):
    n = len(x)
    T = sum(v * v for v in x)
    P = sum(v**3 for v in x)
    Q = sum(v**4 for v in x)
    mT = max(x[i] * x[l] for i in range(n) for l in range(i + 1, n))
    return (n - 4) * (2 * Q - T * T) * T - 2 * (n - 3) * P * P + (n - 1) * ((n * n - 6 * n + 6) * T * T + 2 * n * Q) * mT


def build(r, shape):
    names = [f"z{s}" for s in range(1, r + 1)] + [f"g{s}" for s in range(1, r + 1)] + ["j"]
    R, *gens = ring(",".join(names), ZZ)
    z, g, j = gens[:r], gens[r:2 * r], gens[2 * r]
    c = [g[s] + 1 for s in range(r)]
    c[0] = g[0] + 2 if shape == "II" else R(1)
    v = [sum(z[s:], R(0)) for s in range(r)]
    a = sum((c[s] * v[s] for s in range(r)), R(0))
    n = R(1) + sum(c, R(0)) + j
    T = a**2 + sum((c[s] * v[s] ** 2 for s in range(r)), R(0))
    P = a**3 - sum((c[s] * v[s] ** 3 for s in range(r)), R(0))
    Q = a**4 + sum((c[s] * v[s] ** 4 for s in range(r)), R(0))
    mT = v[0] ** 2 if shape == "II" else (v[0] * v[1] if r >= 2 else R(0))
    return (n - 4) * (2 * Q - T**2) * T - 2 * (n - 3) * P**2 + (n - 1) * ((n**2 - 6 * n + 6) * T**2 + 2 * n * Q) * mT


rnd = random.Random(2026)
bad = tot = 0
for r in range(1, 5):
    for shape in ("I", "II"):
        G = build(r, shape)
        for _ in range(40):
            zz = [rnd.randint(1, 5) for _ in range(r)]
            gg = [rnd.randint(0, 3) for _ in range(r)]
            jj = rnd.randint(0, 3)
            cc = [1 + q for q in gg]
            cc[0] = gg[0] + 2 if shape == "II" else 1
            vv = [sum(zz[s:]) for s in range(r)]
            x = [sum(cc[s] * vv[s] for s in range(r))]
            for s in range(r):
                x += [-vv[s]] * cc[s]
            x += [0] * jj
            assert sum(x) == 0
            if len(x) < 3:
                continue
            val = G(*zz, *gg, jj)
            tot += 1
            if val != psiT3(x):
                bad += 1
print(f"construction check: {tot} points, mismatches {bad}")
neg = 0
least = None
for _ in range(20000):
    n = rnd.randint(5, 60)
    y = sorted((rnd.randint(0, rnd.choice([3, 20, 1000])) for _ in range(n - 1)), reverse=True)
    if y[0] == 0:
        continue
    x = [sum(y)] + [-v for v in y]
    val = psiT3(x)
    T = sum(v * v for v in x)
    q = Fraction(val, T**3)
    if val < 0:
        neg += 1
    if least is None or q < least[0]:
        least = (q, n, y[:6])
print(f"direct exact test, 20000 random one-positive integer vectors, n <= 60: negative {neg}; least Psi {float(least[0]):.6g} at n={least[1]} y={least[2]}")
