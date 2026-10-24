#!/usr/bin/env python3
import sympy as sp

k, j = sp.symbols("k j", integer=True, positive=True)

# k=m-1 pre-tail cells; theorem assumes k>=2.
A = (8*k + 1)/(k - 1)
B = -18*k/(k**2 - 1)
a = sp.simplify(A + B*j)

sum_a = sp.factor(sp.summation(a, (j, 1, k)))
sum_wa = sp.factor(sp.summation((2*j - 1)*a, (j, 1, k)))
a1 = sp.factor(a.subs(j, 1))
ak = sp.factor(a.subs(j, k))

assert sp.simplify(sum_a + k) == 0
assert sp.simplify(sum_wa + 4*k**2) == 0
assert sp.simplify(a1 - (8*k-1)/(k+1)) == 0
assert sp.simplify(ak + (10*k+1)/(k+1)) == 0

# Exact positive margins for every integer k>=2.
a1_below_8 = sp.factor(8 - a1)
ak_above_minus10 = sp.factor(ak + 10)
h_pre_pos_plus = sp.factor(2 + ak/sp.Integer(10))
h_pre_pos_minus = sp.factor(2 - a1/sp.Integer(10))
tail_pos = sp.Rational(9,20)
last_tail_margin_plus = sp.factor(
    sp.Rational(3,2) + (ak - sp.Rational(1,2))/sp.Integer(10)
)

assert sp.simplify(a1_below_8 - 9/(k+1)) == 0
assert sp.simplify(ak_above_minus10 - 9/(k+1)) == 0
assert sp.simplify(h_pre_pos_plus - (10*k+19)/(10*(k+1))) == 0
assert sp.simplify(h_pre_pos_minus - (12*k+21)/(10*(k+1))) == 0
assert sp.simplify(last_tail_margin_plus - 9*(k+3)/(20*(k+1))) == 0

# Ordering: B<0, so a_j-a_{j+1}=-B>0 for all k>=2.
adjacent_coeff_gap = sp.factor(-B)
assert sp.simplify(adjacent_coeff_gap - 18*k/((k-1)*(k+1))) == 0

# Normalization and mean identities in t are reduced to the two sums above.
# Equal cell length 1/(3k), cell first moment (2j-1)/(18k^2).
t = sp.symbols("t", real=True)
tail_h = (1+t)/2
mass = sp.simplify(
    (1/(3*k))*sp.summation(2 + a*t, (j,1,k))
    + sp.Rational(2,3)*tail_h
)
mean = sp.simplify(
    sp.summation((2*j-1)/(18*k**2) * (2 + a*t), (j,1,k))
    + sp.Rational(4,9)*tail_h
)
assert sp.simplify(mass - 1) == 0
assert sp.simplify(mean - sp.Rational(1,3)) == 0

print("P20 D0010 all-m-piece boundary family symbolic exact core: PASS")
print("assumption: integer k>=2, m=k+1, |t|<=1/10, c=(1+t)/3")
print("sum_j a_j =", sum_a)
print("sum_j (2j-1)a_j =", sum_wa)
print("a_1 =", a1)
print("a_k =", ak)
print("adjacent coefficient gap =", adjacent_coeff_gap, "> 0")
print("8-a_1 =", a1_below_8, "> 0")
print("a_k+10 =", ak_above_minus10, "> 0")
print("pre-tail positivity margin for t>=0 =", h_pre_pos_plus, "> 0")
print("pre-tail positivity margin for t<=0 =", h_pre_pos_minus, "> 0")
print("tail positivity margin =", tail_pos, "> 0")
print("last-pre-tail minus tail margin at t=1/10 =", last_tail_margin_plus, "> 0")
print("normalization =", mass)
print("mean =", mean)
print("ALL_SYMBOLIC_EXACT_CHECKS_PASS")
