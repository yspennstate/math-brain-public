import itertools
import numpy as np

rng = np.random.default_rng(20260923)
trials = 500
max_scaled_identity_error = 0.0
min_schur_slack = float("inf")
failures = 0

for _ in range(trials):
    m = int(rng.integers(3, 8))
    k = int(rng.integers(3, 8))
    M = rng.normal(size=(m, k))
    b = M[0].copy()
    N = M[1:].copy()
    nb = np.linalg.norm(b)
    if nb < 1e-12:
        continue

    P = np.eye(k) - np.outer(b, b) / (nb * nb)

    J = 0.0
    for rr in itertools.combinations(range(1, m), 2):
        rows = (0,) + rr
        for cc in itertools.combinations(range(k), 3):
            J += np.linalg.det(M[np.ix_(rows, cc)]) ** 2

    NP = N @ P
    s = np.linalg.svd(NP, compute_uv=False)
    E2_NP = sum(
        (s[a] ** 2) * (s[bidx] ** 2)
        for a in range(len(s))
        for bidx in range(a + 1, len(s))
    )
    rhs = (nb * nb) * E2_NP
    scaled_error = abs(J - rhs) / max(1.0, abs(J), abs(rhs))
    max_scaled_identity_error = max(max_scaled_identity_error, scaled_error)

    d = float(rng.normal())
    if abs(d) < 0.1:
        d = 0.1 if d >= 0 else -0.1
    u = rng.normal(size=m - 1)
    C = N - np.outer(u, b) / d
    sc = np.linalg.svd(C, compute_uv=False)
    E2_C = sum(
        (sc[a] ** 2) * (sc[bidx] ** 2)
        for a in range(len(sc))
        for bidx in range(a + 1, len(sc))
    )
    slack = E2_C - E2_NP
    min_schur_slack = min(min_schur_slack, slack)

    if scaled_error > 1e-10 or slack < -1e-10:
        failures += 1

print(f"trials={trials}")
print(f"max_scaled_identity_error={max_scaled_identity_error:.17g}")
print(f"min_schur_slack={min_schur_slack:.17g}")
print(f"failures={failures}")
print("STATUS=PASS" if failures == 0 else "STATUS=FAIL")
