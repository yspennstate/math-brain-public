"""Exact symbolic certificate for the R7-06 I0114 omega*_9 leading-shell argument.

Checks the A2 orbit-polynomial identities, the failure of the fully saturated
local Hermite projector on the first forbidden Fourier shell P_{3,3}, and a
repaired shell minorant whose residual is globally nonnegative on the
Hardin--Tenpas transformed A2 triangle.  Exact SymPy arithmetic only.
"""
import sympy as sp

x, y, u, z, t = sp.symbols("x y u z t")
T = sp.chebyshevt


def P(k1, k2):
    """A2 orbit polynomial, k1>=k2>=0 and equal parity."""
    assert k1 >= k2 >= 0 and (k1-k2) % 2 == 0
    return sp.expand((
        T(k1,x)*T(k2,y)
        + T((k1-k2)//2,x)*T((3*k1+k2)//2,y)
        + T((k1+k2)//2,x)*T((3*k1-k2)//2,y)
    ) / sp.Integer(3))


alpha = sp.expand((-1 + 2*y*(x+y))/3)
beta  = sp.expand((-1 + 2*x*(x-3*y+4*y**3))/3)
gamma = sp.expand((2*T(2,x)*T(2,y) + T(4,y))/3)
delta = sp.expand((T(3,x)*y + x*T(5,y) + T(2,x)*T(4,y))/3)
eta   = P(3,3)

assert sp.expand(P(1,1)-alpha) == 0
assert sp.expand(P(2,0)-beta) == 0
assert sp.expand(P(2,2)-gamma) == 0
assert sp.expand(P(3,1)-delta) == 0


def norm2(k1, k2):
    return sp.Rational(3*k1*k1 + k2*k2, 3)


assert norm2(1,1) == sp.Rational(4,3)
assert norm2(2,0) == 4
assert norm2(2,2) == sp.Rational(16,3)
assert norm2(3,1) == sp.Rational(28,3)
assert norm2(3,3) == 12
assert norm2(4,0) == 16

p = {x: sp.Rational(-1,2), y: 1}
q = {x: -1, y: sp.Rational(1,2)}
basis = [sp.Integer(1), alpha, beta, gamma, delta]


def contacts(f):
    f1, f2, f22 = sp.diff(f,x), sp.diff(f,y), sp.diff(f,y,2)
    return sp.Matrix([
        f.subs(p), f.subs(q), f1.subs(p), f2.subs(p),
        (f22 + 6*f1).subs(q)
    ])


# B20 obstruction: saturating both local walls fails already on eta=P_{3,3}.
M = sp.Matrix.hstack(*[contacts(b) for b in basis])
assert M.det() != 0
coef_sat = M.LUsolve(contacts(eta))
assert list(coef_sat) == [-2,-10,-6,-4,-4]
h_sat = sp.expand(sum(coef_sat[i]*basis[i] for i in range(5)))
R_sat = sp.factor(eta-h_sat)
R_sat_expected = sp.factor(
    (2*y-1)*(2*y+1)*(2*x*y+2*y**2-1)
    *(4*x**2+4*x*y+4*y**2-3)/3
)
assert sp.expand(R_sat-R_sat_expected) == 0
assert sp.factor(R_sat.subs(y,1) - (2*x+1)**3) == 0

# Repaired leading-shell correction: choose C=-8,D=-6, with p/q/tangent
# contact determining c0,A,B.
h_eta = sp.expand(sp.Rational(-9,2)-19*alpha-11*beta-8*gamma-6*delta)
R = sp.expand(eta-h_eta)
R_inv = sp.expand(sp.Rational(1,2)+beta+12*alpha**2+36*alpha**3)
assert sp.expand(R-R_inv) == 0

assert sp.expand(gamma - (-1-2*alpha-2*beta+6*alpha**2)) == 0
assert sp.expand(delta - (1+alpha+2*beta-6*alpha**2+3*alpha*beta)) == 0
assert sp.expand(eta - (-2-9*alpha-6*beta-18*alpha*beta+36*alpha**3)) == 0

# No interior critical point: the orbit map is nonsingular in the interior and
# dR/dbeta=1 in invariant coordinates.
J = sp.factor(sp.det(sp.Matrix([
    [sp.diff(alpha,x), sp.diff(alpha,y)],
    [sp.diff(beta,x), sp.diff(beta,y)]
])))
J_expected = sp.factor(-sp.Rational(8,9)*(x-y)*(x-(4*y**3-3*y)))
assert sp.expand(J-J_expected) == 0

# Exact boundary positivity.
R_top = sp.factor(R.subs(y,1))
assert sp.expand(R_top - (2*x+1)**2*(16*x+17)/6) == 0

R_left = sp.factor(R.subs(x,-1))
left_q = 16*y**4-32*y**3-4*y**2+16*y+5
assert sp.expand(R_left - (2*y-1)**2*left_q/6) == 0
left_u = sp.expand(left_q.subs(y,(u+1)/2))
assert sp.expand(left_u-(u**4-7*u**2-2*u+9)) == 0

b = 4*y**3-3*y
R_slant = sp.factor(R.subs(x,b))
Q = 256*z**4-256*z**3-16*z**2+48*z+1
assert sp.expand(
    R_slant-(2*y-1)**2*(2*y+1)**2*Q.subs(z,y**2)/6
) == 0


def bernstein_coeffs(poly, var, a, bnd, n=4):
    expr = sp.Poly(sp.expand(poly.subs(var,a+(bnd-a)*t)), t)
    cs = sp.symbols("c0:"+str(n+1))
    bern = sum(cs[k]*sp.binomial(n,k)*t**k*(1-t)**(n-k)
               for k in range(n+1))
    diff = sp.Poly(sp.expand(bern-expr.as_expr()),t)
    sol = sp.solve([diff.coeff_monomial(t**j) for j in range(n+1)], cs,
                   dict=True)[0]
    return [sp.simplify(sol[c]) for c in cs]


left_bern = bernstein_coeffs(u**4-7*u**2-2*u+9,u,sp.Rational(0),sp.Rational(1))
assert left_bern == [9,sp.Rational(17,2),sp.Rational(41,6),4,1]

intervals = [
    (sp.Rational(1,4),sp.Rational(1,2),[9,sp.Rational(19,2),sp.Rational(53,6),7,5]),
    (sp.Rational(1,2),sp.Rational(2,3),[5,sp.Rational(11,3),sp.Rational(61,27),sp.Rational(29,27),sp.Rational(49,81)]),
    (sp.Rational(2,3),sp.Rational(3,4),[sp.Rational(49,81),sp.Rational(10,27),sp.Rational(17,54),sp.Rational(1,2),1]),
    (sp.Rational(3,4),sp.Rational(1),[1,sp.Rational(5,2),sp.Rational(41,6),16,33]),
]
for a,bnd,expected in intervals:
    got = bernstein_coeffs(Q,z,a,bnd)
    assert got == expected
    assert all(c > 0 for c in got)

# Nondegenerate contact jets used in the small-a perturbation proof.
assert R.subs(p) == 0
assert sp.diff(R,x).subs(p) == 0
assert sp.diff(R,y).subs(p) == -3
assert sp.diff(R,x,2).subs(p) == 12
assert R.subs(q) == 0
assert sp.diff(R,x).subs(q) == 3
assert sp.diff(R,y).subs(q) == 0
assert sp.diff(R,y,2).subs(q) == 12

print("EXACT_CHECK_PASS")
print("orbit_P33 =", eta)
print("low_norm2 =", [norm2(1,1),norm2(2,0),norm2(2,2),norm2(3,1)])
print("eta_norm2 =", norm2(3,3), "next_shell_norm2 =", norm2(4,0))
print("saturated_coeffs =", list(coef_sat))
print("saturated_top_residual =", sp.factor(R_sat.subs(y,1)))
print("repaired_coeffs =", [sp.Rational(-9,2),-19,-11,-8,-6])
print("repaired_residual_invariants =", sp.factor(R_inv))
print("jacobian =", J)
print("top_boundary =", R_top)
print("left_boundary =", R_left)
print("left_bernstein =", left_bern)
for a,bnd,expected in intervals:
    print("slant_Q_bernstein", a, bnd, expected)
print("jets_p =", [R.subs(p),sp.diff(R,x).subs(p),sp.diff(R,y).subs(p),sp.diff(R,x,2).subs(p)])
print("jets_q =", [R.subs(q),sp.diff(R,x).subs(q),sp.diff(R,y).subs(q),sp.diff(R,y,2).subs(q)])
