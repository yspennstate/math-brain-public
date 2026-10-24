#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial

# R13 exact finite-arithmetic SELF-CHECK.
# New ingredients:
#   (i) exact truncated first/second moment certificates for the p=9/5 inverse-chi-square law,
#   (ii) sharp one-sided second-moment (Cantelli) lower-tail bounds after shell conditioning,
#   (iii) a five-threshold occupancy DP for the upper tail.
# All acceptance tests are exact rational arithmetic.

# ---------- retained density and elementary constants ----------
piU = Fraction(355, 113)
sqrt10piU = Fraction(1121, 200)
assert sqrt10piU**2 > 10*piU

D = 135
n = 86
U = Fraction(157, 20)
s0 = Fraction(16, 157)          # because Y=(4/5)/S and Y=U iff S=16/157
c = Fraction(4, 5)

# ---------- exact Gamma(7/5) bracket via Gautschi (retained, rechecked) ----------
N = 1000
root1002U = Fraction(631715, 10000)   # > 1002^(3/5)
root1001L = Fraction(631335, 10000)   # < 1001^(3/5)
assert root1002U**5 > (N+2)**3
assert root1001L**5 < (N+1)**3

poch = Fraction(1)
for j in range(N):
    poch *= Fraction(5*j + 7, 5)

gautschiL = Fraction(factorial(N+1), 1) / (poch * root1002U)
gautschiU = Fraction(factorial(N+1), 1) / (poch * root1001L)

gammaL = Fraction(4434, 5000)
gammaU = Fraction(4437, 5000)
assert gautschiL > gammaL
assert gautschiU < gammaU

# ---------- rational roots for incomplete-gamma integrals ----------
qL = Fraction(401132760363, 10**12)      # < s0^(2/5)
qU = Fraction(401132760364, 10**12)      # > s0^(2/5)
pow2L = Fraction(2639015821545, 10**12) # < 2^(7/5)
pow2U = Fraction(2639015821546, 10**12) # > 2^(7/5)
assert qL**5 < s0**2 < qU**5
assert pow2L**5 < 2**7 < pow2U**5


def partial(z, alpha, m):
    # sum_{k=0}^m (-1)^k z^k / [2^k k! (k+alpha)]
    out = Fraction(0)
    for k in range(m+1):
        out += (-1)**k * z**k / (
            (2**k) * factorial(k) * (Fraction(k, 1) + alpha)
        )
    return out


def exp_half_partial(z, m):
    # m-th alternating partial sum for exp(-z/2)
    return sum(((-1)**k) * z**k / ((2**k)*factorial(k)) for k in range(m+1))


def tail_probability_bounds(rho):
    # P(Y > U*rho^5), rho>=1.  Here z=s0/rho^5 and
    # z^(7/5)=s0^(7/5)/rho^7 = s0*s0^(2/5)/rho^7.
    z = s0 / rho**5
    AL = partial(z, Fraction(7, 5), 5)
    AU = partial(z, Fraction(7, 5), 4)
    low = (s0*qL/rho**7) * AL / (pow2U*gammaU)
    up  = (s0*qU/rho**7) * AU / (pow2L*gammaL)
    assert low < up
    return low, up

# ---------- strengthened low-category probability and first moment ----------
tailProbL, tailProbU = tail_probability_bounds(Fraction(1, 1))
pLowL = Fraction(9878872, 10**7)
pLowU = Fraction(9878955, 10**7)
assert 1-tailProbU > pLowL
assert 1-tailProbL < pLowU

# E[Y;Y>U] = c/(2^(7/5) Gamma(7/5)) * int_0^s0 s^(-3/5)e^(-s/2) ds.
# The integral equals s0^(2/5)*sum (-1)^k s0^k/[2^k k!(k+2/5)].
J1L = qL * partial(s0, Fraction(2, 5), 5)
J1U = qU * partial(s0, Fraction(2, 5), 4)
tailMeanL_exact = c * J1L / (pow2U*gammaU)
tailMeanU_exact = c * J1U / (pow2L*gammaL)

tailMeanL = Fraction(3376616, 10**7)
tailMeanU = Fraction(3378901, 10**7)
assert tailMeanL_exact > tailMeanL
assert tailMeanU_exact < tailMeanU

