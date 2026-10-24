import math
import numpy as np


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


ALPHA_L = 1.0 / phi(-1.0)
ALPHA_U = 12.75
TOTAL_L = 1.0 + ALPHA_L
TOTAL_U = 1.0 + ALPHA_U

# Deterministic finite-N witness that the approximate-rank theorem applies
# to a contaminant block having full ambient rank.
N = 5
r = 2
beta = 0.9
H = np.array([
    [1.0, 2.0],
    [0.0, -1.0],
    [3.0, 1.0],
    [-2.0, 4.0],
    [1.0, -3.0],
])
R = np.zeros((N, r))
R[0, 0] = 1.0
R[1, 1] = 1.0
L = H @ R.T
U = np.eye(N)
B = L + beta * U
svals = np.linalg.svd(B, compute_uv=False)
rank_B = np.linalg.matrix_rank(B, tol=1e-12)

# Here ker(L)=span(e_3,e_4,e_5), and B is beta*I there.
Q = np.eye(N)[:, r:]
restricted = B @ Q
restricted_op = np.linalg.svd(restricted, compute_uv=False)[0]

# Sharpness toy example for the universal margin-budget condition beta<=1.
# N=1, kappa=-1, B=[beta_bad] with beta_bad>1.  The contaminant forces
# x=+1, so a one-row Gaussian core is feasible iff g>=-1, whereas the
# isotropic core alone is always feasible on S^0={-1,+1}.
beta_bad = 1.1
full_feas_prob = phi(1.0)
iso_core_prob = 1.0

# Dimension-loss benchmark for r_N=floor(N^(2/3)) in the concrete model.
benchmarks = []
for NN in [10**3, 10**6, 10**9]:
    rr = int(math.floor(NN ** (2.0 / 3.0)))
    dim_frac = (NN - rr) / NN
    lower_total = 1.0 + dim_frac * ALPHA_L
    benchmarks.append((NN, rr, dim_frac, lower_total))

print(f"ALPHA_L_PHI_MINUS1 {ALPHA_L:.15f}")
print(f"PURE_T03_CERTIFIED_UPPER {ALPHA_U:.12f}")
print(f"FULLRANK_CONTAM_TOTAL_LOWER {TOTAL_L:.15f}")
print(f"FULLRANK_CONTAM_TOTAL_UPPER {TOTAL_U:.12f}")
print(f"FULLRANK_CONTAM_WINDOW_WIDTH {TOTAL_U - TOTAL_L:.15f}")
print("FINITE_EXAMPLE_RANK_B", rank_B)
print("FINITE_EXAMPLE_SINGULAR_VALUES", " ".join(f"{x:.12f}" for x in svals))
print(f"FINITE_EXAMPLE_S_RPLUS1 {svals[r]:.12f}")
print(f"FINITE_EXAMPLE_RESTRICTED_OP {restricted_op:.12f}")
print(f"FINITE_EXAMPLE_BETA {beta:.12f}")
assert rank_B == N
assert svals[r] <= beta + 1e-12
assert restricted_op <= beta + 1e-12
print(f"SHARPNESS_BAD_BETA {beta_bad:.12f}")
print(f"SHARPNESS_ISO_CORE_PROB {iso_core_prob:.15f}")
print(f"SHARPNESS_FULL_SYSTEM_PROB {full_feas_prob:.15f}")
assert full_feas_prob < iso_core_prob
for row in benchmarks:
    print("BENCHMARK", row[0], row[1], f"{row[2]:.12f}", f"{row[3]:.12f}")
print("ALL_CHECKS_PASS")
