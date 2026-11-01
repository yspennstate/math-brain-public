import itertools, json, math
import numpy as np

SEED = 20260923
TRIALS = 2500
rng = np.random.default_rng(SEED)

def orthogonal(m):
    q, _ = np.linalg.qr(rng.normal(size=(m, m)))
    return q

def one_case():
    m = int(rng.integers(5, 13))
    r = int(rng.integers(0, min(3, m-3)))
    K = int(rng.integers(0, min(3, m-r-2)))
    qmin = r + K + 3
    q = int(rng.integers(qmin, m+1))
    kappa = float(rng.uniform(1.0, 3.0))

    U = orthogonal(m)
    good = kappa + rng.random(m-r)*3.0
    bad = rng.uniform(-8.0, kappa-0.2, size=r) if r else np.array([])
    vals = np.concatenate([good, bad])
    rng.shuffle(vals)
    A0 = U @ np.diag(vals) @ U.T

    V = orthogonal(m)
    rv = rng.normal(0.0, 4.0, size=m)
    R = V @ np.diag(rv) @ V.T

    er, Ur = np.linalg.eigh(R)
    neg = np.clip(-er, 0.0, None)
    order = np.argsort(neg)[::-1]
    beta = neg[order]
    W = Ur[:, order]
    N = (W * beta) @ W.T
    NK = (W[:, :K] * beta[:K]) @ W[:, :K].T if K else np.zeros((m, m))
    H = N - NK
    tau = float(np.trace(H) / m)

    # Exact minimizing q-subset for the trace is the q smallest diagonal entries.
    d = np.diag(H)
    J = tuple(np.argsort(d)[:q].tolist())
    JJ = np.ix_(J, J)
    trJ = float(d[list(J)].sum())

    A0J = A0[JJ]
    baseline_good = int(np.sum(np.linalg.eigvalsh(A0J) >= kappa - 1e-8))

    RJ = R[JJ]
    local_hostile = np.sort(np.clip(-np.linalg.eigvalsh(RJ), 0.0, None))[::-1]
    k_local = q-r-3
    eta = float(local_hostile[k_local])
    ell = q-r-K-2
    bound = q*tau/ell

    return {
        "trace_average": trJ <= q*tau + 1e-8,
        "baseline_interlacing": baseline_good >= q-r,
        "hostile_bound": eta <= bound + 1e-8,
        "ratio": eta/bound if bound > 1e-12 else 0.0,
    }

rows = [one_case() for _ in range(TRIALS)]
out = {
    "seed": SEED,
    "trials": TRIALS,
    "all_pass": all(x["trace_average"] and x["baseline_interlacing"] and x["hostile_bound"] for x in rows),
    "max_eta_over_bound": max(x["ratio"] for x in rows),
    "example_constant_r1_K1_tau_le_g_over_4_q10": (24.0/7.0)*math.sqrt(60.0*math.pi),
    "note": "Finite floating-point sanity checks only; the proof in REPORT.md is deterministic and exact."
}
print(json.dumps(out, indent=2, sort_keys=True))
