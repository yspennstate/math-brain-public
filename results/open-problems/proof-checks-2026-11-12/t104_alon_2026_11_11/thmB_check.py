"""Direct check of the operator form of the two-eigenvalue theorem, in the matrix model of V_[n-2,2].

For a unit sum-zero x put X = sum_{i<j} x_i x_j rho((i j)) on V_[n-2,2] and m = max_{i<j} x_i x_j.
Claim B:  lambda_max(X) >= 1/2 - 2 (n-1) m   for n >= 5, equality at the edge and star vectors.
Claim R:  the trace Rayleigh quotient R(x) = tr(X A A^*)/tr(A A^*), A y = P (x y^t + y x^t)/sqrt 2 on {1, x}^perp,
          satisfies (R - 1/2 + 2 (n-1) m) Z = c_n Psi(x) with a constant c_n; the script prints the ratio.
The model: symmetric n x n matrices with zero diagonal and zero row sums; (i j) permutes rows and columns.
"""
import sys
import itertools
import numpy as np

rng = np.random.default_rng(5)


def model_basis(n):
    pairs = list(itertools.combinations(range(n), 2))
    idx = {p: k for k, p in enumerate(pairs)}
    R = np.zeros((n, len(pairs)))
    for (a, b), k in idx.items():
        R[a, k] = 1.0
        R[b, k] = 1.0
    _, s, vt = np.linalg.svd(R)
    B = vt[n:].T                      # orthonormal basis of the kernel of the row-sum map, in pair coordinates
    assert B.shape[1] == n * (n - 3) // 2
    return pairs, idx, B


def transposition(n, pairs, idx, i, j):
    Pm = np.zeros((len(pairs), len(pairs)))
    for (a, b), k in idx.items():
        a2 = j if a == i else i if a == j else a
        b2 = j if b == i else i if b == j else b
        Pm[idx[(min(a2, b2), max(a2, b2))], k] = 1.0
    return Pm


def run(n, trials):
    pairs, idx, B = model_basis(n)
    reps = {p: B.T @ transposition(n, pairs, idx, *p) @ B for p in pairs}
    allsum = sum(reps.values())
    assert np.allclose(allsum, (n - 1) * (n - 4) / 2 * np.eye(B.shape[1]))
    Pi = np.eye(n) - 1.0 / n
    worstB, ratios, worstR = 1e9, [], 1e9
    vecs = []
    e = np.zeros(n); e[0], e[1] = 1, -1
    s = -np.ones(n); s[0] = n - 1
    vecs += [e, s]
    for t in range(trials):
        k = t % 4
        if k == 0:
            v = rng.standard_normal(n)
        elif k == 1:
            v = s + 0.3 * rng.standard_normal(n) * rng.random()
        elif k == 2:
            v = e + 0.3 * rng.standard_normal(n) * rng.random()
        else:
            v = rng.choice([-2.0, -1.0, 0.0, 1.0, 3.0], size=n) + 0.01 * rng.standard_normal(n)
        vecs.append(v)
    for v in vecs:
        x = Pi @ v
        x /= np.linalg.norm(x)
        m = max(x[i] * x[j] for i, j in pairs)
        X = sum(x[i] * x[j] * reps[(i, j)] for i, j in pairs)
        top = np.linalg.eigvalsh(X)[-1]
        rhs = 0.5 - 2 * (n - 1) * m
        worstB = min(worstB, top - rhs)
        # uniform state on {1, x}^perp
        Q = Pi - np.outer(x, x)
        w, U = np.linalg.eigh(Q)
        Y = U[:, w > 0.5]
        num = den = 0.0
        for c in range(Y.shape[1]):
            y = Y[:, c]
            T = (np.outer(x, y) + np.outer(y, x)) / np.sqrt(2)
            T = T - (n / (n - 2.0)) * Pi @ np.diag(np.diag(T)) @ Pi
            assert abs(np.diag(T)).max() < 1e-12 and abs(T.sum(1)).max() < 1e-12
            tv = B.T @ np.array([T[a, b] for a, b in pairs])
            num += tv @ X @ tv
            den += tv @ tv
        Z = 2 * den / (n - 2)              # tr(A C A^*) for C = Q/(n-2), Frobenius norm (twice the sum over a<b)
        q = (x ** 4).sum()
        p3 = (x ** 3).sum()
        Psi = (n - 4) * (2 * q - 1) - 2 * (n - 3) * p3 ** 2 + (n - 1) * (n * n - 6 * n + 6 + 2 * n * q) * m
        Rq = num / den
        worstR = min(worstR, Rq - rhs)
        assert top >= Rq - 1e-10
        if Psi > 1e-6:
            ratios.append((Rq - rhs) * Z / Psi)
        Zf = 1 - 2 * (n - 1 - n * q) / (n - 2) ** 2
        assert abs(Z - Zf) < 1e-10, (Z, Zf)
    ratios = np.array(ratios)
    print("n=%d vectors %d: min(lambda_max - rhs) %.3e, min(R - rhs) %.3e, (R-rhs) Z / Psi in [%.12f, %.12f], "
          "1/((n-1)(n-2)^2)... candidates: %.12f %.12f" % (n, len(vecs), worstB, worstR, ratios.min(), ratios.max(),
                                                      1.0 / ((n - 2) ** 2), 1.0 / ((n - 1) * (n - 2))))
    sys.stdout.flush()


for n, tr in ((5, 2000), (6, 1500), (7, 1000), (8, 500), (4, 500)):
    run(n, tr)
