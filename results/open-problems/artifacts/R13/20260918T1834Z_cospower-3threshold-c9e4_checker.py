#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial

# Exact finite-arithmetic checker for the R13 p=9/5 cosine-power / 3-threshold tail certificate.
# Classical analytic inputs used by the proof, but not machine-proved here:
#   pi < 355/113,
#   Robbins/Stirling upper bound Gamma(x+1) < sqrt(2*pi) x^(x+1/2) exp(-x+1/(12x)), x>0,
#   exp(x) > sum_{k=0}^6 x^k/k! for x>0.

piU = Fraction(355,113)
sqrt2piU = Fraction(250663,100000)
sqrt10piU = Fraction(1121,200)
assert sqrt2piU*sqrt2piU > 2*piU
assert sqrt10piU*sqrt10piU > 10*piU

# Gamma(7/5) upper certificate.
# Gamma(7/5)=(5/7)Gamma(12/5), use Robbins with x=7/5.
# (7/5)^(19/10) = (49/25)/(7/5)^(1/10), and (517/500)^10 < 7/5.
root10_lo = Fraction(517,500)
assert root10_lo**10 < Fraction(7,5)

a = Fraction(563,420) # 7/5 - 1/(12*(7/5))
P6 = sum(a**k / factorial(k) for k in range(7))
gammaU_derived = Fraction(5,7)*sqrt2piU*Fraction(49,25)*Fraction(500,517)/P6
gammaU = Fraction(88869,100000)
assert gammaU_derived < gammaU

# D=134 tail coefficients for thresholds Dt/k, k=1,2,3.
# Formula lower bound:
# A_k >= [2 k (335-k)/2345] * Gamma(7/5)^(-1) * (k^2/112225)^(1/5).
D = 134
A = {
    1: Fraction(31323,1000000),
    2: Fraction(8241,100000),
    3: Fraction(14495,100000),
}
for k, Ak in A.items():
    pref = Fraction(2*k*(335-k),2345) / gammaU
    # Ak < pref * (k^2/112225)^(1/5), checked by fifth powers.
    assert (Ak/pref)**5 < Fraction(k*k,112225)

assert A[1] < A[2] < A[3]
assert A[3] < D # ensures the artificial per-coordinate tail probability is <1 at t=1

# Build the exact polynomial lower bound for the sufficient 3-threshold event:
# at least one Y_i >= Dt, or at least two Y_i >= Dt/2,
# or at least three Y_i >= Dt/3.
# Put x=t^(-7/5), q_k=(A_k/D)x.  The complement has
# N_1=0, N_2<=1, N_3<=2.
a1,a2,a3 = A[1]/D, A[2]/D, A[3]/D
comp = {}
def add(poly, power, val):
    poly[power] = poly.get(power, Fraction(0)) + val

# (1-q3)^D
for j in range(D+1):
    add(comp,j,comb(D,j)*((-a3)**j))
# D(q3-q1)(1-q3)^(D-1)
coef1 = D*(a3-a1)
for j in range(D):
    add(comp,j+1,coef1*comb(D-1,j)*((-a3)**j))
# C(D,2)[(q3-q2)^2+2(q2-q1)(q3-q2)](1-q3)^(D-2)
cat3 = a3-a2
cat2 = a2-a1
coef2 = comb(D,2)*(cat3*cat3 + 2*cat2*cat3)
for j in range(D-1):
    add(comp,j+2,coef2*comb(D-2,j)*((-a3)**j))

# Event polynomial P(x)=1-complement. Constant term cancels.
event = {0: Fraction(1)-comp.get(0,Fraction(0))}
for power,val in comp.items():
    if power:
        event[power] = -val
assert event[0] == 0

# Layer cake: beta = 1/2 integral_1^inf (1-t^-1/2) P(t) dt.
# For x^ell=t^(-7 ell/5), integral = 1/(7ell/5-1)-1/(7ell/5-1/2).
beta = Fraction(0)
for ell,c in event.items():
    if ell == 0:
        continue
    r = Fraction(7*ell,5)
    I = Fraction(1,1)/(r-1) - Fraction(1,1)/(r-Fraction(1,2))
    beta += c*I
beta /= 2
assert beta > 0

# Product-density signing coefficient for p=9/5:
# 3 * [sqrt(pi/2) p/sqrt(p-1)] = 27 sqrt(10*pi)/20.
C_upper = Fraction(27,20)*sqrt10piU*(1-beta)
h_new = Fraction(740179,100000) # 7.40179
assert C_upper < h_new

# Strict active-row count at n=86: d < n^2/h^2, hence d <= ceil(n^2/h^2)-1.
n = 86
ratio = Fraction(n*n,1)/(h_new*h_new)
assert Fraction(134,1) < ratio < Fraction(135,1)
D_active = 134
assert D_active == D

h_old = Fraction(148709,20000) # preceding certified B_R13(86)=7.43545
improvement = h_old-h_new
assert improvement == Fraction(1683,50000) # 0.03366

# A couple of structural sanity checks on the artificial categorical probabilities at t=1.
q1,q2,q3 = a1,a2,a3
assert 0 < q1 < q2 < q3 < 1

print('gammaU_derived_decimal =', float(gammaU_derived))
print('gammaU_derived < 88869/100000 =', gammaU_derived < gammaU)
for k in (1,2,3):
    print(f'A{k}_lower = {A[k]} = {float(A[k])}')
print('beta_134_3threshold_decimal =', float(beta))
print('density_signing_upper_decimal =', float(C_upper))
print('density_signing_upper < 740179/100000 =', C_upper < h_new)
print('h_new =', h_new, '=', float(h_new))
print('86^2/h_new^2_decimal =', float(ratio))
print('134 < 86^2/h_new^2 < 135 =', Fraction(134,1) < ratio < Fraction(135,1))
print('D_active =', D_active)
print('previous_B86 =', h_old, '=', float(h_old))
print('improvement =', improvement, '=', float(improvement))
print('R13_COSPOWER_3THRESHOLD_EXACT_PASS')
