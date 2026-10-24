import math
import numpy as np

# Solve 4 exp(-L)(L+2)=1 by bisection.
lo, hi = 0.0, 20.0
for _ in range(200):
    mid = (lo + hi) / 2
    if 4 * math.exp(-mid) * (mid + 2) > 1:
        lo = mid
    else:
        hi = mid
L = (lo + hi) / 2
z = L + 2
K2 = z + 1 / z
pair_outer = 2 * math.sqrt(2 * K2)

sqrt2 = math.sqrt(2)
C_cross = 2 ** (4 / 3) * (math.log(1 + sqrt2) + sqrt2 * math.log(1 + 1 / sqrt2))
triangle_outer = 2 * math.sqrt(2 * C_cross)
color3 = 2 ** (11 / 4) * 3 ** 0.25

# Explicit genuinely rotated indefinite example.
a = 2.0
b = np.array([0.1, -0.08, 0.12, -0.05])
S = np.array([
    [0.0, 1.3, 0.0, 0.0],
    [1.3, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.4],
    [0.0, 0.0, 0.4, 0.0],
])
C = S + np.outer(b, b) / a
A = np.block([[np.array([[a]]), b[None, :]], [b[:, None], C]])
eigs = np.linalg.eigvalsh(A)
recovered_S = C - np.outer(b, b) / a
example_bound = pair_outer / math.sqrt(a) * (1.3 * 0.4) ** (-0.25)

print(f"L={L:.15f}")
print(f"z={z:.15f}")
print(f"K2={K2:.15f}")
print(f"sqrtK2={math.sqrt(K2):.15f}")
print(f"two_pair_outer_coefficient={pair_outer:.15f}")
print(f"C_cross={C_cross:.15f}")
print(f"triangle_outer_coefficient={triangle_outer:.15f}")
print(f"color3_coefficient={color3:.15f}")
print("A=")
print(A)
print("eig(A)=", np.array2string(eigs, precision=15))
print("three_abs_ge_1=", int(np.sum(np.abs(eigs) >= 1.0)))
print("schur_error=", float(np.max(np.abs(recovered_S - S))))
print(f"example_bound={example_bound:.15f}")
