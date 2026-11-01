#!/usr/bin/env python3
"""
NM13-07 / T03, 2026-09-20.
Exact rational branch-tangent continuation for the already directed-interval
certified complete-second stationary box at alpha0=12.319635.

The only inherited numerical data used below are outward interval enclosures
already archived by NM13-03/NM13-07 for the fixed box:
  H_p, H_B, alpha_p, alpha_B, Psi_p, Psi_B,
the rational preconditioner A, the weighted radii, center residual ceilings,
and the anchor lower bound on Psi at the true stationary root.

All arithmetic in this file is fractions.Fraction.  The new step is:
  (i) prove det D(H,alpha)>0 on the whole box;
  (ii) prove dPsi/dalpha < 1/25 on the whole stationary branch by checking
       the multi-affine inequality N - (1/25) D < 0 at all 64 vertices;
  (iii) continue the contraction uniformly to alpha=12.31963454 and
        transport the positive objective with that slope bound.
"""
from fractions import Fraction as F
import itertools

# Directed-interval enclosures from the archived alpha=12.319635 certificate.
# Slight rational widenings are used intentionally.
Hp  = (F(-3371,100000), F(-2828,100000))
HB  = (F(3284,10_000_000), F(5044,10_000_000))
Ap  = (F(24671,1000), F(25288,1000))
AB  = (F(-60244,100000), F(-6008,10000))
Pp  = (F(8701,10000), F(8955,10000))
PB  = (F(-2137,100000), F(-2115,100000))

slope_cap = F(1,25)

det_min = None
num_min = None
gap_max = None
slope_min_vertex = None
slope_max_vertex = None
for hp,hb,ap,ab,pp,pb in itertools.product(Hp,HB,Ap,AB,Pp,PB):
    det = hp*ab - hb*ap
    num = -pp*hb + pb*hp
    assert det > 0
    gap = num - slope_cap*det
    if det_min is None or det < det_min: det_min = det
    if num_min is None or num < num_min: num_min = num
    if gap_max is None or gap > gap_max: gap_max = gap
    slope = num/det
    if slope_min_vertex is None or slope < slope_min_vertex: slope_min_vertex=slope
    if slope_max_vertex is None or slope > slope_max_vertex: slope_max_vertex=slope

# Multi-affine functions on a rectangle attain extrema at vertices.
# Hence these two exact inequalities hold on the full six-dimensional box.
assert det_min > 0
assert num_min > 0
assert gap_max < 0
assert slope_max_vertex < slope_cap

# Uniform contraction data inherited from the same directed-interval box.
Aq = [[F(-7294853,100000), F(-504965,10000000)],
      [F(-3028867,1000), F(-3758826,1000000)]]
dr = [F(1,10_000_000), F(1,250_000)]
qcon = F(70497781,125000000)
EH = F(47,10**13)     # |H(center)|
Ealpha0 = F(37,10**12) # |alpha(center)-12.319635|

alpha0 = F(12319635,1000000)
delta = F(46,100_000_000) # 4.6e-7
alpha1 = alpha0-delta
EA = Ealpha0 + delta

eta = max(F(1,dr[i])*(abs(Aq[i][0])*EH + abs(Aq[i][1])*EA)
          for i in range(2))
rho = eta/(1-qcon)
assert eta < 1-qcon
assert rho < 1

# Anchor comparison lower bound at the true alpha0 stationary root.
psi0_lb = F(23584189005311,1090044380000000000000)
psi1_lb = psi0_lb - slope_cap*delta
assert psi1_lb > 0

alphaL = F(315148718753,50000000000)        # 6.30297437506
alpha_before = F(61598174139,5000000000)    # 12.3196348278
assert alpha1 == F(615981727,50000000)       # 12.31963454
gain = alpha_before-alpha1
width_before = alpha_before-alphaL
width_after = alpha1-alphaL
assert gain > 0

print("BRANCH_TANGENT_VERTEX_CERTIFICATE")
print("DET_MIN", det_min, float(det_min))
print("NUM_MIN", num_min, float(num_min))
print("SLOPE_VERTEX_MIN", slope_min_vertex, float(slope_min_vertex))
print("SLOPE_VERTEX_MAX", slope_max_vertex, float(slope_max_vertex))
print("SLOPE_CAP", slope_cap, float(slope_cap))
print("MAX_NUM_MINUS_CAP_DET", gap_max, float(gap_max))
print("CONTRACTION_Q", qcon, float(qcon))
print("TARGET_DELTA_FROM_ANCHOR", delta, float(delta))
print("ETA", eta, float(eta))
print("ONE_MINUS_Q", 1-qcon, float(1-qcon))
print("RHO", rho, float(rho))
print("PSI_ANCHOR_LOWER", psi0_lb, float(psi0_lb))
print("PSI_NEW_LOWER", psi1_lb, float(psi1_lb))
print("RIGOROUS_ALPHA_U_BEFORE", float(alpha_before))
print("RIGOROUS_ALPHA_U_AFTER", float(alpha1))
print("SOURCE_GAIN", gain, float(gain))
print("BRACKET_WIDTH_BEFORE", float(width_before))
print("BRACKET_WIDTH_AFTER", float(width_after))
print("ALL_EXACT_BRANCH_TANGENT_CHECKS_PASS")
