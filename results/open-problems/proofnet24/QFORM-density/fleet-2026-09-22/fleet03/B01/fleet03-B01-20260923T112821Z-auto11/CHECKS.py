import math
import numpy as np


def K(p):
    return p * 2 ** (1 + 1 / p) * ((p - 1) / (p - 2)) ** ((p - 1) / p)


print(f"K3={K(3):.15f}")
assert abs(K(3) - 12) < 1e-12

for m in [3, 5, 17, 64]:
    a = np.ones(m) / math.sqrt(m)
    b = np.ones(m) / math.sqrt(m)
    z = np.ones(m) / math.sqrt(m)
    A = np.zeros((3 * m, 3 * m))
    A[:m, m:2*m] = np.outer(a, b)
    A[m:2*m, :m] = np.outer(b, a)
    A[2*m:, 2*m:] = np.outer(z, z)
    ev = np.linalg.eigvalsh(A)
    nonzero = ev[np.abs(ev) > 1e-8]
    maxdiag = float(np.max(np.abs(np.diag(A))))
    maxdet = 0.0
    for i in range(3 * m):
        for j in range(i + 1, 3 * m):
            det = A[i, i] * A[j, j] - A[i, j] * A[j, i]
            maxdet = max(maxdet, abs(float(det)))
    print(
        f"m={m} nonzero={','.join(f'{x:.12f}' for x in nonzero)} "
        f"maxdiag={maxdiag:.12g} max2det={maxdet:.12g}"
    )
    assert len(nonzero) == 3
    assert np.max(np.abs(nonzero - np.array([-1.0, 1.0, 1.0]))) < 1e-8
    assert abs(maxdiag - 1 / m) < 1e-12
    assert abs(maxdet - 1 / m**2) < 1e-12

for kappa, rho in [(1, 1), (2, 3), (0.4, 5)]:
    bound = 12 * kappa ** (-2 / 3) * rho ** (-1 / 3)
    c = 7.0
    scaled = 12 * (c * kappa) ** (-2 / 3) * (c * rho) ** (-1 / 3)
    assert abs(scaled - bound / c) < 1e-12

print("scaling_homogeneity=PASS")
print("STATUS=PASS")
