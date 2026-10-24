from fractions import Fraction
from math import factorial
from decimal import Decimal, getcontext

getcontext().prec = 80

def dec(x: Fraction) -> str:
    return str(Decimal(x.numerator) / Decimal(x.denominator))

def log_bounds(x: Fraction, N: int):
    assert x > 0
    z = (x - 1) / (x + 1)
    z2 = z*z
    p = z
    s = Fraction(0, 1)
    for k in range(N):
        s += 2*p / (2*k + 1)
        p *= z2
    az = abs(z)
    rem = 2*(az**(2*N+1)) / ((2*N+1)*(1-az*az))
    return s-rem, s+rem

# Imported exact finite-state P04 certificate.
Q = 10**15
ROOT_W = 2065789747160742
A_POLICY = Fraction(16139, 31250)
V_BAR = Fraction(2334416160657687, 10**15)
U = Fraction(ROOT_W, Q)

# Margin-extraction lemma: D<=4 and E[C+a(4-D)]<=U<4a imply
# E C / E D <= U/4.
A_AXIS = U/4
AXIS_GAIN = A_POLICY - A_AXIS
assert A_AXIS == Fraction(1032894873580371, 2000000000000000)
assert AXIS_GAIN == Fraction(1126419629, 2000000000000000)
assert AXIS_GAIN > 0

# Imported exact ten-local SAW constants.
A = Fraction(3889, 2000)
B = Fraction(27893, 10000)
R = Fraction(1993, 400)

# New scalar critical slope.
LA_LO, LA_HI = log_bounds(A, 160)
LB_LO, LB_HI = log_bounds(B, 160)
NUM_LO = (R-1)*A_AXIS - LA_HI
NUM_HI = (R-1)*A_AXIS - LA_LO
RHO_STAR_LO = NUM_LO/LB_HI
RHO_STAR_HI = NUM_HI/LB_LO
assert RHO_STAR_LO < RHO_STAR_HI
assert RHO_STAR_LO > Fraction(13567554, 10**7)
assert RHO_STAR_HI < Fraction(13567555, 10**7)

# A genuinely new closed cone: rho0=1.356756 is below the prior certified
# critical lower bracket 1.3567576.
RHO0 = Fraction(339189, 250000)       # 1.356756
C = Fraction(206579, 400000)          # 0.5164475
S = Fraction(3982501, 1000000)        # 3.982501
QG = R/(1+S)
assert QG == Fraction(4982500, 4982501)
BHAT = Fraction(9999997, 10000000)     # 0.9999997

LQ_LO, LQ_HI = log_bounds(QG, 120)
LH_LO, LH_HI = log_bounds(BHAT, 100)
LOGBETA_LO = -LA_HI - RHO0*LB_HI + S*C + (1+RHO0)*LQ_LO
LOGBETA_HI = -LA_LO - RHO0*LB_LO + S*C + (1+RHO0)*LQ_HI
assert LOGBETA_LO <= LOGBETA_HI
assert LOGBETA_HI < LH_LO

DELTA = 2*(C-A_AXIS)
assert DELTA == Fraction(126419629, 10**15)
assert DELTA > Fraction(1,10**7)

# Imported canonical K<2e14. Since 1/(1-QG)=4,982,501,
# K/(1-QG) < 10^21.
K_UPPER = 2*10**14
C_PREF = 10**21
assert K_UPPER*4982501 < C_PREF

# Explicit finite residual at horizontal scale m=10^15.
M = 10**15
ENDPOINT_BOUND = Fraction(49,10**9)    # 4.9e-8
assert V_BAR*(M-1) < (ENDPOINT_BOUND*M)**2

# BHAT=1-3e-7, so BHAT^M <= exp(-3e8).
# exp(-x) <= 20!/x^20.
TAIL_BOUND = 2*C*C_PREF*Fraction(factorial(20),(3*10**8)**20)
assert TAIL_BOUND < Fraction(1,10**120)

FINITE_RESIDUAL = DELTA-ENDPOINT_BOUND-Fraction(3,M)-TAIL_BOUND
assert FINITE_RESIDUAL > Fraction(7,10**8)

print("ALL_EXACT_CHECKS_PASS = True")
print("axis_cap_exact =", A_AXIS)
print("axis_cap_decimal =", dec(A_AXIS))
print("axis_gain_exact =", AXIS_GAIN)
print("axis_gain_decimal =", dec(AXIS_GAIN))
print("rho_star_lower_decimal =", dec(RHO_STAR_LO))
print("rho_star_upper_decimal =", dec(RHO_STAR_HI))
print("rho_star_bracket = (1.3567554, 1.3567555)")
print("new_closed_rho =", dec(RHO0))
print("prior_critical_lower_bracket = 1.3567576")
print("c =", dec(C))
print("q =", QG)
print("logbeta_upper =", dec(LOGBETA_HI))
print("log_bhat_lower =", dec(LH_LO))
print("delta_exact =", DELTA)
print("delta_decimal =", dec(DELTA))
print("finite_m =", M)
print("endpoint_bound =", dec(ENDPOINT_BOUND))
print("tail_bound_decimal =", dec(TAIL_BOUND))
print("finite_residual_lower =", dec(FINITE_RESIDUAL))
print("finite_residual_gt_7e-8 =", FINITE_RESIDUAL > Fraction(7,10**8))
