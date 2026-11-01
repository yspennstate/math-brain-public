import itertools
import math
import numpy as np

rng = np.random.default_rng(26092313)
m = 7
n = m + 2
X = rng.normal(size=(n, n))
A = (X + X.T) / 2
U = [0, 1]
T = list(range(2, n))

Zstar = 0.0
max_cb_error = 0.0
for j in T:
    rows = [i for i in T if i != j]
    Cj = A[np.ix_(rows, U + [j])]
    gram = np.linalg.det(Cj.T @ Cj)
    cb = 0.0
    for S in itertools.combinations(rows, 3):
        cb += np.linalg.det(A[np.ix_(S, U + [j])]) ** 2
    Zstar += cb
    max_cb_error = max(max_cb_error, abs(gram - cb))

theta = 3.0 / 4.0
EW = 0.0
for mask in range(1 << m):
    R = [T[k] for k in range(m) if (mask >> k) & 1]
    C = [j for j in T if j not in R]
    prob = theta ** len(R) * (1.0 - theta) ** len(C)
    W = 0.0
    for j in C:
        for S in itertools.combinations(R, 3):
            W += np.linalg.det(A[np.ix_(S, U + [j])]) ** 2
    EW += prob * W

target = (27.0 / 256.0) * Zstar
assert max_cb_error < 2e-12
assert abs(EW - target) < 2e-12 * max(1.0, abs(target))

factor = (256.0 / 27.0) ** (1.0 / 6.0)
q = 4.0 / 3.0
Cq = 3.0 * math.e / ((3.0 - 2.0 * q) * math.sqrt(q)) * factor
Cent = 12.0 * math.sqrt(math.e) * factor
single_fraction = (2.0 / 3.0) * (27.0 / 256.0)
six_fraction = (63.0 / 64.0) * (27.0 / 256.0)

assert abs(single_fraction - 9.0 / 128.0) < 1e-15
assert abs(six_fraction - 1701.0 / 16384.0) < 1e-15

print(f"max_cauchy_binet_error={max_cb_error:.17g}")
print(f"Zstar={Zstar:.17g}")
print(f"enumerated_EW={EW:.17g}")
print(f"target_27_over_256_Zstar={target:.17g}")
print(f"q43_paid_constant={Cq:.15f}")
print(f"entropy_paid_constant={Cent:.15f}")
print(f"single_row_global_fraction={single_fraction:.15f}")
print(f"six_row_global_fraction={six_fraction:.15f}")
print("QFORM_B13_R26_BORDERED_RANDOM_CUT_CHECK_PASS")
