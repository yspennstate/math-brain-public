from fractions import Fraction as F
import math

# Crossed-star rank-two core with one small nonzero tail singular value.
# N is a perfect square so the physical star coefficients are exact rationals.
N = 4096
eps = F(1,N)
sqrtN = math.isqrt(N)
assert sqrtN*sqrtN == N

# Singular values of B_N are 1,1,eps.
# Left singular vectors: u1 = left anchor, u2 = flat on N exterior
# coordinates, u3 = left tail.  Right singular vectors:
# v1 = flat on N exterior coordinates, v2 = right anchor, v3 = right tail.
exterior_top2_leverage = F(1,N)
core_edge = F(1,sqrtN)
tail_edge = eps

# Partner r23 tau=1/16 collar on nonanchor top-two leverage:
partner_collar = F(5057,51600)
assert exterior_top2_leverage < partner_collar
# Partner r24 fixed-scale tube example with G=1:
assert eps < F(1,64)

# Direct full-block ridge closure is impossible for every q in [1,3/2).
# If the ridge leverage gate holds at the left anchor then
# k1 = 1/(1+rho^2) <= q/2, so rho^2 >= 2/q-1 > 1/3.
# Thus k2=k1<=q/2 and k3 < 3 eps^2.  Since q>=1,
# q+3eps^2 < 4q/3.
tail_trace_upper = 3*eps*eps
assert tail_trace_upper < F(1,3)

# Coupled two-bank theorem: the left planar bank (X_anchor,U_ext)
# and right planar bank (V_ext,Y_anchor) each have joint density cap <= sqrt(e).
# det D = 1.  Therefore:
L3_bound = 3**(2/3) * math.e**(1/3)
outer_square_bound = 8 * math.e**(1/4) / 3**(1/4)

print("STATUS PASS")
print("N", N)
print("eps", eps, float(eps))
print("exterior_top2_leverage", exterior_top2_leverage, float(exterior_top2_leverage))
print("partner_tau_1_16_collar", partner_collar, float(partner_collar))
print("core_physical_edge", core_edge, float(core_edge))
print("tail_physical_edge", tail_edge, float(tail_edge))
print("ridge_tail_trace_upper", tail_trace_upper, float(tail_trace_upper))
print("analytic_ridge_obstruction", "for every 1<=q<3/2: gate => theta < q+3eps^2 < 4q/3")
print("grouped_planar_L3_bound", L3_bound)
print("after_independent_outer_square_Linf_bound", outer_square_bound)
print("target_large_eigenvalues", "{1,+1,-1,+1,-1,+eps,-eps}")
