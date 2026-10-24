# Exact local Boolean sanity check for the only finite local implication in
# the pentagon-incidence lemma.
# Central v is selected. Full opposite pentagons force all four cyclic
# neighbors n0,n1,n2,n3 selected. Each incident square has an opposite
# corner t. If t is unselected, it has the two selected square neighbors,
# violating the multiplicity-one exterior-boundary condition.

allowed=[]
for t0 in (0,1):
    for t1 in (0,1):
        # n0=n1=n2=n3=1 from the two full pentagons.
        mult_t0 = 2 if t0 == 0 else 0
        mult_t1 = 2 if t1 == 0 else 0
        multiplicity_one = mult_t0 <= 1 and mult_t1 <= 1
        if multiplicity_one:
            allowed.append((t0,t1))
assert allowed == [(1,1)]
print('ALLOWED_SQUARE_OPPOSITE_SELECTIONS', allowed)
print('BOTH_PENTAGONS_FULL_PLUS_MULTIPLICITY_ONE_FORCES_BOTH_SQUARES_FULL')
print('ALL_LOCAL_EXACT_CHECKS_PASS')