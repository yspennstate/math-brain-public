import sympy as sp

u, p, d = sp.symbols('u p d', real=True)
c = p + d

# Conditional quantile transport for the two x-slabs.
q1 = p*u/(p+d)
q2 = p + (1-p)*(u-(p+d))/(1-p-d)

cost1 = sp.integrate((u-q1)**2, (u, 0, c))
cost2 = sp.integrate((u-q2)**2, (u, c, 1))
total = sp.factor(sp.simplify(cost1 + cost2))
assert sp.simplify(total - d**2/sp.Integer(3)) == 0

# Exact algebra behind the sharp second-moment ceiling.
prod = sp.expand((d+p)*(1-p-d))
rhs = sp.expand(p*(1-p) + (1-2*p)*d - d**2)
assert sp.simplify(prod-rhs) == 0

# Benchmark separation.
gap = sp.Rational(1,10) - sp.Rational(1,12)
assert gap == sp.Rational(1,60)

# Every 2 x 2 checkerboard copula with uniform marginals is one-parameter.
a, b, c2, e = sp.symbols('a b c e', real=True)
sol = sp.solve([
    sp.Eq(a+b, 2),
    sp.Eq(c2+e, 2),
    sp.Eq(a+c2, 2),
    sp.Eq(b+e, 2),
], [b, c2, e], dict=True)
assert sol == [{b: 2-a, c2: 2-a, e: a}]

# p=1/2, delta=+/-theta/2 on the two y-halves.
theta = sp.symbols('theta', real=True)
checker2 = sp.simplify((((theta/2)**2)/3 + ((-theta/2)**2)/3)/2)
assert checker2 == theta**2/sp.Integer(12)

print('PROB20-05 TWO-SLAB EXACT CHECK PASSED')
print('CONDITIONAL_COST =', total)
print('VARIANCE_IDENTITY =', sp.expand(prod))
print('UNIVERSAL_TWO_SLAB_BOUND =', sp.Rational(1,12))
print('BENCHMARK_GAP =', gap)
print('TWO_BY_TWO_COST =', checker2)
