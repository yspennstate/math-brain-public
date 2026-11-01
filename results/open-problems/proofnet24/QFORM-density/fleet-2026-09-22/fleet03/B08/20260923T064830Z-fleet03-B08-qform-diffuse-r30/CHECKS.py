from fractions import Fraction
from math import e, sqrt
import numpy as np

# Fixed mixed-order certificate.
theta = Fraction(16,25)
q = Fraction(32,25)
k = Fraction(66,25)
assert k - 2*q == Fraction(2,25)
assert k / (k-2*q) == 33
assert Fraction(16,25) * Fraction(1,10800) == Fraction(1,16875)

Cmix = e * float(q)**(-0.5) * 33.0 * (10800.0**(25.0/132.0)) * ((float(theta)**float(theta) * float(1-theta)**float(1-theta))**(25.0/132.0))
assert Cmix < 407.0

# Double-nested constants.
assert abs(sqrt(16875.0) - 75.0*sqrt(3.0)) < 1e-12
Cvol = 2025.0 * e * sqrt(3.0)
assert Cvol < 9535.0
Cpair = 600.0 * sqrt(6.0)
assert Cpair < 1470.0

# Random algebra regression for det[[C,r],[s,n]]=det(C)n-s adj(C) r.
rng = np.random.default_rng(20260923064830)
maxerr = 0.0
for _ in range(1000):
    C = rng.normal(size=(2,2))
    r = rng.normal(size=(2,))
    s = rng.normal(size=(2,))
    n = float(rng.normal())
    M = np.block([[C, r[:,None]], [s[None,:], np.array([[n]])]])
    adj = np.array([[C[1,1], -C[0,1]], [-C[1,0], C[0,0]]])
    rhs = np.linalg.det(C)*n - s @ adj @ r
    err = abs(np.linalg.det(M)-rhs)
    maxerr = max(maxerr, err)
assert maxerr < 1e-11

print(f"Cmix={Cmix:.12f}")
print(f"double_nested=1/{16875}")
print(f"Cvol={Cvol:.12f}")
print(f"Cpair={Cpair:.12f}")
print(f"max_det_identity_error={maxerr:.3e}")
print("QFORM_B08_R30_CHECK_PASS")
