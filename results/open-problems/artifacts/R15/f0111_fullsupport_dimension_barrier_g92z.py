import sympy as sp

d,z,s,t,r = sp.symbols('d z s t r', real=True)

k = 2*z*(1-z**2)/((1-d**2)*(d+3*z))
x = ((d+z)*(1+z)*(1+d+2*z))/(2*(1+d)*(d+3*z))
y = ((d+z)*(1-z)*(1-d-2*z))/(2*(1-d)*(d+3*z))
K2 = (d+z)*(1-z**2)/(d+3*z)
tJ = (1-z)**2 - K2
tK = (1+z)**2 - K2
R = -2*(d+z)*(1-z**2)*(d**2*z + 3*d*z**2 + d + 3*z**3)/(d+3*z)**2
QJ = sp.factor(-k*(1 + 3*tJ**2/R))
QK = sp.factor(-k*(1 + 3*tK**2/R))

QJ_expected = -2*z*(z - 1)*(d**2*z**2 + d**2*z + 7*d*z**3 - 5*d*z**2 + d*z + d + 9*z**4 - 15*z**3 + 10*z**2 - 2*z)/((d - 1)*(d + 1)*(d + z)*(d**2*z + 3*d*z**2 + d + 3*z**3))
QK_expected = -2*z*(z + 1)*(d**2*z**2 - d**2*z + 7*d*z**3 + 5*d*z**2 + d*z - d + 9*z**4 + 15*z**3 + 10*z**2 + 2*z)/((d - 1)*(d + 1)*(d + z)*(d**2*z + 3*d*z**2 + d + 3*z**3))
assert sp.cancel(QJ-QJ_expected) == 0
assert sp.cancel(QK-QK_expected) == 0
print('QJ,QK simplifications: PASS')

# z>1 branch: z=1+s.
expr_plus = sp.factor(sp.together(QK.subs(z,1+s) - sp.Rational(256,9)))
num_plus, den_plus = map(sp.factor, sp.fraction(expr_plus))
# Normalize as num=-2 Pplus, den=9(d-1)(d+1)(d+s+1)Tplus
Pplus = sp.factor(-num_plus/2)
Tplus = d**2*s+d**2+3*d*s**2+6*d*s+4*d+3*s**3+9*s**2+9*s+3
assert sp.expand(den_plus - 9*(d-1)*(d+1)*(d+s+1)*Tplus) == 0
Pplus_poly = sp.Poly(sp.expand(Pplus),s)
coeffs_plus = [sp.factor(Pplus_poly.coeff_monomial(s**j)) for j in range(7)]
expected_plus = [
    8*(d+3)*(2*d-1)**2*(4*d**2+12*d+11),
    2*(64*d**5+512*d**4+1152*d**3+265*d**2-766*d+645),
    512*d**4+2304*d**3+1837*d**2-864*d+2763,
    12*(64*d**3+131*d**2+29*d+271),
    3*(131*d**2+141*d+712),
    9*(7*d+78),
    sp.Integer(81),
]
for got,want in zip(coeffs_plus,expected_plus):
    assert sp.expand(got-want)==0
# The only non-obvious coefficients c1,c2 become coefficientwise positive after d=t/(1+t).
def cleared_coeffs(poly, deg):
    q = sp.expand((1+t)**deg * poly.subs(d,t/(1+t)))
    q = sp.Poly(sp.cancel(q),t)
    return [sp.Integer(q.coeff_monomial(t**j)) for j in range(deg+1)]
assert cleared_coeffs(expected_plus[1],5) == [1290,4918,7302,7602,7544,3744]
assert cleared_coeffs(expected_plus[2],4) == [2763,10188,15823,14438,6552]
print('z>1 positive-polynomial decomposition: PASS')

lim_plus = sp.factor(sp.limit(QK.subs(z,1+s),s,0,dir='+'))
assert sp.cancel(lim_plus - 48/((1-d)*(1+d)**3)) == 0
boundary_plus = sp.factor(lim_plus - sp.Rational(256,9))
expected_boundary_plus = -16*(2*d-1)**2*(4*d**2+12*d+11)/(9*(d-1)*(d+1)**3)
assert sp.cancel(boundary_plus-expected_boundary_plus)==0
print('z>1 boundary minimum 256/9 at d=1/2: PASS')

# z<-1 branch: z=-1-s.
expr_minus = sp.factor(sp.together(QJ.subs(z,-1-s) - 48))
num_minus, den_minus = map(sp.factor, sp.fraction(expr_minus))
Pminus = sp.factor(-num_minus/2)
Tminus = d**2*s+d**2-3*d*s**2-6*d*s-4*d+3*s**3+9*s**2+9*s+3
assert sp.expand(den_minus - (d-1)*(d+1)*(1+s-d)*Tminus) == 0
# Denominator sign: Tminus>0 on 0<=d<1,s>0 after d=1-r.
Tminus_r = sp.expand(Tminus.subs(d,1-r))
Tminus_r_expected = r**2*s+r**2+3*r*s**2+4*r*s+2*r+3*s**3+6*s**2+4*s
assert sp.expand(Tminus_r-Tminus_r_expected)==0
Pminus_poly = sp.Poly(sp.expand(Pminus),s)
# Check positivity of every s-coefficient after d=t/(1+t).
expected_transformed = {
    0:[0,144,528,576,264,48],
    1:[26,486,1782,2258,1176,216],
    2:[131,796,1943,1590,408],
    3:[244,752,1064,412],
    4:[208,369,234],
    5:[78,71],
    6:[9],
}
for j,expected in expected_transformed.items():
    cj = Pminus_poly.coeff_monomial(s**j)
    deg = len(expected)-1
    got = cleared_coeffs(cj,deg)
    assert got == expected, (j,got,expected)
print('z<-1 positive-polynomial decomposition: PASS')

lim_minus = sp.factor(sp.limit(QJ.subs(z,-1-s),s,0,dir='+'))
assert sp.cancel(lim_minus - 48/((1+d)*(1-d)**3)) == 0
boundary_minus = sp.factor(lim_minus-48)
expected_boundary_minus = -48*d*(d**3-2*d**2+2)/((d-1)**3*(d+1))
assert sp.cancel(boundary_minus-expected_boundary_minus)==0
print('z<-1 boundary minimum 48 at d=0: PASS')

# Dimension consequences are exact arithmetic.
n_min_plus = sp.floor(sp.Rational(256,9)) + 2  # n-1>256/9
n_min_minus = sp.Integer(48) + 2                 # n-1>48
assert n_min_plus == 30
assert n_min_minus == 50
print('integer dimension consequences n>=30 and n>=50: PASS')
print('ALL_EXACT_SYMBOLIC_CHECKS_PASS')
