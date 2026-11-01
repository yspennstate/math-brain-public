from fractions import Fraction as F
from itertools import permutations

def det(M):
    n=len(M)
    out=F(0)
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        z=F(-1 if inv%2 else 1)
        for i in range(n):
            z*=M[i][p[i]]
        out+=z
    return out

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(row) for row in zip(*A)]

def submatrix(A, rows, cols):
    return [[A[i][j] for j in cols] for i in rows]

def prod(xs):
    z=F(1)
    for x in xs: z*=x
    return z

# Exact rational orthogonal Householder U = I - vv^T/15, v=(1,2,3,4).
v=[F(1),F(2),F(3),F(4)]
U=[[F(int(i==j))-v[i]*v[j]/F(15) for j in range(4)] for i in range(4)]
assert matmul(transpose(U),U)==[[F(int(i==j)) for j in range(4)] for i in range(4)]

P=[[U[i][j]**2 for j in range(4)] for i in range(4)]
pairs=[(0,1),(0,2),(0,3)]
allset=set(range(4))
def q(S,T):
    return det(submatrix(U,S,T))**2

R=[[F(0) for _ in range(3)] for __ in range(3)]
D=[[F(0) for _ in range(3)] for __ in range(3)]
for aa,S in enumerate(pairs):
    for bb,T in enumerate(pairs):
        Tc=tuple(sorted(allset-set(T)))
        u=q(S,T); w=q(S,Tc)
        R[aa][bb]=u+w
        D[aa][bb]=u-w

E=[[F(1),F(1),F(1)],
   [F(1),F(-1),F(-1)],
   [F(-1),F(1),F(-1)],
   [F(-1),F(-1),F(1)]]
ET=transpose(E)
assert matmul(D,ET)==matmul(ET,P)
assert D==[[x/F(4) for x in row] for row in matmul(matmul(ET,P),E)]
assert [sum(row) for row in R]==[F(1)]*3
assert [sum(R[i][j] for i in range(3)) for j in range(3)]==[F(1)]*3
assert all(R[i][j] >= abs(D[i][j]) for i in range(3) for j in range(3))

# Singular + repeated spectrum test. No division by eigenvalues occurs.
a=[F(0),F(2),F(2),F(7)]
b=[F(3),F(0),F(5),F(5)]
Aplus=[]; Aminus=[]; Bplus=[]; Bminus=[]
for S in pairs:
    Sc=tuple(sorted(allset-set(S)))
    x=prod(a[i] for i in S); xp=prod(a[i] for i in Sc)
    y=prod(b[i] for i in S); yp=prod(b[i] for i in Sc)
    Aplus.append(x+xp); Aminus.append(xp-x)
    Bplus.append(y+yp); Bminus.append(y-yp)

c=[prod(a[r] for r in range(4) if r!=i) for i in range(4)]
d=[prod(b[s] for s in range(4) if s!=j) for j in range(4)]
EA=[sum(E[i][aa]*Aminus[aa] for aa in range(3)) for i in range(4)]
EB=[sum(E[j][bb]*Bminus[bb] for bb in range(3)) for j in range(4)]
H=[[c[i]*b[j]+a[i]*d[j]+EA[i]*EB[j]/F(8) for j in range(4)] for i in range(4)]
constant=prod(a)+prod(b)
decomp=(constant
        +sum(H[i][j]*P[i][j] for i in range(4) for j in range(4))
        +F(1,2)*sum(Aplus[aa]*R[aa][bb]*Bplus[bb]
                    for aa in range(3) for bb in range(3)))

UBU=matmul(matmul(U,[[b[i] if i==j else F(0) for j in range(4)] for i in range(4)]),transpose(U))
M=[[(a[i] if i==j else F(0))+UBU[i][j] for j in range(4)] for i in range(4)]
direct=det(M)
assert direct==decomp==F(148984,225)

print('D E^T = E^T P: PASS')
print('D = (1/4) E^T P E: PASS')
print('R doubly stochastic and R>=|D|: PASS')
print('singular/repeated determinant reconstruction: PASS')
print('det =', direct)
print('P =', P)
print('R =', R)
print('D =', D)
