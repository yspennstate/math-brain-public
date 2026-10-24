from fractions import Fraction

# Exact finite checks for the explicit T09 application in SL_3(Z).
# The freeness input is proved in the accompanying report via Sanov + Schreier;
# this script checks the concrete matrix bookkeeping and rational inequalities.


def eye(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def matmul(A, B):
    n = len(A)
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def transvection(n, i, j, c):
    A = [list(row) for row in eye(n)]
    A[i][j] += c
    return tuple(tuple(row) for row in A)


def mpow(A, k):
    assert k >= 0
    R = eye(len(A))
    X = A
    while k:
        if k & 1:
            R = matmul(R, X)
        X = matmul(X, X)
        k //= 2
    return R


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def mod2(A):
    return tuple(tuple(x % 2 for x in row) for row in A)


n = 3
m = 11
I = eye(n)
u = transvection(n, 0, 1, 2)
u_inv = transvection(n, 0, 1, -2)
v = transvection(n, 1, 0, 2)
v_inv = transvection(n, 1, 0, -2)

A = []
A_inv = []
for j in range(m):
    A.append(matmul(matmul(mpow(u, j), v), mpow(u_inv, j)))
    A_inv.append(matmul(matmul(mpow(u, j), v_inv), mpow(u_inv, j)))

assert all(det3(a) == 1 for a in A + A_inv)
assert len(set(A + A_inv)) == 2 * m
assert all(mod2(a) == I for a in A + A_inv)

B = []
for i in range(n):
    for j in range(n):
        if i != j:
            B.append(transvection(n, i, j, 1))
            B.append(transvection(n, i, j, -1))

assert len(set(B)) == 12
assert all(det3(b) == 1 for b in B)
assert all(mod2(b) != I for b in B)
assert set(A + A_inv).isdisjoint(B)

q = 2 * m - 1
r = len(B)
D = 2 * m + r
assert (q, r, D) == (21, 12, 34)

# sqrt(21) < 23/5, hence ||A_G|| <= 12 + 2 sqrt(21) < 106/5.
sqrt_q_upper = Fraction(23, 5)
assert Fraction(q, 1) < sqrt_q_upper * sqrt_q_upper
adjacency_norm_upper = Fraction(r, 1) + 2 * sqrt_q_upper
assert adjacency_norm_upper == Fraction(106, 5)

# For the D-regular nonbacktracking recurrence z^2-lambda z+(D-1)=0,
# every root has modulus < t if t > sqrt(D-1) and
# |lambda| < t + (D-1)/t.  We certify this at t=20.
t = 20
root_gate = Fraction(t, 1) + Fraction(D - 1, t)
assert root_gate == Fraction(433, 20)
assert adjacency_norm_upper < root_gate
assert D - 1 < t * t

# The free rank-11 subtree gives p_c <= 1/21, while the operator argument
# gives p_{2->2} > 1/20 and hence p_u > 1/20.
gap = Fraction(1, t) - Fraction(1, q)
assert gap == Fraction(1, 420)

print("m", m, "q", q, "r", r, "D", D)
print("A_pm_size", len(set(A + A_inv)), "B_size", len(set(B)))
print("sqrt21_upper", sqrt_q_upper)
print("adjacency_norm_upper", adjacency_norm_upper)
print("NB_root_gate_t20", root_gate)
print("guard_alpha_lt_gate", adjacency_norm_upper < root_gate)
print("guard_sqrt_Dminus1_lt20", D - 1 < t * t)
print("certified_gap_gt", gap, float(gap))
print("ALL_EXACT_CHECKS_PASS")
