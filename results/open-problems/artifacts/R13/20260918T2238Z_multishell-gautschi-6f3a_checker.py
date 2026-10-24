#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial

# R13 exact finite-arithmetic SELF-CHECK.
# New ingredient: sharpen the inverse-chi-square tail normalization by a
# Gautschi gamma certificate and partition the one/two-excursion lower-tail
# event into four disjoint shells. All acceptance comparisons are rational.

# ---------- retained universal/density data ----------
piU = Fraction(355,113)
sqrt10piU = Fraction(1121,200)
assert sqrt10piU**2 > 10*piU

U = Fraction(157,20)
s0 = Fraction(16,157)            # chi-square cutoff corresponding to Y=U
tailMeanL = Fraction(337097,10**6)
varCap = Fraction(9691697959,10**10)

# ---------- exact Gamma(7/5) bracket via Gautschi ----------
# DLMF 5.6.4: for x>0, 0<s<1,
# x^(1-s) < Gamma(x+1)/Gamma(x+s) < (x+1)^(1-s).
# Use x=N+1, s=2/5, then shift Gamma(N+7/5) down to Gamma(7/5).
N = 1000
root1002U = Fraction(631715,10000)   # > 1002^(3/5)
root1001L = Fraction(631335,10000)   # < 1001^(3/5)
assert root1002U**5 > (N+2)**3
assert root1001L**5 < (N+1)**3

poch = Fraction(1)
for j in range(N):
    poch *= Fraction(5*j+7,5)        # product_{j=0}^{N-1}(j+7/5)

gautschiL = Fraction(factorial(N+1),1)/(poch*root1002U)
gautschiU = Fraction(factorial(N+1),1)/(poch*root1001L)

gammaL = Fraction(4434,5000)         # 0.8868
gammaU = Fraction(4437,5000)         # 0.8874
assert gautschiL > gammaL
assert gautschiU < gammaU

# ---------- tight rational roots used in incomplete-gamma tails ----------
qL = Fraction(401132760363,10**12)   # lower for s0^(2/5)
qU = Fraction(401132760364,10**12)   # upper for s0^(2/5)
pow2L = Fraction(2639015821545,10**12) # lower for 2^(7/5)
pow2U = Fraction(2639015821546,10**12) # upper for 2^(7/5)
assert qL**5 < s0**2 < qU**5
assert pow2L**5 < 2**7 < pow2U**5

# For z<=s0, integrate the alternating Taylor series of exp(-s/2):
# I(z)=int_0^z s^(2/5)e^{-s/2} ds
#     = z^(7/5) * sum_k (-1)^k z^k/[2^k k!(k+7/5)].
# Odd partial sum is a lower bound; even partial sum is an upper bound.
def A_partial(z,m):
    out = Fraction(0)
    for k in range(m+1):
        out += (-1)**k * z**k / (
            (2**k) * factorial(k) * (Fraction(k,1)+Fraction(7,5))
        )
    return out

def tail_bounds(rho):
    # y = U*rho^5, z=s0/rho^5, and z^(7/5)=s0^(7/5)/rho^7.
    z = s0/rho**5
    AL = A_partial(z,5)
    AU = A_partial(z,4)
    assert AL < AU
    low = (s0*qL/rho**7)*AL/(pow2U*gammaU)
    up  = (s0*qU/rho**7)*AU/(pow2L*gammaL)
    assert low < up
    return low,up

# ---------- clean lower bounds used in the event count ----------
# Low category Y<=U.
tailUL,tailUU = tail_bounds(Fraction(1,1))
p0 = Fraction(987887,10**6)
assert 1-tailUU > p0

# Since E[Y]=1 and E[Y;Y>U] > tailMeanL, this is a valid upper bound
# for E[Y | Y<=U].
mu = (1-tailMeanL)/p0

# Four disjoint middle shells:
# (U,U*1.03^5], (..,U*1.06^5], (..,U*1.09^5], (..,U*1.13^5].
rhos = [
    Fraction(103,100),
    Fraction(106,100),
    Fraction(109,100),
    Fraction(113,100),
]
pShell = [
    Fraction(22157,10**7),
    Fraction(17660,10**7),
    Fraction(14155,10**7),
    Fraction(14717,10**7),
]
upper = []
prev = Fraction(1,1)
for idx,rho in enumerate(rhos):
    prevL,_ = tail_bounds(prev)
    _,rhoU = tail_bounds(rho)
    rigorous_band_lower = prevL-rhoU
    assert rigorous_band_lower > pShell[idx]
    upper.append(U*rho**5)
    prev = rho

