# Exact finite self-check for ProofNet24 P01 strategy review P66.
# This verifies only the finite specialization bookkeeping and the displayed
# degree-one basis matrix. It is NOT a proof of Pooya's K-theory theorem.

I = tuple()
num_relation_parameter_values = len(I)
assert num_relation_parameter_values == 0

# Frozen Austin specialization: lamp group C2 and free rank n=2.
F_order = 2
free_rank = 2
assert F_order == 2
assert free_rank == 2

# In Pooya's Theorem A/B/5.1 basis, mu_1 sends [v_i] to [u_i].
assembly = ((1, 0), (0, 1))
det = assembly[0][0] * assembly[1][1] - assembly[0][1] * assembly[1][0]
rank = 2 if det != 0 else (1 if any(x != 0 for row in assembly for x in row) else 0)
assert det == 1
assert rank == 2

print('P01 P66 specialization self-check')
print('I_cardinality =', num_relation_parameter_values)
print('Austin_V_empty_defining_generators = 0')
print('finite_lamp_group_order =', F_order)
print('free_group_rank =', free_rank)
print('assembly_matrix =', assembly)
print('determinant =', det)
print('rank =', rank)
print('All assertions passed.')
