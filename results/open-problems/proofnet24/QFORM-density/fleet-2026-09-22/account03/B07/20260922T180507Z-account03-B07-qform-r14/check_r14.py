from fractions import Fraction
from math import e, sqrt

# Exact fixed-skeleton test matrix.
B = [
    [Fraction(1),Fraction(2),Fraction(0),Fraction(1)],
    [Fraction(0),Fraction(1),Fraction(1),Fraction(2)],
    [Fraction(2),Fraction(0),Fraction(1),Fraction(1)],
    [Fraction(1),Fraction(-1),Fraction(2),Fraction(0)],
    [Fraction(2),Fraction(1),Fraction(-1),Fraction(1)],
]

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def det2(M): return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def gram(rows): return [[dot(B[i],B[j]) for j in rows] for i in rows]
def gramdet3(rows): return det3(gram(rows))

# J={0}: direct mass.
mass1=sum(gramdet3((0,j,k)) for j in range(1,5) for k in range(j+1,5))
# Projection onto b0^perp and e2 of residual Gram.
b0=B[0]; n0=dot(b0,b0)
C=[]
for k in range(1,5):
    alpha=dot(B[k],b0)/n0
    C.append([B[k][q]-alpha*b0[q] for q in range(4)])
e2=Fraction(0)
for a in range(4):
    for b in range(a+1,4):
        G=[[dot(C[a],C[a]),dot(C[a],C[b])],[dot(C[b],C[a]),dot(C[b],C[b])]]
        e2+=det2(G)

# J={0,1}: direct mass and orthogonal-complement residual Frobenius energy.
G01=gram((0,1)); detG01=det2(G01)
inv=[[G01[1][1]/detG01,-G01[0][1]/detG01],[-G01[1][0]/detG01,G01[0][0]/detG01]]
fro2=Fraction(0)
for k in (2,3,4):
    rhs=[dot(B[k],B[0]),dot(B[k],B[1])]
    coeff=[sum(inv[a][b]*rhs[b] for b in range(2)) for a in range(2)]
    c=[B[k][q]-coeff[0]*B[0][q]-coeff[1]*B[1][q] for q in range(4)]
    fro2+=dot(c,c)
mass2=sum(gramdet3((0,1,k)) for k in (2,3,4))

print('r1_direct=',mass1)
print('r1_factor=',n0*e2,' n0=',n0,' e2=',e2)
print('r2_direct=',mass2)
print('r2_factor=',detG01*fro2,' detG=',detG01,' fro2=',fro2)

Cfinite=(24*e/sqrt(2))*2**(4/3)*8**(4/17)
Crank3=(3*e/(sqrt(11/4)*(1/4)))*2048**(1/6)
print('finite_scale_constant=',repr(Cfinite))
print('rank3_endpoint_constant=',repr(Crank3))
assert mass1 == n0*e2 == 428
assert mass2 == detG01*fro2 == 230
assert Cfinite < 190
assert Crank3 < 70.10
print('PASS')
