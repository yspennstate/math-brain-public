from sympy import Matrix, Rational, symbols, factor, simplify, sqrt, I

a, z, H, t = symbols('a z H t', positive=True, real=True)
U = 1 - 2*a

# 1. Exact secant/chord identity for z^2 on [a,1-2a].
chord_slack = simplify((1-a)*z - a*(1-2*a) - z**2)
assert factor(chord_slack - (z-a)*(U-z)) == 0

# 2. Global bound C_a(x) and endpoint specialization.
C = 2 - 3*a - a*(1-2*a)*H
C_endpoint = simplify(C.subs(a, Rational(1,12)))
assert simplify(C_endpoint - (Rational(7,4) - Rational(5,72)*H)) == 0

# 3. Unit-modulus endpoint implication H <= 54/5.
# C_endpoint >= 1 iff H <= 54/5.
assert simplify((C_endpoint - 1) - (Rational(3,4) - Rational(5,72)*H)) == 0
assert simplify((Rational(3,4))*Rational(72,5) - Rational(54,5)) == 0

# 4. Coordinate reduction: 1/t + 4/(1-t) <= 54/5.
poly = factor(54*t**2 - 39*t + 5)
assert poly == (6*t-1)*(9*t-5)
assert simplify(poly.subs(t,Rational(1,6))) == 0
assert simplify(poly.subs(t,Rational(5,9))) == 0

# 5. Uniform-in-x consequence using sum 1/x_i >= 9.
C_uniform = simplify((2 - 3*a - 9*a*(1-2*a)))
assert simplify(C_uniform - (2 - 12*a + 18*a**2)) == 0
uniform_poly = factor(C_uniform - 1)
assert uniform_poly == 18*a**2 - 12*a + 1
small_root = simplify((2-sqrt(2))/6)
assert simplify(uniform_poly.subs(a, small_root)) == 0

# 6. Exact endpoint complex example from the archived barycentric extremal.
a0 = Rational(1,12)
b0 = Rational(3,4)
pairs = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
Qrows = [
    (1,0,0), # 11 -> 1
    (1,0,0), # 12 -> 1
    (0,0,1), # 13 -> 3
    (0,1,0), # 22 -> 2
    (0,1,0), # 23 -> 2
    (0,0,1), # 33 -> 3
]
x = [Rational(1,3)]*3
R = Matrix.zeros(3,3)
for j in range(3):
    for i in range(3):
        r = pairs.index((min(i,j),max(i,j)))
        for k in range(3):
            R[j,k] += x[i]*Qrows[r][k]
T = a0*Matrix.ones(3,3) + b0*R
assert R == Matrix([[Rational(2,3),0,Rational(1,3)],
                    [Rational(1,3),Rational(2,3),0],
                    [0,Rational(1,3),Rational(2,3)]])
assert simplify(T.det() - Rational(3,16)) == 0
# At uniform x, the normalized L2(x) matrix equals T. Frobenius^2 - 1
# is the sum of squared nontrivial singular values.
hs_nontriv = simplify(sum(T[j,k]**2 for j in range(3) for k in range(3)) - 1)
assert hs_nontriv == Rational(3,8)
# Complex tangent modulus squared is 4 det(T) = 3/4, below 1.
assert simplify(4*T.det() - Rational(3,4)) == 0
# New harmonic upper bound at the barycentre is 9/8, so this example is consistent.
assert simplify(C_endpoint.subs(H,9) - Rational(9,8)) == 0
assert Rational(3,4) <= Rational(9,8)

print('ALL EXACT HARMONIC COMPLEX-SPECTRUM CHECKS PASSED')
