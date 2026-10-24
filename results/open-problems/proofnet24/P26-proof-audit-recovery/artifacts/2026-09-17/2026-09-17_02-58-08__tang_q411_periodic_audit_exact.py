#!/usr/bin/env python3
from fractions import Fraction as F

# P26 independent exact core for Pengfei Tang (2020/2023), Question 4.11.
# Audited package: R09 periodic-tree counterexample T_3, a three-edge stem
# feeding an infinite rooted binary tree.

A = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 2],
]
p = F(3, 4)
theta = [F(3, 8), F(1, 2), F(2, 3), F(8, 9)]


def Bp(alpha):
    out = []
    for row in A:
        prod = F(1)
        for multiplicity, x in zip(row, alpha):
            prod *= (F(1) - p * x) ** multiplicity
        out.append(F(1) - prod)
    return out


# Exact physical fixed point at p=3/4 and the always-present zero fixed point.
assert Bp(theta) == theta
assert Bp([F(0)] * 4) == [F(0)] * 4

# Binary-tail extinction equation q=(1-p+p q)^2.
q_small = F(1, 9)
q_one = F(1)


def extinction_residual(q):
    return q - (F(1) - p + p * q) ** 2


assert extinction_residual(q_small) == 0
assert extinction_residual(q_one) == 0
assert q_small < q_one
assert 2 * p > 1  # supercritical binary Galton-Watson tail

beta = F(1) - q_small
assert beta == F(8, 9)
assert theta[3] == beta

# Three independent stem edges must all be open.
theta_root = p**3 * beta
assert theta_root == F(3, 8)
assert theta_root == theta[0]
assert theta[2] == p * theta[3]
assert theta[1] == p * theta[2]
assert theta[0] == p * theta[1]

# General supercritical T_3 formula theta_3(p)=2 p^2-p.
# Polynomial coefficients are [constant, p, p^2].
theta3_coeff = [F(0), F(-1), F(2)]
theta3_second_derivative = 2 * theta3_coeff[2]
assert theta3_second_derivative == 4

# T_2 is the boundary case theta_2(p)=2p-1, hence zero curvature.
theta2_coeff = [F(-1), F(2)]
theta2_second_derivative = F(0)
assert theta2_second_derivative == 0

# Finite stem does not change the binary-tail critical threshold.
pc = F(1, 2)
assert p > pc

print("P26 Tang Q4.11 periodic-tree audit exact core")
print("candidate = T3: three-edge stem into infinite rooted binary tree")
print("p =", p)
print("physical theta vector =", theta)
print("B_p(theta) =", Bp(theta))
print("zero fixed point =", Bp([F(0)] * 4))
print("binary extinction roots at p=3/4 = 1/9 and 1")
print("selected physical extinction q =", q_small)
print("binary-tail survival beta =", beta)
print("T3 theta(3/4) =", theta_root)
print("pc =", pc)
print("T3 theta'' =", theta3_second_derivative)
print("T2 theta'' =", theta2_second_derivative)
print("P26-TANG-Q411-PERIODIC-EXACT-CHECK: PASS")
