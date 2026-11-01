import sympy as sp
from fractions import Fraction

# Exact parameters.
s3=sp.sqrt(3)
s5=sp.sqrt(5)
q=sp.Rational(2,1)/s3
h=sp.Rational(4,1)/(1+s3+s5)
g0=sp.Rational(1,1)/(s3+s5-2)
U=sp.Rational(384566,484385)
c=sp.cancel((q+sp.Rational(1,2)*h*(q-1))/(q+1))
gstar=sp.sqrt(c)
F=lambda z: sp.cancel((z+c)/(z+1))

# Symbolic dual-multiplier identity.
g,Q,H=sp.symbols('g Q H')
beta=(Q-1)/(2*(Q+1))
gamma=(1-H*(Q-1)/2)/((g+1)*(Q+1))
C=(Q+H*(Q-1)/2)/(Q+1)
r=(g+C)/(g+1)

coef_a=sp.cancel((1+Q)/(1+Q))
coef_b=sp.cancel((1-Q)/(2*(1+Q)) + beta + gamma)
coef_d=sp.cancel(-2*Q/(1+Q) + 2*beta + gamma)
coef_i=sp.cancel(-Q/(1+Q) - H*beta - g*gamma)

assert sp.cancel(coef_a-1)==0
assert sp.cancel(coef_b-(1-r))==0
assert sp.cancel(coef_d+r)==0
assert sp.cancel(coef_i+r)==0
assert sp.cancel((r-g) - (C-g*g)/(g+1))==0

# Exact rational bracketing of q and h, using only integer-square comparisons.
# sqrt(3) < 40/23 because 3*23^2 < 40^2; hence q=2/sqrt(3)>23/20.
assert 3*23*23 < 40*40
# sqrt(3) > 50/29 because 3*29^2 > 50^2; hence q<29/25.
assert 3*29*29 > 50*50
qL,qU=Fraction(23,20),Fraction(29,25)

# sqrt(3)<7/4 and sqrt(5)<9/4 imply sqrt(3)+sqrt(5)<4, so h>4/5.
assert 3*16 < 49 and 5*16 < 81
# sqrt(3)+sqrt(5)>3 implies h<1; e.g. sqrt(3)>17/10 and sqrt(5)>22/10.
assert 3*100 > 17*17 and 5*100 > 22*22 and Fraction(17+22,10)>3
hL,hU=Fraction(4,5),Fraction(1,1)

# c(q,h) is increasing in q,h for q>1,h>0.
cL=(qL+hL*(qL-1)/2)/(qL+1)
cU=(qU+hU*(qU-1)/2)/(qU+1)
assert cL==Fraction(121,215)
assert cU==Fraction(31,54)
assert cL>Fraction(9,16)       # so g_* > 3/4
assert cU<Fraction(361,625)    # so g_* < 19/25

# Seed lies strictly between 1/2 and 51/100.
# Lower: sqrt3+sqrt5<4 gives g0>1/2.
# Upper: sqrt3>1732/1000 and sqrt5>2236/1000, so sum-2>1.968>100/51.
assert 3*1000*1000 > 1732*1732
assert 5*1000*1000 > 2236*2236
assert Fraction(1732+2236,1000)-2 > Fraction(100,51)
# Therefore g0<51/100<3/4<gstar.

# Retained exact upper is >79/100, while gstar<19/25=76/100.
assert 384566*100 > 79*484385
assert Fraction(19,25)<Fraction(79,100)

# Fixed point algebra.
assert sp.cancel(F(gstar)-gstar)==0

old_lower=sp.Rational(2,1)/(s3+s5-1)
old_width=U-old_lower
new_width=U-gstar

print('q =', sp.N(q,30))
print('h =', sp.N(h,30))
print('c =', sp.N(c,30))
print('c_exact =', c)
print('c_rational_bracket =', f'{cL.numerator}/{cL.denominator}', '< c <',
      f'{cU.numerator}/{cU.denominator}')
print('g_star =', sp.N(gstar,40))
print('seed_g0 =', sp.N(g0,30))
print('previous_lower =', sp.N(old_lower,30))
print('upper =', f'{U.p}/{U.q}', '=', sp.N(U,30))
print('old_width =', sp.N(old_width,30))
print('new_width =', sp.N(new_width,40))
print('relative_gap_reduction_percent =', sp.N((old_width-new_width)/old_width*100,30))
print('symbolic_coefficients =', coef_a, coef_b, coef_d, coef_i)
print('ALL_EXACT_SYMBOLIC_CHECKS_PASS')
