from fractions import Fraction
from collections import defaultdict

# Exact Gaussian-rational Laurent-polynomial self-check for P75.
# Gaussian rational numbers are pairs (real, imag) of Fractions.

def cadd(a, b): return (a[0] + b[0], a[1] + b[1])
def cmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def cconj(a): return (a[0], -a[1])

ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))
I = (Fraction(0), Fraction(1))

def crat(q): return (Fraction(q), Fraction(0))

def padd(p, q):
    r = defaultdict(lambda: ZERO)
    for k, v in p.items():
        r[k] = cadd(r[k], v)
    for k, v in q.items():
        r[k] = cadd(r[k], v)
    return {k: v for k, v in r.items() if v != ZERO}

def pscale(p, c):
    return {k: cmul(v, c) for k, v in p.items() if cmul(v, c) != ZERO}

def pmul(p, q):
    r = defaultdict(lambda: ZERO)
    for a, ca in p.items():
        for b, cb in q.items():
            r[a + b] = cadd(r[a + b], cmul(ca, cb))
    return {k: v for k, v in r.items() if v != ZERO}

def pstar(p):
    return {-k: cconj(v) for k, v in p.items()}

def ppow(p, n):
    r = {0: ONE}
    for _ in range(n):
        r = pmul(r, p)
    return r

def fmtc(c):
    a, b = c
    if b == 0: return str(a)
    if a == 0: return f"{b}*i"
    return f"({a}+{b}*i)"

def fmtp(p):
    return " + ".join(f"{fmtc(p[k])} z^{k}" for k in sorted(p)) or "0"

one = {0: ONE}
z = {1: ONE}
zinv = {-1: ONE}
H = padd(z, zinv)

# Move 16: the first two finite Taylor truncations of exp(iH) are not exact unitaries.
P1 = padd(one, pscale(H, I))
H2 = ppow(H, 2)
P2 = padd(padd(one, pscale(H, I)), pscale(H2, crat(Fraction(-1, 2))))

lhs1 = pmul(pstar(P1), P1)
rhs1 = padd(one, H2)
assert lhs1 == rhs1
assert lhs1 != one

H4 = ppow(H, 4)
lhs2 = pmul(pstar(P2), P2)
rhs2 = padd(one, pscale(H4, crat(Fraction(1, 4))))
assert lhs2 == rhs2
assert lhs2 != one

# Coordinate bookkeeping for V = exp(iH) u_{s1^4 s2^-3}.
coord = (4, -3)
assert coord == (4, -3)

print("P75 exact self-check")
print("H =", fmtp(H))
print("P1* P1 =", fmtp(lhs1))
print("1 + H^2 =", fmtp(rhs1))
print("P1 is not unitary: PASS")
print("P2* P2 =", fmtp(lhs2))
print("1 + H^4/4 =", fmtp(rhs2))
print("P2 is not unitary: PASS")
print("explicit smooth-class coordinate =", coord)
print("ALL ASSERTIONS PASSED")
