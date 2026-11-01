import math

C3 = 3**1.5 * math.e**(2/3) / 2**(2/3)
C4pair = (992 + 448*math.sqrt(2))**0.25
theta = 3/8
K4 = C4pair * C3**theta
L2const = 2*math.pi*K4

print(f"C3={C3:.15f}")
print(f"C4pair={C4pair:.15f}")
print(f"theta={theta:.15f}")
print(f"K4={K4:.15f}")
print(f"2piK4={L2const:.15f}")

assert abs((1-theta) + theta/3 - 3/4) < 1e-15
assert abs((-1/9)*theta - (-1/24)) < 1e-15
assert K4 < 12.719
assert L2const < 79.915
print("STATUS=PASS")
