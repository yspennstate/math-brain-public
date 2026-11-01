from fractions import Fraction as F
from itertools import combinations

PAIRS=list(combinations(range(4),2))
GROUPED=[(0,1),(2,3),(0,2),(1,3),(0,3),(1,2)]
WEDGE_PAIRS=PAIRS
WIDX={p:i for i,p in enumerate(WEDGE_PAIRS)}

def det(M):
    A=[row[:] for row in M]
    n=len(A); ans=F(1)
    for c in range(n):
        p=next((r for r in range(c,n) if A[r][c]),None)
        if p is None: return F(0)
        if p!=c:
            A[p],A[c]=A[c],A[p]; ans=-ans
        q=A[c][c]; ans*=q
        for j in range(c,n): A[c][j]/=q
        for r in range(c+1,n):
            q=A[r][c]
            if q:
                for j in range(c,n): A[r][j]-=q*A[c][j]
    return ans

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def tr(A): return [list(x) for x in zip(*A)]

def root_J(i,j):
    G=eye(4)
    G[i][i]=G[j][j]=F(0)
    G[i][j]=F(1); G[j][i]=F(-1)
    return G

def swap_P(i,j):
    P=eye(4)
    P[i][i]=P[j][j]=F(0)
    P[i][j]=P[j][i]=F(1)
    return P

def wedge_entry(G, rows, cols):
    i,j=rows; a,b=cols
    return G[i][a]*G[j][b]-G[i][b]*G[j][a]

def wedge_matrix(G):
    M=[[wedge_entry(G,r,c) for c in WEDGE_PAIRS] for r in WEDGE_PAIRS]
    ii=[WIDX[p] for p in GROUPED]
    return [[M[i][j] for j in ii] for i in ii]

def block(M,r,c):
    return [[M[2*r+i][2*c+j] for j in range(2)] for i in range(2)]

def neg_transpose(A):
    return [[-A[j][i] for j in range(2)] for i in range(2)]

def is_zero(A): return all(x==0 for row in A for x in row)
def is_I(A): return A==eye(2)

records=[]
for ij in PAIRS:
    G=root_J(*ij)
    assert mm(G,tr(G))==eye(4) and det(G)==1
    P=swap_P(*ij)
    D=mm(G,tr(P))
    assert all(D[r][c]==0 for r in range(4) for c in range(4) if r!=c)
    assert mm(D,P)==G

    W=wedge_matrix(G)
    assert mm(W,tr(W))==eye(6) and det(W)==1
    fixed=[r for r in range(3) if is_I(block(W,r,r))]
    assert len(fixed)==1
    f=fixed[0]
    moving=[r for r in range(3) if r!=f]
    a,g=moving
    Z=block(W,a,g)
    eps=det(Z)
    assert eps in (F(1),F(-1))
    assert block(W,g,a)==neg_transpose(Z)
    assert is_zero(block(W,a,a)) and is_zero(block(W,g,g))
    for r in range(3):
        for c in range(3):
            if r==c==f or (r,c) in ((a,g),(g,a),(a,a),(g,g)):
                continue
            assert is_zero(block(W,r,c))
    records.append((ij,(a,g),int(eps),Z))

ALL=set(range(4))
for ij,ag,eps,Z in records:
    comp=tuple(sorted(ALL-set(ij)))
    rec=next(x for x in records if x[0]==comp)
    assert rec[1]==ag and rec[2]==-eps

print('PASS root-SU2 / Spin(6) block-plane endpoint identification')
for ij,ag,eps,Z in records:
    print(f'row-root {ij[0]+1}{ij[1]+1} -> block planes {ag[0]+1}{ag[1]+1}, det(Z)={eps}, Z={Z}')
print('PASS complementary roots share a block-plane pair with opposite det(Z)')
