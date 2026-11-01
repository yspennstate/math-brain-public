from fractions import Fraction
from decimal import Decimal, getcontext

def L1(d, p):
    """Radius-one lower bound for phi_{T_d}(p). Exact Fraction."""
    return Fraction(1) - (1-p)*(1-p*p)**d

def Phi2(d, p):
    """Radius-two lower bound for phi_{T_d}(p). Exact Fraction."""
    s = 1-p
    branch_fail = s + p*s*(1-p*p)**(d-1)
    return Fraction(1) - s*(branch_fail**d)

def show_margin(name, x):
    assert isinstance(x, Fraction)
    assert x > 0
    print(f"{name}: PASS")
    print(f"  numerator={x.numerator}")
    print(f"  denominator={x.denominator}")
    print(f"  decimal={float(x):.18g}")

print("PROB10-09 SURFACE-PRODUCT FAMILY EXACT CORE")

m34 = 13*Phi2(10, Fraction(19,400)) - 1
show_margin("G34_DEPTH2_13PHI_MINUS_1", m34)

# beta_34 < 50/3 reduces sign-safely to 300 sqrt(13) < 1243.
assert 13*300**2 < 1243**2
print("G34_BETA_LT_50_OVER_3: PASS")
print(f"  square_margin={1243**2 - 13*300**2}")
assert Fraction(19,400)*Fraction(50,3) < 1
print("G34_P0_BETA_LT_1_VIA_50_OVER_3: PASS")
print(f"  rational_margin={1-Fraction(19,400)*Fraction(50,3)}")

m23 = 9*Phi2(6, Fraction(73,1000)) - 1
show_margin("G23_DEPTH2_9PHI_MINUS_1", m23)

# beta_23 = 5+sqrt(5)+sqrt(11+10sqrt(5)); 73 beta_23 < 1000
# reduces, after a positive-side square, to 146000 sqrt(5) < 371251.
assert Fraction(635,73) > 3
assert 5*146000**2 < 371251**2
print("G23_73_BETA_LT_1000: PASS")
print(f"  square_margin={371251**2 - 5*146000**2}")

m24 = 13*L1(6, Fraction(1,16)) - 1
show_margin("G24_RADIUS1_13L_MINUS_1", m24)
# R_24=4+2sqrt(5)+2sqrt(13)<16 follows from sqrt(65)<9.
assert 65 < 81
print("G24_R_LT_16: PASS")
print(f"  square_margin={81-65}")

m33 = 9*L1(10, Fraction(137,2000)) - 1
show_margin("G33_RADIUS1_9L_MINUS_1", m33)
# beta_33=8+sqrt(41), and 137 beta_33<2000 iff 137sqrt(41)<904.
assert 137**2 * 41 < 904**2
print("G33_137_BETA_LT_2000: PASS")
print(f"  square_margin={904**2 - 137**2*41}")

# Generic g>=3,h>=4 after reordering g<=h.
x = Fraction(18,5)
p = Fraction(1,1)/(4*(1+x))
F10 = x*x*p + Fraction(17,18)*10*x*x*p*p*(1-9*p*p)
assert 13*25 > 18**2
assert p < Fraction(1,18)
show_margin("GENERIC_G_GE_3_H_GE_4_F10_MINUS_1_AT_18_OVER_5", F10-1)

# Generic g=2,h>=5.
x = Fraction(41,10)
p = Fraction(1,1)/(4*(1+x))
F6 = x*x*p + Fraction(19,20)*6*x*x*p*p*(1-5*p*p)
assert 17*100 > 41**2
assert p < Fraction(1,20)
show_margin("GENERIC_G2_H_GE_5_F6_MINUS_1_AT_41_OVER_10", F6-1)

# Frozen G34 metric improvement is the old p_c comparison point minus the new one.
delta_improvement = Fraction(13,251) - Fraction(19,400)
show_margin("G34_CERTIFIED_GAP_IMPROVEMENT", delta_improvement)

# High-precision decimals; all theorem sign checks above are exact.
getcontext().prec = 70
D = Decimal
def dsqrt(n):
    return D(n).sqrt()

beta34 = D(5)+dsqrt(13)+(D(11)+D(10)*dsqrt(13)).sqrt()
gap34 = D(1)/beta34-D(19)/D(400)
beta23 = D(5)+dsqrt(5)+(D(11)+D(10)*dsqrt(5)).sqrt()
gap23 = D(1)/beta23-D(73)/D(1000)
beta33 = D(8)+dsqrt(41)
gap33 = D(1)/beta33-D(137)/D(2000)
R24 = D(4)+D(2)*dsqrt(5)+D(2)*dsqrt(13)
beta24 = (R24+(R24*R24-D(92)).sqrt())/D(2)
gap24 = D(1)/beta24-D(1)/D(16)

print("CERTIFIED_DECIMALS")
print(f"  G34_gap_lower={gap34}")
print(f"  G23_gap_lower={gap23}")
print(f"  G24_gap_lower={gap24}")
print(f"  G33_gap_lower={gap33}")

# Numerical diagnostic only for (2,2); NOT an exact obstruction/theorem.
R22 = D(4)+D(4)*dsqrt(5)
beta22 = (R22+(R22*R22-D(60)).sqrt())/D(2)
p22 = D(1)/beta22
s = D(1)-p22
d = 6
H = s
for _ in range(10000):
    Hn = s*(s+p22*H)**(d-1)
    if abs(Hn-H) < D("1e-60"):
        H = Hn
        break
    H = Hn
Q = s*(s+p22*H)**d
phi = D(1)-Q
print("G22_FULL_TREE_CLUSTER_AT_NB_THRESHOLD: NUMERICAL_DIAGNOSTIC_ONLY")
print(f"  p_NB={p22}")
print(f"  5phi={D(5)*phi}")
print("  interpretation=one-sided fiber-cluster branching remains below mean 1 at this comparison point")

print("VERDICT=PASS_EXACT_ARITHMETIC_CORE")
print("STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_BENJAMINI_SCHRAMM")
