from fractions import Fraction as F
from math import factorial

print("HARD7-03 exact four-step pair-overlap Chernoff certificate")


def M2(z, t):
    z = abs(z)
    if z == 2:
        return F(1, 1) / (1 - t) ** 2
    if z == 1:
        return F(2, 1) / ((1 - t) ** 2 * (2 - t))
    if z == 0:
        return F(6, 1) / ((1 - t) ** 2 * (2 - t) * (3 - t))
    raise ValueError("z must be 0,1,2 in absolute value")


def A3(t):
    num = F(2, 1) * (
        F(2268, 1)
        - F(4408, 1) * t
        + F(3748, 1) * t**2
        - F(1918, 1) * t**3
        + F(652, 1) * t**4
        - F(143, 1) * t**5
        + F(18, 1) * t**6
        - t**7
    )
    den = (3 - t) ** 4 * (2 - t) ** 3 * (1 - t) ** 3
    return num / den


def pair_correction(t):
    # Across all fourth-step endpoints, the chain-pair corrections use
    # four common predecessors of each type |z|=0,1,2.
    # min(C1,C2) for iid Exp(1) is Exp(2), whose theta-MGF is 2/(2-theta).
    return F(8, 1) / (2 - t) * (M2(0, t) + M2(1, t) + M2(2, t))


def U4(t):
    # Sum of fourth-step endpoint MGFs after pair-overlap correction.
    return (F(3, 1) * A3(t) - pair_correction(t)) / (1 - t)


theta = F(147, 250)
a = F(29711, 10000)
x = F(4, 1) * theta * a
u4 = U4(theta)
s20 = sum(x**k / factorial(k) for k in range(21))

old_L = F(250, 2989)
new_L = F(2500, 29711)
gain = new_L - old_L

print(f"theta = {theta}")
print(f"a = {a}")
print(f"A3(theta) = {A3(theta)}")
print(f"M2(0;theta) = {M2(0, theta)}")
print(f"M2(1;theta) = {M2(1, theta)}")
print(f"M2(2;theta) = {M2(2, theta)}")
print(f"pair_correction(theta) = {pair_correction(theta)}")
print(f"U4(theta) = {u4}")
print(f"4*theta*a = {x}")
print(f"S20(4*theta*a)-U4(theta) = {s20 - u4}")
print(f"old_L = {old_L}")
print(f"new_L = {new_L}")
print(f"metric_gain = {gain}")

print(f"U4_float = {float(u4):.15f}")
print(f"taylor_margin_float = {float(s20 - u4):.15f}")
print(f"old_L_float = {float(old_L):.15f}")
print(f"new_L_float = {float(new_L):.15f}")
print(f"metric_gain_float = {float(gain):.15f}")

assert F(0, 1) < theta < F(1, 1)
assert M2(0, theta) > M2(1, theta) > M2(2, theta) > 0
assert pair_correction(theta) > 0
assert u4 > 0
assert s20 - u4 > 0
assert new_L > old_L
assert gain == F(44750, 88806179)

print("ALL_EXACT_CHECKS_PASS = True")
