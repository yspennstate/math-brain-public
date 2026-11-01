from fractions import Fraction


def sqrt_upper_margin(n, u):
    u = Fraction(u)
    m = u * u - n
    assert m > 0
    return m


# Endpoint for the SL_n(Z) power-thickened core: M=2 exponent layers, r=10.
M = 2
r = 10
q = 2 * r - 1
D = 3 + 2 * M * r
Q = D - 1
assert (q, D, Q) == (19, 43, 42)

u19 = Fraction(109, 25)
assert sqrt_upper_margin(19, u19) == Fraction(6, 625)
a_upper = Fraction(3, 1) + 4 * u19
assert a_upper == Fraction(511, 25)

z = Fraction(363, 20)
assert z * z > Q
root_margin = z + Fraction(Q, 1) / z - a_upper
assert root_margin == Fraction(291, 12100) and root_margin > 0

pc_upper = Fraction(1, q)
pu_lower = 1 / z
gap = pu_lower - pc_upper
assert pu_lower == Fraction(20, 363)
assert gap == Fraction(17, 6897) and gap > 0

# M=2 for every r>=10.  Since the 3-element complement contributes norm <=3,
# h(q)-a is lower-bounded by g(q)=q-1+4/q-4*sqrt(q).
# At q=19 use sqrt(19)<109/25.
g19_lower = Fraction(18, 1) + Fraction(4, 19) - 4 * u19
assert g19_lower == Fraction(366, 475) and g19_lower > 0

# g'(q)=1-4/q^2-2/sqrt(q).  For q>=19, sqrt(q)>4.
deriv_lower = Fraction(1, 2) - Fraction(4, 19 * 19)
assert deriv_lower == Fraction(353, 722) and deriv_lower > 0

# General exponent-set theorem M>=2.  q0=(2M+1)^2 suffices.
# At y=sqrt(q)=2M+1,
# y^2-2My+M-3 = 3M-2 >0.
# Also q^2 > Q=Mq+M+2 at q=q0, checked symbolically below.
for MM in range(2, 101):
    q0 = (2 * MM + 1) ** 2
    key = q0 - 2 * MM * (2 * MM + 1) + MM - 3
    assert key == 3 * MM - 2 and key > 0
    F = q0 * q0 - (MM * q0 + MM + 2)
    expected = 16 * MM**4 + 28 * MM**3 + 20 * MM**2 + 6 * MM - 1
    assert F == expected and F > 0

print("SLNZ_POWER_THICKENING_ENDPOINT")
print("M =", M, "r =", r, "q =", q, "D =", D, "Q =", Q)
print("sqrt19_upper_margin =", sqrt_upper_margin(19, u19))
print("adjacency_upper =", a_upper, "=", float(a_upper))
print("z =", z, "=", float(z))
print("root_test_margin =", root_margin, "=", float(root_margin))
print("pc_upper =", pc_upper, "=", float(pc_upper))
print("pu_lower =", pu_lower, "=", float(pu_lower))
print("gap_lower =", gap, "=", float(gap))
print("M2_all_r_ge_10_base_margin =", g19_lower, "=", float(g19_lower))
print("M2_derivative_lower_for_q_ge_19 =", deriv_lower, "=", float(deriv_lower))
print("GENERAL_EXPONENT_SET_THRESHOLD_M_2_TO_100_PASS")
print("ALL_EXACT_CHECKS_PASS")