# ---------- retained exact three-threshold upper-tail Jensen defect ----------
gamma7U_retained = Fraction(88869,100000)
def beta_up_exact(D,A):
    for k,Ak in A.items():
        pref = Fraction(5,7)/gamma7U_retained * (1-Fraction(2*k,5*D))
        assert (Ak/pref)**5 < Fraction(2*k,5)**7/(D**2)
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
        beta += c*(1/(rr-1)-1/(rr-Fraction(1,2)))
    beta /= 2
    assert beta > 0
    return beta

D = 135
A135 = {
    1: Fraction(78077,2500000),
    2: Fraction(821737,10000000),
    3: Fraction(36133,250000),
}
betaUp = beta_up_exact(D,A135)

# ---------- shell-conditioned Bernstein lower tail ----------
# If N iid low variables Z=Y|Y<=U have mean <=mu, variance <=varCap,
# and 0<=Z<=U, then for x>mu:
# P(mean(Z)<=x) >= 1-exp(-E) > 1-1/P8(E).
def bern_success(N,x):
    delta = x-mu
    if delta <= 0:
        return None
    E = N*delta**2/(2*varCap + Fraction(2,3)*U*delta)
    P8 = sum(E**j/factorial(j) for j in range(9))
    R = 1-Fraction(1,1)/P8
    assert R > 0
    return R

# Take q=49/500 and t=(1-q)^2. On X_D<=t,
# (1-sqrt(X_D))^2 >= q^2.
q = Fraction(49,500)
t = (1-q)**2

P0 = p0**D * bern_success(D,t)

# Exactly one shell excursion.
P1 = Fraction(0)
for i in range(4):
    x = (D*t-upper[i])/(D-1)
    R = bern_success(D-1,x)
    if R is not None:
        P1 += D*pShell[i]*p0**(D-1)*R

# Exactly two shell excursions. Sum all disjoint shell-count cases whose
# worst-case upper endpoints still leave the low variables below t.
P2 = Fraction(0)
valid_pairs = []
for i in range(4):
    for j in range(i,4):
        x = (D*t-upper[i]-upper[j])/(D-2)
        R = bern_success(D-2,x)
        if R is None:
            continue
        coeff = comb(D,2) if i==j else D*(D-1)
        P2 += coeff*pShell[i]*pShell[j]*p0**(D-2)*R
        valid_pairs.append((i,j))

assert valid_pairs == [(0,0),(0,1)]

Pevent = P0+P1+P2
betaLow = q*q*Pevent/2

# Combine disjoint lower-tail and retained upper-tail Jensen defects.
C135U = Fraction(27,20)*sqrt10piU*(1-betaUp-betaLow)

h_old = Fraction(739733,100000)
h_new = Fraction(739631,100000)
assert C135U < h_new
assert h_old-h_new == Fraction(51,50000)

# Row pruning for n=86: if active rows have norm >h/sqrt(n), then
# d < n^2/h^2. This ratio lies in (135,136), hence d<=135.
n = 86
ratio = Fraction(n*n,1)/(h_new*h_new)
assert Fraction(135,1) < ratio < Fraction(136,1)

print("R13 multishell + Gautschi exact self-check")
print("Gautschi Gamma(7/5) lower certificate =", float(gautschiL))
print("Gautschi Gamma(7/5) upper certificate =", float(gautschiU))
print("tail_U_lower =", float(tailUL))
print("tail_U_upper =", float(tailUU))
print("low_category_probability_lower =", float(p0))
print("conditional_low_mean_upper =", float(mu))
for i in range(4):
    print("shell",i,"upper_Y =",float(upper[i]),"probability_lower =",float(pShell[i]))
print("valid_two_excursion_shell_pairs =", valid_pairs)
print("P0_all_low_lower =", float(P0))
print("P1_one_shell_lower =", float(P1))
print("P2_two_shell_lower =", float(P2))
print("combined_lower_tail_event =", float(Pevent))
print("beta_up_D135 =", float(betaUp))
print("beta_low_multishell_D135 =", float(betaLow))
print("density_signing_D135_upper =", float(C135U))
print("density_signing_D135_upper < 739631/100000 =", C135U < h_new)
print("h_new =", float(h_new))
print("86^2/h_new^2 =", float(ratio))
print("exact_improvement =", float(h_old-h_new))
print("R13_MULTISHELL_GAUTSCHI_EXACT_PASS")
