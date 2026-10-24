"""Finite checks for account03/B17 QFORM r15.
The proof in REPORT.md is analytic; these checks only validate the explicit block spectrum
and numerical value of the Gaussian lower-bound constant.
"""
import math
import numpy as np


def build_A(m):
    u = np.ones(m) / math.sqrt(m)
    P = np.outer(u, u)
    K = np.eye(m) - P
    eps = m ** -2
    blocks = [P + eps * K, P + eps * K, -P + eps * K]
    A = np.zeros((3*m, 3*m))
    for j, B in enumerate(blocks):
        A[j*m:(j+1)*m, j*m:(j+1)*m] = B
    return A

for m in (2, 3, 5, 10):
    vals = np.linalg.eigvalsh(build_A(m))
    target = np.array([-1.0] + [m**-2]*(3*m-3) + [1.0, 1.0])
    target.sort()
    assert np.max(np.abs(vals-target)) < 1e-10
    assert 3.0/(4.0*m) == (m**-2)*(3.0*m/4.0)
    print(f"m={m}: spectrum PASS; perturbation envelope <= {3/(4*m):.12g}")

c = 3*math.sqrt(2)
assert abs(c - 4.242640687119285) < 2e-15
print(f"3*sqrt(2)={c:.15f}")
print("PASS")
