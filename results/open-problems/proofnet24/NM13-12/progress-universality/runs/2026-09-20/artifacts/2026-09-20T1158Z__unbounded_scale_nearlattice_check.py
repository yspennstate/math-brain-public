#!/usr/bin/env python3
import math
from fractions import Fraction

# NM13-12 unbounded-scale near-lattice sanity checker.
# Explicit application: S=1+E, E~Exp(1), sigma_m=m^{-1/3}.

momE = {j: math.factorial(j) for j in range(5)}
mu2 = sum(math.comb(2,j)*momE[j] for j in range(3))
mu4 = sum(math.comb(4,j)*momE[j] for j in range(5))
print("MU2", mu2)
print("MU4", mu4)
assert mu2 == 5 and mu4 == 65

varY = mu2
fourthY = 3*mu4
gauss4 = 3*mu2**2
print("NOISE_VAR", varY)
print("NOISE_FOURTH", fourthY)
print("NOISE_GAUSS_SAME_FOURTH", gauss4)
print("NOISE_FOURTH_CUMULANT", fourthY-gauss4)
assert fourthY-gauss4 == 120

def entry_fourth(sigma):
    t = sigma*sigma
    return (1+30*t+195*t*t)/(1+5*t)**2

for sig in [1.0, 0.5, 0.1, 0.01]:
    print("ENTRY_FOURTH", sig, entry_fourth(sig))
assert abs(entry_fourth(1.0)-float(Fraction(113,18))) < 1e-15
for t in [0.0, 0.01, 0.1, 1.0]:
    deriv = 20*(1+12*t)/(1+5*t)**3
    assert deriv > 0
print("ENTRY_FOURTH_UNIFORM_BOUND", float(Fraction(113,18)))

def rho(m):
    sig = m**(-1/3)
    return sig/math.sqrt(1+5*sig*sig)

def rs1(m):
    r = rho(m)
    return m*r*r/math.log(math.e/r)

for m in [10**3,10**6,10**9,10**12]:
    print("RATE", m, "rho", rho(m), "m_rho2_over_log", rs1(m))
print("RS1_TENDS_INF_ANALYTIC exponent m^(1/3)/log m")

def rs2ratio(m):
    k = m**0.8/(math.log(m)**2)
    r = rho(m)
    return k*(math.log(m)+math.log(math.e/r))/m

for m in [10**6,10**9,10**12]:
    print("RS2_EXAMPLE", m, rs2ratio(m))

pS = 1-math.exp(-1)  # P(1+Exp(1) <= 2)
for q in [1,2,4,8]:
    c = (pS/2)**q/(2*math.sqrt(2*math.pi*q))
    print("CONV_LOWER_CONST_q", q, c)
    assert c > 0

Bxi = float(Fraction(113,18))
qhalf = math.sqrt(1-1/(2*Bxi+6))
print("Q_X_HALF_BOUND", qhalf)
assert qhalf < 1

for m in [10**6,10**12,10**24]:
    sig = math.log(math.log(m))*math.sqrt(math.log(m)/m)
    r = sig/math.sqrt(1+5*sig*sig)
    ratio = m*r*r/math.log(math.e/r)
    print("NEAR_CRIT", m, sig, ratio)

print("ALL_UNBOUNDED_SCALE_NEARLATTICE_CHECKS_PASS")
