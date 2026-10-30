from fractions import Fraction
from itertools import combinations
import math

# Exact-rational regression matrix.  Pivot k=0 is nonzero.
A = [
    [3, 1, 2, -1, 0, 1, -2],
    [1, 2, -1, 1, 2, 0, 1],
    [2,-1, 1, 2,-2, 1, 0],
    [-1,1, 2,-2, 1, 2, 1],
    [0, 2,-2, 1, 3,-1, 2],
    [1, 0, 1, 2,-1, 2,-2],
    [-2,1, 0, 1, 2,-2, 1],
]

def det(mat):
    n=len(mat)
    if n==0:
        return Fraction(1)
    if n==1:
        return mat[0][0]
    ans=Fraction(0)
    for j in range(n):
        sub=[row[:j]+row[j+1:] for row in mat[1:]]
        ans += ((-1)**j)*mat[0][j]*det(sub)
    return ans

k=0
a=Fraction(A[k][k],1)
inds=[i for i in range(len(A)) if i!=k]
S=[[Fraction(A[i][j],1)-Fraction(A[i][k]*A[k][j],A[k][k])
    for j in inds] for i in inds]
m=len(inds)

def disjoint_volume(r):
    total=Fraction(0)
    for R in combinations(range(m),r):
        for C in combinations(range(m),r):
            if set(R).isdisjoint(C):
                d=det([[S[x][y] for y in C] for x in R])
                total += d*d
    return total

def cut_volume(mask,r):
    L=[i for i in range(m) if (mask>>i)&1]
    Rc=[i for i in range(m) if not ((mask>>i)&1)]
    total=Fraction(0)
    for R in combinations(L,r):
        for C in combinations(Rc,r):
            d=det([[S[x][y] for y in C] for x in R])
            total += d*d
    return total

def bordered_volume(r):
    total=Fraction(0)
    for R in combinations(inds,r):
        for C in combinations(inds,r):
            if set(R).isdisjoint(C):
                rows=[k]+list(R)
                cols=[k]+list(C)
                d=det([[Fraction(A[i][j],1) for j in cols] for i in rows])
                total += d*d
    return total

for r in (1,2,3):
    D=disjoint_volume(r)
    values=[cut_volume(mask,r) for mask in range(1<<m)]
    avg=sum(values,Fraction(0))/Fraction(1<<m,1)
    assert avg == D/Fraction(4**r,1)
    print(f'r={r} Dperp={D} average={avg} expected={D/Fraction(4**r,1)} max={max(values)}')

D2=disjoint_volume(2)
D3=disjoint_volume(3)
B3=bordered_volume(2)
B4=bordered_volume(3)
assert B3 == a*a*D2
assert B4 == a*a*D3
print('B3=',B3,'a^2*D2=',a*a*D2)
print('B4=',B4,'a^2*D3=',a*a*D3)

C_H=2*math.sqrt(math.pi/math.sqrt(3.0))
C_E2=C_H*(7.681*(16.0**(1.0/6.0)))**(3.0/4.0)
C_cross3_selected=C_H*(6.787**(3.0/4.0))
C_cross3_cut=C_cross3_selected*(64.0**(1.0/12.0))
C_L3_cut=6.787*(64.0**(1.0/9.0))
C_slab34_cut=14.485199899718856*(64.0**(1.0/8.0))

assert C_E2 < 17.576
assert C_cross3_cut < 16.018
assert C_L3_cut < 10.774
assert C_slab34_cut < 24.362
assert Fraction(1,16*18) == Fraction(1,288)

print('half_Riesz_constant=',repr(C_H))
print('order2_paid_cut_constant=',repr(C_E2))
print('cross3_selected_constant=',repr(C_cross3_selected))
print('cross3_cut_constant=',repr(C_cross3_cut))
print('cutfree_L3_constant=',repr(C_L3_cut))
print('cutfree_threequarter_slab_constant=',repr(C_slab34_cut))
print('trihub_fraction=',Fraction(1,288))
print('QFORM_B13_CUTFREE_COMPILER_CHECK_PASS')
