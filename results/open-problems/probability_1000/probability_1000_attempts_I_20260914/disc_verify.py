"""Direct verification of the 6x6 witness: brute force over all 2^6 sign vectors, no solver involved."""
import numpy as np, itertools

rows = ["--++++", "+--+++", "+++-++", "+-++-+", "-+-+-+", "-----+"]
A = np.array([[1 if c == '+' else -1 for c in r] for r in rows])
print("A =\n", A)
print("row sums of A A^T (orthogonality is not required):", (A @ A.T)[0])
best = None; arg = None
for bits in itertools.product((1, -1), repeat=6):
    x = np.array(bits)
    v = int(np.abs(A @ x).max())
    if best is None or v < best: best, arg = v, x.copy()
print(f"\ndisc(A) = min over all 64 sign vectors of ||Ax||_inf = {best}")
print(f"   attained at x = {arg}, giving Ax = {A @ arg}")
print(f"   ratio disc/sqrt(6) = {best/np.sqrt(6):.4f}   against sqrt(2) = {np.sqrt(2):.4f}")

# and an exhaustive check that no 6x6 sign matrix does better, over all matrices with
# first row and first column normalised to +1 (row and column negations do not change disc)
print("\nexhaustive check over all 6x6 sign matrices, normalised: does any reach disc = 6?")
X = np.array(list(itertools.product((1, -1), repeat=6)))          # 64 sign vectors
R = X                                                              # candidate rows
T = np.abs(R @ X.T)                                                # 64 x 64
best6 = 0
# disc(A) = min_x max_{i} T[r_i, x]; maximise over 6-subsets by covering, checked directly for v=6
cov6 = (T >= 6)
print("   rows whose |r.x| >= 6 for some x: each row covers exactly", cov6[0].sum(), "sign vectors")
print("   so 6 rows can cover at most", 6 * cov6[0].sum(), "of the 64 sign vectors: disc = 6 impossible")
