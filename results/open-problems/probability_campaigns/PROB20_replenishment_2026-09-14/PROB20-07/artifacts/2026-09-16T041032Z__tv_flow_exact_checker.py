import sympy as sp

# Exact scalar algebra for the invariant-set TV theorem.
a, b, D = sp.symbols('a b D', positive=True)
expr = sp.expand(b * (2 * D - D**2) - D)
assert sp.factor(expr) == -D * (b * D - 2 * b + 1)

Dstar = sp.simplify(2 - 1 / b)
assert sp.simplify(b * (2 * Dstar - Dstar**2) - Dstar) == 0
assert sp.simplify(Dstar.subs(b, sp.Rational(3, 4)) - sp.Rational(2, 3)) == 0

# Secondary affinity recurrence: b m^2 - m + 1-b has roots 1 and (1-b)/b.
m = sp.symbols('m')
aff_poly = sp.factor(b * m**2 - m + 1 - b)
assert sp.factor(aff_poly - (m - 1) * (b * m + b - 1)) == 0

# Exact three-state stationary-flow determinant identity.
x1, x2, x3 = sp.symbols('x1 x2 x3', positive=True)
s12, s23, s31, c = sp.symbols('s12 s23 s31 c', real=True)

M = sp.Matrix([
    [x1 - (s12 + s31) / 2, (s12 + c) / 2, (s31 - c) / 2],
    [(s12 - c) / 2, x2 - (s12 + s23) / 2, (s23 + c) / 2],
    [(s31 + c) / 2, (s23 - c) / 2, x3 - (s23 + s31) / 2],
])

det_raw = sp.expand(M.det())
target = (
    x1 * x2 * x3
    + c**2 / 4
    - sp.Rational(1, 2) * (
        s12 * x3 * (x1 + x2)
        + s23 * x1 * (x2 + x3)
        + s31 * x2 * (x1 + x3)
    )
    + sp.Rational(1, 4) * (s12 * s23 + s12 * s31 + s23 * s31)
)

# The displayed report identity is on the simplex x1+x2+x3=1.
diff = sp.factor(det_raw - target)
assert sp.simplify(diff.subs(x3, 1 - x1 - x2)) == 0
assert diff == (c**2 + s12*s23 + s12*s31 + s23*s31) * (x1+x2+x3-1) / 4

# The flow parameterization has the required row and column marginals.
rows = [sp.simplify(sum(M[i, j] for j in range(3))) for i in range(3)]
cols = [sp.simplify(sum(M[i, j] for i in range(3))) for j in range(3)]
assert rows == [x1, x2, x3]
assert cols == [x1, x2, x3]

# Endpoint translation of the parent-symmetry residual cap into flow variables.
aa = sp.Rational(1, 12)
bb = sp.Rational(3, 4)
xj, xk = sp.symbols('xj xk', positive=True)
qk = (xk - aa) / bb
cap_R = (qk + xj**2) / (2 * xj)
cap_M = sp.expand(xj * (aa + bb * cap_R))
target_cap = (xk - aa) / 2 + aa * xj + bb * xj**2 / 2
assert sp.simplify(cap_M - target_cap) == 0

print('ALL EXACT TV/FLOW CHECKS PASSED')
