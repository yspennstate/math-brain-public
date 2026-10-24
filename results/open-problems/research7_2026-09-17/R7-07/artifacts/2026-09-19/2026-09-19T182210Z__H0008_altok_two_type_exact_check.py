from fractions import Fraction as F

canonical_id = "H0008"
checksum = sum(map(ord, canonical_id))

q = [F(1, 2), F(1, 2)]
P = [
    [F(3, 4), F(3, 4)],
    [F(1, 2), F(1, 4)],
]

t = [sum(q[j] * P[i][j] for j in range(2)) for i in range(2)]
Pi = [[q[j] * P[i][j] / t[i] for j in range(2)] for i in range(2)]
mu = [F(4, 7), F(3, 7)]

assert checksum == 272
assert checksum % 7 == 6
assert t == [F(3, 4), F(3, 8)]
assert Pi == [[F(1, 2), F(1, 2)], [F(2, 3), F(1, 3)]]
assert sum(mu) == 1
assert mu[0] * Pi[0][1] == mu[1] * Pi[1][0] == F(2, 7)

print(f"canonical_id={canonical_id}")
print(f"checksum={checksum}")
print(f"residue_mod_7={checksum % 7}")
print(f"t1={t[0]}")
print(f"t2={t[1]}")
print(f"Pi11={Pi[0][0]}")
print(f"Pi12={Pi[0][1]}")
print(f"Pi21={Pi[1][0]}")
print(f"Pi22={Pi[1][1]}")
print(f"mu1={mu[0]}")
print(f"mu2={mu[1]}")
print(f"detailed_balance_12={mu[0] * Pi[0][1]}")
print(f"detailed_balance_21={mu[1] * Pi[1][0]}")
print("ALL_EXACT_CHECKS_PASS")
