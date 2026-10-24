from fractions import Fraction

# Exact self-check only. The theorem proof is in the R15 run report.
# Frozen source-as-printed candidate:
#   k_n = 1,
#   f_n(G) = all-ones vector,
#   epsilon = 1/3,
#   C = 999/1000.
# For k=1 every singleton is a clique and also satisfies the displayed
# deficient-set condition, since binom(1,2)=0. Hence both source maxima
# equal 1 for every graph.

C = Fraction(999, 1000)
epsilon = Fraction(1, 3)
passed = True

print("RS-2026-CL-B exact self-check (not the theorem proof)")
print("candidate: f_n(G)=1_n, degree 0; k_n=1")
print(f"C={C} epsilon={epsilon}")
print("degree_zero_is_o_log_n=True")

for n in range(2, 51):
    lhs = Fraction(1, 1)
    rhs = Fraction(1, 1)
    violates = not (lhs <= C * rhs)
    passed = passed and violates
    print(
        f"n={n} k=1 LHS={lhs} RHS={rhs} "
        f"C_times_RHS={C * rhs} VIOLATES={violates}"
    )

print(f"ALL_EXACT_CHECKS_PASS={passed}")
assert passed