# Conditional mean upper/lower bounds for Z := Y | (Y<=U).
muU = (1-tailMeanL) / pLowL
muL = (1-tailMeanU) / pLowU
assert muL < muU

# ---------- exact truncated second-moment recurrence ----------
# Let M2 = E[Y^2 ; Y<=U].  Integration by parts gives
# M2 = c^2*(5/3)*s0^(-3/5)e^(-s0/2)/(2^(7/5)Gamma(7/5))
#      - 2/3 + (2/3) E[Y;Y>U].
# Since s0^(-3/5)=s0^(2/5)/s0, use qU/qL and alternating exp bounds.
eL = exp_half_partial(s0, 5)
eU = exp_half_partial(s0, 4)
firstTermL = c*c*Fraction(5, 3)*(qL/s0)*eL/(pow2U*gammaU)
firstTermU = c*c*Fraction(5, 3)*(qU/s0)*eU/(pow2L*gammaL)
M2L = firstTermL - Fraction(2, 3) + Fraction(2, 3)*tailMeanL_exact
M2U = firstTermU - Fraction(2, 3) + Fraction(2, 3)*tailMeanU_exact
assert M2L < M2U

EZ2U = M2U / pLowL
varU = EZ2U - muL**2
assert varU > 0

# ---------- retained four middle shells, re-certified from sharpened gamma bounds ----------
rhos = [
    Fraction(103, 100),
    Fraction(106, 100),
    Fraction(109, 100),
    Fraction(113, 100),
]
pShell = [
    Fraction(22157, 10**7),
    Fraction(17660, 10**7),
    Fraction(14155, 10**7),
    Fraction(14717, 10**7),
]
upper = []
prev = Fraction(1, 1)
for idx, rho in enumerate(rhos):
    prevL, _ = tail_probability_bounds(prev)
    _, rhoU = tail_probability_bounds(rho)
    rigorousBandLower = prevL-rhoU
    assert rigorousBandLower > pShell[idx]
    upper.append(U*rho**5)
    prev = rho

# ---------- method #19: five-threshold upper-tail occupancy DP ----------
# For t>=1 and k=1,...,K, the event Y>=D*t/k has probability at least
# (A_k/D) t^(-7/5).  The clean A_k below are certified from the density integral.
K = 5
A = {
    1: Fraction(31276223, 10**9),
    2: Fraction(20573291, 250000000),
    3: Fraction(18092773, 125000000),
    4: Fraction(215878339, 10**9),
    5: Fraction(73539201, 250000000),
}
for k, Ak in A.items():
    pref = Fraction(5, 7)/gammaU * (1-Fraction(2*k, 5*D))
    # Ak < pref * ((2k/5)^7/D^2)^(1/5)
    assert (Ak/pref)**5 < Fraction((2*k)**7, 5**7 * D**2)

# Model category j has mass d_j*x, x=t^(-7/5), where cumulative
# mass through level k is a_k*x with a_k=A_k/D.  Complement of the union
# {at least k coordinates above D t/k for some k<=K} has prefix counts <=k-1.
a = {k: A[k]/D for k in A}
dcat = {1: a[1]}
for k in range(2, K+1):
    dcat[k] = a[k]-a[k-1]
    assert dcat[k] > 0

# Exponential-generating DP for allowed category-count vectors.
dp = {0: Fraction(1)}  # after level 1, n1=0 is forced
for k in range(2, K+1):
    nd = {}
    for rprev, val in dp.items():
        for nk in range(0, (k-1)-rprev+1):
            r = rprev+nk
            nd[r] = nd.get(r, Fraction(0)) + val*dcat[k]**nk/factorial(nk)
    dp = nd

# Expand complement polynomial C_K(x), then Q_K(x)=1-C_K(x).
comp = [Fraction(0) for _ in range(D+1)]
aK = a[K]
for r, weight in dp.items():
    falling = Fraction(factorial(D), factorial(D-r))
    base = falling*weight
    for j in range(D-r+1):
        comp[r+j] += base*comb(D-r, j)*((-aK)**j)
assert comp[0] == 1

betaUp = Fraction(0)
for ell in range(1, D+1):
    coeffQ = -comp[ell]
    rr = Fraction(7*ell, 5)
    betaUp += coeffQ * (Fraction(1, 1)/(rr-1) - Fraction(1, 1)/(rr-Fraction(1, 2)))
betaUp /= 2
assert betaUp > 0

