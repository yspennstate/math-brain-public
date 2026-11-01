from fractions import Fraction as F
from math import factorial

# R13 exact checker: a localized improvement of the p=33/20, D=139
# cosine-power / inverse-gamma directional-TV certificate.
# All acceptance tests below are exact rational inequalities.
#
# Imported theorem/certificate from the immutable predecessor chain:
#   runs/R13/20260919T1001Z_p165-tilted-4f2d.md
#   artifacts/R13/20260919T1001Z_p165-tilted-4f2d_checker.py
#   artifacts/R13/20260919T1001Z_p165-tilted-4f2d.out
# and its arithmetic tightening:
#   runs/R13/20260919T1100Z_mixed-bsb-coverdual-a83f.md
#   artifacts/R13/20260919T1100Z_constant-tightening-a83f_checker.py
# These certify for p=33/20, D=139:
#   delta := 1-E sqrt(X_139) > 53745767/10^9,
# and the old tilted-transform lower polynomial Z_old satisfies Z_old>=0 on
# 0<=u<=43/40.  We recheck the latter positivity below so that the only
# imported numerical theorem is the rational delta floor.

D = 139
q = 40
beta = F(13, 40)       # (p-1)/2 for p=33/20
a_num = 53              # a=(p+1)/2=53/40
cold = F(78472, 100000) # predecessor lower bound for the Frobenius coefficient c_*
cnew = F(78476, 100000) # sharpened lower bound proved below
dc = cnew - cold
dm = F(8839437, 10**7) # predecessor exact lower certificate for D^(-1/40)

# -------------------------------------------------------------------------
# 1. Sharpen c_* by the same Gautschi product, but push the product to N=10000.
# For beta=13/40 and a=1+beta=53/40,
# c_* = beta^(beta-1)/(1+beta) * Gamma(1-beta)/Gamma(beta).
# If P_N=prod_{k=0}^{N-1}(k+beta)/(k+1-beta), Gautschi gives
# c_*^40 > beta^(-27) P_N^40 (N-beta)^14 /(1+beta)^40.
# -------------------------------------------------------------------------
N_GAUTSCHI = 10000
P = F(1)
for k in range(N_GAUTSCHI):
    P *= F(40*k + 13, 40*k + 27)

c40_lower = (
    beta**(-27)
    * P**40
    * (F(N_GAUTSCHI) - beta)**14
    / (1 + beta)**40
)
assert c40_lower > cnew**40
assert cnew > cold

# D^(-1/40)>dm, hence D^(-13/40)>dm^13.
assert dm**40 * D < 1

# -------------------------------------------------------------------------
# 2. Recheck the predecessor pointwise positivity Z_old(u)>=0 on
#    0<=u<=43/40.  This is the same sparse exact construction as the
#    predecessor p=33/20 checker, but we stop before its large integral.
# -------------------------------------------------------------------------
U_old = F(43, 40)
T_old = U_old**q
S_MAX = T_old / D

def padd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
        if out[k] == 0:
            del out[k]
    return out

def pmul(a, b):
    out = {}
    for i, x in a.items():
        if not x:
            continue
        for j, y in b.items():
            if y:
                out[i + j] = out.get(i + j, F(0)) + x * y
    return {k: v for k, v in out.items() if v}

# Analytic Frobenius branch A(s)=0F1(; -beta; beta s).
A = {0: F(1)}
term = F(1)
for k in range(1, 6):
    term *= beta / ((F(k - 1) - beta) * k)
    assert term < 0
    A[q * k] = term / D**k
term6 = term * beta / ((F(5) - beta) * 6)
r = beta * S_MAX / ((F(6) - beta) * 7)
assert 0 < r < 1
A[q * 6] = -abs(term6) / (1 - r) / D**6

# Positive nonanalytic branch, predecessor coefficient cold and five terms.
NB = {}
nb = F(1)
for k in range(5):
    if k > 0:
        nb *= beta / ((F(a_num, q) + k) * k)
    deg = a_num + q * k
    NB[deg] = cold * nb * dm**deg
