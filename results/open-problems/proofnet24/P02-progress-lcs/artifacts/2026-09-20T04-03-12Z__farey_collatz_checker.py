from fractions import Fraction
from math import gcd

# Exact inherited C045/P02 data.
t = Fraction(256717, 800000)
q0 = 800000
p0 = 256717
S = q0**6 * (q0-p0)
a = 1995237757733917147310102692686664915858011319606812684127301
b = 4220452010631561279
M = 5000000000000000000

R = Fraction(a,b)
x = Fraction(a*a-1,b*b)  # two-step Collatz square-rate bound

# Exact Farey bounds around a positive rational x with denominator cap N.
def farey_bounds(x, N):
    n, d = x.numerator, x.denominator
    p0,q0,p1,q1 = 0,1,1,0
    while True:
        aa = n//d
        q2 = q0 + aa*q1
        if q2 > N:
            break
        p0,q0,p1,q1 = p1,q1,p0+aa*p1,q2
        n,d = d,n-aa*d
    k=(N-q0)//q1
    z1=Fraction(p0+k*p1,q0+k*q1)
    z2=Fraction(p1,q1)
    lo=max(z for z in (z1,z2) if z < x)
    hi=min(z for z in (z1,z2) if z > x)
    return lo,hi

lo,hi = farey_bounds(x,M)
assert x.denominator > M
assert lo < x < hi
assert hi.numerator*lo.denominator - lo.numerator*hi.denominator == 1
assert lo.denominator + hi.denominator > M

# Hence any rational with denominator <=M strictly below x is <=lo.
# Apply to each exact row ratio (B^2 V)_i/V_i.
Delta = R*R - lo
assert Delta > Fraction(1,b*b)

# Rational square-root majorant.  beta_F^2 = lo + Delta^2/(4R^2) > lo.
beta_F = R - Delta/(2*R)
assert beta_F > 0
assert beta_F*beta_F > lo

# Previous two-step rational rate bound.
beta_2 = R - Fraction(1,2*a*b)
assert beta_F < beta_2 < R

# Exact improvement factor in the B-rate gap.
improvement = (R-beta_F)/(R-beta_2)
assert improvement == Fraction(168660543882229665139,4939678005094299958)
assert improvement > 34

# Back to the C045 operator A=(t^2/S)B.
lambda_F = t*t*beta_F/Fraction(S,1)
lambda_2 = t*t*beta_2/Fraction(S,1)
assert 0 < lambda_F < lambda_2 < 1
base = 4*t*t
assert 0 < base < 1

# Rigorous -log bounds from the positive atanh series.
def neglog_bounds(z,K=300):
    assert 0 < z < 1
    u=(1-z)/(1+z)
    u2=u*u
    s=Fraction(0,1)
    upow=u
    for m in range(K):
        s += 2*upow/Fraction(2*m+1,1)
        upow *= u2
    tail = 2*upow/Fraction(2*K+1,1)/(1-u2)
    return s,s+tail

Alo,Ahi = neglog_bounds(base)
LFlo,LFhi = neglog_bounds(lambda_F)
L2lo,L2hi = neglog_bounds(lambda_2)

UFlo,UFhi = Alo/LFhi, Ahi/LFlo
U2lo,U2hi = Alo/L2hi, Ahi/L2lo
assert UFhi < U2lo

# A 121-decimal rational separator Q with U_F < Q < U_2.
D=121
scale=10**D
n=(UFhi.numerator*scale + UFhi.denominator-1)//UFhi.denominator
Q=Fraction(n,scale)
assert UFhi < Q < U2lo

def dec_fraction(fr, digits=60):
    # diagnostic only; integer long division, no floating point.
    n,d=fr.numerator,fr.denominator
    sign='-' if n<0 else ''
    n=abs(n)
    i,r=divmod(n,d)
    out=[]
    for _ in range(digits):
        r*=10
        z,r=divmod(r,d)
        out.append(str(z))
    return f"{sign}{i}."+''.join(out)

print("P02 T02 Farey-Collatz exact checker")
print("x_reduced_den=",x.denominator)
print("M=",M)
print("farey_lo_num=",lo.numerator)
print("farey_lo_den=",lo.denominator)
print("farey_hi_num=",hi.numerator)
print("farey_hi_den=",hi.denominator)
print("farey_det=",hi.numerator*lo.denominator-lo.numerator*hi.denominator)
print("farey_den_sum=",lo.denominator+hi.denominator)
print("farey_den_sum_gt_M=",lo.denominator+hi.denominator>M)
print("gap_x_minus_lo_num=", (x-lo).numerator)
print("gap_x_minus_lo_den=", (x-lo).denominator)
print("beta_gap_improvement_num=",improvement.numerator)
print("beta_gap_improvement_den=",improvement.denominator)
print("beta_gap_improvement_gt_34=",improvement>34)
print("lambda_F_lt_lambda_2=",lambda_F<lambda_2)
qdigits=str(n).rjust(D,'0')
print("separator_Q=0."+qdigits)
print("UF_lt_Q_lt_U2_exact=",UFhi<Q<U2lo)
print("UF_upper_diag=",dec_fraction(UFhi,135))
print("U2_lower_diag=",dec_fraction(U2lo,135))
print("EXACT_FAREY_PREDECESSOR_CERTIFICATE_PASS")
print("EXACT_SPECTRAL_STRICTIFICATION_PASS")
print("EXACT_LOG_SEPARATOR_PASS")
print("SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS")
print("ALL_EXACT_CHECKS_PASS")
