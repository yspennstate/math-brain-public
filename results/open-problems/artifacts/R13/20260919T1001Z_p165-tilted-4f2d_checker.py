from fractions import Fraction as F
from math import comb

# R13 exact checker: p=33/20 cosine-power / tilted-Laplace finite-dimensional
# real-Boolean Komlos upper bound. All acceptance tests use exact rational arithmetic.
D = 139
p = F(33,20)
beta = F(13,40)              # (p-1)/2
a_num = 53                    # a=(p+1)/2=53/40
q = 40                        # substitution t=u^40
N_GAUTSCHI = 2000
U = F(43,40)
T = U**q
S_MAX = T/F(D)
c0 = F(78472,100000)          # strict lower bound for c_*
dm = F(8839437,10**7)        # strict lower bound for D^(-1/40)
old_h = F(728151,100000)      # predecessor 7.28151
h = F(182036,25000)           # 7.28144
TAYLOR_EXP_DEG = 61
BINOMIAL_LEVELS = 6

# Rational constants: pi < 355/113.
# base_p^2 = 9 p^2 pi / (2(p-1)) = (9801/520) pi.
base_up = F(1539,200)         # 7.695
assert base_up**2 > F(9801,520)*F(355,113)
assert F(1772454,10**6)**2 > F(355,113)  # sqrt(pi)<1.772454

# For Y~InvGamma(a=53/40,beta=13/40),
# L(s)=0F1(; -beta; beta s)+c_* s^(53/40)0F1(;93/40;beta s), where
# c_*=beta^(beta-1)/(1+beta)*Gamma(1-beta)/Gamma(beta).
# Let P_N=prod_{k=0}^{N-1}(k+beta)/(k+1-beta).
# Gautschi with x=N-beta and s=2 beta gives
# Gamma(N+1-beta)/Gamma(N+beta) > (N-beta)^(1-2 beta).
# Raising the resulting c_* lower bound to power 40 gives the exact rational inequality
# c_*^40 > beta^(-27) P_N^40 (N-beta)^14 /(1+beta)^40.
P = F(1)
for k in range(N_GAUTSCHI):
    P *= F(40*k+13,40*k+27)
c40_lower = beta**(-27) * P**40 * (F(N_GAUTSCHI)-beta)**14 / (1+beta)**40
assert c40_lower > c0**40

# D^(-1/40) exact lower certificate and integration interval.
assert dm**q * D < 1
assert T < D

# Sparse polynomial helpers in u, where t=u^40 and s=t/D.
def padd(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,F(0))+v
        if out[k]==0:
            del out[k]
    return out

def pmul(a,b):
    out={}
    for i,x in a.items():
        if not x: continue
        for j,y in b.items():
            if y:
                out[i+j]=out.get(i+j,F(0))+x*y
    return {k:v for k,v in out.items() if v}

def pscale(a,c):
    return {k:c*v for k,v in a.items() if c*v}

# Analytic Frobenius branch A(s)=0F1(; -beta; beta s).
# Every nonconstant coefficient is negative for 0<beta<1.
# Keep k=1,...,5 exactly and lower-bound the entire k>=6 tail geometrically.
A={0:F(1)}
term=F(1)
for k in range(1,6):
    term *= beta / ((F(k-1)-beta)*k)
    assert term < 0
    A[q*k] = term / D**k
term6 = term * beta / ((F(5)-beta)*6)
assert term6 < 0
# For k>=6, the absolute consecutive-term ratio is at most this r on s<=S_MAX.
r = beta*S_MAX / ((F(6)-beta)*7)
assert 0 < r < 1
A[q*6] = -abs(term6)/(1-r)/D**6

# Positive nonanalytic branch c_* s^a 0F1(;1+a; beta s), a=53/40.
# Keep k=0,...,4. Since dm<D^(-1/40), dm^(53+40k) is a rigorous
# lower bound for D^(-(a+k)) in every retained positive coefficient.
NB={}
nb=F(1)
for k in range(0,5):
    if k>0:
        nb *= beta / ((F(a_num,q)+k)*k)
    deg=a_num+q*k
    NB[deg] = c0*nb*dm**deg
