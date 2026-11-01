from sympy import symbols, sqrt, pi, Rational, simplify, Matrix

m, L = symbols('m L', positive=True)
eps = sqrt(L)/m
R = sqrt(m)/L
mu = R*eps + eps**2/2

assert simplify(sqrt(m)*mu - (L/(2*m**Rational(3,2)) + 1/sqrt(L))) == 0
assert simplify(eps*R**2 - L**Rational(-3,2)) == 0
assert simplify(eps*R**3/sqrt(m) - L**Rational(-5,2)) == 0

# Dense latent matrix B_m = I - (2+1/m) n n^T, n=(1,2,3)/sqrt(14).
n = Matrix([1,2,3])/sqrt(14)
alpha = 2 + 1/m
B = Matrix.eye(3) - alpha*(n*n.T)
assert simplify((B*n)[0] + (1+1/m)*n[0]) == 0
assert simplify((B*n)[1] + (1+1/m)*n[1]) == 0
assert simplify((B*n)[2] + (1+1/m)*n[2]) == 0

v1 = Matrix([2,-1,0])/sqrt(5)
v2 = Matrix([3,6,-5])/sqrt(70)
assert simplify(n.dot(v1)) == 0
assert simplify(n.dot(v2)) == 0
assert all(simplify(z) == 0 for z in (B*v1-v1))
assert all(simplify(z) == 0 for z in (B*v2-v2))

assert simplify(B[0,0] - (12*m-1)/(14*m)) == 0
assert simplify(B[1,1] - (3*m-2)/(7*m)) == 0
assert simplify(B[2,2] + (4*m+9)/(14*m)) == 0

# Pinned Theorem C: lambda1=lambda2=1, mu=1+1/m.
mu_spec = 1 + 1/m
theoremC = simplify(2*pi/sqrt(mu_spec+1))
gauss_cone = simplify(6/sqrt(mu_spec+1))
assert simplify(gauss_cone/theoremC - 3/pi) == 0

print('PASS QFORM-NEARROOTM-SATELLITE-SHARP-WITNESS-v1')
print('normalized bank mean = L^(-1/2) + L/(2 m^(3/2))')
print('satellite variance scale = L^(-3/2)')
print('satellite Lyapunov scale = L^(-5/2)')
print('Theorem-C saturation ratio = 3/pi')
print('required ruled-marginal average in the limit = 6/pi')
