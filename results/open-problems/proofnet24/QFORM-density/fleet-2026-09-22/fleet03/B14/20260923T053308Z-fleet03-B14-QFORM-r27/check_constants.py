import math

y0 = 1 / math.sqrt(2)
theta = 2 / 3
C_cancel = 4 * math.sqrt(2) * math.exp(3/4) / math.sqrt(y0 * (y0 - theta))
C_non = 16 * math.sqrt(60 / theta)
C_exact = 48 * math.sqrt(10)

print(f"y0={y0:.16f}")
print(f"theta={theta:.16f}")
print(f"C_cancel={C_cancel:.15f}")
print(f"C_non={C_non:.15f}")
print(f"48sqrt10={C_exact:.15f}")
print(f"C_cancel<C_non: {C_cancel < C_non}")
print(f"C_non==48sqrt10 within 1e-12: {abs(C_non-C_exact) < 1e-12}")
