from fractions import Fraction as F
from math import factorial

# R13 exact-arithmetic checker for the p={1,2} score-mixture cube.
#
# The analytic proof (in the immutable report) reduces the new D=140
# directional-total-variation constant to two scalar quantities:
#
#   C = integral_0^infty h(z)/M(z) dz
#     = pi - integral_0^infty du/(cosh(u)+38/pi),
#
# and
#
#   E sqrt(Vbar_D)
#     = sqrt(2/(pi D)) integral_0^infty [1-L(x)^D]/x^2 dx,
#
# where L(x)=(1/20)L1(x)+(19/20)L2(x),
# L1(x)=x K_1(x), L2(x)=(1+x)e^{-x}.
#
# Every acceptance comparison below is integer/Fraction arithmetic.
# Floating-point values are printed only as diagnostics.

D = 140
W = F(1, 20)
PI_LO = F(333, 106)
PI_HI = F(355, 113)
TARGET_C = F(72, 25)          # 2.88
TARGET_EROOT = F(1053, 1000) # 1.053
TARGET_H = F(7251, 1000)     # 7.251

def ceil_div(a, b):
    return (a + b - 1) // b

# ---------------------------------------------------------------------------
# Exact logarithm enclosures from log r = e log 2 + 2 atanh(y).
# ---------------------------------------------------------------------------

def _log_atanh_bounds_unit(m, N=18):
    # 1 <= m < 2 except the log(2) helper where m=2; then 0<=y<=1/3.
    y = (m - 1) / (m + 1)
    y2 = y * y
    yp = y
    s = F(0)
    for j in range(N):
        s += F(2, 2*j + 1) * yp
        yp *= y2
    # Tail: denominators are >= 2N+1, so dominate by a geometric series.
    rem = F(2, 2*N + 1) * yp / (1 - y2)
    return s, s + rem

_LOG2_LO, _LOG2_HI = _log_atanh_bounds_unit(F(2), 18)

def log_bounds(r):
    assert r > 0
    e = 0
    m = r
    while m >= 2:
        m /= 2
        e += 1
    while m < 1:
        m *= 2
        e -= 1
    lo, hi = _log_atanh_bounds_unit(m, 18)
    if e >= 0:
        return e*_LOG2_LO + lo, e*_LOG2_HI + hi
    return e*_LOG2_HI + lo, e*_LOG2_LO + hi

# Classical H_n-log(n+1) < gamma.  The exact log enclosure proves gamma>11/20.
H20 = sum(F(1, k) for k in range(1, 21))
LOG21_LO, LOG21_HI = log_bounds(F(21))
GAMMA_LO = F(11, 20)
assert H20 - LOG21_HI > GAMMA_LO

LOG2000_LO, LOG2000_HI = log_bounds(F(2000))
assert LOG2000_HI < 8

# ---------------------------------------------------------------------------
# Support halfwidth C: exact lower Riemann certificate for
# J = int_0^infty du/(cosh u + 38/pi).
# ---------------------------------------------------------------------------

def cosh_upper(x, N=20):
    # Positive Taylor series through x^(2N)/(2N)! plus geometric tail.
    term = F(1)
    s = term
    for k in range(1, N + 1):
        term *= x*x / F((2*k - 1)*(2*k))
        s += term
    nxt = term * x*x / F((2*N + 1)*(2*N + 2))
    ratio = x*x / F((2*N + 3)*(2*N + 4))
    assert ratio < 1
    return s + nxt/(1 - ratio)

A_UP = F(38) / PI_LO
DU = F(1, 50)
J_LO = F(0)
for j in range(400):  # [0,8], right endpoints; integrand is decreasing.
    u_right = F(j + 1, 50)
    J_LO += DU / (A_UP + cosh_upper(u_right))

C_UP = PI_HI - J_LO
assert C_UP < TARGET_C

# ---------------------------------------------------------------------------
# Lower bounds for L1=x K1(x) and L2=(1+x)e^{-x}, x in [0,1/2].
# ---------------------------------------------------------------------------

def exp_neg_lower(x, N=13):
    # Alternating Taylor series; odd N gives a lower bound for x>=0.
    assert N % 2 == 1
    term = F(1)
    s = term
    for k in range(1, N + 1):
        term *= -x / F(k)
        s += term
    return s

