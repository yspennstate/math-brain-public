import json
import math
import numpy as np

SEED = 20260923
rng = np.random.default_rng(SEED)


def counts(vals, L):
    return {
        "pos": int(np.sum(vals >= L)),
        "neg": int(np.sum(vals <= -L)),
        "abs": int(np.sum(np.abs(vals) >= L)),
    }


def schur(A, I):
    n = A.shape[0]
    I = np.array(I, dtype=int)
    Iset = set(int(x) for x in I)
    J = np.array([j for j in range(n) if j not in Iset], dtype=int)
    B = A[np.ix_(I, I)]
    C = A[np.ix_(J, J)]
    E = A[np.ix_(I, J)]
    return C - E.T @ np.linalg.inv(B) @ E


violations = []
tests = 0
thresholds = (0.25, 0.5, 1.0, 1.5, 2.0)

for n in range(3, 10):
    for p in range(1, min(3, n - 1) + 1):
        for _ in range(500):
            Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
            lam = rng.uniform(-4.0, 4.0, size=n)
            tiny = np.abs(lam) < 0.15
            lam[tiny] += np.sign(lam[tiny] + 1e-9) * 0.3
            A = Q @ np.diag(lam) @ Q.T
            I = rng.choice(n, p, replace=False)
            B = A[np.ix_(I, I)]
            if abs(np.linalg.det(B)) < 1e-7:
                continue
            S = schur(A, I)
            eigA = np.linalg.eigvalsh(A)
            eigS = np.linalg.eigvalsh(S)
            for L in thresholds:
                ca = counts(eigA, L)
                cs = counts(eigS, L)
                tests += 1
                if (
                    cs["pos"] < max(0, ca["pos"] - p)
                    or cs["neg"] < max(0, ca["neg"] - p)
                    or cs["abs"] < max(0, ca["abs"] - p)
                ):
                    violations.append(
                        {
                            "n": n,
                            "p": p,
                            "L": L,
                            "A_counts": ca,
                            "S_counts": cs,
                        }
                    )

result = {
    "seed": SEED,
    "threshold_tests": tests,
    "violations": len(violations),
    "first_violation": violations[0] if violations else None,
    "six_sqrt_pi": 6.0 * math.sqrt(math.pi),
    "four_sqrt_six_sqrt_pi": 4.0 * math.sqrt(6.0 * math.sqrt(math.pi)),
    "note": "Finite numerical sanity check only; the theorem is proved by inverse-principal interlacing in REPORT.md.",
}
print(json.dumps(result, indent=2, sort_keys=True))
