from fractions import Fraction as F
from itertools import permutations
from math import factorial

# HARD7-03 exact nested-pair kernel certificate.
# This checker imports the already-certified U4_common rational from the
# immutable 20260919T1418Z checkpoint, then verifies the new exact
# edge/near-edge pair transforms and the improved Chernoff certificate.

theta = F(723, 1250)
q = F(1) - theta
a = F(2) - theta
b = F(3) - theta

# Linear forms in ordered exponential spacings u,v,w.
U = (F(1), F(0), F(0))
V = (F(0), F(1), F(0))
W = (F(0), F(0), F(1))
ordered = [
    U,
    tuple(U[i] + V[i] for i in range(3)),
    tuple(U[i] + V[i] + W[i] for i in range(3)),
]

def add(*vs):
    return tuple(sum((v[i] for v in vs), F(0)) for i in range(3))

def sub(v, w):
    return tuple(v[i] - w[i] for i in range(3))

def scale(c, v):
    return tuple(c * v[i] for i in range(3))

def integ_exp(L, w_power=0):
    rates = [-x for x in L]
    assert all(r > 0 for r in rates), (L, rates)
    if w_power == 0:
        return F(1) / (rates[0] * rates[1] * rates[2])
    assert w_power == 1
    return F(1) / (rates[0] * rates[1] * rates[2]**2)

# Exact transform E exp(S-qT) for the edge nested pair.
E_edge = (F(5)*theta**2 - F(14)*theta + F(10)) / (a**4 * q**2)

# Exact transform E exp(S-qT) for the near-edge nested pair.
# On each order cone of (A_-1,A_0,A_1), write
# low=u, mid=u+v, high=u+v+w.
c0 = F(1)/q - q/(a*a)
c1 = F(2)*q/(a*b)

def near_transform():
    total = F(0)
    pieces = []
    for order in permutations(range(3)):
        vals = [None]*3
        for rank, varidx in enumerate(order):
            vals[varidx] = ordered[rank]
        x, y, z = vals  # A_-1, A_0, A_1
        rank = {var: order.index(var) for var in range(3)}
        m = x if rank[0] > rank[1] else y
        d = sub(y, x) if rank[1] > rank[0] else (F(0), F(0), F(0))
        D = sub(z, m) if rank[2] > max(rank[0], rank[1]) else (F(0), F(0), F(0))
        density_sum = add(x, y, z)

        # e^{-qD}[(1+e^{-d})(D/a + 1/q-q/a^2)-2e^{-d}/a]
        base = add(scale(theta, m), scale(F(-1), density_sum), scale(-q, D))
        val = c0 * integ_exp(base)
        if D != (F(0), F(0), F(0)):
            assert D == W
            val += F(1)/a * integ_exp(base, 1)

        base_d = add(base, scale(F(-1), d))
        val += (c0 - F(2)/a) * integ_exp(base_d)
        if D != (F(0), F(0), F(0)):
            val += F(1)/a * integ_exp(base_d, 1)

        # + 2q e^{-d-aD}/[a b]
        base3 = add(scale(theta, m), scale(F(-1), density_sum),
                    scale(F(-1), d), scale(-a, D))
        val += c1 * integ_exp(base3)

        assert val > 0
        pieces.append((order, val))
        total += val
    return total, pieces

E_near, pieces = near_transform()

# Common-window moments from the preceding exact checkpoint.
J_edge = F(1)/q**2
J_out = (F(8) - F(5)*theta)/(a**3*q**2)
J_in = F(2)*(F(12) - F(7)*theta)/(b*a**3*q**2)

# Exact two-clock kernel:
# P = q^{-1}[ E e^{theta S} - theta/a E e^{S-qT} ].
P_edge = (J_edge - theta/a * E_edge)/q
P_near = (J_out - theta/a * E_near)/q

# Previous common-window pair lower bounds for the same classes.
Q_edge = F(2)/a * J_edge
Q_near = F(2)/a * J_out
Q_center = F(2)/a * J_in

assert P_edge > Q_edge
assert P_near > Q_near

# Two reflections of each type, and each adjacent pair is counted in two
# fourth-step predecessor windows.
delta_C = F(4) * ((P_edge - Q_edge) + (P_near - Q_near))
assert delta_C > 0

# Immutable prior exact value:
# artifacts/.../common_overlap_pair_correction_20260919T1418Z.out
U4_common = F(
    471848329119416840838853418325986387230949832280273437500000,
    533551258662847599879934006185557225047638076531060575909,
)

# Increasing the pair subtraction by delta_C lowers U4 by delta_C/q.
U4_nested = U4_common - delta_C/q
assert U4_nested < U4_common

# New shape target and exact truncated-exp lower bound.
A_old = F(2932597567, 1000000000)
A_new = F(7314597, 2500000)
assert A_new < A_old
x = F(4)*theta*A_new
S32 = sum(x**k / F(factorial(k)) for k in range(33))
margin = S32 - U4_nested
assert margin > 0

# Because S32(x)<exp(x), U4_nested<exp(4 theta A_new).
L_old = F(250000000, 2932597567)
L_new = F(1)/(F(4)*A_new)
assert L_new == F(625000, 7314597)
assert L_new > L_old

print("HARD7-03 exact nested-pair kernel certificate")
print(f"theta = {theta}")
print(f"E_edge = {E_edge}")
print(f"E_near = {E_near}")
for order, val in pieces:
    print(f"near_order_{order} = {val}")
print(f"P_edge = {P_edge}")
print(f"Q_edge = {Q_edge}")
print(f"edge_pair_gain = {P_edge-Q_edge}")
print(f"P_near = {P_near}")
print(f"Q_near = {Q_near}")
print(f"near_pair_gain = {P_near-Q_near}")
print(f"Q_center_retained = {Q_center}")
print(f"delta_C = {delta_C}")
print(f"U4_common = {U4_common}")
print(f"U4_nested = {U4_nested}")
print(f"A_old = {A_old}")
print(f"A_new = {A_new}")
print(f"x = {x}")
print(f"S32_minus_U4_nested = {margin}")
print(f"L_old = {L_old}")
print(f"L_new = {L_new}")
print(f"metric_gain = {L_new-L_old}")
print(f"E_edge_float = {float(E_edge):.15f}")
print(f"E_near_float = {float(E_near):.15f}")
print(f"P_edge_float = {float(P_edge):.15f}")
print(f"P_near_float = {float(P_near):.15f}")
print(f"delta_C_float = {float(delta_C):.15f}")
print(f"U4_nested_float = {float(U4_nested):.15f}")
print(f"A_new_float = {float(A_new):.15f}")
print(f"S32_minus_U4_nested_float = {float(margin):.15e}")
print(f"L_new_float = {float(L_new):.15f}")
print(f"metric_gain_float = {float(L_new-L_old):.15e}")
print("ALL_EXACT_CHECKS_PASS = True")