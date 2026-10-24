from fractions import Fraction as F
import sympy as sp

def qfun(p):
    return p + p*p - p**3

def c_line(p):
    q = qfun(p)
    s = 1 - q
    return s * ((1-p)/(1-s*p))**2

def offspring_mean(N,p):
    return 2*(N-1)*(1-c_line(p))

# Exceptional first product block: N=3, K=Z.
p0 = F(21,125)
m0 = offspring_mean(3,p0)
assert m0 > 1
z0 = F(250,43)
root_margin0 = z0 + F(7,1)/z0 - F(7,1)
assert z0*z0 > 7 and root_margin0 > 0
gap0 = F(43,250) - p0
assert gap0 == F(1,250)

print("N=3 product block")
print("p_c test p =", p0, float(p0))
print("offspring mean =", m0, float(m0))
print("offspring margin =", m0-1, float(m0-1))
print("p_u floor =", F(43,250), float(F(43,250)))
print("nonbacktracking root margin =", root_margin0, float(root_margin0))
print("certified gap >", gap0, float(gap0))

# Uniform critical-side inequality for N>=4 at p=1/(2N).
N = sp.symbols("N", integer=True, positive=True)
p = sp.Rational(1,2)/N
q = p+p**2-p**3
s = 1-q
C = sp.simplify(s*((1-p)/(1-s*p))**2)
crit_margin = sp.factor(2*(N-1)*(1-C)-1)
num, den = sp.fraction(crit_margin)
m = sp.symbols("m", integer=True, nonnegative=True)
num_shift = sp.Poly(sp.expand(num.subs(N,m+4)),m)
assert all(c > 0 for c in num_shift.all_coeffs())
print("N>=4 critical symbolic margin =", crit_margin)
print("numerator at N=m+4 =", num_shift.as_expr())

# Specialized K=Z uniqueness side: z=N+3.
# F(N)=N+(2N+1)/(N+3)-2*sqrt(2N-2).
# F is increasing on [4,infty) since F' > 1-2/sqrt(6)>0.
# At N=4, 37/7 > 2 sqrt(6), certified by squaring.
base_square_margin = F(37,7)**2 - F(24,1)
assert base_square_margin > 0
print("special K=Z root base square margin =", base_square_margin, float(base_square_margin))

# General product H_N x K.  B has size b and contains an infinite-order pair.
# For N>=b+2, at z=2N-1:
# z+Q/z-a = 2N-b-1+b/(2N-1)-2sqrt(2N-2)
# >= N+1-2sqrt(2N-2)>0, since (N+1)^2-8(N-1)=(N-3)^2.
b = sp.symbols("b", integer=True, positive=True)
z = 2*N-1
Q = 2*N+b-1
linear = sp.simplify(z + Q/z - (b+1))
target = sp.simplify(2*N-b-1 + b/z)
assert sp.simplify(linear-target) == 0
square_margin = sp.expand((N+1)**2 - 8*(N-1))
assert sp.factor(square_margin) == (N-3)**2
print("general product linear root part =", target)
print("general square margin =", square_margin, "=", sp.factor(square_margin))
print("ALL_EXACT_CHECKS_PASS")
