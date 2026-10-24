import sympy as sp

n = sp.symbols("n", integer=True, positive=True)
a = sp.symbols("a", real=True)

# B4: the smallest non-Markov exact-uniform routing cell.
p00 = sp.Rational(1, 3)
p01 = sp.Rational(1, 6)
p10 = sp.Rational(1, 6)
p11 = sp.Rational(1, 3)
q00 = sp.Rational(1, 4)
q01 = a
q10 = 1 - a
q11 = sp.Rational(3, 4)

assert sp.simplify(p00 + p01 + p10 + p11 - 1) == 0
assert sp.simplify(p01*q01 + p10*q10 - sp.Rational(1, 6)) == 0

p_x3_given_x1_0 = sp.simplify((p00*q00 + p01*q01) / sp.Rational(1, 2))
p_x3_given_x1_1 = sp.simplify((p10*q10 + p11*q11) / sp.Rational(1, 2))
p_x3_given_x2_0 = sp.simplify((p00*q00 + p10*q10) / sp.Rational(1, 2))
p_x3_given_x2_1 = sp.simplify((p01*q01 + p11*q11) / sp.Rational(1, 2))

d1 = sp.factor(p_x3_given_x1_1 - p_x3_given_x1_0)
d2 = sp.factor(p_x3_given_x2_1 - p_x3_given_x2_0)
assert sp.simplify(d1 - sp.Rational(2, 3)*(1-a)) == 0
assert sp.simplify(d2 - sp.Rational(2, 3)*a) == 0
assert sp.simplify(d1 + d2 - sp.Rational(2, 3)) == 0
assert sp.solve(sp.Eq(d1, d2), a) == [sp.Rational(1, 2)]

# B13/B28: exact-uniform layer moments.
ESn = sp.Rational(1, 2)*n
ESn2 = n*(2*n + 1)/6
ESn1 = sp.Rational(1, 2)*(n + 1)
ESn12 = (n + 1)*(2*n + 3)/6
EX = sp.simplify(ESn1 - ESn)
assert EX == sp.Rational(1, 2)
ESnX = sp.simplify((ESn12 - ESn2 - EX)/2)
Cov_Sn_X = sp.simplify(ESnX - ESn*EX)
assert sp.simplify(ESnX - n/3) == 0
assert sp.simplify(Cov_Sn_X - n/12) == 0

# For fair Bernoulli pairs the signed conditional contrast equals 4 covariance.
total_contrast = sp.simplify(4*Cov_Sn_X)
assert sp.simplify(total_contrast - n/3) == 0

# Pairwise mutual-information kernel for fair Bernoulli variables with contrast d.
d = sp.symbols("d", real=True)
phi = sp.Rational(1, 2)*(1+d)*sp.log(1+d) + sp.Rational(1, 2)*(1-d)*sp.log(1-d)
phi2 = sp.simplify(sp.diff(phi, d, 2))
assert sp.simplify(phi2 - 1/(1-d**2)) == 0
phi_third = sp.simplify(phi.subs(d, sp.Rational(1, 3)))

print("B4 d1 =", d1)
print("B4 d2 =", d2)
print("B4 d1+d2 =", sp.simplify(d1+d2))
print("B4 minimax intersection a =", sp.Rational(1, 2))
print("E[X_{n+1}] =", EX)
print("E[S_n X_{n+1}] =", ESnX)
print("Cov(S_n,X_{n+1}) =", Cov_Sn_X)
print("sum_i d_i =", total_contrast)
print("phi''(d) =", phi2)
print("phi(1/3) =", phi_third)
print("phi(1/3) numeric =", sp.N(phi_third, 18))
print("ALL_EXACT_CHECKS_PASS")
