import itertools, math
import numpy as np

# Live threshold constants from the proof.
tau = 3/10
prod_lower = 7*tau*tau/256
holder_const = math.sqrt(math.e) * math.pi**0.25 * prod_lower**(-0.25)
assert abs(prod_lower - 63/25600) < 1e-15
assert holder_const < 9.856
print(f"two_channel_product_lower={prod_lower:.12f}")
print(f"half_holder_constant={holder_const:.12f}")

# Exact target-class star adversary against a forced rank-two cross cut.
A = np.array([
    [0.,1.,1.,1.],
    [1.,2.,0.,0.],
    [1.,0.,2.,0.],
    [1.,0.,0.,2.],
])
H = A - np.diag(np.diag(A))
eigs = np.linalg.eigvalsh(A)
svH = np.linalg.svd(H, compute_uv=False)
assert np.allclose(eigs, [-1.,2.,2.,3.], atol=1e-12)
assert np.allclose(svH[:2], [math.sqrt(3), math.sqrt(3)], atol=1e-12)
max_cross_rank = 0
cuts = []
# Fix vertex 0 on the + side to avoid complement duplicates.
for bits in itertools.product([1,-1], repeat=3):
    eps = (1,) + bits
    I = [i for i,e in enumerate(eps) if e == 1]
    J = [i for i,e in enumerate(eps) if e == -1]
    if not I or not J:
        continue
    C = H[np.ix_(I,J)]
    rank = np.linalg.matrix_rank(C, tol=1e-12)
    s = np.linalg.svd(C, compute_uv=False)
    s2 = s[1] if len(s) > 1 else 0.0
    max_cross_rank = max(max_cross_rank, rank)
    cuts.append((I,J,rank,s2))
assert max_cross_rank == 1
assert all(abs(row[3]) < 1e-12 for row in cuts)
print("A_eigenvalues=", [round(x,12) for x in eigs])
print("H_top_singular_values=", [round(x,12) for x in svH[:2]])
print("max_cut_cross_rank=", max_cross_rank)
print("all_cut_second_singular_zero=", True)
print("QFORM_CROSSCUT_HALF_HOLDER_CHECK_PASS")
