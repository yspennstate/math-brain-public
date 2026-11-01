from fractions import Fraction
from math import comb


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def padd(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0)] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def pscale(a, c):
    return trim([c * x for x in a])


def pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def p_polys(d, R):
    q = d - 1
    ps = [(Fraction(1),)]
    if R >= 1:
        ps.append((Fraction(0), Fraction(1)))
    for r in range(2, R + 1):
        xp = (Fraction(0),) + ps[r - 1]
        ps.append(padd(pscale(xp, Fraction(d, q)),
                       pscale(ps[r - 2], Fraction(-1, q))))
    return ps


def radial_step_dist(d, k, r):
    q = d - 1
    if r == 0:
        return {k: Fraction(1)}
    M = min(r, k)
    out = {}

    def add(s, p):
        out[s] = out.get(s, Fraction(0)) + p

    add(r + k, Fraction(q, d))
    for j in range(1, M):
        add(r + k - 2 * j, Fraction(q - 1, d * q ** j))
    add(abs(r - k), Fraction(1, d * q ** (M - 1)))
    assert sum(out.values(), Fraction(0)) == 1
    return out


def radial_dist_m(d, k, m):
    dist = {0: Fraction(1)}
    for _ in range(m):
        nxt = {}
        for r, pr in dist.items():
            for s, p in radial_step_dist(d, k, r).items():
                nxt[s] = nxt.get(s, Fraction(0)) + pr * p
        dist = nxt
    return dist


def far_increments(d, k):
    q = d - 1
    out = {k: Fraction(q, d)}
    for j in range(1, k):
        out[k - 2 * j] = Fraction(q - 1, d * q ** j)
    out[-k] = Fraction(1, d * q ** (k - 1))
    assert sum(out.values(), Fraction(0)) == 1
    return out


def speed_formula(d, k):
    q = d - 1
    return (Fraction(k, 1)
            - Fraction(2 * q, d * (q - 1))
            * (1 - Fraction(1, q ** k)))


def check_spherical(d, k, maxm=5):
    ps = p_polys(d, k * maxm)
    lhs = (Fraction(1),)
    for m in range(1, maxm + 1):
        lhs = pmul(lhs, ps[k])
        dist = radial_dist_m(d, k, m)
        rhs = (Fraction(0),)
        for r, a in dist.items():
            rhs = padd(rhs, pscale(ps[r], a))
        assert trim(lhs) == trim(rhs), (d, k, m, lhs, rhs)

    inc = far_increments(d, k)
    v = sum(Fraction(x) * p for x, p in inc.items())
    a = sum(Fraction(x * x) * p for x, p in inc.items())
    assert v == speed_formula(d, k)

    q = d - 1
    num = 2 + (d - 2) * (k + 1)
    den = d
    assert num * num < den * den * q ** k
    D = d * q ** (k - 1)
    assert D - 1 > q ** k
    return v, a, Fraction(num * num, den * den * q ** k), D


def cube_neighbors(x):
    return [x ^ (1 << i) for i in range(3)]


def step_dist_cube(mu):
    out = [Fraction(0)] * 8
    for x, p in enumerate(mu):
        if p:
            for y in cube_neighbors(x):
                out[y] += p / Fraction(3)
    return out


def tv(mu, nu):
    return sum(abs(a - b) for a, b in zip(mu, nu)) / 2


def cube_orbit_tv(mu):
    # Stabilizer of 000 under coordinate permutations: Hamming-weight classes.
    masses = [Fraction(0)] * 4
    for x, p in enumerate(mu):
        masses[x.bit_count()] += p
    stat = [Fraction(comb(3, w), 8) for w in range(4)]
    return tv(masses, stat)


print("EXACT-DISTANCE-k SPHERICAL CHECK")
for d in (3, 4, 6, 8):
    for k in (2, 3, 4):
        v, a, b2, D = check_spherical(d, k, 5)
        print(f"d={d} k={k}: mixture_m<=5 PASS; v={v}; "
              f"E[xi^2]={a}; envelope^2={b2}<1; "
              f"D-1={D-1}>q^k={(d-1)**k}")

v, a, b2, D = check_spherical(6, 3, 5)
inc = far_increments(6, 3)
c2 = v ** 3 / a
print(f"degree-6,k=3 increments={inc}")
print(f"degree-6,k=3 v={v}, second_moment={a}, "
      f"profile_c_squared={c2}, output_degree={D}")

print("STABILIZER-ORBIT QUOTIENT CHECK ON Q3")
mu = [Fraction(0)] * 8
mu[0] = 1
unif = [Fraction(1, 8)] * 8
for s in range(8):
    tf = tv(mu, unif)
    to = cube_orbit_tv(mu)
    assert tf == to
    print(f"Q3 step={s}: TV_full=TV_orbit={tf} PASS")
    mu = step_dist_cube(mu)

print("ALL_EXACT_CHECKS_PASS")
