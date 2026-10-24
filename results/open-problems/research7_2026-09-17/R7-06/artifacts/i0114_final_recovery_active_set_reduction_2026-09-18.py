import sympy as s
x,y,a=s.symbols('x y a', real=True, positive=True)
T2=lambda z:2*z**2-1
T3=lambda z:4*z**3-3*z
T4=lambda z:8*z**4-8*z**2+1
T5=lambda z:16*z**5-20*z**3+5*z
alpha=s.expand((-1+2*y*(x+y))/3)
beta=s.expand((-1+2*x*(x-3*y+4*y**3))/3)
gamma=s.expand((2*T2(x)*T2(y)+T4(y))/3)
delta=s.expand((T3(x)*y+x*T5(y)+T2(x)*T4(y))/3)
KC=s.expand(s.Rational(1,2)+2*alpha+beta+gamma)
KD=s.expand(s.Rational(1,4)+s.Rational(1,2)*alpha+s.Rational(1,2)*beta+delta)
KC_fac=s.factor(KC)
assert s.expand(KC - (2*y-1)*(2*y+1)*(4*x**2+4*x*y+4*y**2-3)/6)==0
b=T3(y)
KC_b=s.factor(KC.subs(x,b))
KD_b=s.factor(KD.subs(x,b))
KC_b_expected=(2*y-1)**3*(2*y+1)**3*(4*y**2-3)/6
KD_b_expected=(2*y-1)**2*(2*y+1)**2*(128*y**6-224*y**4+104*y**2-5)/12
assert s.expand(KC_b-KC_b_expected)==0
assert s.expand(KD_b-KD_b_expected)==0
# exact Poisson weight ratios from orbit norms/cardinalities recorded in prior exact orbit normalization
norm2_gamma=s.Rational(16,3); card_gamma=6
norm2_delta=s.Rational(28,3); card_delta=12
norm2_eta=s.Integer(12); card_eta=6
C_ratio=s.Rational(card_gamma,card_eta)*s.exp(s.pi**2*(norm2_eta-norm2_gamma)/a)-8
D_ratio=s.Rational(card_delta,card_eta)*s.exp(s.pi**2*(norm2_eta-norm2_delta)/a)-6
assert s.simplify(C_ratio-(s.exp(20*s.pi**2/(3*a))-8))==0
assert s.simplify(D_ratio-(2*s.exp(8*s.pi**2/(3*a))-6))==0
aD=8*s.pi**2/(3*s.log(3))
aC=20*s.pi**2/(3*s.log(8))
assert s.simplify(D_ratio.subs(a,aD))==0
assert s.simplify(C_ratio.subs(a,aC))==0
assert s.simplify(C_ratio.subs(a,aD)-(9*s.sqrt(3)-8))==0
assert 64 < 243
# aD<aC follows 8/log3 <20/log8 <=> 64<243
print('EXACT_SYMBOLIC_CHECK_PASS')
print('K_C =', KC_fac)
print('K_C_on_slanted =', KC_b)
print('K_D_on_slanted =', KD_b)
print('C_ratio =', C_ratio)
print('D_ratio =', D_ratio)
print('a_D =', aD)
print('a_D_decimal =', s.N(aD,18))
print('a_C =', aC)
print('a_C_decimal =', s.N(aC,18))
print('C_ratio_at_a_D =', s.simplify(C_ratio.subs(a,aD)))
print('a_D_lt_a_C_integer_check = 64 < 243 =', 64<243)
