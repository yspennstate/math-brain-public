#!/usr/bin/env python3
# Exact finite witness for the two-arm minimax obstruction in H0017.
B = ((-1, 1), (1, -1))

sup_x_min_i = max(min(row) for row in B)
min_i_sup_x = min(max(B[r][c] for r in range(len(B))) for c in range(len(B[0])))

print(f"sup_x min_i B_i(0,x) = {sup_x_min_i}")
print(f"min_i sup_x B_i(0,x) = {min_i_sup_x}")

assert sup_x_min_i == -1
assert min_i_sup_x == 1
assert sup_x_min_i < 0 < min_i_sup_x
print("TWO_ARM_MINIMAX_OBSTRUCTION_PASS")
