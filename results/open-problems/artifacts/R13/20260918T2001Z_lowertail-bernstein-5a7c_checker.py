#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial

# R13 exact finite-arithmetic SELF-CHECK.
#
# New ingredient: a Jensen-defect contribution from the LOWER tail of the
# inverse-chi-square average for the p=9/5 cosine-power cube density.
# We truncate at U=157/20, condition on the product event Y_i<=U, and apply
# one-sided Bernstein to force X_D=(1/D) sum Y_i <= 8183/10000.
#
# Analytic inputs used by the written proof:
#   (i) Sonin / continuous Stirling bounds for Gamma,
#   (ii) one-sided Bernstein for independent bounded variables,
#   (iii) e^x >= 1+x+x^2/2+x^3/6 for x>=0.
# The exact rational consequences used at D=135 (and the diagnostic D=136)
# are all checked below.

# ---- Classical pi / square-root bounds ----
piL = Fraction(333,106)
piU = Fraction(355,113)
sqrt2piL = Fraction(1253,500)
sqrt2piU = Fraction(250663,100000)
sqrt10piU = Fraction(1121,200)
assert sqrt2piL**2 < 2*piL
assert sqrt2piU**2 > 2*piU
assert sqrt10piU**2 > 10*piU

# ---- Gamma(12/5) lower bound from Sonin's continuous Stirling formula ----
# Sonin: Gamma(1+x)=sqrt(2*pi) x^(x+1/2)
#        exp(-x + 1/(12(x+theta))), 0<theta<1/2.
# For x=7/5, the correction is >5/114 and
# aL=7/5-5/114=773/570.
#
# (207/200)^10 > 7/5 implies
# (7/5)^(19/10) > (49/25)*(200/207).
# We prove exp(aL)<1941/500 by a Taylor upper bound with geometric tail.
root10_hi = Fraction(207,200)
assert root10_hi**10 > Fraction(7,5)
aL = Fraction(773,570)
S4 = sum(aL**k/factorial(k) for k in range(5))
term5 = aL**5/factorial(5)
exp_upper = S4 + term5/(1-aL/Fraction(6,1))
exp_cap = Fraction(1941,500)
assert exp_upper < exp_cap
gamma12L = sqrt2piL*Fraction(49,25)*Fraction(200,207)/exp_cap
assert gamma12L == Fraction(491176,401787)
assert gamma12L > Fraction(6,5)

# ---- Gamma(7/5) upper bound, reproducing the preceding R13 certificate ----
# Continuous Stirling upper bound at x=7/5:
# Gamma(12/5) < sqrt(2*pi)(7/5)^(19/10) exp(-563/420),
# then Gamma(7/5)=(5/7)Gamma(12/5).
# (517/500)^10 < 7/5 controls the tenth root, and a degree-6
# positive Taylor polynomial lower-bounds exp(563/420).
root10_lo = Fraction(517,500)
assert root10_lo**10 < Fraction(7,5)
aU = Fraction(563,420)
P6 = sum(aU**k/factorial(k) for k in range(7))
gamma7U_derived = (
    Fraction(5,7)*sqrt2piU*Fraction(49,25)*Fraction(500,517)/P6
)
gamma7U = Fraction(88869,100000)
assert gamma7U_derived < gamma7U

# ---- Truncation constants for p=9/5 ----
# S~chi^2_{14/5}, Y=4/(5S), U=157/20, so Y>U iff S<16/157.
U = Fraction(157,20)

# Using e^{-s/2}<=1:
# P(Y>U) <= (8/157)^(7/5)/Gamma(12/5) < 317/25000.
p0L = Fraction(24683,25000)
tailProbU = 1-p0L
assert tailProbU == Fraction(317,25000)
assert Fraction(8,157)**7 < (tailProbU*gamma12L)**5

# Using e^{-s/2}>=1-s/2 on 0<=s<=16/157:
# E[Y;Y>U] >= (1083/1099)/Gamma(7/5) * (64/24649)^(1/5)
# > 337097/10^6.
tailMeanL = Fraction(337097,1000000)
assert (
    tailMeanL*gamma7U*Fraction(1099,1083)
)**5 < Fraction(64,24649)

# Therefore, conditioned on Y<=U,
# E[Y | Y<=U] < (1-tailMeanL)/p0L = muC.
muC = (1-tailMeanL)/p0L
assert muC == Fraction(662903,987320)
varU = U*muC   # Z^2<=UZ for 0<=Z<=U, hence Var Z<=E Z^2<=U muC.

