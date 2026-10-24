from fractions import Fraction as F
from math import comb

# R13 exact-arithmetic checker for the p=5/3 cosine-power
# Bessel/Frobenius finite-dimensional Boolean Komlos sharpening.
# Every acceptance test below is exact rational arithmetic.

D = 139
N_GAUTSCHI = 1000
M_EXP = 1000
U = F(33, 20)
T = U**6
c0 = F(78847, 100000)          # strict lower bound for the nonanalytic coefficient c_*
dm = F(193046, 10**6)          # strict lower bound for 139^(-1/3)
h = F(45541, 6250)             # 7.28656
old_B86 = F(72991, 10000)      # predecessor 7.29910

# Elementary rational bounds derived from pi < 355/113.
assert F(1773,1000)**2 > F(355,113)       # sqrt(pi) < 1.773
assert F(307,100)**2 > F(1065,113)        # sqrt(3*pi) < 3.07

# For p=5/3, a=4/3 and beta=1/3:
# L(s)=0F1(; -1/3; s/3) + c_* s^(4/3) 0F1(; 7/3; s/3),
# c_*=(27/4) 3^(-4/3) Gamma(2/3)/Gamma(1/3).
#
# Set P_N=prod_{k=0}^{N-1}(3k+1)/(3k+2).
# Gautschi with x=N-1/3, s=2/3 gives
# Gamma(2/3)/Gamma(1/3) > P_N (N-1/3)^(1/3).
# Cubing yields c_*^3 > (243/64) P_N^3 (N-1/3).
P = F(1)
for k in range(N_GAUTSCHI):
    P *= F(3*k+1, 3*k+2)
c3_lower = F(243,64) * P**3 * (F(N_GAUTSCHI)-F(1,3))
assert c3_lower > c0**3

# Exact lower bound D^(-1/3) > dm.
assert dm**3 * D < 1

# The analytic branch is
# 0F1(; -1/3; s/3)=1-s-s^2/4-s^3/60-...
# and after the s^3/60 term the absolute-term ratio is at most s/32.
# Since s=t/D <= T/D, all remaining negative terms are bounded by k3*s^3.
k3 = F(1,60) / (1 - T/F(32*D))
assert T < D
assert T < M_EXP

def padd(a,b):
    n=max(len(a),len(b)); out=[F(0)]*n
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return out

def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if not x:
            continue
        for j,y in enumerate(b):
            if y:
                out[i+j]+=x*y
    return out

def pscale(a,c):
    return [c*x for x in a]

def ppow(a,k):
    out=[F(1)]
    for _ in range(k):
        out=pmul(out,a)
    return out

# Put t=u^6.  Using also the first positive term
# 0F1(;7/3;s/3) >= 1+s/7, define a rigorous lower q by
# L(t/D) >= 1 - t/D + q_lower(t).
#
# D*q_lower has:
# c0 D^(-1/3) t^(4/3)
# + (c0/7) D^(-4/3) t^(7/3)
# - t^2/(4D)
# - k3 t^3/D^2.
Dq=[F(0)]*19
Dq[8]=c0*dm
Dq[14]=c0*dm**4/F(7)
Dq[12]=-F(1,4*D)
Dq[18]=-k3/F(D*D)

# y_bar = t/D - q_lower, so L(t/D) >= 1-y_bar.
y=[F(0)]*19
y[6]=F(1,D)
y[8]=-c0*dm/F(D)
y[14]=-c0*dm**4/F(7*D)
y[12]=F(1,4*D*D)
y[18]=k3/F(D**3)

# Certify 0 <= y_bar <= t/D < 1:
# q_lower >=0 gives the upper inequality, and the direct factor bound gives y_bar>=0.
q_factor_min=Dq[8]
for i in range(9,len(Dq)):
    if Dq[i] < 0:
        q_factor_min += Dq[i]*U**(i-8)
assert q_factor_min > 0

y_factor_min=y[6]
for i in range(7,len(y)):
    if y[i] < 0:
        y_factor_min += y[i]*U**(i-6)
assert y_factor_min > 0
assert T/F(D) < 1

# Sharper log lower bound:
# log(1-y) >= -y-y^2/2-y^3/3-y^4/4-y^5/[5(1-y)].
# Since y<=t/D<=T/D, 1/(1-y)<=D/(D-T).
# Therefore D log L(t/D)+t >= R(t), where
# R = Dq - D*y^2/2 - D*y^3/3 - D*y^4/4
#     - D^2*y^5/[5(D-T)].
R=Dq[:]
for k in range(2,5):
    R=padd(R, pscale(ppow(y,k), -F(D,k)))
R=padd(R, pscale(ppow(y,5), -F(D*D,5)/(F(D)-T)))

# Exact positivity on 0<=u<=U:
# divide by u^8, discard every positive non-leading monomial,
# and place each negative monomial at its worst endpoint U.
pos_margin=R[8]
for i in range(9,len(R)):
    if R[i] < 0:
        pos_margin += R[i]*U**(i-8)
assert pos_margin > 0

# Jensen-defect identity:
# 1-E sqrt(X_D)
# = 1/(2 sqrt(pi)) int_0^inf [L(t/D)^D-e^(-t)] t^(-3/2) dt.
#
# On [0,T], use e^R-1 >= R+R^2/2 and
# e^(-t) >= (1-t/M)^M.
Q=padd(R, pscale(pmul(R,R),F(1,2)))
W=[F(0)]*(6*M_EXP+1)
for k in range(M_EXP+1):
    W[6*k]=F(comb(M_EXP,k))*(-F(1,M_EXP))**k
Ppoly=pmul(W,Q)

# With t=u^6, t^(-3/2)dt = 6u^(-4)du.
I=F(0)
for deg,coef in enumerate(Ppoly):
    if coef:
        assert deg >= 8
        I += 6*coef*U**(deg-3)/F(deg-3)
assert I > 0

# sqrt(pi)<1773/1000 gives delta > I*500/1773.
delta=I*F(500,1773)

# For p=5/3, the Boolean DTV cube half-side is
# C_D = (5/2) sqrt(3*pi) E sqrt(X_D).
# sqrt(3*pi)<307/100 gives C_D < (1535/200)(1-delta).
C_upper=F(1535,200)*(1-delta)
assert C_upper < h

# Row-pruning at n=86.  If rows with norm > h/sqrt(86) are active,
# d < 86^2/h^2.  The exact ratio lies in (139,140), so d<=139.
row_ratio=F(86**2,1)/(h*h)
assert F(139) < row_ratio < F(140)

# Exact metric movement.
assert old_B86 > h
improvement=old_B86-h
assert improvement == F(627,50000)  # 0.01254

print('R13_P53_FROBENIUS_EXACT_PASS')
print('D =',D)
print('n =',86)
print('c0_lower =',float(c0))
print('gautschi_cube_margin =',float(c3_lower/c0**3-1))
print('D_minus_1_over_3_lower =',float(dm))
print('T =',float(T))
print('q_factor_min =',float(q_factor_min))
print('y_factor_min =',float(y_factor_min))
print('R_positivity_margin_factor =',float(pos_margin))
print('exact_integral_I =',float(I))
print('delta_lower =',float(delta))
print('C_upper =',float(C_upper))
print('h =',float(h))
print('row_ratio =',float(row_ratio))
print('old_B86 =',float(old_B86))
print('new_B86 =',float(h))
print('improvement =',float(improvement))
