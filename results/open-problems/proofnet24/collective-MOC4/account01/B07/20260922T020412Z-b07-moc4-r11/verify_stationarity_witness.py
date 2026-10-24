from fractions import Fraction as F
from itertools import permutations

# Exact Gaussian-rational arithmetic z=(re,im).
def zadd(a,b): return (a[0]+b[0], a[1]+b[1])
def zsub(a,b): return (a[0]-b[0], a[1]-b[1])
def zmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
Z0=(F(0),F(0)); Z1=(F(1),F(0))
def zr(x): return (x,F(0))
def sumz(xs):
    s=Z0
    for x in xs: s=zadd(s,x)
    return s

def mm(A,B):
    return [[sumz([zmul(A[i][k],B[k][j]) for k in range(len(B))])
             for j in range(len(B[0]))] for i in range(len(A))]
def madd(A,B):
    return [[zadd(A[i][j],B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def msub(A,B):
    return [[zsub(A[i][j],B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def transpose(A): return [list(x) for x in zip(*A)]
def diag(vals):
    n=len(vals); M=[[Z0 for _ in range(n)] for _ in range(n)]
    for i,x in enumerate(vals): M[i][i]=x
    return M

def perm_sign(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1

def det_derivative(C,D):
    n=len(C); out=Z0
    for p in permutations(range(n)):
        sg=perm_sign(p)
        for k in range(n):
            term=Z1 if sg==1 else (F(-1),F(0))
            term=zmul(term,D[k][p[k]])
            for i in range(n):
                if i!=k: term=zmul(term,C[i][p[i]])
            out=zadd(out,term)
    return out

def rmm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

# Exact generic true-unitary datum from account01/B07 r11b.
U0=[
 [F(492,625),F(-31,625),F(-48,125),F(12,25)],
 [F(-9,25),F(12,25),F(-4,5),F(0)],
 [F(-36,125),F(48,125),F(9,25),F(4,5)],
 [F(-256,625),F(-492,625),F(-36,125),F(9,25)],
]
c=F(24999999,25000001); s=F(10000,25000001)
G=[[F(int(i==j)) for j in range(4)] for i in range(4)]
G[0][0]=c; G[3][3]=c; G[0][3]=s; G[3][0]=-s
U=rmm(U0,G)
assert all(sum(U[k][i]*U[k][j] for k in range(4)) == F(int(i==j))
           for i in range(4) for j in range(4))

a=[
 (F(-9,40),F(-39,20)),
 (F(-7,20),F(-37,40)),
 (F(-13,10),F(13,40)),
 (F(1,4),F(-7,10)),
]
b=[
 (F(-1,40),F(11,40)),
 (F(13,40),F(17,40)),
 (F(-23,40),F(-21,40)),
 (F(-59,40),F(33,40)),
]
Uz=[[zr(x) for x in row] for row in U]
B=mm(mm(Uz,diag(b)),transpose(Uz))
C=madd(diag(a),B)

# Real row-pair (1,3) conjugation G(t) B G(t)^T, with J_13=-1,J_31=+1.
J=[[Z0 for _ in range(4)] for _ in range(4)]
J[0][2]=(F(-1),F(0)); J[2][0]=(F(1),F(0))
dB=msub(mm(J,B),mm(B,J))
dz=det_derivative(C,dB)
expected=F(284796813152662076044041,244140644531250390625000)
assert dz[0] == expected
assert expected > 0
print("U_orthogonal PASS")
print("support_derivative_row_pair_13 =", expected)
print("prior_generic_parity_witness_not_stationary PASS")
