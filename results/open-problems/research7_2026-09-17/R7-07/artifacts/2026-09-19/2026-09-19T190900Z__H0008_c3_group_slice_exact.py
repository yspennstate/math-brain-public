from fractions import Fraction as F

ID = "H0008"
assert sum(map(ord, ID)) % 7 == 6

# Exact C3 group-covariant nonreversible example.
# Types are 0,1,2 mod 3 and p_ij = r[(j-i) mod 3].
r = [F(1, 1), F(3, 4), F(1, 4)]
R = sum(r, F(0, 1))
t = R / 3
nu = F(4, 1)
mean = nu * t
alpha = [x / R for x in r]

# Kolmogorov 3-cycle defect.
forward = r[1] ** 3
reverse = r[2] ** 3
ratio = forward / reverse

# Conditional transmitted-child type kernel on C3.
Pi = [[alpha[(j - i) % 3] for j in range(3)] for i in range(3)]
uniform = [F(1, 3)] * 3
stationary = [sum(uniform[i] * Pi[i][j] for i in range(3)) for j in range(3)]
db01 = (uniform[0] * Pi[0][1], uniform[1] * Pi[1][0])

# Offspring K | nu=4 ~ Binomial(4,2/3).
varK = nu * t * (1 - t)

assert R == 2
assert t == F(2, 3)
assert mean == F(8, 3) > 1
assert alpha == [F(1, 2), F(3, 8), F(1, 8)]
assert stationary == uniform
assert db01 == (F(1, 8), F(1, 24))
assert forward == F(27, 64)
assert reverse == F(1, 64)
assert ratio == 27
assert varK == F(8, 9) > 0

print("H0008_SHARD", sum(map(ord, ID)) % 7)
print("R_SUM", R)
print("t", t)
print("GW_MEAN", mean)
print("alpha", alpha)
print("Pi")
for row in Pi:
    print(row)
print("uniform_stationary", stationary)
print("detailed_balance_01", db01)
print("cycle_forward", forward)
print("cycle_reverse", reverse)
print("cycle_ratio", ratio)
print("VarK", varK)
print("ALL_EXACT_CHECKS_PASS")
