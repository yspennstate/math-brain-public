from fractions import Fraction as F
from math import factorial

# HARD7-03 exact two-step block Chernoff certificate.
#
# For the homogeneous K=2 lazy-LPP representation, group paths into
# two-step time blocks. For a fixed two-step displacement d:
# d=+-2: one path;
# d=+-1: final weight + max of 2 first-layer exponentials;
# d=0: final weight + max of 3 first-layer exponentials.
#
# If E_i are iid Exp(1), then
# H_m(theta)=E exp(theta max_{1<=i<=m} E_i)
#            = m! / prod_{j=1}^m (j-theta), theta<1.
# Summing the fixed-boundary-sequence Chernoff weights over all block
# displacements gives A_2(theta). If exp(2 theta a) > A_2(theta),
# the two-step union/Chernoff bound is summable and the central
# homogeneous shape constant G_1(0) is at most a.

theta = F(16, 25)
a_hi = F(61903, 20000)

def H(m, th):
    out = F(factorial(m), 1)
    for j in range(1, m + 1):
        out /= F(j, 1) - th
    return out

m1 = H(1, theta)
h2 = H(2, theta)
h3 = H(3, theta)

M2 = m1 * m1                   # displacement +/-2
M1 = m1 * h2                   # displacement +/-1
M0 = m1 * h3                   # displacement 0
A2 = 2 * M2 + 2 * M1 + M0

A2_closed = (
    F(1, 1) / (F(1, 1) - theta) ** 2
    * (
        F(2, 1)
        + F(4, 1) / (F(2, 1) - theta)
        + F(6, 1) / ((F(2, 1) - theta) * (F(3, 1) - theta))
    )
)
assert A2 == A2_closed

x = 2 * theta * a_hi

# For x>0, S_N(x)=sum_{k=0}^N x^k/k! is a strict lower bound on exp(x).
N = 15
S = F(0, 1)
term = F(1, 1)
for k in range(N + 1):
    if k == 0:
        term = F(1, 1)
    elif k > 0:
        term *= x / k
    S += term

gap = S - A2
assert x > 0
assert gap > 0

old_L = F(500000, 6578563)
new_L = F(1, 4) / a_hi  # binary Q has numerator 1-r E[1/alpha]=1/4
assert new_L == F(5000, 61903)
movement = new_L - old_L
assert movement > 0

print("HARD7-03 exact two-step homogeneous K=2 block certificate")
print(f"theta = {theta}")
print(f"a_hi = {a_hi}")
print(f"H1 = {m1}")
print(f"H2 = {h2}")
print(f"H3 = {h3}")
print(f"M_|d|=2 = {M2}")
print(f"M_|d|=1 = {M1}")
print(f"M_d=0 = {M0}")
print(f"A2(theta) = {A2}")
print(f"x = 2*theta*a_hi = {x}")
print(f"Taylor_degree = {N}")
print(f"S_{N}(x)-A2(theta) = {gap}")
print("Therefore exp(2*theta*a_hi) > A2(theta) exactly.")
print(f"old_L = {old_L}")
print(f"new_L = {new_L}")
print(f"movement = {movement}")
print("ALL_EXACT_CHECKS_PASS = True")
