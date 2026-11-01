from itertools import product
from math import comb

# Independent exact-arithmetic audit of:
# C30-N11-M27-STRUCTURAL-02
# H = K_{5,5} minus C_10; n=11, m=27.

INF = 10**100

def ceil_div(a, b):
    return (a + b - 1) // b

# 1. Classify all 30 nonconstant binary cyclic left words.
# A cyclic triple 000 contributes d_a, 111 contributes d_b,
# and every mixed triple contributes codegree c(a,b).
type_counts = {}
for w in product((0, 1), repeat=5):
    if len(set(w)) == 1:
        continue
    da = db = cc = 0
    for j in range(5):
        tri = (w[j], w[(j + 1) % 5], w[(j + 2) % 5])
        if tri == (0, 0, 0):
            da += 1
        elif tri == (1, 1, 1):
            db += 1
        else:
            cc += 1
    key = (da, db, cc)
    type_counts[key] = type_counts.get(key, 0) + 1

expected_types = {
    (2, 0, 3): 5,
    (1, 0, 4): 5,
    (0, 0, 5): 10,
    (0, 1, 4): 5,
    (0, 2, 3): 5,
}
assert type_counts == expected_types

# 2. Low-degree deletion branch, worst case d(v)=3:
# (48/54)^15 * (11/10)^20 >= 1,
# i.e. (8/9)^15 >= (10/11)^20.
delete_left = 8**15 * 11**20
delete_right = 9**15 * 10**20
assert delete_left >= delete_right
delete_margin = delete_left - delete_right

# 3. Exact DP over degree sequences:
# 11 simple-graph degrees in [4,10] with sum 54.
def min_sum_obj(obj):
    dp = {(0, 0): 0}
    for _ in range(11):
        ndp = {}
        for (k, s), val in dp.items():
            for x in range(4, 11):
                key = (k + 1, s + x)
                cand = val + obj(x)
                if cand < ndp.get(key, INF):
                    ndp[key] = cand
        dp = ndp
    return dp[(11, 54)]

one_symbol_floor = min_sum_obj(lambda x: x**5)
total_codegree_floor = min_sum_obj(lambda x: comb(x, 2))
assert one_symbol_floor == 32274
assert total_codegree_floor == 106

# 4. Pair lower envelope. Since d_a,d_b >= max(4,c),
# 10 c^5 + 5(d_a+d_b)c^4 + 5(d_a^2+d_b^2)c^3
# is at least F(c).
def F(c):
    q = max(4, c)
    return 10*c**5 + 10*q*c**4 + 10*q*q*c**3

f_values = [F(c) for c in range(11)]
first_diff = [f_values[i + 1] - f_values[i] for i in range(10)]
second_diff = [first_diff[i + 1] - first_diff[i] for i in range(9)]
assert all(x >= 0 for x in first_diff)
assert all(x >= 0 for x in second_diff)

# 5. Exact DP over 55 unordered pairs, codegrees c in [0,10],
# with total codegree at least 106.
dp = {0: 0}
for _ in range(55):
    ndp = {}
    for s, val in dp.items():
        for c in range(11):
            ns = s + c
            cand = val + F(c)
            if cand < ndp.get(ns, INF):
                ndp[ns] = cand
    dp = ndp

pair_floor = min(v for s, v in dp.items() if s >= 106)
best_s = min(s for s, v in dp.items() if s >= 106 and v == pair_floor)
assert pair_floor == 115080
assert best_s == 106

# 6. Source-normalized integer threshold and final margin.
structural_lower_bound = one_symbol_floor + pair_floor
source_integer_threshold = ceil_div(54**15, 11**20)
final_margin = structural_lower_bound * 11**20 - 54**15

assert structural_lower_bound == 147354
assert source_integer_threshold == 143898
assert final_margin == 2325483985034728958670330

print("C29 independent audit of C30-N11-M27-STRUCTURAL-02")
print("binary_type_counts =", sorted(type_counts.items()))
print("deletion_margin =", delete_margin)
print("one_symbol_floor =", one_symbol_floor)
print("total_codegree_floor =", total_codegree_floor)
print("F_values_0_to_10 =", f_values)
print("pair_floor_at_total_codegree>=106 =", pair_floor, "attained_first_at", best_s)
print("structural_lower_bound =", structural_lower_bound)
print("source_integer_threshold =", source_integer_threshold)
print("final_margin =", final_margin)
print("ALL_EXACT_CHECKS_PASS")
