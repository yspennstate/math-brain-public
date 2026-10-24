from fractions import Fraction as F
from math import comb

# R13 exact-arithmetic checker: p=5/3 tilted-transform / binomial-cascade
# finite-dimensional Boolean Komlos sharpening. All acceptance tests are exact.

D = 139
N_GAUTSCHI = 20000
U = F(33, 20)
T = U**6
S_MAX = T/F(D)
c0 = F(788557, 10**6)       # strict lower bound for the nonanalytic coefficient c_*
dm = F(193046411, 10**9)   # strict lower bound for 139^(-1/3)
old_h = F(45541, 6250)       # predecessor 7.28656
h = F(728151, 100000)        # new 7.28151
TAYLOR_EXP_DEG = 81          # odd => global lower Taylor polynomial for exp(-t)
BINOMIAL_LEVELS = 10

# Rational square-root bounds from pi < 355/113.
assert F(1772454, 10**6)**2 > F(355, 113)       # sqrt(pi) < 1.772454
assert F(3069981, 10**6)**2 > F(1065, 113)      # sqrt(3*pi) < 3.069981

# At p=5/3, Y~InvGamma(4/3,1/3) and
# L(s)=0F1(; -1/3; s/3)+c_* s^(4/3) 0F1(;7/3;s/3),
# c_*=(27/4)3^(-4/3) Gamma(2/3)/Gamma(1/3).
# Gautschi with P_N=prod_{k=0}^{N-1}(3k+1)/(3k+2) yields
# c_*^3 > (243/64) P_N^3 (N-1/3).
P = F(1)
for k in range(N_GAUTSCHI):
    P *= F(3*k+1, 3*k+2)
c3_lower = F(243, 64) * P**3 * (F(N_GAUTSCHI)-F(1,3))
assert c3_lower > c0**3

# Exact D^(-1/3) lower certificate.
assert dm**3 * D < 1
assert T < D

# Polynomial helpers in u after t=u^6, s=t/D.
def padd(a,b):
    n=max(len(a),len(b)); out=[F(0)]*n
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return out

def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b):
            if y: out[i+j]+=x*y
    return out

def pscale(a,c):
    return [c*x for x in a]

# Analytic branch A(s)=0F1(; -1/3;s/3):
# A(s)=1-s-s^2/4-s^3/60-s^4/1920-s^5/105600-s^6/8870400-...
# Every nonconstant coefficient is negative. For k>=6,
# |term_{k+1}|/|term_k| = s/((3k-1)(k+1)) <= S_MAX/119.
kappa6 = F(1, 8870400) / (1-S_MAX/F(119))
A=[F(0)]*37
A[0]=F(1)
A[6]=-F(1,D)
A[12]=-F(1,4*D**2)
A[18]=-F(1,60*D**3)
A[24]=-F(1,1920*D**4)
A[30]=-F(1,105600*D**5)
A[36]=-kappa6/F(D**6)

# Positive nonanalytic branch. Keep
# 0F1(;7/3;s/3) >= 1+s/7+s^2/140+s^3/5460+s^4/349440.
# Since s^(4/3)=u^8 D^(-4/3), powers of dm rigorously lower all positive terms.
NB=[F(0)]*57
NB[8]=c0*dm**4
NB[14]=c0*dm**7/F(7)
NB[20]=c0*dm**10/F(140)
NB[26]=c0*dm**13/F(5460)
NB[32]=c0*dm**16/F(349440)
Llo=padd(A,NB)

# Method #18: tilt the Laplace transform G(s)=e^s L(s).
# e^s is bounded below by its degree-8 Taylor polynomial E8(s).
E8=[F(0)]*49
fac=1
for j in range(9):
    if j>1: fac*=j
    E8[6*j]=F(1,D**j*fac)

# Since L(s)>=Llo(s), L(s)>0, and e^s>=E8(s)>0,
# e^s L(s) >= E8(s)Llo(s) = 1+Z(u).
Z=pmul(E8,Llo)
Z[0]-=1

# Method #3: certify the stronger pointwise statement Z(u)>=0 on all 0<=u<=U.
# Divide by the leading u^8, discard every positive higher monomial, and put every
# negative higher monomial at its worst endpoint U.
z_margin=Z[8]
for i in range(9,len(Z)):
    if Z[i] < 0:
        z_margin += Z[i]*U**(i-8)
assert z_margin > 0

# Method #25: count the positive binomial layers. Since Z>=0,
# (1+Z)^D-1 >= sum_{k=1}^{10} binom(D,k) Z^k.
B=[F(0)]
Zpow=[F(1)]
for k in range(1,BINOMIAL_LEVELS+1):
    Zpow=pmul(Zpow,Z)
    B=padd(B,pscale(Zpow,F(comb(D,k))))

# Global lower Taylor polynomial for e^{-t}. Taylor's theorem gives, for odd m,
# e^{-t} >= sum_{j=0}^m (-t)^j/j! for every t>=0.
W=[F(0)]*(6*TAYLOR_EXP_DEG+1)
fac=1
for j in range(TAYLOR_EXP_DEG+1):
    if j>1: fac*=j
    W[6*j]=F((-1)**j,fac)

# Jensen defect:
# 1-E sqrt(X_D)=1/(2sqrt(pi)) int_0^inf [L(t/D)^D-e^{-t}] t^{-3/2}dt.
# On 0<=t<=T,
# L(t/D)^D-e^{-t} = e^{-t}[(e^{t/D}L(t/D))^D-1].
# With Z>=0 and the odd Taylor lower bound, the integrated polynomial below
# is a rigorous lower bound (if W becomes negative, the true integrand is nonnegative,
# so W*B remains a valid lower bound there as well).
Ppoly=pmul(W,B)
I=F(0)
for deg,coef in enumerate(Ppoly):
    if coef:
        assert deg>=8
        I += 6*coef*U**(deg-3)/F(deg-3)
assert I > 0

# sqrt(pi)<1.772454 => 1/(2sqrt(pi)) > 500000/1772454.
delta=I*F(500000,1772454)

# C_{5/3,139}=(5/2)sqrt(3*pi) E sqrt(X_D), sqrt(3*pi)<3.069981.
C_upper=F(5,2)*F(3069981,10**6)*(1-delta)
assert C_upper < h

# Row pruning at n=86. If rows with norm > h/sqrt(86) are active,
# d < 86^2/h^2. The exact ratio lies in (139,140), hence d<=139.
row_ratio=F(86**2,1)/(h*h)
assert F(139) < row_ratio < F(140)

# Exact fixed-metric movement.
improvement=old_h-h
assert improvement == F(101,20000)  # 0.00505

print('R13_TILTED_BINOMIAL_EXACT_PASS')
print('D =',D)
print('n =',86)
print('c0_lower =',float(c0))
print('gautschi_cube_margin =',float(c3_lower/c0**3-1))
print('D_minus_1_over_3_lower =',float(dm))
print('T =',float(T))
print('S_max =',float(S_MAX))
print('Z_factor_margin =',float(z_margin))
print('binomial_levels =',BINOMIAL_LEVELS)
print('exp_lower_taylor_degree =',TAYLOR_EXP_DEG)
print('exact_integral_I =',float(I))
print('delta_lower =',float(delta))
print('C_upper =',float(C_upper))
print('h =',float(h))
print('row_ratio =',float(row_ratio))
print('old_B86 =',float(old_h))
print('new_B86 =',float(h))
print('improvement =',float(improvement))
