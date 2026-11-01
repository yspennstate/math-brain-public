import math
m=3501/8000
g=1/(8*math.sqrt(2))
E0=2**-20
xi=1/64
CE=7.673759290384858
J0=(math.pi*math.e*E0**(-0.25)
    +2**(27/8)*math.pi*math.e**(13/16)*g**(-3/8)*E0**(-5/32))
K_E2=(8/(3**(3/4)))/math.sqrt(2*math.pi*m)*math.sqrt(J0)
K_wedge=CE/math.sqrt(m)*(g*xi)**(-0.25)
tail=math.sqrt(E0)/(g/2)
print(f"m={m:.15f}")
print(f"g={g:.15f}")
print(f"E0={E0:.16g}")
print(f"J0={J0:.15f}")
print(f"K_E2={K_E2:.15f}")
print(f"K_wedge={K_wedge:.15f}")
print(f"tail={tail:.15f}")
assert K_E2 < 92
assert K_wedge < 61
assert abs(tail-math.sqrt(2)/64) < 1e-14
print("QFORM_B20_R12_CONSTANT_CHECK_PASS")
