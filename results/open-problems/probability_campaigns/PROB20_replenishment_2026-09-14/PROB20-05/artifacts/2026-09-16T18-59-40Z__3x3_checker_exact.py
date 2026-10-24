from fractions import Fraction
from itertools import permutations

# Exact 3x3 permutation-checkerboard transport certificates.
# For each permutation sigma, table J[a][b] assigns each source coarse cell (a,b)
# to target diagonal cell (j, sigma(j)). Each j must receive exactly 3 source cells.
CERT = {
    (0,1,2): [[0,0,1],[0,1,2],[1,2,2]],
    (0,2,1): [[0,0,1],[0,2,1],[2,2,1]],
    (1,0,2): [[0,0,0],[1,1,2],[1,2,2]],
    (1,2,0): [[0,0,0],[2,1,1],[2,2,1]],
    (2,0,1): [[1,0,0],[1,1,0],[2,2,2]],
    (2,1,0): [[1,0,0],[2,1,0],[2,2,1]],
}

assert set(CERT) == set(permutations(range(3)))

max_cost = Fraction(0)
for sigma in sorted(CERT):
    J = CERT[sigma]
    counts = [sum(J[a][b] == j for a in range(3) for b in range(3)) for j in range(3)]
    assert counts == [3,3,3]
    integer_cost = sum(
        (a - J[a][b])**2 + (b - sigma[J[a][b]])**2
        for a in range(3) for b in range(3)
    )
    continuum_cost = Fraction(integer_cost, 81)
    max_cost = max(max_cost, continuum_cost)
    print(f"sigma={sigma} counts={counts} integer_cost={integer_cost} continuum_cost={continuum_cost}")

assert max_cost == Fraction(8,81)
assert max_cost < Fraction(1,10)
assert Fraction(1,10) - max_cost == Fraction(1,810)

# Failure of the previous y-frozen conditional-quantile algorithm on the
# 3x3 identity checkerboard: its exact cost is 1/9 > 1/10.
# Conditional target x-law is uniform on I_j; quantile map u -> (j+u)/3.
conditional_costs = []
for j in range(3):
    # Integral_0^1 (u - (j+u)/3)^2 du.
    # Expand exactly: ((2u-j)/3)^2.
    integral = Fraction(1,9) * (Fraction(4,3) - 2*j + j*j)
    conditional_costs.append(integral)
y_frozen = sum(conditional_costs, Fraction(0))/3
assert conditional_costs == [Fraction(4,27), Fraction(1,27), Fraction(4,27)]
assert y_frozen == Fraction(1,9)
assert y_frozen > Fraction(1,10)

print(f"max_permutation_checkerboard_certificate={max_cost}")
print(f"strict_gap_to_diagonal={Fraction(1,10)-max_cost}")
print(f"y_frozen_identity_cost={y_frozen}")
print("PROB20-05 3X3 CHECKERBOARD EXACT CHECK PASSED")
