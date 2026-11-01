from fractions import Fraction as F

# PROB10-10 authoritative exact scalar certificate for the 20260920T0820Z run.
# Consumed theorem dependencies (not recomputed here):
# 1. canonical ten-local-SAW all-length weighted endpoint count with
#       A=3889/2000, B=27893/10000, r=1993/400;
# 2. P04 moving-centered strip theorem
#       mu(e1) <= a_star=294639/500000,
#       E T(0,8N e1) <= 8N a_star + sqrt(N).
# This file certifies the new critical slope bracket, the closed rational
# cone point rho=1.63952, its Chernoff sign, and an explicit finite-scale error.

A=F(3889,2000)
B=F(27893,10000)
r=F(1993,400)
a_star=F(294639,500000)

# Rigorous logarithm bounds for x>1.
def log_bounds_gt1(x,N):
    assert x>1
    z=(x-1)/(x+1)
    L=F(0)
    for k in range(N+1):
        L += F(2)*z**(2*k+1)/F(2*k+1)
    U=L+F(2)*z**(2*N+3)/(F(2*N+3)*(1-z*z))
    return L,U

# Certified bracket for
# rho_* = ((r-1)a_star - log A)/log B.
LA_L,LA_U=log_bounds_gt1(A,20)
LB_L,LB_U=log_bounds_gt1(B,20)
const=(r-1)*a_star
num_L=const-LA_U
num_U=const-LA_L
assert num_L>0 and LB_L>0
rho_star_L=num_L/LB_U
rho_star_U=num_U/LB_L
assert rho_star_L < rho_star_U
assert rho_star_L > F(1639510,1000000)
assert rho_star_U < F(1639511,1000000)

# A clean closed rational cone point strictly above rho_*.
rho=F(10247,6250)             # 1.63952
c=F(3683,6250)                # 0.58928
delta=2*(c-a_star)            # 1/250000
s=F(398250001,100000000)      # r-1 + 1e-8
q=r/(1+s)
beta_hat=F(999999,1000000)
assert rho == F(20494,12500)
assert rho > rho_star_U
assert c>a_star
assert delta == F(1,250000)
assert s > r-1
assert q<1 and q/B<1

# Exact sign: beta(rho)=A^-1 B^-rho exp(sc) q^(1+rho) < beta_hat.
LQ_L,LQ_U=log_bounds_gt1(1/q,4)
LBH_L,LBH_U=log_bounds_gt1(1/beta_hat,4)
logbeta_upper=s*c-LA_L-rho*LB_L-(1+rho)*LQ_L
log_beta_hat_lower=-LBH_U
assert logbeta_upper < log_beta_hat_lower

# Safe all-length startup constant copied from the P04 derivation from the
# canonical ten-local Collatz certificate.
Kbar=F(
    8238929532962105878831551056872795868088655007514624,
    617949527283939289422235868959530625,
)
C=Kbar/(1-q)

# Exact logarithmic proof that beta_hat^700000 < 1/2, avoiding giant powers.
LBH2_L,LBH2_U=log_bounds_gt1(1/beta_hat,4)
L2_L,L2_U=log_bounds_gt1(F(2),20)
assert 700000*LBH2_L > L2_U

# Explicit finite scale.  M is divisible by 4 (axis concatenation) and by
# rho's denominator, so both endpoints are lattice points.
M=10**12
assert M%4==0 and M%6250==0
assert (rho*M).denominator==1
sqrtM=10**6
assert sqrtM*sqrtM==M
# M contains at least 120 disjoint blocks of length 700000, hence
# beta_hat^M <= 2^-120.
assert M >= 120*700000
repair=F(1,2*sqrtM)
exp_error=2*c*C*F(1,2**120)
finite_margin=delta-repair-exp_error
assert finite_margin>0

print("PROB10-10 critical-threshold exact certificate")
print("rho_star_lower_float =",float(rho_star_L))
print("rho_star_upper_float =",float(rho_star_U))
print("rho_star_width_float =",float(rho_star_U-rho_star_L))
print("rho_star > 1.639510 =",rho_star_L > F(1639510,1000000))
print("rho_star < 1.639511 =",rho_star_U < F(1639511,1000000))
print("rho_closed =",rho,"rho_closed_float =",float(rho))
print("c =",c,"a_star =",a_star,"delta =",delta,"delta_float =",float(delta))
print("s =",s,"q_float =",float(q))
print("beta_hat =",beta_hat)
print("logbeta_upper_float =",float(logbeta_upper))
print("log_beta_hat_lower_float =",float(log_beta_hat_lower))
print("beta_exact_sign =",logbeta_upper < log_beta_hat_lower)
print("Kbar_float =",float(Kbar))
print("C_float =",float(C))
print("beta_hat^700000 < 1/2 certificate =",700000*LBH2_L > L2_U)
print("M =",M,"rhoM =",rho*M)
print("repair_float =",float(repair))
print("exp_error_float =",float(exp_error))
print("finite_margin_float =",float(finite_margin))
print("finite_margin_num_bits =",finite_margin.numerator.bit_length(),
      "finite_margin_den_bits =",finite_margin.denominator.bit_length())
print("ALL_EXACT_CHECKS_PASS = True")