# ---- Retained upper-tail defect: exact 3-threshold polynomial ----
def beta_up_exact(D, A):
    for k, Ak in A.items():
        pref = Fraction(5,7)/gamma7U * (1-Fraction(2*k,5*D))
        # A_k is below
        # [5/(7 gammaU)](2k/5)^(7/5)(1-2k/(5D))D^(-2/5).
        assert (Ak/pref)**5 < Fraction(2*k,5)**7/(D**2)
    assert A[1] < A[2] < A[3] < D

    a1,a2,a3 = A[1]/D, A[2]/D, A[3]/D
    comp = {}
    def add(power, value):
        comp[power] = comp.get(power, Fraction(0)) + value

    # Complement of:
    # >=1 coordinate over Dt OR >=2 over Dt/2 OR >=3 over Dt/3.
    for j in range(D+1):
        add(j, comb(D,j)*((-a3)**j))
    coef1 = D*(a3-a1)
    for j in range(D):
        add(j+1, coef1*comb(D-1,j)*((-a3)**j))
    cat3 = a3-a2
    cat2 = a2-a1
    coef2 = comb(D,2)*(cat3*cat3 + 2*cat2*cat3)
    for j in range(D-1):
        add(j+2, coef2*comb(D-2,j)*((-a3)**j))

    beta = Fraction(0)
    for ell in range(1,D+1):
        c = -comp.get(ell,Fraction(0))
        r = Fraction(7*ell,5)
        integral = Fraction(1,1)/(r-1) - Fraction(1,1)/(r-Fraction(1,2))
        beta += c*integral
    beta /= 2
    assert beta > 0
    return beta

# ---- New lower-tail Bernstein defect ----
t = Fraction(8183,10000)
qgap = Fraction(477,5000)
assert (1-qgap)**2 > t  # so qgap < 1-sqrt(t)

def beta_low_exact(D):
    delta = t-muC
    assert delta > 0
    bernE = D*delta**2/(2*varU + Fraction(2,3)*U*delta)
    # e^E >= P3(E), hence 1-e^{-E} >= 1-1/P3(E).
    expLower3 = sum(bernE**k/factorial(k) for k in range(4))
    condSuccessL = 1-Fraction(1,1)/expLower3
    assert condSuccessL > 0
    eventProbL = p0L**D * condSuccessL
    beta = Fraction(1,2)*qgap**2*eventProbL
    assert beta > 0
    return beta, bernE, condSuccessL, eventProbL

# D=135: main moving certificate.
D = 135
A135 = {
    1: Fraction(78077,2500000),
    2: Fraction(821737,10000000),
    3: Fraction(36133,250000),
}
beta_up_135 = beta_up_exact(D,A135)
beta_low_135, bernE135, cond135, prob135 = beta_low_exact(D)
beta_total_135 = beta_up_135+beta_low_135

# p=9/5 signing coefficient:
# C_D <= [27 sqrt(10*pi)/20] * (1-beta_total).
C135_upper = Fraction(27,20)*sqrt10piU*(1-beta_total_135)
h_new = Fraction(185022,25000)   # 7.40088
h_old = Fraction(740179,100000)  # 7.40179
assert C135_upper < h_new

# Row pruning at n=86: active rows d < n^2/h^2.
n = 86
ratio135 = Fraction(n*n,1)/(h_new*h_new)
assert Fraction(135,1) < ratio135 < Fraction(136,1)
assert h_old-h_new == Fraction(91,100000)

# D=136 diagnostic: the SAME rational tail scheme becomes weaker when one
# increases the certified active dimension.  This is a failure of this
# certificate, not an impossibility theorem for better density/tail estimates.
A136 = {
    1: Fraction(155697,5000000),
    2: Fraction(16387,200000),
    3: Fraction(288231,2000000),
}
beta_up_136 = beta_up_exact(136,A136)
beta_low_136, bernE136, cond136, prob136 = beta_low_exact(136)
C136_upper = Fraction(27,20)*sqrt10piU*(1-beta_up_136-beta_low_136)
# The D=136 certified density upper number is already larger than the
# D=135 rational threshold h_new.  Hence this exact same truncation/tail
# certificate does not improve the n=86 bound by moving to D=136.
assert C136_upper > h_new

print("gamma12_lower =", gamma12L, "=", float(gamma12L))
print("exp(773/570)_upper =", float(exp_upper))
print("gamma7_upper_derived =", float(gamma7U_derived))
print("P(Y<=157/20)_lower =", p0L, "=", float(p0L))
print("excluded_mean_lower =", tailMeanL, "=", float(tailMeanL))
print("conditional_mean_upper =", muC, "=", float(muC))
print("A135 =", {k: str(v) for k,v in A135.items()})
print("beta_up_D135 =", float(beta_up_135))
print("bernstein_exponent_D135 =", bernE135, "=", float(bernE135))
print("conditional_success_D135_lower =", float(cond135))
print("lower_event_probability_D135_lower =", float(prob135))
print("beta_low_D135 =", float(beta_low_135))
print("beta_total_D135 =", float(beta_total_135))
print("density_signing_D135_upper =", float(C135_upper))
print("density_signing_D135_upper < 185022/25000 =", C135_upper < h_new)
print("h_new =", h_new, "=", float(h_new))
print("86^2/h_new^2 =", float(ratio135))
print("135 < 86^2/h_new^2 < 136 =", Fraction(135,1) < ratio135 < Fraction(136,1))
print("previous_B86 =", h_old, "=", float(h_old))
print("improvement =", h_old-h_new, "=", float(h_old-h_new))
print("A136 =", {k: str(v) for k,v in A136.items()})
print("beta_up_D136 =", float(beta_up_136))
print("beta_low_D136 =", float(beta_low_136))
print("density_signing_D136_upper =", float(C136_upper))
print("D136_same-certificate_worse_than_h_new =", C136_upper > h_new)
print("R13_LOWERTAIL_BERNSTEIN_EXACT_PASS")
