import math
import numpy as np

# Deterministic regression for QFORM-SPECTRAL-DELETION-RETENTION-v1, r=4.
rng = np.random.default_rng(123)
violations = 0
minimum_ratio = float("inf")
minimum_slack = float("inf")
tests = 0
worst = None

for n in range(5, 20):
    for rep in range(2000):
        M = rng.normal(size=(n, n))
        A = (M + M.T) / 2
        w, V = np.linalg.eigh(A)
        idx = np.argsort(np.abs(w))[::-1]
        s = np.abs(w[idx])
        V = V[:, idx]
        for _ in range(2):
            i = int(rng.integers(n))
            p = float(np.sum(V[i, :4] ** 2))
            C = np.delete(np.delete(A, i, axis=0), i, axis=1)
            sc = np.linalg.svd(C, compute_uv=False)
            rhs = float(s[3] * math.sqrt(max(0.0, 1.0 - p)))
            lhs = float(sc[2])
            tests += 1
            slack = lhs - rhs
            minimum_slack = min(minimum_slack, slack)
            if rhs > 1e-14:
                ratio = lhs / rhs
                if ratio < minimum_ratio:
                    minimum_ratio = ratio
                    worst = (n, rep, i, lhs, rhs, p, float(s[3]))
            if lhs + 1e-10 < rhs:
                violations += 1

eta = 0.31987395050000694
C_R = 288 * math.sqrt(3 * math.e) / 13
m = eta / math.sqrt(2)

print("tests", tests)
print("violations", violations)
print("minimum_ratio", minimum_ratio)
print("minimum_slack", minimum_slack)
print("worst", worst)
print("eta", eta)
print("C_R", C_R)
print("m", m)
print("C_R/m", C_R / m)
print("64/m", 64 / m)
print("m/512", m / 512)
print("eta/512", eta / 512)

if violations != 0:
    raise SystemExit("QFORM_B08_R51_CHECK_FAIL")
print("QFORM_B08_R51_CHECK_PASS")
