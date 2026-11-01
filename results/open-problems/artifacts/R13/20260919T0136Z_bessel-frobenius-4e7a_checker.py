from fractions import Fraction as F
from math import comb

# R13 exact-arithmetic checker for the p=9/5 cosine-power / Bessel-Frobenius
# finite-dimensional Komlos sharpening.  All acceptance tests are rational.

D = 138
N_GAUTSCHI = 1000
M_EXP = 500
U = F(5,4)
T = U**10
c0 = F(8309,10000)
dm = F(139331196,10**9)   # strict lower bound for 138^(-2/5)
h = F(72991,10000)
old_B86 = F(739097,100000)

# elementary rational upper bounds on sqrt(pi) and sqrt(10 pi), using pi < 355/113
assert F(1773,1000)**2 > F(355,113)
assert F(1121,200)**2 > F(3550,113)

# Exact lower bound c_* > 8309/10000 for
# c_*=(25/14) Gamma(3/5)/Gamma(2/5) (2/5)^(2/5).
# Gautschi at x=N-2/5, s=4/5 gives
# Gamma(3/5)/Gamma(2/5) > P_N (N-2/5)^(1/5),
# P_N=prod_{k=0}^{N-1}(5k+2)/(5k+3).
P = F(1)
for k in range(N_GAUTSCHI):
    P *= F(5*k+2, 5*k+3)
lhs5 = (F(25,14)*P)**5 * (F(N_GAUTSCHI)-F(2,5)) * F(2,5)**2
rhs5 = c0**5
assert lhs5 > rhs5

# Exact D^{-2/5} lower bound.
assert dm**5 * D**2 < 1

# Analytic 0F1 tail: after the -s^3/36 term, the absolute-term ratio
# is at most s/26.  On 0 <= t <= T and s=t/D, this gives a rational
# cubic-tail coefficient k3.
k3 = F(1,36) / (1 - T/F(26*D))
assert T < F(D,10)  # in particular s<1/10
assert c0 - F(1,3) - k3 > 0  # crude q(s)>0 for 0<s<1


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

# Put t=u^10.  The lower exponent is built as follows.
# q(s) >= c0*s^(7/5) - s^2/3 - k3*s^3,
# y=s-q.  With log(1-y)>=-y-y^2/(2(1-y)) and t<=T,
# D log L(t/D)+t >= D q - D^2*y^2/(2(D-T)).
Dq=[F(0)]*31
Dq[14]=c0*dm
Dq[20]=-F(1,3*D)
Dq[30]=-k3/F(D*D)

y=[F(0)]*31
y[10]=F(1,D)
y[14]=-c0*dm/F(D)
y[20]=F(1,3*D*D)
y[30]=k3/F(D**3)

R=padd(Dq, pscale(pmul(y,y), -F(D*D,2)/(F(D)-T)))

# Exact positivity on 0<=u<=U: divide by u^14, discard all positive
# non-leading terms, and put every negative monomial at its worst endpoint.
pos_margin=R[14]
for i in range(15,len(R)):
    if R[i] < 0:
        pos_margin += R[i]*U**(i-14)
assert pos_margin > 0

# e^R-1 >= R+R^2/2 and e^{-t} >= (1-t/M)^M for 0<=t<T<M.
# After t=u^10, t^{-3/2}dt=10 u^{-6}du, so the integral is an
# ordinary rational polynomial integral.
Q=padd(R, pscale(pmul(R,R),F(1,2)))
W=[F(0)]*(10*M_EXP+1)
for k in range(M_EXP+1):
    W[10*k]=F(comb(M_EXP,k))*(-F(1,M_EXP))**k
Ppoly=pmul(W,Q)
I=F(0)
for deg,coef in enumerate(Ppoly):
    if coef:
        assert deg>=14
        I += 10*coef*U**(deg-5)/F(deg-5)
assert I > 0

# delta = 1-E sqrt(X_D) > I/(2 sqrt(pi)); sqrt(pi)<1773/1000.
delta=I*F(500,1773)
# C_D < (27/20)*(1121/200)*(1-delta).
C_upper=F(27,20)*F(1121,200)*(1-delta)
assert C_upper < h

# Row-pruning check for n=86: active-row count d < n^2/h^2, and this
# exact ratio lies strictly between 138 and 139, hence d<=138.
row_ratio=F(86**2,1)/(h*h)
assert F(138) < row_ratio < F(139)
assert old_B86 > h
improvement=old_B86-h
assert improvement == F(9187,100000)

print('R13_BESSEL_FROBENIUS_EXACT_PASS')
print('D =',D)
print('n =',86)
print('c0_lower =',float(c0))
print('gautschi_fifth_power_margin =',float(lhs5/rhs5-1))
print('D_minus_2_over_5_lower =',float(dm))
print('T =',float(T))
print('positivity_margin_factor =',float(pos_margin))
print('exact_integral_I =',float(I))
print('delta_lower =',float(delta))
print('C_upper =',float(C_upper))
print('h =',float(h))
print('row_ratio =',float(row_ratio))
print('old_B86 =',float(old_B86))
print('new_B86 =',float(h))
print('improvement =',float(improvement))
