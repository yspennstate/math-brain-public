from fractions import Fraction as F
from itertools import combinations, permutations

U = [
    [F(-220,243), F(71,243), F(-62,243), F(14,81)],
    [F(-61,243), F(-220,243), F(-68,243), F(-16,81)],
    [F(68,243), F(62,243), F(-215,243), F(-22,81)],
    [F(-16,81), F(14,81), F(22,81), F(-25,27)],
]
a = [F(410,81), F(15388,1539), F(-2603,21276), F(1267,984)]
b = [F(-4), F(-2), F(3), F(-1)]

def det(M):
    n=len(M)
    if n==0: return F(1)
    if n==1: return M[0][0]
    out=F(0)
    for j in range(n):
        minor=[row[:j]+row[j+1:] for row in M[1:]]
        out += (F(1) if j%2==0 else F(-1))*M[0][j]*det(minor)
    return out

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def tr(A): return [list(row) for row in zip(*A)]

def diag(v):
    n=len(v)
    return [[v[i] if i==j else F(0) for j in range(n)] for i in range(n)]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def swap(i,j):
    P=[[F(int(r==c)) for c in range(4)] for r in range(4)]
    P[i],P[j]=P[j],P[i]
    return P

def det_value(V):
    X=add(diag(a), mm(mm(V,diag(b)),tr(V)))
    return det(X),X

for i in range(4):
    for j in range(4):
        assert sum(U[k][i]*U[k][j] for k in range(4)) == (F(1) if i==j else F(0))
assert all(U[i][j] != 0 for i in range(4) for j in range(4))

for rs in combinations(range(4),2):
    for cs in combinations(range(4),2):
        m00,m01=U[rs[0]][cs[0]],U[rs[0]][cs[1]]
        m10,m11=U[rs[1]][cs[0]],U[rs[1]][cs[1]]
        mn=m00*m11-m01*m10
        assert mn != 0
        gram_trace=m00*m00+m01*m01+m10*m10+m11*m11
        disc=gram_trace*gram_trace-4*mn*mn
        assert disc != 0

assert len(set(a))==4 and len(set(b))==4
assert all(x != 0 for x in a+b)
assert all(x+y != 0 for x in a for y in b)

D,X=det_value(U)
assert D == 0
for rs in combinations(range(4),3):
    for cs in combinations(range(4),3):
        assert det([[X[i][j] for j in cs] for i in rs]) == 0
for rs in combinations(range(4),2):
    for cs in combinations(range(4),2):
        assert det([[X[i][j] for j in cs] for i in rs]) != 0

B=mm(mm(U,diag(b)),tr(U))
assert all(B[i][j] != 0 for i in range(4) for j in range(i+1,4))

col=[]
row=[]
for i,j in combinations(range(4),2):
    P=swap(i,j)
    dc,_=det_value(mm(U,P))
    dr,_=det_value(mm(P,U))
    assert dc < 0 and dr < 0
    col.append(((i+1,j+1),dc))
    row.append(((i+1,j+1),dr))

verts=[]
for sig in permutations(range(4)):
    z=F(1)
    for i in range(4):
        z *= a[i]+b[sig[i]]
    verts.append((sig,z))
assert len({z for _,z in verts}) == 24
verts_sorted=sorted(verts,key=lambda x:x[1],reverse=True)
assert verts_sorted[0][0] == (2,3,1,0)
assert verts_sorted[0][1] == F(1089898404806915,2609808965856)
assert verts_sorted[1][0] == (3,2,1,0)
unique_gap=verts_sorted[0][1]-verts_sorted[1][1]
assert unique_gap == F(457850522305,4027482972) > 0

vmax=verts_sorted[0][1]
vmin=verts_sorted[-1][1]
assert vmin == F(-749320711645835,1304904482928)
lam_max=F(299728284658334,517707965619717)
lam_min=F(217979680961383,517707965619717)
assert lam_max+lam_min == 1
assert lam_max*vmax+lam_min*vmin == 0
assert lam_max>0 and lam_min>0

print("PASS exact nonmonomial bi-Rayleigh-top certificate")
print("det =", D)
print("rank =", 2)
print("unique_support_max_perm_1based =", tuple(x+1 for x in verts_sorted[0][0]))
print("support_max =", vmax)
print("support_unique_gap =", unique_gap)
print("closest_column_swap =", max(v for _,v in col))
print("closest_row_swap =", max(v for _,v in row))
print("hull_min =", vmin)
print("two_vertex_weights =", (lam_max,lam_min))
