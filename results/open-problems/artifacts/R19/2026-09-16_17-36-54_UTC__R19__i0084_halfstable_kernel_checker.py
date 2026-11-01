import sympy as sp

alpha = sp.Rational(1, 2)
rho = sp.Rational(1, 2)
pi = sp.pi

def free_small_coeff(n):
    return sp.simplify(
        (-1)**(n-1)
        * sp.gamma(1 + sp.Rational(n,1)/alpha)
        / (sp.factorial(n) * sp.gamma(2 + (1/alpha - 1)*n))
        * sp.sin(pi*n*rho) / pi
    )

def free_tail_coeff(n):
    return sp.simplify(
        (-1)**(n-1)
        * sp.gamma(1 + alpha*n)
        / (sp.factorial(n) * sp.gamma(2 + (alpha-1)*n))
        * sp.sin(pi*n*alpha*rho) / pi
    )

small = [free_small_coeff(n) for n in range(1,6)]
tail = [free_tail_coeff(n) for n in range(1,4)]

assert small[0] == 1/pi
assert small[1] == 0
assert small[2] == -5/pi
assert small[3] == 0
assert small[4] == 42/pi
assert sp.simplify(2*small[2] - (-10/pi)) == 0

assert tail[0] == sp.sqrt(2)/(2*pi)
assert tail[0] > 0
lead_derivative = sp.simplify(-(alpha+1)*tail[0])
assert lead_derivative == -3*sp.sqrt(2)/(4*pi)

# Exact normalized worst-case algebra used in C009:
# core derivative = -1; core-mass loss <= 1/4; outside positive
# derivative contribution <= 1/4, hence total <= -1/2.
normalized_upper = -1 + sp.Rational(1,4) + sp.Rational(1,4)
assert normalized_upper == -sp.Rational(1,2)

print("free symmetric alpha=1/2 small-x coefficients n=1..5:", small)
print("free symmetric alpha=1/2 tail coefficients n=1..3:", tail)
print("free symmetric alpha=1/2 density second derivative at zero:", -10/pi)
print("free symmetric alpha=1/2 leading tail derivative coefficient:", lead_derivative)
print("normalized C009 outer derivative upper bound:", normalized_upper)
print("PASS")
