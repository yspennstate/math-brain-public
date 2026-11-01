from fractions import Fraction
import math

# Analytic prefactors for k=3+r in the internally proved e^(k/2) projection-cap version
# and the sharper 2^(k/2) product-marginal version.
for r in range(6):
    k = 3 + r
    primary = math.e * k / (k - 2)
    sharp = 2 * k / (k - 2)
    print(r, k, f"{primary:.12f}", f"{sharp:.12f}")

# Integration identity: alpha=k/2 and T=K^(1/alpha)
# integral_R min(1,K |t|^-alpha) dt = 2 alpha/(alpha-1) K^(1/alpha)
# so after 1/(2pi) and K=pi^(k/2)*... the pi cancels exactly.
for k in range(3, 9):
    alpha = Fraction(k, 2)
    coeff = 2 * alpha / (alpha - 1)
    assert coeff == Fraction(2*k, k-2)

# Monotonicity of k/(k-2) for integer k>=3 on a representative range.
vals = [k/(k-2) for k in range(3, 100)]
assert all(vals[i+1] < vals[i] for i in range(len(vals)-1))
print("STATUS=PASS")
