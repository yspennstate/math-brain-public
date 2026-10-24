from fractions import Fraction as Q

# Exact-arithmetic certification for the K4 short-time auxiliary-gap split
# used in the P0279 B14/B5/B24 run.  No floating-point arithmetic appears.

theta = Q(1, 4)  # tanh(beta)
tanh3 = (3 * theta + theta**3) / (1 + 3 * theta**2)
assert tanh3 == Q(49, 76)

# All-plus initial state on K4.
c_plus = (1 - tanh3) / 2
c_after_neighbor_flip = (1 - theta) / 2
a = c_after_neighbor_flip - c_plus
assert c_plus == Q(27, 152)
assert c_after_neighbor_flip == Q(3, 8)
assert a == Q(15, 76)

# First-order perturbation matrix M_+ has zero diagonal and off-diagonal a.
Mplus = [[Q(0) if i == j else a for j in range(4)] for i in range(4)]

# Balanced ++-- initial state on K4.
c_bal = (1 + theta) / 2
c_same_after = (1 + tanh3) / 2
same = c_same_after - c_bal
opp = (1 - theta) / 2 - c_bal
assert c_bal == Q(5, 8)
assert c_same_after == Q(125, 152)
assert same == Q(15, 76)
assert opp == Q(-1, 4)

Mbal = [[Q(0) for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        if i == j:
            continue
        same_group = (i < 2) == (j < 2)
        Mbal[i][j] = same if same_group else opp


def mv(M, v):
    return [sum(M[i][j] * v[j] for j in range(4)) for i in range(4)]


def check_eigen(M, v, lam):
    assert mv(M, v) == [lam * x for x in v]

# Exact eigenbasis/eigenvalues for Mplus.
check_eigen(Mplus, [1, 1, 1, 1], Q(45, 76))
check_eigen(Mplus, [1, -1, 0, 0], Q(-15, 76))
check_eigen(Mplus, [0, 1, -1, 0], Q(-15, 76))
check_eigen(Mplus, [0, 0, 1, -1], Q(-15, 76))

# Exact eigenbasis/eigenvalues for Mbal.
check_eigen(Mbal, [1, 1, -1, -1], Q(53, 76))
check_eigen(Mbal, [1, 1, 1, 1], Q(-23, 76))
check_eigen(Mbal, [1, -1, 0, 0], Q(-15, 76))
check_eigen(Mbal, [0, 0, 1, -1], Q(-15, 76))

lambda_plus = Q(45, 76)
lambda_bal = Q(53, 76)
assert lambda_bal - lambda_plus == Q(2, 19)
assert lambda_bal > lambda_plus

# K4 has Delta=3.  This chosen theta lies strictly inside tree uniqueness.
Delta = 3
assert (Delta - 1) * theta == Q(1, 2) < 1
# It also lies strictly inside the Dobrushin row-sum region Delta*theta<1.
assert Delta * theta == Q(3, 4) < 1

print("EXACT_CHECK_PASS")
print(f"theta={theta}")
print(f"tanh(3 beta)={tanh3}")
print(f"a={a}")
print(f"lambda_max(M_plus)={lambda_plus}")
print(f"lambda_max(M_balanced)={lambda_bal}")
print(f"slope_gap_difference={lambda_bal - lambda_plus}")
print(f"tree_uniqueness_margin={(1 - (Delta - 1) * theta)}")
print(f"dobrushin_margin={(1 - Delta * theta)}")
