from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 50

# Exact arithmetic in Q(sqrt(2),sqrt(3)), basis (1,sqrt2,sqrt3,sqrt6).
def add(x, y):
    return tuple(x[i] + y[i] for i in range(4))


def mul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return (
        a * e + 2 * b * f + 3 * c * g + 6 * d * h,
        a * f + b * e + 3 * c * h + 3 * d * g,
        a * g + c * e + 2 * b * h + 2 * d * f,
        a * h + d * e + b * g + c * f,
    )


def scale(q, x):
    return tuple(q * v for v in x)


one = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
s2 = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
s3 = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))
s6 = (Fraction(0), Fraction(0), Fraction(0), Fraction(1))

x = Fraction(1, 4)
prod = x * (1 - x)
assert prod == Fraction(3, 16)

# m=(1+sqrt(3))/4, the exact coordinate-tail coefficient.
m = scale(Fraction(1, 4), add(one, s3))
poly_m = add(add(scale(16, mul(m, m)), scale(-8, m)), scale(-2, one))
assert poly_m == (0, 0, 0, 0)

# Uniform row-sum tail coefficient C_* = 1 + 3 sqrt(2) m.
C = add(one, scale(3, mul(s2, m)))
C_expected = add(one, scale(Fraction(3, 4), add(s2, s6)))
assert C == C_expected

# Concrete p=3/4 subcritical-moment constant B_p=1+p C_*/(1-p)=1+3C_*.
p = Fraction(3, 4)
B = add(one, scale(p / (1 - p), C))
B_expected = add(scale(4, one), scale(Fraction(9, 4), add(s2, s6)))
assert B == B_expected

# Exact coefficient split used in the tail proof.
lhs = add(mul(s2, m), scale(2, mul(s2, m)))
rhs = scale(3, mul(s2, m))
assert lhs == rhs

# Decimal values below are display-only; all assertions above are exact.
D2 = Decimal(2).sqrt()
D3 = Decimal(3).sqrt()
D6 = Decimal(6).sqrt()
m_dec = (Decimal(1) + D3) / Decimal(4)
kappa_dec = (Decimal(3) / Decimal(16)).sqrt().sqrt()
C_dec = Decimal(1) + Decimal(3) * D2 * m_dec
B_dec = Decimal(4) + Decimal(9) / Decimal(4) * (D2 + D6)

print("x =", x)
print("x(1-x) =", prod)
print("kappa^4 =", prod)
print("kappa ~= ", kappa_dec)
print("m exact = (1+sqrt(3))/4")
print("m polynomial 16m^2-8m-2 = 0: PASS")
print("m ~= ", m_dec)
print("C_* exact = 1 + (3/4)(sqrt(2)+sqrt(6))")
print("C_* ~= ", C_dec)
print("p =", p)
print("B_p exact at p=3/4 = 4 + (9/4)(sqrt(2)+sqrt(6))")
print("B_3/4 ~= ", B_dec)
print("large+jump coefficient identity: sqrt(2)m + 2sqrt(2)m = 3sqrt(2)m: PASS")
print("ALL_EXACT_CHECKS_PASS = True")
