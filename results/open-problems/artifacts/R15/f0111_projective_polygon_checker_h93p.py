from fractions import Fraction as F

# Exact rational specialization of the two-level null-curve formulas
# used in the projective Gram-polygon report.
delta = F(1, 2)
z = F(-3, 5)

k = 2*z*(1-z*z)/((1-delta*delta)*(delta+3*z))
x = ((delta+z)*(1+z)*(1+delta+2*z))/(2*(1+delta)*(delta+3*z))
y = ((delta+z)*(1-z)*(1-delta-2*z))/(2*(1-delta)*(delta+3*z))
K2 = ((delta+z)*(1-z*z))/(delta+3*z)
tJ = (1-z)**2-K2
tK = (1+z)**2-K2
R = -2*(delta+z)*(1-z*z)*(delta*delta*z+3*delta*z*z+delta+3*z**3)/(delta+3*z)**2
AJ = 1+3*tJ*tJ/R
AK = 1+3*tK*tK/R

old_J_count = x*AJ
old_K_count = y*AK
singleton_K_polygon_J_count = (
    old_J_count
    + ((1-delta)/(1+delta))**2 * y*(1-AK*y)/x
)

expected = {
    "k": F(256, 325),
    "x": F(1, 325),
    "y": F(68, 325),
    "K2": F(16, 325),
    "tJ": F(816, 325),
    "tK": F(36, 325),
    "R": F(1936, 105625),
    "AJ": F(124969, 121),
    "AK": F(364, 121),
    "old_J_count": F(9613, 3025),
    "old_K_count": F(1904, 3025),
    "singleton_K_polygon_J_count": F(269, 45),
}
actual = {
    "k": k,
    "x": x,
    "y": y,
    "K2": K2,
    "tJ": tJ,
    "tK": tK,
    "R": R,
    "AJ": AJ,
    "AK": AK,
    "old_J_count": old_J_count,
    "old_K_count": old_K_count,
    "singleton_K_polygon_J_count": singleton_K_polygon_J_count,
}

for name, want in expected.items():
    got = actual[name]
    assert got == want, (name, got, want)
    print(f"{name} = {got}")

assert k > 0 and x > 0 and y > 0 and R > 0
assert old_K_count < 1
assert F(3, 1) < old_J_count < F(4, 1)
assert F(5, 1) < singleton_K_polygon_J_count < F(6, 1)
print("OLD_COORDINATE_CAP_ALLOWS_M_GE_4_WHEN_N_EQ_1")
print("PROJECTIVE_POLYGON_FORCES_M_GE_6_WHEN_N_EQ_1")
print("ALL_EXACT_CHECKS_PASS")
