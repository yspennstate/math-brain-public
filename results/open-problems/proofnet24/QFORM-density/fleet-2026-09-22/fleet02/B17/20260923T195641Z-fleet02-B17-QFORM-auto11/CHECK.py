from fractions import Fraction
import math

alpha = math.asin(4/5)
K = 2*math.sqrt(2)*alpha + math.sqrt(5)*(math.pi/2-alpha)
sharp_candidate = 3*math.sqrt(2)
assert K < sharp_candidate

# Fully rational certificate used in REPORT.md:
# sqrt(5)<161/72, pi<22/7, 2sqrt(2)-sqrt(5)<3/5, asin(4/5)<1.
cert_upper = Fraction(1771,504) + Fraction(3,5)
cert_lower = Fraction(140,33)  # < 3sqrt(2)
assert cert_upper < cert_lower
assert cert_lower**2 < 18      # (140/33)^2 < (3sqrt(2))^2

# Latest fleet03/B17 bound p<=508/125 + 252 sqrt(6)/R.
# Improve its rational finite-R threshold with sqrt(6)<49/20.
R = 3461
partner_upper = Fraction(508,125) + Fraction(252*49,20*R)
assert partner_upper < Fraction(140,33)

print(f"K_4_5={K:.15f}")
print(f"3sqrt2={sharp_candidate:.15f}")
print(f"gap={sharp_candidate-K:.15f}")
print(f"rational_cert_upper={float(cert_upper):.15f}")
print(f"rational_cert_target={float(cert_lower):.15f}")
print(f"partner_R3461_upper={float(partner_upper):.15f}")
print(f"partner_margin_to_140_over_33={Fraction(140,33)-partner_upper}")
print("PASS QFORM-ONE-HEAVY-UNEQUAL-BANKS-GLOBAL-BARRIER-v1")
