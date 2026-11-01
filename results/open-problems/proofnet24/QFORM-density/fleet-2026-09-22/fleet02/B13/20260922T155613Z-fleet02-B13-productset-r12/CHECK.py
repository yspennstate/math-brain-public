from fractions import Fraction as F
from math import sqrt, pi, sin, cos
from random import Random

def T(M):
    return [list(row) for row in zip(*M)]

def mm(A,B):
    BT=T(B)
    return [[sum(a*b for a,b in zip(row,col)) for col in BT] for row in A]

def mv(A,x):
    return [sum(a*b for a,b in zip(row,x)) for row in A]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

R4=[
    [F(1,2),F(1,2),F(1,2)],
    [F(1,2),F(-1,2),F(-1,2)],
    [F(-1,2),F(1,2),F(-1,2)],
    [F(-1,2),F(-1,2),F(1,2)],
]
Lam=[[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(-1)]]
I3=[[F(int(i==j)) for j in range(3)] for i in range(3)]
assert mm(T(R4),R4)==I3
A4=mm(mm(R4,Lam),T(R4))
expected=[
    [F(1,4),F(1,4),F(1,4),F(-3,4)],
    [F(1,4),F(1,4),F(-3,4),F(1,4)],
    [F(1,4),F(-3,4),F(1,4),F(1,4)],
    [F(-3,4),F(1,4),F(1,4),F(1,4)],
]
assert A4==expected
assert mm(A4,R4)==mm(R4,Lam)
assert [sum(row[j] for row in R4) for j in range(3)]==[F(0),F(0),F(0)]
wAw=(A4[0][0]+A4[1][1]+2*A4[0][1])/2
assert wAw==F(1,2)

L=11
lo=L*L/2-(2*L*sqrt(5)+5)
hi=L*L/2+(2*L*sqrt(5)+5)
assert lo>6 and hi<115
C3=2*pi+3*sqrt(3)
m5=20*C3

def eye(n):
    return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]

A0=[[0.0]*5 for _ in range(5)]
for i in range(4):
    for j in range(4):
        A0[i][j]=float(A4[i][j])
w=[1/sqrt(2),1/sqrt(2),0.0,0.0,0.0]
e5=[0.0,0.0,0.0,0.0,1.0]

def outer(x,y):
    return [[a*b for b in y] for a in x]

def Otheta(th):
    O=eye(5)
    c,s=cos(th),sin(th)
    ww=outer(w,w); ee=outer(e5,e5); ew=outer(e5,w); we=outer(w,e5)
    for i in range(5):
        for j in range(5):
            O[i][j]+=(c-1)*(ww[i][j]+ee[i][j])+s*(ew[i][j]-we[i][j])
    return O

def qform(A,x):
    return dot(x,mv(A,x))

rng=Random(20260922)
sample_ranges=[]
for th in (0.1,0.03,0.01):
    O=Otheta(th)
    Ath=mm(mm(O,A0),T(O))
    qs=[]
    for _ in range(2000):
        x=[rng.random() for _ in range(5)]
        x[4]+=L/sin(th)
        qs.append(qform(Ath,x))
    assert min(qs)>6 and max(qs)<115
    sample_ranges.append((th,min(qs),max(qs)))

print("QFORM_NO_OPNORM_SLAB_CONTINUITY_CHECK_PASS")
print("parseval_exact=True")
print("wAw_exact=1/2")
print(f"analytic_support_interval=[{lo:.12f},{hi:.12f}] subset (6,115)")
print(f"pigeonhole_unit_slab_mass>={1/109:.12f}")
print(f"m5_finite_direction_bound={m5:.12f}")
for th,a,b in sample_ranges:
    print(f"sample_theta={th:.2f} range=[{a:.9f},{b:.9f}]")
