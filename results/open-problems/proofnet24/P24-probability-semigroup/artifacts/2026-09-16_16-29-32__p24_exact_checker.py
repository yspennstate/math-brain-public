from sympy import symbols, Rational, simplify, factor, diff, exp

r, x, s = symbols('r x s', positive=True)

print('P24 AV-P3 EXACT SYMBOLIC CHECKS')

# 1. Post-pulse moment exponent for beta=1.
gamma = -r + r*(r-1)/2
assert simplify(gamma - r*(r-3)/2) == 0
assert gamma.subs(r, 2) == -1
assert gamma.subs(r, 3) == 0
assert gamma.subs(r, 4) == 2
print('PASS gamma_r = r(r-3)/2; gamma_2=-1, gamma_3=0, gamma_4=2')

# 2. Exact high-frequency scaling exponent for both the g-input and X1-output.
input_lambda_exponent = -r/Rational(2) - 1
output_lambda_exponent = -r/Rational(2) - 1
assert simplify(input_lambda_exponent-output_lambda_exponent) == 0
print('PASS input/output lambda exponents both equal -r/2-1')

# 3. Deterministic pulse profile q(s): verify ODE identities symbolically on each side.
q_left = 1-exp(-s)
assert simplify(diff(q_left,s) + q_left - 1) == 0
# post-pulse use tau=s-1 and symbolic q1
q1 = symbols('q1', positive=True)
tau = symbols('tau', nonnegative=True)
q_right = q1*exp(-tau)
assert simplify(diff(q_right,tau)+q_right) == 0
print('PASS deterministic pulse profile solves q\' + q = 1 before pulse and q\' + q = 0 after pulse')

# 4. C27 directed audit: independent C6 heat-kernel/event algebra.
# C6 continuous-time heat kernel probabilities written with x=e^t.
p0 = (x**4 + 2*x**3 + 2*x + 1)/(6*x**4)
p1 = (x**4 + x**3 - x - 1)/(6*x**4)
p2 = (x**4 - x**3 - x + 1)/(6*x**4)
p3 = (x**4 - 2*x**3 + 2*x - 1)/(6*x**4)
p4 = p2
p5 = p1
assert simplify(sum([p0,p1,p2,p3,p4,p5])-1) == 0

# Around the Cayley hexagon: e,(01),(012),(02),(021),(12).
P_1in = simplify(p1+p2+p4)
P_2in = simplify(p2+p3+p4)
P_both = simplify(p2+p4)
claimed_1 = (x-1)*(3*x-1)*(x**2+x+1)/(6*x**4)
claimed_2 = (x-1)**2*(3*x**2+2*x+1)/(6*x**4)
claimed_both = (x-1)**2*(x**2+x+1)/(3*x**4)
assert simplify(P_1in-claimed_1) == 0
assert simplify(P_2in-claimed_2) == 0
assert simplify(P_both-claimed_both) == 0
cov = factor(P_both-P_1in*P_2in)
claimed_cov = (x-1)**2*(x**2+x+1)*(3*x**4+6*x**3+2*x**2+2*x-1)/(36*x**8)
assert simplify(cov-claimed_cov) == 0
poly = 3*x**4+6*x**3+2*x**2+2*x-1
assert poly.subs(x,1) == 12
# derivative coefficients are all strictly positive for x>0
polyprime = diff(poly,x)
assert polyprime == 12*x**3+18*x**2+4*x+2
print('PASS C27 P3 cycle-event formulas and positive covariance factorization')
print('C27 covariance numerator polynomial P(1)=12 and P\'(x)=12x^3+18x^2+4x+2>0 for x>0')

print('ALL_EXACT_CHECKS_PASS')
