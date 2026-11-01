from fractions import Fraction as F
from itertools import permutations
from math import factorial

print("HARD7-03 exact order-cone target-domination certificate")

# Existing exact quantities from the verified four-step chain.
def A3(t):
    return F(2) * (
        F(2268) - F(4408)*t + F(3748)*t**2 - F(1918)*t**3
        + F(652)*t**4 - F(143)*t**5 + F(18)*t**6 - t**7
    ) / ((F(3)-t)**4 * (F(2)-t)**3 * (F(1)-t)**3)

def M2(z, t):
    z = abs(z)
    if z == 2:
        return F(1) / (F(1)-t)**2
    if z == 1:
        return F(2) / ((F(1)-t)**2 * (F(2)-t))
    if z == 0:
        return F(6) / ((F(1)-t)**2 * (F(2)-t) * (F(3)-t))
    raise ValueError(z)

def pair_correction(t):
    return F(8)/(F(2)-t) * (M2(0,t) + M2(1,t) + M2(2,t))

def kappa(t):
    return t / ((F(2)-t)*(F(3)-t))

# Integral over one ordering cone 0 <= x1 <= x2 <= x3 for iid Exp(1)
# variables, after an exponential tilt exp(c1 x1+c2 x2+c3 x3).
def ordered_exp_integral(c):
    c1,c2,c3 = c
    r1 = F(3) - (c1+c2+c3)
    r2 = F(2) - (c2+c3)
    r3 = F(1) - c3
    assert r1 > 0 and r2 > 0 and r3 > 0
    return F(1)/(r1*r2*r3)

A_VARS = (-1,0,1)

# bases[label] is the subset of first-layer A-variables whose maximum is
# the deterministic base u_label of Y_label=u_label+B_label.
#
# Conditional on the bases u, the weighted probability that target i is
# the largest shifted exponential is
#
# e^{u_i} sum_{S subset competitors} (-1)^|S|
#   e^{sum_{j in S}u_j} e^{-(1-t+|S|)M}/(1-t+|S|),
#
# M=max_j u_j.
# On each of the six A-ordering cones, every u_j and M equals one of
# x1,x2,x3, so the remaining integral is exactly ordered_exp_integral.
def weighted_target_max(t, bases, target):
    labels = list(bases)
    competitors = [j for j in labels if j != target]
    total = F(0)
    for perm in permutations(A_VARS):
        rank = {var:i for i,var in enumerate(perm)}
        base_rank = {
            label:max(rank[v] for v in subset)
            for label,subset in bases.items()
        }
        M_rank = max(base_rank.values())
        for mask in range(1 << len(competitors)):
            S = [
                competitors[k] for k in range(len(competitors))
                if (mask >> k) & 1
            ]
            q = F(1) - t + len(S)
            c = [F(0),F(0),F(0)]
            c[base_rank[target]] += 1
            for j in S:
                c[base_rank[j]] += 1
            c[M_rank] -= q
            term = ordered_exp_integral(c) / q
            total += -term if len(S) % 2 else term
    return total

# d=2 edge: it is enough that Y_2 >= Y_1.
BASES_2 = {
    2:{1},
    1:{0,1},
}
# d=1: Y_1 must dominate Y_-1,Y_0,Y_2.
BASES_1 = {
    1:{0,1},
    -1:{-1,0},
    0:{-1,0,1},
    2:{1},
}
# d=0: Y_0 must dominate all other layer-two endpoints.
BASES_0 = {
    0:{-1,0,1},
    -2:{-1},
    -1:{-1,0},
    1:{0,1},
    2:{1},
}

theta = F(47,80)
a = F(9273,3125)  # 2.96736

W2 = weighted_target_max(theta, BASES_2, 2)
W1 = weighted_target_max(theta, BASES_1, 1)
W0 = weighted_target_max(theta, BASES_0, 0)

# Independent closed form for W2, derived directly by conditioning on
# A1,A0,B1 and integrating B2 from the exact threshold.
W2_closed = (F(3)-F(2)*theta) / (
    (F(1)-theta)**2 * (F(2)-theta)**3
)
assert W2 == W2_closed

H_dom = kappa(theta) * (F(2)*W2 + F(2)*W1 + W0)

# The previous sufficient-event lower bounds are included only to certify
# strict improvement of the new target-domination event family.
def J(m,t):
    den = F(1)
    for j in range(1,m+1):
        den *= F(j)-t
    return F(factorial(m-1),1)/den

H_old = kappa(theta) * (
    F(2)*J(2,theta)**2
    + F(2)*J(3,theta)*J(4,theta)
    + J(3,theta)*J(5,theta)
)
assert H_dom > H_old

U4 = (F(3)*A3(theta) - pair_correction(theta) - H_dom) / (F(1)-theta)

x = F(4)*theta*a
S20 = sum(x**k / F(factorial(k),1) for k in range(21))
margin = S20 - U4
assert margin > 0
# S20(x) < exp(x), so U4*exp(-x)<1.

old_L = F(12500,148461)
new_L = F(1)/(F(4)*a)
gain = new_L-old_L
assert new_L == F(3125,37092)
assert gain > 0

print(f"theta = {theta}")
print(f"a = {a}")
print(f"W2 = {W2}")
print(f"W1 = {W1}")
print(f"W0 = {W0}")
print(f"W2_closed = {W2_closed}")
print(f"H_old = {H_old}")
print(f"H_dom = {H_dom}")
print(f"H_gain = {H_dom-H_old}")
print(f"U4 = {U4}")
print(f"U4_float = {float(U4):.15f}")
print(f"x = 4*theta*a = {x}")
print(f"S20_minus_U4 = {margin}")
print(f"S20_minus_U4_float = {float(margin):.15f}")
print(f"old_L = {old_L}")
print(f"new_L = {new_L}")
print(f"metric_gain = {gain}")
print(f"new_L_float = {float(new_L):.15f}")
print("ALL_EXACT_CHECKS_PASS = True")
