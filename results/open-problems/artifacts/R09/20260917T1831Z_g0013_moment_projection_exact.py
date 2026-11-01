#!/usr/bin/env python3
from fractions import Fraction as F

# Exact self-check for R09 G0013 moment-projection/Jacobi improvement.
# This certifies only the finite algebra/arithmetic used in the written proof.

def assert_eq(a,b,msg):
    if a != b:
        raise AssertionError(f"{msg}: {a} != {b}")

# 1. Projection-ramp identity.
# L=(6m-a)/(4m).
# hplus = 4m^2/(3L)-m^2-a^2/12
# equals (a-2m)^3/[12(6m-a)].
# Equivalent polynomial identity after clearing denominators:
# 64m^3 - 12m^2(6m-a) - a^2(6m-a) = (a-2m)^3.
lhs_coeff = {
    (0,3): F(64)-F(72),
    (1,2): F(12),
    (2,1): F(-6),
    (3,0): F(1),
}
rhs_coeff = {
    (3,0): F(1),
    (2,1): F(-6),
    (1,2): F(12),
    (0,3): F(-8),
}
assert_eq(lhs_coeff, rhs_coeff, "ramp projection identity")

# 2. Constant C^3 = 125/768 from the relaxed extremal optimization.
C3 = F(125,768)
assert F(1,27) < C3
endpoint = (F(1,2)**5 * (F(5,2)**3))/3
assert_eq(endpoint, C3, "high-m endpoint")
# d/dm log[m^5(4-3m)^3] has numerator 20-24m, >=8 on [1/3,1/2].
assert 20 - 24*F(1,2) == 8
# phi'(u)=4(u+1)^2(2-u); branch switch is at u=2 when m=1/3.
assert 3*(1-F(1,3)) == 2

# 3. Certified bracket for the unique positive root z_* of
# P(z)=175104 z^3 + 4500 z - 125.
def P(z):
    return 175104*z**3 + 4500*z - 125

z_lo = F(27010941, 10**9)
z_hi = F(27010942, 10**9)
plo, phi = P(z_lo), P(z_hi)
assert plo < 0 < phi
# P'(z)=525312 z^2+4500 >0, hence the root is unique.

# 4. U = 17/171 + 8 z_*/19; certify its bracket and improvement.
def U_of_z(z):
    return F(17,171) + F(8,19)*z

U_lo, U_hi = U_of_z(z_lo), U_of_z(z_hi)
previous = F(2221,20000)
assert U_hi < previous
improvement_floor = previous - U_hi
assert improvement_floor > 0

print("R09 G0013 MOMENT-PROJECTION EXACT SELF-CHECK")
print("C^3 =", C3)
print("C ~= 0.5459877904601868")
print("P(z_lo) =", plo)
print("P(z_hi) =", phi)
print("z_* bracket =", float(z_lo), float(z_hi))
print("U_* theorem bracket =", float(U_lo), float(U_hi))
print("previous bound =", float(previous))
print("certified improvement at least =", improvement_floor, "~", float(improvement_floor))
print("SELF_CHECK_ONLY")
print("PASS")