Llo = padd(A, NB)

# Tilt by a positive degree-8 lower Taylor polynomial for exp(s).
E8 = {}
fac = 1
for j in range(9):
    if j > 1:
        fac *= j
    E8[q * j] = F(1, D**j * fac)
Z = pmul(E8, Llo)
Z[0] = Z.get(0, F(0)) - 1
if Z.get(0) == 0:
    del Z[0]

# The predecessor proof factors u^53 and evaluates every negative higher
# monomial at the right endpoint.  The resulting exact margin is positive.
z_margin = Z[a_num]
for deg, coeff in Z.items():
    if deg > a_num and coeff < 0:
        z_margin += coeff * U_old**(deg - a_num)
assert z_margin > 0

# -------------------------------------------------------------------------
# 3. Localized increment.  The true transform coefficient is at least cnew,
# so on top of the predecessor lower transform we gain at least
#   dc * s^(53/40)
# (we deliberately discard the additional positive exp(s) and 0F1 factors).
# Since Z_old>=0, for G=e^s L(s),
#   G^D-1 >= B_old + D*dc*s^(53/40),
# where B_old is the predecessor's six-binomial-layer lower bound.
# Multiplying by e^{-t} and integrating can therefore be added to the old
# certified Jensen-defect floor without recomputing B_old.
#
# Localize to t=u^40, 0<=u<=41/40.  The odd Taylor polynomial W_9(t)
# is a global lower bound for exp(-t) by Taylor's theorem, and after the
# substitution all exponents are integers:
#   int W_9(t) t^{-7/40} dt
#   = 40 sum_{j=0}^9 (-1)^j/j! * U^(33+40j)/(33+40j).
# -------------------------------------------------------------------------
U = F(41, 40)
assert U < U_old
J = F(0)
for j in range(10):
    J += (
        F((-1)**j, factorial(j))
        * 40
        * U**(33 + 40 * j)
        / F(33 + 40 * j)
    )
assert J > 0

# 1/(2 sqrt(pi)) > 500000/1772454, inherited from the exact classical
# rational sqrt(pi) bound already checked in the predecessor chain.
sqrtpi_inv = F(500000, 1772454)
increment = dc * dm**13 * J * sqrtpi_inv
assert increment > 0

# Imported predecessor rational Jensen-defect floor and prefactor upper bound.
delta_floor_old = F(53745767, 10**9)
delta_floor_new = delta_floor_old + increment
base_up = F(7694998, 10**6)

# New finite-D Boolean DTV upper constant.
C_upper = base_up * (1 - delta_floor_new)
old_h = F(728143, 100000)  # 7.28143
h = F(728141, 100000)      # 7.28141
assert C_upper < h
assert old_h - h == F(2, 100000)

# Active-row pruning at n=86: 139 < 86^2/h^2 < 140, so at most 139 rows
# exceed h/sqrt(86); the D=139 real-Boolean DTV theorem handles them.
row_ratio = F(86**2, 1) / (h * h)
assert F(139) < row_ratio < F(140)

print('R13_LOCALIZED_CSTAR_INCREMENT_EXACT_PASS')
print('c_old =', float(cold))
print('c_new =', float(cnew))
print('gautschi_40_margin =', float(c40_lower / cnew**40 - 1))
print('predecessor_Z_margin =', float(z_margin))
print('localized_U =', float(U))
print('localized_T =', float(U**40))
print('localized_J =', float(J))
print('delta_increment =', float(increment))
print('delta_floor_old =', float(delta_floor_old))
print('delta_floor_new =', float(delta_floor_new))
print('base_up =', float(base_up))
print('C_upper =', float(C_upper))
print('old_h =', float(old_h))
print('new_h =', float(h))
print('improvement =', float(old_h - h))
print('row_ratio =', float(row_ratio))
