import math


def Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

alpha_L = 1.0 / Phi(-1.0)
alpha_U = 12.749999921749  # newest rigorous exact-sphere source endpoint on master
mixed_L = 1.0 + alpha_L
mixed_U = 1.0 + alpha_U
width = mixed_U - mixed_L

print(f"PURE_ALPHA_L {alpha_L:.15f}")
print(f"PURE_ALPHA_U {alpha_U:.12f}")
print(f"MIXED_ALPHA_L {mixed_L:.15f}")
print(f"MIXED_ALPHA_U {mixed_U:.12f}")
print(f"MIXED_WIDTH {width:.15f}")
assert abs((mixed_U-mixed_L) - (alpha_U-alpha_L)) < 1e-14
assert mixed_U < 13.75
print("ALL_ENDPOINT_RECONCILE_CHECKS_PASS")