# ---------- method #24: Cantelli after shell conditioning ----------
# For N iid copies of Z with mean <=muU and variance <=varU,
# Cantelli gives P(mean(Z)<=x) >= N delta^2/(varU+N delta^2), delta=x-muU>0.
def cantelli_success(Nlow, x):
    delta = x-muU
    if delta <= 0:
        return None
    return Nlow*delta**2/(varU + Nlow*delta**2)

q = Fraction(106965, 10**6)
t = (1-q)**2

# Sum disjoint patterns with exactly k middle-shell excursions and all remaining
# coordinates in the low category.  With this q only k=0, k=1 (all four shells),
# and k=2 with both excursions in shell 0 survive the exact x>muU test.
Pparts = {}
Pevent = Fraction(0)
valid_patterns = []
for k in range(0, 5):
    subtotal = Fraction(0)
    # Enumerate the four shell count vectors with total k.
    for c0 in range(k+1):
        for c1 in range(k-c0+1):
            for c2 in range(k-c0-c1+1):
                c3 = k-c0-c1-c2
                counts = (c0, c1, c2, c3)
                sumUpper = sum(counts[i]*upper[i] for i in range(4))
                Nlow = D-k
                x = t if k == 0 else (D*t-sumUpper)/Nlow
                R = cantelli_success(Nlow, x)
                if R is None:
                    continue
                coeff = 1
                if k:
                    for z in range(D-k+1, D+1):
                        coeff *= z
                    for cc in counts:
                        coeff //= factorial(cc)
                term = Fraction(coeff, 1) * pLowL**Nlow * R
                for i, cc in enumerate(counts):
                    term *= pShell[i]**cc
                subtotal += term
                valid_patterns.append((k, counts))
    if subtotal:
        Pparts[k] = subtotal
        Pevent += subtotal

assert [p for p in valid_patterns if p[0] == 0] == [(0, (0, 0, 0, 0))]
assert [p for p in valid_patterns if p[0] == 1] == [
    (1, (0, 0, 0, 1)), (1, (0, 0, 1, 0)), (1, (0, 1, 0, 0)), (1, (1, 0, 0, 0))
]
assert [p for p in valid_patterns if p[0] == 2] == [(2, (2, 0, 0, 0))]
assert all(p[0] <= 2 for p in valid_patterns)

betaLow = q*q*Pevent/2

# ---------- combine disjoint upper/lower Jensen defects ----------
C135U = Fraction(27, 20)*sqrt10piU*(1-betaUp-betaLow)

hOld = Fraction(739631, 100000)
hNew = Fraction(739377, 100000)
assert C135U < hNew
assert hOld-hNew == Fraction(127, 50000)  # 0.00254

# Row pruning for n=86: active rows have norm >h/sqrt(n), so d<n^2/h^2.
ratio = Fraction(n*n, 1)/(hNew*hNew)
assert Fraction(135, 1) < ratio < Fraction(136, 1)

print('R13 Cantelli + moment recurrence + occupancy cascade exact self-check')
print('Gamma(7/5) Gautschi lower =', float(gautschiL))
print('Gamma(7/5) Gautschi upper =', float(gautschiU))
print('P(Y<=U) lower =', float(pLowL))
print('P(Y<=U) upper =', float(pLowU))
print('E[Y;Y>U] lower =', float(tailMeanL))
print('E[Y;Y>U] upper =', float(tailMeanU))
print('conditional mean lower =', float(muL))
print('conditional mean upper =', float(muU))
print('conditional second moment upper =', float(EZ2U))
print('conditional variance upper =', float(varU))
print('upper-tail threshold count K =', K)
print('beta_up_K5_D135 =', float(betaUp))
print('q_lower_tail =', float(q))
for k in sorted(Pparts):
    print('lower-tail exact-shell count', k, 'probability contribution =', float(Pparts[k]))
print('combined lower-tail event probability =', float(Pevent))
print('beta_low_Cantelli_D135 =', float(betaLow))
print('density_signing_D135_upper =', float(C135U))
print('density_signing_D135_upper < 739377/100000 =', C135U < hNew)
print('h_old =', float(hOld))
print('h_new =', float(hNew))
print('86^2/h_new^2 =', float(ratio))
print('exact_improvement =', float(hOld-hNew))
print('R13_CANTELLI_CASCADE_EXACT_PASS')
