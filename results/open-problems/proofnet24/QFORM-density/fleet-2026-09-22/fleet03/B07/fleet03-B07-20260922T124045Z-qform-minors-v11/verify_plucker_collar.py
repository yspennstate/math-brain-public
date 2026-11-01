from fractions import Fraction as F
from itertools import combinations


def det2(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def det3(a):
    return (
        a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
    )


def transpose(a):
    return [list(x) for x in zip(*a)]


def matmul(a,b):
    bt=transpose(b)
    return [[sum(x*y for x,y in zip(r,c)) for c in bt] for r in a]


def submatrix_rows(a, rows):
    return [a[i][:] for i in rows]


def gram(rows):
    r=submatrix_rows(U, rows)
    return matmul(transpose(r),r)


def inv3(a):
    d=det3(a)
    assert d != 0
    cof=[]
    for i in range(3):
        row=[]
        for j in range(3):
            m=[[a[r][c] for c in range(3) if c!=j] for r in range(3) if r!=i]
            row.append((F(-1) if (i+j)%2 else F(1))*det2(m))
        cof.append(row)
    return [[transpose(cof)[i][j]/d for j in range(3)] for i in range(3)]


def qform(v,a):
    return sum(v[i]*a[i][j]*v[j] for i in range(3) for j in range(3))


# First three normalized columns of the 4x4 Sylvester Hadamard matrix.
U=[
    [F(1,2), F(1,2), F(1,2)],
    [F(1,2),-F(1,2), F(1,2)],
    [F(1,2), F(1,2),-F(1,2)],
    [F(1,2),-F(1,2),-F(1,2)],
]
I=[[F(int(i==j)) for j in range(3)] for i in range(3)]
assert gram(range(4)) == I

# Exact Cauchy-Binet/Plucker mass.
w={}
for S in combinations(range(4),3):
    d=det3(submatrix_rows(U,S))
    w[S]=d*d
assert set(w.values()) == {F(1,4)}
assert sum(w.values(),F(0)) == 1

# Full leverage = 3/4, and q after deleting coordinate 0 is 1/4.
G0=gram(range(4))
G0i=inv3(G0)
ell0=qform(U[0],G0i)
assert ell0 == F(3,4)
R1=[1,2,3]
G1=gram(R1)
q1=det3(G1)
assert q1 == F(1,4)
assert q1 == F(1)*(1-ell0)

# With exactly three retained rows in rank three, whitening makes every
# retained row leverage one. Check through G1^{-1} exactly.
G1i=inv3(G1)
ells1={i:qform(U[i],G1i) for i in R1}
assert set(ells1.values()) == {F(1)}

# Deleting any further row kills the rank-three retained volume.
R2=[2,3]
G2=gram(R2)
assert det3(G2) == 0
assert det3(G2) == q1*(1-ells1[1])
assert det3(G2) < F(1,8)

# The localized pair J={0,1} captures an entire spectral direction.
# K=U_J^T U_J has eigenvector v=(1,0,1) with eigenvalue 1.
UJ=submatrix_rows(U,[0,1])
K=matmul(transpose(UJ),UJ)
v=[F(1),F(0),F(1)]
Kv=[sum(K[i][j]*v[j] for j in range(3)) for i in range(3)]
assert Kv == v
# Hence its normalized Rayleigh quotient is 1 > 1/2.
assert qform(v,K) / sum(x*x for x in v) == 1

print('PASS')
print('plucker_weights=', {str(k):str(v) for k,v in w.items()})
print('initial_leverage=', ell0)
print('q_after_one_deletion=', q1)
print('conditional_leverages_after_one_deletion=', ells1)
print('q_after_two_deletions=', det3(G2))
print('localized_pair_rayleigh=', qform(v,K)/sum(x*x for x in v))
