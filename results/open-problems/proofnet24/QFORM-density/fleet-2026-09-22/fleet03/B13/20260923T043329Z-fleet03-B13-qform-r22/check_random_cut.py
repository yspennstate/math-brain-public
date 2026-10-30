from fractions import Fraction
from itertools import combinations
import math

A = [
    [3, 1, 2, -1, 0, 1, -2],
    [1, 2, -1, 1, 2, 0, 1],
    [2,-1, 1, 2,-2, 1, 0],
    [-1,1, 2,-2, 1, 2, 1],
    [0, 2,-2, 1, 3,-1, 2],
    [1, 0, 1, 2,-1, 2,-2],
    [-2,1, 0, 1, 2,-2, 1],
]


def det2(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]


def det3(m):
    a,b,c=m[0]; d,e,f=m[1]; g,h,i=m[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def det(mat):
    n=len(mat)
    if n==0: return Fraction(1)
    if n==1: return mat[0][0]
    ans=Fraction(0)
    for j in range(n):
        sub=[row[:j]+row[j+1:] for row in mat[1:]]
        ans += ((-1)**j)*mat[0][j]*det(sub)
    return ans

k=0
a=Fraction(A[k][k],1)
inds=[i for i in range(len(A)) if i!=k]
S=[[Fraction(A[i][j],1)-Fraction(A[i][k]*A[k][j],A[k][k]) for j in inds] for i in inds]
m=len(inds)

pairs=list(combinations(range(m),2))
triples=list(combinations(range(m),3))
D2=Fraction(0)
for R in pairs:
    for C in pairs:
        if set(R).isdisjoint(C):
            d=det2([[S[r][c] for c in C] for r in R])
            D2 += d*d
D3=Fraction(0)
for R in triples:
    for C in triples:
        if set(R).isdisjoint(C):
            d=det3([[S[r][c] for c in C] for r in R])
            D3 += d*d

def cut_z(mask,r):
    L=[i for i in range(m) if (mask>>i)&1]
    Rside=[i for i in range(m) if not ((mask>>i)&1)]
    z=Fraction(0)
    if len(L)<r or len(Rside)<r: return z
    for U in combinations(L,r):
        for V in combinations(Rside,r):
            mat=[[S[u][v] for v in V] for u in U]
            d=det2(mat) if r==2 else det3(mat)
            z += d*d
    return z

z2=[cut_z(mask,2) for mask in range(1<<m)]
z3=[cut_z(mask,3) for mask in range(1<<m)]
avg2=sum(z2,Fraction(0))/Fraction(1<<m,1)
avg3=sum(z3,Fraction(0))/Fraction(1<<m,1)

B3=Fraction(0)
for R in combinations(inds,2):
    for C in combinations(inds,2):
        if set(R).isdisjoint(C):
            rows=[k]+list(R); cols=[k]+list(C)
            d=det([[Fraction(A[i][j],1) for j in cols] for i in rows])
            B3 += d*d
B4=Fraction(0)
for R in combinations(inds,3):
    for C in combinations(inds,3):
        if set(R).isdisjoint(C):
            rows=[k]+list(R); cols=[k]+list(C)
            d=det([[Fraction(A[i][j],1) for j in cols] for i in rows])
            B4 += d*d

assert avg2 == D2/Fraction(16,1)
assert avg3 == D3/Fraction(64,1)
assert B3 == a*a*D2
assert B4 == a*a*D3

C_pair=26.335*math.sqrt(2.0)
C_cross3=16.018*math.sqrt(2.0)
print('D2perp=',D2)
print('average_cut_E2=',avg2)
print('D2perp/16=',D2/Fraction(16,1))
print('max_cut_E2=',max(z2))
print('B3=',B3,'a^2*D2=',a*a*D2)
print('D3perp=',D3)
print('average_cut_E3=',avg3)
print('D3perp/64=',D3/Fraction(64,1))
print('max_cut_E3=',max(z3))
print('B4=',B4,'a^2*D3=',a*a*D3)
print('pair_cut_constant=',repr(C_pair))
print('cross3_cut_constant=',repr(C_cross3))
print('QFORM_B13_R22_RANDOM_CUT_CHECK_PASS')
