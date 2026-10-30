import json, math
import numpy as np

SEED = 350035
TRIALS = 10000
rng = np.random.default_rng(SEED)
tested = 0
violations = 0
min_margin = float("inf")
worst = None

for it in range(TRIALS):
    n = int(rng.integers(10, 35))
    m = int(rng.integers(5, n))
    Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    vals = rng.uniform(-4, 4, size=n)
    A = (Q * vals) @ Q.T
    Lam = float(rng.uniform(0.4, 1.8))
    high = np.abs(vals) >= Lam
    if not np.any(high):
        continue
    P = Q[:, high] @ Q[:, high].T
    H = np.sort(rng.choice(n, size=m, replace=False))
    L = np.setdiff1d(np.arange(n), H)
    C = A[np.ix_(H, H)]
    B = A[np.ix_(H, L)]
    PH = P[np.ix_(H, H)]
    pe = np.linalg.eigvalsh(PH)[::-1]
    cs = np.linalg.svd(C, compute_uv=False)
    bs = np.linalg.svd(B, compute_uv=False)

    for r in range(min(4, m)):
        c = float(cs[r])
        for k in range(r + 1, m + 1):
            if k - r > len(bs):
                continue
            a = float(pe[k - 1])
            rhs = Lam * Lam * a - c * c
            if rhs <= 1e-10:
                continue
            tested += 1
            lhs = float(bs[k - r - 1] ** 2)
            margin = lhs - rhs
            if margin < min_margin:
                min_margin = margin
                worst = {
                    "trial": it, "n": n, "m": m, "Lambda": Lam,
                    "r": r, "k": k, "a": a, "c": c,
                    "lhs_singular_square": lhs, "rhs": rhs
                }
            if margin < -1e-8:
                violations += 1

out = {
    "seed": SEED,
    "trials": TRIALS,
    "positive_certificates_tested": tested,
    "violations": violations,
    "minimum_margin_lhs_minus_rhs": min_margin,
    "worst_case": worst,
    "constants": {
        "seven_carrier_physical": 2 * math.sqrt(84 * math.pi),
        "seven_carrier_ridge": 15 * math.sqrt(6 * math.e) / 2,
        "five_carrier_physical": 2 * math.sqrt(60 * math.pi),
        "five_carrier_volume": 3 * math.sqrt(2) * math.e,
        "partner_gap": (41 - 5 * math.sqrt(17)) / 20,
        "partner_bound": 40 * math.sqrt(30 * math.pi) / (41 - 5 * math.sqrt(17))
    },
    "note": "Finite numerical sanity checks only; the proof is analytic."
}
print(json.dumps(out, indent=2, sort_keys=True))
