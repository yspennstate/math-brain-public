import math

pi = math.pi
a = pi*math.sqrt(2.0)
b = 3.0*math.sqrt(3.0)
r2 = b/a
r = math.sqrt(r2)
Crot_1 = a*r + b/r
Crot_2 = 2.0*math.sqrt(3.0*pi*math.sqrt(6.0))
assert abs(Crot_1-Crot_2) < 1e-12

Cold = 2.0*pi + 3.0*math.sqrt(3.0)
assert Crot_1 < Cold

Cbranch = 2.0*(3.0**0.25)*math.sqrt(pi*math.e)
for m in range(2,10000):
    Bm=(1.0-1.0/m)**(-(m-1))
    assert Bm < math.e + 1e-12
    Cm=2.0*math.sqrt(pi)*(3.0**0.25)*math.sqrt(Bm)
    assert Cm < Cbranch + 1e-12

print(f"r_star_squared={r2:.15f}")
print(f"C_rot={Crot_1:.15f}")
print(f"old_3var_constant={Cold:.15f}")
print(f"improvement={Cold-Crot_1:.15f}")
print(f"one_heavy_uniform_envelope={Cbranch:.15f}")
print(f"three_sqrt_two={3.0*math.sqrt(2.0):.15f}")
print("STATUS=PASS")
