from fractions import Fraction as F

# Exact rational 4x2 orthonormal frame: first two normalized Hadamard columns.
R = [
    [F(1,2), F(1,2)],
    [F(1,2), F(1,2)],
    [F(1,2), F(-1,2)],
    [F(1,2), F(-1,2)],
]
S = [0,2]
T = [1,3]
lam = [F(2), F(3)]

def transpose(A):
    return [list(x) for x in zip(*A)]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

RS = [R[i] for i in S]
RT = [R[i] for i in T]
L = [[lam[0], F(0)], [F(0), lam[1]]]
M = matmul(matmul(RS,L),transpose(RT))

# Cauchy-Binet/Pluecker masses for this 2+2 split.
W_S = det2(RS)**2
W_T = det2(RT)**2

# Since M is 2x2 here, product of its singular values is |det M|.
lhs = abs(det2(M))
# W_S=W_T=1/4, so sqrt(W_S W_T)=1/4 exactly.
assert W_S == F(1,4)
assert W_T == F(1,4)
rhs = abs(lam[0]*lam[1]) * F(1,4)
assert lhs == rhs == F(3,2)

# Verify R^T R = I_2.
RTR = matmul(transpose(R), R)
assert RTR == [[F(1),F(0)],[F(0),F(1)]]

print({
    "status": "PASS",
    "M": [[str(x) for x in row] for row in M],
    "W_S": str(W_S),
    "W_T": str(W_T),
    "singular_product_via_det": str(lhs),
    "pluecker_formula_rhs": str(rhs),
})
