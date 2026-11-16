"""LO05: the explicit claims of Section 5 of "Hilbert's tenth problem over the rational numbers" (OpenAI, 6 Oct 2026).
E: y^2 = x^3 - d^2 x over F = Q(sqrt 2), d = 75 - 53 sqrt 2. Exact arithmetic; elements a + b sqrt 2 as pairs."""
from fractions import Fraction as Fr
from math import gcd, sqrt

def say(*a):
    print(*a, flush=True)

class Z2:
    __slots__ = ("a", "b")
    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)
    def __add__(s, o): o = lift(o); return Z2(s.a + o.a, s.b + o.b)
    def __sub__(s, o): o = lift(o); return Z2(s.a - o.a, s.b - o.b)
    def __neg__(s): return Z2(-s.a, -s.b)
    def __mul__(s, o): o = lift(o); return Z2(s.a * o.a + 2 * s.b * o.b, s.a * o.b + s.b * o.a)
    def __eq__(s, o): o = lift(o); return s.a == o.a and s.b == o.b
    def norm(s): return s.a * s.a - 2 * s.b * s.b
    def conj(s): return Z2(s.a, -s.b)
    def inv(s): n = s.norm(); return Z2(s.a / n, -s.b / n)
    def __truediv__(s, o): return s * lift(o).inv()
    def real(s, sign=1): return float(s.a) + sign * float(s.b) * sqrt(2)
    def __repr__(s): return f"({s.a}) + ({s.b}) sqrt2"
def lift(o): return o if isinstance(o, Z2) else Z2(o, 0)
def power(x, n):
    r = Z2(1)
    for _ in range(n): r = r * x
    return r

ok_all = True
def check(name, cond, extra=""):
    global ok_all
    ok_all = ok_all and bool(cond)
    say(f"  {'ok  ' if cond else 'FAIL'} {name}{(': ' + extra) if extra else ''}")

d = Z2(75, -53)
eps = Z2(1, 1)
say("A. The fixed data")
check("norm of d is 7", d.norm() == 7, f"norm {d.norm()}")
check("d is positive at both real embeddings", d.real(1) > 0 and d.real(-1) > 0, f"{d.real(1):.6f}, {d.real(-1):.4f}")
w = Z2(-5, 4)
check("w = -5 + 4 sqrt2 equals d (1 + sqrt2)^3", w == d * power(eps, 3))
check("w^3 - w = -8 d", power(w, 3) - w == d * (-8))
x, y = -(d * w), Z2(0, 2) * d * d
check("Q = (-d w, 2 sqrt2 d^2) lies on y^2 = x^3 - d^2 x", y * y == power(x, 3) - d * d * x)
check("x(Q) has opposite signs at the two embeddings", x.real(1) * x.real(-1) < 0, f"{x.real(1):.5f}, {x.real(-1):.2f}")
check("x(Q) = -(1 + sqrt2) times a square (class outside 1, -1, d, -d)", x == -(eps * power(d * eps, 2)))
check("-4 is not a square modulo 7", all((u * u + 4) % 7 for u in range(7)), f"squares mod 7: {sorted(set(u*u % 7 for u in range(7)))}")
check("1 + sqrt2 has norm -1 (a totally positive unit is an even power, hence a square)", eps.norm() == -1)

say()
say("B. Torsion of E(F): point counts at split primes (torsion injects into the reduction at a good prime)")
def count(p, dd):
    a = (-dd * dd) % p
    sq = [0] * p
    for t in range(p): sq[t * t % p] += 1
    return 1 + sum(sq[(xx * xx * xx + a * xx) % p] for xx in range(p))
g = 0
rows = []
for p in (17, 23, 31, 41, 47, 71, 73, 79, 89, 97, 103, 113):
    roots = [r for r in range(p) if (r * r - 2) % p == 0]
    for r in roots:
        dd = (75 - 53 * r) % p
        if dd == 0: continue
        n = count(p, dd)
        g = gcd(g, n)
        rows.append((p, r, n))
say("  (p, sqrt2 mod p, #E):", " ".join(f"({p},{r},{n})" for p, r, n in rows[:12]), "...")
check("gcd of the point counts is 4, so the torsion of E(F) is the 2-torsion", g == 4, f"gcd {g} over {len(rows)} reductions")
check("y(Q) is not 0, so Q is not 2-torsion and has infinite order", not (y == 0))

say()
say("C. Doubling Q (independent of the paper): 2Q on the curve, and its x a square in F")
lam = (x * x * 3 - d * d) / (y * 2)
x2 = lam * lam - x * 2
y2 = lam * (x - x2) - y
check("2Q lies on the curve", y2 * y2 == power(x2, 3) - d * d * x2)
s = (x * x + d * d) / (y * 2)
check("x(2Q) = ((x^2 + d^2) / 2y)^2", x2 == s * s, f"x(2Q) = {x2}")

say()
say("D. Inequality (5.2): t - 1 - v_p(t) >= K for every t > K when p > K + 1")
def vp(t, p):
    k = 0
    while t % p == 0: t //= p; k += 1
    return k
primes = [p for p in range(2, 400) if all(p % q for q in range(2, int(p ** 0.5) + 1))]
bad = 0; n = 0
for K in range(1, 41):
    for p in primes:
        if p <= K + 1: continue
        for t in range(K + 1, 6000):
            n += 1
            if t - 1 - vp(t, p) < K: bad += 1
check("(5.2) for K <= 40, p < 400, t < 6000", bad == 0, f"{n} cases, {bad} failures")

say()
say("E. Index formula (5.1): with im alpha of order 8 and im alpha' trivial, 8 * 1 = 4 * 2^rank gives rank", (8 // 4).bit_length() - 1)
say()
say("F. Section 4.1: the Shimura curve of discriminant 210 = 2*3*5*7 at maximal level")
def kron4(p): return 0 if p == 2 else (1 if p % 4 == 1 else -1)
def kron3(p): return 0 if p == 3 else (1 if p % 3 == 1 else -1)
ps = (2, 3, 5, 7)
phi = 1
for p in ps: phi *= p - 1
e2 = 1; e3 = 1
for p in ps:
    e2 *= 1 - kron4(p); e3 *= 1 - kron3(p)
genus = Fr(1) + Fr(phi, 12) - Fr(e2, 4) - Fr(e3, 3)
check("no elliptic points of order 2 or 3 (the uniformizing group acts freely)", e2 == 0 and e3 == 0, f"e2 {e2}, e3 {e3}")
check("genus 5", genus == 5, f"1 + {phi}/12 = {genus}")
# quotient by the Atkin-Lehner group (Z/2)^4 of order 16: 2g - 2 = 16 (2 g' - 2) + 8 b, b points of index two
b = Fr(2 * 5 - 2 - 16 * (0 - 2), 8)
check("a genus-0 quotient by the 16 Atkin-Lehner involutions has exactly five branch points of index two", b == 5, f"b = {b}")

say()
say(f"SUMMARY: all checks pass {ok_all}")
