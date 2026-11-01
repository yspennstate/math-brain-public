from fractions import Fraction
from math import sqrt

# Exact second-order algebra for the three-bank rotated diffuse witness.
# This checker is arithmetic only; it is not a substitute for the analytic Edgeworth/coarea proof.

# Symbolic coefficients after cone averaging, represented by formal variables r2=sum u_i^4,
# r3=sum u_i^6, r4=sum u_i^8.  The r4 terms cancel in the final coefficient.
# We check the cancellation and representative exact values by hand-expanded Fraction arithmetic.

def A6(r2, r3):
    return -Fraction(15,128) * (19*r3 - 111*r2 + 234)

def A8(r2, r3, r4):
    return Fraction(105,2048) * (611*r4 - 492*r3 - 1902*r2 + 3645)

def A44(r2, r3, r4):
    return Fraction(3,4096) * (21385*r2*r2 + 228*r2 + 7380*r3 - 21385*r4 + 10458)

def d_from_parts(r2, r3, r4):
    return Fraction(1,105)*A6(r2,r3) + Fraction(1,800)*A8(r2,r3,r4) + Fraction(1,400)*A44(r2,r3,r4)

def d_closed(r2, r3):
    return (449085*r2*r2 + 27618*r2 - 449840*r3 - 96507) / Fraction(11468800)

def c_first(r2):
    return (Fraction(177) - Fraction(39)*r2) / Fraction(640)

cases = {
    "aligned": ([Fraction(1),Fraction(0),Fraction(0)], Fraction(0)),
    "isotropic": ([Fraction(1,3)]*3, Fraction(7,113)),
    "u10": ([Fraction(100,2601),Fraction(100,2601),Fraction(2401,2601)], Fraction(11,173)),
}

for name,(s, dummy_r4_shift) in cases.items():
    r2 = sum(x*x for x in s)
    r3 = sum(x*x*x for x in s)
    r4 = sum(x*x*x*x for x in s)
    assert d_from_parts(r2,r3,r4) == d_closed(r2,r3)
    # r4 cancellation is exact: perturbing formal r4 leaves d_from_parts unchanged.
    assert d_from_parts(r2,r3,r4+dummy_r4_shift) == d_closed(r2,r3)
    print(name, "c=", c_first(r2), float(c_first(r2)), "d=", d_closed(r2,r3), float(d_closed(r2,r3)))

# First-order coefficient interval: r2 in [1/3,1].
assert c_first(Fraction(1)) == Fraction(69,320)
assert c_first(Fraction(1,3)) == Fraction(41,160)

# Second-order negativity.  Since r3 >= r2^2, the numerator is at most
# P(z)=-755 z^2+27618 z-96507, z=r2 in [1/3,1].
# P is increasing there because P'(z)=27618-1510z >=26108>0.
P1 = -755 + 27618 - 96507
assert P1 == -69644
assert Fraction(P1,11468800) == -Fraction(17411,2867200)
assert -Fraction(17411,2867200) < 0

# Exact representative values.
r2_iso = Fraction(1,3)
r3_iso = Fraction(1,9)
assert d_closed(r2_iso,r3_iso) == -Fraction(3511,460800)

s10=[Fraction(100,2601),Fraction(100,2601),Fraction(2401,2601)]
r2_10=sum(x*x for x in s10); r3_10=sum(x*x*x for x in s10)
assert c_first(r2_10) == Fraction(53990741,240540480)
assert d_closed(r2_10,r3_10) < 0

print("uniform_second_order_upper=", -Fraction(17411,2867200), float(-Fraction(17411,2867200)))
print("3sqrt2=", 3*sqrt(2))
print("QFORM_B17_SECOND_ORDER_ROTATED_CHECK_PASS")
