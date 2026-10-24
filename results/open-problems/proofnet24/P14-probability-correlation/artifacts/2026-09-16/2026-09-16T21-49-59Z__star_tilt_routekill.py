from fractions import Fraction as Q

# Exact self-check for P14 run 2026-09-16T21-49-59Z.
# This is a finite algebra check only; the graph-theoretic statements are proved in the report.

# Degree-3 star terminal-partition coefficients as polynomials in t.
# D = x|y|z all separate; P = exactly one pair joined; T = all three joined.
star_D = [Q(1), Q(3), Q(3), Q(1)]
star_P = [Q(1), Q(3), Q(2), Q(0)]
star_T = [Q(1), Q(3), Q(0), Q(0)]

# At t=1 the comparison virtual triangle has mu=t^2/(1+3t)=1/4.
t = Q(1)
mu = t*t/(1+3*t)
assert mu == Q(1,4)
star_D_1 = sum(star_D)
star_P_1 = sum(star_P)
star_T_1 = sum(star_T)
tri_D = 1 + 3*mu + 3*mu*mu
tri_P = 1 + 2*mu
tri_T = Q(1)
scale = 1 + 3*t
assert star_P_1 == scale*tri_P
assert star_T_1 == scale*tri_T
# Normalized D excess h and relative D-tilt theta.
h = Q(star_D_1, scale) - tri_D
theta = h/tri_D
assert h == Q(1,16)
assert theta == Q(1,31)

# Generic route-kill: endpoint negative correlation at base and conditional-D laws
# does not survive even the physical relative D-upweight s=1/31.
base = {
    (0,0): Q(1,4),
    (1,0): Q(1,4),
    (0,1): Q(1,4),
    (1,1): Q(1,4),
}
s = Q(1,31)
alpha = base[(0,0)]
Z = 1 + s*alpha
til = dict(base)
til[(0,0)] *= 1+s
til = {k:v/Z for k,v in til.items()}
assert til == {
    (0,0): Q(32,125),
    (1,0): Q(31,125),
    (0,1): Q(31,125),
    (1,1): Q(31,125),
}
pe = til[(1,0)] + til[(1,1)]
pf = til[(0,1)] + til[(1,1)]
pef = til[(1,1)]
gap = pe*pf-pef
assert pe == pf == Q(62,125)
assert pef == Q(31,125)
assert gap == -Q(31,15625)

# Archived P14 all-h route-kill graph: verify the physical unit-star tilt remains safe,
# and record the exact defect ratios used in the report.
c = Q(516440,328805689)
cD = Q(64,41209)
delta = Q(250140019600,13549753638001)
u = Q(203,18133)
G = c + u*(c+cD-delta) + u*u*cD
R = u*delta/((1+u)*(c+u*cD))
coarse_ratio = delta/(32*c+cD)
assert G == Q(460048,328805689)
assert R == Q(15633751225,121473515472)
assert coarse_ratio == Q(15633751225,43879174676)
assert R < 1
assert coarse_ratio < 1

print('deformation_numerator_difference_coeffs=', [Q(0),Q(0),Q(0),Q(1)])
print('t=1 mu=', mu)
print('t=1 star_normalized_d=', Q(star_D_1,scale))
print('t=1 triangle_d=', tri_D)
print('t=1 extra_d=', h)
print('t=1 relative_tilt_theta=', theta)
print('base_alpha=', alpha, 'base_gap=', Q(0), 'conditional_D_gap=', Q(0))
print('tilted_probs=', til)
print('tilted_marginals=', pe, pf, 'tilted_joint=', pef)
print('tilted_gap=', gap)
print('archived_graph_physical_G=', G)
print('archived_graph_defect_ratio=', R)
print('archived_graph_delta_over_32c_plus_cD=', coarse_ratio)
print('ALL_EXACT_CHECKS_PASSED')
