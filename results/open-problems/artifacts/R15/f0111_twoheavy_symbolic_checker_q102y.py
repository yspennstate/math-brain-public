import sympy as sp

N,y,AK,x,AJ,R2,T,a,b = sp.symbols('N y AK x AJ R2 T a b', positive=True)
LK = AK*y
Tcap = y*(N-LK)

# Exact K-K aggregate residual-Gram capacity simplification.
Vmax = sp.factor(sp.Rational(1,2)*(Tcap-y+AK*y**2))
assert Vmax == y*(N-1)/2
print('Vmax =', Vmax)

# Exact J-J aggregate coefficient mass after summing the residual Gram identity.
# sum_i e_i = x-AJ*R2 and ||sum_J w_i||^2=(b/a)^2*T.
gram_pair = sp.Rational(1,2)*((b/a)**2*T-(x-AJ*R2))
rank_pair = AJ*sp.Rational(1,2)*(x**2-R2)
U_J = sp.factor(gram_pair+rank_pair)
expected = sp.Rational(1,2)*((b/a)**2*T-x+AJ*x**2)
assert sp.factor(U_J-expected) == 0
print('U_J =', U_J)

# Carried exact scalar ranges imply two heavy-cap coordinates have enough total capacity:
# x<41/40, s<3/200, and the stricter heavy cap uses C<=17.
# Therefore 2(1-Cs) > 2(1-17*3/200)=149/100 > 41/40 > x.
margin = sp.Rational(149,100)-sp.Rational(41,40)
assert margin == sp.Rational(93,200) and margin > 0
print('two_cap_margin =', margin)

print('ALL_EXACT_SYMBOLIC_CHECKS_PASS')
