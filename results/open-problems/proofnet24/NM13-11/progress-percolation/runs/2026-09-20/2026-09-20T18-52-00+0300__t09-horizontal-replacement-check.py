from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 50

p_c_test = Fraction(3,40)
s = 1-p_c_test
# Radius-three open cluster in an 8-regular tree.
# h_r is the PGF at x=s of a rooted 7-forward branch of depth r.
h = s
for _ in range(2):
    h = s*(s+p_c_test*h)**7
C3 = s*(s+p_c_test*h)**8
m3 = 7*(1-C3)
assert m3 > Fraction(251,250)  # in particular >1, with a rational margin

# Operator / nonbacktracking certificate for the degree-20 replacement graph.
# ||A|| <= 4 sqrt(7)+4 < 175/12 because sqrt(7)<127/48.
assert Fraction(127,48)**2 > 7
A_upper = Fraction(175,12)
z = Fraction(250,19)
Q = 19
root_margin = z + Fraction(Q,1)/z - A_upper
assert z*z > Q
assert root_margin > 0
assert root_margin == Fraction(529,28500)

p_u_floor = Fraction(19,250)
gap = p_u_floor - p_c_test
assert gap == Fraction(1,1000)

# Decimal display only; all assertions above are exact Fraction arithmetic.
def dec(fr):
    return Decimal(fr.numerator)/Decimal(fr.denominator)

print('p_c_test =', p_c_test, '=', dec(p_c_test))
print('m3 =', dec(m3))
print('m3-1 =', dec(m3-1))
print('m3 > 251/250 =', m3 > Fraction(251,250))
print('sqrt7 rational bound check:', Fraction(127,48)**2, '> 7')
print('A_upper =', A_upper, '=', dec(A_upper))
print('z =', z, '=', dec(z))
print('z^2-Q =', z*z-Q, '=', dec(z*z-Q))
print('root_margin =', root_margin, '=', dec(root_margin))
print('p_u_floor =', p_u_floor, '=', dec(p_u_floor))
print('certified gap lower bound =', gap, '=', dec(gap))
print('ALL_EXACT_CHECKS_PASS')
