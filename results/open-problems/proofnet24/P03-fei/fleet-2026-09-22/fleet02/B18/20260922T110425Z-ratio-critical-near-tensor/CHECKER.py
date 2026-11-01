from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
LN2 = D(2).ln()


def h2(x):
    if x == 0 or x == 1:
        return D(0)
    return -(x * x.ln() + (D(1) - x) * (D(1) - x).ln()) / LN2


sqrt31 = D(31).sqrt()
a = (D(16) + sqrt31) / D(32)
j = D(1) - h2(a)
H_phi = (D(961) / D(1024)) * ((D(1024) / D(961)).ln() / LN2) + D(630) / D(1024)
P_phi = D(6) * j
F_phi = H_phi - P_phi
gap = D(3) / D(4) - F_phi


def budget(N, epsilon):
    t = D(2) * epsilon.sqrt()
    return (
        D(2) * h2(t)
        + D(2 * N - 6) * t
        + D(2 * N - 6) * (D(2) + D(1) / LN2) * t * t
    )


print("H_phi", H_phi)
print("P_phi", P_phi)
print("F_phi", F_phi)
print("4J_minus_F", gap)
assert F_phi < D(1) / D(4)
assert gap > D(1) / D(2)

coarse = D(463) / D(1152)
print("coarse_radius_budget_bound", coarse)
print("coarse_negative_margin", D(1) / D(2) - coarse)
assert coarse < D(1) / D(2)

for N in (18, 24, 30, 60, 120):
    epsilon = D(2) ** D(-N)
    radius = D(1) / (D(256) * D(N) * D(N))
    b = budget(N, epsilon)
    print("N", N, "surgery_epsilon", epsilon, "radius", radius, "budget", b)
    assert epsilon < radius
    assert b < gap

print("RESULT PASS")
