# Exact self-check for P24/AV-P3-SPECTRAL-SHELL-63
# Pure integer arithmetic; no external dependencies.


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def mat_vec(A, v):
    return [sum(A[i][j] * v[j] for j in range(2)) for i in range(2)]


I = [[1, 0], [0, 1]]
# K_theta = R_theta diag(1,-1) R_theta^{-1} at theta=0,pi/4,pi/2,3pi/4.
Ks = [
    [[1, 0], [0, -1]],
    [[0, 1], [1, 0]],
    [[-1, 0], [0, 1]],
    [[0, -1], [-1, 0]],
]

S = [[0, 0], [0, 0]]
for K in Ks:
    S = mat_add(S, K)
    assert mat_mul(transpose(K), K) == I
    assert mat_mul(K, K) == I
assert S == [[0, 0], [0, 0]]

K0 = Ks[0]
IpK = mat_add(I, K0)
e1 = [1, 0]
assert mat_vec(IpK, e1) == [2, 0]

# For dZ=-Z ds+c Z dW, the p=2 moment exponent is -2+c^2.
conjugate_exponent = -2 + 2**2
average_exponent = -2 + 1**2
assert conjugate_exponent == 2
assert average_exponent == -1

print("four_conjugate_sum =", S)
print("each_KT_K_equals_I = PASS")
print("(I+K0)e1 =", mat_vec(IpK, e1))
print("p2_exponent_conjugate =", conjugate_exponent)
print("p2_exponent_average =", average_exponent)
print("ALL_EXACT_CHECKS_PASS")
