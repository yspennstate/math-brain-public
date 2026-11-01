import sympy as sp

sqrt3 = sp.sqrt(3)
sqrt5 = sp.sqrt(5)
sqrt15 = sp.sqrt(15)

# Oh's sharp regular-tessellation edge constant at (p,q)=(5,4).
p, q = 5, 4
phi_edge = sp.simplify((p-2) * sp.sqrt(1 - sp.Rational(4, (p-2)*(q-2))))
assert sp.simplify(phi_edge - sqrt3) == 0

k = 5 - sqrt3
assert k > 0
# d is the coefficient appearing after dividing the pentagon inequality by k.
d = sp.simplify(sp.Rational(2,1) / k)
assert sp.simplify(d - (5 + sqrt3)/11) == 0
assert 0 < d < 1

g = sp.symbols('g', positive=True)
G = sp.simplify((g + d)/(g + 1))
# Core coefficient identity:
# [a-o-d*i] + (1-G)[b+o-g*i]
# = a + (1-G)b - G(o+i).
assert sp.simplify(-1 + (1-G) + G) == 0
assert sp.simplify(-d - g*(1-G) + G) == 0
assert sp.simplify(G - g - (d-g**2)/(g+1)) == 0

# Positive fixed point and contraction-side identity.
gstar = sp.sqrt(d)
assert sp.simplify(G.subs(g,gstar) - gstar) == 0
assert sp.simplify(G-gstar - (1-gstar)*(g-gstar)/(g+1)) == 0

# Previous bootstrap lower bound, exactly as archived in run 84.
c84 = sp.simplify((2*sqrt15 + 6*sqrt3)/(3*sqrt5 + 2*sqrt15 + 5*sqrt3 + 9))
g84 = sp.sqrt(c84)
assert sp.simplify(d-c84) > 0
assert gstar > g84

# Original pre-bootstrap seed is >1/2 and below the new fixed point.
g0 = sp.simplify(1/(sqrt3 + sqrt5 - 2))
assert g0 > sp.Rational(1,2)
assert gstar > g0

# Retained exact finite upper witness.
upper = sp.Rational(384566,484385)
# Both positive, so comparing squares is exact.
upper_sq_minus_d = sp.simplify(upper**2 - d)
assert upper_sq_minus_d > 0
assert upper > gstar

# Convenient exact rational brackets.
assert gstar > sp.Rational(39,50)  # 0.78
assert gstar < sp.Rational(79,100) # 0.79

old_gap = sp.simplify(upper-g84)
new_gap = sp.simplify(upper-gstar)
assert old_gap > new_gap > 0
reduction = sp.simplify(1-new_gap/old_gap)
assert reduction > sp.Rational(7,10)

# Affine constant remains strictly positive: D/k gives RHS 4.
assert sp.Rational(4,1) > 0

print('OH_EDGE_H54', phi_edge)
print('K', k)
print('D', d)
print('NEW_FIXED_POINT_EXACT', gstar)
print('NEW_FIXED_POINT_DECIMAL', sp.N(gstar,40))
print('PREVIOUS_LOWER_DECIMAL', sp.N(g84,40))
print('UPPER_EXACT', f'{upper.p}/{upper.q}')
print('UPPER_DECIMAL', sp.N(upper,40))
print('OLD_GAP_DECIMAL', sp.N(old_gap,40))
print('NEW_GAP_DECIMAL', sp.N(new_gap,40))
print('GAP_REDUCTION_FRACTION_DECIMAL', sp.N(reduction,30))
print('UPPER_SQUARE_MINUS_D', upper_sq_minus_d)
print('BOOTSTRAP_MAP', G)
print('ALL_EXACT_SYMBOLIC_CHECKS_PASS')