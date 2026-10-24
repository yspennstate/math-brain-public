#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial

# R13 exact finite-arithmetic SELF-CHECK.
# New ingredient: bound the conditional SECOND MOMENT of the truncated
# inverse-chi-square law, rather than using Var(Z) <= U E Z.
# This sharpens the lower-tail Bernstein contribution at D=135.

# ---- Classical rational constants ----
piL = Fraction(333,106)
piU = Fraction(355,113)
sqrt2piL = Fraction(1253,500)
sqrt2piU = Fraction(250663,100000)
sqrt10piU = Fraction(1121,200)
assert sqrt2piL**2 < 2*piL
assert sqrt2piU**2 > 2*piU
assert sqrt10piU**2 > 10*piU

# ---- Gamma bounds retained from the preceding R13 certificate ----
# Sonin lower bound for Gamma(12/5).
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
gamma7L = Fraction(5,7)*gamma12L
assert gamma7L == Fraction(350840,401787)

# Continuous-Stirling upper bound for Gamma(7/5), used in beta_up.
root10_lo = Fraction(517,500)
assert root10_lo**10 < Fraction(7,5)
aU = Fraction(563,420)
P6 = sum(aU**k/factorial(k) for k in range(7))
gamma7U_derived = Fraction(5,7)*sqrt2piU*Fraction(49,25)*Fraction(500,517)/P6
gamma7U = Fraction(88869,100000)
assert gamma7U_derived < gamma7U

# ---- Truncation law: S~chi^2_{14/5}, Y=4/(5S), U=157/20 ----
U = Fraction(157,20)
s0 = Fraction(16,157)  # Y<=U iff S>=s0
p0L = Fraction(24683,25000)  # retained exact lower bound on P(Y<=U)
tailMeanL = Fraction(337097,1000000) # retained lower bound E[Y;Y>U]
muC = (1-tailMeanL)/p0L
assert muC == Fraction(662903,987320) # upper bound on E[Y | Y<=U]

# ---- NEW: conditional second moment bound ----
# E[Y^2; Y<=U] = (16/25)/(2^(7/5) Gamma(7/5))
#                 * int_{s0}^infty s^(-8/5)e^(-s/2) ds.
# On [s0,1], use e^{-s/2} <= 1-s/2+s^2/8.
# Rational root bounds:
R = Fraction(19681,5000)       # s0^(-3/5) < R
Q = Fraction(1003,2500)        # s0^(2/5) < Q
r2 = Fraction(2639,1000)       # r2 < 2^(7/5)
rminus = Fraction(33,100)      # 2^(-8/5) < rminus
assert R**5 > Fraction(157,16)**3
assert Q**5 > s0**2
assert r2**5 < 2**7
assert rminus**5 > Fraction(1,256)

# Dropping the final negative term -5/56*s0^(7/5) is safe.
I1U = Fraction(5,3)*(R-1) - Fraction(5,4)*(1-Q) + Fraction(5,56)

# On [1,2], use s^(-8/5)<=1; on [2,infty], <=2^(-8/5)<33/100.
# Alternating Taylor bounds: even partial = upper, odd partial = lower for e^{-x}.
def exp_neg_even_upper(x, N):
    assert N % 2 == 0
    return sum((-x)**k/factorial(k) for k in range(N+1))
def exp_neg_odd_lower(x, N):
    assert N % 2 == 1
    return sum((-x)**k/factorial(k) for k in range(N+1))

emhU = exp_neg_even_upper(Fraction(1,2),10)
e1L = exp_neg_odd_lower(Fraction(1),11)
e1U = exp_neg_even_upper(Fraction(1),10)
I2U = 2*(emhU-e1L) + 2*rminus*e1U

M2_uncond_U = Fraction(16,25)/(r2*gamma7L)*(I1U+I2U)
M2_cond_U = M2_uncond_U/p0L
m2cap = Fraction(697,500) # 1.394
assert M2_cond_U < m2cap

# NEW: lower bound on conditional mean, needed to subtract its square.
# E[Y;Y>U] <= 2 s0^(2/5)/(2^(7/5)Gamma(7/5))
#            < 2 Q/(r2 gamma7L) < 34821/100000.
tailMeanU = 2*Q/(r2*gamma7L)
tailMeanUCap = Fraction(34821,100000)
assert tailMeanU < tailMeanUCap
meanLower = 1-tailMeanUCap # P(Y<=U)<=1 makes conditional mean even larger
assert meanLower == Fraction(65179,100000)

# Therefore Var(Z) < E Z^2 - (E Z)^2 < this rational cap.
varCap = m2cap - meanLower**2
assert varCap == Fraction(9691697959,10000000000)
assert varCap > 0

