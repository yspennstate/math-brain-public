from fractions import Fraction as F
from math import sqrt, pi

alpha = F(1,128)
A3 = [
    [F(-1,4), F(3,4),  F(-1,4), F(-1,4)],
    [F(3,4),  F(-1,4), F(-1,4), F(-1,4)],
    [F(-1,4), F(-1,4), F(3,4),  F(-1,4)],
    [F(-1,4), F(-1,4), F(-1,4), F(3,4)],
]
A = [[A3[i][j] + alpha*F(1,4) for j in range(4)] for i in range(4)]

def mv(M,x):
    return [sum(M[i][j]*x[j] for j in range(4)) for i in range(4)]

eigvecs = [
    ([F(1),F(1),F(1),F(1)], alpha),
    ([F(1),F(-1),F(0),F(0)], F(-1)),
    ([F(1),F(1),F(-1),F(-1)], F(1)),
    ([F(0),F(0),F(1),F(-1)], F(1)),
]
for x, lam in eigvecs:
    assert mv(A,x) == [lam*t for t in x]
print("A_alpha exact spectrum certificate: {1,1,-1,1/128}: PASS")

r, s, t = A[0][0], A[0][2], A[2][2]
detH = r*t-s*s
assert (r,s,t,detH) == (F(-127,512),F(-127,512),F(385,512),F(-127,512))
D = -detH
tau = r+t
assert 4*D > tau + F(1,4)  # equivalent to sigma_min(H)>1/4 for this indefinite 2x2 block
print("full-matrix pair H(1,3): r=%s s=%s t=%s det=%s; kappa>1/4: PASS" % (r,s,t,detH))

# Exact-rank-three core partner resource.
core_r = A3[0][0]
Delta13 = F(3,4)*F(3,4)-F(-1,4)*F(-1,4)
assert core_r == F(-1,4) and Delta13 == F(1,2)
C_partner = 16*sqrt(15)*(2**0.25) * (float(abs(core_r)*Delta13))**(-0.25)
print("fleet03/B06 core bound = %.12f (<124)" % C_partner)

# Weighted scalar-conditioning envelope for iid Uniform[0,1]^4.
# Corner conditional trace cap: 3*pi*sqrt(3)/s^2; Irwin-Hall corner density: s^3/6.
corner = pi*sqrt(3)/4
middle = 9*pi * F(11,12)
W = 2*corner + float(middle)
assert W < 29
print("weighted envelope bound = pi*(33/4+sqrt(3)/2) = %.12f (<29)" % W)

# The stronger scalar-conditioning supremum fails: support width <= (3/2)s^2.
for s0 in [F(1,10), F(1,100), F(1,1000)]:
    lower = F(2,3) / (s0*s0)
    print("s=%s: conditional-sup lower bound >= %.6f" % (s0, float(lower)))

# Current arbitrary-rank pair theorem gives a coarse law-uniform certificate on A_alpha.
# D>1/5 and kappa>1/4 imply D^2*kappa>1/100.
C_full = 3*(400**(1/3))*(100**(1/6))
assert C_full < 48
print("full-matrix pair theorem coarse bound < %.12f (<48)" % C_full)

# Singleton + two independent spectral banks: local pair inversion loses m^(1/4),
# while grouping yields pi*sqrt(2) uniformly.
for m in [4,16,256]:
    local = 16*sqrt(15)*(2**0.25)*(m**0.25)
    grouped = pi*sqrt(2)
    print("bank m=%d: partner single-pair <= %.6f; grouped <= %.6f" % (m,local,grouped))

print("PASS")
