from fractions import Fraction
from itertools import product


def det3(m):
    return (
        m[0][0]*m[1][1]*m[2][2]
        + m[0][1]*m[1][2]*m[2][0]
        + m[0][2]*m[1][0]*m[2][1]
        - m[0][2]*m[1][1]*m[2][0]
        - m[0][1]*m[1][0]*m[2][2]
        - m[0][0]*m[1][2]*m[2][1]
    )

# Exact q=2 motif-ledger sanity check on a fixed symmetric integer matrix.
A = [
    [3,2,1,-1,2,0],
    [2,5,-2,1,3,-1],
    [1,-2,4,2,-1,1],
    [-1,1,2,6,0,2],
    [2,3,-1,0,7,-2],
    [0,-1,1,2,-2,8],
]
H1=[0]; H2=[1]; R=[2,3]; C=[4,5]
P2=0
for i,j,r,c in product(H1,H2,R,C):
    m=[[A[i][i],A[i][j],A[i][c]],
       [A[j][i],A[j][j],A[j][c]],
       [A[r][i],A[r][j],A[r][c]]]
    P2 += det3(m)**2
D1=sum(A[i][i]**2 for i in H1)
D2=sum(A[j][j]**2 for j in H2)
F=sum(A[r][c]**2 for r in R for c in C)
G=sum(A[i][j]**4 for i in H1 for j in H2)
Ri={i:sum(A[i][r]**2 for r in R) for i in H1+H2}
Ci={i:sum(A[i][c]**2 for c in C) for i in H1+H2}
M=[
    D1*D2*F,
    G*F,
    D1*sum(Ri[j]*Ci[j] for j in H2),
    D2*sum(Ri[i]*Ci[i] for i in H1),
    sum(A[i][j]**2*Ri[i]*Ci[j] for i in H1 for j in H2),
    sum(A[i][j]**2*Ci[i]*Ri[j] for i in H1 for j in H2),
]
assert P2 == 764
assert M == [1350,96,450,200,80,80]
assert P2 <= 6*sum(M)

# Exact rank-one singular-pair factorization.
a,b,d = 4,2,1
assert a*d-b*b == 0
Aik={2:Fraction(3),3:Fraction(-1),4:Fraction(2),5:Fraction(5)}
Ajk={2:Fraction(1),3:Fraction(4),4:Fraction(-2),5:Fraction(0)}
ArC={(2,4):Fraction(7),(2,5):Fraction(-3),(3,4):Fraction(6),(3,5):Fraction(2)}
s={k:Ajk[k]-Fraction(b,a)*Aik[k] for k in Aik}

def mixed_det(r,c):
    return det3([
        [Fraction(a),Fraction(b),Aik[c]],
        [Fraction(b),Fraction(d),Ajk[c]],
        [Aik[r],Ajk[r],ArC[(r,c)]],
    ])

for r in [2,3]:
    for c in [4,5]:
        assert mixed_det(r,c) == -a*s[r]*s[c]
U=sum(s[r]**2 for r in [2,3])
V=sum(s[c]**2 for c in [4,5])
w=sum(mixed_det(r,c)**2 for r in [2,3] for c in [4,5])
assert U == Fraction(41,2)
assert V == Fraction(61,4)
assert w == 5002 == a*a*U*V

# Target-level motif constants from the previous colored packet bounds.
assert Fraction(1,5184)/36 == Fraction(1,186624)
assert Fraction(1,3125)/36 == Fraction(1,112500)
assert Fraction(1,512)/36 == Fraction(1,18432)
assert Fraction(1,18)/36 == Fraction(1,648)

print('P2=', P2)
print('motifs=', M)
print('singular_star_U,V,w=', U, V, w)
print('STATUS=PASS')
