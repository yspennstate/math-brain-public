from fractions import Fraction
from math import sqrt, e

cmin = Fraction(63,64)
C_zero = 3*2**(4/3)*(64/63)**(1/3)
C_diff = 4*sqrt(2*e)*sqrt(64/63)*8
C_partner = 128*sqrt(64/63)*8
assert C_zero < 7.6
assert C_diff < 76
assert C_partner < 1033

# Counterexample interface: q_a=a y^2+2uy+v^2, det G=-1.
# Hyperbolic coordinates p=v-u/sqrt(a), q=v+u/sqrt(a):
# p in [1,R], q in [a/(2p),a/p] has (u,v)-area a^(3/2) log(R)/4.
# Taking log R=4/a^(3/2) makes the area exactly one.
# With y=-u/a+s, |s|<=1/2, q_a=a s^2+(v^2-u^2/a)
# lies in [a/2,5a/4], length 3a/4, so density height >=4/(3a).
for a in (Fraction(1,16), Fraction(1,256), Fraction(1,4096)):
    assert Fraction(4,3)/a > 1

print(f"C_zero={C_zero:.12f}")
print(f"C_diff_threshold={C_diff:.12f}")
print(f"C_partner_threshold={C_partner:.12f}")
print("counterexample_height_at_a=1/4096=", float(Fraction(4,3)/Fraction(1,4096)))
print("STATUS=PASS")
