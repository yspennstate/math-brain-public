import sympy as sp

x, a = sp.symbols("x a", real=True)
sqrt3 = sp.sqrt(3)
theta1 = sp.Matrix([1, 0])
theta2 = sp.Matrix([-sp.Rational(1, 2), sqrt3 / 2])
theta3 = sp.Matrix([-sp.Rational(1, 2), -sqrt3 / 2])


def sqdist(z, t):
    return sp.expand((z - t).dot(z - t))


# Source H^2 comparison: for ideal nuclei (theta_i,r_i), compare
# r_i |z-theta_i|^2.  Fix cube-root boundary angles and radii (a,1,1).
zaxis = sp.Matrix([x, 0])
d1 = sqdist(zaxis, theta1)
d2 = sqdist(zaxis, theta2)
d3 = sqdist(zaxis, theta3)
assert sp.simplify(d2 - d3) == 0
assert sp.simplify(d1 - (x - 1) ** 2) == 0
assert sp.simplify(d2 - (x**2 + x + 1)) == 0

F = sp.expand(a * d1 - d2)
disc = sp.factor(sp.discriminant(F, x))
a_of_x = sp.factor(d2 / d1)
der = sp.factor(sp.diff(a_of_x, x))
assert sp.simplify(disc - 3 * (4 * a - 1)) == 0
assert sp.simplify(a_of_x - (x**2 + x + 1) / (x - 1) ** 2) == 0
assert sp.simplify(der + 3 * (x + 1) / (x - 1) ** 3) == 0
assert sp.simplify(a_of_x.subs(x, -1)) == sp.Rational(1, 4)
assert sp.limit(a_of_x, x, 1, dir="-") == sp.oo
assert sp.simplify(F.subs(a, 1) + 3 * x) == 0
assert sp.simplify(
    F.subs(a, sp.Rational(1, 4))
    + sp.Rational(3, 4) * (x + 1) ** 2
) == 0

# Finite vertex-set obstruction: two distinct equal-radius angle triples
# have the same unique common Voronoi vertex z=0 but different cells.
u, v = sp.symbols("u v", real=True)
z = sp.Matrix([u, v])
A = [theta1, theta2, theta3]
B = [sp.Matrix([1, 0]), sp.Matrix([0, 1]), sp.Matrix([-1, 0])]
solA = sp.solve(
    [sqdist(z, A[0]) - sqdist(z, A[1]),
     sqdist(z, A[0]) - sqdist(z, A[2])],
    [u, v], dict=True,
)
solB = sp.solve(
    [sqdist(z, B[0]) - sqdist(z, B[1]),
     sqdist(z, B[0]) - sqdist(z, B[2])],
    [u, v], dict=True,
)
assert solA == [{u: 0, v: 0}]
assert solB == [{u: 0, v: 0}]

# The two Voronoi partitions really differ at this exact rational point.
zt = sp.Matrix([-sp.Rational(3, 8), sp.Rational(1, 8)])
distA = [sp.simplify(sqdist(zt, t)) for t in A]
distB = [sp.simplify(sqdist(zt, t)) for t in B]
assert sp.simplify(distA[0] - distA[1]) > 0
assert sp.simplify(distA[2] - distA[1]) > 0
assert sp.simplify(distB[0] - distB[2]) > 0
assert sp.simplify(distB[1] - distB[2]) > 0

print("P0408_FINITE_CORE_EXACT")
print("F(a,x) =", F)
print("discriminant_x =", disc)
print("a(x) =", a_of_x)
print("a'(x) =", der)
print("a(-1) =", a_of_x.subs(x, -1))
print("lim_x_to_1_minus a(x) =", sp.limit(a_of_x, x, 1, dir="-"))
print("threshold_factor =", sp.factor(F.subs(a, sp.Rational(1, 4))))
print("vertex_solutions_A =", solA)
print("vertex_solutions_B =", solB)
print("test_point =", tuple(zt))
print("distances_A =", distA)
print("distances_B =", distB)
print("ALL_EXACT_CHECKS_PASS")
