from fractions import Fraction
from decimal import Decimal, getcontext
from hashlib import sha256


def dec(q, digits=24):
    getcontext().prec = digits + 8
    return Decimal(q.numerator) / Decimal(q.denominator)

# k=9: depth-two C-fibre / vertical-tree Galton--Watson certificate.
p = Fraction(109, 2000)
s = 1 - p
h0 = s
h1 = s * (s + p*h0)**17
C2 = s * (s + p*h1)**18
m2 = 7 * (1 - C2)
assert m2 > 1
# m2>1 iff C2<6/7, so this cross-multiplied integer is an exact sign certificate.
cross = 6*C2.denominator - 7*C2.numerator
assert cross > 0
print("k9_pc_p =", p, "m2 =", dec(m2))
print("k9_pc_supercritical =", m2 > 1)
print("k9_pc_cross_positive =", cross > 0,
      "digits =", len(str(cross)),
      "sha256 =", sha256(str(cross).encode()).hexdigest())

# Rational square-root upper bounds used in the nonbacktracking root tests.
for n, q in [(11, Fraction(199,60)),
             (7, Fraction(127,48)),
             (17, Fraction(33,8)),
             (19, Fraction(109,25))]:
    assert q*q > n
    print("sqrt_upper", n, "<", q, "square_margin =", q*q-n)

# k=9 uniqueness-side certificate: beta_38(a)<200/11, hence p_u>11/200.
z9 = Fraction(200,11)
Q9 = 37
ub9 = 2*Fraction(199,60) + 2*Fraction(127,48) + 2*Fraction(33,8)
assert z9*z9 > Q9
margin9 = z9 + Fraction(Q9,1)/z9 - ub9
assert margin9 == Fraction(23,550) > 0
gap9 = Fraction(11,200) - p
assert gap9 == Fraction(1,2000)
print("k9_pu_root_margin =", margin9)
print("k9_gap =", gap9)

# k=10 explicit rational endpoint inside the all-k>=10 theorem.
z10 = Fraction(5000,269)
Q10 = 39
ub10 = 2*Fraction(199,60) + 2*Fraction(127,48) + 2*Fraction(109,25)
assert z10*z10 > Q10
margin10 = z10 + Fraction(Q10,1)/z10 - ub10
assert margin10 == Fraction(27277,672500) > 0
gap10 = Fraction(269,5000) - Fraction(1,19)
assert gap10 == Fraction(111,95000)
print("k10_pu_root_margin =", margin10)
print("k10_gap =", gap10)

# General k>=10 positivity. Put x=2k-1>=19 and Q=x+20.
# f(x)=x+1+20/x-2*sqrt(x)-2*sqrt(11)-2*sqrt(7).
# At x=19, sqrt(11)<10/3, sqrt(7)<8/3, sqrt(19)<22/5,
# so f(19)>400/19-104/5=24/95.
# For x>=19, f'(x)=1-20/x^2-1/sqrt(x)>1-20/361-1/4=1003/1444.
base_margin = Fraction(400,19) - Fraction(104,5)
derivative_lower = Fraction(1) - Fraction(20,361) - Fraction(1,4)
assert base_margin == Fraction(24,95) > 0
assert derivative_lower == Fraction(1003,1444) > 0
print("general_base_margin_x19 =", base_margin)
print("general_derivative_lower_x>=19 =", derivative_lower)

print("ALL_EXACT_CHECKS_PASS")
