from fractions import Fraction as F

# Exact rational upper bounds used for the four-pair dependent perturbation.
r11 = F(199,60)
r7 = F(127,48)
r3 = F(26,15)
assert r11*r11 > 11
assert r7*r7 > 7
assert r3*r3 > 3

# Base T_12 x T_8 adjacency plus two F_2 power layers.
a_hi = 2*r11 + 2*r7 + 4*r3
assert a_hi == F(2263,120)

# Degree 28, hence Q=D-1=27.  Test z=5000/289.
Q = F(27,1)
z = F(5000,289)
assert z*z > Q
root_margin = z + Q/z - a_hi
assert root_margin == F(7163,2167500)
assert root_margin > 0

# Prior product-fibre branching certificate on the standard spanning subgraph.
pc_hi = F(7,125)
pu_lo = F(289,5000)
gap = pu_lo - pc_hi
assert gap == F(9,5000)
assert gap > 0

print("sqrt11 square margin =", r11*r11-F(11,1))
print("sqrt7 square margin =", r7*r7-F(7,1))
print("sqrt3 square margin =", r3*r3-F(3,1))
print("adjacency rational upper =", a_hi, float(a_hi))
print("z =", z, float(z))
print("z^2-Q =", z*z-Q, float(z*z-Q))
print("root-test margin =", root_margin, float(root_margin))
print("pc upper pivot =", pc_hi, float(pc_hi))
print("pu lower pivot =", pu_lo, float(pu_lo))
print("certified gap >", gap, float(gap))
print("ALL_EXACT_CHECKS_PASS")
