from fractions import Fraction as F


def matmul(A, B):
    return [
        [sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
         for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def matadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def scalar(c, A):
    return [[c * x for x in row] for row in A]


def max_row_sum(A):
    return max(sum(abs(x) for x in row) for row in A)


I = [[F(1), F(0)], [F(0), F(1)]]
M = F(100)

# Large one-way coupling, but a small round trip.
K_good = [[F(0), M], [F(1, 400), F(0)]]
K_good_2 = matmul(K_good, K_good)
prod_good = matmul(matsub(I, K_good), matadd(I, K_good))
inv_good = scalar(F(4, 3), matadd(I, K_good))
check_inv_good = matmul(matsub(I, K_good), inv_good)

# Large round trip as well.  The power-contraction criterion fails,
# but I-K is still invertible.  This stress-tests necessity claims.
K_bad = [[F(0), M], [F(1, 25), F(0)]]
K_bad_2 = matmul(K_bad, K_bad)
prod_bad = matmul(matsub(I, K_bad), matadd(I, K_bad))
inv_bad = scalar(F(-1, 3), matadd(I, K_bad))
check_inv_bad = matmul(matsub(I, K_bad), inv_bad)

print("P15 exact feedback sanity check")
print("good K =", K_good)
print("good ||K||_infty =", max_row_sum(K_good))
print("good K^2 =", K_good_2)
print("good ||K^2||_infty =", max_row_sum(K_good_2))
print("(I-K)(I+K) =", prod_good)
print("(I-K)^-1 = 4/3(I+K) check =", check_inv_good)
print("bad K =", K_bad)
print("bad ||K||_infty =", max_row_sum(K_bad))
print("bad K^2 =", K_bad_2)
print("bad spectral radius = 2 (since K^2=4I)")
print("(I-K)(I+K) =", prod_bad)
print("(I-K)^-1 = -1/3(I+K) check =", check_inv_bad)

assert K_good_2 == scalar(F(1, 4), I)
assert prod_good == scalar(F(3, 4), I)
assert check_inv_good == I
assert K_bad_2 == scalar(F(4), I)
assert prod_bad == scalar(F(-3), I)
assert check_inv_bad == I

print("ALL_EXACT_CHECKS_PASSED")
