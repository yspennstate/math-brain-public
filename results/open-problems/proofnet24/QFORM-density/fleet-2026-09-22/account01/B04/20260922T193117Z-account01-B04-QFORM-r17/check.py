import math
import numpy as np

C_match = math.sqrt(3.0) * math.gamma(0.25)**2 / (2.0*math.pi)
C_R = math.sqrt(3.0/2.0) * math.gamma(0.25)**2 / math.pi
print(f"C_R={C_R:.15f}")
print(f"C_match={C_match:.15f}")
print(f"4*C_match={4*C_match:.15f}")
print(f"diffuse_limit={C_match*2**0.25:.15f}")

A = np.array([
    [0.0, 1.0, 0.0, 0.0, 0.30],
    [1.0, 0.0, 0.0, 0.0,-0.20],
    [0.0, 0.0, 0.0, 1.0, 0.25],
    [0.0, 0.0, 1.0, 0.0, 0.15],
    [0.30,-0.20,0.25,0.15,2.00],
])
print("eig=", np.array2string(np.linalg.eigvalsh(A), precision=12))
print(f"det={np.linalg.det(A):.12f}")

# Numerical sanity checks only for I(u) <= (1+u/6)^(-1/2).
# Midpoint quadrature on [-1/2,1/2].
for u in [0.0, 0.01, 0.1, 1.0, 10.0, 100.0]:
    if u == 0.0:
        I = 1.0
    else:
        n = 100000
        x = (np.arange(n)+0.5)/n - 0.5
        I = np.mean(np.exp(-u*x*x))
    rhs = (1.0+u/6.0)**(-0.5)
    print(f"u={u:g} I={I:.12f} rhs={rhs:.12f} slack={rhs-I:.12e}")
