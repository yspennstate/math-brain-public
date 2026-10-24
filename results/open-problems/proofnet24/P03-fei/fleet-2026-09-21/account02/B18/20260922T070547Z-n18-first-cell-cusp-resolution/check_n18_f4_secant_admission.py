#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

# Rigorous interval endpoints imported verbatim from account02/B16
# 20260922T063230Z-n18-exact-entropy-two-secant/check_exact_entropy_two_secant.out.
Q_LO = D("0.999599660938737401432340239630242384364398154263826596748193326851263222362652769671793794")
Q_HI = D("0.999599660938737401432340239630242384364398154263826596748203275313631173833727945601271399")
TH_LO = D("0.00505221312246045939434655084170303695806690469020713564802098136946390390674655961205924090")
TH_HI = D("0.00505221312246045939434655084171251509323056376160455332539176967559630087008270123646436340")

# Exact source-bias point and output from the same B16 certificate.
R_IN = D(1)/D(2) - D(1)/D(5000)
P_OUT = D("0.500400781197500003959999884800000512")
R_OUT = D(1) - P_OUT

# The source report for cert_vi_h96k40_f4 states refinement factor 4
# of the old 1/2048 uniform-p grid, hence local step 1/8192.
H = D(1)/D(8192)
LN2 = D(2).ln()
P = [D(1)/2 - D(j)*H for j in range(5)]
X = [(D(1)/p).ln()/LN2 for p in P]
XI = (D(1)/R_IN).ln()/LN2
XO = (D(1)/R_OUT).ln()/LN2

# First secant [1,XI] uses local slopes s1,s2.
w11=(X[1]-X[0])/(XI-X[0])
w12=(XI-X[1])/(XI-X[0])
# Second secant [XI,XO] uses s2,s3,s4.
w22=(X[2]-XI)/(XO-XI)
w23=(X[3]-X[2])/(XO-XI)
w24=(XO-X[3])/(XO-XI)

# A sufficient source-exact inequality uses the adverse endpoints q=Q_HI,
# theta=TH_HI: m1 - q*m12 >= theta.
c1=w11
c2=w12-Q_HI*w22
c3=-Q_HI*w23
c4=-Q_HI*w24

assert D(1) < (D("0.5")-R_IN)/H < D(2)
assert D(3) < (D("0.5")-R_OUT)/H < D(4)
assert abs(w11+w12-D(1)) < D("1e-70")
assert abs(w22+w23+w24-D(1)) < D("1e-70")

print("PASS")
print("r_in =",R_IN)
print("r_out =",R_OUT)
print("refined_grid_offsets =", (D("0.5")-R_IN)/H, (D("0.5")-R_OUT)/H)
print("segments = 2 4")
print("m1_weights =",w11,w12)
print("m12_weights =",w22,w23,w24)
print("q_interval =",Q_LO,Q_HI)
print("theta_interval =",TH_LO,TH_HI)
print("sufficient_four_slope_coefficients =",c1,c2,c3,c4)
print("coefficient_sum =",c1+c2+c3+c4)
print("equal_slope_critical_upper =",TH_HI/(D(1)-Q_HI))
print("allowed_convexity_at_m12_30 =", (D(1)-Q_HI)*D(30)-TH_HI)
print("allowed_convexity_at_m12_31 =", (D(1)-Q_HI)*D(31)-TH_HI)
print("equal30_sufficient_reserve =", D(30)-Q_HI*D(30)-TH_HI)
print("m1_30_m12_30p01_necessary_gap =", D(30)-Q_LO*D("30.01")-TH_LO)
assert D(30)-Q_HI*D(30) > TH_HI
assert D(30)-Q_LO*D("30.01") < TH_LO
print("interpretation = global |slope|<31 cannot decide; the exact test needs adjacent-secant relative curvature")
