import math
from fractions import Fraction
import numpy as np


def frame_check(m, ell):
    n = 3 + 3*m
    C = np.zeros((3, n))
    C[:, :3] = math.sqrt(ell) * np.eye(3)
    col = 3
    for j in range(3):
        for _ in range(m):
            C[j, col] = math.sqrt((1-ell)/m)
            col += 1
    B = np.diag([1.0, 1.0, -1.0])
    A = C.T @ B @ C
    frame_err = np.max(np.abs(C @ C.T - np.eye(3)))
    vals = np.linalg.eigvalsh(A)
    target = np.array([-1.0] + [0.0]*(n-3) + [1.0, 1.0])
    spec_err = np.max(np.abs(vals-target))
    return frame_err, spec_err


c_aligned = Fraction(177-39, 640)
assert c_aligned == Fraction(69, 320)
assert c_aligned > 0

for m in [1, 2, 5, 13]:
    ferr, serr = frame_check(m, 0.2)
    assert ferr < 1e-12
    assert serr < 1e-12
    print(f"m={m} frame_err={ferr:.3e} spectrum_err={serr:.3e}")

print("aligned coefficient", c_aligned, float(c_aligned))
print("baseline 3sqrt2", 3*math.sqrt(2))
print("PASS QFORM-SEPARATED-SYMMETRIC-UNIMODAL-OFFZERO-v1")
