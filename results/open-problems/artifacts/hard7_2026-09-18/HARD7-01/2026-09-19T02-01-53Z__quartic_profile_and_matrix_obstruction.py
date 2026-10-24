from fractions import Fraction
import math

# HARD7-01 run 6 exact certificate.
#
# Purpose: refute an ABSTRACT level-profile gluing principle for the quartic
# (p=4), n=3 reduction. This is NOT a counterexample to dimensional
# Brunn--Minkowski: geometric realizability of the profiles by convex-body
# intersections is not asserted.
#
# Define, on 0<=y<=1,
#   phi_a(y)=y                  (0<=y<=a),
#            4y-3a             (a<=y<=1).
# Every phi_a is convex, has phi_a'(0+)=1, and the same terminal profile height
# y=1. For t=3/10, the weighted infimal convolution of phi_a0 and phi_a1 is
# exactly phi_at with at=(1-t)a0+t a1.
#
# Let
#   I_A(a)=3 int_0^1 y^2 exp(-phi_a(y)^4) dy.
# The desired abstract profile gluing would require
#   I_A(at)^(1/3) >= (1-t)I_A(a0)^(1/3)+t I_A(a1)^(1/3).
# This script certifies the strict reverse inequality by rational interval
# arithmetic.

NE = 60
NO = 61
R = Fraction(2)
GRID = 10**9


def first_piece_bounds(a):
    # 3*int_0^a y^2 exp(-y^4)dy.
    # Taylor's theorem gives P_odd(x)<=exp(-x)<=P_even(x) for x>=0.
    def integ(N):
        s = Fraction(0)
        for k in range(N + 1):
            coeff = Fraction((-1)**k, math.factorial(k))
            s += 3 * coeff * a**(4*k + 3) / (4*k + 3)
        return s
    lo, hi = integ(NO), integ(NE)
    assert lo <= hi
    return lo, hi


def transformed_piece_bounds(a):
    # int_a^2 (z+3a)^2 exp(-z^4)dz, where z=4y-3a.
    c = 3*a
    def integ(N):
        s = Fraction(0)
        for k in range(N + 1):
            coeff = Fraction((-1)**k, math.factorial(k))
            for power, fac in (
                (4*k + 2, Fraction(1)),
                (4*k + 1, 2*c),
                (4*k, c*c),
            ):
                s += coeff * fac * (R**(power + 1) - a**(power + 1)) / (power + 1)
        return s
    lo, hi = integ(NO), integ(NE)
    assert lo <= hi
    return lo, hi


def IA_bounds(a):
    # For our three a-values, z_max=4-3a > 2.
    zmax = 4 - 3*a
    assert zmax > R

    lo1, hi1 = first_piece_bounds(a)
    lo2, hi2 = transformed_piece_bounds(a)

    # For z>=2, convexity of z^4 gives z^4>=16+32(z-2).
    # Also exp(-16)<2^-16 because e>2. Hence the integral from 2 to zmax
    # is bounded above by the integral to infinity displayed below.
    lam = Fraction(32)
    c = R + 3*a
    tail_poly = Fraction(2, lam**3) + Fraction(2*c, lam**2) + Fraction(c*c, lam)
    tail_hi = Fraction(1, 2**16) * tail_poly

    lo = lo1 + Fraction(3, 64)*lo2
    hi = hi1 + Fraction(3, 64)*(hi2 + tail_hi)
    assert 0 < lo <= hi
    return lo, hi


def floor_cube_root_on_grid(x):
    lo, hi = 0, 2*GRID
    while lo + 1 < hi:
        m = (lo + hi)//2
        if Fraction(m**3, GRID**3) <= x:
            lo = m
        else:
            hi = m
    return Fraction(lo, GRID)


def cube_root_bracket(xlo, xhi):
    lo = floor_cube_root_on_grid(xlo)
    fl = floor_cube_root_on_grid(xhi)
    hi = fl if fl**3 == xhi else fl + Fraction(1, GRID)
    assert lo**3 <= xlo <= xhi <= hi**3
    return lo, hi


a0 = Fraction(1, 200)
a1 = Fraction(1, 2)
t = Fraction(3, 10)
at = (1-t)*a0 + t*a1
assert at == Fraction(307, 2000)

vals = {}
for name, a in (("a0", a0), ("at", at), ("a1", a1)):
    L, U = IA_bounds(a)
    rL, rU = cube_root_bracket(L, U)
    vals[name] = (rL, rU)

lhs_upper = vals["at"][1]
rhs_lower = (1-t)*vals["a0"][0] + t*vals["a1"][0]
gap = rhs_lower - lhs_upper

assert vals["a0"] == (Fraction(123291671, 500000000),
                      Fraction(246583857, 1000000000))
assert vals["at"] == (Fraction(88275809, 250000000),
                      Fraction(44137951, 125000000))
assert vals["a1"] == (Fraction(606213843, 1000000000),
                      Fraction(606214097, 1000000000))
assert gap == Fraction(13688843, 10000000000)
assert gap > 0

print("HARD7_01_ABSTRACT_PROFILE_CERTIFICATE")
print(f"a0={a0}; at={at}; a1={a1}; t={t}")
print(f"cube_root_bracket_a0={vals['a0'][0]},{vals['a0'][1]}")
print(f"cube_root_bracket_at={vals['at'][0]},{vals['at'][1]}")
print(f"cube_root_bracket_a1={vals['a1'][0]},{vals['a1'][1]}")
print(f"lhs_upper={lhs_upper}")
print(f"rhs_lower={rhs_lower}")
print(f"rhs_lower_minus_lhs_upper={gap}")
print("PROFILE_GLUE_COUNTEREXAMPLE_CERTIFIED=True")

# Exact arithmetic for the line-concentration obstruction to the entire
# radial-style pointwise-matrix proof template.
#
# theta=(1,2,0)/sqrt(5), A=[[0,1,0],[1,2,0],[0,0,0]].
# Along x=r theta under the quartic line law:
#   E[r^4]=25/17,
#   E[sum x_i^2 (A x)_i^2]=104/17,
#   E[(grad W . A x)^2/(x . grad W)]=1764/289.
# For any symmetric M(x) satisfying Mx=grad W and Hess W+M >=0,
# PSD Cauchy forces
#   <My,y> >= 4(grad W.y)^2/(x.grad W)-3 sum x_i^2 y_i^2.
# The resulting minimal RHS already exceeds ||A||_F^2=6 in the line limit.
D_line = Fraction(104, 17)
rank_line = Fraction(1764, 289)
minimal_template_rhs = 4*rank_line - 3*D_line
hess_norm_sq = Fraction(6)
matrix_gap = minimal_template_rhs - hess_norm_sq

assert minimal_template_rhs == Fraction(1752, 289)
assert hess_norm_sq == Fraction(1734, 289)
assert matrix_gap == Fraction(18, 289)
assert matrix_gap > 0

print(f"line_D_term={D_line}")
print(f"line_rank_term={rank_line}")
print(f"minimal_matrix_template_rhs={minimal_template_rhs}")
print(f"hessian_norm_sq={hess_norm_sq}")
print(f"matrix_template_gap={matrix_gap}")
print("MATRIX_TEMPLATE_LIMIT_OBSTRUCTION_CERTIFIED=True")
