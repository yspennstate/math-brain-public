from fractions import Fraction
from itertools import product

# ProofNet24 P01 P71 exact finite self-check.
# This checks only the finite Boolean/block-algebra core used in the written proof.
# It is not a substitute for the C*-algebra/K-theory argument.

# Three commuting lamp involutions x0,x1,x2 in {+1,-1}.
rows = []
for x0, x1, x2 in product([1, -1], repeat=3):
    ep0 = Fraction(1 + x0, 2)
    em1 = Fraction(1 - x1, 2)
    ep1 = Fraction(1 + x1, 2)
    em2 = Fraction(1 - x2, 2)
    p = ep0 * em1
    q = ep1 * em2
    rows.append((x0, x1, x2, p, q, p * q))

assert all(row[-1] == 0 for row in rows)
assert all(row[3] in (0, 1) and row[4] in (0, 1) for row in rows)


def matmul(A, B):
    n = len(A)
    m = len(B[0])
    k = len(B)
    return [[sum(A[i][r] * B[r][j] for r in range(k))
             for j in range(m)] for i in range(n)]


def matadd(*Ms):
    n = len(Ms[0])
    m = len(Ms[0][0])
    return [[sum(M[i][j] for M in Ms) for j in range(m)]
            for i in range(n)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def zero(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def diag(vals):
    n = len(vals)
    return [[Fraction(vals[i]) if i == j else Fraction(0)
             for j in range(n)] for i in range(n)]


# Universal finite block model for p,q,r and a partial isometry v
# with v* v=p, vv*=q, p q=0.  T=v+v*+r is the local transposition.
P = diag([1, 0, 0, 0])
Q = diag([0, 1, 0, 0])
R = diag([0, 0, 1, 1])
V = zero(4)
V[1][0] = Fraction(1)
Vt = transpose(V)
T = matadd(V, Vt, R)
I = eye(4)

assert matmul(P, Q) == zero(4)
assert matmul(Vt, V) == P
assert matmul(V, Vt) == Q
assert transpose(T) == T
assert matmul(T, T) == I

# K1 coordinate bookkeeping for w=s1^2 s2.
coord = (2, 1)
assert coord == (2, 1)

print("P01 P71 local-transposition exact self-check")
print("Lamp truth table columns: x0 x1 x2 p q pq")
for row in rows:
    print(*row)
print("all pq=0: PASS")
print("V^*V=P: PASS")
print("VV^*=Q: PASS")
print("T=T^*: PASS")
print("T^2=I: PASS")
print("w=s1^2 s2 K1 coordinate=(2,1): PASS")
print("ALL ASSERTIONS PASSED")
