import math
import numpy as np

rng = np.random.default_rng(20260923)
max_formula_error = 0.0
max_weyl_violation = 0.0
cases = 0

for n in range(3, 11):
    for _ in range(500):
        M = rng.normal(size=(n, n))
        A = (M + M.T) / 2
        i = int(rng.integers(0, n))
        perm = [i] + [j for j in range(n) if j != i]
        A = A[np.ix_(perm, perm)]
        a = float(A[0, 0])
        b = A[1:, 0]
        C = A[1:, 1:]
        beta = float(np.linalg.norm(b))

        E = np.zeros_like(A)
        E[0, 0] = a
        E[0, 1:] = b
        E[1:, 0] = b

        sE = np.linalg.svd(E, compute_uv=False)
        eta = (math.sqrt(a*a + 4*beta*beta) - abs(a)) / 2
        max_formula_error = max(max_formula_error, abs(float(sE[1]) - eta))

        sA = np.linalg.svd(A, compute_uv=False)
        sC = np.linalg.svd(C, compute_uv=False)
        violation = float(sA[2] - (sC[1] + eta))
        max_weyl_violation = max(max_weyl_violation, violation)
        cases += 1

assert max_formula_error < 1e-11
assert max_weyl_violation < 1e-11

print("QFORM_B08_R27_ARROWHEAD_CHECK_PASS")
print("cases", cases)
print("max_formula_error", repr(max_formula_error))
print("max_weyl_violation", repr(max_weyl_violation))
