from fractions import Fraction
from itertools import permutations

def det2(B):
    return B[0][0]*B[1][1]-B[0][1]*B[1][0]

def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def givens6(i, j, c, s):
    G = eye(6)
    G[i][i] = c
    G[j][j] = c
    G[i][j] = -s
    G[j][i] = s
    return G

def block_row_energy(O, alpha):
    E = Fraction(0)
    triples = []
    for beta in range(3):
        B = [[Fraction(O[2*alpha+i][2*beta+j]) for j in range(2)]
             for i in range(2)]
        R = sum(x*x for row in B for x in row) / 2
        D = det2(B)
        e = R*R - D*D
        triples.append((R, D, e))
        E += e
    return E, triples

# Sharp SO(6) signed-permutation witness.
perm = [0, 2, 1, 3, 4, 5]       # odd scalar permutation
sign = [-1, 1, 1, 1, 1, 1]      # extra sign makes determinant +1
O = [[0]*6 for _ in range(6)]
for i, j in enumerate(perm):
    O[i][j] = sign[i]
sharp = [block_row_energy(O, a)[0] for a in range(3)]
assert sharp == [Fraction(1,2), Fraction(1,2), Fraction(0)]

# Exhaust all 720 scalar permutation matrices: exact sanity/sharpness check.
mx = Fraction(0)
eq_rows = 0
for p in permutations(range(6)):
    P = [[0]*6 for _ in range(6)]
    for i, j in enumerate(p):
        P[i][j] = 1
    for alpha in range(3):
        E, _ = block_row_energy(P, alpha)
        assert E <= Fraction(1,2)
        mx = max(mx, E)
        eq_rows += int(E == Fraction(1,2))
assert mx == Fraction(1,2)

# Dense rational SO(6) sanity check from exact Givens rotations.
rots = [
    (0,1,Fraction(3,5),Fraction(4,5)),
    (1,2,Fraction(5,13),Fraction(12,13)),
    (2,3,Fraction(8,17),Fraction(15,17)),
    (3,4,Fraction(7,25),Fraction(24,25)),
    (4,5,Fraction(20,29),Fraction(21,29)),
    (0,5,Fraction(12,13),Fraction(5,13)),
    (1,4,Fraction(9,41),Fraction(40,41)),
    (0,3,Fraction(35,37),Fraction(12,37)),
    (2,5,Fraction(28,53),Fraction(45,53)),
    (0,4,Fraction(11,61),Fraction(60,61)),
]
Q = eye(6)
for i,j,c,s in rots:
    Q = matmul(givens6(i,j,c,s), Q)
dense_E = [block_row_energy(Q, a)[0] for a in range(3)]
assert all(e <= Fraction(1,2) for e in dense_E)

# Exact residual identities on a complete small integer box.
cases = 0
for a in range(-3,4):
    for b in range(-3,4):
        for c in range(-3,4):
            for d in range(-3,4):
                f2 = a*a+b*b+c*c+d*d
                det = a*d-b*c
                np = f2 + 2*det
                nm = f2 - 2*det
                assert np == (a+d)**2 + (c-b)**2
                assert nm == (a-d)**2 + (b+c)**2
                assert np*nm == f2*f2 - 4*det*det
                cases += 1

print("sharp block-row energies:", sharp)
print("max over 720 scalar permutations:", mx)
print("equality row occurrences:", eq_rows)
print("dense rational exact energies:", dense_E)
print("residual identity cases:", cases)
print("PASS MOC4-B08-BLOCKROW-HALF-ENERGY-v1")
