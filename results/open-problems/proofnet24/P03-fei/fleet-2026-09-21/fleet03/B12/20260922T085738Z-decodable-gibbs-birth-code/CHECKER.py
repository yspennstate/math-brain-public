import math


def h2(z: float) -> float:
    if z == 0.0 or z == 1.0:
        return 0.0
    return -z * math.log2(z) - (1.0 - z) * math.log2(1.0 - z)


# Current LIMIT-PRIME-GATE-LIFT-v1 center.
C = 6.521851214
x = 2.0 ** (-C)
A0 = (1.0 + x) ** 5 - 1.0
K = A0 / x

assert K > 1.0
print(f"x={x:.15f}")
print(f"A0={A0:.15f}")
print(f"K={K:.15f}")
print(f"log2K={math.log2(K):.15f}")

# Universal k=5 multi-axis birth-transport correction from Theorem 4.5.
for eps in (4.4e-6, 2.59e-5):
    correction = math.comb(5, 2) * eps * h2(4.0 * eps * eps)
    print(f"eps={eps:.12g} correction={correction:.15e}")

# Refutation of the overstrong zero-correction claim on AND2.
s1 = 0.1
s2 = -0.1
and_excess = (-s2) * h2(4.0 * s1 * s1)
assert and_excess > 0.0
print(f"AND2_zero_correction_excess={and_excess:.15f}")
print("PASS")