Llo=padd(A,NB)

# Tilt G(s)=e^s L(s). Degree-8 Taylor polynomial is a positive lower bound for e^s.
E8={}
fac=1
for j in range(9):
    if j>1:
        fac*=j
    E8[q*j]=F(1,D**j*fac)
Z=pmul(E8,Llo)
Z[0]=Z.get(0,F(0))-1
if Z.get(0)==0:
    Z.pop(0,None)
lead=a_num
assert all(deg>=lead for deg in Z)
assert Z[lead]>0

# Pointwise positivity: Z(u)>=z_margin*u^53 on 0<=u<=U.
# Divide by u^53, discard positive higher terms, and evaluate every negative
# higher monomial at its worst endpoint U.
z_margin=Z[lead]
for deg,c in Z.items():
    if deg>lead and c<0:
        z_margin += c*U**(deg-lead)
assert z_margin > 0

# Since G>=1+Z and Z>=0, retain six positive binomial layers of (1+Z)^D-1.
B={}
Zpow={0:F(1)}
for k in range(1,BINOMIAL_LEVELS+1):
    Zpow=pmul(Zpow,Z)
    B=padd(B,pscale(Zpow,F(comb(D,k))))

# The odd Taylor polynomial W_61(t) is a global lower bound for e^{-t} on t>=0.
W={}
fac=1
for j in range(TAYLOR_EXP_DEG+1):
    if j>1:
        fac*=j
    W[q*j]=F((-1)**j,fac)

# Jensen defect:
# 1-E sqrt(X_D)=1/(2sqrt(pi)) int_0^inf [L(t/D)^D-e^{-t}]t^{-3/2}dt.
# On [0,T], L(t/D)^D-e^{-t}=e^{-t}(G(t/D)^D-1).
# If W_61<0, W_61*B is still a valid lower bound because the true integrand
# and B are nonnegative. Under t=u^40, t^{-3/2}dt=40u^{-21}du.
Ppoly=pmul(W,B)
I=F(0)
for deg,coef in Ppoly.items():
    if coef:
        assert deg>20
        I += q*coef*U**(deg-20)/F(deg-20)
assert I > 0

# sqrt(pi)<1.772454 gives 1/(2sqrt(pi))>500000/1772454.
delta = I*F(500000,1772454)
assert 0 < delta < 1

# C_{p,D}=3p sqrt(pi/2)/sqrt(p-1) * E sqrt(X_D), and base_p<7.695.
C_upper = base_up*(1-delta)
assert C_upper < h

# Active-row pruning at n=86. Since 139<86^2/h^2<140, at most 139 rows
# can have Euclidean norm >h/sqrt(86); inactive rows are <=h by Cauchy-Schwarz.
row_ratio = F(86**2,1)/(h*h)
assert F(139) < row_ratio < F(140)

# Exact fixed-metric movement.
improvement = old_h-h
assert improvement == F(7,100000)

print('R13_P165_TILTED_EXACT_PASS')
print('p =',p)
print('D =',D)
print('n =',86)
print('c0_lower =',float(c0))
print('gautschi_40_margin =',float(c40_lower/c0**40-1))
print('D_minus_1_over_40_lower =',float(dm))
print('T =',float(T))
print('S_max =',float(S_MAX))
print('Z_factor_margin =',float(z_margin))
print('binomial_levels =',BINOMIAL_LEVELS)
print('exp_lower_taylor_degree =',TAYLOR_EXP_DEG)
print('exact_integral_I =',float(I))
print('delta_lower =',float(delta))
print('base_upper =',float(base_up))
print('C_upper =',float(C_upper))
print('h =',float(h))
print('row_ratio =',float(row_ratio))
print('old_B86 =',float(old_h))
print('new_B86 =',float(h))
print('improvement =',float(improvement))
