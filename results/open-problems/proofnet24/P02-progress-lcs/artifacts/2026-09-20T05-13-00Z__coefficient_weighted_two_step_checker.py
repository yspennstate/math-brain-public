from fractions import Fraction
from math import gcd

# Inherited exact C045 primitive scaling.
p = 256717
q = 800000
M = 5_000_000_000_000_000_000
a = int("1995237757733917147310102692686664915858011319606812684127301")
b = int("4220452010631561279")
S = q**6 * (q-p)

assert gcd(a,b) == 1
assert b <= M < 2*b

# A=t^2 H, B=S H. Each nonzero entry of B is a sum of these
# primitive positive label coefficients.
coeff = [q**(6-k)*(q-p)*p**k for k in range(7)] + [p**7]
m0 = min(coeff)
assert m0 == p**7
assert a >= m0*M

R = Fraction(a,b)
t = Fraction(p,q)
scale = t*t / S
base = 4*t*t
assert 0 < base < 1

# Recover the current P02 Farey certificate from the exact one-step rate.
def farey_bounds(frac, max_den):
    n,d = frac.numerator, frac.denominator
    assert d > max_den
    p0,q0,p1,q1 = 0,1,1,0
    nn,dd = n,d
    while True:
        aa = nn//dd
        q2 = q0 + aa*q1
        if q2 > max_den:
            break
        p0,q0,p1,q1 = p1,q1,p0+aa*p1,q2
        nn,dd = dd,nn-aa*dd
    k = (max_den-q0)//q1
    f1 = Fraction(p0+k*p1,q0+k*q1)
    f2 = Fraction(p1,q1)
    lo,hi = (f1,f2) if f1 < f2 else (f2,f1)
    assert lo < frac < hi
    assert lo.denominator <= max_den and hi.denominator <= max_den
    assert hi.numerator*lo.denominator - lo.numerator*hi.denominator == 1
    assert lo.denominator + hi.denominator > max_den
    return lo,hi

xF = R*R
lF,hF = farey_bounds(xF,M)
DeltaF = xF-lF
betaF = R - DeltaF/(2*R)
lambdaF = scale*betaF

# New coefficient-weighted two-step theorem.
#
# With s_i = a V_i - b(BV)_i >= 0,
# a^2 V_i - b^2(B^2V)_i
#   = a s_i + b sum_j B_ij s_j.
#
# If s_i>0, the RHS is >=a>=m0*M>=m0*V_i.
# If s_i=0, then b|V_i and b<=M<2b, hence V_i=b.
# If every positive successor also had zero slack, all successor V_j=b,
# so (BV)_i would be divisible by b; but tightness gives (BV)_i=a,
# contradicting gcd(a,b)=1 and b>1. Thus a positive successor has
# slack >=1, and every positive B_ij>=m0, giving RHS>=b*m0=m0*V_i.
#
# Therefore B^2 V <= ((a^2-m0)/b^2)V. By concavity of sqrt,
# sqrt(R^2-m0/b^2) < R-m0/(2ab) = betaW.
betaW = R - Fraction(m0,2*a*b)
lambdaW = scale*betaW
assert betaW*betaW > R*R - Fraction(m0,b*b)
assert 0 < lambdaW < lambdaF < 1

improvement_factor = (R-betaW)/(R-betaF)
assert improvement_factor > 10**36

# Exact positive atanh-series enclosures for the endpoint separator.
def neglog_bounds(z, K=160):
    assert 0 < z < 1
    u = (1-z)/(1+z)
    u2 = u*u
    pw = u
    s = Fraction(0,1)
    for k in range(K):
        s += 2*pw/Fraction(2*k+1,1)
        pw *= u2
    tail = 2*pw/Fraction(2*K+1,1)/(1-u2)
    return s, s+tail

Alo,Ahi = neglog_bounds(base)
FWlo,FWhi = neglog_bounds(lambdaF)
WWlo,WWhi = neglog_bounds(lambdaW)

# 84-decimal rational strictly between the new and old source endpoints.
Q = Fraction(
    826275942762282625015106581537296632823461996193190023880806183312562944430299564492,
    10**84
)
U_W_upper = Ahi/WWlo
U_F_lower = Alo/FWhi
assert U_W_upper < Q < U_F_lower

print("P02 T02 coefficient-weighted two-step checker")
print(f"S={S}")
print("primitive_coefficients=" + ",".join(str(x) for x in coeff))
print(f"m0={m0}")
print(f"a_ge_m0M={a >= m0*M}")
print(f"betaW_num={betaW.numerator}")
print(f"betaW_den={betaW.denominator}")
print(f"improvement_factor_num={improvement_factor.numerator}")
print(f"improvement_factor_den={improvement_factor.denominator}")
print(f"Q_num={Q.numerator}")
print(f"Q_den={Q.denominator}")
print("EXACT_MIN_POSITIVE_COEFFICIENT_PASS")
print("EXACT_WEIGHTED_TWO_STEP_CONSTANTS_PASS")
print("EXACT_RATE_BEATS_CURRENT_FAREY_PASS")
print("EXACT_LOG_SEPARATOR_PASS")
print("SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS")
print("ALL_EXACT_CHECKS_PASS")
