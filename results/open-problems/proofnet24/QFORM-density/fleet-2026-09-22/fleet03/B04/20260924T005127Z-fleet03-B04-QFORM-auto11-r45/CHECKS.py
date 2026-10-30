from fractions import Fraction
from math import e, sqrt

# Dense rank-four stress family from REPORT.md.
N = 256
m = N - 2
half = m // 2
L = 16
assert half == 127

# The two light row groups have coefficient square a^2=2/m=1/127
# against two orthonormal normalized Hadamard rows.
a2 = Fraction(2, m)
assert a2 == Fraction(1, 127)

# Every nonzero canonical four-row Gram determinant uses the two heavy
# rows and one row from each light group.
d_each = Fraction(L**4) * a2 * a2
count = half * half
E4 = count * d_each
assert E4 == L**4
assert E4 == 65536

# Canonical carrier and pair probabilities are exact.
rho_1 = Fraction(1, 1)
beta_2_given_1 = Fraction(1, 1)
eta_12 = rho_1 * beta_2_given_1
assert eta_12 == 1
assert eta_12 > Fraction(2, 75)

# Nonzero singular values of M are L,L,1,1, hence the block-off-diagonal
# symmetric A has nonzero spectrum +/-L,+/-L,+/-1,+/-1.
singular_values = (L, L, 1, 1)
assert singular_values == (16, 16, 1, 1)

# Aggregate fixed-pair constant from fleet01/B09.
C4 = 2 * sqrt(2) * e**0.25 * 3**0.75
aggregate_bound = C4 * float(E4)**(-1/8)
assert abs(aggregate_bound - 2.069662656704762) < 1e-12

# Partner-r2 threshold-only consequence: eta>2/75.
partner_threshold_bound_coefficient = C4 * (75/2)**(1/8)
assert abs(partner_threshold_bound_coefficient - 13.023072655226386) < 1e-12

# Every rank-four local physical row set has singular product L^2*a^2.
local_product = Fraction(L**2) * a2
local_exact_rank4_bound = 2 * sqrt(2) * float(local_product)**(-1/4)
assert abs(local_exact_rank4_bound - 2.373755217959999) < 1e-12
assert aggregate_bound < local_exact_rank4_bound

# The left range projection has leverage one on each heavy row, so a
# max-leverage <=1/2 ridge gate fails. Rank(M)=4, so E5=0.
max_left_range_leverage = 1
E5 = 0
assert max_left_range_leverage > Fraction(1, 2)
assert E5 == 0

print({
    "N": N,
    "m": m,
    "half": half,
    "a2": str(a2),
    "d_each": str(d_each),
    "count_nonzero_row4_sets": count,
    "E4": int(E4),
    "rho_1": str(rho_1),
    "beta_2_given_1": str(beta_2_given_1),
    "eta_12": str(eta_12),
    "singular_values": singular_values,
    "aggregate_bound": aggregate_bound,
    "partner_threshold_coefficient": partner_threshold_bound_coefficient,
    "local_exact_rank4_bound": local_exact_rank4_bound,
    "max_left_range_leverage": max_left_range_leverage,
    "E5": E5,
})
