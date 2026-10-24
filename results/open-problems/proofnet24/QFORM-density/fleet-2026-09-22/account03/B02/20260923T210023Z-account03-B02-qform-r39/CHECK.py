import itertools
import numpy as np

SEED = 20260923
C0 = 16.0 / 3125.0


def e2(N):
    s = 0.0
    for P in itertools.combinations(range(N.shape[0]), 2):
        for Q in itertools.combinations(range(N.shape[1]), 2):
            s += np.linalg.det(N[np.ix_(P, Q)]) ** 2
    return s


def v1(A):
    n = A.shape[0]
    triples = list(itertools.combinations(range(n), 3))
    out = 0.0
    for I in triples:
        SI = set(I)
        for J in triples:
            if len(SI.intersection(J)) == 1:
                out += np.linalg.det(A[np.ix_(I, J)]) ** 2
    return out


def packet(A, colors):
    H = [i for i, x in enumerate(colors) if x == 0]
    L = [i for i, x in enumerate(colors) if x == 1]
    R = [i for i, x in enumerate(colors) if x == 2]
    N = A[np.ix_(L, R)]
    E = e2(N)
    W = A0 = T0 = 0.0
    for h in H:
        a = A[h, h]
        c = A[L, h]
        r = A[h, R]
        D = 0.0
        for P in itertools.combinations(range(len(L)), 2):
            for Q in itertools.combinations(range(len(R)), 2):
                rows = [h, L[P[0]], L[P[1]]]
                cols = [h, R[Q[0]], R[Q[1]]]
                D += np.linalg.det(A[np.ix_(rows, cols)]) ** 2
        Pc = np.eye(len(L)) if np.dot(c, c) == 0 else np.eye(len(L)) - np.outer(c, c) / np.dot(c, c)
        Pr = np.eye(len(R)) if np.dot(r, r) == 0 else np.eye(len(R)) - np.outer(r, r) / np.dot(r, r)
        C = Pc @ N @ Pr
        T = np.dot(c, c) * np.dot(r, r) * np.linalg.norm(C, "fro") ** 2
        if np.sqrt(max(D, 0.0)) > abs(a) * np.sqrt(E) + np.sqrt(max(T, 0.0)) + 1e-9:
            raise AssertionError("local shared-hub Minkowski identity failed")
        W += D
        A0 += a * a * E
        T0 += T
    return W, A0, T0


rng = np.random.default_rng(SEED)
max_expectation_relerr = 0.0
min_best_ratio = float("inf")
violations = 0
trials = 0

for n, reps in [(5, 8), (6, 8), (7, 4)]:
    for _ in range(reps):
        X = rng.normal(size=(n, n))
        A = (X + X.T) / 2.0
        V = v1(A)
        EW = 0.0
        best = (-1.0, None)
        for colors in itertools.product(range(3), repeat=n):
            W, A0, T0 = packet(A, colors)
            nh = sum(x == 0 for x in colors)
            nl = sum(x == 1 for x in colors)
            nr = n - nh - nl
            prob = (1.0 / 5.0) ** nh * (2.0 / 5.0) ** (nl + nr)
            EW += prob * W
            if W > best[0]:
                best = (W, (A0, T0))
        if V > 1e-14:
            target = C0 * V
            max_expectation_relerr = max(max_expectation_relerr, abs(EW - target) / target)
            min_best_ratio = min(min_best_ratio, best[0] / V)
        W, (A0, T0) = best
        if max(A0, T0) + 1e-9 < W / 4.0:
            violations += 1
        trials += 1

print("seed", SEED)
print("trials", trials)
print("violations", violations)
print("max_expectation_relative_error", max_expectation_relerr)
print("min_maxcolor_W_over_V1", min_best_ratio)
print("rigorous_expectation_floor", C0)
