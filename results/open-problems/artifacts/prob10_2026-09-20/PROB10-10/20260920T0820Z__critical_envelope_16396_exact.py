from fractions import Fraction as F

# PROB10-10 exact recombination certificate.
# Dependencies consumed, not re-proved here:
# (i) canonical ten-local-SAW weighted endpoint-count theorem:
#     A=3889/2000, B=27893/10000, r=1993/400;
# (ii) P04 moving-centered strip theorem:
#     mu(e1) <= a_star=294639/500000 and
#     E T(0,8N e1) <= 8N a_star + sqrt(N).
#
# This checker certifies only the new scalar Chernoff/log comparisons,
# the restricted strict-triangle defect, and one explicit finite-scale residual.

A=F(3889,2000)
B=F(27893,10000)
r=F(1993,400)
s=F(3982501,1000000)
q=r/(1+s)
c=F(73661,125000)
rho=F(4099,2500)
beta_hat=F(99997,100000)
a_star=F(294639,500000)

assert c-a_star == F(1,100000)
assert q == F(4982500,4982501)
assert q < 1
assert q/B < 1
assert rho < F(41,25)

# Safe all-length startup constant from the neighboring P04 report,
# derived there from the canonical ten-local Collatz certificate.
Kbar=F(
    8238929532962105878831551056872795868088655007514624,
    617949527283939289422235868959530625,
)
C=Kbar/(1-q)

# Rigorous log bounds for x>1:
# log x = 2 sum_{k>=0} z^(2k+1)/(2k+1), z=(x-1)/(x+1).
# Partial sum is a lower bound; tail is bounded geometrically.
def log_bounds_gt1(x,N):
    assert x>1
    z=(x-1)/(x+1)
    L=F(0)
    for k in range(N+1):
        L += F(2)*z**(2*k+1)/F(2*k+1)
    tail=F(2)*z**(2*N+3)/(F(2*N+3)*(1-z*z))
    return L,L+tail

LA_L,LA_U=log_bounds_gt1(A,14)
LB_L,LB_U=log_bounds_gt1(B,14)
LQ_L,LQ_U=log_bounds_gt1(1/q,2)
LBH_L,LBH_U=log_bounds_gt1(1/beta_hat,3)

# log beta(rho) = s c - log A - rho log B -(1+rho) log(1/q).
# Lower bounds on positive logarithms give an upper bound on log beta.
logbeta_upper=s*c-LA_L-rho*LB_L-(1+rho)*LQ_L
# log beta_hat = -log(1/beta_hat); an upper bound on log(1/beta_hat)
# therefore gives a lower bound on log beta_hat.
log_beta_hat_lower=-LBH_U
assert logbeta_upper < log_beta_hat_lower

# Infinite-volume strict-triangle defect after consuming P04's axis cap.
delta=2*(c-a_star)
assert delta == F(1,50000)
assert delta > 0

# Exact exponential finite-scale compression:
# beta_hat^25000 < 1/2.
lhs=2*(99997**25000)
rhs=100000**25000
assert lhs < rhs

# Take M=10^12. It is divisible by 4 (P04 axis-block concatenation)
# and 2500 (so rho*M is integral).
M=10**12
assert M % 4 == 0
assert M % 2500 == 0
rhoM=rho*M
assert rhoM.denominator == 1

# Since M >= 100*25000, beta_hat^M <= 2^-100.
# P04 finite axis estimate contributes 1/(2 sqrt(M)) after normalization.
sqrtM=10**6
assert sqrtM*sqrtM == M
repair=F(1,2*sqrtM)
exp_error=2*c*C*F(1,2**100)
finite_margin=delta-repair-exp_error
assert finite_margin > 0

print("PROB10-10 critical-envelope recombination exact certificate")
print("A =",A,"B =",B,"r =",r)
print("s =",s,"q =",q,"q_float =",float(q))
print("c =",c,"a_star =",a_star,"c_minus_a_star =",c-a_star)
print("rho0 =",rho,"rho0_float =",float(rho))
print("previous_rho =",F(41,25),"strict_cone_improvement =",rho < F(41,25))
print("beta_hat =",beta_hat)
print("logbeta_upper_float =",float(logbeta_upper))
print("log_beta_hat_lower_float =",float(log_beta_hat_lower))
print("logbeta_upper < log_beta_hat_lower =",logbeta_upper < log_beta_hat_lower)
print("delta =",delta,"delta_float =",float(delta))
print("Kbar_float =",float(Kbar))
print("C_float =",float(C))
print("half_block_inequality =",lhs < rhs)
print("M =",M,"rhoM =",rhoM)
print("repair_float =",float(repair))
print("exp_error_float =",float(exp_error))
print("finite_margin_float =",float(finite_margin))
print("finite_margin_num_bits =",finite_margin.numerator.bit_length(),
      "finite_margin_den_bits =",finite_margin.denominator.bit_length())
print("ALL_EXACT_CHECKS_PASS = True")
