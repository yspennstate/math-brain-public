from fractions import Fraction as F


def record_span(A, p, c):
    m = len(p)
    assert len(A) == m + 1
    x = [F(1)]
    for pj in p:
        x.append(x[-1] - pj)
    y = [Aj - c for Aj in A]
    assert all(x[j] > 0 for j in range(len(x)))
    ratios = [y[j] / x[j] for j in range(len(x))]
    assert all(ratios[j] <= ratios[j+1] for j in range(m))
    assert all(y[j] >= y[j+1] for j in range(m))

    P = sum(p, F(0))
    sigma = sum(p[j] / (A[j] * A[j+1]) for j in range(m))
    K = 2 * P / (A[0] * A[-1]) - sigma

    r0 = ratios[0]
    xi = y[-1] / r0
    assert x[-1] <= xi <= x[0]
    L = x[0] - xi
    R = xi - x[-1]
    refined = L / (A[0] * A[-1]) + R / (A[-1] * A[-1])
    margin = (
        R / (A[0] * A[-1])
        + L * (c + r0 * x[-1]) / (A[0] * A[-1] * A[-1])
    )
    assert sigma <= refined
    assert K >= margin > 0
    return x, y, ratios, sigma, K, xi, refined, margin


def waiting_identity(A, p, V):
    m = len(p)
    P = sum(p, F(0))
    lhs = 2 * P * V[-1] / (A[0] * A[-1]) - sum(
        p[j] * V[j] / (A[j] * A[j+1]) for j in range(m)
    )
    sigma = sum(p[j] / (A[j] * A[j+1]) for j in range(m))
    K = 2 * P / (A[0] * A[-1]) - sigma
    rhs = K * V[-1] + sum(
        p[j] * (V[-1] - V[j]) / (A[j] * A[j+1])
        for j in range(m-1)
    )
    assert lhs == rhs
    assert rhs > 0
    return lhs, rhs, K


def scalar_collapse(A, p, c, q):
    m = len(p)
    a = A[-1]
    rho = 1 - c
    P = sum(p, F(0))
    r = 1 - P
    assert r > 0
    w = [1 / A[j] for j in range(m)]
    wbar = sum(p[j] * w[j] for j in range(m)) / P
    var = sum(p[j] * (w[j] - wbar) ** 2 for j in range(m))
    sigma = sum(p[j] / (A[j] * A[j+1]) for j in range(m))
    K = 2 * P / (A[0] * a) - sigma
    C = K + r / (a * c)
    assert K > 0 and C > 0

    y = 1 - a
    u = sum(q, F(0))
    assert 0 <= u <= y <= rho
    sumq2 = sum(q[j] * q[j] / p[j] for j in range(m))

    B = 2 * rho - rho / a + u / a - sum(w[j] * q[j] for j in range(m))
    B += K * F(1, 2) * (sumq2 + (y - u) ** 2 / r)
    B += r * F(1, 2) / (a * c) * (sumq2 + (rho - u) ** 2 / r)

    Bstar = (
        2 * rho - rho / a
        + u * (1 / a - wbar)
        - var / (2 * C)
        + C * u * u / (2 * P)
        + K * (y - u) ** 2 / (2 * r)
        + (rho - u) ** 2 / (2 * a * c)
    )

    qstar = [
        p[j] * (u / P + (w[j] - wbar) / C)
        for j in range(m)
    ]
    residual = C * F(1, 2) * sum(
        (q[j] - qstar[j]) ** 2 / p[j] for j in range(m)
    )
    assert B - Bstar == residual
    assert residual >= 0
    return wbar, var, K, C, u, B, Bstar, residual


# Rational record chain 1.
A1 = [F(1), F(9, 10), F(7, 10), F(2, 5)]
p1 = [F(1, 5), F(3, 10), F(3, 10)]
c1 = F(1, 5)
out1 = record_span(A1, p1, c1)
print("CASE1_X", out1[0])
print("CASE1_RATIOS", out1[2])
print("CASE1_SIGMA", out1[3])
print("CASE1_K", out1[4])
print("CASE1_XI", out1[5])
print("CASE1_REFINED", out1[6])
print("CASE1_MARGIN", out1[7])

# Rational record chain 2, with strictly increasing record ratios.
A2 = [F(1), F(191, 200), F(41, 50), F(19, 40)]
p2 = [F(1, 10), F(3, 10), F(7, 20)]
c2 = F(1, 10)
out2 = record_span(A2, p2, c2)
print("CASE2_X", out2[0])
print("CASE2_RATIOS", out2[2])
print("CASE2_K", out2[4])
print("CASE2_MARGIN", out2[7])

# Exact factor-two waiting-reserve decomposition.
wait = waiting_identity(A1, p1, [F(1), F(3), F(7)])
print("WAIT_LHS", wait[0])
print("WAIT_RHS", wait[1])
print("WAIT_K", wait[2])

# Exact arbitrary-prefix square completion.  q_j are scaled block first moments.
sc = scalar_collapse(
    A1, p1, c1,
    [F(1, 20), F(3, 20), F(1, 5)],
)
print("SCALAR_WBAR", sc[0])
print("SCALAR_VAR", sc[1])
print("SCALAR_K", sc[2])
print("SCALAR_C", sc[3])
print("SCALAR_U", sc[4])
print("SCALAR_B", sc[5])
print("SCALAR_BSTAR", sc[6])
print("SCALAR_RESIDUAL", sc[7])

print("ALL_EXACT_CHECKS_PASS")
