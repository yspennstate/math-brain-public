import math
import random

A = math.pi / math.sqrt(2.0)
C1 = 1.5 * A ** (1.0 / 3.0)
C2 = 3.0 * A ** (2.0 / 3.0)
Cstar = (2.0 * math.pi / 3.0) * (math.gamma(0.25) / math.gamma(0.75)) ** 2
Cr52 = 1.5 * Cstar ** (2.0 / 3.0)
print(f"A={A:.15f}")
print(f"adaptive_p1={C1:.15f}")
print(f"adaptive_p2={C2:.15f}")
print(f"partner_Cstar={Cstar:.15f}")
print(f"partner_product_recip={Cr52:.15f}")
assert C1 < 1.958
assert C2 < 5.108
assert Cr52 < 10.430

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

rng = random.Random(20260924)
maxerr = 0.0
for _ in range(100):
    k = 0.2 + 3.0 * rng.random()
    c = (1.0 if rng.random() < 0.5 else -1.0) * (0.2 + 3.0 * rng.random())
    eta = -2.0 + 4.0 * rng.random()
    delta = -2.0 + 4.0 * rng.random()
    M = [[0.0, k, 0.0],
         [k, delta + c * eta * eta, c * eta],
         [0.0, c * eta, c]]
    N = [[-delta / (k * k), 1.0 / k, -eta / k],
         [1.0 / k, 0.0, 0.0],
         [-eta / k, 0.0, 1.0 / c]]
    P = matmul(M, N)
    for i in range(3):
        for j in range(3):
            target = 1.0 if i == j else 0.0
            maxerr = max(maxerr, abs(P[i][j] - target))
assert maxerr < 1e-12
print(f"inverse_formula_max_error={maxerr:.3e}")

for p in (0.5, 1.0, 1.5, 1.9):
    val = 2.0 / (2.0 - p)
    print(f"rank2_moment_beta1_p{p:.1f}={val:.12f}")

print("QFORM_B11_ADAPTIVE_INVERSE_MOMENT_CHECK_PASS")
