import math

D0 = 1001/12544
k0 = 13/112
a0 = 49/576
KLambda = 6144*math.e**2
C5 = 2*math.sqrt(30*math.pi)

C0 = (2**(13/4))*(3*math.e)**(1/8)*(D0**(-3/16))*(k0**(-1/4))*(a0**(-1/16))
C1 = C0*KLambda**(-1/16)
K50 = C1**16

assert abs(C0 - 39.70613727827169) < 1e-10
assert abs(C1 - 20.3138681411028) < 1e-10
assert K50 < 8.408e20
assert abs(C5 - 19.41625912555699) < 1e-10
assert abs(8*C5/7 - 22.19001042920799) < 1e-10
assert K50/C5 < 4.331e19
assert abs((3/4)*16 - 12) < 1e-15

print("QFORM_B13_R50_HEAVY_DELETE_CHECK_PASS")
print("C0 =", C0)
print("C1 =", C1)
print("K50 =", K50)
print("C5 =", C5)
print("K50/C5 =", K50/C5)
