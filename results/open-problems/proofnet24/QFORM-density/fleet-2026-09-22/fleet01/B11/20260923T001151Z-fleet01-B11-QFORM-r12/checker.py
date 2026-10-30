import itertools
import math
import numpy as np

N = 7
M = np.diag([1.0, 1.0, -2.0])
theta = np.arange(N) * 2.0 * math.pi / N
R = np.sqrt(2.0 / N) * np.column_stack(
    [np.cos(theta), np.sin(theta), np.ones(N) / math.sqrt(2.0)]
)
A = R @ M @ R.T

assert np.linalg.norm(R.T @ R - np.eye(3), ord=np.inf) < 1e-12
assert np.max(np.abs(np.diag(A))) < 1e-12
s = min(abs(np.linalg.eigvalsh(M)))

max_errors = []
for i in range(N):
    r = R[i]
    c = float(r @ r)
    keep = np.arange(N) != i
    Rm = R[keep]
    G = np.eye(3) - np.outer(r, r)
    B = Rm @ M @ Rm.T
    a = Rm @ M @ r
    v = Rm @ np.linalg.solve(G, r)

    errors = [
        np.linalg.norm(B @ v - a),
        abs(v @ B @ v),
        abs(v @ v - c / (1.0 - c)),
        abs(a @ a - r @ M @ M @ r),
        abs(a @ B @ a - np.linalg.det(M) * c),
    ]
    max_errors.append(max(errors))

    u = a / np.linalg.norm(a)
    q = float(u @ B @ u)
    assert abs(q) >= s / 2.0 - 1e-10

    best = 0.0
    m = N - 1
    for bits in itertools.product([0, 1], repeat=m):
        S = [j for j, bit in enumerate(bits) if bit]
        T = [j for j, bit in enumerate(bits) if not bit]
        if not S or not T:
            continue
        value = abs(u[S] @ B[np.ix_(S, T)] @ u[T])
        best = max(best, value)
    assert best >= abs(q) / 4.0 - 1e-10

triangle_error = 0.0
for i, j, k in itertools.combinations(range(N), 3):
    lhs = 2.0 * A[i, j] * A[i, k] * A[j, k]
    w = np.linalg.det(R[[i, j, k], :]) ** 2
    rhs = np.linalg.det(M) * w
    triangle_error = max(triangle_error, abs(lhs - rhs))

print("N", N)
print("frame_error", np.linalg.norm(R.T @ R - np.eye(3), ord=np.inf))
print("diag_error", np.max(np.abs(np.diag(A))))
print("max_identity_error", max(max_errors))
print("max_triangle_error", triangle_error)
print("QFORM_NULL_RULING_MATCHED_CURVATURE_CHECK_PASS")
