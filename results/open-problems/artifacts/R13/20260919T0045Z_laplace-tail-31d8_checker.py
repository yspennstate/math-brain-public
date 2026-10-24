from fractions import Fraction as F
from math import comb

# R13 exact checker: Laplace-tail finite-dimensional Jensen defect.
# All acceptance tests below use Fraction exact arithmetic.

D = 135
n = 86
old_h = F(739377, 100000)
new_h = F(739097, 100000)

# Retained analytic lemma from the preceding Gautschi-certified R13 package:
# Gamma(7/5) < 4437/5000. We verify that it implies
# c=(2/5)^(7/5)/Gamma(7/5) > 39/125 by a fifth-power comparison.
gamma_upper = F(4437, 5000)
c0 = F(39, 125)
assert F(2,5)**7 > (c0 * gamma_upper)**5

# D^(-2/5) > 1757/12500, again by exact fifth powers.
d0 = F(1757, 12500)
assert d0**5 < F(1, D**2)

# Rational square-root majorants used later.
# pi < 355/113 is classical.
pi_upper = F(355, 113)
sqrt_pi_upper = F(1773, 1000)
sqrt_10pi_upper = F(1121, 200)
assert sqrt_pi_upper**2 > pi_upper
assert sqrt_10pi_upper**2 > 10*pi_upper

# Lower exponent R(t) valid for 0 <= t <= 10:
# R(t)=a1*t^(7/5)-a3*t^2-a2*t^(12/5).
ac = c0*d0
a1 = ac*F(25,14)
a2 = ac*F(1,1134)
a3 = F(1,250)

# R(t)>=0 on [0,10]: factor t^(7/5) and use t^(3/5)<=4.
positive_bracket = ac*(F(25,14)-F(10,1134)) - F(4,250)
assert positive_bracket > 0

# Integrate exactly after t=u^10, on 0<=u<=5/4.
# Then T=(5/4)^10<10, and t^(-3/2) dt = 10 u^(-6) du.
u0 = F(5,4)
T = u0**10
assert T < 10

def padd(p,q):
    out = dict(p)
    for e,c in q.items():
        out[e] = out.get(e,F(0)) + c
    return {e:c for e,c in out.items() if c}

def pscale(p,c):
    return {e:v*c for e,v in p.items() if v*c}

def pmul(p,q):
    out = {}
    for e,a in p.items():
        for f,b in q.items():
            out[e+f] = out.get(e+f,F(0)) + a*b
    return {e:c for e,c in out.items() if c}

# Under t=u^10:
# t^(7/5)=u^14, t^2=u^20, t^(12/5)=u^24.
R = {14:a1, 20:-a3, 24:-a2}
Rplus = padd(R, pscale(pmul(R,R), F(1,2)))

# e^(-t) >= (1-t/100)^100.
W = {10*k: F(((-1)**k)*comb(100,k), 100**k) for k in range(101)}
P = pmul(W,Rplus)

# Multiply by 10*u^(-6) and integrate term-by-term exactly.
I = F(0)
for e,c in P.items():
    power = e-6
    assert power >= 0
    I += 10*c*u0**(power+1)/F(power+1,1)

assert I > 0

# 1/(2 sqrt(pi)) > 500/1773.
delta_lower = I * F(500,1773)

# Directional-TV signing constant:
# (27 sqrt(10 pi)/20) * (1-delta).
prefactor_upper = F(27,20)*sqrt_10pi_upper
C_upper = prefactor_upper*(1-delta_lower)
assert C_upper < new_h

# Active-row pruning at n=86 requires at most D=135 active rows.
ratio = F(n*n,1)/(new_h*new_h)
assert F(135,1) < ratio < F(136,1)

assert new_h < old_h
improvement = old_h-new_h
assert improvement == F(7,2500)  # 0.0028

print("gamma_consequence_c0 =", float(c0))
print("D_minus_2_over_5_lower =", float(d0))
print("T =", float(T))
print("exact_integral_I =", float(I))
print("delta_lower =", float(delta_lower))
print("directional_TV_C135_upper =", float(C_upper))
print("new_h =", float(new_h))
print("86^2/new_h^2 =", float(ratio))
print("exact_improvement =", float(improvement))
print("R13_LAPLACE_TAIL_EXACT_PASS")
