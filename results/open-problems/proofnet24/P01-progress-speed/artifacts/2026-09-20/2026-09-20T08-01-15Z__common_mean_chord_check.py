from fractions import Fraction as F


def cert(D, p, L):
    # Common-mean ratio lemma gives c_D/c_1 <= (1+L)/(D+L),
    # valid when D(1-L) >= 1+L.
    assert D * (1 - L) >= 1 + L
    t = (1 + L) / (D + L)
    theta = p * t / (1 - p + p * t)
    assert L >= F(1, 2)
    vertex = (2 * L - 1) / (2 * L)
    assert theta <= vertex
    A = L / (1 - L)
    h = D - 1
    G = 1 + h * theta - A * h * theta * (1 - theta)
    R = 1 + h * theta
    margin = 2 * G / (R + L) ** 2
    return t, theta, vertex, G, R, margin


# Headline: {1,12}, p<=1/2, lambda<=1671/2500.
D = 12
p = F(1, 2)
L = F(1671, 2500)
t, th, v, G, R, margin = cert(D, p, L)
assert t == F(4171, 31671)
assert th == F(4171, 35842)
assert G == F(111630693, 1064973991156)
assert margin == F(116281971875000, 4822111054469803383)
assert margin > F(1, 42000)

# Method-frontier bracket for D=12,p=1/2 after substitution.
def P12(x):
    return 37 * x ** 3 + 334 * x ** 2 + 227 * x - 312


assert P12(F(1671, 2500)) == F(-111630693, 15625000000)
assert P12(F(1671, 2500)) < 0
assert P12(F(1337, 2000)) == F(521342861, 8000000000)
assert P12(F(1337, 2000)) > 0

# Robust landmark at lambda=2/3 for same family.
t2, th2, v2, G2, R2, m2 = cert(12, F(1, 2), F(2, 3))
assert t2 == F(5, 38)
assert th2 == F(5, 43)
assert G2 == F(34, 1849)
assert m2 == F(153, 36100)

# Breadth extension: p<=2/5, {1,46}, lambda<=2/3.
t46, th46, v46, G46, R46, m46 = cert(46, F(2, 5), F(2, 3))
assert t46 == F(1, 28)
assert th46 == F(1, 43)
assert G46 == F(4, 1849)
assert m46 == F(18, 30625)
assert m46 > F(1, 1800)

# Immediate D=47 certificate failure for same p,L (method boundary only).
t47, th47, v47, G47, R47, m47 = cert(47, F(2, 5), F(2, 3))
assert G47 == F(-19, 192721)
assert G47 < 0

# Far-support extension just above the support-free p-threshold 3/8.
t221, th221, v221, G221, R221, m221 = cert(221, F(19, 50), F(2, 3))
assert t221 == F(1, 133)
assert th221 == F(1, 218)
assert G221 == F(1, 11881)
assert m221 == F(18, 765625)
assert m221 > F(1, 50000)

# Immediate D=222 failure of this sufficient certificate (not a counterexample).
t222, th222, v222, G222, R222, m222 = cert(222, F(19, 50), F(2, 3))
assert G222 == F(-5126, 432764809)
assert G222 < 0

print("HEADLINE_D12_L =", L)
print("HEADLINE_t =", t)
print("HEADLINE_theta =", th)
print("HEADLINE_G =", G)
print("HEADLINE_margin =", margin, "=", float(margin))
print("HEADLINE_margin_gt_1_over_42000 =", margin > F(1, 42000))
print("D12_frontier_poly_at_0.6684 =", P12(F(1671, 2500)))
print("D12_frontier_poly_at_0.6685 =", P12(F(1337, 2000)))
print("D12_L_2_3_margin =", m2, "=", float(m2))
print("D46_p_2_5_margin =", m46, "=", float(m46))
print("D47_p_2_5_G =", G47)
print("D221_p_19_50_margin =", m221, "=", float(m221))
print("D222_p_19_50_G =", G222)
print("ALL_EXACT_CHECKS_PASS")
