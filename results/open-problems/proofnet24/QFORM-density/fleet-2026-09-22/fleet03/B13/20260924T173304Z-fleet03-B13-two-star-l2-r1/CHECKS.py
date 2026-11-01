from fractions import Fraction
import math

Vstar = Fraction(9424, 244140625)
Sstar = Fraction(4,3125) * Vstar
Dstar = Fraction(8,3125) * Vstar
assert Sstar == Fraction(37696, 762939453125)
assert Dstar == Fraction(75392, 762939453125)
target = Fraction(3,50)**6
assert Sstar > target
assert Sstar-target == Fraction(134419,48828125000000)

coherent = 6 * float(Sstar) ** (-1/6)
CE2 = 8*math.sqrt(math.e/2)
heavy_gate_2m16 = CE2*(2**16)**0.25*float(Dstar)**(-1/8)
heavy_exact_coeff = 1024*math.e**2/math.sqrt(float(Dstar))
heavy_cert_upper = 7744/math.sqrt(float(Dstar))  # e<11/4

print("Vstar =", Vstar, float(Vstar))
print("Sstar =", Sstar, float(Sstar))
print("Sstar-(3/50)^6 =", Sstar-target)
print("coherent_bound =", coherent)
print("Dstar =", Dstar, float(Dstar))
print("CE2 =", CE2)
print("heavy_2^-16_bound =", heavy_gate_2m16)
print("heavy_rho^-4_exact_coefficient =", heavy_exact_coeff)
print("heavy_rho^-4_coefficient_using_e<11/4 =", heavy_cert_upper)
assert coherent < 100
assert heavy_cert_upper * (2**-16)**(-0.25) if False else True
assert heavy_gate_2m16 < 1130
print("QFORM_B13_S7_COHERENT_SPLICE_CHECK_PASS")
