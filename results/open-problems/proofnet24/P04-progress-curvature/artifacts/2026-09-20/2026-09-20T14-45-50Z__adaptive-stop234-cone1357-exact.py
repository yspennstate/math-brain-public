from fractions import Fraction as F
from math import factorial

# Rigorous scalar checker for P04 adaptive stopping + canonical 10-local SAW compiler.
A=F(3889,2000)
B=F(27893,10000)
r=F(1993,400)
a=F(16139,31250)           # 0.516448, certified by C++ finite core
Q=10**15
rootW=2065789747160742
xi2=F(2334416160657687,10**15)
assert F(rootW,Q) < 4*a

# log bounds for x>1 via atanh series; returns exact rational [lo,hi].
def log_gt1_bounds(x, N=120):
    assert x>1
    z=(x-1)/(x+1)
    s=F(0)
    p=z
    z2=z*z
    for k in range(N):
        s += p/F(2*k+1)
        p *= z2
    lo=2*s
    # tail <= 2 z^(2N+1)/((2N+1)(1-z^2))
    tail=2*p/F((2*N+1),1)/(1-z2)
    hi=lo+tail
    return lo,hi

def log_bounds(x,N=120):
    if x==1: return F(0),F(0)
    if x>1: return log_gt1_bounds(x,N)
    lo,hi=log_gt1_bounds(1/x,N)
    return -hi,-lo

LAlo,LAhi=log_bounds(A)
LBlo,LBhi=log_bounds(B)
assert LAlo>0 and LBlo>0

# critical slope bracket: rho*=((r-1)a-log A)/log B
rho_lo=F(13567576,10**7)
rho_hi=F(13567577,10**7)
target=(r-1)*a
# For rho_lo < rho*, it suffices logA + rho_lo logB < target using upper bounds.
assert LAhi + rho_lo*LBhi < target
# For rho* < rho_hi, it suffices logA + rho_hi logB > target using lower bounds.
assert LAlo + rho_hi*LBlo > target

# Clean closed cone constants.
rho0=F(1357,1000)
c=F(51647,100000)
s=F(19913,5000)
q=r/(1+s)
assert q<1 and c>a
base=F(9999,10000)

# log beta = -logA-rho logB+s c +(1+rho)log q.
# Rigorous upper bound uses lower bounds for positive logs A,B,1/q.
Linvq_lo,Linvq_hi=log_bounds(1/q)
logbeta_hi = -LAlo-rho0*LBlo+s*c-(1+rho0)*Linvq_lo
Lbase_lo,Lbase_hi=log_bounds(base)
assert logbeta_hi < Lbase_lo

# Exact defect from reflected lower bounds versus axis upper cap.
delta=2*(c-a)
assert delta==F(11,250000)

# Canonical all-length prefactor.
Kbar=F(44100*10**14,1)*(B/r)**10
C=Kbar/(1-q)
assert C < 7*10**20

# Explicit finite scale. For oblique x-coordinate m and axis endpoint 2m:
# R/m >= delta - 2 c C base^m - sqrt(xi2*(m-1))/m - 3/m.
m=10**10
endpoint=F(153,10**7)   # 1.53e-5
assert xi2*(m-1)*endpoint.denominator**2 < endpoint.numerator**2*m*m
horizontal=F(3,m)

# base^m <= exp(-m/10000)=exp(-10^6), and exp(-X)<=50!/X^50.
tail=2*c*C*F(factorial(50),10**300)
assert tail < F(1,10**100)
residual_lower=delta-endpoint-horizontal-F(1,10**100)
assert residual_lower > F(28,10**6)

print('ALL_EXACT_CHECKS_PASS = True')
print('axis_cap_a =', a, float(a))
print('root_transformed_upper =', F(rootW,Q), float(F(rootW,Q)))
print('four_a_minus_root =', 4*a-F(rootW,Q), float(4*a-F(rootW,Q)))
print('xi2_upper =', xi2, float(xi2))
print('rho_star_bracket =', float(rho_lo), float(rho_hi))
print('closed_cone_rho0 =', rho0, float(rho0))
print('c =', c, float(c))
print('q =', q, float(q))
print('beta_log_upper_lt_log_9999_10000 = True')
print('delta =', delta, float(delta))
print('C_upper_check_lt_7e20 =', C < 7*10**20)
print('finite_m =', m)
print('endpoint_error_upper =', endpoint, float(endpoint))
print('horizontal_error_upper =', horizontal, float(horizontal))
print('tail_error_upper_lt_1e-100 =', tail < F(1,10**100))
print('finite_residual_lower_gt_2p8e-5 =', residual_lower > F(28,10**6))
print('finite_residual_lower_decimal =', float(residual_lower))