# ---- Retained exact three-threshold upper-tail defect ----
def beta_up_exact(D,A):
    for k, Ak in A.items():
        pref = Fraction(5,7)/gamma7U * (1-Fraction(2*k,5*D))
        assert (Ak/pref)**5 < Fraction(2*k,5)**7/(D**2)
    assert A[1] < A[2] < A[3] < D
    a1,a2,a3 = A[1]/D,A[2]/D,A[3]/D
    comp = {}
    def add(power,value):
        comp[power] = comp.get(power,Fraction(0)) + value
    for j in range(D+1):
        add(j,comb(D,j)*((-a3)**j))
    coef1 = D*(a3-a1)
    for j in range(D):
        add(j+1,coef1*comb(D-1,j)*((-a3)**j))
    cat3 = a3-a2
    cat2 = a2-a1
    coef2 = comb(D,2)*(cat3*cat3 + 2*cat2*cat3)
    for j in range(D-1):
        add(j+2,coef2*comb(D-2,j)*((-a3)**j))
    beta = Fraction(0)
    for ell in range(1,D+1):
        c = -comp.get(ell,Fraction(0))
        r = Fraction(7*ell,5)
        integral = Fraction(1,1)/(r-1) - Fraction(1,1)/(r-Fraction(1,2))
        beta += c*integral
    beta /= 2
    assert beta > 0
    return beta

# ---- NEW lower-tail Bernstein defect with second-moment variance cap ----
t = Fraction(987,1250)    # 0.7896
qgap = Fraction(557,5000) # 0.1114
assert (1-qgap)**2 > t

def beta_low_second_moment(D):
    delta = t-muC
    assert delta > 0
    bernE = D*delta**2/(2*varCap + Fraction(2,3)*U*delta)
    # e^E >= P8(E), hence 1-e^{-E} >= 1-1/P8(E).
    expLower8 = sum(bernE**k/factorial(k) for k in range(9))
    condSuccessL = 1-Fraction(1,1)/expLower8
    assert condSuccessL > 0
    eventProbL = p0L**D * condSuccessL
    beta = Fraction(1,2)*qgap**2*eventProbL
    assert beta > 0
    return beta,bernE,condSuccessL,eventProbL

# ---- D=135 main moving certificate ----
D=135
A135={
    1: Fraction(78077,2500000),
    2: Fraction(821737,10000000),
    3: Fraction(36133,250000),
}
beta_up_135=beta_up_exact(D,A135)
beta_low_135,bernE135,cond135,prob135=beta_low_second_moment(D)
beta_total_135=beta_up_135+beta_low_135
C135U = Fraction(27,20)*sqrt10piU*(1-beta_total_135)
h_new = Fraction(73979,10000) # 7.3979
h_old = Fraction(185022,25000) # 7.40088
assert C135U < h_new
assert h_old-h_new == Fraction(149,50000)

# Row-pruning at n=86: if ||row||_2>h/sqrt(n), then number active d<n^2/h^2.
n=86
ratio = Fraction(n*n,1)/(h_new*h_new)
assert Fraction(135,1) < ratio < Fraction(136,1)

# D=136 diagnostic for the same certificate: still does not beat h_new.
A136={
    1: Fraction(155697,5000000),
    2: Fraction(16387,200000),
    3: Fraction(288231,2000000),
}
beta_up_136=beta_up_exact(136,A136)
beta_low_136,bernE136,cond136,prob136=beta_low_second_moment(136)
C136U = Fraction(27,20)*sqrt10piU*(1-beta_up_136-beta_low_136)
assert C136U > h_new

print('gamma7_lower =', gamma7L, '=', float(gamma7L))
print('I1_upper =', float(I1U))
print('I2_upper =', float(I2U))
print('conditional_second_moment_upper =', float(M2_cond_U))
print('conditional_second_moment_upper < 697/500 =', M2_cond_U < m2cap)
print('removed_mean_upper =', float(tailMeanU))
print('removed_mean_upper < 34821/100000 =', tailMeanU < tailMeanUCap)
print('conditional_mean_lower =', meanLower, '=', float(meanLower))
print('conditional_variance_upper =', varCap, '=', float(varCap))
print('beta_up_D135 =', float(beta_up_135))
print('bernstein_exponent_D135 =', float(bernE135))
print('conditional_success_D135_lower =', float(cond135))
print('lower_event_probability_D135_lower =', float(prob135))
print('beta_low_D135 =', float(beta_low_135))
print('beta_total_D135 =', float(beta_total_135))
print('density_signing_D135_upper =', float(C135U))
print('density_signing_D135_upper < 73979/10000 =', C135U < h_new)
print('h_new =', h_new, '=', float(h_new))
print('86^2/h_new^2 =', float(ratio))
print('135 < 86^2/h_new^2 < 136 =', Fraction(135)<ratio<Fraction(136))
print('previous_B86 =', h_old, '=', float(h_old))
print('improvement =', h_old-h_new, '=', float(h_old-h_new))
print('beta_up_D136 =', float(beta_up_136))
print('beta_low_D136 =', float(beta_low_136))
print('density_signing_D136_upper =', float(C136U))
print('D136_same-certificate_worse_than_h_new =', C136U > h_new)
print('R13_TRUNC_SECOND_MOMENT_EXACT_PASS')
