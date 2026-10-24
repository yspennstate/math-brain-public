from fractions import Fraction as F
from itertools import permutations, combinations

# Exact Gaussian rationals are pairs (real, imag) of Fractions.
def Z(r=0, i=0): return (F(r), F(i))
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def sub(x,y): return (x[0]-y[0], x[1]-y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0], -x[1])
def scale(x,q): return (x[0]*q, x[1]*q)
def sumz(xs):
    out=Z()
    for x in xs: out=add(out,x)
    return out

def mm(A,B):
    return [[sumz(mul(A[i][k],B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def adj(A): return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def diag(v): return [[v[i] if i==j else Z() for j in range(4)] for i in range(4)]

def sign(p):
    return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1

def det4(A):
    out=Z()
    for p in permutations(range(4)):
        t=Z(1)
        for i in range(4): t=mul(t,A[i][p[i]])
        out=add(out,scale(t,F(sign(p))))
    return out

# Dense complex rational Cayley unitary found from a skew-Hermitian Gaussian-integer generator.
# U = G/3562.  All entries and all 2x2 minors are nonzero.
G=[
 [(-2724,-1551),(234,247),(-1219,167),(1106,-96)],
 [(236,-101),(-2782,1417),(1,1607),(490,228)],
 [(1443,39),(845,793),(-2522,702),(234,-1534)],
 [(-820,200),(-416,1144),(-1060,-784),(-2910,536)]
]
U=[[scale(Z(r,i),F(1,3562)) for (r,i) in row] for row in G]
I=[[Z(1 if i==j else 0) for j in range(4)] for i in range(4)]
assert mm(U,adj(U))==I
assert all(x!=Z() for row in U for x in row)

# Every 2x2 minor is nonzero.
for rs in combinations(range(4),2):
    for cs in combinations(range(4),2):
        d=sub(mul(U[rs[0]][cs[0]],U[rs[1]][cs[1]]),
              mul(U[rs[0]][cs[1]],U[rs[1]][cs[0]]))
        assert d!=Z()

a=[Z(18,-17),Z(-20,2),Z(15,-22),Z(-21,2)]
b=[Z(-19,4),Z(25,-5),Z(18,-1),Z(-18,1)]
assert len(set(a))==4 and len(set(b))==4
assert all(add(x,y)!=Z() for x in a for y in b)

B=mm(mm(U,diag(b)),adj(U))
AplusB=[[add(diag(a)[i][j],B[i][j]) for j in range(4)] for i in range(4)]
D=det4(AplusB)
assert D==(F(278808875,3562),F(24903390,1781))

PERMS=list(permutations(range(4)))
def vertex(p):
    t=Z(1)
    for i in range(4): t=mul(t,add(a[i],b[p[i]]))
    return t
V=[vertex(p) for p in PERMS]
assert len(set(V))==24

# One exact common support direction for all 24 target vertices and D.
def L(w): return -5782*w[0] + 19099*w[1]
LV=[L(w) for w in V]
M=max(LV); m=min(LV); LD=L(D); gap=M-LD
assert M==F(-61633500)
assert m==F(-59822291610)
assert LD==F(-2411727095,13)
assert gap==F(1610491595,13)>0
maximizers=[PERMS[i] for i,x in enumerate(LV) if x==M]
assert maximizers==[(0,1,2,3),(0,2,3,1)]
normalized=gap/(M-m)
assert normalized==F(322098319,155377711086)

# Exact three-vertex Caratheodory rescue certificate.
den=F(406763017440)
lam0=F(73409846651,406763017440)
lam1=F(98803540981,406763017440)
lam5=F(234549629808,406763017440)
assert lam0>=0 and lam1>=0 and lam5>=0 and lam0+lam1+lam5==1
Dcert=add(add(scale(V[0],lam0),scale(V[1],lam1)),scale(V[5],lam5))
assert Dcert==D
assert V[0]==Z(115344,31692)
assert V[1]==Z(2400,-4500)
assert V[5]==Z(98632,16226)

print('PASS exact unitary/common-support/Caratheodory verification')
print('D =',D)
print('support M =',M,'L(D) =',LD,'gap =',gap)
print('normalized support gap =',normalized,'~',float(normalized))
print('support maximizers (zero-based) =',maximizers)
print('Caratheodory weights =',lam0,lam1,lam5)
