from fractions import Fraction
from math import factorial
from decimal import Decimal, getcontext

getcontext().prec = 70

def dec(x: Fraction) -> str:
    return str(Decimal(x.numerator) / Decimal(x.denominator))

def log_bounds(x: Fraction, N: int):
    # log(x)=2 atanh(z), z=(x-1)/(x+1).
    # Tail absolute value is bounded by
    # 2 |z|^(2N+1) / ((2N+1)(1-|z|^2)).
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

# Consumed P04 finite-state certificate.
Q = 10**15
ROOT_W = 2065789747160742
A_OLD = Fraction(16139, 31250)
V_BAR = Fraction(2334416160657687, 10**15)

# New deterministic extraction: if E[C+a(4-D)] <= U and D<=4,
# then E C / E D <= U/4.
U = Fraction(ROOT_W, Q)
A_AXIS = U/4
GAIN = A_OLD - A_AXIS
assert A_AXIS == Fraction(1032894873580371, 2000000000000000)
assert GAIN == Fraction(1126419629, 2000000000000000)
assert GAIN > 0

# Consumed ten-local SAW constants.
A = Fraction(3889, 2000)
B = Fraction(27893, 10000)
R = Fraction(1993, 400)

# Critical scalar slope rho_* = ((R-1)a - log A)/log B.
LA_LO, LA_HI = log_bounds(A, 140)
LB_LO, LB_HI = log_bounds(B, 140)
NUM_LO = (R-1)*A_AXIS - LA_HI
NUM_HI = (R-1)*A_AXIS - LA_LO
RHO_LO = NUM_LO / LB_HI
RHO_HI = NUM_HI / LB_LO
assert RHO_LO < RHO_HI
assert RHO_LO > Fraction(13567554, 10**7)
assert RHO_HI < Fraction(13567555, 10**7)

# Clean closed cone rho0=1.3568 with a positive lower-tail level.
RHO0 = Fraction(848, 625)
C = Fraction(103291, 200000)  # 0.516455
S = Fraction(19913, 5000)     # 3.9826
QG = R/(1+S)
assert QG == Fraction(49825, 49826)
BHAT = Fraction(99999, 100000)

LQ_LO, LQ_HI = log_bounds(QG, 100)
LH_LO, LH_HI = log_bounds(BHAT, 80)
LOGBETA_LO = -LA_HI - RHO0*LB_HI + S*C + (1+RHO0)*LQ_LO
LOGBETA_HI = -LA_LO - RHO0*LB_LO + S*C + (1+RHO0)*LQ_HI
assert LOGBETA_LO <= LOGBETA_HI
assert LOGBETA_HI < LH_LO  # hence beta(rho0) < BHAT

DELTA = 2*(C-A_AXIS)
assert DELTA == Fraction(15126419629, 10**15)
assert DELTA > Fraction(15, 10**6)

# Finite error. The canonical ten-local certificate has K<2e14.
# Since 1/(1-QG)=49826, C_pref < 1e19.
K_UPPER = 2*10**14
C_PREF = 10**19
assert K_UPPER * 49826 < C_PREF

M = 10**11
ENDPOINT_BOUND = Fraction(4832, 10**9)  # 4.832e-6
assert V_BAR*(M-1) < (ENDPOINT_BOUND*M)**2

# BHAT^M <= exp(-M/1e5)=exp(-1e6).
# exp(-x) <= 20!/x^20 for x>0.
TAIL_BOUND = 2*C*C_PREF*Fraction(factorial(20), (10**6)**20)
assert TAIL_BOUND < Fraction(1, 10**82)

FINITE_RESIDUAL = DELTA - ENDPOINT_BOUND - Fraction(3, M) - Fraction(1,10**82)
assert FINITE_RESIDUAL > Fraction(1, 10**5)

print("ALL_EXACT_CHECKS_PASS = True")
print("axis_cap_exact =", A_AXIS)
print("axis_cap_decimal =", dec(A_AXIS))
print("axis_gain_exact =", GAIN)
print("axis_gain_decimal =", dec(GAIN))
print("rho_star_lower_decimal =", dec(RHO_LO))
print("rho_star_upper_decimal =", dec(RHO_HI))
print("rho_star_bracket = (1.3567554, 1.3567555)")
print("rho0 =", dec(RHO0))
print("c =", dec(C))
print("q =", QG)
print("logbeta_upper =", dec(LOGBETA_HI))
print("log_bhat_lower =", dec(LH_LO))
print("delta_exact =", DELTA)
print("delta_decimal =", dec(DELTA))
print("finite_m =", M)
print("endpoint_bound =", dec(ENDPOINT_BOUND))
print("tail_bound_decimal <", dec(Fraction(1,10**82)))
print("finite_residual_lower =", dec(FINITE_RESIDUAL))
print("finite_residual_gt_1e-5 =", FINITE_RESIDUAL > Fraction(1,10**5))
