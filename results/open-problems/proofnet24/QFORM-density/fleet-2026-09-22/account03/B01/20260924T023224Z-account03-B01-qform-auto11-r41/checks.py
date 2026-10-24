import math
import numpy as np


def Cq(q0):
    r = q0 / (q0 - 1)
    alpha = (r - 1) / r
    theta = r / (2 * r - 1)
    C = ((1 + alpha) / (math.pi * alpha)) * (
        (alpha * math.pi / 2)
        * (2 / (r - 1)) ** (1 / r)
        * (2 * math.pi) ** alpha
        * 2 ** (alpha + 0.5)
    ) ** theta
    scale = -r / (2 * r - 1) + q0 * (r - 1) / (2 * r - 1)
    return r, C, scale


print("joint compiler endpoint constant:", 3 * 2 ** (-2 / 3))
print(
    "after partner q2 and K projection constant:",
    3 * 2 ** (-2 / 3) * (2 ** 0.5) ** (2 / 3) * (2 ** 0.5) ** (2 / 3),
)
for q0 in [2, 3, 4]:
    r, C, scale = Cq(q0)
    print(f"q0={q0} r={r:.12g} C={C:.12g} scale_exponent={scale:.12g}")

A = np.array(
    [
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
    ],
    dtype=float,
)
eigs = np.linalg.eigvalsh(A)
print("stress eigenvalues:", " ".join(f"{x:.12f}" for x in eigs))
print("num |lambda|>=1:", int(np.sum(np.abs(eigs) >= 1 - 1e-12)))
assert abs(3 * 2 ** (-2 / 3) * 2 ** (1 / 3) * 2 ** (1 / 3) - 3) < 1e-12
for q0 in [2, 3, 4]:
    _, _, scale = Cq(q0)
    assert abs(scale) < 1e-12
assert np.sum(np.abs(eigs) >= 1 - 1e-12) >= 3
print("STATUS=PASS")
