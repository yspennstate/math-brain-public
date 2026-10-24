import math
import numpy as np

# Constants in the proof.
C_product_l2 = 4.0
C_scaled_bilinear_l2 = C_product_l2 / math.sqrt(2.0)
C_two_products_caps = C_scaled_bilinear_l2 ** 2
C_projection_bank = C_two_products_caps * math.sqrt((math.sqrt(2.0)) ** 4)
C_pairlog_composite = 7.0 * (math.pi / 12.0) ** (1.0 / 7.0) * 16.0 ** (2.0 / 7.0)

print(f"C_product_l2={C_product_l2:.12f}")
print(f"C_scaled_bilinear_l2={C_scaled_bilinear_l2:.12f}")
print(f"C_two_products_caps={C_two_products_caps:.12f}")
print(f"C_projection_bank={C_projection_bank:.12f}")
print(f"C_pairlog_composite={C_pairlog_composite:.12f}")

assert abs(C_projection_bank - 16.0) < 1e-12
assert C_pairlog_composite < 12.764

# Compressed four-bank stress matrix.
B = np.array([
    [0.0, 1.0, 0.0, 0.0],
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0],
])
evals = np.linalg.eigvalsh(B)
print("compressed_eigenvalues=", evals.tolist())
assert np.allclose(evals, [-1.0, -1.0, 1.0, 1.0])

for m in [1, 2, 5, 20]:
    u = np.ones(m) / math.sqrt(m)
    cross = np.outer(u, u)
    max_entry = np.max(np.abs(cross))
    print(f"m={m} max_physical_cross_entry={max_entry:.12f}")
    assert abs(max_entry - 1.0 / m) < 1e-12

print("STATUS=PASS")
