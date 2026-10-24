from __future__ import annotations

import sympy as sp

# Exact symbolic self-check for the one-flipped-branch continuum transport.
# No floating point is used in the asserted identities.

u, v, s, d, r = sp.symbols('u v s d r', positive=True)

# ---------- Lower-half interval I=[a,b] subset [0,1/2] ----------
# a=2u^2, b=2v^2, h=2(v^2-u^2), c=u^2+v^2.
h = 2 * (v**2 - u**2)
c = u**2 + v**2
z = 2 * s**2  # diagonal target parameter F_S(s) on s<=1/2

# Monotone transport of the d-marginal on A={u<=s<=v, |d|<=s}
# to the uniform vertical segment [-h/2,h/2].
g1 = 2 * (v-u) * d                     # 0<=d<=u
g2 = 2 * v * d - d**2 - u**2          # u<=d<=v

assert sp.simplify(g1.subs(d, u) - g2.subs(d, u)) == 0
assert sp.simplify(g2.subs(d, v) - h/2) == 0
assert sp.simplify(sp.diff(g1, d) - 2*(v-u)) == 0
assert sp.simplify(sp.diff(g2, d) - 2*(v-d)) == 0

# Euclidean squared-cost difference at a source point in rotated coordinates.
# Original Euclidean cost is 2[(s-s')^2+(d-d')^2].
def point_delta(g):
    return sp.expand(2 * ((s-c)**2 + (d-g)**2 - ((s-z)**2 + d**2)))

pd1 = point_delta(g1)
pd2 = point_delta(g2)

# Source Lebesgue measure is dxdy = 2 ds dd.  Integrate d>=0 and double by d symmetry,
# hence overall factor 4 multiplying the positive-d integral of point_delta.
delta_lower = sp.simplify(4 * (
    sp.integrate(sp.integrate(pd1, (s, u, v)), (d, 0, u))
    + sp.integrate(sp.integrate(pd2, (s, d, v)), (d, u, v))
))

expected_lower = -sp.Rational(4, 15) * (v-u)**2 * (
    12*u**3 + 19*u**2*v + 6*u*v**2 + 3*v**3
)
assert sp.simplify(delta_lower - expected_lower) == 0

# Endpoint simplification a=0, b=h0.  Then v=sqrt(h0/2).
h0 = sp.symbols('h0', positive=True)
endpoint_expr = sp.simplify(expected_lower.subs({u: 0, v: sp.sqrt(h0/2)}))
expected_endpoint = -sp.sqrt(2) * h0**sp.Rational(5,2) / 10
assert sp.simplify(endpoint_expr - expected_endpoint) == 0

# ---------- Central symmetric interval I=[a,1-a] ----------
# Put r=sqrt(a/2), so h_c=1-4r^2 and c=1/2.
hc = 1 - 4*r**2
cc = sp.Rational(1,2)
zlow = 2*s**2

# On A={r<=s<=1-r, |d|<=min(s,1-s)}, positive d marginal density is
# 2(1-2r) for d<=r, and 2(1-2d) for r<=d<=1/2.
gcent1 = 2*(1-2*r)*d
gcent2 = 2*d - 2*d**2 - 2*r**2
assert sp.simplify(gcent1.subs(d, r) - gcent2.subs(d, r)) == 0
assert sp.simplify(gcent2.subs(d, sp.Rational(1,2)) - hc/2) == 0
assert sp.simplify(sp.diff(gcent1,d) - 2*(1-2*r)) == 0
assert sp.simplify(sp.diff(gcent2,d) - 2*(1-2*d)) == 0


def point_delta_c(g):
    return sp.expand(2 * ((s-cc)**2 + (d-g)**2 - ((s-zlow)**2 + d**2)))

pc1 = point_delta_c(gcent1)
pc2 = point_delta_c(gcent2)

# Integrate only s<=1/2,d>=0.  There are two symmetries (s<->1-s,d<->-d),
# and Jacobian dxdy=2 ds dd, so factor 8.
delta_center = sp.simplify(8 * (
    sp.integrate(sp.integrate(pc1, (s, r, sp.Rational(1,2))), (d, 0, r))
    + sp.integrate(sp.integrate(pc2, (s, d, sp.Rational(1,2))), (d, r, sp.Rational(1,2)))
))
expected_center = -sp.Rational(8,3) * r**2 * (2*r-1)**2 * (2*r+1)
assert sp.simplify(delta_center - expected_center) == 0

# Equal m-bin central branch (m odd): a=(m-1)/(2m), r=1/2*sqrt(1-1/m).
m = sp.symbols('m', positive=True)
sigma = sp.sqrt(1-1/m)
center_m = sp.simplify(expected_center.subs(r, sigma/2))
expected_center_m = -sp.Rational(2,3)/m * (1-1/m) * (1-sigma)
assert sp.simplify(center_m - expected_center_m) == 0

# Exact finite sanity checks for m=2..25: every equal-bin single flip has a strictly
# negative certified cost change using the corresponding closed form.
# We compare algebraic expressions via exact positivity after squaring where needed.
def lower_gap_for_bin(mv: int, j: int):
    # j-th bin, assuming (j+1)/m <= 1/2.
    uu = sp.sqrt(sp.Rational(j, 2*mv))
    vv = sp.sqrt(sp.Rational(j+1, 2*mv))
    gap = sp.simplify(-expected_lower.subs({u: uu, v: vv}))
    # all factors in the manifest formula are positive for v>u>=0.
    assert gap.is_positive is True
    return gap

checked = 0
for mv in range(2, 26):
    for j in range(mv):
        a = sp.Rational(j, mv)
        b = sp.Rational(j+1, mv)
        if b <= sp.Rational(1,2):
            lower_gap_for_bin(mv, j)
            checked += 1
        elif a >= sp.Rational(1,2):
            # upper-half case follows by the exact square isometry (x,y)->(1-x,1-y),
            # reducing to the reflected lower bin.
            jj = mv-1-j
            lower_gap_for_bin(mv, jj)
            checked += 1
        else:
            # Equal-bin crossing can occur only for odd m, and then it is centered.
            assert mv % 2 == 1 and j == mv//2
            sig = sp.sqrt(1-sp.Rational(1,mv))
            gap = sp.simplify(sp.Rational(2,3*mv)*(1-sp.Rational(1,mv))*(1-sig))
            assert gap.is_positive is True
            checked += 1

assert checked == sum(range(2,26))

print('PROB20-05 ONE-FLIP EXACT CHECK PASSED')
print('LOWER_INTERVAL_DELTA =', sp.factor(delta_lower))
print('ENDPOINT_DELTA =', endpoint_expr)
print('CENTRAL_INTERVAL_DELTA =', sp.factor(delta_center))
print('CENTRAL_EQUAL_M_DELTA =', center_m)
print('EXACT_EQUAL_BIN_SINGLE_FLIP_CASES_CHECKED_m2_to_m25 =', checked)
print('BASELINE_COST = 1/10; every displayed delta is <=0, and is <0 for every proper flipped bin.')
