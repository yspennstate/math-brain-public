from fractions import Fraction
from math import sqrt

# Exact Taylor multiplication:
# exp(ell*x^2/24) * sinc(sqrt(ell)*x/2)
exp_coeff = [
    Fraction(1),
    Fraction(1,24),
    Fraction(1,1152),
    Fraction(1,82944),
]
sinc_coeff = [
    Fraction(1),
    -Fraction(1,24),
    Fraction(1,1920),
    -Fraction(1,322560),
]
prod = []
for n in range(4):
    prod.append(sum(exp_coeff[k]*sinc_coeff[n-k] for k in range(n+1)))
assert prod == [
    Fraction(1),
    Fraction(0),
    -Fraction(1,2880),
    -Fraction(1,181440),
]

# Exact fully coupled partner orientation u_10.
u = [Fraction(10,51), Fraction(10,51), Fraction(49,51)]
assert sum(x*x for x in u) == 1
c = (Fraction(177) - Fraction(39)*sum(x**4 for x in u))/Fraction(640)
assert c == Fraction(53990741,240540480)

# Equivalent off-diagonal formula for B=I-2uu^T.
offsq = Fraction(0)
for i in range(3):
    for j in range(i+1,3):
        Bij = -2*u[i]*u[j]
        assert Bij != 0
        offsq += Bij*Bij
c2 = Fraction(69,320) + Fraction(39,1280)*offsq
assert c2 == c

# Universal orientation range.
assert Fraction(69,320) < c < Fraction(41,160)

baseline = 3*sqrt(2)
print('PASS QFORM-PARTIAL-HEAVY-QUADRATIC-BARRIER-v1')
print('series=', prod)
print('c_u10=', c, float(c))
print('baseline_3sqrt2=', baseline)
print('predicted ratios:')
for ell in (0.02,0.05,0.10):
    print(ell, 1-float(c)*ell*ell)
