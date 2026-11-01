import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923)
max_decomp = 0.0
max_overlap = 0.0
max_schur = 0.0
max_cut = 0.0
min_interlace_margin = float('inf')

for n in range(4, 9):
    A = rng.normal(size=(n, n))
    A = (A + A.T) / 2
    if abs(A[0, 0]) < 0.2:
        A[0, 0] += 1.0
    a = A[0, 0]
    r = A[1:, 0]
    H = A[1:, 1:] - np.outer(r, r) / a

    sA = np.linalg.svd(A, compute_uv=False)
    sH = np.linalg.svd(H, compute_uv=False)
    min_interlace_margin = min(min_interlace_margin, sH[1] - sA[2])

    m = n - 1
    pairs = list(itertools.combinations(range(m), 2))
    s = np.linalg.svd(H, compute_uv=False)
    exterior = sum((s[p] * s[q]) ** 2
                   for p in range(m) for q in range(p + 1, m))

    principal = overlap = disjoint = 0.0
    for R in pairs:
        for C in pairs:
            minor = np.linalg.det(H[np.ix_(R, C)])
            z = minor * minor
            d = len(set(R).intersection(C))
            if d == 2:
                principal += z
            elif d == 1:
                overlap += z
            else:
                disjoint += z

            AR = [0] + [x + 1 for x in R]
            AC = [0] + [x + 1 for x in C]
            lifted = np.linalg.det(A[np.ix_(AR, AC)])
            max_schur = max(max_schur, abs(lifted - a * minor))

    # The partner W2 sum after the first scalar completion.
    wsum = 0.0
    for j in range(m):
        rest = [k for k in range(m) if k != j]
        for k in rest:
            for ell in rest:
                if k == ell:
                    continue
                wsum += (H[j, j] * H[k, ell] - H[j, k] * H[j, ell]) ** 2

    max_decomp = max(max_decomp, abs(exterior - principal - overlap - disjoint))
    max_overlap = max(max_overlap, abs(overlap - wsum))

    # Exhaust all fair two-colourings for these small dimensions.
    cut_values = []
    for bits in itertools.product([0, 1], repeat=m):
        I = [i for i, bit in enumerate(bits) if bit == 0]
        J = [i for i, bit in enumerate(bits) if bit == 1]
        e2 = 0.0
        if len(I) >= 2 and len(J) >= 2:
            for R in itertools.combinations(I, 2):
                for C in itertools.combinations(J, 2):
                    e2 += np.linalg.det(H[np.ix_(R, C)]) ** 2
        cut_values.append(e2)
    max_cut = max(max_cut, abs(sum(cut_values) / len(cut_values) - disjoint / 16))

C_E2 = 2 * math.sqrt(10) * 7 ** (9 / 10)
C_disjoint = C_E2 * math.sqrt(2)
C_branch = C_disjoint * 3 ** (1 / 8)
C_alpha_1_64 = 8 * C_branch

print(f'max_compound_decomposition_error={max_decomp:.3e}')
print(f'max_partner_overlap_identity_error={max_overlap:.3e}')
print(f'max_scalar_schur_minor_lift_error={max_schur:.3e}')
print(f'max_random_cut_expectation_error={max_cut:.3e}')
print(f'min_interlacing_margin_s2H_minus_s3A={min_interlace_margin:.12g}')
print(f'C_E2={C_E2:.12f}')
print(f'C_disjoint={C_disjoint:.12f}')
print(f'C_branch_D_ge_1_over_3={C_branch:.12f}')
print(f'C_branch_alpha_1_over_64={C_alpha_1_64:.12f}')
assert max_decomp < 1e-9
assert max_overlap < 1e-9
assert max_schur < 1e-10
assert max_cut < 1e-10
assert min_interlace_margin > -1e-10
print('STATUS=PASS')
