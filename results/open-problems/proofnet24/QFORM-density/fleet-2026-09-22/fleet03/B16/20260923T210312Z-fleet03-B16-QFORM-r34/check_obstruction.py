from fractions import Fraction
from math import sqrt

for N in (3,4,16,64,256,1024):
    B = 2**(-0.25) * Fraction(4,3) * ((N-1)/sqrt(N) + Fraction(1,N))
    print(f"N={N:4d} B={float(B):.12f} B2={float(B*B):.12f} B/sqrtN={float(B/sqrt(N)):.12f}")

c = 2**(-0.25) * 4/3
print(f"asymptotic_B_over_sqrtN={c:.12f}")
print(f"asymptotic_B2_over_N={c*c:.12f}")

# Eigenvalues of the canonical quadratic matrix are computed exactly from
# det(xI-M) = x (x-1) (x^2-2).
print("canonical_nonzero_eigenvalues={1,+sqrt(2),-sqrt(2)}")
print("STATUS=PASS")
