"""End-to-end check of Theorem 1.1 on tight laws and adversarial structures (the T1 test of verify.py, made cheap).

Every coordinate is uniform on [0,1] or on [-1/2,1/2] (density exactly 1, the extreme allowed), b = 0, and A is one
of: nine unit squares; five positive and four negative unit squares (the level set through 0 is a cone); nine
hyperbolic pairs 2 x_i y_i; a random orthonormal eigenbasis with nine eigenvalues +-1; the same plus a heavy row; a
rank-nine matrix with small entries (no pivot) evaluated in factored form. The statistic is the largest histogram
density of Q times s_9(A); the theorem says it is at most 400. Monte Carlo evidence, not proof.
"""
import json
import math
import sys

import numpy as np


def qvals(X, A=None, U=None, lam=None, dcorr=None):
    if U is not None:
        # exact: x^T (U diag(lam) U^T - diag(dcorr)) x
        Y = X @ U
        return (Y * Y) @ lam - (X * X) @ dcorr
    return np.einsum("ni,ij,nj->n", X, A, X)


def max_density(Q):
    h = max(0.002 * np.std(Q), 1e-3)
    cnt, _ = np.histogram(Q, bins=np.arange(Q.min(), Q.max() + h, h))
    return cnt.max() / (len(Q) * h), h


def main():
    rng = np.random.default_rng(20260924)
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    rows = []
    for trial in range(24):
        kind = trial % 6
        centred = trial % 12 < 6
        U = lam = A = dcorr = None
        if kind == 0:
            n = 9 + trial % 3
            A = np.diag(np.concatenate([np.ones(9), np.zeros(n - 9)]))
        elif kind == 1:
            n = 9 + trial % 3
            A = np.diag(np.concatenate([np.ones(5), -np.ones(4), np.zeros(n - 9)]))
        elif kind == 2:
            n = 18
            A = np.zeros((n, n))
            for i in range(0, 18, 2):
                A[i, i + 1] = A[i + 1, i] = 1.0
        elif kind == 3:
            n = 12
            Qm, _ = np.linalg.qr(rng.normal(size=(n, n)))
            lam9 = np.zeros(n); lam9[:9] = rng.choice([-1.0, 1.0], 9)
            A = (Qm * lam9) @ Qm.T
        elif kind == 4:
            n = 12
            Qm, _ = np.linalg.qr(rng.normal(size=(n, n)))
            lam9 = np.zeros(n); lam9[:9] = rng.choice([-1.0, 1.0], 9)
            A = (Qm * lam9) @ Qm.T
            A[0, 1:] += 3.0; A[1:, 0] += 3.0
        else:
            n = 200
            Ur = rng.choice([-1.0, 1.0], size=(n, 9)) / math.sqrt(n)
            lamr = rng.choice([-1.0, 1.0], 9) * rng.uniform(1.0, 1.6, 9)
            B = (Ur * lamr) @ Ur.T
            dcorr = np.diag(B).copy()
            np.fill_diagonal(B, 0.0)
            U, lam, A = Ur, lamr, None
        ev = np.sort(np.abs(np.linalg.eigvalsh(A if A is not None else B)))[::-1]
        s9 = ev[8]
        chunks = []
        per = max(50_000, 20_000_000 // max(n, 1))
        for start in range(0, N, per):
            m = min(per, N - start)
            X = rng.uniform(-0.5, 0.5, (m, n)) if centred else rng.uniform(0.0, 1.0, (m, n))
            chunks.append(qvals(X, A, U, lam, dcorr))
        Q = np.concatenate(chunks)
        d, h = max_density(Q)
        rows.append({"kind": kind, "n": n, "centred": centred, "s9": float(s9), "max_density": float(d),
                     "bin": float(h), "density_times_s9": float(d * s9)})
        print(rows[-1], flush=True)
    worst = max(r["density_times_s9"] for r in rows)
    out = {"N": N, "rows": rows, "max_density_times_s9": worst, "pass": worst < 400}
    json.dump(out, open("results_t1_tight.json", "w", encoding="utf-8"), indent=1)
    print("max density * s9 = %.4f; bound 400; %s" % (worst, "PASS" if worst < 400 else "FAIL"))


if __name__ == "__main__":
    main()
