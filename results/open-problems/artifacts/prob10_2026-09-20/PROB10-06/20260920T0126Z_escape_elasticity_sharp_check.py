from fractions import Fraction as F
from math import comb

# PROB10-06 exact-arithmetic self-check for the escape-elasticity sharpening.
# No floating-point quantity is used in an assertion.

def a_sharp(lam):
    return F(2,1)/((F(2)-lam)*(F(4)-lam)) - F(6,1)/((F(3)-lam)*(F(9)-lam))

def a_old(lam):
    return F(2,1)/((F(2)-lam)*(F(4)-lam)) - F(3,1)/(F(9)-lam)

def b(lam):
    return lam*a_sharp(lam)

def b_old(lam):
    return lam*a_old(lam)

def H(x):
    # H(x)<0 for x>5 iff x<5+2sqrt(6).
    return x*x - 10*x + 1

# Direct symbolic simplification gives
# b'(lambda)=2*N(lambda) /
# [(lambda-9)^2(lambda-4)^2(lambda-3)^2(lambda-2)^2].
# Certify N>0 on lambda in [1,2] by positive Bernstein coefficients
# for N(1+x), x in [0,1].
power = [F(1090), F(-826), F(-525), F(600), F(-145), F(0), F(2)]
bernstein = []
n = 6
for k in range(n+1):
    bernstein.append(sum(
        power[j] * F(comb(k,j), comb(n,j))
        for j in range(k+1)
    ))
expected_bernstein = [
    F(1090), F(2857,3), F(2339,3), F(602),
    F(1319,3), F(910,3), F(196)
]
assert bernstein == expected_bernstein
assert all(x > 0 for x in bernstein)
assert b(F(1)) == F(7,24)

# Unique sharp threshold bracket.
lo = F(92367,50000)  # 1.84734
hi = F(36947,20000)  # 1.84735
Hlo = H(b(lo))
Hhi = H(b(hi))
assert Hlo == F(-2078280487807137641230229997699671,
                393343078158007832889703683428300329)
assert Hhi == F(532969554220686987050919219699361,
                187892431806720794125922020689299361)
assert Hlo < 0 < Hhi

# Clean closed endpoint L=1.847.
L = F(1847,1000)
bL = b(L)
HL = H(bL)
assert bL == F(26815418308000,2716770751281)
assert HL == F(-2065939077356906498339039,
               7380843315015929163140961)
assert HL < 0

# The previous lower-elasticity input does NOT certify L=1.847,
# demonstrating that this is a genuine certificate improvement.
HoldL = H(b_old(L))
assert HoldL == F(31018230514982569420,5551973331770680929)
assert HoldL > 0

# Uniform all-mixture derivative margin on 1 <= lambda <= L.
# For d=2, theta in [0,1], M=2+theta, and b<=b(L).
# min_theta [2+theta-b theta(1-theta)]
# = 2-(b-1)^2/(4b), because b(L)>1.
m = F(2) - (bL-F(1))**2/(F(4)*bL)
assert m == F(2065939077356906498339039,
              291405376570157767410192000)
assert m > 0
delta = F(2)*m/(F(3)+L)**2
assert delta == F(258242384669613312292379875,
                  427881606035108351518406964033)
assert delta > 0

print("PASS")
print("bernstein_coefficients_N(1+x)=", bernstein)
print("b(1)=", b(F(1)))
print("root_bracket=(92367/50000,36947/20000)")
print("H_at_lower=", Hlo)
print("H_at_upper=", Hhi)
print("L=", L)
print("b_sharp(L)=", bL)
print("H_sharp(L)=", HL)
print("H_old(L)=", HoldL)
print("uniform_bracket_margin_m=", m)
print("uniform_-ell_prime_lower=", delta)
