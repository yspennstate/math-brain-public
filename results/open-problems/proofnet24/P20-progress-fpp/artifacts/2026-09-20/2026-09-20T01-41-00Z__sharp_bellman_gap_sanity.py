import numpy as np, math

SEED = 20260920
N = 200000
U_GRID = [0.1, 0.25, 0.5, 1.0]
CASES = {
    "equal": [0.0, 0.0, 0.0, 0.0],
    "mild": [0.0, 0.2, 0.5, 1.0],
    "two_tied": [0.0, 0.0, 2.0, 2.0],
    "dominant": [0.0, 2.0, 4.0, 6.0],
    "split": [0.0, 1.0, 1.0, 1.0],
}

rng = np.random.default_rng(SEED)

def sample_s(offsets):
    a = np.asarray(offsets, dtype=float)
    E = rng.exponential(size=(N, 4))
    X = E + a[None, :]
    I = np.argmin(X, axis=1)
    M = X[np.arange(N), I]
    first_gap = X - M[:, None]
    slack = np.minimum(first_gap, 2.0 * E)
    slack[np.arange(N), I] = np.inf
    return np.min(slack, axis=1)

print(f"seed={SEED} N={N}")
print("theorem_bound: P(S>u|outside)>=exp(-3u), E[S|outside]>=1/3")
for name, offsets in CASES.items():
    S = sample_s(offsets)
    print(name, "mean", f"{S.mean():.12f}")
    for u in U_GRID:
        emp = np.mean(S > u)
        bound = math.exp(-3.0*u)
        print(" ", f"u={u:.2f}", f"emp_tail={emp:.8f}", f"bound={bound:.8f}",
              f"diff={emp-bound:+.8f}")
