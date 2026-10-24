from fractions import Fraction as F
import itertools

E = [
    [1, 1, 1],
    [1,-1,-1],
    [-1,1,-1],
    [-1,-1,1],
]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return list(map(list, zip(*A)))

def D_from_P(P):
    EP = matmul(transpose(E), P)
    EPE = matmul(EP, E)
    return [[x/F(4) for x in row] for row in EPE]

def tau(i,a):
    candidates=[k for k in range(4) if k != i and E[k][a] == E[i][a]]
    assert len(candidates)==1
    return candidates[0]

# P-coupled deficit identities are affine in doubly stochastic P.
# Verify them exactly on all 24 permutation vertices.
for perm in itertools.permutations(range(4)):
    P=[[F(int(perm[i]==j)) for j in range(4)] for i in range(4)]
    D=D_from_P(P)
    for i in range(4):
        for j in range(4):
            p=P[i][j]
            for a in range(3):
                Ds=sum(D[a][b]*E[j][b] for b in range(3))
                rowmass=(F(1)-F(E[i][a])*Ds)/2
                rhs=F(1)-p-P[tau(i,a)][j]
                assert rowmass==rhs
            for b in range(3):
                sD=sum(E[i][a]*D[a][b] for a in range(3))
                colmass=(F(1)-F(E[j][b])*sD)/2
                rhs=F(1)-p-P[i][tau(j,b)]
                assert colmass==rhs

# Strictness witness in the two-rook polytope.
S = [
    [F(7,20), F(7,15), F(1,15)],
    [F(7,30), F(0),    F(31,60)],
    [F(7,60), F(1,30), F(13,60)],
]
row=[sum(r) for r in S]
col=[sum(S[i][j] for i in range(3)) for j in range(3)]
assert sum(row)==2
assert all(F(0)<=x<=1 for x in row+col)

# Explicit denominator-60 convex combination of the 18 two-rook vertices.
M2=[]
labels=[]
for rows in itertools.combinations(range(3),2):
    for cols in itertools.combinations(range(3),2):
        for pp in itertools.permutations(cols):
            M=[[F(0) for _ in range(3)] for _ in range(3)]
            for r,c in zip(rows,pp):
                M[r][c]=F(1)
            M2.append(M)
            labels.append((rows,pp))
counts=[0,12,19,1,6,0,0,0,2,1,10,2,0,0,1,6,0,0]
S2=[[sum(F(counts[k],60)*M2[k][i][j] for k in range(18))
      for j in range(3)] for i in range(3)]
assert S2==S

# Exact radical comparisons.  For a,b,c >= 0,
# sqrt(a) <= sqrt(b)+sqrt(c) iff either a<=b+c,
# or (a-b-c)^2 <= 4bc.
def sqrt_le_sum2(a,b,c):
    if a <= b+c:
        return True
    return (a-b-c)**2 <= 4*b*c

def sqrt_gt_sum2(a,b,c):
    if a <= b+c:
        return False
    return (a-b-c)**2 > 4*b*c

# Determinant-term radicands in permutation order.
rad=[]
for pp in itertools.permutations(range(3)):
    q=F(1)
    for i,j in enumerate(pp):
        q*=S[i][j]
    rad.append((pp,q))
largest=max(rad, key=lambda z: float(z[1]))
a=largest[1]
b=dict(rad)[(1,0,2)]
c=dict(rad)[(2,0,1)]
assert sqrt_le_sum2(a,b,c)

# Augmented-unitary column bracelet for columns 1 and 2 fails.
bdef=[F(1)-x for x in col]
A=bdef[1]*bdef[2]
B=S[0][1]*S[0][2]
C=S[2][1]*S[2][2]   # middle-row contribution is zero
assert sqrt_gt_sum2(A,B,C)

print("PASS MOC4-SPINOR-P-COUPLED-UNISTOCHASTIC-v1")
print("PASS P-coupled deficit identities on all 24 permutation vertices")
print("strictness S rows =", [str(x) for x in row])
print("strictness S cols =", [str(x) for x in col])
print("nonzero two-rook weights =", [(labels[k], f"{counts[k]}/60") for k in range(18) if counts[k]])
print("determinant largest radicand =", largest)
print("determinant witness bound uses radicands =", a,b,c)
print("bracelet failure radicands =", A,B,C)
print("bracelet exact test: sqrt(A) > sqrt(B)+sqrt(C)")
