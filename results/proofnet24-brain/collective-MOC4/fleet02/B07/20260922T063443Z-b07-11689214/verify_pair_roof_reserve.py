from fractions import Fraction as F
from itertools import permutations, combinations

# Exact Gaussian rationals as (real,imag).
def Z(r=0,i=0): return (F(r),F(i))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def scale(x,q): return (x[0]*q,x[1]*q)
def sumz(xs):
    out=Z()
    for x in xs: out=add(out,x)
    return out
def mm(A,B):
    return [[sumz(mul(A[i][k],B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def adj(A): return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def diag(v): return [[v[i] if i==j else Z() for j in range(4)] for i in range(4)]
def sign(p): return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1
def det4(A):
    out=Z()
    for p in permutations(range(4)):
        t=Z(1)
        for i in range(4): t=mul(t,A[i][p[i]])
        out=add(out,scale(t,F(sign(p))))
    return out

# Current fleet03/B08 MOC4-DENSE-CAYLEY-ADVERSARY-v1 exact datum.
G=[
 [(-2724,-1551),(234,247),(-1219,167),(1106,-96)],
 [(236,-101),(-2782,1417),(1,1607),(490,228)],
 [(1443,39),(845,793),(-2522,702),(234,-1534)],
 [(-820,200),(-416,1144),(-1060,-784),(-2910,536)]
]
U=[[scale(Z(r,i),F(1,3562)) for (r,i) in row] for row in G]
a=[Z(18,-17),Z(-20,2),Z(15,-22),Z(-21,2)]
b=[Z(-19,4),Z(25,-5),Z(18,-1),Z(-18,1)]

def determinant_at(V):
    B=mm(mm(V,diag(b)),adj(V))
    X=[[add(diag(a)[i][j],B[i][j]) for j in range(4)] for i in range(4)]
    return det4(X)

def L(z): return -5782*z[0]+19099*z[1]
def vertex(p):
    out=Z(1)
    for i in range(4): out=mul(out,add(a[i],b[p[i]]))
    return out

def swap_rows(V,r,s):
    W=[row[:] for row in V]; W[r],W[s]=W[s],W[r]; return W

def swap_cols(V,r,s):
    W=[row[:] for row in V]
    for i in range(4): W[i][r],W[i][s]=W[i][s],W[i][r]
    return W

M=max(L(vertex(p)) for p in permutations(range(4)))
h=L(determinant_at(U))
gamma=h-M
pairs=list(combinations(range(4),2))
row={}; col={}
for pair in pairs:
    for store,hp in ((row,L(determinant_at(swap_rows(U,*pair)))),
                     (col,L(determinant_at(swap_cols(U,*pair))))):
        g=h-hp
        reserve=M-(h+hp)/2
        assert reserve>=0
        assert g==2*(gamma+reserve)
        store[pair]=(g,reserve)

G_row=sum(x[0] for x in row.values())
G_col=sum(x[0] for x in col.values())
assert G_row==G_col
comp={(0,1):(2,3),(0,2):(1,3),(0,3):(1,2)}
P_row=sum(row[p][0]*row[q][0] for p,q in comp.items())
P_col=sum(col[p][0]*col[q][0] for p,q in comp.items())

print('PASS exact pair-roof reserve regression')
print('M =',M)
print('h =',h)
print('gamma=h-M =',gamma)
print('common transposition deficit G =',G_row)
print('min row reserve =',min(x[1] for x in row.values()))
print('min column reserve =',min(x[1] for x in col.values()))
print('row complementary product sum =',P_row)
print('column complementary product sum =',P_col)
