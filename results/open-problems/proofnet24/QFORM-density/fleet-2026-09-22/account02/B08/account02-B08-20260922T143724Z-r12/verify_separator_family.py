from fractions import Fraction
from math import e


def sylvester(n):
    H = [[1]]
    while len(H) < n:
        top = [row + row for row in H]
        bot = [row + [-x for x in row] for row in H]
        H = top + bot
    return H


def transpose(A):
    return [list(x) for x in zip(*A)]


def mm(A, B):
    BT = transpose(B)
    return [[sum(a*b for a, b in zip(row, col)) for col in BT] for row in A]


def msub(A, B):
    return [[a-b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def eye(n):
    return [[Fraction(int(i == j), 1) for j in range(n)] for i in range(n)]


def inv(A):
    n = len(A)
    aug = [
        [Fraction(A[i][j]) for j in range(n)]
        + [Fraction(int(i == j), 1) for j in range(n)]
        for i in range(n)
    ]
    for c in range(n):
        p = next(i for i in range(c, n) if aug[i][c])
        aug[c], aug[p] = aug[p], aug[c]
        v = aug[c][c]
        aug[c] = [x / v for x in aug[c]]
        for i in range(n):
            if i != c and aug[i][c]:
                q = aug[i][c]
                aug[i] = [x - q*y for x, y in zip(aug[i], aug[c])]
    return [row[n:] for row in aug]


def det(A):
    A = [[Fraction(x) for x in row] for row in A]
    n = len(A)
    s = Fraction(1)
    for c in range(n):
        p = next((i for i in range(c, n) if A[i][c]), None)
        if p is None:
            return Fraction(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            s = -s
        v = A[c][c]
        s *= v
        for j in range(c, n):
            A[c][j] /= v
        for i in range(c + 1, n):
            q = A[i][c]
            for j in range(c, n):
                A[i][j] -= q*A[c][j]
    return s


n = 16
H16 = sylvester(n)
U = [[Fraction(H16[i][j], 4) for j in range(3)] for i in range(n)]
Hidx = [0, 1, 2]
Tidx = [i for i in range(n) if i not in Hidx]
UH = [U[i] for i in Hidx]
UT = [U[i] for i in Tidx]
K = mm(UT, inv(UH))
KT = transpose(K)
I13 = eye(len(Tidx))

# Residual C in H,T ordering: C=[K^T K,-K^T;-K,I].
C_HH = mm(KT, K)
C_HT = [[-x for x in row] for row in KT]
C_TH = [[-x for x in row] for row in K]
C = [C_HH[i] + C_HT[i] for i in range(3)] + [C_TH[i] + I13[i] for i in range(len(Tidx))]
Uord = UH + UT
assert all(x == 0 for row in mm(C, Uord) for x in row)

# Exact PSD factorization C=F^T F and hence kernel contains span(U).
F = [[-x for x in row] + I13[i] for i, row in enumerate(K)]
assert mm(transpose(F), F) == C

G = mm(transpose(UH), UH)
I3 = eye(3)
Gm1 = msub(G, [[Fraction(1, 16)*x for x in row] for row in I3])
Gm4 = msub(G, [[Fraction(1, 4)*x for x in row] for row in I3])
assert all(x == 0 for row in mm(Gm1, Gm4) for x in row)
assert sum(G[i][i] for i in range(3)) == Fraction(9, 16)

MT = msub(I3, G)
assert det(MT) == Fraction(135, 256)
raw_leverage = max(sum(x*x for x in row) for row in U)
assert raw_leverage == Fraction(3, 16)
assert raw_leverage / (1 - Fraction(1, 4)) == Fraction(1, 4)

# Off-diagonal graph of C is connected.
N = len(C)
adj = [set() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j and C[i][j] != 0:
            adj[i].add(j)
seen = {0}
stack = [0]
while stack:
    i = stack.pop()
    for j in adj[i]:
        if j not in seen:
            seen.add(j)
            stack.append(j)
assert len(seen) == N

bound = 3*e*float(Fraction(256, 135))**(1/3)

print("QFORM_B08_SEPARATOR_CHECK_PASS")
print("UH_gram=", G)
print("UH_gram_spectrum={1/16,1/4,1/4}")
print("det_MT=135/256")
print("raw_selected_leverage=3/16")
print("coarse_whitened_leverage<=1/4")
print("residual_CU_zero=True")
print("residual_C_psd_factorization=True")
print("residual_offdiag_graph_connected=True")
print("residual_TT_identity=True")
print("whitened_diagonal_bound=3e*(256/135)^(1/3)=%.15f" % bound)
print("partner_separator_bound=32*(2+sqrt(3))")
