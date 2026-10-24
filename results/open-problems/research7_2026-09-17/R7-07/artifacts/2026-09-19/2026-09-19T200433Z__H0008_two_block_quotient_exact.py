from fractions import Fraction as F

# Four-type source-compatible witness from the accompanying admission note.
# q_j = 1/4, nu = 3 deterministically.
q = [F(1, 4)] * 4
P = [
    [F(1),   F(1, 2), F(3, 4), F(1, 4)],
    [F(3,4), F(3, 4), F(1, 8), F(7, 8)],
    [F(1,4), F(3, 4), F(1),   F(3, 4)],
    [F(2,3), F(1, 3), F(7, 8), F(7, 8)],
]

A = [[q[j] * P[i][j] for j in range(4)] for i in range(4)]


def signature(i, partition):
    return tuple(sum(A[i][j] for j in block) for block in partition)


def refine(partition):
    out = []
    for block in partition:
        groups = {}
        for i in block:
            groups.setdefault(signature(i, partition), []).append(i)
        out.extend(tuple(v) for v in groups.values())
    return out


history = []
partition = [tuple(range(4))]
while True:
    history.append(partition)
    nxt = refine(partition)
    if nxt == partition:
        break
    partition = nxt

assert partition == [(0, 1), (2, 3)]

# Verify strong lumpability on the terminal partition.
for block in partition:
    sig0 = signature(block[0], partition)
    for i in block[1:]:
        assert signature(i, partition) == sig0

C = []
for block in partition:
    i = block[0]
    C.append([sum(A[i][j] for j in target) for target in partition])

assert C == [
    [F(3, 8), F(1, 4)],
    [F(1, 4), F(7, 16)],
]

retention = [sum(row) for row in C]
assert retention == [F(5, 8), F(11, 16)]
assert retention[0] != retention[1]

m_star = F(3)
Mbar = [[m_star * x for x in row] for row in C]
assert Mbar == [
    [F(9, 8), F(3, 4)],
    [F(3, 4), F(21, 16)],
]

tr = Mbar[0][0] + Mbar[1][1]
det = Mbar[0][0] * Mbar[1][1] - Mbar[0][1] * Mbar[1][0]
disc = tr * tr - 4 * det
assert tr == F(39, 16)
assert det == F(117, 128)
assert disc == F(585, 256)
# sqrt(585) = 3 sqrt(65), so rho = (39 + 3 sqrt(65))/32.

# Verify the exact intertwining M E = E Mbar, where E lifts
# a 2-block vector to a block-constant 4-type vector.
M = [[m_star * x for x in row] for row in A]
ME = [
    [sum(M[i][j] for j in partition[B]) for B in range(2)]
    for i in range(4)
]
EMbar = [Mbar[0], Mbar[0], Mbar[1], Mbar[1]]
assert ME == EMbar

# Verify all hidden-label conditional kernels are positive and stochastic.
for Aidx, block in enumerate(partition):
    for i in block:
        for Bidx, target in enumerate(partition):
            denom = C[Aidx][Bidx]
            assert denom > 0
            probs = [A[i][j] / denom for j in target]
            assert all(x > 0 for x in probs)
            assert sum(probs) == 1

# R14's retained two-type diagnostic is already an irreducible two-block core:
# q=(1/2,1/2), P=[[3/4,3/4],[1/2,1/4]].
q2 = [F(1, 2), F(1, 2)]
P2 = [[F(3, 4), F(3, 4)], [F(1, 2), F(1, 4)]]
row_totals2 = [sum(q2[j] * P2[i][j] for j in range(2)) for i in range(2)]
assert row_totals2 == [F(3, 4), F(3, 8)]
assert row_totals2[0] != row_totals2[1]

print('refinement_history =', history)
print('coarsest_partition =', partition)
print('aggregate_block_probabilities =', C)
print('total_retention_by_block =', retention)
print('quotient_mean_matrix =', Mbar)
print('quotient_trace =', tr)
print('quotient_det =', det)
print('quotient_discriminant =', disc)
print('PF_root = (39 + 3*sqrt(65))/32')
print('intertwining_M_E_equals_E_Mbar =', ME)
print('diagnostic_row_totals =', row_totals2)
print('ALL_EXACT_CHECKS_PASS')
