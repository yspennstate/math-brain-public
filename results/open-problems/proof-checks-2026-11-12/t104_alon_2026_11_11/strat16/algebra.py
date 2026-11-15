"""Exact selected-projector functional for a tied edge and an m-vertex part."""
import sympy as s


def laplacian(edges, n=5):
    L = s.zeros(n)
    for i, j, w in edges:
        L[i, i] += w
        L[j, j] += w
        L[i, j] -= w
        L[j, i] -= w
    return L


def components(L, U, k):
    n = L.rows
    R = U.dot(U)
    P = U * U.T / R
    A = s.eye(n) - L
    mass = (s.trace(L) + 1) / 2
    h = sum(P[i, i] * L[i, i] for i in range(n)) + s.Rational(1, 2)
    B = sum(P[i, j] * A[i, j]**2 for i in range(n) for j in range(n))
    Y = -2 * sum(L[i, j] * (P[i, i] + P[j, j] - 2 * P[i, j]) *
                 (2 - L[i, i] - L[j, j] + 2 * L[i, j])
                 for i in range(n) for j in range(i + 1, n))
    X1 = 2 * (s.trace(L) - s.trace(L * L))
    X2 = 2 * (k + 2) * B / k
    X3 = (mass - 1) / k**2 * (2 * (k + 1) * (k - 2) - 4 * k * mass + 2 * (k + 2) * h)
    return X1, X2, X3, Y


def functional(L, U, k):
    a, b, c, d = components(L, U, k)
    return a + b + c - d


def quadratic(E, U, k):
    n = E.rows
    P = U * U.T / U.dot(U)
    p = P.diagonal().T
    d = E.diagonal().T
    m = s.trace(E) / 2
    B = sum(P[i, j] * E[i, j]**2 for i in range(n) for j in range(n))
    return (-2 * s.trace(E * E) + (2 * (k + 2) / k - 4) * B
            + 4 * sum(P[i, i] * (E * E)[i, i] for i in range(n))
            - 2 * (p.T * E * d)[0]
            + m / k**2 * (-4 * k * m + 2 * (k + 2) * p.dot(d)))


def spanning(U):
    n = len(U)
    K = s.zeros(n, n - 2)
    for c, j in enumerate(range(1, n - 1)):
        K[0, c] = U[-1] - U[j]
        K[j, c] = U[0] - U[-1]
        K[-1, c] = U[j] - U[0]
    return K
