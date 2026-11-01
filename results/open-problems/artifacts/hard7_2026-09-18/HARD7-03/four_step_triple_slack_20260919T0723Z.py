from fractions import Fraction as F
from math import factorial, comb

print("HARD7-03 exact four-step triple-slack correction certificate")


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


def J(m, t):
    # E[e^{tX_1} 1{X_1=max(X_1,...,X_m)}] for iid Exp(1).
    den = F(1)
    for j in range(1, m+1):
        den *= F(j)-t
    closed = F(factorial(m-1), 1) / den
    expanded = sum(
        F((-1)**k * comb(m-1, k), 1) / (F(k+1)-t)
        for k in range(m)
    )
    assert closed == expanded
    return closed


def kappa(t):
    # If A=min(C_1,C_3)~Exp(2), B=C_2~Exp(1), independent, then
    # E[(e^{tA}-e^{tB})_+] = t/((2-t)(3-t)).
    term_a = F(2)/(F(2)-t) - F(2)/(F(3)-t)
    term_b = F(1)/(F(3)-t)
    integral = term_a - term_b
    closed = t / ((F(2)-t)*(F(3)-t))
    assert integral == closed
    return closed


theta = F(5877, 10000)
a = F(148461, 50000)   # 2.96922

# Missing-slack lower bounds for the five three-predecessor fourth-step endpoints.
# d=+/-2: domination event uses two independent two-way maxima.
H2 = kappa(theta) * J(2,theta) * J(2,theta)
# d=+/-1: force the layer-2 endpoint Y_1 to dominate its four relevant competitors.
H1 = kappa(theta) * J(3,theta) * J(4,theta)
# d=0: force Y_0 to dominate the entire five-endpoint layer-2 profile.
H0 = kappa(theta) * J(3,theta) * J(5,theta)
H_total = F(2)*H2 + F(2)*H1 + H0

U4_pair = (F(3)*A3(theta) - pair_correction(theta)) / (F(1)-theta)
U4_refined = (F(3)*A3(theta) - pair_correction(theta) - H_total) / (F(1)-theta)
assert U4_refined < U4_pair

x = F(4)*theta*a
S21 = sum(x**k / F(factorial(k),1) for k in range(22))
margin = S21 - U4_refined
assert margin > 0
# Since S21(x) < exp(x) for x>0, U4_refined * exp(-x) < 1.

old_L = F(2500, 29711)
new_L = F(1,1) / (F(4)*a)
gain = new_L - old_L
assert new_L == F(12500, 148461)
assert gain > 0

print(f"theta = {theta}")
print(f"a = {a}")
print(f"A3(theta) = {A3(theta)}")
print(f"pair_correction(theta) = {pair_correction(theta)}")
for m in (2,3,4,5):
    print(f"J{m}(theta) = {J(m,theta)}")
print(f"kappa(theta) = {kappa(theta)}")
print(f"H2 = {H2}")
print(f"H1 = {H1}")
print(f"H0 = {H0}")
print(f"H_total = {H_total}")
print(f"U4_pair = {U4_pair}")
print(f"U4_refined = {U4_refined}")
print(f"U4_pair_float = {float(U4_pair):.15f}")
print(f"U4_refined_float = {float(U4_refined):.15f}")
print(f"4*theta*a = {x}")
print(f"S21_minus_U4_refined = {margin}")
print(f"S21_minus_U4_refined_float = {float(margin):.15f}")
print(f"old_L = {old_L}")
print(f"new_L = {new_L}")
print(f"metric_gain = {gain}")
print(f"new_L_float = {float(new_L):.15f}")
print("ALL_EXACT_CHECKS_PASS = True")
