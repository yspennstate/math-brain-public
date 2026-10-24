from fractions import Fraction
import sympy as sp

k, j, c = sp.symbols('k j c', integer=True, positive=True)
A = (8*k + 1)/(k - 1)
B = -18*k/(k**2 - 1)
a = sp.simplify(A + B*j)

sum_a = sp.simplify(sp.summation(a, (j, 1, k)))
sum_w = sp.simplify(sp.summation((2*j - 1)*a, (j, 1, k)))
a1 = sp.simplify(a.subs(j, 1))
ak = sp.simplify(a.subs(j, k))
gap = sp.simplify(a.subs(j, j) - a.subs(j, j+1))
pos_tplus = sp.simplify(2 + ak/sp.Integer(10))
pos_tminus = sp.simplify(2 - a1/sp.Integer(10))
last_tail_margin = sp.simplify(sp.Rational(3,2) + (ak-sp.Rational(1,2))/10)

assert sp.simplify(sum_a + k) == 0
assert sp.simplify(sum_w + 4*k**2) == 0
assert sp.simplify(a1 - (8*k-1)/(k+1)) == 0
assert sp.simplify(ak + (10*k+1)/(k+1)) == 0
assert sp.simplify(gap - 18*k/(k**2-1)) == 0
assert sp.simplify(pos_tplus - (10*k+19)/(10*(k+1))) == 0
assert sp.simplify(pos_tminus - 3*(4*k+7)/(10*(k+1))) == 0
assert sp.simplify(last_tail_margin - 9*(k+3)/(20*(k+1))) == 0

# Exact specialization k=2 (m=3) equals the previously audited three-piece family.
t = 3*c - 1
h1 = sp.simplify(2 + a.subs({k:2,j:1})*t)
h2 = sp.simplify(2 + a.subs({k:2,j:2})*t)
h3 = sp.simplify((1+t)/2)
assert sp.simplify(h1 - (15*c-3)) == 0
assert sp.simplify(h2 - (9-21*c)) == 0
assert sp.simplify(h3 - sp.Rational(3,2)*c) == 0

print('P26 exact audit of P20 D0010 all-m symbolic core')
print('sum_j a_j =', sum_a)
print('sum_j (2j-1)a_j =', sum_w)
print('a_1 =', a1)
print('a_k =', ak)
print('adjacent coefficient gap =', gap)
print('minimum pre-tail height for t>=0 =', pos_tplus)
print('minimum pre-tail height for t<=0 =', pos_tminus)
print('minimum last-pre-tail minus tail height =', last_tail_margin)
print('k=2 specialization =', h1, ';', h2, ';', h3)
print('P26-D0010-ALLM-EXACT-CHECK: PASS')
