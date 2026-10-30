from fractions import Fraction

p1 = Fraction(223, 456)
pout = Fraction(1019, 2048)
alpha1 = Fraction(57, 256)
alpha_rest = Fraction(465, 256)
a = Fraction(33525607, 125000000)       # 0.268204856
peer_deficit_lb = Fraction(38023, 1000000)  # -D_Gamma^dagger > this

Q = (
    alpha1 * p1 * (1 - p1)
    + alpha_rest * Fraction(1, 4)
    - pout * (1 - pout)
)
assert Q == Fraction(62098577, 239075328)
assert Q > 0

c_lower = a + peer_deficit_lb / Q
assert c_lower == Fraction(3218187637329239, 7762322125000000)

and_cert_upper = Fraction(1, 100)
assert c_lower > and_cert_upper

gap = c_lower - and_cert_upper
center_lower = Fraction(64548, 10000) + c_lower / 4

print("Q =", Q)
print("Q_decimal =", float(Q))
print("c_G lower bound =", c_lower)
print("c_G lower decimal =", float(c_lower))
print("certified AND upper =", float(and_cert_upper))
print("gap lower =", float(gap))
print("quadratic-ray center lower =", float(center_lower))
print("PASS")