def L1_lower(x, Nser=5):
    # Exact series:
    # x K1(x) = 1 + (x^2/2) sum_{k>=0}
    # [log(x/2)+gamma-(H_k+H_{k+1})/2]
    # (x^2/4)^k/[k!(k+1)!].
    #
    # On 0<x<=1/2 all coefficients are negative.  We use lower bounds for
    # log and gamma in the retained terms, then a uniform exact negative-tail
    # bound.  For x>=1/1000, -log(x/2)<log(2000)<8 and H_{k+1}<=k+1, so
    # |coefficient_k| < k+9.
    q = x*x/4
    log_lo, _ = log_bounds(x/2)
    s = F(0)
    Hk = F(0)
    b = F(1)  # q^0/(0!1!)
    for k in range(Nser):
        if k > 0:
            b *= q / F(k*(k+1))
        Hkp1 = Hk + F(1, k+1)
        a_lo = log_lo + GAMMA_LO - (Hk + Hkp1)/2
        assert a_lo < 0
        s += a_lo*b
        Hk = Hkp1

    N = Nser
    bN = b * q / F(N*(N+1))
    cN = F(N+9)*bN
    # For k>=N and q<=1/16 the ratio of successive (k+9)b_k terms
    # is bounded by the following number.
    rmax = F(N+10, N+9) * F(1,16) / F((N+1)*(N+2))
    assert rmax < 1
    tail_abs = cN/(1-rmax)
    return 1 + x*x/2*(s - tail_abs)

# ---------------------------------------------------------------------------
# Exact upper Riemann certificate for I_D.
#
# g(x)=[1-L(x)^D]/x^2 is decreasing because
# 1-L(sqrt(2s))^D is a concave Bernstein function vanishing at zero.
#
# On [0,h], 1-a^D<=D(1-a), and:
#  1-L2 <= x^2/2,
#  1-L1 <= (x^2/2)[1+log(2/x)].
# On [1/2,infty], g(x)<=1/x^2, whose integral is 2.
# ---------------------------------------------------------------------------

Q = 10**9      # downward quantization for L
GS = 10**9     # upward quantization for g
h = F(1,1000)

FIRST = F(D,2)*h*(1 + W*(LOG2000_HI + 1))
FIRST_SCALED = ceil_div(FIRST.numerator*GS, FIRST.denominator)

QD = pow(Q, D)
SUM_G_SCALED = 0
MIN_L_NUM = Q

for j in range(1, 500):
    x = F(j, 1000)
    l1 = L1_lower(x)
    l2 = (1+x)*exp_neg_lower(x)
    L_lower = W*l1 + (1-W)*l2
    assert 0 < L_lower <= 1

    # Quantize downward, preserving a rigorous lower bound.
    L_num = (L_lower.numerator*Q)//L_lower.denominator
    assert 0 < L_num <= Q
    MIN_L_NUM = min(MIN_L_NUM, L_num)

    # g <= [1-(L_num/Q)^D]/x^2, then quantize upward to GS^{-1}.
    LP = pow(L_num, D)
    g_num = (QD - LP)*10**6
    g_den = QD*j*j
    g_scaled = ceil_div(g_num*GS, g_den)
    SUM_G_SCALED += g_scaled

# I_upper = FIRST + h*sum(g_j upper) + 2.
# Use one common modest denominator after all pointwise exact comparisons.
I_NUM = FIRST_SCALED*1000 + SUM_G_SCALED + 2*GS*1000
I_DEN = GS*1000
I_UP = F(I_NUM, I_DEN)

# Eroot <= sqrt(2/(pi D))*I_UP.  Verify Eroot<1053/1000 by squaring
# with pi>=PI_LO.
assert I_UP*I_UP * F(2,1)/(PI_LO*D) < TARGET_EROOT*TARGET_EROOT

# ---------------------------------------------------------------------------
# Combine C and I directly:
# 3 C sqrt(2/pi) Eroot
#   = 6 C I /(pi sqrt(D)).
# ---------------------------------------------------------------------------

SQRT_D_LO = F(118321, 10000)
assert SQRT_D_LO*SQRT_D_LO < D

H_UP = 6*C_UP*I_UP/(PI_LO*SQRT_D_LO)
assert H_UP < TARGET_H

# Row-pruning check for n=86: with h=7.251, the number of rows whose
# Euclidean norm exceeds h/sqrt(86) is strictly below 141, hence <=140.
N = 86
assert F(N*N,1)/(TARGET_H*TARGET_H) < D+1
# Equivalent tail branch condition h > n/sqrt(D+1).
assert N*N < TARGET_H*TARGET_H*(D+1)

print("R13_SCORE_MIXTURE_CUBE_EXACT_PASS")
print("D =", D)
print("gamma_lower =", float(GAMMA_LO))
print("J_lower =", float(J_LO))
print("C_upper =", float(C_UP))
print("I_upper =", float(I_UP))
print("Eroot_target =", float(TARGET_EROOT))
print("combined_DTV_halfwidth_upper =", float(H_UP))
print("new_branch_constant =", float(TARGET_H))
print("row_pruning_ratio =", float(F(N*N,1)/(TARGET_H*TARGET_H)))
print("min_quantized_L_on_grid =", MIN_L_NUM/Q)
print("support_certificate = C < 72/25")
print("root_certificate = E_sqrt_meanV < 1053/1000")
print("ALL_ACCEPTANCE_TESTS_USE_EXACT_RATIONAL_ARITHMETIC")
