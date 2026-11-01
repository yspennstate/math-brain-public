from fractions import Fraction
from itertools import combinations

# Exact coloring probabilities for overlap q=0,1,2,3.
p0 = Fraction(36, 6**6)
p1 = Fraction(1, 5) * Fraction(2, 25) * Fraction(2, 25)
p2 = Fraction(2, 16) * Fraction(1, 4) * Fraction(1, 4)
p3 = Fraction(6, 27)
assert (p0, p1, p2, p3) == (Fraction(1,1296), Fraction(4,3125), Fraction(1,128), Fraction(2,9))
assert tuple(p/Fraction(4,1) for p in (p0,p1,p2,p3)) == (
    Fraction(1,5184), Fraction(1,3125), Fraction(1,512), Fraction(1,18)
)

A = [
    [3,1,2,0,1],
    [1,2,1,1,0],
    [2,1,4,2,1],
    [0,1,2,3,1],
    [1,0,1,1,2],
]
n = len(A)

def submat(rows, cols):
    return [[Fraction(A[i][j]) for j in cols] for i in rows]

def det(M):
    M = [row[:] for row in M]
    m = len(M)
    ans = Fraction(1)
    for i in range(m):
        p = next((j for j in range(i,m) if M[j][i]), None)
        if p is None:
            return Fraction(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            ans = -ans
        piv = M[i][i]
        ans *= piv
        for j in range(i+1,m):
            c = M[j][i] / piv
            for k in range(i+1,m):
                M[j][k] -= c*M[i][k]
    return ans

def inv2(B):
    d = det(B)
    assert d
    return [[B[1][1]/d, -B[0][1]/d],[-B[1][0]/d, B[0][0]/d]]

# Verify W_H = det(A_HH)^2 ||S_H||_F^2 for every physical pair H.
sumW = Fraction(0)
for Ht in combinations(range(n), 2):
    H = list(Ht)
    rest = [i for i in range(n) if i not in H]
    B = submat(H,H)
    dB = det(B)
    assert dB != 0
    E = submat(rest,H)
    C = submat(rest,rest)
    Bi = inv2(B)
    S = [[C[i][j] for j in range(len(rest))] for i in range(len(rest))]
    for i in range(len(rest)):
        for j in range(len(rest)):
            S[i][j] -= sum(E[i][u]*Bi[u][v]*E[j][v] for u in range(2) for v in range(2))
    W = sum(det(submat(H+[r], H+[c]))**2 for r in rest for c in rest)
    rhs = dB*dB*sum(x*x for row in S for x in row)
    assert W == rhs
    sumW += W

# Verify global pair-overlap counting: sum_H W_H = E_2 + 3 E_3.
E = {q: Fraction(0) for q in range(4)}
triples = list(combinations(range(n),3))
for I in triples:
    for J in triples:
        E[len(set(I)&set(J))] += det(submat(I,J))**2
assert sumW == E[2] + 3*E[3]
assert E == {0: Fraction(0), 1: Fraction(200), 2: Fraction(1880), 3: Fraction(1380)}
assert sumW == Fraction(6020)

print('COLOR_PROBS', p0, p1, p2, p3)
print('DOMINANT_PACKET_LOWER_BOUNDS', p0/4, p1/4, p2/4, p3/4)
print('E_OVERLAP', E)
print('PAIR_LEDGER', sumW)
print('STATUS=PASS')
