"""Second reading of the referee's n = 5 example: the uniform state on {1, x}^perp, pushed to V_[3,2] by A,
does not satisfy the single-transposition inequalities of Proposition 2.1.

x = (1, 1, 0, 0, -2)/sqrt 6, transposition (1 5).  Expected: tr(A A^*) = 2, tr(D rho((1 5))) = -5/18,
left side 2 - (x_1 - x_5)^2 = 1/2, right side (3/4)(1 + tr(D rho)) = 13/24.
Model of V_[n-2,2]: symmetric matrices with zero diagonal and zero row sums; (i j) permutes rows and columns.
"""
from fractions import Fraction
import numpy as np

n = 5
x = np.array([1.0, 1.0, 0.0, 0.0, -2.0]) / np.sqrt(6.0)
Pi = np.eye(n) - 1.0 / n
Q = Pi - np.outer(x, x)
w, U = np.linalg.eigh(Q)
Y = U[:, w > 0.5]
assert Y.shape[1] == n - 2


def proj(T):
    T = T - (n / (n - 2.0)) * Pi @ np.diag(np.diag(T)) @ Pi
    assert abs(np.diag(T)).max() < 1e-12 and abs(T.sum(1)).max() < 1e-12
    return T


mats = [proj((np.outer(x, Y[:, c]) + np.outer(Y[:, c], x)) / np.sqrt(2)) for c in range(Y.shape[1])]
den = sum((T * T).sum() for T in mats)
print("tr(A A^*) = %.12f (expected 2)" % den)
worst = None
for i in range(n):
    for j in range(i + 1, n):
        S = np.eye(n)
        S[[i, j]] = S[[j, i]]
        num = sum((T * (S @ T @ S)).sum() for T in mats)
        t = num / den
        lhs = 2 - (x[i] - x[j]) ** 2
        rhs = 0.75 * (1 + t)
        fr = Fraction(t).limit_denominator(1000)
        print("(%d %d): tr(D rho) = %+.12f ~ %s, lhs %.6f, rhs %.6f, lhs - rhs %+.6f" % (i + 1, j + 1, t, fr, lhs, rhs,
                                                                                       lhs - rhs))
        if worst is None or lhs - rhs < worst[0]:
            worst = (lhs - rhs, i + 1, j + 1)
print("least lhs - rhs: %+.12f at (%d %d); -1/24 = %+.12f" % (worst[0], worst[1], worst[2], -1 / 24))
# weighted sum against w_ij = m - x_i x_j (g = 1, c = m): Lemma 5.4 says the weighted inequality holds
m = max(x[i] * x[j] for i in range(n) for j in range(i + 1, n))
tot = 0.0
for i in range(n):
    for j in range(i + 1, n):
        S = np.eye(n)
        S[[i, j]] = S[[j, i]]
        t = sum((T * (S @ T @ S)).sum() for T in mats) / den
        tot += (m - x[i] * x[j]) * ((2 - (x[i] - x[j]) ** 2) - 0.75 * (1 + t))
print("m = %.6f; weighted sum of (lhs - rhs) with weights m - x_i x_j: %+.12f (>= 0 expected)" % (m, tot))
