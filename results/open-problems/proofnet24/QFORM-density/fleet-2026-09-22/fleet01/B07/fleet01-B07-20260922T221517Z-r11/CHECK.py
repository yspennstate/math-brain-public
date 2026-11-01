from fractions import Fraction as F
from itertools import combinations

# Tiny exact linear-algebra helpers over Fraction.
def T(A): return [list(x) for x in zip(*A)]
def mm(A,B):
    BT=T(B)
    return [[sum(x*y for x,y in zip(r,c)) for c in BT] for r in A]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(a,A): return [[a*x for x in r] for r in A]
def det(A):
    A=[r[:] for r in A]; n=len(A); out=F(1)
    for k in range(n):
        pivots=[i for i in range(k,n) if A[i][k]]
        if not pivots: return F(0)
        p=pivots[0]
        if p!=k: A[k],A[p]=A[p],A[k]; out=-out
        piv=A[k][k]; out*=piv
        for i in range(k+1,n):
            q=A[i][k]/piv
            for j in range(k+1,n): A[i][j]-=q*A[k][j]
    return out
def inv(A):
    n=len(A); M=[A[i][:]+eye(n)[i] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if M[i][k])
        M[k],M[p]=M[p],M[k]
        q=M[k][k]; M[k]=[x/q for x in M[k]]
        for i in range(n):
            if i==k: continue
            q=M[i][k]
            M[i]=[M[i][j]-q*M[k][j] for j in range(2*n)]
    return [r[n:] for r in M]
def submatrix(B,I,J): return [[B[i][j] for j in J] for i in I]
def Ek(B,k):
    if k==0: return F(1)
    m,n=len(B),len(B[0]); s=F(0)
    for I in combinations(range(m),k):
        for J in combinations(range(n),k): s += det(submatrix(B,I,J))**2
    return s
def DB(B,z):
    m=len(B)
    return det(add(eye(m),scale(z,mm(B,T(B)))))
def anchored(B,i,j,k):
    m,n=len(B),len(B[0]); s=F(0)
    for I in combinations(range(m),k):
        if i not in I: continue
        for J in combinations(range(n),k):
            if j not in J: continue
            s += det(submatrix(B,I,J))**2
    return s

# Nonzero-edge example checks Cauchy--Binet, graph-DPP inclusion, and Schur conditioning.
B=[[F(2),F(1),F(-1)],[F(3),F(2),F(0)],[F(1),F(-2),F(1)],[F(0),F(1),F(2)]]
z=F(2,3); i=1; j=0; m=len(B); n=len(B[0])
D=DB(B,z)
Ms=[anchored(B,i,j,k) for k in range(1,min(m,n)+1)]
Fij=sum(z**(k+1)*Ms[k] for k in range(len(Ms)))
rows=[a for a in range(m) if a!=i]; cols=[a for a in range(n) if a!=j]
b=B[i][j]; r=[[B[i][a] for a in cols]]; c=[[B[a][j]] for a in rows]; C=submatrix(B,rows,cols)
Csharp=[[C[a][q]-c[a][0]*r[0][q]/b for q in range(len(cols))] for a in range(len(rows))]
assert Ms == [b*b*Ek(Csharp,k) for k in range(0,min(len(rows),len(cols))+1)]
assert Fij == z*b*b*DB(Csharp,z)

# Graph projection identity, avoiding sqrt(z): H_ij^2=z*(B(I+zB^TB)^-1)_ij^2.
KL=mm(scale(z,mm(B,T(B))),inv(add(eye(m),scale(z,mm(B,T(B))))))
KR=mm(scale(z,mm(T(B),B)),inv(add(eye(n),scale(z,mm(T(B),B)))))
BR=mm(B,inv(add(eye(n),scale(z,mm(T(B),B)))))
joint=KL[i][i]*KR[j][j]+z*BR[i][j]**2
assert Fij/D == joint

# Zero-edge bordered resolvent identity.
C=[[F(1),F(2),F(0)],[F(0),F(1),F(-1)]]
c=[[F(2)],[F(-1)]]; r=[[F(1),F(3),F(-2)]]; z=F(3,5)
B0=[[F(0)]+r[0]] + [[c[a][0]]+C[a] for a in range(len(C))]
DC=DB(C,z)
AC=inv(add(eye(len(C)),scale(z,mm(C,T(C)))))
RC=inv(add(eye(len(C[0])),scale(z,mm(T(C),C))))
alpha=z*mm(mm(T(c),AC),c)[0][0]
beta=z*mm(mm(r,RC),T(r))[0][0]
core=mm(mm(T(c),AC),mm(C,T(r)))[0][0]
gamma2=z**3*core**2
rhsD=DC*((1+alpha)*(1+beta)+gamma2)
assert DB(B0,z)==rhsD
F0=sum(z**k*anchored(B0,0,0,k) for k in range(1,min(len(B0),len(B0[0]))+1))
assert F0==DC*(alpha*beta+gamma2)

# Constants used in the theorem.
p0=F(529,576)
assert 3*p0-2 == F(145,192)
assert (3*p0-2)/4 == F(145,768)
assert (3*p0-2)/2 == F(145,384)
assert 2/p0-1 == F(623,529)

print('QFORM_DETERMINANT_CONDITIONED_ANCHOR_CHECK_PASS')
print('D_nonzero_edge=',D)
print('F_nonzero_edge=',Fij)
print('M_nonzero_edge=',Ms)
print('D_zero_edge=',DB(B0,z))
print('F_zero_edge=',F0)
print('p0=',p0,'loworder=',F(145,192),'tau_sharp_cap=',F(623,529))
