from fractions import Fraction as F

# Exact finite arithmetic checks for the PROB10-06 two-point offspring argument.
# No floating-point assertion is used.

def poly(x):
    # P(lambda) whose unique zero in (1,2) is the d=2 threshold.
    return -5*x**3 + 104*x**2 - 490*x + 576

def pprime(x):
    return -15*x**2 + 208*x - 490

lam = F(9,5)
Q = (F(2)-lam)*(F(2)-lam/F(2))
V = F(3)-lam/F(3)
a = F(1,Q) - F(1,V)
Fmargin = F(2,1)/lam - a/F(4,1)

assert Q == F(11,50)
assert V == F(12,5)
assert a == F(545,132)
assert Fmargin == F(125,1584) and Fmargin > 0

# Robust uniform derivative lower bound on 1 <= lambda <= 9/5:
# Q >= 11/50, 1/V >= 3/8, lambda/2 <= 9/10,
# (3+lambda)^2 <= (24/5)^2.
a_upper = F(50,11) - F(3,8)
numerator_lower = F(4,1) - F(9,10)*a_upper
derivative_lower = numerator_lower / (F(24,5)**2)
assert numerator_lower == F(217,880)
assert derivative_lower == F(1085,101376) and derivative_lower > 0

# The known all-offspring m1=2 endpoint is 4-2*sqrt(2), and it is < 9/5.
# This follows exactly from sqrt(2)>11/10, i.e. 2>121/100.
assert F(2,1) > F(121,100)

# Root isolation for theta_2: P is strictly decreasing on [1,2]
# because P''=-30 lambda+208 >0 there and P'(2)=-134<0.
assert pprime(F(2,1)) == -134
assert -30*F(2,1)+208 > 0
assert poly(F(1811,1000)) == F(622069,200000000) > 0
assert poly(F(1812,1000)) == F(-497877,3125000) < 0

# Explicit expected contraction on p<=1/4, lambda<=9/5.
# Degree-2 Lipschitz cap 9/10, degree-3 cap 60/49.
rho = F(3,4)*F(9,10) + F(1,4)*F(60,49)
assert rho == F(1923,1960) and rho < 1

print('PASS')
print('Q(9/5)=', Q)
print('V(9/5)=', V)
print('a(9/5)=', a)
print('criterion_margin_F(9/5)=', Fmargin)
print('uniform_-ell_prime_lower_on_[1,9/5]=', derivative_lower)
print('theta_2_exact_bracket=[1811/1000,1812/1000]')
print('P(1811/1000)=', poly(F(1811,1000)))
print('P(1812/1000)=', poly(F(1812,1000)))
print('truncation_rho_cap=', rho)
print('derivative_truncation_bound: E|U_n-U| <= 5*rho^n + 21*n*rho^(n-1)')
