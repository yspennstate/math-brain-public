from fractions import Fraction as F

# Exact certificate for the radius-5, two-type multiseed branching process
# on T_12 x T_8 and the arbitrary-four-pair nonbacktracking uniqueness bound.

p = F(1353, 25000)      # critical-side test point = 0.05412
s = 1 - p
R = 5

# h_r(x)=PGF of open cluster size in a rooted 7-ary tree, truncated at depth r.
# We evaluate h_r(s) and d/dx h_r(x)|_{x=s} exactly.
def h_val_deriv(r):
    x = s
    h = x
    dh = F(1)
    for _ in range(r):
        u = s + p*h
        h_new = x * u**7
        dh_new = u**7 + x*7*u**6*p*dh
        h, dh = h_new, dh_new
    return h, dh

# Type 1: one seed, full T_8 ball of radius R.
h4, dh4 = h_val_deriv(R-1)
u1 = s + p*h4
F1 = s * u1**8
F1p = u1**8 + s*8*u1**7*p*dh4
q11 = p*F1p                    # exactly one horizontal crossing
q12 = 1 - F1 - q11            # at least two crossings

# Type 2: two distinct seeds; use two disjoint outward 7-ary cones of depth R.
h5, dh5 = h_val_deriv(R)
F2 = h5**2
F2p = 2*h5*dh5
q21 = p*F2p
q22 = 1 - F2 - q21

A = 11*q11
B = 11*q12
C = 11*q21
D = 11*q22

# Human-readable rational lower bounds for a strict Perron certificate.
assert A > F(2311,2500)         # 0.9244
assert B > F(4013,100000)       # 0.04013
assert C > F(8107,5000)         # 1.6214
assert D > F(7,50)              # 0.14

lhs_upper = (1-F(2311,2500))*(1-F(7,50))
rhs_lower = F(4013,100000)*F(8107,5000)
assert rhs_lower - lhs_upper == F(25391,500000000)
assert rhs_lower > lhs_upper

# Direct exact determinant check as a redundant certificate.
det_I_minus_M = (1-A)*(1-D) - B*C
assert det_I_minus_M < 0

# Uniqueness side: four completely arbitrary added inverse pairs.
# ||A|| < 2 sqrt(11)+2 sqrt(7)+8 < 797/40.
assert F(199,60)**2 > 11
assert F(127,48)**2 > 7
a_upper = F(797,40)

p_u_floor = F(1083,20000)       # 0.05415
z = 1/p_u_floor
Q = 27
z2_margin = z*z - Q
root_margin = z + F(Q,1)/z - a_upper
assert z2_margin > 0
assert root_margin == F(92503,21660000)
assert root_margin > 0

# Final positive gap.
gap = p_u_floor - p
assert gap == F(3,100000)

print('T09_TWOSEED_ARBITRARY4_EXACT_CHECK')
print('p_c_test =', p, '=', float(p))
print('mean_matrix_float =')
print('  A =', float(A))
print('  B =', float(B))
print('  C =', float(C))
print('  D =', float(D))
print('coarse_det_margin =', rhs_lower-lhs_upper, '=', float(rhs_lower-lhs_upper))
print('direct_det_I_minus_M_float =', float(det_I_minus_M))
print('direct_det_num_bits =', abs(det_I_minus_M.numerator).bit_length())
print('direct_det_den_bits =', det_I_minus_M.denominator.bit_length())
print('adjacency_upper =', a_upper, '=', float(a_upper))
print('p_u_floor =', p_u_floor, '=', float(p_u_floor))
print('z^2-Q =', z2_margin, '=', float(z2_margin))
print('root_margin =', root_margin, '=', float(root_margin))
print('certified_gap =', gap, '=', float(gap))
print('ALL_EXACT_CHECKS_PASS')
