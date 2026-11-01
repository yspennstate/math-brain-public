from fractions import Fraction as F
from itertools import permutations

Z=(F(0),F(0)); O=(F(1),F(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def scale(q,x): return (q*x[0],q*x[1])
def sumc(xs):
    r=Z
    for x in xs: r=add(r,x)
    return r
def prod(xs):
    r=O
    for x in xs: r=mul(r,x)
    return r
def adj(A): return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def mm(A,B):
    return [[sumc(mul(A[i][k],B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def eye(n): return [[O if i==j else Z for j in range(n)] for i in range(n)]
def det(A):
    n=len(A); ans=Z
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=prod(A[i][p[i]] for i in range(n))
        ans=add(ans,scale(F(-1 if inv%2 else 1),term))
    return ans
def C(re=0,im=0,den=1): return (F(re,den),F(im,den))
def fmt(z): return f"{z[0]} + ({z[1]})i"

U=[
[C(9248596,-2204309,9965689),C(-460963,1041129,9965689),C(-1388656,618674,9965689),C(131,-511,2281)],
[C(563773,1612493,9965689),C(8519772,-3082155,9965689),C(-394626,1491668,9965689),C(-563,-555,2281)],
[C(1113265,1577639,9965689),C(-685277,3478279,9965689),C(-766988,-597724,9965689),C(-1962,671,2281)],
[C(-384,-538,4369),C(114,-796,4369),C(-3443,-2480,4369),Z]
]
assert mm(U,adj(U))==eye(4)
assert U[3][3]==Z
assert all(U[i][j]!=Z for i in range(4) for j in range(4) if (i,j)!=(3,3))

a=[C(-12,13),C(1,-24),C(-22,12),C(1,-19)]
b=[C(7,11),C(-18,-5),C(-7,24),C(10,-13)]
B=mm([[mul(U[i][j],b[j]) for j in range(4)] for i in range(4)],adj(U))
D=det([[add(B[i][j],a[i] if i==j else Z) for j in range(4)] for i in range(4)])
assert D==(F(681177468907,9965689),F(-540878230401,9965689))

ps=list(permutations(range(4)))
V=[prod(add(a[i],b[p[i]]) for i in range(4)) for p in ps]
def L(z): return -F(158949)*z[0]-F(904287)*z[1]
vals=[L(v) for v in V]
M=max(vals); m=min(vals)
assert M==F(54642495840)
assert m==F(-1020841356720)
assert [ps[i] for i,x in enumerate(vals) if x==M]==[(0,3,1,2),(1,3,2,0)]
gap=M-L(D)
assert gap==F(163713444895903416,9965689)
norm=gap/(M-m)
assert norm==F(6821393537329309,446580733297283910)

# Exact Caratheodory rescue for the original dense zero-face candidate.
w0=F(409612355129822,34569108916249415)
w1=F(32512105995924378,34569108916249415)
w4=F(329478113039043,6913821783249883)
assert min(w0,w1,w4)>=0 and w0+w1+w4==1
Dc=add(add(scale(w0,V[0]),scale(w1,V[1])),scale(w4,V[4]))
assert Dc==D

# Apply a genuine rational left row-plane rotation, preserving U_44=0.
t=F(-1,1000)
c=(1-t*t)/(1+t*t); s=2*t/(1+t*t)
R=eye(4)
R[1][1]=(c,F(0)); R[2][2]=(c,F(0))
R[1][2]=(s,F(0)); R[2][1]=(-s,F(0))
U1=mm(R,U)
assert mm(U1,adj(U1))==eye(4) and U1[3][3]==Z
B1=mm([[mul(U1[i][j],b[j]) for j in range(4)] for i in range(4)],adj(U1))
D1=det([[add(B1[i][j],a[i] if i==j else Z) for j in range(4)] for i in range(4)])
improve=L(D1)-L(D)
assert improve==F(130344534495211750236720000,9965708931387965689)
assert improve>0
gap1=M-L(D1)
assert gap1==F(163583427788461709501491183416,9965708931387965689)
assert gap1>0
norm1=gap1/(M-m)
assert norm1==F(6815976157852571229228799309,446581626459197085301117283910)

# The improved candidate also has an exact 3-vertex hull certificate.
i,j,k=4,17,22
q0=F(9841626785216570230204205,13075879305406521841292301)
q1=F(260224163944627976615229199,1320663809846058705970522401)
q2=F(66435340594557136104668497,1320663809846058705970522401)
assert min(q0,q1,q2)>=0 and q0+q1+q2==1
assert add(add(scale(q0,V[i]),scale(q1,V[j])),scale(q2,V[k]))==D1

print("PASS exact zero-face true-unitary verification")
print("D =",fmt(D))
print("common support maximum M =",M)
print("maximizing permutations (1-based) = 1423, 2431")
print("original exact gap =",gap)
print("original normalized gap =",norm,"~",float(norm))
print("original Caratheodory vertices = 1234, 1243, 1423")
print("row-plane ascent t=-1/1000 exact support improvement =",improve)
print("improved exact gap =",gap1)
print("improved normalized gap =",norm1,"~",float(norm1))
print("improved Caratheodory vertices =", ''.join(str(x+1) for x in ps[i]), ''.join(str(x+1) for x in ps[j]), ''.join(str(x+1) for x in ps[k]))
