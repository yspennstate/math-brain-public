#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial

# R13 exact finite-arithmetic SELF-CHECK.
# New ingredient: a two-band lower-tail event for the p=9/5
# cosine-power DTV density. It adds the disjoint cases:
#   (0) all Y_i <= U;
#   (1) exactly one U < Y_i <= V and all other Y_j <= U.
# No floating-point comparison is used for acceptance.

# ---- Classical rational constants and retained gamma certificates ----
piU = Fraction(355,113)
sqrt10piU = Fraction(1121,200)
assert sqrt10piU**2 > 10*piU

gamma7L = Fraction(350840,401787)
gamma7U = Fraction(88869,100000)
assert gamma7L < gamma7U

# ---- Retained truncated-law data ----
# S~chi^2_{14/5}, Y=4/(5S), U=157/20, s0=4/(5U)=16/157.
U = Fraction(157,20)
s0 = Fraction(16,157)
p0L = Fraction(24683,25000)             # P(Y<=U) > p0L
tailMeanL = Fraction(337097,1000000)     # E[Y;Y>U] > this
muC = (1-tailMeanL)/p0L                  # upper bound E[Y|Y<=U]
assert muC == Fraction(662903,987320)
varCap = Fraction(9691697959,10000000000) # retained Var(Y|Y<=U) upper bound

# ---- NEW middle band U<Y<=V ----
# Bounds for s0^(2/5) and 2^(7/5).
qL = Fraction(4011,10000)
qU = Fraction(1003,2500)
pow2L = Fraction(2639,1000)
pow2U = Fraction(66,25)
assert qL**5 < s0**2 < qU**5
assert pow2L**5 < 2**7 < pow2U**5

# Set V=U*(12/11)^5. Then z_V=s0/(12/11)^5, so the 7/5
# power scales by the exact rational factor (11/12)^7.
rho = Fraction(12,11)
V = U*rho**5
assert V == Fraction(9766656,805255)

# Lower bound P(Y>U):
# on 0<=s<=s0, exp(-s/2) >= 1-s0/2.
tailU_L = Fraction(5,7)*s0*qL*(1-s0/Fraction(2,1))/(pow2U*gamma7U)

# Upper bound P(Y>V):
# exp(-s/2)<=1, s0^(7/5)<s0*qU, and z_V^(7/5)=s0^(7/5)/rho^7.
tailV_U = Fraction(5,7)*s0*qU/(rho**7*pow2L*gamma7L)

pMidL = tailU_L-tailV_U
assert pMidL > 0

# ---- Retained exact three-threshold upper-tail Jensen defect ----
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
        rr = Fraction(7*ell,5)
        beta += c*(Fraction(1,1)/(rr-1)-Fraction(1,1)/(rr-Fraction(1,2)))
    beta /= 2
    assert beta > 0
    return beta

# Bernstein conditional-success lower bound.
# If N iid low-band variables have mean <=muC, variance <=varCap, and
# are bounded by U, then for x>muC:
# P(mean <=x) >= 1-exp(-E) >= 1-1/P8(E).
def bern_success_lower(N,x):
    delta = x-muC
    assert delta > 0
    E = N*delta**2/(2*varCap + Fraction(2,3)*U*delta)
    P8 = sum(E**j/factorial(j) for j in range(9))
    R = 1-Fraction(1,1)/P8
    assert R > 0
    return E,R

# ---- D=135 moving certificate ----
D=135
A135 = {
    1: Fraction(78077,2500000),
    2: Fraction(821737,10000000),
    3: Fraction(36133,250000),
}
betaUp = beta_up_exact(D,A135)

# Target lower-tail level t=(9/10)^2, so on X_D<=t,
# (1-sqrt(X_D))^2 >= 1/100.
t = Fraction(81,100)

# Case 0: all variables in the low band.
E0,R0 = bern_success_lower(D,t)
Pevent0 = p0L**D * R0

# Case 1: exactly one middle-band variable U<Y<=V.
# It contributes at most V; the other D-1 variables need mean <=t1.
t1 = (D*t-V)/(D-1)
E1,R1 = bern_success_lower(D-1,t1)
Pevent1 = D*pMidL*p0L**(D-1)*R1

# Cases 0 and 1 are disjoint and both imply X_D<=t.
Pevent = Pevent0+Pevent1
betaLowTwoBand = Fraction(1,200)*Pevent
assert betaLowTwoBand > 0

# DTV signing constant: (27 sqrt(10 pi)/20)*(1-betaUp-betaLow).
C135U = Fraction(27,20)*sqrt10piU*(1-betaUp-betaLowTwoBand)
hnew = Fraction(739733,100000) # 7.39733
hold = Fraction(73979,10000)   # 7.3979
assert C135U < hnew
assert hold-hnew == Fraction(57,100000)

# Row-pruning for n=86: active rows d < n^2/h^2, hence d<=135.
n=86
ratio = Fraction(n*n,1)/(hnew*hnew)
assert Fraction(135,1) < ratio < Fraction(136,1)

print("R13 two-band lower-tail exact self-check")
print("V =", V, "=", float(V))
print("tail_U_lower =", float(tailU_L))
print("tail_V_upper =", float(tailV_U))
print("middle_band_probability_lower =", float(pMidL))
print("conditional_mean_upper =", float(muC))
print("conditional_variance_upper =", float(varCap))
print("t =", t, "=", float(t))
print("one_middle_low_threshold =", float(t1))
print("bernstein_E0 =", float(E0))
print("all_low_event_lower =", float(Pevent0))
print("bernstein_E1 =", float(E1))
print("one_middle_event_lower =", float(Pevent1))
print("combined_lower_event =", float(Pevent))
print("beta_up_D135 =", float(betaUp))
print("beta_low_two_band_D135 =", float(betaLowTwoBand))
print("density_signing_D135_upper =", float(C135U))
print("density_signing_D135_upper < 739733/100000 =", C135U < hnew)
print("h_new =", hnew, "=", float(hnew))
print("86^2/h_new^2 =", float(ratio))
print("135 < 86^2/h_new^2 < 136 =", Fraction(135)<ratio<Fraction(136))
print("previous_B86 =", hold, "=", float(hold))
print("improvement =", hold-hnew, "=", float(hold-hnew))
print("R13_TWOBAND_LOWERTAIL_EXACT_PASS")
