import sympy as sp
from math import comb

# Exact symbolic regression for the multi-flip theorem.
u, v, s, d, x, h = sp.symbols('u v s d x h', positive=True)

P = 12*u**3 + 19*u**2*v + 6*u*v**2 + 3*v**3
P_sd = sp.expand(P.subs({u:(s-d)/2, v:(s+d)/2}))
Qx = sp.Rational(1,2) + sp.Rational(5,2)*x - 5*x**2 + 5*x**3
Qsd = d**3 * Qx.subs(x, s/d)
assert sp.simplify(P_sd - Qsd) == 0

q = sp.simplify(Qx / x**sp.Rational(5,2))
qprime = sp.factor(sp.diff(q, x))
qprime_expected = 5*(x-1)*(2*x**2 + 4*x + 1)/(4*x**sp.Rational(7,2))
assert sp.simplify(qprime - qprime_expected) == 0
assert sp.simplify(Qx.subs(x, 1) - 3) == 0

# Fixed-width lower-half equal-bin gap: delta*s = h/2 and x=s/delta.
delta = sp.sqrt(h/(2*x))
gamma_x = sp.simplify(sp.Rational(4,15) * delta**5 * Qx)
gamma_endpoint = sp.sqrt(2) * h**sp.Rational(5,2) / 10
assert sp.simplify(gamma_x.subs(x,1) - gamma_endpoint) == 0

# Central odd bin comparison used in the theorem:
# Gamma_c >= h^2(1-h)/3 >= 2h^2/9 for h<=1/3,
# while Gamma_end <= sqrt(2/3) h^2 / 10.
constant_margin = sp.simplify(sp.Rational(2,9) - sp.sqrt(sp.Rational(2,3))/10)
assert constant_margin.is_positive is True
# Squared rational verification of the same positive comparison.
assert sp.simplify(sp.Rational(4,81) - sp.Rational(1,150)) > 0

# Symbolic check of the y-reflection reduction for reverse-bin branches.
j, m, X = sp.symbols('j m X', integer=True, positive=True)
y_antidiag = 1 - X
y_reverse_increasing = X + (m - 1 - 2*j)/m
assert sp.simplify(1 - y_antidiag - X) == 0
assert sp.simplify((1 - y_reverse_increasing) - ((2*j+1)/m - X)) == 0

# Exact combinatorial regression of the finite pattern counts m=2,...,12.
strict_patterns = 0
two_flip_patterns = 0
for mm in range(2, 13):
    strict_patterns += 2*((1 << mm) - 1)
    two_flip_patterns += 2*comb(mm, 2)
assert strict_patterns == 16354
assert two_flip_patterns == 572

print('PROB20-05 MULTI-FLIP EXACT CHECK PASSED')
print('P_IN_S_DELTA =', sp.factor(P_sd))
print('Q_X =', sp.factor(Qx))
print('D_Q_OVER_X_5_2 =', qprime)
print('ENDPOINT_GAP =', gamma_endpoint)
print('CENTRAL_CONSTANT_MARGIN =', constant_margin)
print('STRICT_SIGNED_ID_OR_REVERSE_PATTERNS_m2_to_m12 =', strict_patterns)
print('EXACT_TWO_FLIP_PATTERNS_m2_to_m12 =', two_flip_patterns)
print('THEOREM_SCOPE = all m>=2 analytically; finite counts are regression only')
