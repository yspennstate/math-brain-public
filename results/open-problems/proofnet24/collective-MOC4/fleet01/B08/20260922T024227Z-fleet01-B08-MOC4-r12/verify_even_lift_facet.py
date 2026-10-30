from fractions import Fraction as F
from itertools import combinations, permutations, product


def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def tr(A):
    return [list(x) for x in zip(*A)]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def rank(A):
    A=[list(map(F,row)) for row in A]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def det(A):
    A=[row[:] for row in A]; n=len(A); ans=F(1)
    for c in range(n):
        p=next((i for i in range(c,n) if A[i][c]),None)
        if p is None: return F(0)
        if p!=c:
            A[c],A[p]=A[p],A[c]; ans=-ans
        z=A[c][c]; ans*=z
        for i in range(c+1,n):
            if A[i][c]:
                t=A[i][c]/z
                for j in range(c,n): A[i][j]-=t*A[c][j]
    return ans

# Exact real unitary (orthogonal) counterexample. It is a product of rational Givens rotations.
U=[
 [F(636,1105),F(-423,1105),F(-12,65),F(-772,1105)],
 [F(3576,5525),F(332,5525),F(-144,325),F(3411,5525)],
 [F(164,425),F(348,425),F(9,25),F(-96,425)],
 [F(27,85),F(-36,85),F(4,5),F(24,85)],
]
assert mm(tr(U),U)==eye(4)
assert det(U)==1
assert all(U[i][j] for i in range(4) for j in range(4))
assert all(U[I[0]][J[0]]*U[I[1]][J[1]]-U[I[0]][J[1]]*U[I[1]][J[0]]
           for I in combinations(range(4),2) for J in combinations(range(4),2))

# Complementary-pair basis: (12,34 | 13,-24 | 14,23), with 0-based indices.
ordr=[(0,1),(2,3),(0,2),(1,3),(0,3),(1,2)]
sgn=[1,1,1,-1,1,1]
O=[[F(0) for _ in range(6)] for __ in range(6)]
for a,I in enumerate(ordr):
    for b,J in enumerate(ordr):
        m=U[I[0]][J[0]]*U[I[1]][J[1]]-U[I[0]][J[1]]*U[I[1]][J[0]]
        O[a][b]=sgn[a]*sgn[b]*m
assert mm(tr(O),O)==eye(6)
assert det(O)==1

# B_{ab}: z -> m z + n zbar. q+ = |m|^2, q- = |n|^2.
qp=[[F(0) for _ in range(3)] for __ in range(3)]
qm=[[F(0) for _ in range(3)] for __ in range(3)]
for a in range(3):
    for b in range(3):
        A,B=O[2*a][2*b],O[2*a][2*b+1]
        C,D=O[2*a+1][2*b],O[2*a+1][2*b+1]
        qp[a][b]=((A+D)**2+(C-B)**2)/4
        qm[a][b]=((A-D)**2+(C+B)**2)/4
R=[[qp[a][b]+qm[a][b] for b in range(3)] for a in range(3)]
D=[[qp[a][b]-qm[a][b] for b in range(3)] for a in range(3)]
assert [sum(x) for x in R]==[F(1)]*3
assert [sum(R[a][b] for a in range(3)) for b in range(3)]==[F(1)]*3

# Candidate even-lift facet.
def Phi(R,D):
    return (R[0][0]-R[0][1]+3*D[0][2]+3*D[1][0]+R[1][1]-R[1][2]
            -R[2][0]-3*D[2][1]+R[2][2])

vertices=[]; vals=[]; tight=[]
for p in permutations(range(3)):
    for eps in product((1,-1),repeat=3):
        if eps[0]*eps[1]*eps[2]!=1: continue
        RR=[[F(0) for _ in range(3)] for __ in range(3)]
        DD=[[F(0) for _ in range(3)] for __ in range(3)]
        v=[0]*18
        for a in range(3):
            RR[a][p[a]]=1; DD[a][p[a]]=eps[a]
            v[(a*3+p[a])*2+(0 if eps[a]==1 else 1)]=1
        val=Phi(RR,DD); vals.append(val); vertices.append(v)
        if val==3: tight.append(v)
assert max(vals)==3
assert sorted(set(vals))==[-9,-3,3]
assert len(tight)==13
assert rank([[vertices[i][j]-vertices[0][j] for j in range(18)] for i in range(1,24)])==13
assert rank([[tight[i][j]-tight[0][j] for j in range(18)] for i in range(1,13)])==12

value=Phi(R,D); gap=value-3
assert gap==F(114063834,763140625)>0
print('U orthogonal det=1: PASS')
print('all 16 entries nonzero: PASS')
print('all 36 two-by-two minors nonzero: PASS')
print('even-endpoint facet max = 3')
print('endpoint facet values =', sorted(set(vals)))
print('polytope affine dimension = 13')
print('tight vertices = 13; tight affine rank = 12')
print('Phi(actual q) =', value)
print('facet violation =', gap, float(gap))
print('PASS: actual true-unitary Bogoliubov q is outside conv(24 even colored matchings)')
