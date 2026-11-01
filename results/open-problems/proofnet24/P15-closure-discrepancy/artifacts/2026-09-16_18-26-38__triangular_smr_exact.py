from itertools import product

# Exact integer sanity check for the nilpotent-flag / triangular-noise family.
# This is a finite self-check supporting the theorem in the corresponding
# P15 run report; the theorem itself is proved on the page.

def matmul(A, B):
    n = len(A)
    m = len(B[0])
    k = len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def smul(c, A):
    return [[c * x for x in row] for row in A]


def iszero(A):
    return all(x == 0 for row in A for x in row)


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


B1 = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]  # E_12
B2 = [[0, 0, 0], [0, 0, 1], [0, 0, 0]]  # E_23
E13 = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]

commutator = matsub(matmul(B1, B2), matmul(B2, B1))
assert commutator == E13
assert not iszero(commutator)

# Every word of length three in the generators vanishes: the generated
# strictly-upper-triangular algebra is nilpotent of step at most three.
for word in product([B1, B2], repeat=3):
    assert iszero(matmul(matmul(word[0], word[1]), word[2]))

# A concrete noncompactness witness for the associated shear mechanism.
# The report proves (I+B1)^k = I+kB1 for all k by B1^2=0; here we verify
# the first seven exact integer instances.
I = eye(3)
T = matadd(I, B1)
P = I
for k in range(1, 8):
    P = matmul(P, T)
    assert P == matadd(I, smul(k, B1))

print("EXACT_TRIANGULAR_FAMILY_CHECK")
print("B1=E12, B2=E23")
print("commutator=[B1,B2]=E13 != 0")
print("all generator words of length 3 vanish")
print("(I+B1)^k = I + k B1 verified for k=1..7; written proof holds for all k")
print("consequence: the shear subgroup is unbounded/noncompact, so this example is not a compact-isometric-flow instance")
print("ALL_EXACT_CHECKS_PASSED")
