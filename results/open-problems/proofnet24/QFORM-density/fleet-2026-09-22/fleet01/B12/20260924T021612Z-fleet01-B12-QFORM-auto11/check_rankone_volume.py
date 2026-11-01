import numpy as np

rng = np.random.default_rng(0)
max_relative_error = 0.0
violations = 0
trials = 5000

for _ in range(trials):
    p, m = 8, 5
    M = rng.normal(size=(p, m))
    if np.linalg.matrix_rank(M) < m:
        continue
    a = rng.normal(size=p)
    b = rng.normal(size=m)
    theta = 5.0 * rng.normal()
    G = M.T @ M
    c = np.linalg.solve(G, M.T @ a)
    a_perp = a - M @ c
    q = b @ c
    r = (a_perp @ a_perp) * (b @ np.linalg.solve(G, b))
    M1 = M + theta * np.outer(a, b)
    lhs = np.linalg.det(M1.T @ M1)
    rhs = np.linalg.det(G) * ((1.0 + theta*q)**2 + theta**2 * r)
    rel = abs(lhs-rhs) / max(1.0, abs(lhs), abs(rhs))
    max_relative_error = max(max_relative_error, rel)
    if lhs < -1e-8 or rhs < -1e-8:
        violations += 1

print({"trials": trials,
       "max_relative_error": max_relative_error,
       "sign_violations": violations})
